# 扩展架构与部分LLM提取：12篇历史核查与1篇后续增补

当前共13篇。第13节为2026-10-28直接核验增补；以下2026-09-30时间、版本表及前12节保留原核查快照，不代表本轮重新下载全部历史PDF。

核查时间：2026-09-30。目录来源：springli07/awesome-cryptanalytic-extraction 当前 main/data/papers.json（updated=2026-09-30）。全部12篇原始PDF已正常公开下载并全文提取检查；没有运行论文代码。下面页码均为所下载PDF从1计数的物理页，便于URL追加 #page=N 定位。NR=查阅对应方法/复杂度/实验章节后未报告该项；“poly”仅保留作者条件性主张，不补造指数。查询次数、采样次数、实数运算、bit complexity、墙钟时间分列理解。

## 版本与可复核文件标识

以下为2026-09-30实际读取的官方PDF；ePrint日期直接取官方History，arXiv版本号取PDF首页。SHA-256用于精确锁定文件，避免后续同URL更新导致页码/结论漂移。

| Paper ID | 本次版本 | 页数 | SHA-256 |
|---|---|---:|---|
| eprint-2025-1970 | 2025-10-24 approved；2025-10-21 received | 32 | db9a8d51e1093083d3e200d3728c5b2c6a87a7673347e27835d8db62e38e52eb |
| eprint-2026-178 | 2026-02-06 approved；2026-02-03 received | 39 | 27557ffbae790abcba5b8a69a24adbcedd58bf07e32c9309ebe1fb184775f88b |
| eprint-2026-253 | 2026-02-16 approved；2026-02-13 received | 33 | ebe4080c30a61c1ce1ca3a1699009c9a07b8194a57ffc2be7ebbab194d8eaf78 |
| eprint-2026-1066 | 2026-05-31 approved；2026-05-27 received | 31 | f771f5abd060140eed2c0e5daa7003ba2041cea03fcee7bb6aa28fc63d8a0335 |
| eprint-2026-168 | 2026-09-18，last of 2 revisions；2026-02-01 received | 34 | b096d4f6425d19254d0fb4e4ef7653e18ebd4761d4cfa6f0a2fd25ed49b748f2 |
| eprint-2026-719 | 2026-04-19 approved；2026-04-13 received | 20 | b2791b2be9d9fde33c3fb8be5015442a8f922af40a6b162ccdb454ed3e21181c |
| arxiv-2601.16873 | v2，2026-05-04 | 18 | e5221682c1da801dbae06aa21ab2d8469839d49cba2f623ae12b770fbe5a76f8 |
| arxiv-2608.03294 | v3，2026-08-24 | 39 | 7d08f64a35f9d3b3268759a8ddd2199c32caaffd5195545dd920d57db25e5bc1 |
| eprint-2026-1678 | 2026-08-15 revised；2026-08-13 received | 31 | 9dcc514494113a6c7135fbb594d364f0c00730c4f671011981b0e95b47ecf45d |
| arxiv-2608.06631 | v1，2026-08-06 | 11 | f2a72cd14354a5920165c014bb2f5f637bbfde0f2c111c9eda50c4ebdff797f7 |
| arxiv-2403.06634 | v2，2024-07-09 | 27 | 65e2ade24ecefc77ab5eaab511b744a611bbc7efd0ec9ad6d434a3f23003be3c |
| arxiv-2403.09539 | v3，2024-11-08 | 15 | a5a1d06963f2b2cf82faca2589417c5a4cb50f7fd5779b4ce60af1d22e410341 |

版本更正：eprint-2026-168 本次PDF为1,143,269 bytes，SHA如上；当前目录记录仍为1,050,687 bytes、SHA fc39c1f1ffb4c54c83d247b992e65def6b8885699ee3d74547e5fbc10f1a3c18。本报告以官方2026-09-18修订PDF为准。其余11份下载文件的SHA与目录一致。

## 可比性总规则

