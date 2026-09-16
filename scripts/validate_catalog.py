"""Offline consistency checks; optionally verify a local PDF corpus by hash."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", type=Path, help="Optional local reference directory")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "scripts/render_catalog.py"), "--check"], check=True)
    data = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    papers = data["papers"]
    identities = [u for p in papers for u in [p["url"], *p["aliases"]]]
    assert len(identities) == len(set(identities)), "Alias duplicates another work"
    for name in ["README.md", "README_zh-CN.md", "docs/progress-2026-09.md", "docs/search-audit-2026-09-17.md"]:
        file = ROOT / name
        text = file.read_text(encoding="utf-8")
        assert "awesome-cryptanalytic-model-extraction" not in text
        assert "\ufffd" not in text
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if not urlparse(link).scheme and not link.startswith("#"):
                assert (file.parent / unquote(link.split("#")[0])).exists(), (name, link)
        if name.startswith("README"):
            rows = [line for line in text.splitlines() if re.match(r"\| 20\d\d \|", line)]
            assert len(rows) == len(papers)
            for p in papers:
                assert sum(f"]({p['url']})" in row for row in rows) == 1, p["id"]
    bib = (ROOT / "bib/cryptanalytic_extraction.bib").read_text(encoding="utf-8")
    assert len(re.findall(r"^@misc\{", bib, re.M)) == len(papers)
    assert bib.count("{") == bib.count("}")
    if args.ref:
        for p in papers:
            path = args.ref / p["pdf"]["filename"]
            content = path.read_bytes()
            assert content.startswith(b"%PDF-")
            assert len(content) == p["pdf"]["bytes"]
            assert hashlib.sha256(content).hexdigest() == p["pdf"]["sha256"], path
    print(f"PASS: {len(papers)} unique papers, aliases, bilingual rows, local links, BibTeX" + (", and local PDF hashes." if args.ref else "."))


if __name__ == "__main__":
    main()
