<p align="center">
  <img src="assets/taxonomy.png" alt="神经网络与分组密码的结构类比" width="100%">
</p>

# Awesome Cryptanalytic Extraction

**神经网络密码分析提取**专题目录：结构与参数恢复、源码、可行性边界及防御。

[English](README.md) · [九月进展](docs/progress-2026-09.md) · [检索审计](docs/search-audit-2026-09-17.md) · [BibTeX](bib/cryptanalytic_extraction.bib) · [结构化目录](data/papers.json)

**更新于 2026-09-18 · 49 篇独立文献 · 13 类。** 包含预印本、明确单列的相关理论、两篇综述及一篇课程报告。已广泛检索并核对来源，但不宣称覆盖所有模型窃取论文。

## 近期进展

- **9 月 18 日更新：** 新增仅标签符号恢复论文 [Normal Alignment](https://arxiv.org/abs/2609.18751)，更新 [ePrint 2026/848](https://eprint.iacr.org/2026/848)，后者现题为 *Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning*。这是 1 篇新增和 1 篇重大修订，不重复计数。[结果、代码状态及边界](docs/update-2026-09-18.md)。

- **未知结构：** 九月的[猜测确定法](https://arxiv.org/abs/2609.14379)联合恢复 ReLU 全连接网络结构及参数，不代表任意 CNN 或 Transformer 已可恢复；同时收录早期[几何逆向工作](https://arxiv.org/abs/1910.00744)，避免忽略历史背景。
- **数值可行性：** [有限精度误差分析](https://eprint.iacr.org/2026/1943)研究提取原语的数值误差；[输出舍入报告](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf)评价适应舍入后的攻击。二者均不能给出所有网络通用的安全精度阈值。
- **超越 ReLU MLP：** 已纳入 [softmax 注意力](https://eprint.iacr.org/2026/1678)、[多头注意力查询学习](https://arxiv.org/abs/2608.03294)、[孤立 GLU 模块](https://arxiv.org/abs/2608.06631)、RNN、GNN、CNN 池化及光滑激活。模块级恢复不是完整 LLM 提取。
- **仅标签的进展与限制：** [代数签名](https://eprint.iacr.org/2026/1164)已包含 max-pooling CNN 实验；[跨层提取与多项式性分析](https://eprint.iacr.org/2025/1868)指出持久及死亡神经元问题。签名、符号及端到端可执行模型恢复必须分别陈述。

## 范围与阅读路径

密码分析类比将权重视为隐藏参数、输入视为选择查询，通过差分、几何或代数泄漏获取结构信息，而不只是模仿自然测试集上的行为。这是研究类比，并不意味着神经网络就是安全密码。

1. 先读**基础工作**，再读 CRYPTO 2020、EUROCRYPT 2024 及原始输出提取改进。
2. **仅标签提取**应与部分层恢复、多项式性限制一起阅读。
3. 比较 **CNN/池化、激活、RNN/GNN、注意力**时，先核对预言机与结构假设。
4. 将理想化定理用于实际系统前，阅读**有限精度与防御**。
5. **相关理论、LLM 部分提取及侧信道**单列为背景，不能互换威胁模型。

| 维度 | 必须保留的区别 |
|---|---|
| 预言机 | 原始实数输出、概率/top-k 分数、仅 top-1 标签、解释/梯度、物理泄漏 |
| 恢复对象 | 结构、带比例/符号歧义的签名、定向参数、规范等价函数、局部模块、完整可执行模型 |
| 假设 | 已知结构、一般位置、可辨识神经元、连续选择输入、有限精度、可直接访问中间模块 |
| 证据 | 条件化定理、查询量、实际时间、采样保真度、参数误差、经认证的函数等价 |

## 目录约定

**¹ 年份**采用归档/报告年份，发表年份另列。改题及 ePrint/arXiv 交叉版本只算一篇。链接 PDF 为归档版本，不保证采用出版社终稿排版。已核对副本的版本信息、页数及 SHA-256 在 JSON 中。

**² 代码**默认指作者或论文明确链接的仓库。`404` 仅表示核查时不可访问，不等于确认删除；匿名附件的 `410` 表示服务明确报告过期。补充代码、作者扩展分支和阅读清单均单独标注，不冒充完整攻击实现。“未检索到”不等于代码不存在。可访问性核查**不等于执行代码或复现结果**。

## 论文分类

### 基础与早期工作 (3)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2019 | [Reverse-Engineering Deep ReLU Networks](https://arxiv.org/abs/1910.00744) · [PDF](https://arxiv.org/pdf/1910.00744) | ICML 2020 | Real-valued queries<br>Deep ReLU | 在假设下利用边界几何恢复结构及参数，允许网络对称性。 | 未检索到 |
| 2019 | [High Accuracy and High Fidelity Extraction of Neural Networks](https://arxiv.org/abs/1909.01838) · [PDF](https://arxiv.org/pdf/1909.01838) | USENIX Security 2020 | Raw outputs / prediction queries<br>Shallow and deep NN | 区分准确率与保真度，包含浅层等价恢复和混合攻击。 | 未检索到 |
| 2016 | [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) · [PDF](https://arxiv.org/pdf/1609.02943) | USENIX Security 2016 | Prediction scores / labels<br>Classical ML / shallow NN | 方程求解及早期 API 提取，不是任意深网的精确恢复。 | [官方](https://github.com/ftramer/Steal-ML) |

### 原始输出 ReLU 提取 (6)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Navigating the Deep: End-to-End Extraction on Deep Neural Networks](https://eprint.iacr.org/2026/296) · [PDF](https://eprint.iacr.org/2026/296.pdf) | EUROCRYPT 2026 | Raw outputs<br>Deep ReLU MLP | 针对深层恢复瓶颈的端到端提取。 | [官方](https://github.com/PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction) |
| 2026 | [Geometric Critical Point Screening: Clustering-Free Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2026/1025) · [PDF](https://eprint.iacr.org/2026/1025.pdf) | Preprint | Raw outputs<br>ReLU networks | 几何临界点筛选，避免聚类阶段。 | [官方](https://github.com/1983321048/Geometric-Critical-Point-Screening) |
| 2026 | [Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption](https://arxiv.org/abs/2609.14379) · [PDF](https://arxiv.org/pdf/2609.14379) | Preprint | Raw outputs; architecture unknown<br>ReLU fully connected networks | 猜测确定法联合恢复结构及参数；不等于任意 CNN 或 Transformer 恢复。 | 未检索到 |
| 2024 | [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011) · [PDF](https://arxiv.org/pdf/2406.10011) | NeurIPS 2024 | Raw outputs<br>ReLU MLP | 加速实际符号恢复，运行时间与查询量需分别评价。 | [官方](https://github.com/hannafoe/cryptanalytical-extraction) |
| 2023 | [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526) · [PDF](https://eprint.iacr.org/2023/1526.pdf) | EUROCRYPT 2024 | Raw outputs<br>ReLU MLP | 多项式时间符号恢复，改进原始密码分析提取流程。 | [官方](https://github.com/Crypto-TII/deti) |
| 2020 | [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884) · [PDF](https://arxiv.org/pdf/2003.04884) | CRYPTO 2020 | Raw outputs<br>ReLU MLP | 差分临界点提取，依次恢复签名、符号与参数。 | [官方](https://github.com/google-research/cryptanalytic-model-extraction) |

### 仅标签提取 (6)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](https://eprint.iacr.org/2026/1164) · [PDF](https://eprint.iacr.org/2026/1164.pdf) | Preprint | Top-1 label only<br>FCNN / max-pooling CNN | 代数签名向量替代高代价 SVD 聚类；实验含 FC 前层及 LeNet-5 签名，不是任意网络完整恢复。 | 已宣告；URL 为占位符 |
| 2026 | [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751) · [PDF](https://arxiv.org/pdf/2609.18751) | Preprint | Top-1 label only; sign-recovery stage<br>Deep ReLU MLP | 法向量与签名对齐结合 eSOE，在报告模型中恢复 512/512、320/320 个符号；属于符号恢复，非已展示的完整端到端攻击。 | 已宣告；URL 为占位符 |
| 2025 | [Is the Hard-Label Cryptanalytic Model Extraction Really Polynomial?](https://eprint.iacr.org/2025/1868) · [PDF](https://eprint.iacr.org/2025/1868.pdf) | CRYPTO 2026 | Top-1 label only<br>ReLU MLP | 持久及死亡神经元限制多项式性论断，并提出跨层提取。 | [论文所链；404](https://github.com/ECSIS-lab/hard-label-cross-layer-extraction) |
| 2025 | [Extracting Some Layers of Deep Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2025/1118) · [PDF](https://eprint.iacr.org/2025/1118.pdf) | LATINCRYPT 2025 | Top-1 label only<br>ReLU MLP | 结构条件下的部分层及输出层恢复，并非无条件端到端提取。 | [官方](https://github.com/deividafonso281/hard-label-contract-output) |
| 2024 | [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580) · [PDF](https://eprint.iacr.org/2024/1580.pdf) | EUROCRYPT 2025; extended version | Top-1 label only<br>Deep ReLU MLP | 双点、签名与符号恢复，依赖结构和几何条件。 | [官方](https://github.com/Jchavezsaab/hard-label-dnn-extraction) |
| 2024 | [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403) · [PDF](https://eprint.iacr.org/2024/1403.pdf) | ASIACRYPT 2024 | Top-1 label only<br>ReLU MLP | 从决策边界几何开展仅标签密码分析提取。 | [官方](https://github.com/AI-Lab-Y/NN_cryptanalytic_extraction) |

### CNN 与池化 (4)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [End-to-End Polynomial-Time Cryptanalytic Extraction of Convolutional Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/902) · [PDF](https://eprint.iacr.org/2026/902.pdf) | Preprint | Top-1 label only<br>Average-pooling CNN; known architecture | 端到端流程仍依赖保留正确候选等结构性假设。 | [匿名附件](https://anonymous.4open.science/r/cnn_hard_label_extraction-83F4) |
| 2026 | [Model Extraction of Convolutional Neural Networks with Max-Pooling](https://eprint.iacr.org/2026/464) · [PDF](https://eprint.iacr.org/2026/464.pdf) | ToSC 2026 | Raw outputs<br>Max-pooling CNN | 利用池化信息与感受野结构开展提取。 | [官方](https://github.com/PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling) |
| 2026 | [Algebraic Attack on Convolutional Neural Networks with Max Pooling](https://eprint.iacr.org/2026/241) · [PDF](https://eprint.iacr.org/2026/241.pdf) | CRYPTO 2026 | Raw outputs<br>Max-pooling CNN | 代数方法处理池化切换；原始输出结果不能直接迁移至仅标签场景。 | [论文所链；404](https://github.com/czr-eric/Algebraic-Attack-on-CNN) |
| 2026 | [Cryptanalytic Extraction of Convolutional Neural Networks](https://eprint.iacr.org/2026/139) · [PDF](https://eprint.iacr.org/2026/139.pdf) | ACISP 2026 | Top-1 label only<br>Average-pooling CNN | 利用卷积结构恢复卷积核。 | [已过期；410](https://anonymous.4open.science/r/cnn-extraction-93C4) |

### 激活函数扩展 (4)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Deep Neural Networks with Non-Linear Activations](https://eprint.iacr.org/2026/253) · [PDF](https://eprint.iacr.org/2026/253.pdf) | CRYPTO 2026 | Raw outputs<br>Smooth/non-linear activations | 高阶及近线性几何支持所研究非线性激活的恢复，不代表任意光滑函数。 | [官方](https://github.com/mstealercryptocrypto-ops/mod_stealer26) |
| 2026 | [Cryptanalytic Extraction of Neural Networks with Various Activation Functions](https://eprint.iacr.org/2026/178) · [PDF](https://eprint.iacr.org/2026/178.pdf) | ToSC 2026 | Raw outputs / hard labels (variant-dependent)<br>PReLU / LeakyReLU / HardTanh / Step | 扩展到多种激活函数，各变体的预言机假设不同。 | [官方](https://github.com/qixiaokang1-stack/cryptanalytic-model-various-functions) |
| 2026 | [Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2026/1066) · [PDF](https://eprint.iacr.org/2026/1066.pdf) | Preprint | Top-1 label only<br>PReLU | 放宽仅标签提取中的斜率及结构限制。 | 未检索到 |
| 2025 | [Delving into Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2025/1970) · [PDF](https://eprint.iacr.org/2025/1970.pdf) | ASIACRYPT 2025 | Raw outputs / top-m probabilities<br>PReLU | 在给定条件下恢复 PReLU 参数，不是仅标签结果。 | [官方](https://github.com/AI-Lab-Y/Extracting_PReLU_NN) |

### RNN 与 GNN (2)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/719) · [PDF](https://eprint.iacr.org/2026/719.pdf) | Preprint | Top-1 label only<br>Message-passing GNN | 在文中模型下利用图与消息传递结构开展提取。 | [官方](https://github.com/springli07/GNN_MP_CEA) |
| 2026 | [Cryptanalytic Extraction of Recurrent Neural Network Models](https://eprint.iacr.org/2026/168) · [PDF](https://eprint.iacr.org/2026/168.pdf) | Preprint | Raw outputs / top-1 labels<br>RNN | 利用循环结构；长展开序列共享权重，不能等同于独立深层。 | 未检索到 |

### 注意力与 GLU 模块 (4)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Multi-Head Softmax Attention Models](https://eprint.iacr.org/2026/1678) · [PDF](https://eprint.iacr.org/2026/1678.pdf) | Preprint | Raw outputs / chosen continuous inputs<br>Multi-head softmax attention | 恢复规范等价表示；Q/K/V 分解存在规范自由度。 | 未检索到 |
| 2026 | [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631) · [PDF](https://arxiv.org/pdf/2608.06631) | Preprint | Direct queries to an isolated block<br>Bias-free GLU FFN | 对孤立无偏置模块做对踵分离，不是经 token API 提取完整 LLM。 | 未检索到 |
| 2026 | [Provably Learning Multi-Head Attention with Queries](https://arxiv.org/abs/2608.03294) · [PDF](https://arxiv.org/pdf/2608.03294) | Preprint | Chosen real-valued queries<br>Multi-head attention / restricted one-layer Transformer | 恢复规范化注意力头；单层 Transformer 扩展有额外假设。 | 未检索到 |
| 2026 | [Provably Learning Attention with Queries](https://arxiv.org/abs/2601.16873) · [PDF](https://arxiv.org/pdf/2601.16873) | ICML 2026 | Chosen real-valued queries<br>Attention | 注意力模型假设下的查询学习保证。 | 未检索到 |

### LLM 部分结构与输出空间提取 (2)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2024 | [Logits of API-Protected LLMs Leak Proprietary Information](https://arxiv.org/abs/2403.09539) · [PDF](https://arxiv.org/pdf/2403.09539) | COLM 2024 | Logprobs / restricted API<br>LLM output subspace | softmax 瓶颈泄露隐藏维度及输出子空间信息，不是全网恢复。 | 未检索到 |
| 2024 | [Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) · [PDF](https://arxiv.org/pdf/2403.06634) | ICML 2024 | Restricted logprobs / logit-bias API<br>LLM output projection | 恢复带对称性的部分输出投影，不是全部权重；公开代码为补充材料。 | [官方补充代码](https://github.com/dpaleka/stealing-part-lm-supplementary) |

### PPML 与更强侧信道预言机 (5)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning](https://eprint.iacr.org/2026/848) · [PDF](https://eprint.iacr.org/2026/848.pdf) | Preprint | Finite-ring/fixed-point inference; variants include top-1 + probability<br>PPML neural inference | 9 月 17 日修订：多点投影聚合支持扩张网络，并优化符号探测方向；文中基准的符号恢复查询较 Neuron Wiggle 减少 30%-74%，不是通用降幅或加密破解。 | [匿名附件](https://anonymous.4open.science/r/PPML_Model_Extraction_Attack) |
| 2025 | [Activation Functions Considered Harmful: Recovering Neural Network Weights through Controlled Channels](https://arxiv.org/abs/2503.19142) · [PDF](https://arxiv.org/pdf/2503.19142) | Preprint | SGX controlled channels<br>DNN activation implementation | 激活访存泄漏支持权重恢复，第一层及后续层恢复程度不同。 | [官方](https://github.com/heavyimage/afch_paper) |
| 2024 | [A Divide-and-Conquer Strategy for Hard-Label Extraction of Deep Neural Networks via Side-Channel Attacks](https://eprint.iacr.org/2024/1870) · [PDF](https://eprint.iacr.org/2024/1870.pdf) | TCHES 2026; revised title | Top-1 labels + side channel<br>Deep NN / non-FC components | 利用物理泄漏分治，能力强于纯黑盒仅标签访问。 | [官方](https://github.com/bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN) |
| 2020 | [SNIFF: Reverse Engineering of Neural Networks with Fault Attacks](https://arxiv.org/abs/2002.11021) · [PDF](https://arxiv.org/pdf/2002.11021) | Preprint / IEEE Transactions on Reliability | Fault injection + outputs<br>Neural networks | 符号位故障攻击的攻击者能力强于普通 API 查询。 | 未检索到 |
| 2018 | [CSI Neural Network: Using Side-channels to Recover Your Artificial Neural Network Information](https://arxiv.org/abs/1810.09076) · [PDF](https://arxiv.org/pdf/1810.09076) | USENIX Security 2019; published title differs | Power / EM side channels<br>Embedded neural networks | 物理观测泄露结构及参数，作为历史背景收录。 | 未检索到 |

### 有限精度与可行性 (1)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Finite-Precision Error Analysis of Cryptanalytic Model Extraction](https://eprint.iacr.org/2026/1943) · [PDF](https://eprint.iacr.org/2026/1943.pdf) | Preprint; ASIACRYPT 2026 acceptance author-listed | Finite-precision raw outputs<br>Cryptanalytic signature recovery | 量化提取原语的数值误差，不是普遍不可能性或通用防御证明。 | [论文所链；404](https://github.com/CryptAnalystDesigner/Finite-Precision-Feasibility-of-Cryptanalytic-Model-Extraction) |

### 防御与适应性评价 (2)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2026 | [Output Rounding Is Not a Free Defense Against Cryptanalytic Neural Network Extraction](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) · [PDF](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | MIT 6.5610 Spring 2026 course report | Rounded raw outputs<br>Small ReLU MLP | 步间距攻击适应输出舍入；是小模型实验证据，不是通用安全阈值。 | 提及补充代码；未找到 URL |
| 2025 | [Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks](https://arxiv.org/abs/2509.16546) · [PDF](https://arxiv.org/pdf/2509.16546) | NeurIPS 2025 | Defense against parameter extraction<br>ReLU MLP | 训练时神经元相似性正则化，需针对适应性攻击评价。 | [官方](https://github.com/anonymous-123-code/anonymouscode) |

### 相关可辨识性与学习理论 (8)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2025 | [Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries](https://arxiv.org/abs/2511.20312) · [PDF](https://arxiv.org/pdf/2511.20312) | UniReps 2025 workshop | Input-output queries<br>Teacher-student parameter recovery | 数据增强改进 Expand-and-Cluster，代码为作者扩展分支。 | [作者扩展分支](https://github.com/alexl4123/expand-and-cluster) |
| 2024 | [Model Stealing for Any Low-Rank Language Model](https://arxiv.org/abs/2411.07536) · [PDF](https://arxiv.org/pdf/2411.07536) | Preprint | Conditional queries<br>Low-rank sequence distributions / HMM | 学习低秩输出分布，不是任意 Transformer 权重恢复。 | 未检索到 |
| 2024 | [Provably learning a multi-head attention layer](https://arxiv.org/abs/2402.04084) · [PDF](https://arxiv.org/pdf/2402.04084) | STOC 2025 | Random examples (not chosen queries)<br>Multi-head attention | 非退化假设下的学习理论，不是实用全模型 API 提取演示。 | 未检索到 |
| 2023 | [Reverse Engineering Deep ReLU Networks An Optimization-based Algorithm](https://arxiv.org/abs/2312.04675) · [PDF](https://arxiv.org/pdf/2312.04675) | Preprint | Input-output queries<br>Deep ReLU | 基于优化的逆向工程，区分所提保证与已展示的可扩展性。 | 未检索到 |
| 2023 | [Expand-and-Cluster: Parameter Recovery of Neural Networks](https://arxiv.org/abs/2304.12794) · [PDF](https://arxiv.org/pdf/2304.12794) | ICML 2024 | Input-output samples<br>Neural networks | 过参数化学生网络及聚类恢复参数，与差分提取相关但并不相同。 | [官方](https://github.com/flavio-martinelli/expand-and-cluster) |
| 2022 | [Finite Sample Identification of Wide Shallow Neural Networks with Biases](https://arxiv.org/abs/2211.04589) · [PDF](https://arxiv.org/pdf/2211.04589) | Preprint | Finite input-output samples / queries<br>Wide shallow networks with biases | 模型及采样条件下的方向、偏置辨识。 | 未检索到 |
| 2021 | [An Exact Poly-Time Membership-Queries Algorithm for Extraction a three-Layer ReLU Network](https://arxiv.org/abs/2105.09673) · [PDF](https://arxiv.org/pdf/2105.09673) | ICLR 2023 | Membership / real-valued queries<br>Three-layer ReLU | 深度及一般位置假设下的精确多项式查询恢复。 | 未检索到 |
| 2018 | [Model Reconstruction from Model Explanations](https://arxiv.org/abs/1807.05185) · [PDF](https://arxiv.org/pdf/1807.05185) | FAT* 2019 | Gradient/explanation oracle<br>Neural networks | 解释及梯度预言机提供强于普通预测的恢复能力。 | 未检索到 |

### 综述与阅读资源 (2)

| 年份¹ | 论文与 PDF | 发表状态 | 预言机 / 架构 | 恢复目标与边界 | 代码² |
|---|---|---|---|---|---|
| 2025 | [A Systematic Survey of Model Extraction Attacks and Defenses: State-of-the-Art and Perspectives](https://arxiv.org/abs/2508.15031) · [PDF](https://arxiv.org/pdf/2508.15031) | Preprint survey | Multiple<br>Multiple | 广义模型提取综述，也涵盖本仓库核心范围之外的替代模型窃取。 | [阅读清单，非攻击代码](https://github.com/kzhao5/ModelExtractionPapers) |
| 2025 | [A Survey on Model Extraction Attacks and Defenses for Large Language Models](https://arxiv.org/abs/2506.22521) · [PDF](https://arxiv.org/pdf/2506.22521) | Preprint survey | Multiple LLM APIs<br>LLM | LLM 提取及防御背景综述，不是精确恢复攻击。 | [阅读清单，非攻击代码](https://github.com/kzhao5/ModelExtractionPapers) |


## 更新后的开放问题

- **一般未知结构：** ReLU 全连接网络已有进展，不应再称完全空白；混合算子、残差路径和极弱先验仍需独立证据。
- **仅标签 max-pooling：** 已有相关实验，不能笼统称尚无结果；需要超越小规模签名演示，评估全层、符号、偏置、池化赢家切换与事件可观测性。
- **实际精度与代价：** 同时评估条件数、查询预算、限流、拒答和概率截断，不把实数运算模型中的多项式性等同于低成本提取。
- **可辨识性：** 明确死亡/持久神经元、等价参数化及规范化。某一参数表示恢复失败不自动构成安全性。
- **适应性防御：** 固定效用与攻击预算评价训练正则化、输出修改和适应性攻击，小模型实验不能建立普遍安全结论。
- **模块组合：** 注意力、输出投影或孤立 GLU 的恢复，不代表经普通 token API 可以恢复它们组成的整个网络。

## 维护与贡献

在 [data/papers.json](data/papers.json) 中维护官方题名、作者、来源、发表状态、预言机、能力边界、代码来源及 PDF 指纹。正文修改[中文模板](docs/readme_zh.template.md)或[英文模板](docs/readme_en.template.md)，然后运行：

```console
python scripts/render_catalog.py
python scripts/render_catalog.py --check
```

明确标注预印本及课程报告，优先使用一手来源和作者代码。不将第三方实现或受版权保护的 PDF 直接打包到本仓库。本地 `ref` 可使用结构化目录中的文件名、官方 PDF 地址和哈希。论文宣称将开源，不代表已经公开可用。

## 声明

仅用于授权模型及系统上的学术研究与防御分析。收录不代表独立验证论文全部结论，也不构成对第三方服务开展攻击的授权。