- A组：chosen continuous inputs + raw scalar/vector outputs，PReLU/光滑激活/LeakyReLU网络。不同激活、全网或单层、精度、宽度仍不相同，不能仅按最大参数量排名。
- B组：hard-label网络，但PReLU、RNN序列oracle和GNN固定局部图oracle不是同一单位。node queries不等于graph API calls；RNN一次query是一条完整序列，1024步不等于1024独立隐藏层。
- C组：直接连续值attention/GLU block oracle。可比较单头/多头canonical recovery的理论query，但不能与token API的完整Transformer/LLM恢复混同。scalar attention与full-vector GLU每次返回的信息量不同。
- D组：受限LLM API的logprob/logit-bias，恢复输出维数/投影子空间，不恢复所有层。预处理成本与之后每prompt边际成本必须拆开。
- 所有“100% fidelity”是论文指定样本/分布上的指标，除有额外定理条件外不等于全输入域认证；storage exact、参数误差、方向余弦与功能误差不是一种指标。

## 1. eprint-2025-1970

Delving into Cryptanalytic Extraction of PReLU Neural Networks
源：https://eprint.iacr.org/2025/1970.pdf

- oracle/范围：raw outputs或top-m probabilities；PReLU前馈网络，按层恢复权重、bias、符号和slope，不是label-only。
- 逐阶段Q：附录D.1 pp.30–31，层i宽d_i，输入到该层维度d_(i−1)。coupon collector（均匀性假设）收集O(d_i log₂ d_i)临界点；每点定位ε次查询，ε被作者作为binary-search精度决定的小常数；每点差分权重恢复4d_(i−1)−1次；已有权重后的符号/slope恢复0额外query。作者层级汇总Q_i=O(d_i(4d_(i−1)−1)log₂ d_i)。全网逐层求和，不能删掉精度常数后当bit complexity。
- 逐阶段时间：差分后解线性方程；作者仅给poly及oracle运行占主导的论述，未提供全网算术次数的完整显式式子，T_explicit=NR。D.2 p.31仅称top-m变体同为poly，未给m依赖显式系数。
- 实证：§8/Table2 p.24；128–64–1、8,385参数，workflow2 Q=2^19.34，输出误差(ε,0)=2^-29.55，max参数误差2^-33.79。64–32–32–1、3,233参数，workflow2 Q=2^18.64，输出误差2^-23.14、参数误差2^-27.44；workflow1同模型Q=2^21.35且输出误差2^-5.20，说明workflow选择影响很大。实测墙钟该表NR。
- 限制：§8注释p.23区分layerwise assumed-perfect prefix与真正end-to-end误差传递。不能把此前ReLU sign方法套PReLU的失败率当本文恢复精度。以上Q不是MNIST所有模型统一成本。

## 2. eprint-2026-178

Cryptanalytic Extraction of Neural Networks with Various Activation Functions
源：https://eprint.iacr.org/2026/178.pdf

- oracle/分支：S5 raw-output；S1 hard-label（paper taxonomy）。LeakyReLU、HardTanh、PReLU、ELU、Step必须逐分支展示，不能合为“各种激活均端到端poly”。
- 复杂度证据：Table1 p.5及§3–6。LeakyReLU signature poly；raw-output sign只在contractive情况下保证poly，否则指数；hard-label对应方法poly。HardTanh因奇对称无需sign，sign stage O(1)，但signature未全恢复。PReLU hard-label方法仅contractive结构且依赖slope限制（见后续1066推广）；Step signature poly、sign/exhaustive search指数（§6，及p.22关于穷举最坏指数）。ELU仅小宽/小深raw-output实验，无hard-label成功。
- 显式阶段Q、统一算术式、逐表运行秒数：NR；Table1的poly/exp主要是time分类，不能直接改填为相同的query Big-O。
- 实证：Table2 p.28/MNIST，LeakyReLU raw 784–10–1、7,861参数，最大参数误差2^-32.16；hard-label 784–64^4–10、63,370参数，2^-24.89。PReLU hard-label同宽深63,626参数，2^-7.48。ELU raw 784–2²–1、1,579参数，2^-6.72。Step 784–3–2–10、2,393参数，raw/hard分别2^-12.43 / 2^-8.08。
- HardTanh限制：Table3 p.28–29，784–128²–10、118,282总参数，只恢复第一层122/128、第二层86/128；784–64^4–10各层62/64、52/64、52/64、42/64。表中max error仅针对恢复成功部分。禁止写“118K参数完整精确提取”。不同颜色checkmark在纯文本丢失语义，应用需直接保留scope文字。

