from googlenewsdecoder._parse import (
    apply_decoded,
    article_id,
    build_batchexecute_body,
    err,
    next_google_hop,
    params_page_url,
    parse_batchexecute,
    parse_signature,
)

READ = (
    "https://news.google.com/read/CBMiABC123?hl=en-US&gl=US&ceid=US%3Aen"
)
ARTICLES = "https://news.google.com/articles/CBMiXYZ"
RSS = "https://news.google.com/rss/articles/CBMiRSS?oc=5"


def test_article_id_read_articles_rss():
    assert article_id(READ) == "CBMiABC123"
    assert article_id(ARTICLES) == "CBMiXYZ"
    assert article_id(RSS) == "CBMiRSS"


def test_params_page_url_uses_rss_and_locale():
    assert params_page_url("CBMi1") == (
        "https://news.google.com/rss/articles/CBMi1?hl=en-US&gl=US&ceid=US%3Aen"
    )
    assert params_page_url("CBMi1", READ).endswith("hl=en-US&gl=US&ceid=US%3Aen")
    assert "rss/articles/CBMi1" in params_page_url("CBMi1", READ)


def test_article_id_rejects_non_google():
    assert article_id("https://example.com/articles/CBMiABC") is None
    assert article_id("not-a-url") is None


def test_parse_signature_from_cwiz():
    html = (
        '<html><c-wiz><div jscontroller="ctrl" '
        'data-n-a-sg="SIG" data-n-a-ts="1700000000"></div></c-wiz></html>'
    )
    assert parse_signature(html) == ("SIG", "1700000000")


def test_parse_signature_regex_fallback():
    html = '<div data-n-a-sg="S2" data-n-a-ts="99"></div>'
    assert parse_signature(html) == ("S2", "99")


def test_parse_signature_missing():
    assert parse_signature("<html><body>nope</body></html>") is None


def test_batchexecute_roundtrip_single():
    body = build_batchexecute_body([("0", "CBMi1", "1", "sig")])
    assert "Fbv4je" in body
    assert "garturlreq" in body
    assert "CBMi1" in body


def test_parse_batchexecute_keeps_request_ids():
    inner_a = '["garturlres","https://a.example/1"]'
    inner_b = '["garturlres","https://b.example/2"]'
    text = (
        ")]}'\n\n"
        + __import__("json").dumps(
            [
                ["wrb.fr", "Fbv4je", inner_b, None, None, None, "2"],
                ["wrb.fr", "Fbv4je", inner_a, None, None, None, "0"],
                ["di", 1],
            ]
        )
    )
    assert parse_batchexecute(text) == [
        ("2", "https://b.example/2"),
        ("0", "https://a.example/1"),
    ]


def test_next_google_hop_same_origin_only():
    current = "https://news.google.com/rss/articles/CBMi1"
    assert next_google_hop(current, current + "?hl=en-US") == current + "?hl=en-US"
    assert next_google_hop(current, "https://www.cnn.com/story") is None
    assert next_google_hop(current, None) is None


def test_apply_decoded_skips_failed_middle_id():
    results = [err("pending"), err("pending"), err("pending")]
    pending = [(0, "a", "1", "s"), (2, "c", "3", "s")]
    pairs = [("2", "https://c.example"), ("0", "https://a.example")]
    apply_decoded(results, pending, pairs)
    assert results[0]["decoded_url"] == "https://a.example"
    assert results[1]["message"] == "pending"
    assert results[2]["decoded_url"] == "https://c.example"
