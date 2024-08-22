# Google News Decoder

Google News Decoder is a Python package that can decode Google News links or Google News URLs to their original URLs. It is a simple tool that saves you time and effort. If you find it useful, please support the package by hitting the star on GitHub. Your support helps keep the project going!

[Pypi Package](https://pypi.org/project/googlenewsdecoder/)

## Update

- Version 0.1.3:

  - Small bug fix.

- Version 0.1.2:

  - This update enhances error handling by returning a dictionary containing `status=False` and an appropriate error message when decoding fails.
  - It ensures more robust and clear responses when processing URLs, improving the package's usability and debugging capabilities.
  - decoderv3 is introduced in this version, which handles both `/rss/articles` and `/read` URLs, with comprehensive error reporting.

- Version 0.1.1:
  - This update ensures that the package can now decode URLs that contain `/read` in addition to the previously supported `/rss/articles` format.
  - The functionality was primarily available in **`decoderv2`**.

## Demo

![newss](https://github.com/user-attachments/assets/d85c5abe-8c24-45a2-bee7-d951c0bdf5b9)

## Installation

- You can install this package using pip:

```sh
pip install googlenewsdecoder
```

- You can upgrade this package using pip:

```sh
pip install googlenewsdecoder --upgrade
```

## Usage

Here is an example of how to use this package with different decoders:

### Using decoderv1

```python
from googlenewsdecoder import decoderv1

def main():

    source_url = "https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5"

    decoded_url = decoderv1(source_url)

    print("Decoded URL:", decoded_url)
    # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o

if __name__ == "__main__":
    main()
```

### Using decoderv2

```python
from googlenewsdecoder import decoderv2

def main():

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    decoded_url = decoderv2(source_url)

    print("Decoded URL:", decoded_url)
    # Output: Decoded URL: https://www.whitehouse.gov/briefing-room/statements-releases/2024/08/15/statement-from-president-joe-biden-on-lower-prescription-drug-prices/

if __name__ == "__main__":
    main()
```

### Using decoderv3

```python
from googlenewsdecoder import decoderv3

def main():

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    decoded_url = decoderv3(source_url)

    # Output: decoded_url - {'status': True, 'url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}

    if decoded_url.get("status"):
        print("Decoded URL:", decoded_url["url"])
    else:
        print("Error:", decoded_url)

    # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o
    # If there's an error: Error: Invalid Google News URL
    # Error: {'status': False, 'error': 'Header not found in response: )]}\'\n\n[["wrb.fr","Fbv4je",null,null,null,[3],"generic"],["di",20],["af.httprm",19,"-3096564523984356080",33]]'}

if __name__ == "__main__":
    main()
```

### Using a for loop to decode multiple URLs

```python
from googlenewsdecoder import decoderv3

def main():

    source_urls = ["https://news.google.com/read/CBMilgFBVV95cUxOM0JJaFRwV2dqRDk5dEFpWmF1cC1IVml5WmVtbHZBRXBjZHBfaUsyalRpa1I3a2lKM1ZnZUI4MHhPU2sydi1nX3JrYU0xWjhLaHNfU0N6cEhOYVE2TEptRnRoZGVTU3kzZGJNQzc2aDZqYjJOR0xleTdsemdRVnJGLTVYTEhzWGw4Z19lR3AwR0F1bXlyZ0HSAYwBQVVfeXFMTXlLRDRJUFN5WHg3ZTI0X1F4SjN6bmFIck1IaGxFVVZyOFQxdk1JT3JUbl91SEhsU0NpQzkzRFdHSEtjVGhJNzY4ZTl6eXhESUQ3XzdWVTBGOGgwSmlXaVRmU3BsQlhPVjV4VWxET3FQVzJNbm5CUDlUOHJUTExaME5YbjZCX1NqOU9Ta3U?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/read/CBMiiAFBVV95cUxQOXZLdC1hSzFqQVVLWGJVZzlPaDYyNjdWTURScV9BbVp0SWhFNzZpSWZxSzdhc0tKbVlHMU13NmZVOFdidFFkajZPTm9SRnlZMWFRZ01CVHh0dXU0TjNVMUxZNk9Ibk5DV3hrYlRiZ20zYkIzSFhMQVVpcTFPc00xQjhhcGV1aXM00gF_QVVfeXFMTmtFQXMwMlY1el9WY0VRWEh5YkxXbHF0SjFLQVByNk1xS3hpdnBuUDVxOGZCQXl1QVFXaUVpbk5lUGgwRVVVT25tZlVUVWZqQzc4cm5MSVlfYmVlclFTOUFmTHF4eTlfemhTa2JKeG14bmNabENkSmZaeHB4WnZ5dw?hl=en-US&gl=US&ceid=US%3Aen"]

    for url in source_urls:

        decoded_url = decoderv3(url)

        # Output: decoded_url - {'status': True, 'url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}

        if decoded_url.get("status"):
            print("Decoded URL:", decoded_url["url"])

            # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o
        else:
            print("Error:", decoded_url["error"])

            # If there's an error: Error: Invalid Google News URL

            # Example Error: {'status': False, 'error': 'Header not found in response: )]}\'\n\n[["wrb.fr","Fbv4je",null,null,null,[3],"generic"],["di",20],["af.httprm",19,"-3096564523984356080",33]]'}

if __name__ == "__main__":
    main()
```

## Thank You

Thank you for installing and using Google News Decoder! I hope this tool saves you time and effort when working with Google News URLs. If you find it useful, please consider hitting the star button on GitHub. If you’d like to contribute or fork the project, your support is greatly appreciated. Thank you for your support!

## Credits

- Original script by [huksley](https://gist.github.com/huksley/)
=======
# Google News Decoder

Google News Decoder is a Python package that can decode Google News links or Google News URLs to their original URLs. It is a simple tool that saves you time and effort. If you find it useful, please support the package by hitting the star on GitHub. Your support helps keep the project going!

[Pypi Package](https://pypi.org/project/googlenewsdecoder/)

## Update

- Version 0.1.2:

  - This update enhances error handling by returning a dictionary containing `status=False` and an appropriate error message when decoding fails.
  - It ensures more robust and clear responses when processing URLs, improving the package's usability and debugging capabilities.
  - decoderv3 is introduced in this version, which handles both `/rss/articles` and `/read` URLs, with comprehensive error reporting.

- Version 0.1.1:
  - This update ensures that the package can now decode URLs that contain `/read` in addition to the previously supported `/rss/articles` format.
  - The functionality was primarily available in **`decoderv2`**.

## Demo

![newss](https://github.com/user-attachments/assets/d85c5abe-8c24-45a2-bee7-d951c0bdf5b9)

## Installation

- You can install this package using pip:

```sh
pip install googlenewsdecoder
```

- You can upgrade this package using pip:

```sh
pip install googlenewsdecoder --upgrade
```

## Usage

Here is an example of how to use this package with different decoders:

### Using decoderv1

```python
from googlenewsdecoder import decoderv1

def main():

    source_url = "https://news.google.com/rss/articles/CBMiLmh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy9hcnRpY2xlcy9jampqbnhkdjE4OG_SATJodHRwczovL3d3dy5iYmMuY29tL25ld3MvYXJ0aWNsZXMvY2pqam54ZHYxODhvLmFtcA?oc=5"

    decoded_url = decoderv1(source_url)

    print("Decoded URL:", decoded_url)
    # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o

if __name__ == "__main__":
    main()
```

### Using decoderv2

```python
from googlenewsdecoder import decoderv2

def main():

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    decoded_url = decoderv2(source_url)

    print("Decoded URL:", decoded_url)
    # Output: Decoded URL: https://www.whitehouse.gov/briefing-room/statements-releases/2024/08/15/statement-from-president-joe-biden-on-lower-prescription-drug-prices/

if __name__ == "__main__":
    main()
```

### Using decoderv3

```python
from googlenewsdecoder import decoderv3

def main():

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    decoded_url = decoderv3(source_url)

    # Output: decoded_url - {'status': True, 'url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}

    if decoded_url.get("status"):
        print("Decoded URL:", decoded_url["url"])
    else:
        print("Error:", decoded_url)

    # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o
    # If there's an error: Error: Invalid Google News URL
    # Error: {'status': False, 'error': 'Header not found in response: )]}\'\n\n[["wrb.fr","Fbv4je",null,null,null,[3],"generic"],["di",20],["af.httprm",19,"-3096564523984356080",33]]'}

if __name__ == "__main__":
    main()
```

### Using a for loop to decode multiple URLs

```python
from googlenewsdecoder import decoderv3

def main():

    source_urls = ["https://news.google.com/read/CBMilgFBVV95cUxOM0JJaFRwV2dqRDk5dEFpWmF1cC1IVml5WmVtbHZBRXBjZHBfaUsyalRpa1I3a2lKM1ZnZUI4MHhPU2sydi1nX3JrYU0xWjhLaHNfU0N6cEhOYVE2TEptRnRoZGVTU3kzZGJNQzc2aDZqYjJOR0xleTdsemdRVnJGLTVYTEhzWGw4Z19lR3AwR0F1bXlyZ0HSAYwBQVVfeXFMTXlLRDRJUFN5WHg3ZTI0X1F4SjN6bmFIck1IaGxFVVZyOFQxdk1JT3JUbl91SEhsU0NpQzkzRFdHSEtjVGhJNzY4ZTl6eXhESUQ3XzdWVTBGOGgwSmlXaVRmU3BsQlhPVjV4VWxET3FQVzJNbm5CUDlUOHJUTExaME5YbjZCX1NqOU9Ta3U?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/read/CBMiiAFBVV95cUxQOXZLdC1hSzFqQVVLWGJVZzlPaDYyNjdWTURScV9BbVp0SWhFNzZpSWZxSzdhc0tKbVlHMU13NmZVOFdidFFkajZPTm9SRnlZMWFRZ01CVHh0dXU0TjNVMUxZNk9Ibk5DV3hrYlRiZ20zYkIzSFhMQVVpcTFPc00xQjhhcGV1aXM00gF_QVVfeXFMTmtFQXMwMlY1el9WY0VRWEh5YkxXbHF0SjFLQVByNk1xS3hpdnBuUDVxOGZCQXl1QVFXaUVpbk5lUGgwRVVVT25tZlVUVWZqQzc4cm5MSVlfYmVlclFTOUFmTHF4eTlfemhTa2JKeG14bmNabENkSmZaeHB4WnZ5dw?hl=en-US&gl=US&ceid=US%3Aen"]

    for url in source_urls:

        decoded_url = decoderv3(url)

        # Output: decoded_url - {'status': True, 'url': 'https://healthdatamanagement.com/articles/empowering-the-quintuple-aim-embracing-an-essential-architecture/'}

        if decoded_url.get("status"):
            print("Decoded URL:", decoded_url["url"])

            # Output: Decoded URL: https://www.bbc.com/news/articles/cjjjnxdv188o
        else:
            print("Error:", decoded_url["error"])

            # If there's an error: Error: Invalid Google News URL

            # Example Error: {'status': False, 'error': 'Header not found in response: )]}\'\n\n[["wrb.fr","Fbv4je",null,null,null,[3],"generic"],["di",20],["af.httprm",19,"-3096564523984356080",33]]'}

if __name__ == "__main__":
    main()
```

## Thank You

Thank you for installing and using Google News Decoder! I hope this tool saves you time and effort when working with Google News URLs. If you find it useful, please consider hitting the star button on GitHub. If you’d like to contribute or fork the project, your support is greatly appreciated. Thank you for your support!

## Credits

- Original script by [huksley](https://gist.github.com/huksley/)