## 3. eprint-2026-253

Cryptanalytic Extraction of Deep Neural Networks with Non-Linear Activations
源：https://eprint.iacr.org/2026/253.pdf

- oracle/假设：raw logits；σ两端指数趋近线性或常数，非线性带足够窄，能找到主要由一个神经元非线性支配的输入。不是任意smooth函数的无条件定理。
- 阶段：§3.1 pp.6–8二阶导数比值signature+sieve；§3.2 p.9伪法向移动降噪；§3.3 pp.10起adjacent linear zones(ALZ)；随后layer distinguisher、scale/sign/bias与activation识别。
- Q/T：§3.1 “Efficiency” pp.8–9：在神经元大致均匀被采样、每个sample有常数成功率的简化模型下，O(n log n)是采样点数，不是完整oracle调用数；每sample处理poly，精确导数有限差分调用数/全网显式Q与T=NR。不能把O(n log n)直接与PReLU逐点4d−1的Q放同一列。
- 实证：Table2 p.23，16×16^8×10：42s、data=2^20.14、首层16/16、272/272参数；这些不是全网参数。Table3 p.24一小时预算，784×128×1恢复70/128、54,950/100,480（54.7%）；MNIST784×16^8×1恢复15/16首层（93.8%）；CIFAR3072×8^8×1首层8/8、24,584/24,584。
- 分阶段墙钟：Table2 sieve/ALZ/check，例如16×16^8×10为7.7%/88.1%/1.5%；Table3后端不同，作者明确仅sieve/ALZ的Cython部分可公平比较，check Python更慢。
- 深层限制：Table6 p.26，16×16^8×10第四层2小时后13/16检测，152/256部分参数、0/256 fully denoised参数；所以不能宣称任意深网完整高精恢复。wallclock与data计数原样保留，不替换成统一Q。

## 4. eprint-2026-1066

Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks
源：https://eprint.iacr.org/2026/1066.pdf

- oracle/范围：top-1 label，联合signature+slope，residual analysis、progressive parameter decoupling放宽旧PReLU限制。实验重点是目标层，不等于完整网络所有参数端到端实证。
- 阶段Q/T：Algorithm1 p.22、§6.4 p.23：Stage1收集dual并建空间；Stage2最多T个非线性方程组，0query，作者主张poly求解；Stage3 progressive decoupling复用Stage1 dual（§7.2 p.26明确0新增query）。Stage1/3继承既有方法的poly主张，未给全流程显式次数/系数，Q_explicit/T_explicit=NR。非线性求解的“poly”按作者声称标注，不升级为一般非线性系统多项式保证。
- §6.4还承认persistent active/inactive可令旧dual发现退化指数；两种PReLU结构采样100,000点观察activation概率0.2–0.8 / 0.1–0.9，只是实证缓解，不能推出最坏情形保证。
- 实证：§7.1 p.25，单模型单层不超过2^11秒、2^26 queries；196–20–25–30–10恢复第3层，Stage1约2^9.645秒、2^24.93 queries，Stage2平均2^5.75秒、0query，约20,000 dual且大量属于前层。此处PDF排版“2^9.645”，不是29.645秒。
- Table2 p.26：20–22–24–26–10经Stage3后目标层24/24、26/26成功，max signature error2^-24.61、2^-17.64；MNIST784–20–22–24–10为22/22、24/24，2^-27.98、2^-26.98。成功阈值2^-10；不是输出fidelity。

