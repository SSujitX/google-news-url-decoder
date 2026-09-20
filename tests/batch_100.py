import asyncio
import re
from rich import print
import httpx

from googlenewsdecoder import gnews_decoder_async


def get_rss_urls(limit=100):
    feeds = [
        "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/headlines/section/topic/NATION?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/rss/headlines/section/topic/SCIENCE?hl=en-US&gl=US&ceid=US:en",
    ]
    urls = []
    for feed in feeds:
        page = httpx.get(feed, follow_redirects=True, timeout=15.0).text
        for url in re.findall(
            r"https://news\.google\.com/rss/articles/[A-Za-z0-9_\-]+", page
        ):
            if url not in urls:
                urls.append(url)
        if len(urls) >= limit:
            break
    return urls[:limit]


def get_read_urls(limit=100):
    pages = [
        "https://news.google.com/?hl=en-US&gl=US&ceid=US:en",
        "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en",
    ]
    urls = []
    for page_url in pages:
        page = httpx.get(page_url, follow_redirects=True, timeout=15.0).text
        for url in re.findall(
            r"(?:https://news\.google\.com/|\./)read/[A-Za-z0-9_\-]+", page
        ):
            if url.startswith("./"):
                url = "https://news.google.com/" + url[2:]
            if url not in urls:
                urls.append(url)
        if len(urls) >= limit:
            break
    return urls[:limit]


def main():
    interval_time = 1  # interval is optional, default is None
    source_urls = get_rss_urls(50) + get_read_urls(50)
    print(f"Total URLs: {len(source_urls)}")
    
    try:
        results = asyncio.run(
            gnews_decoder_async(source_urls, interval=interval_time)
        )
        for result in results:
            print(f"Success: {result['success']}")
            if result["success"]:
                print("Decoded URL:", result["decoded_url"])
            else:
                print("Error:", result["message"])
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
