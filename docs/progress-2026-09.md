# Research Progress / 近期研究进展

Snapshot: **2026-09-17**. This synthesis distinguishes published papers, preprints and a course report. It reports the scope of the cited work, not independent reproduction. See the [complete catalog](../README.md) and [Chinese catalog](../README_zh-CN.md).

## September: Architecture Knowledge and Finite Precision

**Architecture knowledge is becoming an attack variable.** The September 13 preprint *Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption* uses guess-and-determine with architecture-sensitive traces during signature and sign recovery. Its target is ReLU fully connected networks, with expansive and non-expansive examples. This is not evidence that arbitrary residual or Transformer architectures have been recovered. Earlier geometry-based structure recovery should remain part of the historical comparison. [September preprint](https://arxiv.org/abs/2609.14379), [Rolnick and Kording](https://arxiv.org/abs/1910.00744).

**未知结构正在从前提变为攻击对象。** 9 月 13 日预印本利用签名/符号恢复中的结构敏感信息，采用猜测确定法联合提取结构与参数。范围是 ReLU 全连接网络，不是任意残差网络或 Transformer。早期几何结构恢复也应保留在比较中。

**Numerical analysis is now a separate research line.** *Finite-Precision Error Analysis of Cryptanalytic Model Extraction*, received September 9 and revised September 14, examines error propagation in cryptanalytic extraction. ASIACRYPT 2026 acceptance is author-listed; the linked document is a preprint. Numerical difficulty in a particular recovery primitive does not prove that every adapted attack fails. Its paper-linked GitHub URL returned 404 during checking. [ePrint](https://eprint.iacr.org/2026/1943), [author's acceptance notice](https://liuzhang-xdu.github.io/).

**数值可行性已成为独立研究线。** 9 月 9 日提交、9 月 14 日修订的有限精度分析研究提取误差传播。作者列为 ASIACRYPT 2026 接收，当前链接仍是预印本。特定原语的数值困难不等于所有适应性攻击不可能；其论文所链 GitHub 核查时返回 404。

## Attention and Language-Model Components

The 2026 attention results should be read together: single-head/query learning, multi-head query learning, and cryptanalytic multi-head softmax extraction. Their target representations and assumptions differ. Canonical head/function recovery must not be reported as unique recovery of all original Q/K/V factors. Access to chosen real-valued block inputs is stronger than ordinary text-token API access. [Single-head query learning](https://arxiv.org/abs/2601.16873), [multi-head query learning](https://arxiv.org/abs/2608.03294), [softmax extraction](https://eprint.iacr.org/2026/1678).

2026 年的注意力查询学习与密码分析提取应并列阅读，但规范表示、原始参数分解以及访问假设不能混用。直接选择模块实数输入，比普通文本 token API 更强。

The GLU preprint studies **isolated, bias-free feed-forward blocks** via antipodal separation. The 2024 LLM papers concern output projections/subspaces and restricted API leakage. None of these results alone is an end-to-end extraction of an entire modern LLM. The low-rank-language-model theorem is separately categorized as distribution-learning theory, not Transformer-weight recovery. [GLU](https://arxiv.org/abs/2608.06631), [partial production LM](https://arxiv.org/abs/2403.06634), [logit leakage](https://arxiv.org/abs/2403.09539), [low-rank theory](https://arxiv.org/abs/2411.07536).

GLU 工作仅针对孤立无偏置前馈模块；2024 年 LLM 工作主要涉及输出投影、子空间及受限 API 泄漏。它们不能直接组成“完整大模型已被提取”的结论。低秩语言模型定理属于分布学习理论，也不等于 Transformer 权重恢复。

## Hard Labels, Pooling and Depth

Algebraic signature vectors reduce reliance on expensive SVD-based dual-point clustering. The ASV paper includes FCNN and hard-label max-pooling CNN results, with early-layer/signature experiments. Consequently, “no hard-label max-pooling result exists” is outdated, but “general end-to-end hard-label max-pooling extraction is solved” is also unsupported. For average-pooling CNNs, the end-to-end preprint explicitly retains candidate/structure assumptions. [ASV](https://eprint.iacr.org/2026/1164), [average-pooling pipeline](https://eprint.iacr.org/2026/902).

代数签名向量降低对高代价 SVD 双点聚类的依赖。ASV 已涵盖 FCNN 及仅标签 max-pooling CNN 的早期层/签名实验，因此“完全没有结果”已过时，但也不能声称“一般端到端恢复已经解决”。平均池化端到端工作仍保留候选及结构假设。

The polynomiality critique and cross-layer strategy make persistent/dead-neuron behavior important to any comparison. Raw-output deep extraction and sign-recovery improvements should be evaluated with both queries and wall-clock time. A long RNN unrolling reuses parameters; 1,024 recurrent steps are not 1,024 independent parameter layers. [Cross-layer/limitations](https://eprint.iacr.org/2025/1868), [deep extraction](https://eprint.iacr.org/2026/296), [sign recovery](https://arxiv.org/abs/2406.10011), [RNN](https://eprint.iacr.org/2026/168).

持久/死亡神经元是评估多项式性和跨层恢复时不可省略的条件。深层与符号恢复应同时报告查询量及时间。RNN 展开共享参数，不能将 1,024 个时间步表述为 1,024 个独立参数层。

## Defenses and Deployment

*Train to Defend* studies training-time regularization; the MIT *Output Rounding* course report studies an adapted step-spacing attack after naive finite differences fail. Their scope and evidence differ. No rounding threshold from a few small models is a universal defense guarantee. PPML work exploits finite-ring/fixed-point inference behavior, not cryptographic key recovery; some restricted variants still expose the winning probability. Side-channel and fault work requires stronger access and is grouped separately. [Training defense](https://arxiv.org/abs/2509.16546), [rounding report](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf), [PPML](https://eprint.iacr.org/2026/848), [side-channel strategy](https://eprint.iacr.org/2024/1870).

训练正则化防御与输出舍入报告的证据不同。舍入报告展示朴素差分失效后仍可适配攻击，小规模阈值不能充当普遍安全保证。PPML 工作针对有限环/定点推理行为，不是恢复加密密钥；某些受限接口仍提供获胜类别概率。侧信道及故障攻击需要更强访问能力，已独立归类。

## What to Measure Next / 后续评价重点

| Dimension / 维度 | Report separately / 应分别报告 |
|---|---|
| Recovery / 恢复 | Signatures, signs, scales, biases, output layer, executable model / 签名、符号、尺度、偏置、输出层、可执行模型 |
| Oracle / 接口 | Exact/raw output, rounded scores, top-k probabilities, top-1 only, side channel / 原始输出、舍入分数、top-k 概率、仅标签、侧信道 |
| Cost / 成本 | All charged queries, restarts, failed candidates, runtime, precision / 全部查询、重启、失败候选、时间、精度 |
| Correctness / 正确性 | Parameter error, sampled agreement and certified equivalence are different / 参数误差、采样一致与认证等价不可混用 |
| Scope / 范围 | Structural assumptions, identifiability, partial blocks and composition / 结构假设、可辨识性、局部模块及组合 |

No unpublished or rumor-only ResNet claim is used in this update.

本次更新未采用未公开或仅传闻的 ResNet 提取结论。