## 5. eprint-2026-168

Cryptanalytic Extraction of Recurrent Neural Network Models
源：https://eprint.iacr.org/2026/168.pdf

- oracle/范围：raw outputs或hard labels；ReLU recurrent，隐藏态不可见，可控制整段连续输入；构造等价FCN，复用时间权重，τ是时间步、n是recurrent layers，二者必须分列。
- 阶段：输入权重等价FCN恢复→RPA排列/缩放对齐→RPR recurrent rows/bias→困难神经元FBD。Theorem1 §3 p.11、Theorem2 §4 p.18为条件性功能等价；不意味着所有训练RNN都有可观测充足事件。
- RPA离线算术：§3 “Complexity” p.15，O(K d1²+d1³)，K探针数；明确不含Φ/B构建；Hungarian O(d1³)，应用变换O(d1²)。
- RPR hard-label离线：AppendixA.3 pp.31–32，N记录、n_a=d_l anchor、N_j经筛选记录、q_j额外rank-repair components：O(N d0 d_l² + N d_l³ + n_a N d_l² + Σ_j[N_j² d_l +(1+q_j)(d_l³+N d_l²)+N log N])。假设d_(l−1)=O(d_l)、中位过滤次数有界；不含dual acquisition/Jacobian。
- RPR raw离线：AppendixA.3 pp.32–33，O(d_l² [N d_l(d0+d_l)+(T_iter+1)(N d0+d_l²)+R(N+d0+d_l)])。T_iter global reassignment/fit轮，R rank completion candidate checks；不含记录采集、feature/Jacobian和gradient jumps。固定维数下N线性只在R也固定时成立。
- 全网显式oracle Q与完整wallclock式NR，不能把以上offline当整个攻击成本。
- 实证：Table1 p.5，200–32–1 raw τ20 Q2^22.07，最大绝对输出误差2^-23.31，75分位相对误差2^-26.65；τ1024 Q2^21.58，2^-23.30/2^-26.83。同结构hard τ20 Q2^26.48，2^-18.46/2^-21.03。三recurrent层200–32³–1 raw Q2^22.78、abs2^-12.19；hard Q2^32.51、abs2^-11.11。指标来自10^5完整Gaussian sequences，不能解读为全域认证。

## 6. eprint-2026-719

Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting
源：https://eprint.iacr.org/2026/719.pdf

- oracle/范围：message-passing ReLU GNN固定局部查询模型；local operator在查询间不变、可选连续局部features，硬标签node responses。不是任意图API，只允许自然图输入时定理不自动成立。
- 阶段：dual discovery→single-differential/local-isolation筛选→signature合并→sign probes→scale-chain cancellation（Theorem4.1 p.12）与输出恢复，取消显式逐层scale fitting。
- 条件性复杂度：Proposition4.4 / Eq32 p.13，T_post=O(N K d²+N K_sign)，Q=poly(L,d,K,C,κ_dual)。N=Σ_(l=0)^(L−1)d_l recovered neurons，K accepted dual coverage/neuron，K_sign sign probes/neuron，κ_dual归纳accepted-dual discovery成本。该命题显式把事件发现与post-processing分开；Q没有展开成单项式。假设accepted single-differential、local isolation、non-degeneracy，不能隐去κ_dual。
- 实证：§5/Table3 p.15，ogbn-arxiv四类8,171nodes，最大32–32^5–4、10,660参数，平均/最大误差1.96e−6/6.66e−5、100% sampled fidelity。Cora1,804、CiteSeer2,223也100%，但四类子集与同固定局部模型。
- Table4 p.16 dedicated32–32^4–4 checkpoint，48.68M node queries，train/test/random fidelity100%；random是10,000 standard-normal two-node queries。48.68M不应绑定到最大10,660模型所有结构都一致。硬随机distillation65.37M，test fidelity99.63%、random61.95%，说明test fidelity不等于域内整体恢复。硬件单RTX4090，完整墙钟NR。

