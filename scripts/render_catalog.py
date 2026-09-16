"""Render bilingual catalogs and archive-oriented BibTeX from reviewed JSON."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "official": ("Official", "官方"),
    "anonymous_attachment": ("Anonymous attachment", "匿名附件"),
    "unavailable_404": ("Paper-linked; 404", "论文所链；404"),
    "expired_410": ("Expired; 410", "已过期；410"),
    "supplementary": ("Official supplementary", "官方补充代码"),
    "author_extension_fork": ("Author extension fork", "作者扩展分支"),
    "reading_resource": ("Reading list, not attack code", "阅读清单，非攻击代码"),
    "not_found": ("Not located", "未检索到"),
    "announced": ("Announced; placeholder URL", "已宣告；URL 为占位符"),
    "mentioned": ("Supplement mentioned; URL not located", "提及补充代码；未找到 URL"),
}


def esc(value):
    return value.replace("|", "&#124;").replace("\n", " ")


def catalog(data, zh):
    lang = "zh" if zh else "en"
    out = [f"## {'论文分类' if zh else 'Paper Catalog'}", ""]
    for c in data["categories"]:
        papers = sorted((p for p in data["papers"] if p["category"] == c["id"]), key=lambda p: (p["year"], p["id"]), reverse=True)
        out += [f"### {c[lang]} ({len(papers)})", ""]
        out += ["| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |" if zh else "| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |", "|---|---|---|---|---|---|"]
        for p in papers:
            code = p["code"]
            label = LABELS[code["status"]][int(zh)]
            code_cell = f"[{label}]({code['url']})" if code.get("url") else label
            out.append(f"| {p['year']} | [{esc(p['title'])}]({p['url']}) · [PDF]({p['pdf_url']}) | {esc(p['venue_status'])} | {esc(p['oracle'])}<br>{esc(p['architecture'])} | {esc(p['summary_' + lang])} | {code_cell} |")
        out.append("")
    return "\n".join(out)


def bibtex(data):
    def tex(s):
        for old, new in [("\\", "\\textbackslash{}"), ("&", "\\&"), ("%", "\\%"), ("_", "\\_"), ("#", "\\#")]:
            s = s.replace(old, new)
        return s
    result = ["% Archive-oriented records. Year refers to the archive/report year, not necessarily the venue year.", "% Venue/status is retained in note; no unverified proceedings pages or DOIs are invented.", ""]
    for p in data["papers"]:
        result += ["@misc{" + p["id"].replace("-", "") + ",", "  title = {{" + tex(p["title"]) + "}},", "  author = {" + " and ".join(tex(a) for a in p["authors"]) + "},", f"  year = {{{p['year']}}},", f"  url = {{{p['url']}}},", "  note = {" + tex(p["venue_status"]) + "}", "}", ""]
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated outputs differ")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    papers = data["papers"]
    assert len({p["id"] for p in papers}) == len(papers)
    assert len({p["url"] for p in papers}) == len(papers)
    categories = {c["id"] for c in data["categories"]}
    for p in papers:
        assert p["category"] in categories and p["code"]["status"] in LABELS
        assert p["authors"] and p["pdf"]["pages"] > 0
        assert len(p["pdf"]["sha256"]) == 64
    outputs = {}
    for zh, name in [(False, "README.md"), (True, "README_zh-CN.md")]:
        template = (ROOT / "docs" / ("readme_zh.template.md" if zh else "readme_en.template.md")).read_text(encoding="utf-8")
        outputs[name] = template.replace("{{DATE}}", data["updated"]).replace("{{COUNT}}", str(len(papers))).replace("{{CATALOG}}", catalog(data, zh))
    outputs["bib/cryptanalytic_extraction.bib"] = bibtex(data)
    for path, value in outputs.items():
        target = ROOT / path
        if args.check:
            assert target.exists() and target.read_text(encoding="utf-8") == value, f"Regenerate {path}"
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value, encoding="utf-8")
    print(f"{'Validated' if args.check else 'Rendered'} {len(papers)} records, two languages and BibTeX.")


if __name__ == "__main__":
    main()
