<p align="center">
  <img src="assets/taxonomy.png" alt="Neural-network and block-cipher structural analogy" width="100%">
</p>

# Awesome Cryptanalytic Extraction

A curated bibliography of **cryptanalytic neural-network extraction**, structural and parameter recovery, reproducibility code, limitations, and defenses.

[中文版](README_zh-CN.md) · [September progress](docs/progress-2026-09.md) · [October progress](docs/progress-2026-10.md) · [Search audit](docs/search-audit-2026-10-28.md) · [BibTeX](bib/cryptanalytic_extraction.bib) · [Machine-readable catalog](data/papers.json) · [Stage comparisons](docs/comparison_en.md) · [Original code collection](code/README.md)

**Updated {{DATE}} · {{COUNT}} unique works · 13 categories.** Includes preprints, selected adjacent theory, two surveys, and one explicitly labeled course report. This is a broad, source-checked collection, not a claim of exhaustive coverage of all model stealing.

## Recent Developments

**Source status:** ePrint 2026/1025 was withdrawn on September 19 and ePrint 2026/2127 on October 1. Both are retained as historical records. The comparison covers all {{COUNT}} records and separates stage costs, oracle assumptions and experimental scope.

- **October 28 reconciliation:** added [Beyond Scalar Probes](https://arxiv.org/abs/2609.35487) for vector-output signature estimation and [Extraction meets Distillation](https://arxiv.org/abs/2610.33671) for assisted partial recovery plus reconstruction. The latter uses privileged internal information; neither establishes a new complete black-box parameter attack. Added ePrint aliases [2097](https://eprint.iacr.org/2026/2097), [2095](https://eprint.iacr.org/2026/2095), and [2061](https://eprint.iacr.org/2026/2061) to existing records, and clarified the unknown-architecture MLP v2. [Primary-source audit](docs/search-audit-2026-10-28.md).

- **September 30 update:** added three preprints on [limited architecture knowledge (withdrawn October 1)](https://eprint.iacr.org/2026/2127), [end-to-end hard-label extraction](https://arxiv.org/abs/2609.21941), and [unknown-architecture CNNs](https://arxiv.org/abs/2609.27427). Existing arXiv:2609.14379 is retained once; ePrint 2026/2161 is an alias, not another work. [Source audit and limitations](docs/update-2026-09-30.md).

- **September 18 update:** added [Normal Alignment](https://arxiv.org/abs/2609.18751) for hard-label sign recovery and refreshed [ePrint 2026/848](https://eprint.iacr.org/2026/848), now titled *Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning*. This is one new work plus one major revision. [Results, code status and limits](docs/update-2026-09-18.md).

- **Unknown architecture:** [guess-and-determine extraction](https://arxiv.org/abs/2609.14379) and the historical [limited-knowledge proposal (withdrawn)](https://eprint.iacr.org/2026/2127) address ReLU fully connected networks under different priors. [CNN spatial geometry](https://arxiv.org/abs/2609.27427) extends architecture recovery to studied convolution/pooling networks, inheriting the parameter attack’s assumptions. These results do not establish arbitrary mixed-network or Transformer recovery.
- **Numerical feasibility:** [Finite-Precision Error Analysis](https://eprint.iacr.org/2026/1943) studies numerical error in cryptanalytic primitives. [Output Rounding](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) evaluates an adapted attack on rounded outputs. Neither supports a universal precision threshold for all networks.
- **Beyond ReLU MLPs:** the catalog now covers [softmax attention](https://eprint.iacr.org/2026/1678), [multi-head query learning](https://arxiv.org/abs/2608.03294), [isolated GLU blocks](https://arxiv.org/abs/2608.06631), RNNs, GNNs, CNN pooling and smooth activations. Block-level recovery is not full-LLM extraction.
- **Hard-label progress and limits:** [algebraic signatures](https://eprint.iacr.org/2026/1164) include max-pooling CNN experiments, while [cross-layer extraction and polynomiality analysis](https://eprint.iacr.org/2025/1868) expose important persistent/dead-neuron caveats. Signature recovery, sign recovery and end-to-end executable recovery remain different outcomes.

## Scope and Reading Guide

The cryptanalytic analogy treats weights as hidden parameters and inputs as chosen queries. Differential, geometric or algebraic leakage can expose more than ordinary test-set imitation. It is an analogy, not an assertion that a network is a secure cipher.

1. Start with **foundations**, then CRYPTO 2020, EUROCRYPT 2024 and the raw-output improvements.
2. Read **hard-label extraction** together with its partial-layer and polynomiality limitations.
3. Compare **CNN/pooling, activation, RNN/GNN and attention** results under their exact oracle assumptions.
4. Read **finite precision and defenses** before treating an idealized recovery theorem as a deployable attack.
5. Use **related theory, partial LLM extraction and side-channel work** as explicitly separated context, not interchangeable threat models.

| Axis | Distinctions to retain |
|---|---|
| Oracle | Raw real-valued outputs; probabilities/top-k scores; top-1 label only; explanations; physical leakage |
| Recovery | Architecture; signature up to scale/sign; oriented parameters; canonical equivalent function; partial block; whole executable model |
| Assumptions | Known structure; generic position; identifiable neurons; chosen continuous inputs; finite precision; access to intermediate blocks |
| Evidence | Theorem under stated assumptions; query count; wall-clock time; sampled fidelity; parameter error; certified equivalence |

## Catalog Conventions

**¹ Year** is the archive/report year; venue year is shown separately. Revised titles and cross-listed ePrint/arXiv versions count once. Linked PDFs are archive copies, not necessarily publisher-final layouts. Versions, page counts, byte sizes and SHA-256 hashes of the reviewed PDFs are in the JSON catalog. Fingerprints identify those exact copies, including retained historical PDFs; verifying an alias or its revision date does not verify that archive’s PDF bytes. Alias links in a row do not add works.

**² Code** means an author/paper-linked repository unless labeled otherwise. `404` means unavailable at checking time, not proof of deletion; anonymous `410` means the service reports expiration. Supplementary code, author forks and reading resources are distinguished from complete attack implementations. `Not located` means no usable author-linked URL was found, not that no code exists. Accessibility checks are **not** execution or reproduction of results.

{{CATALOG}}

## Open Questions After These Results

- **Unknown general architectures:** studied ReLU fully connected and convolution/pooling models now have architecture-recovery results. Mixed operators, residual paths, weak size priors and composition still require separate evidence.
- **Hard-label max-pooling:** no longer an empty category. Robust full-layer/sign/bias recovery, winner switches and event observability should be evaluated beyond small signature-recovery demonstrations.
- **Practical precision and cost:** relate numerical stability to query budgets, conditioning, rate limits, abstentions and probability truncation; do not equate real-arithmetic polynomiality with cheap extraction.
- **Identifiability:** report dead/persistent neurons, equivalent parameterizations and canonicalization explicitly. A failure to recover one parameterization is not automatically security.
- **Adaptive defenses:** evaluate training regularization and output modifications against adapted attacks, with utility loss and attack budget fixed. Small-model experiments do not establish universal security.
- **Composition:** recovering attention, output projections or isolated GLU blocks does not establish recovery of their composition through an ordinary token API.

## Contributing and Maintenance

Edit [data/papers.json](data/papers.json), including official title/authors, source, venue/status, oracle, scope limits, code provenance and PDF version fingerprint. Edit the [English template](docs/readme_en.template.md) or [Chinese template](docs/readme_zh.template.md) for prose, then run:

```console
python scripts/render_catalog.py
python scripts/render_catalog.py --check
python scripts/validate_catalog.py
python scripts/render_comparisons.py
python scripts/validate_comparisons.py --strict
python scripts/test_collection.py
```

Keep preprints and course reports visibly labeled. Prefer primary sources and author-linked code; do not vendor third-party implementations or copyrighted PDFs into this repository. A local `ref` corpus can use the filenames, official PDF URLs and hashes in the catalog. No code release is implied by a paper's promise to publish it.

## Disclaimer

For academic research and defensive analysis on authorized models and systems. Listing a paper does not independently validate its claims or endorse an attack against a third-party service.
