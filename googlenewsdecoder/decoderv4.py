import requests
import base64


def fetch_decoded_batch_execute(ids):
    try:
        envelopes = []
        for i, id in enumerate(ids, start=1):
            envelope = (
                f'["Fbv4je","[\\"garturlreq\\",[[\\"en-US\\",\\"US\\",[\\"FINANCE_TOP_INDICES\\",\\"WEB_TEST_1_0_0\\"],'
                f'null,null,1,1,\\"US:en\\",null,180,null,null,null,null,null,0,null,null,[1608992183,723341000]],'
                f'\\"en-US\\",\\"US\\",1,[2,3,4,8],1,0,\\"655000234\\",0,0,null,0],\\"{id}\\"]",null,"{i}"]'
            )
            envelopes.append(envelope)

        s = f'[[{",".join(envelopes)}]]'

        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "Referer": "https://news.google.com/",
        }

        response = requests.post(
            url="https://news.google.com/_/DotsSplashUi/data/batchexecute?rpcids=Fbv4je",
            headers=headers,
            data={"f.req": s},
        )

        if response.status_code != 200:
            return {"status": False, "error": "Failed to fetch data from Google."}

        text = response.text
        urls = []
        header = '[\\"garturlres\\",\\"'
        footer = '\\",'
        while header in text:
            start = text.split(header, 1)[1]
            if footer not in start:
                return {"status": False, "error": "Footer not found in response."}
            url = start.split(footer, 1)[0]
            urls.append(url)
            text = start.split(footer, 1)[1]

        return {"status": True, "urls": urls}
    except Exception as e:
        return {"status": False, "error": str(e)}


def decode_google_news_url(source_urls):
    results = []
    batch_ids = []
    id_to_index_map = {}

    try:
        for index, source_url in enumerate(source_urls):
            url = requests.utils.urlparse(source_url)
            path = url.path.split("/")
            if (
                url.hostname == "news.google.com"
                and len(path) > 1
                and (path[-2] == "articles" or path[-2] == "read")
            ):
                base64_str = path[-1]
                decoded_bytes = base64.urlsafe_b64decode(base64_str + "==")
                decoded_str = decoded_bytes.decode("latin1")

                prefix = b"\x08\x13\x22".decode("latin1")
                if decoded_str.startswith(prefix):
                    decoded_str = decoded_str[len(prefix) :]

                suffix = b"\xd2\x01\x00".decode("latin1")
                if decoded_str.endswith(suffix):
                    decoded_str = decoded_str[: -len(suffix)]

                bytes_array = bytearray(decoded_str, "latin1")
                length = bytes_array[0]
                if length >= 0x80:
                    decoded_str = decoded_str[2 : length + 1]
                else:
                    decoded_str = decoded_str[1 : length + 1]

                if decoded_str.startswith("AU_yqL"):
                    batch_ids.append(base64_str)
                    id_to_index_map[base64_str] = index
                else:
                    results.append({"status": True, "url": decoded_str})
            else:
                results.append({"status": False, "error": "Invalid Google News URL"})

        if batch_ids:
            decoded_result = fetch_decoded_batch_execute(batch_ids)
            if decoded_result["status"]:
                for id, url in zip(batch_ids, decoded_result["urls"]):
                    index = id_to_index_map[id]
                    results.insert(index, {"status": True, "url": url})
            else:
                results.extend(
                    [{"status": False, "error": decoded_result["error"]}]
                    * len(batch_ids)
                )
    except Exception as e:
        results.append({"status": False, "error": str(e)})

    return results


# # Example usage
# if __name__ == "__main__":
#     # source_url = "https://news.google.com/rss/articles/CBMiVkFVX3lxTE4zaGU2bTY2ZGkzdTRkSkJ0cFpsTGlDUjkxU2FBRURaTWU0c3QzVWZ1MHZZNkZ5Vzk1ZVBnTDFHY2R6ZmdCUkpUTUJsS1pqQTlCRzlzbHV3?oc=5"
#     source_url = "https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMTRqdUZpNl9hQldXbGo2YVVLOGFQdkFLYldlMUxUVlNEaElsYjRRODVUMkF3R1RYdWxvT1NoVzdUYS0xSHg3eVdpTjdVODQ5cVJJLWt4dk9vZFBScVp2ZmpzQXZZRy1ncDM5c2tRbXBVVHVrQnpmMGVrQXNkQVItV3h4dVQ1V1BTbjhnM3k2ZUdPdnhVOFk1NmllNTZkdGJTbW9NX0k5U3E2Tkk?oc=5"

#     decoded_urls = decode_google_news_url([source_url])
#     print(decoded_urls)
