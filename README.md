# API Response Visualizer

A practical developer tool for turning raw JSON API responses into flat, readable tables.

## What problem it solves

Many APIs return nested JSON that is hard to scan quickly.  
This tool fetches a response and converts it into:

- flattened table rows
- CSV export
- compact console preview
- metadata about nesting depth and field coverage

## Features

- works with live endpoints
- also supports local JSON files
- flattens nested dictionaries
- keeps list payloads usable for table output
- exports CSV and JSON preview

## Usage

From an API:

```bash
python -m src.main --url https://jsonplaceholder.typicode.com/users --csv-out outputs/users.csv
```

From a local file:

```bash
python -m src.main --file examples/sample_response.json
```

## Testing

```bash
pytest
```
