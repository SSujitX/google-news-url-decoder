from .decoderv1 import decode_google_news_url as decoderv1
from .decoderv2 import decode_google_news_url as decoderv2
from .decoderv3 import decode_google_news_url as decoderv3
from .decoderv4 import decode_google_news_url as decoderv4
from .new_decoderv1 import decode_google_news_url as new_decoderv1
from .new_decoderv2 import GoogleDecoder
from .new_decoderv3 import GoogleDecoderAsync
from .__version__ import __version__


def gnewsdecoder(source_url, interval=None, proxy=None):
    """
    Decodes a Google News article URL into its original source URL.
    This is a convenience function that uses the GoogleDecoder class internally.

    Parameters:
        source_url (str): The Google News article URL.
        interval (int, optional): Delay time in seconds before decoding to avoid rate limits.
        proxy (str, optional): Proxy to be used for all requests.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    decoder = GoogleDecoder(proxy=proxy)
    return decoder.decode_google_news_url(source_url, interval=interval)

async def gnews_decoder_async(source_url, interval=None, proxy=None):
    """
    Decodes a Google News article URL into its original source URL Asynchronously.
    This is a convenience function that uses the GoogleDecoderAsync class internally using httpx library to do request asynchronously.
    Parameters:
        source_url (str): The Google News article URL.
        interval (int, optional): Delay time in seconds before decoding to avoid rate limits.
        proxy (str, optional): Proxy to be used for all requests.

    Returns:
        dict: A dictionary containing 'status' and 'decoded_url' if successful,
              otherwise 'status' and 'message'.
    """
    decoder = GoogleDecoderAsync(proxy=proxy)
    return await decoder.decode_google_news_url(source_url, interval=interval)


__all__ = [
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
