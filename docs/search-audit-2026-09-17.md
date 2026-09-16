# Literature and Code Audit

Cutoff: **2026-09-17**, Asia/Shanghai. Main collection performed September 16, with final source/code checks September 17.

## Coverage

- **48 unique works**, up from 23 entries in the previous README: 25 additions to the public catalog.
- 13 primary categories. A paper is listed once; cross-cutting results are discussed in the progress note.
- Includes preprints, selected related identifiability/learning theory and stronger-oracle work, two surveys and one MIT course report. The 48 count is **not** a count of 48 core cryptanalytic attacks.
- Local reference synchronization: **21 new PDFs, 4 refreshed PDFs, 23 unchanged matched copies**. There are 49 local PDFs for 48 works because the historical ePrint 2020/107 and arXiv 2003.04884 copies are both retained. Prior replaced bytes were backed up, not discarded.
- The public repository links official PDFs rather than redistributing them. `data/papers.json` records reviewed-copy page counts, byte lengths and SHA-256 hashes; a later upstream revision can legitimately change these hashes.

## Retrieval Method

1. Checked IACR ePrint titles and annual listings across 2020-2026; followed relevant entries to their official abstract pages and PDFs. The [classic annual index](https://eprint-classic.github.io/2026.html) was a discovery aid, not the sole authority for claims.
2. Queried arXiv for `(all:cryptanalytic OR all:cryptanalytical) AND (all:extraction OR all:extracting)`: 15 returned results, including irrelevant cryptanalysis applications and cross-listed aliases.
3. Queried arXiv for `(ti:"model extraction" OR ti:"neural network extraction" OR ti:"parameter extraction" OR ti:"recovering neural" OR ti:"learning attention" OR ti:"learning multi-head") AND submittedDate:[202501010000 TO 202609162359]`: 72 returned records were screened.
4. Used a broader extraction/recovery/reconstruction/learning query as a discovery aid only. It exceeded the 150-result request and is **not** counted as an exhaustive screened query.
5. Chased foundational and recent-paper references for sign recovery, three-layer query learning, geometric structure recovery, Expand-and-Cluster, attention identifiability, physical leakage and LLM output-space recovery.
6. Performed a final September 17 web freshness check, including the official [unknown-architecture page](https://arxiv.org/abs/2609.14379). No additional publicly verifiable core paper was identified in that final pass. Indexing delays remain possible.
7. Read official metadata and extracted full PDF text. Checked PDF headers, full-page parsing, page counts, first-page identity and SHA-256. Inspected code mentions and PDF hyperlink annotations, then checked author-linked repositories.

This is broad manual curation, not a registered systematic review or proof that no paper was missed. Search wording can miss papers that use different terminology, older learning-theory results or very recent unindexed preprints. General surrogate distillation, watermark-only work, training-data extraction and unrelated parameter-estimation papers are outside the core scope. The related-theory and side-channel sections are selected context, not exhaustive surveys of those entire fields.

## Version and Title Deduplication

The catalog records known ePrint/arXiv aliases rather than counting them as new papers. Examples:

| Primary record | Alias / correction |
|---|---|
| arXiv:2003.04884 | ePrint 2020/107 |
| ePrint 2023/1526 | arXiv:2310.08708; EUROCRYPT 2024 |
| ePrint 2024/1403 | arXiv:2409.11646; ASIACRYPT 2024 |
| ePrint 2024/1580 | arXiv:2410.05750; EUROCRYPT 2025 extended version |
| ePrint 2024/1870 | arXiv:2411.10174; now titled *A Divide-and-Conquer Strategy for Hard-Label Extraction of Deep Neural Networks via Side-Channel Attacks*, TCHES 2026; formerly *A Hard-Label Cryptanalytic Extraction of Non-Fully Connected Deep Neural Networks using Side-Channel Attacks* |
| ePrint 2025/1868 | arXiv:2510.06692; CRYPTO 2026 |
| ePrint 2025/1970 | arXiv:2509.16620; ASIACRYPT 2025 |
| ePrint 2026/1164 | arXiv:2608.05736 |
| ePrint 2026/241 | arXiv:2608.08030; current title uses *Neural Networks* |
| ePrint 2026/296 | Correct title: *Navigating the Deep: End-to-End Extraction on Deep Neural Networks* |

Additional title notes: arXiv:2105.09673 retains the archive's grammatical title variant; its ICLR 2023 title uses *Extracting a Three-Layer ReLU Network*. arXiv:1810.09076 is the earlier *CSI Neural Network* title; the USENIX 2019 publication is *CSI NN: Reverse Engineering of Neural Network Architectures Through Electromagnetic Side Channel*. These are not extra papers.

BibTeX is deliberately archive-oriented (`@misc`), with publication status in `note`. Archive year and publication year are not silently conflated. No unverified proceedings pages are fabricated. The PDF linked for a published paper may remain its public preprint layout.

## Code Status Findings

| Paper | Verified state on 2026-09-17 |
|---|---|
| Geometric Critical Point Screening | Correct [official URL](https://github.com/1983321048/Geometric-Critical-Point-Screening) is accessible; previous URL missed a hyphen. |
| Max-pooling CNN, ePrint 2026/464 | PDF p.28 links [official code](https://github.com/PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling); accessible. |
| Algebraic max-pooling, ePrint 2026/241 | PDF p.5 links [this repository](https://github.com/czr-eric/Algebraic-Attack-on-CNN); GitHub returned 404. |
| Cross-layer/polynomiality, ePrint 2025/1868 | PDF pp.1/5 link [this repository](https://github.com/ECSIS-lab/hard-label-cross-layer-extraction); GitHub returned 404. |
| Finite precision, ePrint 2026/1943 | PDF p.3 links [this repository](https://github.com/CryptAnalystDesigner/Finite-Precision-Feasibility-of-Cryptanalytic-Model-Extraction); GitHub returned 404. |
| CNN, ePrint 2026/139 | Anonymous file-list endpoint returns 410 `repository_expired`; the ordinary SPA landing page is not adequate availability evidence. |
| End-to-end CNN, ePrint 2026/902 | Official abstract links [anonymous attachment](https://anonymous.4open.science/r/cnn_hard_label_extraction-83F4); file-list endpoint returns 200 with source files. |
| PPML, ePrint 2026/848 | PDF p.23 links [anonymous attachment](https://anonymous.4open.science/r/PPML_Model_Extraction_Attack); file-list endpoint returns 200 with source files. |
| ASV, ePrint 2026/1164 | PDF p.4 contains `XXX` for the code URL; marked announced, not available. |
| MIT rounding report | Supplementary code mentioned, but usable public URL not located. |
| Stealing Part of a Production LM | [Official supplementary repository](https://github.com/dpaleka/stealing-part-lm-supplementary), not a complete turnkey extraction implementation. |
| Data augmentation | [Author's extension fork](https://github.com/alexl4123/expand-and-cluster), distinct from the [original Expand-and-Cluster implementation](https://github.com/flavio-martinelli/expand-and-cluster). |

Other linked GitHub repositories were checked for accessibility and correspondence to the paper. Related dependencies, unrelated implementations and a paper's references to other projects were not relabeled as its official code. No third-party attack code was executed. HTTP 404 does not distinguish private, unreleased, renamed and removed repositories.

## Recheck

```console
python scripts/render_catalog.py --check
```

This validates catalog structure and generated-file consistency, not live network availability or scientific correctness. Future additions should repeat source, version and code checks rather than inheriting old availability labels.
