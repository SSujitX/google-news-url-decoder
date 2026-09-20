import json
import re
from urllib.parse import parse_qs, quote, urljoin, urlparse

from selectolax.parser import HTMLParser

_SG = re.compile(r'data-n-a-sg="([^"]+)"')
_TS = re.compile(r'data-n-a-ts="([^"]+)"')

BATCHEXECUTE_URL = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
RSS_ARTICLE_URL = "https://news.google.com/rss/articles/{id}"

_GARTURLREQ_CTX = [
    ["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None, None, None, None, 0, 1],
    "X",
    "X",
    1,
    [1, 1, 1],
    1,
    1,
    None,
    0,
    0,
    None,
    0,
]


def article_id(source_url: str) -> str | None:
    """Return the article id from a Google News URL, or None if the URL is invalid.

    Parameters:
        source_url: A ``/read/``, ``/articles/``, or ``/rss/articles/`` URL.
    """
    try:
        url = urlparse(source_url)
        path = url.path.split("/")
        if (
            url.hostname == "news.google.com"
            and len(path) > 1
            and path[-2] in ("articles", "read")
        ):
            return path[-1] or None
    except Exception:
        return None
    return None


def params_page_url(art_id: str, source_url: str | None = None) -> str:
    """Article-page URL that actually returns ``data-n-a-sg``.

    ``/articles/{id}`` and ``/read/{id}`` 302 to ``google.com/sorry`` from
    non-browser clients. ``/rss/articles/{id}?hl=&gl=&ceid=`` returns 200.
    Locale is copied from ``source_url`` when present.
    """
    hl, gl, ceid = "en-US", "US", "US:en"
    if source_url:
        qs = parse_qs(urlparse(source_url).query)
        if qs.get("hl"):
            hl = qs["hl"][0]
        if qs.get("gl"):
            gl = qs["gl"][0]
        if qs.get("ceid"):
            ceid = qs["ceid"][0]
    return (
        f"{RSS_ARTICLE_URL.format(id=art_id)}"
        f"?hl={quote(hl, safe='')}&gl={quote(gl, safe='')}&ceid={quote(ceid, safe='')}"
    )


def next_google_hop(current: str, location: str | None) -> str | None:
    """Return the next URL if Location stays on news.google.com."""
    if not location:
        return None
    dest = urljoin(current, location)
    if urlparse(dest).hostname == "news.google.com":
        return dest
    return None


def parse_signature(html: str) -> tuple[str, str] | None:
    """Read ``data-n-a-sg`` and ``data-n-a-ts`` from an article page.

    Parameters:
        html: Raw HTML from ``/articles/{id}`` or ``/rss/articles/{id}``.

    Returns:
        ``(signature, timestamp)`` or None if those attributes are missing.
    """
    node = HTMLParser(html).css_first("c-wiz > div[jscontroller]")
    if node is not None:
        sg = node.attributes.get("data-n-a-sg")
        ts = node.attributes.get("data-n-a-ts")
        if sg and ts:
            return sg, ts
    sg_m = _SG.search(html)
    ts_m = _TS.search(html)
    if sg_m and ts_m:
        return sg_m.group(1), ts_m.group(1)
    return None


def build_batchexecute_body(items: list[tuple[str, str, str, str]]) -> str:
    """Build the ``f.req=...`` body for one batchexecute POST.

    Parameters:
        items: ``(request_id, article_id, timestamp, signature)`` tuples.
            ``request_id`` is the caller's list index so the response can be
            matched if Google omits or reorders a row.
    """
    envelopes = []
    for req_id, art_id, ts, sig in items:
        inner = [
            "garturlreq",
            _GARTURLREQ_CTX,
            art_id,
            int(ts) if str(ts).isdigit() else ts,
            sig,
        ]
        envelopes.append(
            ["Fbv4je", json.dumps(inner, separators=(",", ":")), None, str(req_id)]
        )
    return f"f.req={quote(json.dumps([envelopes], separators=(',', ':')))}"


def parse_batchexecute(text: str) -> list[tuple[str | None, str]]:
    """Pull ``(request_id, url)`` pairs out of a batchexecute response.

    Parameters:
        text: Raw response body from the batchexecute POST.
    """
    body = text
    if "\n\n" in body:
        body = body.split("\n\n", 1)[1]
    body = body.lstrip()
    if body.startswith(")]}'"):
        body = body.split("\n", 1)[1] if "\n" in body else body[4:]
        body = body.lstrip()
    rows = json.loads(body)
    if rows and rows[-1] and isinstance(rows[-1], list) and rows[-1][0] == "di":
        rows = rows[:-1]
    if rows and isinstance(rows[-1], list) and rows[-1] and rows[-1][0] == "e":
        rows = rows[:-1]

    pairs: list[tuple[str | None, str]] = []
    for row in rows:
        if not (isinstance(row, list) and len(row) >= 3):
            continue
        payload = row[2]
        if row[0] == "wrb.fr" or row[1] == "Fbv4je":
            if isinstance(payload, str):
                payload = json.loads(payload)
            if isinstance(payload, list) and payload and payload[0] == "garturlres":
                req_id = None
                for cell in reversed(row[3:]):
                    if cell is not None:
                        req_id = str(cell)
                        break
                pairs.append((req_id, payload[1]))
    return pairs


def apply_decoded(
    results: list[dict],
    pending: list[tuple[int, str, str, str]],
    pairs: list[tuple[str | None, str]],
) -> list[dict]:
    """Write decoded URLs onto ``results`` by request id, or by order if ids are missing."""
    by_id = {req_id: url for req_id, url in pairs if req_id is not None}
    ordered = [url for _, url in pairs]
    for offset, (i, *_) in enumerate(pending):
        url = by_id.get(str(i))
        if url is None and not by_id and offset < len(ordered):
            url = ordered[offset]
        if url:
            results[i] = ok(decoded_url=url)
        else:
            results[i] = err("No decoded URL in batchexecute response.")
    return results


def ok(**fields) -> dict:
    return {"success": True, **fields}


def err(message: str) -> dict:
    return {"success": False, "message": message}
