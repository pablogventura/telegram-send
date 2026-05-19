# Contributing

Fork of [rahiel/telegram-send](https://github.com/rahiel/telegram-send). Keep GPL-3.0+ attribution when merging changes derived from upstream.

## Development

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/telegram-send-wait --version
```

Manual checks: see [run_tests.bash](run_tests.bash) and the wait-reply comments at the end of that file.

## Publishing to PyPI

1. Create a [PyPI](https://pypi.org) account and verify your email.
2. Create an API token (project scope `telegram-send-wait` or whole account for the first upload).
3. Confirm the name is available: search [pypi.org/project/telegram-send-wait](https://pypi.org/project/telegram-send-wait) or run `pip index versions telegram-send-wait`.
4. Bump `telegram_send/version.py` if needed.
5. `uv sync && uv build && uv publish` (see [release.bash](release.bash)).
6. Smoke test: `pipx install telegram-send-wait && telegram-send-wait --version`.
7. Tag the release on GitHub, e.g. `git tag v1.0.0 && git push origin v1.0.0`.
