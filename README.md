[![PyPI version](https://badge.fury.io/py/googlenewsdecoder.svg)](https://badge.fury.io/py/googlenewsdecoder)
[![Python Versions](https://img.shields.io/badge/python-3.9-blue)](https://pypi.org/project/facebook-pages-scraper/)
[![Downloads](https://static.pepy.tech/badge/googlenewsdecoder)](https://pepy.tech/project/googlenewsdecoder)
[![Downloads](https://static.pepy.tech/badge/googlenewsdecoder/month)](https://pepy.tech/project/googlenewsdecoder)
[![Downloads](https://static.pepy.tech/badge/googlenewsdecoder/week)](https://pepy.tech/project/googlenewsdecoder)

# Google News Decoder

Google News Decoder is a Python package that can decode Google News links or Google News URLs to their original URLs. It is a simple tool that saves you time and effort. If you find it useful, please support the package by hitting the star on GitHub. Your support helps keep the project going!

[Pypi Package](https://pypi.org/project/googlenewsdecoder/)

## Update

- Version 0.1.6:

  - Improved: Enhanced error handling with a fallback mechanism for decoding parameters.
  - Refined: Optimized get_decoding_params to try decoding via https://news.google.com/articles first, falling back to https://news.google.com/rss/articles if needed
  - Updated: Reduced occurrences of HTTP 429 (Too Many Requests).
  - Removed: Logging functionality for a cleaner codebase.
  - Fixed: Resolved time delay issue between requests.

## Demo

![Google News Decoder](https://github.com/user-attachments/assets/3a3c3279-1c54-4e19-96cb-6f22f889aa2a)

## Installation

- You can install this package using pip:

```sh
pip install googlenewsdecoder
```

- You can upgrade this package using pip (upgrade to latest version):

```sh
pip install googlenewsdecoder --upgrade
```

## Usage

Here is an example of how to use this package with different decoders:

### Using new_decoderv1

```python
from googlenewsdecoder import new_decoderv1

def main():

    interval_time = 5 # default interval is 1 sec, if not specified

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    try:
        decoded_url = new_decoderv1(source_url, interval=interval_time)
        if decoded_url.get("status"):
            print("Decoded URL:", decoded_url["decoded_url"])
        else:
            print("Error:", decoded_url["message"])
    except Exception as e:
        print(f"Error occurred: {e}")

    # Output: decoded_urls - [{'status': True, 'decoded_url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}]

if __name__ == "__main__":
    main()
```

### Using a for loop to decode multiple URLs

```python
from googlenewsdecoder import new_decoderv1

def main():

    interval_time = 5 # default interval is None, if not specified

    source_urls = ["https://news.google.com/read/CBMilgFBVV95cUxOM0JJaFRwV2dqRDk5dEFpWmF1cC1IVml5WmVtbHZBRXBjZHBfaUsyalRpa1I3a2lKM1ZnZUI4MHhPU2sydi1nX3JrYU0xWjhLaHNfU0N6cEhOYVE2TEptRnRoZGVTU3kzZGJNQzc2aDZqYjJOR0xleTdsemdRVnJGLTVYTEhzWGw4Z19lR3AwR0F1bXlyZ0HSAYwBQVVfeXFMTXlLRDRJUFN5WHg3ZTI0X1F4SjN6bmFIck1IaGxFVVZyOFQxdk1JT3JUbl91SEhsU0NpQzkzRFdHSEtjVGhJNzY4ZTl6eXhESUQ3XzdWVTBGOGgwSmlXaVRmU3BsQlhPVjV4VWxET3FQVzJNbm5CUDlUOHJUTExaME5YbjZCX1NqOU9Ta3U?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/read/CBMiiAFBVV95cUxQOXZLdC1hSzFqQVVLWGJVZzlPaDYyNjdWTURScV9BbVp0SWhFNzZpSWZxSzdhc0tKbVlHMU13NmZVOFdidFFkajZPTm9SRnlZMWFRZ01CVHh0dXU0TjNVMUxZNk9Ibk5DV3hrYlRiZ20zYkIzSFhMQVVpcTFPc00xQjhhcGV1aXM00gF_QVVfeXFMTmtFQXMwMlY1el9WY0VRWEh5YkxXbHF0SjFLQVByNk1xS3hpdnBuUDVxOGZCQXl1QVFXaUVpbk5lUGgwRVVVT25tZlVUVWZqQzc4cm5MSVlfYmVlclFTOUFmTHF4eTlfemhTa2JKeG14bmNabENkSmZaeHB4WnZ5dw?hl=en-US&gl=US&ceid=US%3Aen"]

    for url in source_urls:
        try:
            decoded_url = new_decoderv1(url, interval=interval_time)
            if decoded_url.get("status"):
                print("Decoded URL:", decoded_url["decoded_url"])
            else:
                print("Error:", decoded_url["message"])
        except Exception as e:
            print(f"Error occurred: {e}")

    # Output: decoded_url - {'status': True, 'decoded_url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}


if __name__ == "__main__":
    main()
```



### Using a proxy to deal with rate limiting

```python
from googlenewsdecoder import new_decoderv1

def main():

    interval_time = 5 # default interval is 1 sec, if not specified

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    try:
        decoded_url = new_decoderv1(source_url, proxy="http://user:pass@localhost:8080")
        if decoded_url.get("status"):
            print("Decoded URL:", decoded_url["decoded_url"])
        else:
            print("Error:", decoded_url["message"])
    except Exception as e:
        print(f"Error occurred: {e}")

    # Output: decoded_urls - [{'status': True, 'decoded_url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}]

if __name__ == "__main__":
    main()
```

## Thank You

Thank you for installing and using Google News Decoder! I hope this tool saves you time and effort when working with Google News URLs. If you find it useful, please consider hitting the star button on GitHub. If you’d like to contribute or fork the project, your support is greatly appreciated. Thank you for your support!

## Credits

- Original script by [huksley](https://gist.github.com/huksley/)
