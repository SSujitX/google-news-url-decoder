DEFAULT_TIMEOUT = 10.0
"""Seconds any single HTTP request may take. `requests` and `httpx` apply this per
connect/read/write operation, so it bounds a stalled socket, not the whole call."""

DEFAULT_USER_AGENT = "python-requests/2.32.3"
"""User-Agent the decoding pages are served to. Google returns the JS interstitial (no
`c-wiz > div[jscontroller]`, so nothing to decode) to browser and unknown agents alike;
simple clients such as requests, curl and wget get the real page. The sync decoders
inherit this from requests' own default, so only the httpx-based async decoder has to
send it explicitly."""
