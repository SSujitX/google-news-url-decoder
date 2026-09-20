from __future__ import annotations

import asyncio
import json

import httpx

from ._parse import (
    BATCHEXECUTE_URL,
    apply_decoded,
    article_id,
    build_batchexecute_body,
    err,
    next_google_hop,
    ok,
    params_page_url,
    parse_batchexecute,
    parse_signature,
)


class GoogleDecoderAsync:
    """Async decoder. Use ``async with`` so the HTTP client is closed.

    Parameters:
        proxy: Optional HTTP/HTTPS/SOCKS5 proxy URL.
            Examples: ``http://user:pass@host:port``, ``socks5://host:port``.
        timeout: Seconds per HTTP operation. None waits indefinitely.
        user_agent: Optional User-Agent. None uses httpx's default.
    """

    def __init__(
        self,
        proxy: str | None = None,
        timeout: float | None = 10.0,
        user_agent: str | None = None,
    ):
        headers = {"User-Agent": user_agent} if user_agent else None
        self.client = httpx.AsyncClient(
            proxy=proxy,
            follow_redirects=True,
            timeout=timeout,
            http2=True,
            headers=headers,
        )

    async def __aenter__(self) -> GoogleDecoderAsync:
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self.client.aclose()

    async def get_decoding_params(self, art_id: str, source_url: str | None = None) -> dict:
        """Fetch signature and timestamp for one article id.

        Uses ``/rss/articles/{id}?hl=&gl=&ceid=``. ``/articles/`` and ``/read/``
        302 to a sorry page from non-browser clients.

        Parameters:
            art_id: The Google News article id (path after ``read`` or ``articles``).
            source_url: Original URL, used only to copy ``hl`` / ``gl`` / ``ceid``.

        Returns:
            ``{"success": True, "signature", "timestamp", "base64_str"}`` or
            ``{"success": False, "message"}``.
        """
        current = params_page_url(art_id, source_url)
        try:
            response = None
            for _ in range(3):
                response = await self.client.get(current, follow_redirects=False)
                if not response.is_redirect:
                    break
                nxt = next_google_hop(current, response.headers.get("location"))
                if nxt is None:
                    return err("Failed to fetch data attributes from Google News.")
                current = nxt
            if response is None or not response.is_success:
                return err("Failed to fetch data attributes from Google News.")
        except httpx.HTTPError as exc:
            return err(f"Request error fetching params: {exc}")
        parsed = parse_signature(response.text)
        if parsed:
            signature, timestamp = parsed
            return ok(signature=signature, timestamp=timestamp, base64_str=art_id)
        return err("Failed to fetch data attributes from Google News.")

    async def _batchexecute(self, items: list[tuple[str, str, str]]) -> dict:
        """POST one or many ids to batchexecute. items are (id, timestamp, signature)."""
        try:
            response = await self.client.post(
                BATCHEXECUTE_URL,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
                },
                content=build_batchexecute_body(items),
            )
            response.raise_for_status()
            pairs = parse_batchexecute(response.text)
            if not pairs:
                return err("No decoded URL in batchexecute response.")
            return ok(pairs=pairs)
        except httpx.HTTPError as exc:
            return err(f"Request error in decode: {exc}")
        except (json.JSONDecodeError, IndexError, TypeError, KeyError, ValueError) as exc:
            return err(f"Parsing error in decode: {exc}")

    async def decode_google_news_url(
        self, source_url: str, interval: int | None = None
    ) -> dict:
        """Decode one Google News URL.

        Parameters:
            source_url: A ``/read/``, ``/articles/``, or ``/rss/articles/`` URL.
            interval: Seconds to wait after the article-page fetch. None means no wait.

        Returns:
            ``{"success": True, "decoded_url"}`` or ``{"success": False, "message"}``.
        """
        results = await self.decode_google_news_urls(
            [source_url], interval=interval, concurrency=1
        )
        return results[0]

    async def decode_google_news_urls(
        self,
        source_urls: list[str],
        interval: int | None = None,
        concurrency: int = 8,
    ) -> list[dict]:
        """Decode many URLs. Article pages are fetched in parallel, then one POST.

        Parameters:
            source_urls: Google News URLs.
            interval: Seconds to wait after each article-page fetch. None means no wait.
            concurrency: Max parallel article-page fetches.

        Returns:
            One result dict per input URL, in the same order.
        """
        results: list[dict] = [err("pending") for _ in source_urls]
        pending: list[tuple[int, str, str, str]] = []
        sem = asyncio.Semaphore(max(1, concurrency))

        async def fetch_one(i: int, source_url: str) -> None:
            art_id = article_id(source_url)
            if not art_id:
                results[i] = err("Invalid Google News URL format.")
                return
            async with sem:
                params = await self.get_decoding_params(art_id, source_url)
            if interval:
                await asyncio.sleep(interval)
            if not params["success"]:
                results[i] = params
                return
            pending.append(
                (i, params["base64_str"], params["timestamp"], params["signature"])
            )

        await asyncio.gather(
            *(fetch_one(i, url) for i, url in enumerate(source_urls))
        )
        pending.sort(key=lambda item: item[0])

        if not pending:
            return results

        decoded = await self._batchexecute(
            [(str(p[0]), p[1], p[2], p[3]) for p in pending]
        )
        if not decoded["success"]:
            for i, *_ in pending:
                results[i] = err(decoded["message"])
            return results
        return apply_decoded(results, pending, decoded["pairs"])
