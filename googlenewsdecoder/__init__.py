from importlib.metadata import version

from .decoder import GoogleDecoder
from .decoder_async import GoogleDecoderAsync

__version__ = version("googlenewsdecoder")


def gnewsdecoder(
    source_url: str | list[str],
    interval: int | None = None,
    proxy: str | None = None,
    timeout: float | None = 10.0,
) -> dict | list[dict]:
    """Decode one Google News URL, or a list of them, to the original article URL.

    A string returns one dict. A list uses one batchexecute POST and returns a
    list of dicts. Each item is ``{"success": True, "decoded_url": "..."}`` or
    ``{"success": False, "message": "..."}``.

    Parameters:
        source_url: One Google News URL or a list of them
            (``/read/``, ``/articles/``, or ``/rss/articles/``).
        interval: Seconds to wait after each article-page fetch. None means no wait.
        proxy: Optional HTTP/HTTPS/SOCKS5 proxy URL.
            Examples: ``http://user:pass@host:port``, ``socks5://host:port``.
        timeout: Seconds per HTTP operation. None waits indefinitely.

    Returns:
        One result dict, or a list of result dicts when ``source_url`` is a list.
    """
    with GoogleDecoder(proxy=proxy, timeout=timeout) as decoder:
        if isinstance(source_url, str):
            return decoder.decode_google_news_url(source_url, interval=interval)
        return decoder.decode_google_news_urls(source_url, interval=interval)


async def gnews_decoder_async(
    source_url: str | list[str],
    interval: int | None = None,
    proxy: str | None = None,
    timeout: float | None = 10.0,
    concurrency: int = 8,
) -> dict | list[dict]:
    """Async version of ``gnewsdecoder``. Same return shape.

    Parameters:
        source_url: One Google News URL or a list of them.
        interval: Seconds to wait after each article-page fetch. None means no wait.
        proxy: Optional HTTP/HTTPS/SOCKS5 proxy URL.
            Examples: ``http://user:pass@host:port``, ``socks5://host:port``.
        timeout: Seconds per HTTP operation. None waits indefinitely.
        concurrency: Max parallel article-page fetches when ``source_url`` is a list.

    Returns:
        One result dict, or a list of result dicts when ``source_url`` is a list.
    """
    async with GoogleDecoderAsync(proxy=proxy, timeout=timeout) as decoder:
        if isinstance(source_url, str):
            return await decoder.decode_google_news_url(source_url, interval=interval)
        return await decoder.decode_google_news_urls(
            source_url, interval=interval, concurrency=concurrency
        )


__all__ = [
    "GoogleDecoder",
    "GoogleDecoderAsync",
    "gnews_decoder_async",
    "gnewsdecoder",
]
