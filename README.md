<p align="center">
  <img src="assets/taxonomy.png" alt="Neural-network and block-cipher structural analogy" width="100%">
</p>

# Awesome Cryptanalytic Extraction

A curated bibliography of **cryptanalytic neural-network extraction**, structural and parameter recovery, reproducibility code, limitations, and defenses.

[中文版](README_zh-CN.md) · [September progress](docs/progress-2026-09.md) · [Search audit](docs/search-audit-2026-09-17.md) · [BibTeX](bib/cryptanalytic_extraction.bib) · [Machine-readable catalog](data/papers.json)

**Updated 2026-09-18 · 49 unique works · 13 categories.** Includes preprints, selected adjacent theory, two surveys, and one explicitly labeled course report. This is a broad, source-checked collection, not a claim of exhaustive coverage of all model stealing.

## Recent Developments

- **September 18 update:** added [Normal Alignment](https://arxiv.org/abs/2609.18751) for hard-label sign recovery and refreshed [ePrint 2026/848](https://eprint.iacr.org/2026/848), now titled *Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning*. This is one new work plus one major revision. [Results, code status and limits](docs/update-2026-09-18.md).

- **Unknown architecture:** September's [guess-and-determine extraction](https://arxiv.org/abs/2609.14379) jointly recovers ReLU fully connected architectures and parameters. This does not establish arbitrary CNN/Transformer extraction; earlier [geometric reverse engineering](https://arxiv.org/abs/1910.00744) is included for context.
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

**¹ Year** is the archive/report year; venue year is shown separately. Revised titles and cross-listed ePrint/arXiv versions count once. Linked PDFs are archive copies, not necessarily publisher-final layouts. Versions, page counts and SHA-256 hashes of the reviewed PDFs are in the JSON catalog.

**² Code** means an author/paper-linked repository unless labeled otherwise. `404` means unavailable at checking time, not proof of deletion; anonymous `410` means the service reports expiration. Supplementary code, author forks and reading resources are distinguished from complete attack implementations. `Not located` means no usable author-linked URL was found, not that no code exists. Accessibility checks are **not** execution or reproduction of results.

## Paper Catalog

### Foundations (3)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2019 | [Reverse-Engineering Deep ReLU Networks](https://arxiv.org/abs/1910.00744) · [PDF](https://arxiv.org/pdf/1910.00744) | ICML 2020 | Real-valued queries<br>Deep ReLU | Boundary geometry recovers structure and parameters up to network symmetries under assumptions. | Not located |
| 2019 | [High Accuracy and High Fidelity Extraction of Neural Networks](https://arxiv.org/abs/1909.01838) · [PDF](https://arxiv.org/pdf/1909.01838) | USENIX Security 2020 | Raw outputs / prediction queries<br>Shallow and deep NN | Separates accuracy from fidelity; functional-equivalent shallow recovery and hybrid attacks. | Not located |
| 2016 | [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) · [PDF](https://arxiv.org/pdf/1609.02943) | USENIX Security 2016 | Prediction scores / labels<br>Classical ML / shallow NN | Equation-solving and early API extraction; not general deep exact recovery. | [Official](https://github.com/ftramer/Steal-ML) |

### Raw-Output ReLU Extraction (6)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Navigating the Deep: End-to-End Extraction on Deep Neural Networks](https://eprint.iacr.org/2026/296) · [PDF](https://eprint.iacr.org/2026/296.pdf) | EUROCRYPT 2026 | Raw outputs<br>Deep ReLU MLP | End-to-end extraction with techniques for deeper-layer recovery. | [Official](https://github.com/PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction) |
| 2026 | [Geometric Critical Point Screening: Clustering-Free Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2026/1025) · [PDF](https://eprint.iacr.org/2026/1025.pdf) | Preprint | Raw outputs<br>ReLU networks | Geometric critical-point screening avoids the clustering stage. | [Official](https://github.com/1983321048/Geometric-Critical-Point-Screening) |
| 2026 | [Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption](https://arxiv.org/abs/2609.14379) · [PDF](https://arxiv.org/pdf/2609.14379) | Preprint | Raw outputs; architecture unknown<br>ReLU fully connected networks | Guess-and-determine jointly recovers architecture and parameters; not arbitrary CNN/Transformer recovery. | Not located |
| 2024 | [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011) · [PDF](https://arxiv.org/pdf/2406.10011) | NeurIPS 2024 | Raw outputs<br>ReLU MLP | Practical sign-recovery improvements; distinguish runtime from query count. | [Official](https://github.com/hannafoe/cryptanalytical-extraction) |
| 2023 | [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526) · [PDF](https://eprint.iacr.org/2023/1526.pdf) | EUROCRYPT 2024 | Raw outputs<br>ReLU MLP | Polynomial-time sign recovery improves the original cryptanalytic pipeline. | [Official](https://github.com/Crypto-TII/deti) |
| 2020 | [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) · [PDF](https://arxiv.org/pdf/2003.04884) | CRYPTO 2020 | Raw outputs<br>ReLU MLP | Differential critical-point extraction; signatures, signs and final parameter recovery. | [Official](https://github.com/google-research/cryptanalytic-model-extraction) |

### Hard-Label Extraction (6)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](https://eprint.iacr.org/2026/1164) · [PDF](https://eprint.iacr.org/2026/1164.pdf) | Preprint | Top-1 label only<br>FCNN / max-pooling CNN | Algebraic signature vectors replace SVD-heavy clustering; experiments include early FC layers and LeNet-5 signatures, not universal full recovery. | Announced; placeholder URL |
| 2026 | [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751) · [PDF](https://arxiv.org/pdf/2609.18751) | Preprint | Top-1 label only; sign-recovery stage<br>Deep ReLU MLP | Normal-signature alignment plus eSOE recovers 512/512 and 320/320 signs in the reported models; sign recovery, not a demonstrated complete end-to-end attack. | Announced; placeholder URL |
| 2025 | [Is the Hard-Label Cryptanalytic Model Extraction Really Polynomial?](https://eprint.iacr.org/2025/1868) · [PDF](https://eprint.iacr.org/2025/1868.pdf) | CRYPTO 2026 | Top-1 label only<br>ReLU MLP | Persistent/dead neurons challenge polynomiality claims; cross-layer extraction addresses limitations. | [Paper-linked; 404](https://github.com/ECSIS-lab/hard-label-cross-layer-extraction) |
| 2025 | [Extracting Some Layers of Deep Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2025/1118) · [PDF](https://eprint.iacr.org/2025/1118.pdf) | LATINCRYPT 2025 | Top-1 label only<br>ReLU MLP | Partial/output-layer recovery under structural conditions, not unrestricted end-to-end extraction. | [Official](https://github.com/deividafonso281/hard-label-contract-output) |
| 2024 | [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) · [PDF](https://eprint.iacr.org/2024/1580.pdf) | EUROCRYPT 2025; extended version | Top-1 label only<br>Deep ReLU MLP | Dual points, signatures and signs; recovery depends on structural and geometric conditions. | [Official](https://github.com/Jchavezsaab/hard-label-dnn-extraction) |
| 2024 | [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403) · [PDF](https://eprint.iacr.org/2024/1403.pdf) | ASIACRYPT 2024 | Top-1 label only<br>ReLU MLP | Label-only cryptanalytic extraction from decision-boundary geometry. | [Official](https://github.com/AI-Lab-Y/NN_cryptanalytic_extraction) |

### CNN and Pooling (4)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [End-to-End Polynomial-Time Cryptanalytic Extraction of Convolutional Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/902) · [PDF](https://eprint.iacr.org/2026/902.pdf) | Preprint | Top-1 label only<br>Average-pooling CNN; known architecture | End-to-end pipeline; retained-candidate and structural assumptions remain material. | [Anonymous attachment](https://anonymous.4open.science/r/cnn_hard_label_extraction-83F4) |
| 2026 | [Model Extraction of Convolutional Neural Networks with Max-Pooling](https://eprint.iacr.org/2026/464) · [PDF](https://eprint.iacr.org/2026/464.pdf) | ToSC 2026 | Raw outputs<br>Max-pooling CNN | Pooling-aware extraction and receptive-field structure. | [Official](https://github.com/PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling) |
| 2026 | [Algebraic Attack on Convolutional Neural Networks with Max Pooling](https://eprint.iacr.org/2026/241) · [PDF](https://eprint.iacr.org/2026/241.pdf) | CRYPTO 2026 | Raw outputs<br>Max-pooling CNN | Algebraic extraction handles pooling switches; raw-output results do not automatically transfer to label-only access. | [Paper-linked; 404](https://github.com/czr-eric/Algebraic-Attack-on-CNN) |
| 2026 | [Cryptanalytic Extraction of Convolutional Neural Networks](https://eprint.iacr.org/2026/139) · [PDF](https://eprint.iacr.org/2026/139.pdf) | ACISP 2026 | Top-1 label only<br>Average-pooling CNN | Uses convolutional structure for kernel recovery. | [Expired; 410](https://anonymous.4open.science/r/cnn-extraction-93C4) |

### Activation Extensions (4)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Deep Neural Networks with Non-Linear Activations](https://eprint.iacr.org/2026/253) · [PDF](https://eprint.iacr.org/2026/253.pdf) | CRYPTO 2026 | Raw outputs<br>Smooth/non-linear activations | Higher-order/near-linear geometry enables recovery for studied non-linear activations; not every smooth function. | [Official](https://github.com/mstealercryptocrypto-ops/mod_stealer26) |
| 2026 | [Cryptanalytic Extraction of Neural Networks with Various Activation Functions](https://eprint.iacr.org/2026/178) · [PDF](https://eprint.iacr.org/2026/178.pdf) | ToSC 2026 | Raw outputs / hard labels (variant-dependent)<br>PReLU / LeakyReLU / HardTanh / Step | Extends extraction to several activation families; oracle assumptions differ by variant. | [Official](https://github.com/qixiaokang1-stack/cryptanalytic-model-various-functions) |
| 2026 | [Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2026/1066) · [PDF](https://eprint.iacr.org/2026/1066.pdf) | Preprint | Top-1 label only<br>PReLU | Broadens allowable slopes and architectures for hard-label extraction. | Not located |
| 2025 | [Delving into Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2025/1970) · [PDF](https://eprint.iacr.org/2025/1970.pdf) | ASIACRYPT 2025 | Raw outputs / top-m probabilities<br>PReLU | Recovers PReLU parameters under stated conditions; not a label-only result. | [Official](https://github.com/AI-Lab-Y/Extracting_PReLU_NN) |

### RNN and GNN (2)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/719) · [PDF](https://eprint.iacr.org/2026/719.pdf) | Preprint | Top-1 label only<br>Message-passing GNN | Graph/message-passing structure supports extraction under the stated model. | [Official](https://github.com/springli07/GNN_MP_CEA) |
| 2026 | [Cryptanalytic Extraction of Recurrent Neural Network Models](https://eprint.iacr.org/2026/168) · [PDF](https://eprint.iacr.org/2026/168.pdf) | Preprint | Raw outputs / top-1 labels<br>RNN | Exploits recurrence; long unrollings share weights and are not independent deep layers. | Not located |

### Attention and GLU Blocks (4)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Multi-Head Softmax Attention Models](https://eprint.iacr.org/2026/1678) · [PDF](https://eprint.iacr.org/2026/1678.pdf) | Preprint | Raw outputs / chosen continuous inputs<br>Multi-head softmax attention | Recovers a canonical equivalent representation; Q/K/V factors have gauge ambiguity. | Not located |
| 2026 | [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631) · [PDF](https://arxiv.org/pdf/2608.06631) | Preprint | Direct queries to an isolated block<br>Bias-free GLU FFN | Antipodal separation for isolated blocks; not extraction of a complete LLM through its token API. | Not located |
| 2026 | [Provably Learning Multi-Head Attention with Queries](https://arxiv.org/abs/2608.03294) · [PDF](https://arxiv.org/pdf/2608.03294) | Preprint | Chosen real-valued queries<br>Multi-head attention / restricted one-layer Transformer | Canonical head recovery; additional assumptions for the Transformer extension. | Not located |
| 2026 | [Provably Learning Attention with Queries](https://arxiv.org/abs/2601.16873) · [PDF](https://arxiv.org/pdf/2601.16873) | ICML 2026 | Chosen real-valued queries<br>Attention | Query-learning guarantees under attention-model assumptions. | Not located |

### Partial LLM and Output-Space Extraction (2)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2024 | [Logits of API-Protected LLMs Leak Proprietary Information](https://arxiv.org/abs/2403.09539) · [PDF](https://arxiv.org/pdf/2403.09539) | COLM 2024 | Logprobs / restricted API<br>LLM output subspace | Softmax bottleneck reveals hidden dimension and output-space information, not full-network recovery. | Not located |
| 2024 | [Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) · [PDF](https://arxiv.org/pdf/2403.06634) | ICML 2024 | Restricted logprobs / logit-bias API<br>LLM output projection | Partial projection recovery up to symmetries, not all model weights; released code is supplementary. | [Official supplementary](https://github.com/dpaleka/stealing-part-lm-supplementary) |

### PPML and Stronger Side-Channel Oracles (5)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning](https://eprint.iacr.org/2026/848) · [PDF](https://eprint.iacr.org/2026/848.pdf) | Preprint | Finite-ring/fixed-point inference; variants include top-1 + probability<br>PPML neural inference | Revised Sep 17: multi-point projection aggregation for expansive networks and optimal sign probes; reports 30%-74% fewer sign-recovery queries than Neuron Wiggle on its benchmark, not a universal reduction or encryption break. | [Anonymous attachment](https://anonymous.4open.science/r/PPML_Model_Extraction_Attack) |
| 2025 | [Activation Functions Considered Harmful: Recovering Neural Network Weights through Controlled Channels](https://arxiv.org/abs/2503.19142) · [PDF](https://arxiv.org/pdf/2503.19142) | Preprint | SGX controlled channels<br>DNN activation implementation | Activation-access leakage supports weight recovery; first-layer and deeper-layer outcomes differ. | [Official](https://github.com/heavyimage/afch_paper) |
| 2024 | [A Divide-and-Conquer Strategy for Hard-Label Extraction of Deep Neural Networks via Side-Channel Attacks](https://eprint.iacr.org/2024/1870) · [PDF](https://eprint.iacr.org/2024/1870.pdf) | TCHES 2026; revised title | Top-1 labels + side channel<br>Deep NN / non-FC components | Divide-and-conquer with physical leakage; stronger than black-box label access. | [Official](https://github.com/bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN) |
| 2020 | [SNIFF: Reverse Engineering of Neural Networks with Fault Attacks](https://arxiv.org/abs/2002.11021) · [PDF](https://arxiv.org/pdf/2002.11021) | Preprint / IEEE Transactions on Reliability | Fault injection + outputs<br>Neural networks | Sign-bit fault attacks use a stronger attacker than ordinary API queries. | Not located |
| 2018 | [CSI Neural Network: Using Side-channels to Recover Your Artificial Neural Network Information](https://arxiv.org/abs/1810.09076) · [PDF](https://arxiv.org/pdf/1810.09076) | USENIX Security 2019; published title differs | Power / EM side channels<br>Embedded neural networks | Architecture/parameter leakage via physical observations; selected historical context. | Not located |

### Finite Precision and Feasibility (1)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Finite-Precision Error Analysis of Cryptanalytic Model Extraction](https://eprint.iacr.org/2026/1943) · [PDF](https://eprint.iacr.org/2026/1943.pdf) | Preprint; ASIACRYPT 2026 acceptance author-listed | Finite-precision raw outputs<br>Cryptanalytic signature recovery | Quantifies numerical error in extraction primitives; neither universal impossibility nor a proven generic defense. | [Paper-linked; 404](https://github.com/CryptAnalystDesigner/Finite-Precision-Feasibility-of-Cryptanalytic-Model-Extraction) |

### Defenses and Adaptive Evaluations (2)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2026 | [Output Rounding Is Not a Free Defense Against Cryptanalytic Neural Network Extraction](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) · [PDF](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | MIT 6.5610 Spring 2026 course report | Rounded raw outputs<br>Small ReLU MLP | Step-spacing adapts to rounding; empirical small-model evidence, not a universal security threshold. | Supplement mentioned; URL not located |
| 2025 | [Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks](https://arxiv.org/abs/2509.16546) · [PDF](https://arxiv.org/pdf/2509.16546) | NeurIPS 2025 | Defense against parameter extraction<br>ReLU MLP | Training-time neuron-similarity regularization; evaluate against adapted attacks. | [Official](https://github.com/anonymous-123-code/anonymouscode) |

### Related Identifiability and Learning Theory (8)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2025 | [Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries](https://arxiv.org/abs/2511.20312) · [PDF](https://arxiv.org/pdf/2511.20312) | UniReps 2025 workshop | Input-output queries<br>Teacher-student parameter recovery | Data augmentation improves Expand-and-Cluster; linked code is the authors' extension fork. | [Author extension fork](https://github.com/alexl4123/expand-and-cluster) |
| 2024 | [Model Stealing for Any Low-Rank Language Model](https://arxiv.org/abs/2411.07536) · [PDF](https://arxiv.org/pdf/2411.07536) | Preprint | Conditional queries<br>Low-rank sequence distributions / HMM | Learns low-rank output distributions, not arbitrary Transformer weights. | Not located |
| 2024 | [Provably learning a multi-head attention layer](https://arxiv.org/abs/2402.04084) · [PDF](https://arxiv.org/pdf/2402.04084) | STOC 2025 | Random examples (not chosen queries)<br>Multi-head attention | Learning theory under nondegeneracy; not a practical full-model API extraction demonstration. | Not located |
| 2023 | [Reverse Engineering Deep ReLU Networks An Optimization-based Algorithm](https://arxiv.org/abs/2312.04675) · [PDF](https://arxiv.org/pdf/2312.04675) | Preprint | Input-output queries<br>Deep ReLU | Optimization-based reverse engineering; distinguish proposed guarantees from demonstrated scalability. | Not located |
| 2023 | [Expand-and-Cluster: Parameter Recovery of Neural Networks](https://arxiv.org/abs/2304.12794) · [PDF](https://arxiv.org/pdf/2304.12794) | ICML 2024 | Input-output samples<br>Neural networks | Overparameterized students plus clustering recover parameters; related to, but not the same as, differential extraction. | [Official](https://github.com/flavio-martinelli/expand-and-cluster) |
| 2022 | [Finite Sample Identification of Wide Shallow Neural Networks with Biases](https://arxiv.org/abs/2211.04589) · [PDF](https://arxiv.org/pdf/2211.04589) | Preprint | Finite input-output samples / queries<br>Wide shallow networks with biases | Identification of directions and biases under model and sampling conditions. | Not located |
| 2021 | [An Exact Poly-Time Membership-Queries Algorithm for Extraction a three-Layer ReLU Network](https://arxiv.org/abs/2105.09673) · [PDF](https://arxiv.org/pdf/2105.09673) | ICLR 2023 | Membership / real-valued queries<br>Three-layer ReLU | Exact polynomial-query recovery under depth/generic-position assumptions. | Not located |
| 2018 | [Model Reconstruction from Model Explanations](https://arxiv.org/abs/1807.05185) · [PDF](https://arxiv.org/pdf/1807.05185) | FAT* 2019 | Gradient/explanation oracle<br>Neural networks | Reconstruction with explanations uses a stronger oracle than ordinary predictions. | Not located |

### Surveys and Reading Resources (2)

| Year¹ | Paper and PDF | Venue / status | Oracle / architecture | Recovery target and limits | Code² |
|---|---|---|---|---|---|
| 2025 | [A Systematic Survey of Model Extraction Attacks and Defenses: State-of-the-Art and Perspectives](https://arxiv.org/abs/2508.15031) · [PDF](https://arxiv.org/pdf/2508.15031) | Preprint survey | Multiple<br>Multiple | Broad model-extraction survey; includes surrogate stealing outside this repository's core scope. | [Reading list, not attack code](https://github.com/kzhao5/ModelExtractionPapers) |
| 2025 | [A Survey on Model Extraction Attacks and Defenses for Large Language Models](https://arxiv.org/abs/2506.22521) · [PDF](https://arxiv.org/pdf/2506.22521) | Preprint survey | Multiple LLM APIs<br>LLM | Contextual survey of LLM extraction and defenses; not an exact-recovery attack. | [Reading list, not attack code](https://github.com/kzhao5/ModelExtractionPapers) |


## Open Questions After These Results

- **Unknown general architectures:** no longer untouched for ReLU fully connected models. Mixed operators, residual paths and weak prior knowledge still require separate evidence.
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
```

Keep preprints and course reports visibly labeled. Prefer primary sources and author-linked code; do not vendor third-party implementations or copyrighted PDFs into this repository. A local `ref` corpus can use the filenames, official PDF URLs and hashes in the catalog. No code release is implied by a paper's promise to publish it.

## Disclaimer

For academic research and defensive analysis on authorized models and systems. Listing a paper does not independently validate its claims or endorse an attack against a third-party service.
