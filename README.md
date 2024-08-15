# Google News Decoder

A Python package to decode Google News URLs.

## Installation

You can install this package using pip:

```bash
pip install googlenewsdecoder


```

Usage
Here is an example of how to use this package:

python
Copy code
from googlenewsdecoder import decoderv1, decoderv2

# Example Google News URL

source_url = 'https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5'

# Decode the URL using decoderv1

decoded_url_v1 = decoderv1(source_url)
print(decoded_url_v1)

# Decode the URL using decoderv2

decoded_url_v2 = decoderv2(source_url)
print(decoded_url_v2)
