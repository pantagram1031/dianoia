#!/usr/bin/env python3
"""Small arXiv lookup wrapper for dianoia subagents."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def text(node: ET.Element | None) -> str:
    return "" if node is None or node.text is None else " ".join(node.text.split())


def parse_entry(entry: ET.Element) -> dict[str, object]:
    raw_id = text(entry.find("atom:id", NS))
    arxiv_id = raw_id.rstrip("/").split("/")[-1]
    authors = [text(author.find("atom:name", NS)) for author in entry.findall("atom:author", NS)]
    published = text(entry.find("atom:published", NS))
    doi = text(entry.find("arxiv:doi", NS))
    links = []
    for link in entry.findall("atom:link", NS):
        href = link.attrib.get("href")
        if href:
            links.append({"rel": link.attrib.get("rel", ""), "type": link.attrib.get("type", ""), "href": href})
    return {
        "arxiv_id": arxiv_id,
        "title": text(entry.find("atom:title", NS)),
        "authors": authors,
        "year": published[:4] if published else "",
        "published": published,
        "updated": text(entry.find("atom:updated", NS)),
        "doi": doi,
        "abstract": text(entry.find("atom:summary", NS)),
        "links": links,
    }


def query(params: dict[str, str]) -> list[dict[str, object]]:
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "dianoia-arxiv-connector/0.1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = response.read()
    root = ET.fromstring(payload)
    return [parse_entry(entry) for entry in root.findall("atom:entry", NS)]


def fetch_abs_page(arxiv_id: str) -> dict[str, object]:
    url = f"https://arxiv.org/abs/{urllib.parse.quote(arxiv_id)}"
    req = urllib.request.Request(url, headers={"User-Agent": "dianoia-arxiv-connector/0.1"})
    with urllib.request.urlopen(req, timeout=30) as response:
        page = response.read().decode("utf-8", errors="replace")

    def meta(name: str) -> str:
        pattern = rf'<meta\s+name="{re.escape(name)}"\s+content="([^"]*)"'
        match = re.search(pattern, page)
        return html.unescape(match.group(1)).strip() if match else ""

    authors = re.findall(r'<meta\s+name="citation_author"\s+content="([^"]*)"', page)
    published = meta("citation_date")
    pdf_url = meta("citation_pdf_url")
    title = meta("citation_title")
    abstract_match = re.search(r'<blockquote class="abstract mathjax">\s*<span class="descriptor">Abstract:</span>\s*(.*?)\s*</blockquote>', page, re.S)
    abstract = ""
    if abstract_match:
        abstract = re.sub(r"<[^>]+>", " ", abstract_match.group(1))
        abstract = " ".join(html.unescape(abstract).split())
    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": [html.unescape(author).strip() for author in authors],
        "year": published[:4] if published else "",
        "published": published,
        "updated": "",
        "doi": meta("citation_doi"),
        "abstract": abstract,
        "links": [{"rel": "alternate", "type": "text/html", "href": url}]
        + ([{"rel": "related", "type": "application/pdf", "href": pdf_url}] if pdf_url else []),
        "source": "arxiv_abs_fallback",
    }


def search(args: argparse.Namespace) -> list[dict[str, object]]:
    return query(
        {
            "search_query": f"all:{args.query}",
            "start": "0",
            "max_results": str(args.max_results),
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )


def fetch(args: argparse.Namespace) -> list[dict[str, object]]:
    try:
        return query({"id_list": args.arxiv_id, "max_results": "1"})
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            return [fetch_abs_page(args.arxiv_id)]
        raise


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Lookup arXiv records as compact JSON.")
    sub = parser.add_subparsers(dest="command", required=True)

    search_parser = sub.add_parser("search", help="Search arXiv records")
    search_parser.add_argument("query")
    search_parser.add_argument("--max-results", type=int, default=5)
    search_parser.set_defaults(func=search)

    fetch_parser = sub.add_parser("fetch", help="Fetch one arXiv id")
    fetch_parser.add_argument("arxiv_id")
    fetch_parser.set_defaults(func=fetch)

    args = parser.parse_args(argv)
    records = args.func(args)
    print(json.dumps(records, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