## 7. arxiv-2601.16873

Provably Learning Attention with Queries
源：https://arxiv.org/pdf/2601.16873

- oracle：chosen arbitrary real token vectors、scalar value query，canonical merged W∈R^(d×d), v∈R^d，v≠0。不是分别恢复Q/K/V原始因子。
- Theorem4.1 §4 pp.3–4：length1 queries d次恢复v；length2每列d次，W共d²次；总d+d²。线性系统求解poly，整体精确算术显式T大O NR（不自行填O(d³)）。
- Theorem5.1 §5 pp.5–6：rank(W)≤r，d+m queries，m=O(rd)，Gaussian rank-one measurements+核范数凸规划，成功概率≥1−exp(−Ω(m))，polytime。不能只写O(rd)而不注明低秩。
- Theorem6.1 p.6：approximate-value oracle、∥W∥F≤known bound W≥2、∥v∥≤1，非零坐标≥μ；O(d²)queries，τ=O(min{μ, ε_v/√d, μ ε_W/(W²d)})，输出给定v/W误差。这里τ是可以要求的oracle tolerance，现实float64 API未必满足。
- 单层bias-free ReLU Transformer §4.1 pp.4–5：FFN primitive Q_FFN(d,m)+O(d²)，反对称f(X)−f(−X)每个attention query需两个Transformer query，v=A w_o≠0、FFN可学习结构假设。MHA §7仅known pairwise-orthogonal subspaces特殊情形；不是一般MHA。
- 数值实验尺寸/Q/墙钟/fidelity：全文无独立实验节，NR（理论工作）。

## 8. arxiv-2608.03294

Provably Learning Multi-Head Attention with Queries
源：https://arxiv.org/pdf/2608.03294

- oracle/假设：chosen real-valued scalar value query；H canonical heads，W_h两两不同、v_h非零，精确实数算术、log与多项式factorization可用。只恢复canonical pairs up to permutation。
- Theorem5.1 p.5：总Q=4Hd²−2H+1，max sequence length2H+1；1个one-token response+2d²−1个local atom decoding，每个2H repeated-token queries。H仅上界H0时用4H0d²−2H0+1并辨识有效head数；低秩扩展附录O(Hrd)，需其附加假设。
- Offline p.6：2d²−1次degree-H polynomial factorization（理论作为exact primitive），之外O(d²H³+d³H)运算、O(d²H)exact logs及比较；数值dense companion eigensolver使factorization也O(H³)，数值总算术O(d²H³+d³H)。不是bit complexity。
- Theorem5.2 p.6：近似oracle版本Q=4Hd²−2H+2d−1，多查询全部one-token；error≤C_stab τ，仅τ<τ0且模型/探针决定这些常数，无uniform conditioning保证；offline仍exact。
- 单层ReLU Transformer扩展（Theorem5.3，pp.6–7）：2(4Hd²−2H+1)仅是恢复奇部attention的查询；剩余ReLU重建另需搜索及符号配置消歧。附加非退化与Z单射条件下，定理保证几乎必然有限次查询终止并恢复全域等价函数，但未给完整Transformer的统一多项式查询/时间界。不能把此前Q当完整Transformer总成本。
- 附录G.3/Table3 p.37：180位oracle与offline，(d,H)=(128,8)、132,096 merged参数、524,273queries，100模型全成功，max E_param9.97e−110；8种尺寸总800模型<1e−100。
- 附录G.4/Tables5–6 p.39：相同方向和180位offline仅换binary64 responses，原算法(3,2)/(3,4)/(3,8)/(8,4)成功99/100、1/100、0/100、0/100；direct-one-token额外2d−2 queries为100/100、31/100、0/100、0/100。成功定义all H且E_param<1e−2。完整wallclock NR。

## 9. eprint-2026-1678

Cryptanalytic Extraction of Multi-Head Softmax Attention Models
源：https://eprint.iacr.org/2026/1678.pdf

