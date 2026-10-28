# October progress / 十月进展

Reviewed **2026-10-28, Asia/Shanghai**, including a later monitoring follow-up. Catalog: **55 unique works, 13 categories**, including two retained withdrawn records. See the [follow-up source audit](search-audit-2026-10-28-followup.md), [earlier same-day reconciliation](search-audit-2026-10-28.md), [September progress](progress-2026-09.md) and [stage comparisons](comparison_en.md). / 补查后目录现有 55 篇、13 类；包含两条保留的已撤回历史记录。

## Smooth-FFN backfill and publication update / 光滑 FFN 补漏与发表更新

Added the previously missed August 28 / September 16 v2 preprint [Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks](https://arxiv.org/abs/2608.28843), by Munawar Hasan (NIST and Michigan Technological University) and Apostol Vassilev (NIST). It estimates the first-layer directions of a known GELU/SiLU FFN up to sign/permutation using direct post-LayerNorm branch queries. Shared vector stencils cost **8,193 structural queries** at input dimension 64; optional completion adds **12,000**, for **20,193 vector-output calls**. Table 2 reports mean direction alignments 0.9187 / 0.9402 and classifier agreements 92.81% / 94.97% for GELU / SiLU. The classifier tests replace one FFN while retaining all other victim parameters. Local identifiability is conditional; approximate directions and sampled agreement do not establish exact parameters or full Transformer extraction.

该文是补漏而非十月新发表。首层方向估计与后续拟合分别计费；完整分类器评价沿用其余原模型参数，不能称为全 Transformer 提取。三随机重启及自适应差分步长的额外开销也不能由单次模板预算消除。已核对 v2 的实际 PDF 字节及作者链接的 MIT 代码仓库，未执行或复现实验。

Existing [ePrint 2024/1580](https://eprint.iacr.org/2024/1580) is now [Journal of Cryptology 39, article 32](https://doi.org/10.1007/s00145-026-09586-5), published October 1. Same five authors and existing extended-version lineage: one publication-status update, not a new work or newly verified technical revision. The reviewed ePrint fingerprint remains unchanged. The existing RNN record also adopts the official title *Beyond Feedforward Networks: Cryptanalytic Extraction of RNNs*, retaining its former title and historical fingerprint; this metadata correction is not counted as a substantive new revision. / 正式发表更新与 RNN 题名更正均不增加论文数，未获取的当前 PDF 不补造指纹。

## Assisted recovery and reconstruction / 辅助恢复与重建

[Extraction meets Distillation](https://arxiv.org/abs/2610.33671), also [ePrint 2026/2628](https://eprint.iacr.org/2026/2628), combines partial direction recovery with sign search, output fitting and label-based refinement for ReLU/Leaky ReLU MLPs. The evaluated pipeline uses internal gradients, activations and true parameters (§3.4, Table 1); it belongs to the existing stronger-oracle systems category. A complete reconstructed classifier is not complete recovery of the victim's parameters, and subsequent label training does not make the earlier assisted extraction label-only.

该工作将部分方向恢复与符号搜索、输出层拟合及标签学习组合；原文披露使用梯度、隐藏激活及真实参数，因此归入现有更强预言机类别。重建出完整分类器不等于恢复全部原模型参数，后续仅用标签训练不能消除前期额外访问。

The paper distinguishes label requests from batch calls and privileged reads. Its seeded synthetic evaluations and CIFAR experiments use different settings; high synthetic agreement must not be merged with the lower CIFAR results into a composite success claim. The linked author repository is pinned as a source reference, with no project license verified and no scientific reproduction claimed.

## September backfill and status changes / 九月补漏及状态变化

- Added the missed September 28 [Beyond Scalar Probes](https://arxiv.org/abs/2609.35487): vector-output row/column signatures and normalized bias estimation, not a new end-to-end parameter attack. / 向量输出签名与归一化偏置原语，非完整参数攻击。
- Existing records gained ePrint aliases 2026/2097 (hard-label end-to-end), 2026/2095 (unknown-architecture MLP v2), and 2026/2061 (Normal Alignment). Existing CNN alias 2026/2161 was reconfirmed. / 别名与修订不新增计数。
- [ePrint 2026/2127](https://eprint.iacr.org/2026/2127) was withdrawn October 1. Retained historical claims and fingerprint are explicitly labeled, alongside the already withdrawn 2026/1025. / 撤回记录保留原证据并显著标注。

Both PDFs added by the earlier reconciliation have verified raw-byte fingerprints. Metadata-only ePrint alias checks are kept separate from PDF verification. The follow-up adds one further verified PDF; all 55 works now have comparison records and code manifests. No unreviewed comparison metric is released as a measured zero.
