# Comparison data and version policy / 比较数据及版本约定

`data/papers.json` remains the bibliographic source. `data/comparisons.json` contains exactly one record for every catalog ID; each record holds its own oracle, scope, assumptions, stages and experiment context. The four `data/research-*.json` inputs and complete `docs/comparisons/*.zh.md` reports retain the reviewed group evidence. / 主目录保持书目来源；比较按paperID一一覆盖，原始分组数据与完整稿保留证据。

Each stage has four separate metrics: `theoretical_queries`, `arithmetic`, `experimental_queries`, and `runtime`. Every reviewed metric includes `status`, `value`, `unit` and `evidence`. / 理论查询、离线算术、实验查询和时间分别记录。

```json
{
  "status": "reported",
  "value": "d + d^2",
  "unit": "scalar value queries",
  "evidence": [{
    "url": "https://arxiv.org/pdf/2601.16873v2",
    "locator": "Theorem 4.1, Section 4, PDF pp.3-4",
    "pdf_sha256": "e5221682c1da801dbae06aa21ab2d8469839d49cba2f623ae12b770fbe5a76f8"
  }]
}
```

- `reported`: directly reported under the stated conditions, including conditional qualitative polynomial claims. / 原文声明，保留全部条件。
- `derived`: a calculation by this comparison, requiring `premises` or `derivation`; never presented as a new paper theorem. / 明示推导，必须列前提。
- `NR`: checked relevant methods/results but not reported in a independently citable form; null is not zero. / 核查后未报告，空值不等于零。
- `NA`: the work has no corresponding original algorithm/stage, for example a survey. / 不适用，例如综述的原创攻击成本。
- `pending`: not reviewed; strict release validation rejects it. Failure to obtain a source is not NR. / 尚未核查，严格发布检查拒绝；无法访问不是未报告。

Point/sample budgets retain their units. Query and arithmetic bounds do not imply a bit-complexity or measured-runtime bound. Experiment rows retain model dimensions, precision, hardware, acquisition scope and evaluation distribution; no composite best-case rows are created from unrelated trials. / 点数与采样数保留单位；实验保留尺寸、精度、硬件、范围和分布，不拼接不同实验的最佳数字。

Source locators refer to the actual reviewed PDF. `data/version-audit.json` preserves prior catalog fingerprints when a current record changes. A code audit can legitimately refer to an older paper snapshot: its hash/page is preserved, not silently relabeled as latest. / 页码绑定实际读取版本；更新指纹时保留旧记录，代码审计的旧快照不改称新版。

`code/source-audit.json` records all 55 papers, 27 upstream repositories, commit pins, provenance, license evidence and documented entrypoints. Gitlinks point to upstream authors' history, without bundling their source, datasets or models. Unknown licenses remain references; this index grants no redistribution rights. Reading lists and placeholders do not count as attack implementations. / gitlink保留原作者来源，不将源码/数据/权重写入主库；无明确许可证保留引用，阅读清单与占位仓库不冒充实现。

From the repository root:

```console
python scripts/merge_comparisons.py data/research-raw.json data/research-hard-cnn.json data/research-architecture.json data/research-context.json --strict
python scripts/render_comparisons.py
python scripts/render_catalog.py
python scripts/validate_catalog.py
python scripts/validate_comparisons.py --strict
python scripts/test_collection.py
python scripts/fetch_code.py --paper arxiv-2003.04884
```

The final command previews the selected fixed source without network calls or writes. `--fetch` opts into a source-only local snapshot for a verified licensed upstream, with preserved LICENSE, Git blob verification, size limits and a receipt. No dependencies or upstream code are executed. / 最后一条默认离线预览；明确加`--fetch`才下载合许可源码快照，保留许可证并核验Git blob，不执行上游代码。

The October 28 reconciliation adds two reviewed records without changing schema version 1. Existing alias identities and withdrawn dates live in the bibliography. Comparison rendering reads each withdrawn date instead of assuming one date for all works. Code manifests and original-source pins cover all 54 records; previous paper/code snapshots retain their original dates and fingerprints. / 10 月 28 日核对新增两条，不改变 schema v1；撤回日期按论文读取，代码清单逐条覆盖，历史证据不改称新版。

The [later October 28 monitoring pass](search-audit-2026-10-28-followup.md) backfills one smooth-FFN work, bringing coverage to 55 records, 27 sources and 22 pinned gitlinks. Its direct v2 review is appended to the architecture group; the 12 earlier architecture reviews retain their original supplied-report provenance. A journal DOI updates an existing hard-label record. `former_titles` now participates in normalized identity validation; title corrections do not create new works. / 后续补查新增一篇光滑 FFN，旧记录的发表与改题在原条目更新；旧证据版本保持不变。
