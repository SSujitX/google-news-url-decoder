# Google News Decoder

A Python package to decode Google News URLs.

## Update

- Version 0.1.2:

  - This update enhances error handling by returning a dictionary containing `status=False` and an appropriate error message when decoding fails.
  - It ensures more robust and clear responses when processing URLs, improving the package's usability and debugging capabilities.
  - decoderv3 is introduced in this version, which handles both `/rss/articles` and `/read` URLs, with comprehensive error reporting.

- Version 0.1.1:
  - This update ensures that the package can now decode URLs that contain `/read` in addition to the previously supported `/rss/articles` format.
  - The functionality was primarily available in **`decoderv2`**.

## Demo

![news](https://github.com/user-attachments/assets/96af4ef4-57a0-4be7-a4ef-f1acd10d0c84)


## Installation

You can install this package using pip:

```sh
pip install googlenewsdecoder
```

## Credits

Original script by [huksley](https://gist.github.com/huksley/)

## Usage

Here is an example of how to use this package:

```python

from googlenewsdecoder import decoderv1, decoderv2

if __name__ == "__main__":

    # source_url = "https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5"
    # source_url = "https://news.google.com/rss/articles/CBMiVkFVX3lxTE4zaGU2bTY2ZGkzdTRkSkJ0cFpsTGlDUjkxU2FBRURaTWU0c3QzVWZ1MHZZNkZ5Vzk1ZVBnTDFHY2R6ZmdCUkpUTUJsS1pqQTlCRzlzbHV3?oc=5"
    # source_url = "https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMTRqdUZpNl9hQldXbGo2YVVLOGFQdkFLYldlMUxUVlNEaElsYjRRODVUMkF3R1RYdWxvT1NoVzdUYS0xSHg3eVdpTjdVODQ5cVJJLWt4dk9vZFBScVp2ZmpzQXZZRy1ncDM5c2tRbXBVVHVrQnpmMGVrQXNkQVItV3h4dVQ1V1BTbjhnM3k2ZUdPdnhVOFk1NmllNTZkdGJTbW9NX0k5U3E2Tkk?oc=5"

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    decoded_url = decoderv2(source_url)

    print(decoded_url)
```
