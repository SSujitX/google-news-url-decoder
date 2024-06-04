# Google News URL Decoder

This Python script decodes Google News article URLs. 

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/google-news-url-decoder.git
    cd google-news-url-decoder
    ```

2. Run the script:
    ```sh
    python decode_google_news_url.py
    ```

## Example

You can decode a Google News article URL using the `decode_google_news_url` function:

```python
import base64
from urllib.parse import urlparse

def decode_google_news_url(source_url):
    url = urlparse(source_url)
    path = url.path.split('/')
    if (
        url.hostname == "news.google.com" and
        len(path) > 1 and
        path[-2] == "articles"
    ):
        base64_str = path[-1]
        decoded_bytes = base64.urlsafe_b64decode(base64_str + '==')
        decoded_str = decoded_bytes.decode('latin1')

        prefix = bytes([0x08, 0x13, 0x22]).decode('latin1')
        if decoded_str.startswith(prefix):
            decoded_str = decoded_str[len(prefix):]

        suffix = bytes([0xd2, 0x01, 0x00]).decode('latin1')
        if decoded_str.endswith(suffix):
            decoded_str = decoded_str[:-len(suffix)]

        bytes_array = bytearray(decoded_str, 'latin1')
        length = bytes_array[0]
        if length >= 0x80:
            decoded_str = decoded_str[2:length+1]
        else:
            decoded_str = decoded_str[1:length+1]

        return decoded_str
    else:
        return source_url

# Example usage:
if __name__ == "__main__":
    source_url = 'https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5'
    print(decode_google_news_url(source_url))
