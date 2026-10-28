# Monitoring follow-up / 文献监测补查

Checked **2026-10-28, UTC**, after cloning, checking out `main`, fetching and fast-forwarding against `origin/main` at `586e4fe`. The baseline already contains **54 works in 13 categories**, including the additions and ePrint aliases in the [earlier same-day audit](search-audit-2026-10-28.md). Catalog, prior progress/search/update documents, templates, BibTeX, comparison/version metadata, source audit and validation workflow were inspected before searching or editing. / 先同步阅读仓库，后检索；先前的新增与别名均不重复计数。

Outcome: **one previously missed work**, **one publication-status update**, and **one official-title correction**. Current catalog: **55 works, same 13 categories**. The added paper was submitted in August and revised in September; it is not an October submission. No timestamp-only revision is counted.

## Searches and limits / 检索及覆盖边界

Both required sources were queried directly. The web tool initially could not open Scholar/IACR search URLs; ordinary HTTPS requests with a browser User-Agent returned HTTP 200 and readable result pages. Search discoveries were verified on primary pages and, for the new work, the full PDF.

| Source | Exact query / coverage actually screened |
|---|---|
| [Google Scholar](https://scholar.google.com/scholar?q=%22cryptanalytic+extraction%22&as_ylo=2026&scisbd=1) | `"cryptanalytic extraction"`, year >= 2026, date order: two pages, 15 displayed rows. Displayed approximate totals changed from 13 to 15; they are not stable unique-work counts. |
| [Scholar](https://scholar.google.com/scholar?q=%22cryptanalytic+model+extraction%22&as_ylo=2026&scisbd=1) | `"cryptanalytic model extraction"`, year >= 2026/date order: 5 rows. |
| [Scholar](https://scholar.google.com/scholar?q=%22cryptanalytic+neural+network+extraction%22+OR+%22cryptanalytic+parameter+extraction%22&as_ylo=2026) | `"cryptanalytic neural network extraction" OR "cryptanalytic parameter extraction"`, year >= 2026: 3 rows. |
| [Scholar](https://scholar.google.com/scholar?q=cryptanalysis+transformer+%22extraction%22&as_ylo=2026&scisbd=1) | `cryptanalysis transformer "extraction"`, year >= 2026/date order: 5 rows, including the curvature paper. Exact `"Curvature Cryptanalysis"` returned one work. |
| Scholar, complementary | `cryptanalytic neural extraction` (first 10 of approximately 30); `"sign recovery" "neural"` (4); `"cryptanalytic" "defense"` (3); `"hard-label" "extraction"` (first 10 of approximately 18), all year >= 2026/date order. First-page limits retained. |
| [Scholar](https://scholar.google.com/scholar?q=%22Polynomial-Time+Cryptanalytic+Extraction%22+%2209586%22) | `"Polynomial-Time Cryptanalytic Extraction" "09586"`: one publisher record. |
| [IACR ePrint](https://eprint.iacr.org/search?q=cryptanalytic%20extraction) | `cryptanalytic extraction`: 36 result rows, including unrelated cryptographic extraction. |
| [IACR ePrint](https://eprint.iacr.org/search?q=neural%20extraction) | `neural extraction`: 69 result rows; titles and archive abstract excerpts screened. |
| [IACR ePrint](https://eprint.iacr.org/search?q=sign%20recovery) | `sign recovery`: first 100 rows; many key/signature rather than neuron-sign results. Later pages not exhaustively crawled. |
| [IACR ePrint](https://eprint.iacr.org/search?q=signature%20recovery%20neural) | `signature recovery neural`: 13 rows. |
| [arXiv API](https://export.arxiv.org/api/query) | `(all:cryptanalytic OR all:cryptanalytical) AND (all:extraction OR all:extracting)`, last-update order, max 100: all 20 returned records. |
| arXiv API, broader terminology | `(all:cryptanalysis OR all:cryptanalytic OR all:cryptanalytical) AND (all:neural OR all:transformer OR all:attention) AND (all:extraction OR all:recovery OR all:recovering)`, max 100: all 48 records, including the missed curvature paper. |
| arXiv API, recent titles | `(ti:"model extraction" OR ti:"neural network extraction" OR ti:"parameter extraction" OR ti:"recovering neural" OR ti:"learning attention" OR ti:"learning multi-head" OR ti:"signature extraction" OR ti:"parameter recovery") AND lastUpdatedDate:[202609180000 TO 202610282359]`, max 150: all 14 returned titles/abstracts. |

The arXiv API also returned metadata for all **30 primary arXiv catalog IDs**, checked for version/title changes. Of **29 primary/alias IACR metadata requests**, 19 succeeded and 10 hit HTTP 429. Rate-limited: 2026/1678, 848, 1943, 2127, 2097, 2095, 2061, 2161, 2628 and 2024/1870. Search pages still exposed their titles/latest-update dates, but no fresh full-version review is claimed. Current RNN PDF requests, plain and `?download=1`, returned HTTP 403. / 部分单篇页限流，RNN PDF 被拒；搜索摘要与历史指纹不冒充本次全文核查。

Examples excluded after primary-result title/abstract screening:

- [ePrint 2026/2499](https://eprint.iacr.org/2026/2499) is private face recognition; [2026/2358](https://eprint.iacr.org/2026/2358) is DNN-assisted cryptographic side-channel analysis. Neither extracts neural-network parameters.
- [ePrint 2026/1989](https://eprint.iacr.org/2026/1989) concerns watermark geometry; [2026/785](https://eprint.iacr.org/2026/785) concerns LowMC cryptanalysis, not neuron-signature recovery in this line.
- Recent [query-monitoring limits](https://arxiv.org/abs/2610.13083) and the [text-only LLM defense benchmark](https://arxiv.org/abs/2610.00839) concern surrogate distillation. [Contextual linear optimization](https://arxiv.org/abs/2610.29918) studies a different decision/model class. Their abstracts do not establish a specific cryptanalytic neural-parameter contribution; no core attack entries were inferred.

This is targeted monitoring, not a systematic review or proof of absence. Older audits retain their original counts. Vocabulary, indexing delays and access limits can hide work; affected sources remain eligible for later checks.

## Identity and change decisions / 去重与变更判定

Compared relevant candidates against all 54 baseline records and prior monitoring documents using DOI/resolver URLs, version-independent archive IDs, normalized titles, canonical URLs, aliases and author/title combinations. Former titles now also participate in automated validation, with a regression case for a differently titled duplicate.

| Candidate | Decision and primary evidence |
|---|---|
| [arXiv:2608.28843](https://arxiv.org/abs/2608.28843), archive DOI `10.48550/arXiv.2608.28843` | **Add one work**, existing attention/GLU-block category. No identifier/title/author/alias collision in catalog or previous monitoring records. Submitted August 28; v2 September 16. Archive DOI is not peer review. |
| [Journal DOI 10.1007/s00145-026-09586-5](https://link.springer.com/article/10.1007/s00145-026-09586-5) | **Update ePrint 2024/1580**, also arXiv:2410.05750. Same five authors and extended-version lineage; publisher title has a hyphen and omits “Extended Version.” Published October 1, 2026; *Journal of Cryptology* 39, article 32. Add DOI/alias/status, not a paper or newly verified algorithmic revision. |
| [ePrint 2026/168](https://eprint.iacr.org/2026/168) | **Correct title in place** to *Beyond Feedforward Networks: Cryptanalytic Extraction of RNNs*. Same eight authors, identifier and September 18 revision date. Preserve former title *Cryptanalytic Extraction of Recurrent Neural Network Models*. Metadata correction, not a substantive new revision. |
| ePrint 2026/2628; arXiv:2610.33671 | Already cataloged with alias and privileged-access caveats. No addition. |
| ePrint 2026/2097, 2095, 2061, 2161 | Existing aliases of hard-label end-to-end, unknown-architecture MLP, Normal Alignment and unknown-architecture CNN respectively. No additions. |
| ePrint 2026/2127 and 2026/1025 | Withdrawals already recorded. Retain historical claims/fingerprints; no repeated status update. |

The journal publisher verifies Nicholas Carlini (Google DeepMind, London), Jorge Chávez-Saab, Anna Hambitzer and Francisco Rodríguez-Henríquez (Cryptography Research Center, Technology Innovation Institute, Abu Dhabi), and Adi Shamir (Weizmann Institute, Rehovot). Publisher full text is subscription-gated; the reviewed 48-page ePrint comparison/fingerprint is retained, not represented as the journal PDF. The RNN record also retains its reviewed-copy date/fingerprint; current-title evidence is separate. / 发表状态及题名在原条目更新，归档全文证据不改称出版社或当前 PDF。

## New work: verified scope / 新条目的核验范围

**Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks**, Munawar Hasan (NIST and Michigan Technological University) and Apostol Vassilev (NIST), as shown on [v2 PDF p.1](https://arxiv.org/pdf/2608.28843v2). No venue beyond the preprint was verified.

The paper queries a **known, post-LayerNorm GELU/SiLU FFN branch** at chosen representation-space inputs and receives full vector outputs (§3, pp.4–6). Shared finite-difference Hessians expose normalized W1 directions **up to sign/permutation**; scales, oriented signs, biases and W2 are not recovered at that stage. Local identifiability is conditional on a restricted-Jacobian condition; nonconvex optimization has no global recovery guarantee (§4–5).

At `d=k=64, m=128, P=1, T=16`, shared stencils cost **8,193 full-vector branch calls**; optional fitting adds **12,000**, giving **20,193** (§5.1 Eq.(20), §6 Eq.(26)). Table 2 (p.18), across three trained victims per activation, reports mean direction alignment **0.9187 / 0.9402** and classifier agreement **92.81% / 94.97%** for GELU/SiLU. Full mean±SD metrics and separate stage budgets are in the [architecture addendum](comparisons/architecture.zh.md) and structured comparison.

Classifier evaluation replaces **one FFN while retaining all other victim parameters**, with additional access to natural branch inputs. Testing blocks separately does not establish their composition or full Transformer extraction. Sampled fidelity is not mathematical equivalence or recovery of all original parameters. Exact-Hessian/ground-truth diagnostics are privileged evaluation, distinct from the finite-difference attack. Gated/SwiGLU extensions remain future work (§7).

Table 8 (p.22) on one GELU target restores alignment to **0.9188 / 0.9081** under four-decimal rounding / Gaussian noise SD `1e-4` at `h=0.30`; l fresh step trials cost **l*8193** calls. This is not a universal defeat of defenses. Numeric dtype is not explicitly reported in the manuscript. Hardware/settings do not establish wall-clock runtime; independent stage arithmetic/runtime fields are **NR**, not zero. / 模块方向、拟合替换、原参数与全网恢复分开；结构、拟合、自适应试探及离线优化开销分别记述。

## PDF and code provenance / PDF 与代码来源

Downloaded actual [arXiv v2 PDF](https://arxiv.org/pdf/2608.28843v2), verified `%PDF-`, first-page identity, all pages' text parsing, raw byte count and SHA-256:

| Copy | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| arXiv:2608.28843v2 | 25 | 1188439 | `8ee0b4ae84a3e960bdd4d6208d6d01dc4e4d18c0a7b2925869e64b302dcfd6d2` |

PDF p.1 footnote 1 links [mhasan08/curvature-cryptanalysis](https://github.com/mhasan08/curvature-cryptanalysis). Inspected tree, README, dependency metadata, [MIT license](https://github.com/mhasan08/curvature-cryptanalysis/blob/2d9dd4f2bf1e8ca2939794ef1f3b8cdb93ea5534/LICENSE) and [optimized documentation](https://github.com/mhasan08/curvature-cryptanalysis/blob/2d9dd4f2bf1e8ca2939794ef1f3b8cdb93ea5534/optimized/README.txt) at **`2d9dd4f2bf1e8ca2939794ef1f3b8cdb93ea5534`**. Root retains separate-stencil code; `optimized/` documents shared stencils. README opening numbers differ from its detailed tables, so manuscript v2 Table 2 supplies cited results. The tree lists checkpoints/results, which were not collected or executed; the README states that the victim-training script is not supplied.

Added one fixed gitlink and manifest using the existing pointer workflow. No upstream code, dependency, model or data was executed/installed/collected; no results were reproduced. No third-party PDF is vendored. Previous code audits and PDF locators remain historical. `data/version-audit.json` records publication/title evidence with affected fingerprints unchanged.

## Repository checks / 仓库检查

Kept schema version 1 and taxonomy. Merged reviewed group inputs; regenerated bilingual catalog/BibTeX, comparisons and code indexes. Release workflow: both renderers' render/check modes, `validate_catalog.py`, `validate_comparisons.py --strict`, `test_collection.py`, new source's offline collector preview, and `git diff --check`. Coverage: **55 papers, 27 code sources, 22 pinned gitlinks**. The full historical `validate_catalog.py --ref` corpus is unavailable; only the new PDF above was freshly fingerprinted. / 不声称重验所有历史 PDF 或复现实验。
