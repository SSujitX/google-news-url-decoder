# Google News Decoder

A Python package to decode Google News URLs.

## Installation

You can install this package using pip:

## Usage

Here is an example of how to use this package:

pip install googlenewsdecoder

```bash

from googlenewsdecoder import decoderv1, decoderv2

if __name__ == "__main__":
    # source_url = "https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5"
    # source_url = "https://news.google.com/rss/articles/CBMiVkFVX3lxTE4zaGU2bTY2ZGkzdTRkSkJ0cFpsTGlDUjkxU2FBRURaTWU0c3QzVWZ1MHZZNkZ5Vzk1ZVBnTDFHY2R6ZmdCUkpUTUJsS1pqQTlCRzlzbHV3?oc=5"
    source_url = "https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMTRqdUZpNl9hQldXbGo2YVVLOGFQdkFLYldlMUxUVlNEaElsYjRRODVUMkF3R1RYdWxvT1NoVzdUYS0xSHg3eVdpTjdVODQ5cVJJLWt4dk9vZFBScVp2ZmpzQXZZRy1ncDM5c2tRbXBVVHVrQnpmMGVrQXNkQVItV3h4dVQ1V1BTbjhnM3k2ZUdPdnhVOFk1NmllNTZkdGJTbW9NX0k5U3E2Tkk?oc=5"
    # Decode the URL using decoderv1
    decoded_url_v1 = decoderv1(source_url)
    print(decoded_url_v1)
    
    # Decode the URL using decoderv2
    decoded_url_v2 = decoderv2(source_url)
    print(decoded_url_v2)
    print(decoded_url)
