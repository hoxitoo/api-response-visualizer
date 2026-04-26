from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from .data_source import load_from_file, load_from_url
from .flatten import normalize_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Flatten and preview API responses.")
    parser.add_argument("--url", help="HTTP endpoint that returns JSON.")
    parser.add_argument("--file", type=Path, help="Local JSON file.")
    parser.add_argument("--csv-out", type=Path, help="Optional CSV export path.")
    parser.add_argument("--json-out", type=Path, help="Optional normalized JSON export path.")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if not args.url and not args.file:
        raise SystemExit("Provide either --url or --file")

    payload = load_from_url(args.url) if args.url else load_from_file(args.file)
    rows = normalize_payload(payload)
    frame = pd.DataFrame(rows)

    print(f"Rows parsed: {len(frame)}")
    print(f"Columns detected: {len(frame.columns)}")
    if not frame.empty:
        print("\nPreview:")
        print(frame.head(5).to_string(index=False))

    if args.csv_out:
        args.csv_out.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(args.csv_out, index=False)
        print(f"CSV written to: {args.csv_out}")

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
        print(f"JSON written to: {args.json_out}")


if __name__ == "__main__":
    main()
