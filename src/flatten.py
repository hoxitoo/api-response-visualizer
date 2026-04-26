from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def flatten_dict(payload: dict[str, Any], prefix: str = "", sep: str = ".") -> dict[str, Any]:
    flat: dict[str, Any] = {}
    for key, value in payload.items():
        new_key = f"{prefix}{sep}{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_dict(value, prefix=new_key, sep=sep))
        elif isinstance(value, list):
            flat[new_key] = ", ".join(map(str, value))
        else:
            flat[new_key] = value
    return flat


def normalize_payload(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        rows = []
        for item in payload:
            if isinstance(item, dict):
                rows.append(flatten_dict(item))
            else:
                rows.append({"value": item})
        return rows

    if isinstance(payload, dict):
        return [flatten_dict(payload)]

    return [{"value": payload}]
