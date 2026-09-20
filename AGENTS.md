## Learned User Preferences

- Use UV as the only packaging and local-dev path; do not keep setup.py or requirements.txt as a second source of truth.
- Keep packaging migrations conservative: preserve the live PyPI name and existing `pip install googlenewsdecoder` installs.
- Start releases from Actions → Release → Run workflow with a bump (`current` / `patch` / `minor` / `major`) that tags `vX.Y.Z`; keep a single version source in `pyproject.toml`. GitHub Release notes are generated from conventional commits (`.github/scripts/generate-release-notes.sh`). No `RELEASE.md`.

## Learned Workspace Facts

- PyPI and import name is `googlenewsdecoder`; the GitHub repo is `google-news-url-decoder`.
- Packaging is UV with `uv_build` and a flat layout (`module-name = "googlenewsdecoder"`, `module-root = ""`).
- `googlenewsdecoder.__version__` comes from `importlib.metadata.version("googlenewsdecoder")`, not a `__version__.py` file.
- `.github/workflows/publish.yml` (workflow name Release) publishes on `workflow_dispatch` bump or a `vX.Y.Z` tag push via OIDC trusted publishing. Unprefixed tags like `0.1.7` no longer trigger publish. Do not auto-publish on every push to main.
- Requires Python >=3.11. Sync and async decoders both use `httpx[http2,socks]`. Package files: `_parse.py`, `decoder.py`, `decoder_async.py`. Version is `pyproject.toml` / `__version__` from metadata. Timeout default is `10.0` and async batch concurrency is `8` on the call signatures.
- Public result dict key is `success` (bool), plus `decoded_url` or `message`. `rich` is a UV dev extra only, not a package dependency.
- Google News decode (proved live 2026-09-21): article id is opaque (`AU_yqL…`, no URL in base64). RSS XML and the homepage have no publisher URL. Fetch only `https://news.google.com/rss/articles/{id}?hl=&gl=&ceid=` (copy locale from the input URL; default `en-US` / `US` / `US:en`) and read `data-n-a-sg` / `data-n-a-ts`. Then one POST to `https://news.google.com/_/DotsSplashUi/data/batchexecute` RPC `Fbv4je` / `garturlreq`. Response request id is the last non-null slot after the payload (live: `row[6]`); Google can reorder rows. `sg`/`ts` change every fetch — cache the decoded URL, not the signature.
- Do not GET `/articles/{id}` or `/read/{id}` from httpx: both 302 to `google.com/sorry` (bot interstitial). A real browser `/read/` JS-navigates to the publisher; that is not the library path. Do not follow `sorry` or publisher hops. Same-origin `?hl=` 302s are OK.
- Headers/UA do not matter on the RSS splash path (httpx default, Chrome UA, and Referer+Accept-Language all returned `sg`). They also do not fix `/articles/` or `/read/`. Proxy and `interval` are only for 429 on many HTML GETs (~590KB each); the batch POST is one request. No captcha solve, no header spoof required.
- When asked to reverse-engineer / re-check Google News: live-compare those three paths, confirm `data-n-a-sg` still exists, dump one batchexecute row shape (id slot), and only change `_parse.py` / decoders if the live protocol moved.
