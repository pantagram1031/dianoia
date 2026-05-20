#!/usr/bin/env python3
"""Small OEIS lookup wrapper for dianoia subagents."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request


API = "https://oeis.org/search"


def fetch_json(query: str, max_results: int) -> dict:
    params = {"q": query, "fmt": "json", "start": "0"}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "dianoia-oeis-connector/0.1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = response.read().decode("utf-8", errors="replace")
    data = json.loads(payload)
    if isinstance(data, list):
        results = data
    else:
        results = data.get("results", [])
    return {"results": results[:max_results], "source": "oeis_json"}


def compact_record(record: dict) -> dict[str, object]:
    number = record.get("number", "")
    sequence_id = f"A{int(number):06d}" if isinstance(number, int) else str(record.get("number", ""))
    return {
        "id": sequence_id,
        "name": record.get("name", ""),
        "data": record.get("data", ""),
        "comment": record.get("comment", []),
        "reference": record.get("reference", []),
        "link": record.get("link", []),
        "author": record.get("author", ""),
        "url": f"https://oeis.org/{sequence_id}" if sequence_id else "",
    }


def search(args: argparse.Namespace) -> list[dict[str, object]]:
    data = fetch_json(args.query, args.max_results)
    return [compact_record(record) for record in data["results"]]


def fetch(args: argparse.Namespace) -> list[dict[str, object]]:
    seq = args.sequence_id.upper()
    if not seq.startswith("A"):
        seq = f"A{int(seq):06d}"
    data = fetch_json(f"id:{seq}", 1)
    return [compact_record(record) for record in data["results"]]


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Lookup OEIS records as compact JSON.")
    sub = parser.add_subparsers(dest="command", required=True)

    search_parser = sub.add_parser("search", help="Search OEIS records")
    search_parser.add_argument("query")
    search_parser.add_argument("--max-results", type=int, default=5)
    search_parser.set_defaults(func=search)

    fetch_parser = sub.add_parser("fetch", help="Fetch one OEIS sequence")
    fetch_parser.add_argument("sequence_id")
    fetch_parser.set_defaults(func=fetch)

    args = parser.parse_args(argv)
    print(json.dumps(args.func(args), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
