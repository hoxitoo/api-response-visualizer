from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests


def load_from_file(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_from_url(url: str, timeout: int = 20) -> Any:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
