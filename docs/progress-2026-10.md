# October progress / 十月进展

Reviewed **2026-10-28, Asia/Shanghai**. Catalog: **54 unique works, 13 categories**, including two retained withdrawn records. See the [current source audit](search-audit-2026-10-28.md), [September progress](progress-2026-09.md) and [stage comparisons](comparison_en.md). / 目录现有 54 篇、13 类；包含两条保留的已撤回历史记录。

## Assisted recovery and reconstruction / 辅助恢复与重建

[Extraction meets Distillation](https://arxiv.org/abs/2610.33671), also [ePrint 2026/2628](https://eprint.iacr.org/2026/2628), combines partial direction recovery with sign search, output fitting and label-based refinement for ReLU/Leaky ReLU MLPs. The evaluated pipeline uses internal gradients, activations and true parameters (§3.4, Table 1); it belongs to the existing stronger-oracle systems category. A complete reconstructed classifier is not complete recovery of the victim's parameters, and subsequent label training does not make the earlier assisted extraction label-only.

该工作将部分方向恢复与符号搜索、输出层拟合及标签学习组合；原文披露使用梯度、隐藏激活及真实参数，因此归入现有更强预言机类别。重建出完整分类器不等于恢复全部原模型参数，后续仅用标签训练不能消除前期额外访问。

The paper distinguishes label requests from batch calls and privileged reads. Its seeded synthetic evaluations and CIFAR experiments use different settings; high synthetic agreement must not be merged with the lower CIFAR results into a composite success claim. The linked author repository is pinned as a source reference, with no project license verified and no scientific reproduction claimed.

## September backfill and status changes / 九月补漏及状态变化

- Added the missed September 28 [Beyond Scalar Probes](https://arxiv.org/abs/2609.35487): vector-output row/column signatures and normalized bias estimation, not a new end-to-end parameter attack. / 向量输出签名与归一化偏置原语，非完整参数攻击。
- Existing records gained ePrint aliases 2026/2097 (hard-label end-to-end), 2026/2095 (unknown-architecture MLP v2), and 2026/2061 (Normal Alignment). Existing CNN alias 2026/2161 was reconfirmed. / 别名与修订不新增计数。
- [ePrint 2026/2127](https://eprint.iacr.org/2026/2127) was withdrawn October 1. Retained historical claims and fingerprint are explicitly labeled, alongside the already withdrawn 2026/1025. / 撤回记录保留原证据并显著标注。

Both new PDFs have verified raw-byte fingerprints. Metadata-only ePrint alias checks are kept separate from PDF verification. All 54 works have comparison records and code manifests; no unreviewed comparison metric is released as a measured zero.
