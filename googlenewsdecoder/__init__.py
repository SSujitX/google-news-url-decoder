from typing import Optional
from .decoderv1 import decode_google_news_url as decoderv1
from .decoderv2 import decode_google_news_url as decoderv2
from .decoderv3 import decode_google_news_url as decoderv3
from .decoderv4 import decode_google_news_url as decoderv4
from .new_decoderv1 import decode_google_news_url as new_decoderv1
from .new_decoderv2 import GoogleDecoder
from .new_decoderv3 import GoogleDecoderAsync
from .__version__ import __version__
from .constants import DEFAULT_TIMEOUT, DEFAULT_USER_AGENT


def gnewsdecoder(
    source_url: str,
    interval: Optional[int] = None,
    proxy: Optional[str] = None,
    timeout: Optional[float] = DEFAULT_TIMEOUT,
) -> dict:
    """
    Decodes a Google News article URL into its original source URL.
    This is a convenience function that uses the GoogleDecoder class internally.

    Parameters:
        source_url (str): The Google News article URL.
        interval (int, optional): Delay time in seconds before decoding to avoid rate limits.
        proxy (str, optional): Proxy to be used for all requests.
        timeout (float, optional): Seconds any single request may take before it is
                                   abandoned. None waits indefinitely.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    decoder = GoogleDecoder(proxy=proxy, timeout=timeout)
    return decoder.decode_google_news_url(source_url, interval=interval)

async def gnews_decoder_async(
    source_url: str,
    interval: Optional[int] = None,
    proxy: Optional[str] = None,
    timeout: Optional[float] = DEFAULT_TIMEOUT,
) -> dict:
    """
    Decodes a Google News article URL into its original source URL Asynchronously.
    This is a convenience function that uses the GoogleDecoderAsync class internally using httpx library to do request asynchronously.
    Parameters:
        source_url (str): The Google News article URL.
        interval (int, optional): Delay time in seconds before decoding to avoid rate limits.
        proxy (str, optional): Proxy to be used for all requests.
        timeout (float, optional): Seconds any single request may take before it is
                                   abandoned. None waits indefinitely.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    decoder = GoogleDecoderAsync(proxy=proxy, timeout=timeout)
    try:
        return await decoder.decode_google_news_url(source_url, interval=interval)
    finally:
        await decoder.close()


__all__ = [
    "DEFAULT_TIMEOUT",
    "DEFAULT_USER_AGENT",
    "decoderv1",
    "decoderv2",
    "decoderv3",
    "decoderv4",
    "new_decoderv1",
    "GoogleDecoder",
    "GoogleDecoderAsync",
    "gnewsdecoder",
    "gnews_decoder_async",
]
