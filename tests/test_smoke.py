import googlenewsdecoder as pkg
from googlenewsdecoder import (
    GoogleDecoder,
    GoogleDecoderAsync,
    gnews_decoder_async,
    gnewsdecoder,
)


def test_version_present():
    assert pkg.__version__


def test_invalid_url_is_local():
    assert gnewsdecoder("https://example.com/x")["success"] is False
    assert gnewsdecoder(["https://example.com/x"])[0]["success"] is False


def test_public_api():
    assert callable(gnewsdecoder)
    assert callable(gnews_decoder_async)
    assert GoogleDecoder is not None
    assert GoogleDecoderAsync is not None