- scalar continuous value oracle，canonical G有效heads、H已知上界，合并同W的heads、删零贡献。Theorem1 canonical identifiability §4；不恢复有gauge ambiguity的原Q/K/V因子。
- §4.6 pp.19–20阶段Q：d length-one得Σv；1 anchor atom set、d perturbations恢复v、d² sets恢复W，每set2H calls；Q=d+2H(1+d+d²)，max length2H+1。G=H时比generic merged参数P=G(d²+d)下界只常数倍；下界依赖每query scalar。
- coincident v的替代matching p.20需2H(1+2d+d²)queries，其量级仍O(Hd²)。rational-interpolation/roots/linear solves的整体显式算术T=NR；不能挪用另一篇精确T填入。
- biased single-head Transformer §5.5 pp.24–26：StageI FFN提取Q_FFN；StageII安全非退化two-token probes d²；总Q_FFN+d²（n_anc≥d时Q_FFN+n_anc d）。要求FFN primitive成功且g(q+u)−g(q)≠0，local affine区与独立anchors，不能推广深层Transformer。
- Table2 p.26：float64 d8,G=H6，no-refine43,284calls、参数误差2^-5.95/功能2^-4.09；refine45,012、2^-51.54/2^-50。d8,G5,H10 refine123,544calls、参数2^-49.19、功能2^-47。实测Q包括拒绝probe、过采样、校验和Gauss–Newton修正，比exact公式大很多；条件常数固定时作者仍称O(Hd²)。
- Table3 p.28：biased单头block d16,m32，Q_FFN42,542；n_anc16/32/64各Q_total42,798/43,054/43,566；n_anc32功能误差2^-25.89、参数2^-29.71。墙钟NR。
- 与2608.03294可在exact canonical scalar模型下比较Q常数；数值成功率不能直接横排，因为其训练victims/refinement vs随机模型/固定queries/180位offline流程不同。

## 10. arxiv-2608.06631

Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation
源：https://arxiv.org/pdf/2608.06631

- 直接full-vector isolated bias-free GLU f:R^n→R^n_out；已知结构，SwiGLU/GeGLU；不展示从final token API产生block input/output的方法。
- §3 pp.3–6：Stage0 finite-difference Hessian和antipodal observations；Stage1 rank-one direction candidates；1A odd-view幅度/coupling；1B even-view符号；Stage2 refinement/residual rescue；Stage3 scale selection+storage rounding。迭代优化离线总time complexity/普遍收敛定理=NR。
- §5 p.7明确query预算：coordinate Hessian4d n1²，n1=192,d=64得9,437,184calls；Stage1A/B 440,000 paired calls，candidate selector4,096，共9,881,280。Stage2、saved-residual repairs、factor polish复用观测0call；factor-polish selector另4,096；final disjoint evaluation4,096不计攻击预算。不得把paired calls再自行翻倍。
- full-input extension每步终点n_i成本4MK n_i，M8,K64，Qwen192→384→576→768→960→1024新增7,602,176，总17,483,456（pre-polish）；直接n1024 coordinate Hessian为268,435,456。
- Table4 p.8：Qwen3-0.6B抽取单个block的3072 hidden units、192输入/128输出，FP64 cast checkpoint，L0–L5 median forward8.2e−4至1.4e−3。Table5同页扩至1024输入、仍仅128/1024输出，polish后median3.91e−8至8.84e−6，training/guard calls477k–986k另计。
- §6.3 p.8 Gemma n1152,m6912,n_out1152全输入输出block，FP64 computation，forward median4.9e−3、p99 1.8e−2；不是完整Gemma。
- §6.6/§7 pp.9–10 Qwen BF16 execution stress：median4.6269%、p90 7.7392%；2,752,512恢复weights仅2.19% storage exact。所有有限精度run均非storage exact；单run、Gaussian block validation、不证明下游任务等价。
- 9.9–28.5M queries ×假设10–100ms所算27小时–33天是说明性估计，绝不能登记为实测wallclock。

## 11. arxiv-2403.06634

