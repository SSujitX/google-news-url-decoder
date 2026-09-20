<p align="center">
  <a href="https://badge.fury.io/py/googlenewsdecoder"><img src="https://badge.fury.io/py/googlenewsdecoder.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/googlenewsdecoder/"><img src="https://img.shields.io/badge/python-%3E%3D3.11-blue" alt="Python >=3.11"></a>
  <a href="https://pepy.tech/project/googlenewsdecoder"><img src="https://static.pepy.tech/badge/googlenewsdecoder" alt="Downloads"></a>
  <a href="https://pepy.tech/project/googlenewsdecoder"><img src="https://static.pepy.tech/badge/googlenewsdecoder/week" alt="Downloads this week"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/SSujitX/google-news-url-decoder/main/assets/google_image_decoder.jpg" alt="Google News URL Decoder">
</p>

# Google News Decoder

Google News Decoder is a Python package that can decode Google News links or Google News URLs to their original URLs. It is a simple tool that saves you time and effort. If you find it useful, please support the package by hitting the star on GitHub. Your support helps keep the project going!

Use **googlenewsdecoder** to decode a Google News URL, extract the original article URL from `news.google.com/read/`, `/articles/`, or Google News RSS `/rss/articles/` feeds, and resolve the Google News redirect to the publisher source. Works with `pip install googlenewsdecoder` or `uv add googlenewsdecoder` on Python 3.11+.

<details>
<summary><strong>Looking for a sponsor</strong></summary>

<a href="mailto:ssujitxx@gmail.com">ssujitxx@gmail.com</a>
</details>

## Demo

![Decode a Google News URL to the original article URL](https://raw.githubusercontent.com/SSujitX/google-news-url-decoder/main/assets/google-news-url-decoder.gif)

## How it works

Google News wraps every story in an encoded link. After 2024 that id is opaque — it is not a base64 publisher URL.

This package fetches the per-article signature from Google News, then resolves the original URL with one `batchexecute` POST. Pass a **list** and those signatures share that single POST (no for-loop of POSTs).

Accepted input:

- `https://news.google.com/read/...`
- `https://news.google.com/articles/...`
- `https://news.google.com/rss/articles/...`

Each result is `{"success": True, "decoded_url": "..."}` or `{"success": False, "message": "..."}`.

## Installation

```sh
uv add googlenewsdecoder
```

```sh
pip install googlenewsdecoder
```

```sh
pip install googlenewsdecoder --upgrade
```


This repo uses [uv](https://docs.astral.sh/uv/):

```sh
uv sync --group dev
```

## Parameters

| Parameter | Default | What it is |
|---|---|---|
| `source_url` | required | One Google News URL, or a list of them. |
| `interval` | `None` | Seconds to wait after each article-page fetch. Use on large batches if you hit HTTP 429. |
| `proxy` | `None` | Optional HTTP/HTTPS/SOCKS5 proxy if this IP is rate-limited. |
| `timeout` | `10.0` | Seconds per HTTP call. `None` waits indefinitely. |
| `concurrency` | `8` | **Async list only.** Max parallel article-page fetches. |

`proxy` stays `None` unless you need one. Examples:

```text
http://user:pass@host:port
https://host:port
socks5://user:pass@host:port
```

## Usage

### Sync — `gnewsdecoder`

```python
from googlenewsdecoder import gnewsdecoder


def main():
    interval_time = 1  # optional; None means no wait
    timeout = 15.0
    # Optional. Examples:
    #   proxy = "http://user:pass@host:port"
    #   proxy = "https://host:port"
    #   proxy = "socks5://user:pass@host:port"
    proxy = None

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    try:
        result = gnewsdecoder(
            source_url,
            interval=interval_time,
            proxy=proxy,
            timeout=timeout,
        )
        if result["success"]:
            print("Decoded URL:", result["decoded_url"])
        else:
            print("Error:", result["message"])
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Async — `gnews_decoder_async`

```python
import asyncio

from googlenewsdecoder import gnews_decoder_async


def main():
    interval_time = 1  # optional; None means no wait
    timeout = 15.0
    # Optional. Examples:
    #   proxy = "http://user:pass@host:port"
    #   proxy = "https://host:port"
    #   proxy = "socks5://user:pass@host:port"
    proxy = None

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    try:
        result = asyncio.run(
            gnews_decoder_async(
                source_url,
                interval=interval_time,
                proxy=proxy,
                timeout=timeout,
            )
        )
        if result["success"]:
            print("Decoded URL:", result["decoded_url"])
        else:
            print("Error:", result["message"])
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Async batch

Pass a list. Article pages can run in parallel; decode is still one POST.

```python
import asyncio

from googlenewsdecoder import gnews_decoder_async


def main():
    interval_time = 1  # optional; None means no wait
    timeout = 15.0
    # Optional. Examples:
    #   proxy = "http://user:pass@host:port"
    #   proxy = "https://host:port"
    #   proxy = "socks5://user:pass@host:port"
    proxy = None

    source_urls = [
        "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen",
        "https://news.google.com/rss/articles/CBMiiAFBVV95cUxQOXZLdC1hSzFqQVVLWGJVZzlPaDYyNjdWTURScV9BbVp0SWhFNzZpSWZxSzdhc0tKbVlHMU13NmZVOFdidFFkajZPTm9SRnlZMWFRZ01CVHh0dXU0TjNVMUxZNk9Ibk5DV3hrYlRiZ20zYkIzSFhMQVVpcTFPc00xQjhhcGV1aXM?hl=en-US&gl=US&ceid=US%3Aen",
    ]

    try:
        results = asyncio.run(
            gnews_decoder_async(
                source_urls,
                interval=interval_time,
                proxy=proxy,
                timeout=timeout,
            )
        )
        for result in results:
            if result["success"]:
                print("Decoded URL:", result["decoded_url"])
            else:
                print("Error:", result["message"])
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```

`gnewsdecoder(source_urls)` also accepts a list (sync fetch, one POST). For many URLs, async batch is the better call.

## Credits

- Original script by [huksley](https://gist.github.com/huksley/)

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=SSujitX/google-news-url-decoder&type=date&legend=top-left&sealed_token=klBsl0qWHyFzyLVTz2my834KZ0EyA_IpgZBtTGoLPBVom69GLKRrRBMJVQ19wtHUjElTizag2kr3Bl0_BhyVeuGHJtunfu-12ftkOVPzK4--86MLY7OaG09Mws3HPqunNwwdrfbq6-4RFCkpTn2YCPLrwGNoBAaGdKWuGjM7Y2e2y3po1FucXQ2J9qDF)](https://www.star-history.com/?repos=SSujitX%2Fgoogle-news-url-decoder&type=date&legend=top-left)

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FSSujitX%2Fgoogle-news-url-decoder&countColor=%23263759&labelStyle=upper)
