import asyncio

from googlenewsdecoder import gnews_decoder_async


def main():
    interval_time = 1  # optional; None means no wait
    timeout = 15.0
    # Optional. Examples:
    #   proxy = "http://user:pass@host:port"
    #   proxy = "https://host:port"
    #   proxy = "socks5://user:pass@host:port"
    proxy = None

    source_url = "https://news.google.com/read/CBMi2AFBVV95cUxPd1ZCc1loODVVNHpnbFFTVHFkTG94eWh1NWhTeE9yT1RyNTRXMVV2S1VIUFM3ZlVkVjl6UHh3RkJ0bXdaTVRlcHBjMWFWTkhvZWVuM3pBMEtEdlllRDBveGdIUm9GUnJ4ajd1YWR5cWs3VFA5V2dsZnY1RDZhVDdORHRSSE9EalF2TndWdlh4bkJOWU5UMTdIV2RCc285Q2p3MFA4WnpodUNqN1RNREMwa3d5T2ZHS0JlX0MySGZLc01kWDNtUEkzemtkbWhTZXdQTmdfU1JJaXY?hl=en-US&gl=US&ceid=US%3Aen"

    try:
        result = asyncio.run(
            gnews_decoder_async(
                source_url,
                interval=interval_time,
                proxy=proxy,
                timeout=timeout,
            )
        )
        if result["success"]:
            print("Decoded URL:", result["decoded_url"])
        else:
            print("Error:", result["message"])
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