Stealing Part of a Production Language Model
源：https://arxiv.org/pdf/2403.06634

- oracle：实际token API的top-k logprobs+logit_bias，另有无logprob的bias版本。目标hidden dimension和最后output projection up to invertible transform；不恢复全模型参数。
- §4 pp.3–4：收集logit matrix，rank/SVD找h，UΣ获得W的等价基。n prompts须span h维；一次full-vector logit query和一次restricted API调用分开统计。原始SVD完整算术/墙钟显式界NR。
- §5.3 p.5：common-reference top-K，每query K−1新logits，1/(K−1)queries/logit。§5.4 top1不同反演。无logprobs binary search §F：N log(B/ε)，N logits、B gap bound、ε tolerance；更强方法含不同数值效果。
- Table4 p.7实际单logit恢复：top5/reference方法0.25queries/logit、23bits；理论5-logit方法实测0.64、11.5bits（数值不稳）；top1为1.0、6.1bits；无logprob one-of-n3.7、18bits。不能用理论1/5代替实测0.64。
- Table3 p.7：ada h1024已证，projection <2e7queries/$4、RMS5e−4；babbage h2048，<4e7/$12、RMS7e−4。GPT3.5-turbo-instruct投影<4e8/$2,000是估计且明确未实施；1106 <4e8/$8,000也估计未实施。维度实提取与整个投影估计成本不能混称完成攻击。金额是2024论文实验/估计，非当前价格。

## 12. arxiv-2403.09539

Logits of API-Protected LLMs Leak Proprietary Information
源：https://arxiv.org/pdf/2403.09539

- oracle/目标：logprob+logit_bias API，softmax bottleneck的image/输出空间/hidden dimension；CLR/Aitchison几何下low-dimensional probabilities，不宜错误描述为普通概率向量在欧式空间直接线性子空间。
- Table1/§3 pp.4–6：v vocabulary，k top-logprobs，d embedding dimension，n stochastic outputs。每full output普通logprob v/k calls、数值稳定reference v/(k−1)、stochastically robust期望n v/(k−2)；logprob-free对照v log(β_max/ε)。这些是API calls，不是算术T。
- §4 p.6 preprocessing收集d个独立输出，O(vd)API calls（忽略k）；Algorithm2 p.7缓存后写O(vd/k)，只dimension O(d²/k)。之后每新完整输出O(d)queries（保留k常数省略约定），还需本地解线性重构；本地算术显式阶/实测墙钟NR。不能把O(d)当首次恢复image成本。
- Table1 p.5示例v100000,d4096,k5,n4,ε1e−6,βmax100：单output20k/25k/133k API calls；image估计$410/$512/$2724；precomputed-image边际800calls。均back-of-envelope for gpt3.5-like API，不全是实付成本。
- §4/图2 p.7：Pythia70m/160m/410m维数512/768/1024，gpt3.5-turbo估计4096≤d≤4650（不要硬写exact4096）。通过image可以重建输出/识别变化，不意味着得到隐层权重或跨prompt生成完全等价的LLM。

## 13. arxiv-2608.28843 — 2026-10-28 直接核验增补

[Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks](https://arxiv.org/abs/2608.28843)，Munawar Hasan（NIST、Michigan Technological University）与 Apostol Vassilev（NIST）。8 月 28 日 v1、9 月 16 日 v2；预印本。本节为本轮实际下载的 [v2](https://arxiv.org/pdf/2608.28843v2) 核查，不改变前 12 条 9 月 30 日来源快照。25 页、1,188,439 字节，SHA-256 `8ee0b4ae84a3e960bdd4d6208d6d01dc4e4d18c0a7b2925869e64b302dcfd6d2`。

- **接口与对象**：§3 pp.4–6 为已知结构的两层 GELU/SiLU FFN，直接选择 post-LayerNorm 表示空间输入并获得完整模块向量输出，已知 d/k/m、激活与模块位置。非普通 token、仅标签或全网末端 logits 接口。
- **结构恢复**：§4 pp.6–10 将投影输入 Hessian 分解为共享对称秩一因子，估计 W1 单位方向，保留符号与排列歧义；尚无尺度、偏置、W2 或定向符号。Theorem 1 条件为 restricted Jacobian 单射，局部稳定性还受最小奇异值约束。d=64,m=128 时 T>=5 只是必要维数界，不是充分条件或全局优化保证。
- **阶段成本**：§5.1 Eq.(20) pp.11–12、Algorithm 1 p.14：P 个不同探测位置需 `P(2d^2+1)` 次完整向量模块调用。d=k=64,m=128,P=1,T=16 时只需 **8,193** 次；16 个投影在共享向量响应上离线计算，不是 16 份独立 stencil。§5.2 三次随机重启、按 Hessian 重建损失选择，无新增预言机调用但保留获取和离线优化代价。§5.3、Algorithm 2、§6 Eq.(26) 用 **12,000** 对自然模块输入/输出固定方向拟合其余参数，1,500 AdamW 步不再查询；默认合计 **20,193** 次，不是全分类器 API 预算。
- **实验**：§6 pp.15–18：CIFAR-10 ViT，4 blocks、4 heads、embedding64、FFN128，每种激活 3 个独立训练 victim。Table 2 均值±样本标准差：GELU/SiLU 方向绝对余弦 **0.9187±0.0138 / 0.9402±0.0119**；Hit_0.90 **0.8672±0.0234 / 0.9115±0.0325**；分类器一致率 **92.81±0.22% / 94.97±0.36%**；准确率下降 **1.24±0.23 / 0.57±0.09** 个百分点。另一个固定 victim 的攻击种子、每个 block 的测试与 privileged exact-Hessian ablation 分别报告，不拼接最佳行。
- **恢复边界**：§5.3、§6.3 仅替换一个拟合 FFN，保留完整分类器其余原参数，另有自然中间输入访问。逐 block 测试不代表联合提取和组合全 Transformer。近似方向与采样保真不认证严格函数等价、唯一原参数或完整参数恢复。§4.1 pre-LayerNorm 接口会多出归一化曲率；§7 gated/SwiGLU 需要更丰富分解，仍属后续工作。
- **精度与防御**：§6 clean h=0.01；全文未明确 numeric dtype，不能从硬件推断 float32/64。Table 8 pp.21–22 一个 GELU victim：四位小数舍入及高斯噪声 SD1e-4，在 h=0.01 时方向分数0.3255/0.3295，h=0.30 时0.9188/0.9081。每个 fresh h 重新花8,193次，l个需l×8,193；并非无额外预算或普遍防御失效证明。
- **时间/算术**：§5–6 给定优化器及硬件（Core Ultra9、64GB RAM、RTX4070 8GB、PyTorch2.5.1/CUDA12.4），未报告各阶段总算术界或独立墙钟时间，记 NR 而非零。结构阶段的“0额外query”只在 Hessian 已获得后成立。
- **代码**：p.1 footnote1 链接 [官方仓库固定版本](https://github.com/mhasan08/curvature-cryptanalysis/tree/2d9dd4f2bf1e8ca2939794ef1f3b8cdb93ea5534)，MIT 许可证已核；root 保留 separate-stencil 实现，optimized/ 对应共享模板。README 开头数字与其详细表不一致，因此论文数值取 v2 Table2。未安装依赖、收集权重或执行/复现代码。

## 页面实现建议

每条至少显示：paper_id、oracle、target_scope、model_dimensions、stage、query_formula、arithmetic_formula、reported_runtime、precision、conditioning_assumptions、empirical_metric、source_section、source_page、source_url、NR_reason。缺失值用null+NR_reason而不是0；“0新增query”才用0。把accepted-sample count、API calls、node queries、full-sequence queries、block vector queries定义为枚举单位；不要统一一个无单位“queries”柱图。每个实验row单独绑定尺寸/精度/方法，不把最大模型、最小Q、最佳误差拼成虚构一行。
