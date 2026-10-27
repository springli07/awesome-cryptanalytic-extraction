# 逐阶段横向对比

[English](comparison_en.md) · [中文](comparison_zh.md) · [Catalog](../README.md) · [原代码 / Original code](../code/README.md)

**54 papers / 篇 · 13 categories / 类 · checked 2026-10-28.**

NR = reviewed but not reported / 已核查未报告；NA = not applicable / 不适用；Derived = explicit inference / 明示推导。

Compare only equal oracles, targets, dimensions, precision and assumptions. Critical/dual points, samples, API calls, node responses and full-sequence responses are separate units. Arithmetic operations are not wall-clock or bit complexity. Stage reuse does not remove upstream acquisition costs. Sampled fidelity is not certified equivalence.

只在预言机、目标、尺寸、精度和假设相同时比较。临界点、双点、样本、API调用、节点响应和完整序列响应分别计量；算术次数不等于墙钟或位复杂度。复用阶段仍须计入前期获取成本，采样保真不认证严格等价。

## Full source-reviewed group reports / 分组完整证据

- [Foundations + raw outputs / 基础及原始输出](comparisons/raw.zh.md)
- [Hard-label + CNN / 仅标签及CNN](comparisons/hard-cnn.zh.md)
- [Activations, recurrent, attention, GLU and partial LLM / 扩展架构](comparisons/architecture.zh.md)
- [PPML, side channels, precision, defenses, theory and surveys / 上下文](comparisons/context.zh.md)

The full reviewed reports above preserve experimental protocols, failure cases, hardware and version caveats. The tables below summarize stage costs; they are not a speed leaderboard. / 完整稿保留实验协议、失败结果、硬件与版本限制；下表为阶段摘要，不是速度排行榜。

## 基础与早期工作 (3)

### arxiv-1609.02943: [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943)

Oracle / 预言机: Prediction scores / labels.

Scope / 范围: 方程求解及早期 API 提取，不是任意深网的精确恢复。

Assumptions / 假设: Invertible scores; independent inputs; known feature representation

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| binary logistic regression<br>notes: Arithmetic is derived only for standard dense Gaussian elimination, not a paper theorem. | d₀+1 [oracle_calls]<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | Derived / 推导: O(d₀³) [arithmetic_operations]<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) |
| MLP equation-solving experiment<br>notes: Experimental budget Q=αP is not a theoretical guarantee; nonconvex optimization. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | 11,125 [oracle_calls]<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) | 89 seconds (solver only) [wall_clock]<br>[§4.1.1–4.1.2 pp.5–6; Table4 p.6](https://arxiv.org/pdf/1609.02943v2) |

### arxiv-1909.01838: [High Accuracy and High Fidelity Extraction of Neural Networks](https://arxiv.org/abs/1909.01838)

Oracle / 预言机: Raw outputs / prediction queries.

Scope / 范围: 区分准确率与保真度，包含浅层等价恢复和混合攻击。

Assumptions / 假设: h<d₀; full row rank; chosen continuous inputs;64-bit raw logits

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| critical point acquisition | O(h log h) [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) |
| signature differences | O(d₀h) [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) |
| row signs | 3h [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) |
| output least squares<br>notes: Requires full-rank system; bias handling retained. | h (may reuse existing calls) [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | 0 additional queries [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) |
| total shallow recovery<br>notes: Paired model rows in Table6; special exponential query examples in Theorem1 prohibit generalization. | O(h log h+d₀h+h)=O(d₀h) [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | 2^17.2 /2^18.2 /2^19.2 /2^20.2 [oracle_calls]<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§6 pp.7–12;Appendix D p.18](https://arxiv.org/pdf/1909.01838v2) |

### arxiv-1910.00744: [Reverse-Engineering Deep ReLU Networks](https://arxiv.org/abs/1910.00744)

Oracle / 预言机: Real-valued queries.

Scope / 范围: 在假设下利用边界几何恢复结构及参数，允许网络对称性。

Assumptions / 假设: Linear Regions Assumption; connected boundaries intersect; nondegeneracy; sufficient adjacent region coverage

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| first-layer geometric boundary recovery<br>notes: Bounded biases,long lines,coupon collector and natural random assumptions;not worst-case. | O(d₀ N log d₁) expected/heuristic [oracle_calls]<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) |
| deep boundary traversal<br>notes: Intersections determine costs; no uniform end-to-end Q/A table; second-layer experiments leave weights unidentified. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4 pp.6–9;§5.1 p.10;§6 pp.12–13](https://arxiv.org/pdf/1910.00744v2) |

## 原始输出 ReLU 提取 (8)

### arxiv-2003.04884: [Cryptanalytic Extraction of Neural Network Models](https://arxiv.org/abs/2003.04884)

Oracle / 预言机: Raw outputs.

Scope / 范围: 差分临界点提取，依次恢复签名、符号与参数。

Assumptions / 假设: Known ReLU architecture;chosen continuous inputs;complete raw outputs

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| first-layer signature at isolated critical point<br>notes: Derived from coordinate finite differences; m≫N log N denotes point-pool size under uniform visibility, not Q. | Derived / 推导: O(d₀) [oracle_calls]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |
| general expanding-layer signs<br>notes: Reuses collected information; exponential local work does not imply exponential Q. Contractive case requires feasible preimages and rank. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | 2^dᵢ configurations × validation cost [arithmetic_operations]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |
| binary critical-point refinement<br>notes: Two-line intersection may avoid bisection only for an isolated verified kink; no general bit-complexity theorem. | approximately b calls for b precision bits [oracle_calls]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |
| end-to-end experiment | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | 2^21.5 [oracle_calls]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |
| end-to-end experiment | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | 2^18.5 [oracle_calls]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |
| end-to-end experiment | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | 2^17.8 [oracle_calls]<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.2–4.4 pp.10–19;§5 pp.20–25;Table1 p.4](https://arxiv.org/pdf/2003.04884v2) |

### eprint-2023-1526: [Polynomial Time Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2023/1526)

Oracle / 预言机: Raw outputs.

Scope / 范围: 多项式时间符号恢复，改进原始密码分析提取流程。

Assumptions / 假设: Signatures and correct prefixes given;visibility/statistical signal;rank;controllable projections

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| SOE signs | dᵢ+1 [oracle_calls]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | O(dᵢ³) [arithmetic_operations]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) |
| Neuron Wiggle signs<br>notes: Excludes signature collection,linearity checks and confidence retries. | 3s dᵢ [oracle_calls]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | O(s dᵢ Dᵢ³), Dᵢ=max(d₀,dᵢ) [arithmetic_operations]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) |
| last hidden layer signs | 4dL+1 [oracle_calls]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | O(dL DL³) [arithmetic_operations]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) |
| parallel sign estimate<br>notes: Not measured single-core end-to-end wall time. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) | approximately30 minutes (256-neuron parallel estimate) [wall_clock]<br>[§4.1 pp.15–16;§4.2 pp.16–19;§4.3 pp.20–21;§5.3 pp.24–27](https://eprint.iacr.org/2023/1526.pdf) |

### arxiv-2406.10011: [Beyond Slow Signs in High-fidelity Model Extraction](https://arxiv.org/abs/2406.10011)

Oracle / 预言机: Raw outputs.

Scope / 范围: 加速实际符号恢复，运行时间与查询量需分别评价。

Assumptions / 假设: Correct prefixes;signature visibility;low-confidence signs may need exponential fallback

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| sign trials<br>notes: Inherited Wiggle operation expression; s does not give uniform success guarantee. | 5 calls per trial (s=15 experimental choice) [oracle_calls]<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | O(s dᵢ Dᵢ³) [arithmetic_operations]<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) |
| difficult-sign fallback<br>notes: Parallelization does not remove exponential total work. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | 2^k subsequent-layer signature-recovery runs [arithmetic_operations]<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) |
| second-layer experiment<br>notes: Another training seed signature4649.95s; layer4/8 of784–16^8–1 only6/16,0/16 after36h. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | approximately3.05×10^6 [oracle_calls]<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) | signature496.2s;sign6.32s [wall_clock]<br>[§3.1–3.4 pp.4–7;Table1 p.8;Table2 pp.8–10](https://arxiv.org/pdf/2406.10011v1) |

### eprint-2026-296: [Navigating the Deep: End-to-End Extraction on Deep Neural Networks](https://eprint.iacr.org/2026/296)

Oracle / 预言机: Raw outputs.

Scope / 范围: 针对深层恢复瓶颈的端到端提取。

Assumptions / 假设: Known architecture;control/rank/visibility;search box radius10³;finite precision

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| signature filtering/intersection/refinement<br>notes: No complete stage Q/A expression; Table4 independent layers assume correct prefix. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |
| output linear layer<br>notes: Not zero whole-attack queries. | 0 additional calls (reuse) [oracle_calls]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |
| end-to-end signatures | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 2^29.42 [oracle_calls]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 19h18m [wall_clock]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |
| end-to-end signs | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 2^27.68 [oracle_calls]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 12m36s [wall_clock]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |
| end-to-end signatures | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 2^27.44 [oracle_calls]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 1h43m [wall_clock]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |
| end-to-end signs | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 2^26.77 [oracle_calls]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) | 4m2s [wall_clock]<br>[§3 pp.14–19;§4 pp.20–22;Table5 p.28;error p.29](https://arxiv.org/pdf/2506.17047v2) |

### eprint-2026-1025: [Geometric Critical Point Screening: Clustering-Free Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2026/1025)

Oracle / 预言机: Raw outputs.

Scope / 范围: 历史方法：几何筛选早期层签名；2026年9月19日已撤回，保留历史记录，不作为现行未撤回结果。

**WITHDRAWN 2026-09-19 / 已撤回；以下仅为历史版本声明。**

Assumptions / 假设: Known architecture;raw continuous outputs;d₀≥d₁ and full row rank;uniform visibility

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| historical geometric screening<br>notes: Assumes constant-time midpoint verification;excludes acquisition,precision,retries,index building,dimension operations. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | approximately O(N²) [arithmetic_operations]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |
| historical selected signatures<br>notes: Ideal target-only signature calculation;not total Q. Baseline O(&#124;S&#124;d₀) signature calls and O(&#124;S&#124;²) clustering. | O(d₁d₀) [oracle_calls]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |
| historical first-layer signatures<br>notes: Second layer uses true first-layer parameters;not end-to-end;withdrawn historical result. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 2^16.66 [oracle_calls]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 3.5s [wall_clock]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |
| historical first-layer signatures<br>notes: Second layer uses true first-layer parameters;not end-to-end;withdrawn historical result. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 2^18.28 [oracle_calls]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 25s [wall_clock]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |
| historical second-layer signatures<br>notes: Second layer uses true first-layer parameters;not end-to-end;withdrawn historical result. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 2^14.48 [oracle_calls]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 16s [wall_clock]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |
| historical second-layer signatures<br>notes: Second layer uses true first-layer parameters;not end-to-end;withdrawn historical result. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 2^17.02 [oracle_calls]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) | 43s [wall_clock]<br>[§3.3 pp.9–12;§4.3 pp.13–15;Tables1–2 pp.16–18](https://eprint.iacr.org/archive/2026/1025/1779420008.pdf) |

### arxiv-2609.14379: [Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption](https://arxiv.org/abs/2609.14379)

Oracle / 预言机: Raw outputs; architecture unknown.

Scope / 范围: v2: zero-suffix signature and equality-pattern sign routes infer hidden widths; fixed output coefficients and a global linear relation handle the second-to-last layer. Raw-output ReLU MLP experiments include dagger-marked true-sign-assisted rows; not general CNN/Transformer recovery. / v2：签名零后缀与符号等值模式推断隐藏宽度；固定输出系数及全局线性关系处理倒数第二层。原始输出 ReLU MLP 实验中 † 行使用真实符号辅助，非一般 CNN/Transformer 恢复。

Assumptions / 假设: Only input/output dimensions known;raw output;continuous inputs;signature route rank;sign route non-expanding

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| architecture width search<br>notes: §4.3 discusses linear-in-width baseline multiplier;no complete uniform Q/A;critical points may be reused. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) |
| last-layer candidate fitting<br>notes: Proposition2 excludes always-inactive neurons and zero output connections;finite residual not global certificate. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) |
| signature-route experiment<br>notes: Three other dagger-marked rows use true signs and must not be called full black-box. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | 2^23.7 [oracle_calls]<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | 9036.6s [wall_clock]<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) |
| sign-route experiment | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | 2^23.0 [oracle_calls]<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) | 2640.5s [wall_clock]<br>[§4.3 p.12;Lemma1 p.14;Proposition1 p.15;Table1 pp.21–24](https://arxiv.org/pdf/2609.14379v2) |

### eprint-2026-2127: [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Limited Architecture Knowledge Setting](https://eprint.iacr.org/2026/2127)

Oracle / 预言机: Raw logits; limited architecture knowledge.

Scope / 范围: Withdrawn October 1, 2026; retained historically. Omission detection/backtracking used raw logits and approximate total neuron scale; overall runtime/query costs were not reported. / 2026 年 10 月 1 日已撤回，保留历史记录。原方法以原始 logits 检测遗漏并回溯，仍需大致神经元规模；未报告总体时间与查询成本。

**WITHDRAWN 2026-10-01 / 已撤回；以下仅为历史版本声明。**

Assumptions / 假设: Rough total neuron count known;raw logits;continuous inputs;64-bit

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| initial critical-point pool<br>notes: O(N log N) points under sampling strategy is not a proved end-to-end oracle bound. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) |
| cached rank test<br>notes: Only given H′ and α;building α,resampling,backtracking and total arithmetic NR. | Derived / 推导: 0 additional calls [oracle_calls]<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) |
| overall extraction<br>notes: §4.4 explicitly omits overall query/runtime costs; inherited polynomial primitives do not bound retries. | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [arithmetic_operations]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [oracle_calls]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) | NR [wall_clock]<br>Reviewed cited method/complexity/experiment sections; no independent value for this stage reported.<br>[§3.2 p.14;Algorithm1 p.17;§4.1 p.18;Table3 pp.19–20;§4.4 p.21](https://eprint.iacr.org/2026/2127.pdf) |

### arxiv-2609.35487: [Beyond Scalar Probes: Exploiting Vector-Valued Outputs in ReLU Networks For Signature Extraction](https://arxiv.org/abs/2609.35487)

Oracle / 预言机: Raw vector-valued outputs; signature-estimation stage.

Scope / 范围: Rank-one Jacobian differences expose row and column signatures; SVD pooling improves float32 estimates. Experiments isolate signature/normalized-bias estimation after critical-point acquisition; no sign resolution, backward extraction or complete model attack. / 秩一 Jacobian 差揭示行列签名，SVD 汇聚改善 float32 估计。实验隔离临界点获取之后的签名及归一化偏置估计；未完成符号定向、反向提取或完整模型攻击。

Assumptions / 假设: Adjacent affine cells with one nonzero visible neuron transition; raw vector outputs; critical point already acquired; adaptive cell tests are heuristic.

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| J-vector-fixed 签名与归一化偏置估计<br>dimensions: 784 input; one hidden layer of width 8 or 32; raw vector output<br>precision: simulated float64/float32/float16 in forward pass and finite differences<br>target: signature direction and normalized hyperplane offset, not physical bias or oriented weights<br>notes: Full-vector oracle calls after a supplied estimated critical point; median across widths 8/32 in Table 1. Does not include critical-point search or complete extraction. SVD row pooling leaves global sign/scale ambiguity. Float16 usable-transition rate is only 2.4% random / 1.1% trained; conditional accepted-trial medians are not whole-attack success rates. | NR [oracle_calls]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§4, pp.15–22; §5.1–5.2, Tables 1–2, pp.22–26](https://arxiv.org/pdf/2609.35487v1) | NR [arithmetic_operations]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§4, pp.15–22; §5.1–5.2, Tables 1–2, pp.22–26](https://arxiv.org/pdf/2609.35487v1) | 1,570 [oracle_calls]<br>[§4, pp.15–22; §5.1–5.2, Tables 1–2, pp.22–26](https://arxiv.org/pdf/2609.35487v1) | NR [wall_clock]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§4, pp.15–22; §5.1–5.2, Tables 1–2, pp.22–26](https://arxiv.org/pdf/2609.35487v1) |

## 仅标签提取 (7)

### eprint-2024-1403: [Hard-Label Cryptanalytic Extraction of Neural Network Models](https://eprint.iacr.org/2024/1403)

Oracle / 预言机: top-1 binary label.

Scope / 范围: 正尺度输出函数

Assumptions / 假设: 已知ReLU FC架构、任意实数输入；n=隐藏神经元总数，k=隐藏层数。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A/B 边界点与局部仿射恢复<br>notes: 采样预算c_n2^n；不是按参数数计。 | O(d₀ 2^n log(1/ϵ)) [oracle_calls]<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | NR [arithmetic_operations]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | NR [oracle_calls]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | NR [wall_time]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) |
| C/D/E 候选分配、符号猜测、线性求解<br>notes: 作者简化操作计数；忽略线性系统大小差异；不是bit complexity。 | NR [oracle_calls]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | O(n·2^(n²+n+k)) [arithmetic_operations]<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | NR [oracle_calls]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) | NR [wall_time]<br>已检查 Appendix B pp.27–28；未给该阶段独立可引用界或数值。<br>[Appendix B pp.27–28](https://eprint.iacr.org/2024/1403.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 25120-4-1; 100,489 parameters; precision: 10^-16; hardware: NR; target: 正尺度输出函数 | 2^26.67 [oracle_calls]<br>[§7 Table 1](https://eprint.iacr.org/2024/1403.pdf) | NR [wall_time]<br>已检查 §7 Table 1；未单列该项实验指标。<br>[§7 Table 1](https://eprint.iacr.org/2024/1403.pdf) | PMR=100%<br>单核数小时为概述；精确硬件/独立阶段时间NR。 |

### eprint-2024-1580: [Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Extended Version)](https://eprint.iacr.org/2024/1580)

Oracle / 预言机: top-1 label.

Scope / 范围: ReLU MLP签名、符号、输出与结构

Assumptions / 假设: 双点可见性、均匀性、非退化；近死/持久神经元可使采点指数增长。48页扩展版。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A 双点与交空间获取<br>notes: 作者条件性poly；双点量不是oracle Q。 | NR [oracle_calls]<br>已检查 §4; §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§4; §9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [arithmetic_operations]<br>已检查 §4; §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§4; §9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [oracle_calls]<br>已检查 §4; §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§4; §9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [wall_time]<br>已检查 §4; §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§4; §9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) |
| B/C 朴素聚类与签名<br>notes: 单位是consistency tests，每次另含多项式线性代数，非完整算术阶。 | NR [oracle_calls]<br>已检查 §5；未给该阶段独立可引用界或数值。<br>[§5](https://eprint.iacr.org/2024/1580.pdf) | O(Q_dp²) consistency tests [consistency_tests]<br>[§5](https://eprint.iacr.org/2024/1580.pdf) | NR [oracle_calls]<br>已检查 §5；未给该阶段独立可引用界或数值。<br>[§5](https://eprint.iacr.org/2024/1580.pdf) | NR [wall_time]<br>已检查 §5；未给该阶段独立可引用界或数值。<br>[§5](https://eprint.iacr.org/2024/1580.pdf) |
| D/E Future Toggle与输出层<br>notes: 独立阶段oracle Big-O NR。 | NR [oracle_calls]<br>已检查 §6; §8；未给该阶段独立可引用界或数值。<br>[§6; §8](https://eprint.iacr.org/2024/1580.pdf) | NR [arithmetic_operations]<br>已检查 §6; §8；未给该阶段独立可引用界或数值。<br>[§6; §8](https://eprint.iacr.org/2024/1580.pdf) | NR [oracle_calls]<br>已检查 §6; §8；未给该阶段独立可引用界或数值。<br>[§6; §8](https://eprint.iacr.org/2024/1580.pdf) | NR [wall_time]<br>已检查 §6; §8；未给该阶段独立可引用界或数值。<br>[§6; §8](https://eprint.iacr.org/2024/1580.pdf) |
| F 架构与停止<br>notes: 均匀双点下已知宽度O(d log d)、未知宽度O(d²(log d+log(1/δ)))双点；不是oracle Q。 | NR [oracle_calls]<br>已检查 §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [arithmetic_operations]<br>已检查 §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [oracle_calls]<br>已检查 §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) | NR [wall_time]<br>已检查 §9.1–9.2；未给该阶段独立可引用界或数值。<br>[§9.1–9.2](https://eprint.iacr.org/2024/1580.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 32-32-32-32-10; precision: NR; hardware: 32-core machine; target: ReLU MLP签名、符号、输出与结构 | 3.97×10^7 [oracle_calls]<br>[§8 Tables 4–5](https://eprint.iacr.org/2024/1580.pdf) | 74 seconds [wall_time]<br>[§8 Tables 4–5](https://eprint.iacr.org/2024/1580.pdf) | 96/96 signatures and signs; max layer relative error 4×10^-14<br>Dual acquisition Q=2.02×10^7; 6,880 duals; 100,000随机及边界两侧输入验证。 |
| dimensions: 3072-256×3-64-10; precision: NR; hardware: 256 cores / GPU support; target: 辅助符号梯度的概念验证 | NR [oracle_calls]<br>已检查 §7；未单列该项实验指标。<br>[§7](https://eprint.iacr.org/2024/1580.pdf) | signature ≈16 h; sign ≈8.5 h [wall_time]<br>[§7](https://eprint.iacr.org/2024/1580.pdf) | None<br>省略大规模聚类计时，不是全黑盒端到端。 |

### eprint-2025-1118: [Extracting Some Layers of Deep Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2025/1118)

Oracle / 预言机: top-1 label.

Scope / 范围: 给定前缀与无符号签名后的sign/输出层

Assumptions / 假设: 第一层满行秩或深层局部前缀秩≥dᵢ，扰动不切换已恢复层；q_T/t_T为transition point成本。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| D freeze<br>notes: T=dᵢ(t_T+t₁)是含采点时间的混合时间公式，不能当纯算术。 | dᵢ(q_T+2) [oracle_calls]<br>[§4.2](https://eprint.iacr.org/2025/1118.pdf) | NR [arithmetic_operations]<br>已检查 §4.2；未给该阶段独立可引用界或数值。<br>[§4.2](https://eprint.iacr.org/2025/1118.pdf) | NR [oracle_calls]<br>已检查 §4.2；未给该阶段独立可引用界或数值。<br>[§4.2](https://eprint.iacr.org/2025/1118.pdf) | NR [wall_time]<br>已检查 §4.2；未给该阶段独立可引用界或数值。<br>[§4.2](https://eprint.iacr.org/2025/1118.pdf) |
| D SOE<br>notes: T=(dᵢ+1)t_T+t₁；已有法向量m时新增Q=0，伪逆与矩阵向量乘仍需本地计算。 | (dᵢ+1)q_T [oracle_calls]<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [arithmetic_operations]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [oracle_calls]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [wall_time]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) |
| D SOE复用已知m<br>notes: 仅新增查询；不含上游采点。 | 0 [oracle_calls]<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [arithmetic_operations]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [oracle_calls]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) | NR [wall_time]<br>已检查 §4.3；未给该阶段独立可引用界或数值。<br>[§4.3](https://eprint.iacr.org/2025/1118.pdf) |
| E 输出层<br>notes: 作者给poly；最大秩K(d_r+1)−(d_r+2)，有共同平移/尺度规范。 | NR [oracle_calls]<br>已检查 §3.2–3.3；未给该阶段独立可引用界或数值。<br>[§3.2–3.3](https://eprint.iacr.org/2025/1118.pdf) | NR [arithmetic_operations]<br>已检查 §3.2–3.3；未给该阶段独立可引用界或数值。<br>[§3.2–3.3](https://eprint.iacr.org/2025/1118.pdf) | NR [oracle_calls]<br>已检查 §3.2–3.3；未给该阶段独立可引用界或数值。<br>[§3.2–3.3](https://eprint.iacr.org/2025/1118.pdf) | NR [wall_time]<br>已检查 §3.2–3.3；未给该阶段独立可引用界或数值。<br>[§3.2–3.3](https://eprint.iacr.org/2025/1118.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 3072-256×3-64-10; precision: NR; hardware: NR; target: 已恢复隐层后的输出层 | NR [oracle_calls]<br>已检查 §5 Table 1；未单列该项实验指标。<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | equation acquisition 6.5 h; solve <1 s [wall_time]<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | 5,000 U(-1,1) label agreement 100%<br> |
| dimensions: 3072-256×3-64-10; precision: NR; hardware: NR; target: 第一层sign | NR [oracle_calls]<br>已检查 §5 Table 1；未单列该项实验指标。<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | freeze 33.41 s; SOE reconstruct normals 358.27 s; reuse m <1 s [wall_time]<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | None<br> |
| dimensions: 3072-1000-350-100-30-10; precision: NR; hardware: NR; target: sign与输出分阶段；非完整攻击 | NR [oracle_calls]<br>已检查 §5 Table 1；未单列该项实验指标。<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | SOE with m: 0.50/0.30/0.23/0.22 s; output equations ≈13 h [wall_time]<br>[§5 Table 1](https://eprint.iacr.org/2025/1118.pdf) | None<br> |

### eprint-2025-1868: [Is the Hard-Label Cryptanalytic Model Extraction Really Polynomial?](https://eprint.iacr.org/2025/1868)

Oracle / 预言机: top-1 label / noiseless intersection spaces.

Scope / 范围: persistent方向或span及等价表示

Assumptions / 假设: ε-dead/persistent相对输入分布；ε<1/N在预算N下通常不可见；交点无噪声假设。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A 可观察性<br>notes: 深度切换稀少为训练网络实证，不是所有自适应算法指数下界。 | NR [oracle_calls]<br>已检查 §4.2–4.4；未给该阶段独立可引用界或数值。<br>[§4.2–4.4](https://eprint.iacr.org/2025/1868.pdf) | NR [arithmetic_operations]<br>已检查 §4.2–4.4；未给该阶段独立可引用界或数值。<br>[§4.2–4.4](https://eprint.iacr.org/2025/1868.pdf) | NR [oracle_calls]<br>已检查 §4.2–4.4；未给该阶段独立可引用界或数值。<br>[§4.2–4.4](https://eprint.iacr.org/2025/1868.pdf) | NR [wall_time]<br>已检查 §4.2–4.4；未给该阶段独立可引用界或数值。<br>[§4.2–4.4](https://eprint.iacr.org/2025/1868.pdf) |
| B/C 初始三元搜索<br>notes: n=候选交空间数；完整特征问题维度及全流程界NR。 | NR [oracle_calls]<br>已检查 §5.1；未给该阶段独立可引用界或数值。<br>[§5.1](https://eprint.iacr.org/2025/1868.pdf) | O(n³) [arithmetic_operations]<br>[§5.1](https://eprint.iacr.org/2025/1868.pdf) | NR [oracle_calls]<br>已检查 §5.1；未给该阶段独立可引用界或数值。<br>[§5.1](https://eprint.iacr.org/2025/1868.pdf) | NR [wall_time]<br>已检查 §5.1；未给该阶段独立可引用界或数值。<br>[§5.1](https://eprint.iacr.org/2025/1868.pdf) |
| D/E 等价线性贡献吸收<br>notes: 多个persistent只辨span不辨原基；分类概率≥1−(n+m)ε有分布限定。 | NR [oracle_calls]<br>已检查 §5.2–5.3; §6；未给该阶段独立可引用界或数值。<br>[§5.2–5.3; §6](https://eprint.iacr.org/2025/1868.pdf) | NR [arithmetic_operations]<br>已检查 §5.2–5.3; §6；未给该阶段独立可引用界或数值。<br>[§5.2–5.3; §6](https://eprint.iacr.org/2025/1868.pdf) | NR [oracle_calls]<br>已检查 §5.2–5.3; §6；未给该阶段独立可引用界或数值。<br>[§5.2–5.3; §6](https://eprint.iacr.org/2025/1868.pdf) | NR [wall_time]<br>已检查 §5.2–5.3; §6；未给该阶段独立可引用界或数值。<br>[§5.2–5.3; §6](https://eprint.iacr.org/2025/1868.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: width 64/128/256; layer 4 has 1/2/13 persistent neurons; precision: NR; hardware: NR; target: 借第5层交空间验证局部span | NR [oracle_calls]<br>已检查 §5–6；未单列该项实验指标。<br>[§5–6](https://eprint.iacr.org/2025/1868.pdf) | NR [wall_time]<br>已检查 §5–6；未单列该项实验指标。<br>[§5–6](https://eprint.iacr.org/2025/1868.pdf) | max principal angle ≈10^-8<br>20×256 MNIST/FMNIST仅切换稀少分析，不是全网恢复。 |

### eprint-2026-1164: [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](https://eprint.iacr.org/2026/1164)

Oracle / 预言机: hard-label normals; 部分黑盒辅助实验.

Scope / 范围: NRC/ASV签名聚类

Assumptions / 假设: n=已采双点数；d=目标维度；平均界要求均匀d簇，false-negative可补采。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| B 原rank-check基线 | NR [oracle_calls]<br>已检查 §3.2 Eq18；未给该阶段独立可引用界或数值。<br>[§3.2 Eq18](https://eprint.iacr.org/2026/1164.pdf) | O(n²d³) [arithmetic_operations]<br>[§3.2 Eq18](https://eprint.iacr.org/2026/1164.pdf) | NR [oracle_calls]<br>已检查 §3.2 Eq18；未给该阶段独立可引用界或数值。<br>[§3.2 Eq18](https://eprint.iacr.org/2026/1164.pdf) | NR [wall_time]<br>已检查 §3.2 Eq18；未给该阶段独立可引用界或数值。<br>[§3.2 Eq18](https://eprint.iacr.org/2026/1164.pdf) |
| B 局部求解预处理 | NR [oracle_calls]<br>已检查 §4.4；未给该阶段独立可引用界或数值。<br>[§4.4](https://eprint.iacr.org/2026/1164.pdf) | O(nd³) [arithmetic_operations]<br>[§4.4](https://eprint.iacr.org/2026/1164.pdf) | NR [oracle_calls]<br>已检查 §4.4；未给该阶段独立可引用界或数值。<br>[§4.4](https://eprint.iacr.org/2026/1164.pdf) | NR [wall_time]<br>已检查 §4.4；未给该阶段独立可引用界或数值。<br>[§4.4](https://eprint.iacr.org/2026/1164.pdf) |
| B NRC/ASV匹配（含预处理）<br>notes: 匹配O(d)/次；均匀簇平均O(nd²)，最坏O(n²d)。深层约1.2×点保持覆盖，总Q可增。 | 0 additional calls with cached normals [oracle_calls]<br>[§4.4–4.5](https://eprint.iacr.org/2026/1164.pdf) | average O(nd³+nd²); worst O(nd³+n²d) [arithmetic_operations]<br>[§4.4–4.5](https://eprint.iacr.org/2026/1164.pdf) | NR [oracle_calls]<br>已检查 §4.4–4.5；未给该阶段独立可引用界或数值。<br>[§4.4–4.5](https://eprint.iacr.org/2026/1164.pdf) | NR [wall_time]<br>已检查 §4.4–4.5；未给该阶段独立可引用界或数值。<br>[§4.4–4.5](https://eprint.iacr.org/2026/1164.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 64-64×4-10; F1; precision: NR; hardware: RTX5080 16GB; target: F1 signature | 2^24.30 [oracle_calls]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | 0.05 h [wall_time]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | None<br>基线0.92h。 |
| dimensions: 64-64×4-10; F2; precision: NR; hardware: RTX5080 16GB; target: F2 signature | 2^30.76 [oracle_calls]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | 4.22 h [wall_time]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | None<br>基线1478.55h是外推；F3仅26/64。 |
| dimensions: max-pool LeNet-5 convolution block; precision: NR; hardware: RTX5080 16GB; target: 卷积签名 | 2^30.96 [oracle_calls]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | 12.65 h [wall_time]<br>[§6 Tables1–3](https://eprint.iacr.org/2026/1164.pdf) | None<br> |

### arxiv-2609.18751: [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751)

Oracle / 预言机: hard-label;部分实验真参数法向量.

Scope / 范围: 给定双点/签名/前缀后的sign

Assumptions / 假设: 后缀分布/投影；eSOE需正确非活跃删除、非零活跃系数、rank &#124;U&#124;−1。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| D normal alignment与eSOE<br>notes: 普通alignment复用法向量；eSOE需兼容transition points；可能exhaustive fallback；统一整网Q界NR。 | NR [oracle_calls]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://arxiv.org/pdf/2609.18751) | NR [arithmetic_operations]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://arxiv.org/pdf/2609.18751) | NR [oracle_calls]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://arxiv.org/pdf/2609.18751) | NR [wall_time]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://arxiv.org/pdf/2609.18751) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 192-64×8-10 CIFAR; precision: NR; hardware: NR; target: 512/512 signs with true-parameter normals | Derived / 推导: 2^31.13 [oracle_calls]<br>[§6 Table1](https://arxiv.org/pdf/2609.18751) | ≈2^10.73 seconds [wall_time]<br>[§6 Table1](https://arxiv.org/pdf/2609.18751) | 512/512 signs<br>论文估算Q，非实际黑盒计数；每神经元200尝试。 |
| dimensions: 64-96×3-32-10 MNIST; precision: NR; hardware: NR; target: hard-label sign recovery | 2^28.71 [oracle_calls]<br>[§6 Table1](https://arxiv.org/pdf/2609.18751) | ≈2^11.20 seconds [wall_time]<br>[§6 Table1](https://arxiv.org/pdf/2609.18751) | 320/320 signs<br> |
| dimensions: 3072-256×3-64-10; precision: NR; hardware: 8 CPU cores; no neuron-level parallelism; target: true-normal sign proof of concept | NR [oracle_calls]<br>已检查 §6; Appendix A；未单列该项实验指标。<br>[§6; Appendix A](https://arxiv.org/pdf/2609.18751) | 1 h 43 m [wall_time]<br>[§6; Appendix A](https://arxiv.org/pdf/2609.18751) | 832/832 signs<br> |

### arxiv-2609.21941: [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/abs/2609.21941)

Oracle / 预言机: top-1 hard label.

Scope / 范围: 小型已知架构ReLU MLP端到端

Assumptions / 假设: Proposition1需包含全部活跃竞争者、竞争span秩小于前缀秩、目标不落其span；实验排除死/近死。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A/B/C 交空间获取、伪组筛除与签名<br>notes: 4层20,000、6层400,000交空间不是Q；预收集占主要总查询。 | NR [oracle_calls]<br>已检查 §4.1–4.3; Appendix H；未给该阶段独立可引用界或数值。<br>[§4.1–4.3; Appendix H](https://arxiv.org/pdf/2609.21941v1v1) | NR [arithmetic_operations]<br>已检查 §4.1–4.3; Appendix H；未给该阶段独立可引用界或数值。<br>[§4.1–4.3; Appendix H](https://arxiv.org/pdf/2609.21941v1v1) | NR [oracle_calls]<br>已检查 §4.1–4.3; Appendix H；未给该阶段独立可引用界或数值。<br>[§4.1–4.3; Appendix H](https://arxiv.org/pdf/2609.21941v1v1) | NR [wall_time]<br>已检查 §4.1–4.3; Appendix H；未给该阶段独立可引用界或数值。<br>[§4.1–4.3; Appendix H](https://arxiv.org/pdf/2609.21941v1v1) |
| D cosine/projection signs<br>notes: 复用已给交空间/签名；其余条件用统计判别与span-violation纠错。 | 0 additional calls [oracle_calls]<br>[§3 Proposition1](https://arxiv.org/pdf/2609.21941v1v1) | NR [arithmetic_operations]<br>已检查 §3 Proposition1；未给该阶段独立可引用界或数值。<br>[§3 Proposition1](https://arxiv.org/pdf/2609.21941v1v1) | NR [oracle_calls]<br>已检查 §3 Proposition1；未给该阶段独立可引用界或数值。<br>[§3 Proposition1](https://arxiv.org/pdf/2609.21941v1v1) | NR [wall_time]<br>已检查 §3 Proposition1；未给该阶段独立可引用界或数值。<br>[§3 Proposition1](https://arxiv.org/pdf/2609.21941v1v1) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: MNIST 784-16×4-10; precision: NR; hardware: NR; target: 小型已知架构ReLU MLP端到端 | 2^32.31 [oracle_calls]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | NR [wall_time]<br>已检查 §4 Table3；未单列该项实验指标。<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | 100,000 standard Gaussian label agreement 98.477%<br>预收集墙钟NR；不能把signature/sign相加当完整总时间。max signature L2 error 9.34×10^-6；未测试persistent恢复。 |
| dimensions: MNIST 784-16×6-10; precision: NR; hardware: NR; target: 小型已知架构ReLU MLP端到端 | 2^36.62 [oracle_calls]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | signature 1h05m36s; sign 26m34s [wall_time]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | 100,000 standard Gaussian label agreement 99.948%<br>预收集墙钟NR；不能把signature/sign相加当完整总时间。max signature L2 error 9.34×10^-6；未测试persistent恢复。 |
| dimensions: FMNIST 784-16×4-10; precision: NR; hardware: NR; target: 小型已知架构ReLU MLP端到端 | 2^32.30 [oracle_calls]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | NR [wall_time]<br>已检查 §4 Table3；未单列该项实验指标。<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | 100,000 standard Gaussian label agreement 100.000%<br>预收集墙钟NR；不能把signature/sign相加当完整总时间。max signature L2 error 9.34×10^-6；未测试persistent恢复。 |
| dimensions: FMNIST 784-16×6-10; precision: NR; hardware: NR; target: 小型已知架构ReLU MLP端到端 | 2^36.62 [oracle_calls]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | signature 47m04s; sign 30m16s [wall_time]<br>[§4 Table3](https://arxiv.org/pdf/2609.21941v1v1) | 100,000 standard Gaussian label agreement 99.744%<br>预收集墙钟NR；不能把signature/sign相加当完整总时间。max signature L2 error 9.34×10^-6；未测试persistent恢复。 |

## CNN 与池化 (5)

### eprint-2026-139: [Cryptanalytic Extraction of Convolutional Neural Networks](https://eprint.iacr.org/2026/139)

Oracle / 预言机: top-1 hard label.

Scope / 范围: 已知平均池化CNN单层签名

Assumptions / 假设: kernel均匀采样才有coupon-collector设计指导；r=3,δ=.02；非均匀98%不是保证。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| B kernel-centric clustering<br>notes: 单次搜索线性，整流程还乘簇数、rank tests/refinement；m≥C_out[ln C_out+(r−1)ln ln C_out+ln(1/δ)]为覆盖设计点数。 | NR [oracle_calls]<br>已检查 §3.3 Algorithm1 Eq10；未给该阶段独立可引用界或数值。<br>[§3.3 Algorithm1 Eq10](https://eprint.iacr.org/2026/139.pdf) | NR [arithmetic_operations]<br>已检查 §3.3 Algorithm1 Eq10；未给该阶段独立可引用界或数值。<br>[§3.3 Algorithm1 Eq10](https://eprint.iacr.org/2026/139.pdf) | NR [oracle_calls]<br>已检查 §3.3 Algorithm1 Eq10；未给该阶段独立可引用界或数值。<br>[§3.3 Algorithm1 Eq10](https://eprint.iacr.org/2026/139.pdf) | NR [wall_time]<br>已检查 §3.3 Algorithm1 Eq10；未给该阶段独立可引用界或数值。<br>[§3.3 Algorithm1 Eq10](https://eprint.iacr.org/2026/139.pdf) |
| C 协方差特征分解<br>notes: n×p矩阵改DᵀD的p×p分解并分块累积；不改变采点Q。 | NR [oracle_calls]<br>已检查 §3.4 Eq11；未给该阶段独立可引用界或数值。<br>[§3.4 Eq11](https://eprint.iacr.org/2026/139.pdf) | NR [arithmetic_operations]<br>已检查 §3.4 Eq11；未给该阶段独立可引用界或数值。<br>[§3.4 Eq11](https://eprint.iacr.org/2026/139.pdf) | NR [oracle_calls]<br>已检查 §3.4 Eq11；未给该阶段独立可引用界或数值。<br>[§3.4 Eq11](https://eprint.iacr.org/2026/139.pdf) | NR [wall_time]<br>已检查 §3.4 Eq11；未给该阶段独立可引用界或数值。<br>[§3.4 Eq11](https://eprint.iacr.org/2026/139.pdf) |
| D/E sign与输出<br>notes: 完整端到端证据及独立公式NR。 | NR [oracle_calls]<br>已检查 §4.2 Tables1–2；未给该阶段独立可引用界或数值。<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) | NR [arithmetic_operations]<br>已检查 §4.2 Tables1–2；未给该阶段独立可引用界或数值。<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) | NR [oracle_calls]<br>已检查 §4.2 Tables1–2；未给该阶段独立可引用界或数值。<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) | NR [wall_time]<br>已检查 §4.2 Tables1–2；未给该阶段独立可引用界或数值。<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: LeNet-5 average pooling target layer; precision: NR; hardware: Intel i7;16GB;RTX3060; target: single-layer signature | 2^32.34 [oracle_calls]<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) | 2^19.39 seconds [wall_time]<br>[§4.2 Tables1–2](https://eprint.iacr.org/2026/139.pdf) | error 2^-17.75<br>≈190.84h；最大2^9.26 speedup含外推基线。 |

### eprint-2026-241: [Algebraic Attack on Convolutional Neural Networks with Max Pooling](https://eprint.iacr.org/2026/241)

Oracle / 预言机: raw real outputs.

Scope / 范围: max-pool CNN卷积块/reduced全网/partial Full LeNet

Assumptions / 假设: RPCP与PSP分开；PSP不泄漏共享bias，每核至少一个RPCP。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| B/C RPCP/PSP签名核系统<br>notes: RPCP d^(k)变量，PSP l_c变量；作者poly但完整展开NR。 | NR [oracle_calls]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://eprint.iacr.org/2026/241.pdf) | NR [arithmetic_operations]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://eprint.iacr.org/2026/241.pdf) | NR [oracle_calls]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://eprint.iacr.org/2026/241.pdf) | NR [wall_time]<br>已检查 §4–5；未给该阶段独立可引用界或数值。<br>[§4–5](https://eprint.iacr.org/2026/241.pdf) |
| D/E bias与定向<br>notes: 10,000第二层点仅15 RPCP与1548 PSP；稀少RPCP仍瓶颈。 | NR [oracle_calls]<br>已检查 §6.1; §7；未给该阶段独立可引用界或数值。<br>[§6.1; §7](https://eprint.iacr.org/2026/241.pdf) | NR [arithmetic_operations]<br>已检查 §6.1; §7；未给该阶段独立可引用界或数值。<br>[§6.1; §7](https://eprint.iacr.org/2026/241.pdf) | NR [oracle_calls]<br>已检查 §6.1; §7；未给该阶段独立可引用界或数值。<br>[§6.1; §7](https://eprint.iacr.org/2026/241.pdf) | NR [wall_time]<br>已检查 §6.1; §7；未给该阶段独立可引用界或数值。<br>[§6.1; §7](https://eprint.iacr.org/2026/241.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: LeNet convolution block 2572 parameters; precision: NR; hardware: most experiments RTX5080 16GB; target: convolution block | 2^27.29 [oracle_calls]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | 2^17.21 seconds [wall_time]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | max parameter error 2^-27.31<br>Full LeNet行不能称全部参数恢复。 |
| dimensions: Reduced LeNet 400-20-10;10772 parameters; precision: NR; hardware: most experiments RTX5080 16GB; target: complete reduced network | 2^27.65 [oracle_calls]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | 2^17.38 seconds [wall_time]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | max parameter error 2^-27.14<br>Full LeNet行不能称全部参数恢复。 |
| dimensions: Full LeNet 61706 parameters; precision: NR; hardware: most experiments RTX5080 16GB; target: complete conv block + FC1 93.33% weights | 2^27.31 [oracle_calls]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | 2^18.46 seconds [wall_time]<br>[§6 Table2; Supplement C.1 Table3](https://eprint.iacr.org/2026/241.pdf) | None<br>Full LeNet行不能称全部参数恢复。 |

### eprint-2026-464: [Model Extraction of Convolutional Neural Networks with Max-Pooling](https://eprint.iacr.org/2026/464)

Oracle / 预言机: raw-output / soft-label finite differences.

Scope / 范围: max-pool CNN逐层权重与sign

Assumptions / 假设: 前层正确已知；ERF/CRF定位排不安全CP；CP与存储字节不是Q。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A/B/C 感受野定位与核恢复<br>notes: 完整Q/T Big-O NR。 | NR [oracle_calls]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [arithmetic_operations]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [oracle_calls]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [wall_time]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) |
| D/E sign与bias<br>notes: Conv2沿用Wiggle；bias需ReLU CP。 | NR [oracle_calls]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [arithmetic_operations]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [oracle_calls]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) | NR [wall_time]<br>已检查 §3–5；未给该阶段独立可引用界或数值。<br>[§3–5](https://eprint.iacr.org/2026/464.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: CIFAR small VGG 4 conv layers channels4/8/8/16; precision: float64 stored query results; hardware: Intel i7-14700F; target: 逐层；前缀已知 | NR [oracle_calls]<br>已检查 §6 Table4；未单列该项实验指标。<br>[§6 Table4](https://eprint.iacr.org/2026/464.pdf) | NR [wall_time]<br>已检查 §6 Table4；未单列该项实验指标。<br>[§6 Table4](https://eprint.iacr.org/2026/464.pdf) | Conv1 4/4;Conv2 7/8;Conv3 99.49% weights;Conv4 98.52%<br>Conv1 44CP；Conv3/4 10,000CP；Conv4 sign11/12 discovered；4/16 always-off，非全网100%。 |
| dimensions: localized CP systems; precision: NR; hardware: NR; target: 同求解器局部线性系统 | NR [oracle_calls]<br>已检查 §6 Table6；未单列该项实验指标。<br>[§6 Table6](https://eprint.iacr.org/2026/464.pdf) | NR [wall_time]<br>已检查 §6 Table6；未单列该项实验指标。<br>[§6 Table6](https://eprint.iacr.org/2026/464.pdf) | memory reduction75.40%–93.80%;runtime reduction73.73%–93.36%<br>不是总攻击Q/T同百分比降幅。 |

### eprint-2026-902: [End-to-End Polynomial-Time Cryptanalytic Extraction of Convolutional Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/902)

Oracle / 预言机: top-1 hard label.

Scope / 范围: 已知架构平均池化受控ReLU CNN端到端

Assumptions / 假设: m_max含channel×空间预算；非发现保证；sign正确候选保留且B_i受控才有poly。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| A dual acquisition<br>notes: 原文T_dual实为query count。 | O(L m_max κ log(1/ε)) [oracle_calls]<br>[§IV Eq36](https://eprint.iacr.org/2026/902.pdf) | NR [arithmetic_operations]<br>已检查 §IV Eq36；未给该阶段独立可引用界或数值。<br>[§IV Eq36](https://eprint.iacr.org/2026/902.pdf) | NR [oracle_calls]<br>已检查 §IV Eq36；未给该阶段独立可引用界或数值。<br>[§IV Eq36](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §IV Eq36；未给该阶段独立可引用界或数值。<br>[§IV Eq36](https://eprint.iacr.org/2026/902.pdf) |
| C SVD signatures<br>notes: p=C_in k²；总简式需m≈p与良好条件。 | NR [oracle_calls]<br>已检查 §IV Eqs37–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs37–40](https://eprint.iacr.org/2026/902.pdf) | O(min(m,p)²max(m,p)); conditional total O(L_conv C_max p³) [arithmetic_operations]<br>[§IV Eqs37–40](https://eprint.iacr.org/2026/902.pdf) | NR [oracle_calls]<br>已检查 §IV Eqs37–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs37–40](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §IV Eqs37–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs37–40](https://eprint.iacr.org/2026/902.pdf) |
| D voting/candidate verification<br>notes: O(Σ C_out^(i)n_patches^(i)m_vote+Σ B_i V_i)为混合预算，不填纯Q/FLOPs；未筛选2^&#124;C_low&#124;。 | NR [oracle_calls]<br>已检查 §IV Eq38；未给该阶段独立可引用界或数值。<br>[§IV Eq38](https://eprint.iacr.org/2026/902.pdf) | NR [arithmetic_operations]<br>已检查 §IV Eq38；未给该阶段独立可引用界或数值。<br>[§IV Eq38](https://eprint.iacr.org/2026/902.pdf) | NR [oracle_calls]<br>已检查 §IV Eq38；未给该阶段独立可引用界或数值。<br>[§IV Eq38](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §IV Eq38；未给该阶段独立可引用界或数值。<br>[§IV Eq38](https://eprint.iacr.org/2026/902.pdf) |
| E FC least squares | NR [oracle_calls]<br>已检查 §IV Eqs39–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs39–40](https://eprint.iacr.org/2026/902.pdf) | O(N_FC d²) per output; O(Kd³) if N_FC≈d [arithmetic_operations]<br>[§IV Eqs39–40](https://eprint.iacr.org/2026/902.pdf) | NR [oracle_calls]<br>已检查 §IV Eqs39–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs39–40](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §IV Eqs39–40；未给该阶段独立可引用界或数值。<br>[§IV Eqs39–40](https://eprint.iacr.org/2026/902.pdf) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: 1D MNIST Conv(8-8-4)-FC10; precision: NR; hardware: RTX4090; target: 已知架构平均池化受控ReLU CNN端到端 | 2,371,020 [oracle_calls]<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §V TablesIII–VIII；未单列该项实验指标。<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | 21/21 signs;100% test prediction fidelity<br>Dual2,363,020; sign8,000; candidate combinations8/2/4；非全域等价。 |
| dimensions: 2D variants; precision: NR; hardware: RTX4090; target: 已知架构平均池化受控ReLU CNN端到端 | .39M/.76M/1.54M [oracle_calls]<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §V TablesIII–VIII；未单列该项实验指标。<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | 100% test prediction fidelity<br> |
| dimensions: RGB LeNet(6-16-120); precision: NR; hardware: RTX4090; target: 已知架构平均池化受控ReLU CNN端到端 | Derived / 推导: ≈4.03M [oracle_calls]<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | NR [wall_time]<br>已检查 §V TablesIII–VIII；未单列该项实验指标。<br>[§V TablesIII–VIII](https://eprint.iacr.org/2026/902.pdf) | 100% test prediction fidelity<br>作者按实测单位率×8,662可恢复单元缩放估算，非完整计数。 |

### arxiv-2609.27427: [Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting](https://arxiv.org/abs/2609.27427)

Oracle / 预言机: raw-output or hard-label upstream.

Scope / 范围: CNN architecture from recovered sparse vectors

Assumptions / 假设: 继承上游满秩、可观察点和签名；不解决任意hard-label稀有事件。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| F geometry architecture<br>notes: 非整网O(1)；没有所有稀有点分布统一常数证明。 | constant relative to (k^(L))² kernel parameters; shared subset of upstream queries [oracle_calls]<br>[§4; §9](https://arxiv.org/pdf/2609.27427v1v1) | NR [arithmetic_operations]<br>已检查 §4; §9；未给该阶段独立可引用界或数值。<br>[§4; §9](https://arxiv.org/pdf/2609.27427v1v1) | NR [oracle_calls]<br>已检查 §4; §9；未给该阶段独立可引用界或数值。<br>[§4; §9](https://arxiv.org/pdf/2609.27427v1v1) | NR [wall_time]<br>已检查 §4; §9；未给该阶段独立可引用界或数值。<br>[§4; §9](https://arxiv.org/pdf/2609.27427v1v1) |

| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |
|---|---|---|---|
| dimensions: two-conv (2+1), raw-output; precision: NR; hardware: dual Xeon Gold5318Y@2.10GHz;503GB; target: total parameter recovery | 2^20.48 [oracle_calls]<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | 27.31 seconds [wall_time]<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | None<br> |
| dimensions: same two-conv (2+1), raw-output; precision: NR; hardware: dual Xeon Gold5318Y@2.10GHz;503GB; target: architecture subset | 2^17.71 [oracle_calls]<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | 24.08 seconds [wall_time]<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | None<br>与total不可相加重复计费。 |
| dimensions: three conv NoPool/AvgPool/MaxPool kernels3/5/3 strides1/1/2; precision: NR; hardware: NR; target: layerwise raw-output geometry | NR [oracle_calls]<br>已检查 §9；未单列该项实验指标。<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | NR [wall_time]<br>已检查 §9；未单列该项实验指标。<br>[§9](https://arxiv.org/pdf/2609.27427v1v1) | None<br>每层700CP；非全黑盒hard-label端到端。 |

## 激活函数扩展 (4)

### eprint-2025-1970: [Delving into Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2025/1970)

Oracle / 预言机: oracle/范围：raw outputs或top-m probabilities；PReLU前馈网络，按层恢复权重、bias、符号和slope，不是label-only。.

Scope / 范围: oracle/范围：raw outputs或top-m probabilities；PReLU前馈网络，按层恢复权重、bias、符号和slope，不是label-only。

Assumptions / 假设: oracle/范围：raw outputs或top-m probabilities；PReLU前馈网络，按层恢复权重、bias、符号和slope，不是label-only。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| 临界点收集与定位<br>notes: 均匀coupon collector: O(d_i log₂ d_i)临界点；每点ε次定位query，ε为作者视作小常数的精度成本；点数不是oracle Q。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) |
| 每点差分权重恢复<br>notes: 差分后解线性系统；显式算术未展开。 | 4d_(i−1)−1 per critical point [oracle_calls]<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) |
| 已有权重后的符号与slope<br>notes: 仅在已有权重条件下。 | 0 additional queries [oracle_calls]<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) |
| 层级汇总<br>notes: 全网逐层求和；精度常数不能当bit complexity消去；top-m变体仅poly声称，m依赖未给。 | O(d_i(4d_(i−1)−1)log₂ d_i) [oracle_calls]<br>[Appendix D.1–D.2, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1–D.2, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1–D.2, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix D.1–D.2, pp.30–31](https://eprint.iacr.org/2025/1970.pdf) |
| workflow2 128–64–1<br>notes: 8,385参数；输出误差(ε,0)=2^-29.55，max参数误差2^-33.79；表未报告墙钟。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | 2^19.34 [oracle_calls]<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) |
| workflow2 64–32–32–1<br>notes: 3,233参数；输出误差2^-23.14，参数误差2^-27.44。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | 2^18.64 [oracle_calls]<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) |
| workflow1 64–32–32–1<br>notes: 输出误差2^-5.20；不同workflow不可混拼。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | 2^21.35 [oracle_calls]<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§8, Table 2, p.24](https://eprint.iacr.org/2025/1970.pdf) |

### eprint-2026-178: [Cryptanalytic Extraction of Neural Networks with Various Activation Functions](https://eprint.iacr.org/2026/178)

Oracle / 预言机: oracle/分支：S5 raw-output；S1 hard-label（paper taxonomy）。LeakyReLU、HardTanh、PReLU、ELU、Step必须逐分支展示，不能合为“各种激活均端到端poly”。.

Scope / 范围: oracle/分支：S5 raw-output；S1 hard-label（paper taxonomy）。LeakyReLU、HardTanh、PReLU、ELU、Step必须逐分支展示，不能合为“各种激活均端到端poly”。

Assumptions / 假设: oracle/分支：S5 raw-output；S1 hard-label（paper taxonomy）。LeakyReLU、HardTanh、PReLU、ELU、Step必须逐分支展示，不能合为“各种激活均端到端poly”。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| LeakyReLU signature/sign<br>notes: signature poly；raw sign仅contractive保证poly，否则指数；hard-label对应方法poly。Table1是time分类，未给显式query或算术式。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6](https://eprint.iacr.org/2026/178.pdf) |
| HardTanh sign与部分signature<br>notes: 奇对称无需sign；signature未全恢复。784–128²–10首层122/128、第二层86/128；不能将118,282总参数称完整恢复。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; Tables 2–3, pp.28–29](https://eprint.iacr.org/2026/178.pdf) | O(1) sign stage [arithmetic_operations]<br>[Table 1, p.5; Tables 2–3, pp.28–29](https://eprint.iacr.org/2026/178.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; Tables 2–3, pp.28–29](https://eprint.iacr.org/2026/178.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; Tables 2–3, pp.28–29](https://eprint.iacr.org/2026/178.pdf) |
| PReLU hard-label<br>notes: 仅contractive及slope限制；784–64^4–10的63,626参数实验max误差2^-7.48。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6; Table 2, p.28](https://eprint.iacr.org/2026/178.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6; Table 2, p.28](https://eprint.iacr.org/2026/178.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6; Table 2, p.28](https://eprint.iacr.org/2026/178.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §3–6; Table 2, p.28](https://eprint.iacr.org/2026/178.pdf) |
| Step signature/sign<br>notes: signature poly；sign/exhaustive search指数，未给显式阶或Q。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§6, p.22; Table 1, p.5](https://eprint.iacr.org/2026/178.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§6, p.22; Table 1, p.5](https://eprint.iacr.org/2026/178.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§6, p.22; Table 1, p.5](https://eprint.iacr.org/2026/178.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§6, p.22; Table 1, p.5](https://eprint.iacr.org/2026/178.pdf) |
| ELU raw-output<br>notes: 只小宽/小深raw实验，无hard-label成功；784–2²–1误差2^-6.72。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.28; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.28; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.28; §3–6](https://eprint.iacr.org/2026/178.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.28; §3–6](https://eprint.iacr.org/2026/178.pdf) |

### eprint-2026-253: [Cryptanalytic Extraction of Deep Neural Networks with Non-Linear Activations](https://eprint.iacr.org/2026/253)

Oracle / 预言机: oracle/假设：raw logits；σ两端指数趋近线性或常数，非线性带足够窄，能找到主要由一个神经元非线性支配的输入。不是任意smooth函数的无条件定理。.

Scope / 范围: oracle/假设：raw logits；σ两端指数趋近线性或常数，非线性带足够窄，能找到主要由一个神经元非线性支配的输入。不是任意smooth函数的无条件定理。

Assumptions / 假设: oracle/假设：raw logits；σ两端指数趋近线性或常数，非线性带足够窄，能找到主要由一个神经元非线性支配的输入。不是任意smooth函数的无条件定理。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| 二阶导signature与sieve<br>notes: O(n log n)是均匀且每sample常数成功率简化模型的采样点数，不是完整Q；每sample处理poly；有限差分调用数及完整算术式NR。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.1, pp.6–9, Efficiency](https://eprint.iacr.org/2026/253.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.1, pp.6–9, Efficiency](https://eprint.iacr.org/2026/253.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.1, pp.6–9, Efficiency](https://eprint.iacr.org/2026/253.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.1, pp.6–9, Efficiency](https://eprint.iacr.org/2026/253.pdf) |
| 伪法向降噪与ALZ<br>notes: 非线性带足够窄且单神经元主导，后续layer distinguisher/scale/sign/bias/activation依赖这些观测。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.2, p.9; §3.3, pp.10 onward](https://eprint.iacr.org/2026/253.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.2, p.9; §3.3, pp.10 onward](https://eprint.iacr.org/2026/253.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.2, p.9; §3.3, pp.10 onward](https://eprint.iacr.org/2026/253.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3.2, p.9; §3.3, pp.10 onward](https://eprint.iacr.org/2026/253.pdf) |
| 16×16^8×10首层<br>notes: data=2^20.14是论文data计数，不替换oracle Q；16/16神经元、272/272首层参数。sieve/ALZ/check墙钟比例7.7%/88.1%/1.5%。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.23](https://eprint.iacr.org/2026/253.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.23](https://eprint.iacr.org/2026/253.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.23](https://eprint.iacr.org/2026/253.pdf) | 42 [seconds]<br>[Table 2, p.23](https://eprint.iacr.org/2026/253.pdf) |
| 一小时首层预算<br>notes: 784×128×1 70/128，54,950/100,480参数；MNIST784×16^8×1首层15/16；CIFAR3072×8^8×1首层8/8；不同后端只有Cython sieve/ALZ可公平比较。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.24](https://eprint.iacr.org/2026/253.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.24](https://eprint.iacr.org/2026/253.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.24](https://eprint.iacr.org/2026/253.pdf) | 3600 (budget) [seconds]<br>[Table 3, p.24](https://eprint.iacr.org/2026/253.pdf) |
| 16×16^8×10第四层<br>notes: 13/16检测，152/256部分参数，0/256 fully denoised，不是全网成功。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 6, p.26](https://eprint.iacr.org/2026/253.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 6, p.26](https://eprint.iacr.org/2026/253.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 6, p.26](https://eprint.iacr.org/2026/253.pdf) | 7200 (budget) [seconds]<br>[Table 6, p.26](https://eprint.iacr.org/2026/253.pdf) |

### eprint-2026-1066: [Breaking Slope and Structure Restrictions: Broadening Hard-Label Cryptanalytic Extraction of PReLU Neural Networks](https://eprint.iacr.org/2026/1066)

Oracle / 预言机: oracle/范围：top-1 label，联合signature+slope，residual analysis、progressive parameter decoupling放宽旧PReLU限制。实验重点是目标层，不等于完整网络所有参数端到端实证。.

Scope / 范围: oracle/范围：top-1 label，联合signature+slope，residual analysis、progressive parameter decoupling放宽旧PReLU限制。实验重点是目标层，不等于完整网络所有参数端到端实证。

Assumptions / 假设: oracle/范围：top-1 label，联合signature+slope，residual analysis、progressive parameter decoupling放宽旧PReLU限制。实验重点是目标层，不等于完整网络所有参数端到端实证。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| Stage1 dual收集与空间构建<br>notes: 196–20–25–30–10第3层；约20,000 dual大量来自前层；persistent状态可使发现退化指数；所有单模型单层≤2^26 queries、≤2^11秒是作者实验约束。 | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | 2^24.93 [oracle_calls]<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | 2^9.645 [seconds]<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) |
| Stage2 非线性方程组<br>notes: 最多T个系统，poly求解仅作者声称，不升级一般非线性系统保证；同196–20–25–30–10目标第3层。 | 0 additional queries [oracle_calls]<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | 0 [oracle_calls]<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) | 2^5.75 (average) [seconds]<br>[Algorithm 1, p.22; §6.4, p.23; §7.1, p.25](https://eprint.iacr.org/2026/1066.pdf) |
| Stage3 progressive decoupling<br>notes: 复用Stage1 dual；20–22–24–26–10目标层24/24、26/26；MNIST784–20–22–24–10目标层22/22、24/24；signature阈值2^-10，不是输出fidelity。 | 0 additional queries [oracle_calls]<br>[§7.2, p.26; Table 2](https://eprint.iacr.org/2026/1066.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§7.2, p.26; Table 2](https://eprint.iacr.org/2026/1066.pdf) | NR [oracle_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§7.2, p.26; Table 2](https://eprint.iacr.org/2026/1066.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§7.2, p.26; Table 2](https://eprint.iacr.org/2026/1066.pdf) |

## RNN 与 GNN (2)

### eprint-2026-168: [Cryptanalytic Extraction of Recurrent Neural Network Models](https://eprint.iacr.org/2026/168)

Oracle / 预言机: oracle/范围：raw outputs或hard labels；ReLU recurrent，隐藏态不可见，可控制整段连续输入；构造等价FCN，复用时间权重，τ是时间步、n是recurrent layers，二者必须分列。.

Scope / 范围: oracle/范围：raw outputs或hard labels；ReLU recurrent，隐藏态不可见，可控制整段连续输入；构造等价FCN，复用时间权重，τ是时间步、n是recurrent layers，二者必须分列。

Assumptions / 假设: oracle/范围：raw outputs或hard labels；ReLU recurrent，隐藏态不可见，可控制整段连续输入；构造等价FCN，复用时间权重，τ是时间步、n是recurrent layers，二者必须分列。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| 等价FCN输入权重与FBD<br>notes: 隐藏态不可见，控制完整连续输入序列；条件性功能等价；τ时间步不等于recurrent层数n。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, Theorem 1, p.11; §4, Theorem 2, p.18](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, Theorem 1, p.11; §4, Theorem 2, p.18](https://eprint.iacr.org/2026/168.pdf) | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, Theorem 1, p.11; §4, Theorem 2, p.18](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, Theorem 1, p.11; §4, Theorem 2, p.18](https://eprint.iacr.org/2026/168.pdf) |
| RPA离线排列与缩放<br>notes: 不含Φ/B构建；Hungarian O(d1³)，应用变换O(d1²)。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3 Complexity, p.15](https://eprint.iacr.org/2026/168.pdf) | O(K d1²+d1³) [arithmetic_operations]<br>[§3 Complexity, p.15](https://eprint.iacr.org/2026/168.pdf) | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3 Complexity, p.15](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3 Complexity, p.15](https://eprint.iacr.org/2026/168.pdf) |
| RPR hard-label离线<br>notes: n_a=d_l；d_(l−1)=O(d_l)、中位过滤有界；不含dual acquisition/Jacobian。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.31–32](https://eprint.iacr.org/2026/168.pdf) | O(N d0 d_l² + N d_l³ + n_a N d_l² + Σ_j[N_j² d_l +(1+q_j)(d_l³+N d_l²)+N log N]) [arithmetic_operations]<br>[Appendix A.3, pp.31–32](https://eprint.iacr.org/2026/168.pdf) | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.31–32](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.31–32](https://eprint.iacr.org/2026/168.pdf) |
| RPR raw离线<br>notes: 不含记录采集、feature/Jacobian和gradient jumps；固定维N线性仅R也固定。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.32–33](https://eprint.iacr.org/2026/168.pdf) | O(d_l² [N d_l(d0+d_l)+(T_iter+1)(N d0+d_l²)+R(N+d0+d_l)]) [arithmetic_operations]<br>[Appendix A.3, pp.32–33](https://eprint.iacr.org/2026/168.pdf) | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.32–33](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix A.3, pp.32–33](https://eprint.iacr.org/2026/168.pdf) |
| 200–32–1 raw τ20<br>notes: abs2^-23.31，75分位relative2^-26.65；10^5完整Gaussian sequences，不是全域认证。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | 2^22.07 [full_sequence_queries]<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) |
| 200–32–1 raw τ1024<br>notes: abs2^-23.30，relative2^-26.83；10^5完整Gaussian sequences，不是全域认证。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | 2^21.58 [full_sequence_queries]<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) |
| 200–32–1 hard τ20<br>notes: abs2^-18.46，relative2^-21.03；10^5完整Gaussian sequences，不是全域认证。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | 2^26.48 [full_sequence_queries]<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) |
| 200–32³–1 raw<br>notes: abs2^-12.19；10^5完整Gaussian sequences，不是全域认证。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | 2^22.78 [full_sequence_queries]<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) |
| 200–32³–1 hard<br>notes: abs2^-11.11；10^5完整Gaussian sequences，不是全域认证。 | NR [full_sequence_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | 2^32.51 [full_sequence_queries]<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5](https://eprint.iacr.org/2026/168.pdf) |

### eprint-2026-719: [Polynomial-Time Cryptanalytic Extraction of Graph Neural Networks in the Hard-Label Setting](https://eprint.iacr.org/2026/719)

Oracle / 预言机: oracle/范围：message-passing ReLU GNN固定局部查询模型；local operator在查询间不变、可选连续局部features，硬标签node responses。不是任意图API，只允许自然图输入时定理不自动成立。.

Scope / 范围: oracle/范围：message-passing ReLU GNN固定局部查询模型；local operator在查询间不变、可选连续局部features，硬标签node responses。不是任意图API，只允许自然图输入时定理不自动成立。

Assumptions / 假设: oracle/范围：message-passing ReLU GNN固定局部查询模型；local operator在查询间不变、可选连续局部features，硬标签node responses。不是任意图API，只允许自然图输入时定理不自动成立。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| accepted-dual发现及全流程条件性Q<br>notes: 未展开单项式；κ_dual为accepted-dual发现成本；固定local operator、连续features、single-differential/local isolation/non-degeneracy。 | poly(L,d,K,C,κ_dual) [node_queries]<br>[Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | NR [node_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) |
| signature/sign与scale-chain后处理<br>notes: N=Σ_(l=0)^(L−1)d_l recovered neurons；K accepted coverage/neuron；K_sign probes/neuron；postprocessing不含发现阶段。 | NR [node_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, p.12; Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | O(N K d²+N K_sign) [arithmetic_operations]<br>[Theorem 4.1, p.12; Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | NR [node_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, p.12; Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, p.12; Proposition 4.4, Eq.32, p.13](https://eprint.iacr.org/2026/719.pdf) |
| dedicated32–32^4–4 checkpoint<br>notes: RTX4090；train/test/random fidelity100%；random为10,000 standard-normal two-node queries；不可绑定最大10,660参数模型。 | NR [node_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.16](https://eprint.iacr.org/2026/719.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.16](https://eprint.iacr.org/2026/719.pdf) | 48.68 million [node_queries]<br>[Table 4, p.16](https://eprint.iacr.org/2026/719.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.16](https://eprint.iacr.org/2026/719.pdf) |

## 注意力与 GLU 模块 (4)

### arxiv-2601.16873: [Provably Learning Attention with Queries](https://arxiv.org/abs/2601.16873)

Oracle / 预言机: oracle：chosen arbitrary real token vectors、scalar value query，canonical merged W∈R^(d×d), v∈R^d，v≠0。不是分别恢复Q/K/V原始因子。.

Scope / 范围: oracle：chosen arbitrary real token vectors、scalar value query，canonical merged W∈R^(d×d), v∈R^d，v≠0。不是分别恢复Q/K/V原始因子。

Assumptions / 假设: oracle：chosen arbitrary real token vectors、scalar value query，canonical merged W∈R^(d×d), v∈R^d，v≠0。不是分别恢复Q/K/V原始因子。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| length1恢复v<br>notes: canonical merged v≠0；chosen real token vectors。 | d [scalar_attention_queries]<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) |
| length2恢复W及总量<br>notes: canonical W，不是原Q/K/V因子；线性求解poly但显式算术阶NR。 | d² for W; d+d² total [scalar_attention_queries]<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 4.1, §4, pp.3–4](https://arxiv.org/pdf/2601.16873) |
| 低秩W<br>notes: rank(W)≤r；Gaussian rank-one measurements、核范数凸规划；成功≥1−exp(−Ω(m))。 | d+m, m=O(rd) [scalar_attention_queries]<br>[Theorem 5.1, §5, pp.5–6](https://arxiv.org/pdf/2601.16873) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.1, §5, pp.5–6](https://arxiv.org/pdf/2601.16873) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.1, §5, pp.5–6](https://arxiv.org/pdf/2601.16873) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.1, §5, pp.5–6](https://arxiv.org/pdf/2601.16873) |
| 近似oracle<br>notes: 已知∥W∥F≤W≥2，∥v∥≤1，非零坐标≥μ；τ=O(min{μ,ε_v/√d,μ ε_W/(W²d)})可要求oracle容差，现实float64未必满足。 | O(d²) [scalar_attention_queries]<br>[Theorem 6.1, p.6](https://arxiv.org/pdf/2601.16873) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 6.1, p.6](https://arxiv.org/pdf/2601.16873) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 6.1, p.6](https://arxiv.org/pdf/2601.16873) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 6.1, p.6](https://arxiv.org/pdf/2601.16873) |
| bias-free单层Transformer<br>notes: 奇部每attention query用两Transformer calls；v=A w_o≠0、FFN可学习；MHA仅known orthogonal subspaces特殊情形；无独立实验节。 | Q_FFN(d,m)+O(d²) [transformer_queries]<br>[§4.1, pp.4–5; §7](https://arxiv.org/pdf/2601.16873) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.1, pp.4–5; §7](https://arxiv.org/pdf/2601.16873) | NR [transformer_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.1, pp.4–5; §7](https://arxiv.org/pdf/2601.16873) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.1, pp.4–5; §7](https://arxiv.org/pdf/2601.16873) |

### arxiv-2608.03294: [Provably Learning Multi-Head Attention with Queries](https://arxiv.org/abs/2608.03294)

Oracle / 预言机: oracle/假设：chosen real-valued scalar value query；H canonical heads，W_h两两不同、v_h非零，精确实数算术、log与多项式factorization可用。只恢复canonical pairs up to permutation。.

Scope / 范围: oracle/假设：chosen real-valued scalar value query；H canonical heads，W_h两两不同、v_h非零，精确实数算术、log与多项式factorization可用。只恢复canonical pairs up to permutation。

Assumptions / 假设: oracle/假设：chosen real-valued scalar value query；H canonical heads，W_h两两不同、v_h非零，精确实数算术、log与多项式factorization可用。只恢复canonical pairs up to permutation。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| exact canonical MHA<br>notes: max length2H+1；distinct W_h、nonzero v_h、exact real arithmetic；H上界时替H0；低秩O(Hrd)须额外假设；不是bit complexity。 | 4Hd²−2H+1 [scalar_attention_queries]<br>[Theorem 5.1, p.5; Offline, p.6](https://arxiv.org/pdf/2608.03294) | 2d²−1 degree-H polynomial factorizations + O(d²H³+d³H) operations + O(d²H) exact logs/comparisons; numerical companion eigensolver gives O(d²H³+d³H) [arithmetic_operations]<br>[Theorem 5.1, p.5; Offline, p.6](https://arxiv.org/pdf/2608.03294) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.1, p.5; Offline, p.6](https://arxiv.org/pdf/2608.03294) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.1, p.5; Offline, p.6](https://arxiv.org/pdf/2608.03294) |
| approximate oracle<br>notes: error≤C_stab τ，仅τ<τ0，模型/探针条件常数，无uniform conditioning；offline仍exact。 | 4Hd²−2H+2d−1 [scalar_attention_queries]<br>[Theorem 5.2, p.6](https://arxiv.org/pdf/2608.03294) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.2, p.6](https://arxiv.org/pdf/2608.03294) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.2, p.6](https://arxiv.org/pdf/2608.03294) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.2, p.6](https://arxiv.org/pdf/2608.03294) |
| 单层ReLU Transformer奇部<br>notes: ReLU重建另需搜索及符号消歧；非退化及Z单射下几乎必然有限queries终止、全域等价；无完整Transformer统一poly Q/T。 | 2(4Hd²−2H+1) for odd attention only [transformer_queries]<br>[Theorem 5.3, pp.6–7](https://arxiv.org/pdf/2608.03294) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.3, pp.6–7](https://arxiv.org/pdf/2608.03294) | NR [transformer_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.3, pp.6–7](https://arxiv.org/pdf/2608.03294) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Theorem 5.3, pp.6–7](https://arxiv.org/pdf/2608.03294) |
| 180位(d,H)=(128,8)<br>notes: 132,096 merged参数；100模型全成功，max E_param9.97e−110；八种尺寸800模型<1e−100。 | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.3, Table 3, p.37](https://arxiv.org/pdf/2608.03294) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.3, Table 3, p.37](https://arxiv.org/pdf/2608.03294) | 524,273 [scalar_attention_queries]<br>[Appendix G.3, Table 3, p.37](https://arxiv.org/pdf/2608.03294) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.3, Table 3, p.37](https://arxiv.org/pdf/2608.03294) |
| binary64 oracle/180位offline<br>notes: 原算法(3,2)/(3,4)/(3,8)/(8,4)成功99/100,1/100,0/100,0/100；direct-one-token额外2d−2 calls为100/100,31/100,0/100,0/100；成功all H且E_param<1e−2。 | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.4, Tables 5–6, p.39](https://arxiv.org/pdf/2608.03294) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.4, Tables 5–6, p.39](https://arxiv.org/pdf/2608.03294) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.4, Tables 5–6, p.39](https://arxiv.org/pdf/2608.03294) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix G.4, Tables 5–6, p.39](https://arxiv.org/pdf/2608.03294) |

### eprint-2026-1678: [Cryptanalytic Extraction of Multi-Head Softmax Attention Models](https://eprint.iacr.org/2026/1678)

Oracle / 预言机: scalar continuous value oracle，canonical G有效heads、H已知上界，合并同W的heads、删零贡献。Theorem1 canonical identifiability §4；不恢复有gauge ambiguity的原Q/K/V因子。.

Scope / 范围: scalar continuous value oracle，canonical G有效heads、H已知上界，合并同W的heads、删零贡献。Theorem1 canonical identifiability §4；不恢复有gauge ambiguity的原Q/K/V因子。

Assumptions / 假设: scalar continuous value oracle，canonical G有效heads、H已知上界，合并同W的heads、删零贡献。Theorem1 canonical identifiability §4；不恢复有gauge ambiguity的原Q/K/V因子。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| canonical MHA length-one及atom sets<br>notes: d恢复Σv；1 anchor、d扰动、d² W sets各2H；max length2H+1；G有效heads、H上界；scalar参数计数下界；不恢复Q/K/V gauge因子。 | d+2H(1+d+d²) [scalar_attention_queries]<br>[§4.6, pp.19–20](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, pp.19–20](https://eprint.iacr.org/2026/1678.pdf) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, pp.19–20](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, pp.19–20](https://eprint.iacr.org/2026/1678.pdf) |
| coincident v matching替代<br>notes: O(Hd²)；rational interpolation/roots/linear solves统一算术式NR。 | 2H(1+2d+d²) [scalar_attention_queries]<br>[§4.6, p.20](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, p.20](https://eprint.iacr.org/2026/1678.pdf) | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, p.20](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4.6, p.20](https://eprint.iacr.org/2026/1678.pdf) |
| biased单头Transformer<br>notes: FFN primitive成功、g(q+u)−g(q)≠0、local affine及independent anchors；非深Transformer。 | Q_FFN+d²; Q_FFN+n_anc d when n_anc≥d [transformer_queries]<br>[§5.5, pp.24–26](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.5, pp.24–26](https://eprint.iacr.org/2026/1678.pdf) | NR [transformer_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.5, pp.24–26](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.5, pp.24–26](https://eprint.iacr.org/2026/1678.pdf) |
| float64 d8,G=H6 no-refine<br>notes: 参数误差2^-5.95、功能2^-4.09；包含拒绝、过采样、校验、Gauss–Newton；不是exact公式预算。 | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | 43,284 [scalar_attention_queries]<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) |
| float64 d8,G=H6 refine<br>notes: 参数2^-51.54、功能2^-50；包含拒绝、过采样、校验、Gauss–Newton；不是exact公式预算。 | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | 45,012 [scalar_attention_queries]<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) |
| float64 d8,G5,H10 refine<br>notes: 参数2^-49.19、功能2^-47；包含拒绝、过采样、校验、Gauss–Newton；不是exact公式预算。 | NR [scalar_attention_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | 123,544 [scalar_attention_queries]<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 2, p.26](https://eprint.iacr.org/2026/1678.pdf) |
| biased block d16,m32<br>notes: n_anc32功能2^-25.89、参数2^-29.71；每数值绑定对应anchors，墙钟NR。 | NR [transformer_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.28](https://eprint.iacr.org/2026/1678.pdf) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.28](https://eprint.iacr.org/2026/1678.pdf) | Q_FFN=42,542; n_anc=16/32/64 total=42,798/43,054/43,566 [transformer_queries]<br>[Table 3, p.28](https://eprint.iacr.org/2026/1678.pdf) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.28](https://eprint.iacr.org/2026/1678.pdf) |

### arxiv-2608.06631: [Cryptanalytic Extraction of Isolated Bias-Free GLU Feed-Forward Blocks by Antipodal Separation](https://arxiv.org/abs/2608.06631)

Oracle / 预言机: 直接full-vector isolated bias-free GLU f:R^n→R^n_out；已知结构，SwiGLU/GeGLU；不展示从final token API产生block input/output的方法。.

Scope / 范围: 直接full-vector isolated bias-free GLU f:R^n→R^n_out；已知结构，SwiGLU/GeGLU；不展示从final token API产生block input/output的方法。

Assumptions / 假设: 直接full-vector isolated bias-free GLU f:R^n→R^n_out；已知结构，SwiGLU/GeGLU；不展示从final token API产生block input/output的方法。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| Stage0 coordinate Hessian<br>notes: isolated bias-free SwiGLU/GeGLU直接full-vector oracle；无token API到block oracle构造。 | 4d n1² [block_vector_queries]<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | 9,437,184 (n1=192,d=64) [block_vector_queries]<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) |
| Stage1A/B及candidate selector<br>notes: 不再翻倍paired calls。 | NR [block_vector_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | 440,000 paired calls + 4,096 selector; attack total=9,881,280 [block_vector_queries]<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) |
| Stage2 refinement/residual及factor polish<br>notes: factor-polish selector另4,096；final disjoint evaluation4,096不计攻击；无优化收敛或统一算术界。 | 0 additional calls for observation-reusing refinement/repairs/factor polish [block_vector_queries]<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | NR [block_vector_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§3, pp.3–6; §5, p.7](https://arxiv.org/pdf/2608.06631) |
| full-input extension<br>notes: M8,K64，Qwen192→384→576→768→960→1024；直接n1024 Hessian268,435,456；额外polish training/guard477k–986k分列。 | 4MK n_i per endpoint step [block_vector_queries]<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | 7,602,176 additional; 17,483,456 pre-polish total [block_vector_queries]<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5, p.7](https://arxiv.org/pdf/2608.06631) |
| 有限精度block评估<br>notes: Qwen192输入128输出/扩至1024仍128输出；Gemma1152全block非整模型；BF16 median4.6269%、p90 7.7392%，仅2.19% storage exact；27h–33天是假定10–100ms说明性估计，非实测墙钟。 | NR [block_vector_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Tables 4–5, p.8; §6.3, p.8; §6.6–7, pp.9–10](https://arxiv.org/pdf/2608.06631) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Tables 4–5, p.8; §6.3, p.8; §6.6–7, pp.9–10](https://arxiv.org/pdf/2608.06631) | NR [block_vector_queries]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Tables 4–5, p.8; §6.3, p.8; §6.6–7, pp.9–10](https://arxiv.org/pdf/2608.06631) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Tables 4–5, p.8; §6.3, p.8; §6.6–7, pp.9–10](https://arxiv.org/pdf/2608.06631) |

## LLM 部分结构与输出空间提取 (2)

### arxiv-2403.06634: [Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634)

Oracle / 预言机: oracle：实际token API的top-k logprobs+logit_bias，另有无logprob的bias版本。目标hidden dimension和最后output projection up to invertible transform；不恢复全模型参数。.

Scope / 范围: oracle：实际token API的top-k logprobs+logit_bias，另有无logprob的bias版本。目标hidden dimension和最后output projection up to invertible transform；不恢复全模型参数。

Assumptions / 假设: oracle：实际token API的top-k logprobs+logit_bias，另有无logprob的bias版本。目标hidden dimension和最后output projection up to invertible transform；不恢复全模型参数。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| logit matrix/rank/SVD<br>notes: n prompts span h；W等价基，非全模型；full-vector logit calls与restricted calls分开；统一原始SVD算术界NR。 | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, pp.3–4](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, pp.3–4](https://arxiv.org/pdf/2403.06634) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, pp.3–4](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, pp.3–4](https://arxiv.org/pdf/2403.06634) |
| top-K common-reference<br>notes: 每call K−1新logits；top1另有§5.4方法。 | 1/(K−1) calls/logit [api_calls_per_logit]<br>[§5.3, p.5](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.3, p.5](https://arxiv.org/pdf/2403.06634) | NR [api_calls_per_logit]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.3, p.5](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§5.3, p.5](https://arxiv.org/pdf/2403.06634) |
| 无logprobs binary search<br>notes: N logits，B gap bound，ε tolerance。 | N log(B/ε) [api_calls]<br>[Appendix F](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix F](https://arxiv.org/pdf/2403.06634) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix F](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Appendix F](https://arxiv.org/pdf/2403.06634) |
| 实际单logit恢复<br>notes: 精度分别23/11.5/6.1/18bits；不同方法逐项绑定，理论1/5不能代实测0.64。 | NR [api_calls_per_logit]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.7](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.7](https://arxiv.org/pdf/2403.06634) | top5/reference=0.25; theoretical-five-logit implementation=0.64; top1=1.0; no-logprob one-of-n=3.7 [api_calls_per_logit]<br>[Table 4, p.7](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 4, p.7](https://arxiv.org/pdf/2403.06634) |
| ada输出投影<br>notes: h1024；2024费用$4，RMS5e−4。 | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | <2e7 [api_calls]<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) |
| babbage输出投影<br>notes: h2048；2024费用$12，RMS7e−4；GPT3.5-turbo-instruct <4e8/$2000和1106 <4e8/$8000为未实施估计，不登记实测。 | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | <4e7 [api_calls]<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 3, p.7](https://arxiv.org/pdf/2403.06634) |

### arxiv-2403.09539: [Logits of API-Protected LLMs Leak Proprietary Information](https://arxiv.org/abs/2403.09539)

Oracle / 预言机: oracle/目标：logprob+logit_bias API，softmax bottleneck的image/输出空间/hidden dimension；CLR/Aitchison几何下low-dimensional probabilities，不宜错误描述为普通概率向量在欧式空间直接线性子空间。.

Scope / 范围: oracle/目标：logprob+logit_bias API，softmax bottleneck的image/输出空间/hidden dimension；CLR/Aitchison几何下low-dimensional probabilities，不宜错误描述为普通概率向量在欧式空间直接线性子空间。

Assumptions / 假设: oracle/目标：logprob+logit_bias API，softmax bottleneck的image/输出空间/hidden dimension；CLR/Aitchison几何下low-dimensional probabilities，不宜错误描述为普通概率向量在欧式空间直接线性子空间。

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| 单个完整输出恢复<br>notes: v词表、k top-logprobs、d embedding、n stochastic outputs；CLR/Aitchison输出空间，非普通欧式概率线性空间。 | ordinary v/k; reference v/(k−1); expected robust n v/(k−2); no-logprob v log(β_max/ε) [api_calls]<br>[Table 1, §3, pp.4–6](https://arxiv.org/pdf/2403.09539) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, §3, pp.4–6](https://arxiv.org/pdf/2403.09539) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, §3, pp.4–6](https://arxiv.org/pdf/2403.09539) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, §3, pp.4–6](https://arxiv.org/pdf/2403.09539) |
| image与dimension预处理<br>notes: d independent outputs；不是隐层权重恢复。 | image O(vd) ignoring k; O(vd/k) with caching; dimension-only O(d²/k) [api_calls]<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) |
| precomputed image后边际输出<br>notes: 另本地线性重构；不是首次image成本。 | O(d) with k treated constant [api_calls]<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[§4, p.6; Algorithm 2, p.7](https://arxiv.org/pdf/2403.09539) |
| 说明性成本示例<br>notes: v100000,d4096,k5,n4,ε1e−6,βmax100：20k/25k/133k，image费用$410/$512/$2724、缓存后800calls均back-of-envelope非实付。GPT3.5维数4096≤d≤4650非exact4096。 | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §4/Fig.2, p.7](https://arxiv.org/pdf/2403.09539) | NR [arithmetic_operations]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §4/Fig.2, p.7](https://arxiv.org/pdf/2403.09539) | NR [api_calls]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §4/Fig.2, p.7](https://arxiv.org/pdf/2403.09539) | NR [seconds]<br>在上述定位的方法/复杂度/实验内容未报告该阶段独立可引用值；完整限制见 details 与分组文档。<br>[Table 1, p.5; §4/Fig.2, p.7](https://arxiv.org/pdf/2403.09539) |

## PPML 与更强侧信道预言机 (6)

### eprint-2026-848: [Cryptanalytic Extraction of Neural Networks for Privacy-Preserving Machine Learning](https://eprint.iacr.org/2026/848)

Oracle / 预言机: finite-ring wraparound; raw outputs or top-1 probability.

Scope / 范围: layerwise signatures and signs

Assumptions / 假设: observable wraparound; local nondegeneracy; previous layers perfect; cleartext MPC simulation M=2^64,S=2^6

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| wraparound discovery / local normal / aggregation<br>dimensions: 3072-256×4-10 / 100-200×4-10<br>precision: fixed-point; ReLU ~14 bits, smooth activations ~7–10 bits<br>target: layerwise signatures and signs<br>notes: 1 point/neuron first layer, ~9–28 deeper. Point counts are not oracle calls. Expanded LeakyReLU only first two layers; sigmoid/tanh no later wraparound. | NR<br>Reviewed Alg.5; §4; Table5 pp.24–25; no independent bound/value reported for this stage.<br>[Alg.5; §4; Table5 pp.24–25](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed Alg.5; §4; Table5 pp.24–25; no independent bound/value reported for this stage.<br>[Alg.5; §4; Table5 pp.24–25](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed Alg.5; §4; Table5 pp.24–25; no independent bound/value reported for this stage.<br>[Alg.5; §4; Table5 pp.24–25](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed Alg.5; §4; Table5 pp.24–25; no independent bound/value reported for this stage.<br>[Alg.5; §4; Table5 pp.24–25](https://eprint.iacr.org/2026/848.pdf) |
| naive multi-point combination (not implemented)<br>target: layerwise signatures and signs<br>notes: Naive alternative not experimentally evaluated; not total pipeline complexity. | NR<br>Reviewed §6.1 p.25; no independent bound/value reported for this stage.<br>[§6.1 p.25](https://eprint.iacr.org/2026/848.pdf) | O(N^m) [operations]<br>[§6.1 p.25](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed §6.1 p.25; no independent bound/value reported for this stage.<br>[§6.1 p.25](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed §6.1 p.25; no independent bound/value reported for this stage.<br>[§6.1 p.25](https://eprint.iacr.org/2026/848.pdf) |
| pseudoinverse direction and sign voting<br>dimensions: 1024 hidden neurons<br>target: layerwise signatures and signs<br>notes: Mean wraparound point counts ReLU24.82→6.61, LeakyReLU7.25→5.09, nonlinear14.58→5.22; 100% signs in this benchmark. Independent Gaussian / wide-limit stability assumptions; no full Q/T bound. | NR<br>Reviewed §5 Theorems5–7; Table7 p.27; no independent bound/value reported for this stage.<br>[§5 Theorems5–7; Table7 p.27](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed §5 Theorems5–7; Table7 p.27; no independent bound/value reported for this stage.<br>[§5 Theorems5–7; Table7 p.27](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed §5 Theorems5–7; Table7 p.27; no independent bound/value reported for this stage.<br>[§5 Theorems5–7; Table7 p.27](https://eprint.iacr.org/2026/848.pdf) | NR<br>Reviewed §5 Theorems5–7; Table7 p.27; no independent bound/value reported for this stage.<br>[§5 Theorems5–7; Table7 p.27](https://eprint.iacr.org/2026/848.pdf) |

### eprint-2024-1870: [A Divide-and-Conquer Strategy for Hard-Label Extraction of Deep Neural Networks via Side-Channel Attacks](https://eprint.iacr.org/2024/1870)

Oracle / 预言机: top-1 plus neuron-state EM side channel.

Scope / 范围: layerwise signatures/signs and final classifier

Assumptions / 假设: perfect previous layers; full-rank equations; main extraction assumes perfect states from one trace

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| critical point bisection<br>target: layerwise signatures/signs and final classifier | O(log₂(L₀/Δ)) [state-oracle calls per critical point]<br>[§4.1 p.13](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.1 p.13; no independent bound/value reported for this stage.<br>[§4.1 p.13](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.1 p.13; no independent bound/value reported for this stage.<br>[§4.1 p.13](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.1 p.13; no independent bound/value reported for this stage.<br>[§4.1 p.13](https://eprint.iacr.org/2024/1870.pdf) |
| signature least squares / alignment<br>target: layerwise signatures/signs and final classifier<br>notes: Rare states/input-off increase discovery cost; state accuracy85.9% single trace,7/13 voting >99%/>99.9%. Actual physical trace budget needs repetitions. | NR<br>Reviewed §4.2 pp.14–17; §4.3; §5.2 p.21; no independent bound/value reported for this stage.<br>[§4.2 pp.14–17; §4.3; §5.2 p.21](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.2 pp.14–17; §4.3; §5.2 p.21; no independent bound/value reported for this stage.<br>[§4.2 pp.14–17; §4.3; §5.2 p.21](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.2 pp.14–17; §4.3; §5.2 p.21; no independent bound/value reported for this stage.<br>[§4.2 pp.14–17; §4.3; §5.2 p.21](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.2 pp.14–17; §4.3; §5.2 p.21; no independent bound/value reported for this stage.<br>[§4.2 pp.14–17; §4.3; §5.2 p.21](https://eprint.iacr.org/2024/1870.pdf) |
| sign alignment using cached traces<br>target: layerwise signatures/signs and final classifier | 0 additional [state-oracle calls]<br>[§4.3; §5.2](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.3; §5.2; no independent bound/value reported for this stage.<br>[§4.3; §5.2](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.3; §5.2; no independent bound/value reported for this stage.<br>[§4.3; §5.2](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed §4.3; §5.2; no independent bound/value reported for this stage.<br>[§4.3; §5.2](https://eprint.iacr.org/2024/1870.pdf) |
| reported model extraction MLP-a<br>dimensions: MLP-a<br>target: layerwise signatures/signs and final classifier<br>notes: 99.5% sampled label agreement; final-layer errors exceed hidden-layer errors; no all-parameter precision guarantee. | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | 2^17.12 [perfect neuron-state oracle calls]<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) |
| reported model extraction MLP-b<br>dimensions: MLP-b<br>target: layerwise signatures/signs and final classifier<br>notes: 97.2% sampled label agreement; final-layer errors exceed hidden-layer errors; no all-parameter precision guarantee. | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | 2^26.2 [perfect neuron-state oracle calls]<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) |
| reported model extraction MLP-c 1.72M parameters<br>dimensions: MLP-c 1.72M parameters<br>target: layerwise signatures/signs and final classifier<br>notes: 93.2% sampled label agreement; final-layer errors exceed hidden-layer errors; no all-parameter precision guarantee. | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | 2^26 [perfect neuron-state oracle calls]<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) |
| reported model extraction truncated MobileNetv1 5234 parameters<br>dimensions: truncated MobileNetv1 5234 parameters<br>target: layerwise signatures/signs and final classifier<br>notes: 88.4% sampled label agreement; final-layer errors exceed hidden-layer errors; no all-parameter precision guarantee. | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | 2^18.6 [perfect neuron-state oracle calls]<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) | NR<br>Reviewed Table3 p.23; no independent bound/value reported for this stage.<br>[Table3 p.23](https://eprint.iacr.org/2024/1870.pdf) |

### arxiv-1810.09076: [CSI Neural Network: Using Side-channels to Recover Your Artificial Neural Network Information](https://arxiv.org/abs/1810.09076)

Oracle / 预言机: embedded power/EM traces.

Scope / 范围: architecture, activation, floating-point weights

Assumptions / 假设: candidate range/precision and hardware-dependent leakage

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| timing structure / correlation weight search / layer propagation<br>target: architecture, activation, floating-point weights<br>notes: p.8 example1000 traces/group reused across weights. §VII implementation scaling linear in size and ~20s additional measurement discussion are not universal full-model runtime. Single-trace input recovery is separate. | NR<br>Reviewed §III; §V pp.5–12; §VII p.13; no independent bound/value reported for this stage.<br>[§III; §V pp.5–12; §VII p.13](https://arxiv.org/pdf/1810.09076) | NR<br>Reviewed §III; §V pp.5–12; §VII p.13; no independent bound/value reported for this stage.<br>[§III; §V pp.5–12; §VII p.13](https://arxiv.org/pdf/1810.09076) | NR<br>Reviewed §III; §V pp.5–12; §VII p.13; no independent bound/value reported for this stage.<br>[§III; §V pp.5–12; §VII p.13](https://arxiv.org/pdf/1810.09076) | NR<br>Reviewed §III; §V pp.5–12; §VII p.13; no independent bound/value reported for this stage.<br>[§III; §V pp.5–12; §VII p.13](https://arxiv.org/pdf/1810.09076) |

### arxiv-2002.11021: [SNIFF: Reverse Engineering of Neural Networks with Fault Attacks](https://arxiv.org/abs/2002.11021)

Oracle / 预言机: targeted sign-bit faults plus normal/fault outputs.

Scope / 范围: unknown last layer with known frozen feature extractor

Assumptions / 假设: fault localization; selected features nonzero; physical retries/search excluded

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| bias algebraic recovery<br>dimensions: m biases<br>precision: Keras float64 experiments ~10^-13 error<br>target: unknown last layer with known frozen feature extractor | m faults; 2m network executions [faults and network executions]<br>[Theorem1 p.5; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem1 p.5; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem1 p.5; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem1 p.5; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem1 p.5; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem1 p.5; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem1 p.5; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) |
| weight algebraic recovery<br>dimensions: n×m weights<br>precision: Keras float64 experiments ~10^-13 error<br>target: unknown last layer with known frozen feature extractor | nm faults; 2nm network executions [faults and network executions]<br>[Theorem2; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem2; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem2; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem2; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem2; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed Theorem2; Corollary1–2 p.6; no independent bound/value reported for this stage.<br>[Theorem2; Corollary1–2 p.6](https://arxiv.org/pdf/2002.11021) |
| nonzero input search / physical fault localization<br>target: unknown last layer with known frozen feature extractor<br>notes: Not included in algebraic execution counts. | NR<br>Reviewed §IV–V; no independent bound/value reported for this stage.<br>[§IV–V](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed §IV–V; no independent bound/value reported for this stage.<br>[§IV–V](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed §IV–V; no independent bound/value reported for this stage.<br>[§IV–V](https://arxiv.org/pdf/2002.11021) | NR<br>Reviewed §IV–V; no independent bound/value reported for this stage.<br>[§IV–V](https://arxiv.org/pdf/2002.11021) |

### arxiv-2503.19142: [Activation Functions Considered Harmful: Recovering Neural Network Weights through Controlled Channels](https://arxiv.org/abs/2503.19142)

Oracle / 预言机: SGX-Step instruction-granularity page traces.

Scope / 范围: first-layer weights/biases; deeper unsigned sets

Assumptions / 假设: controllable inputs; input-dependent activation branches; physical trace capabilities

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| input-center calibration<br>target: first-layer weights/biases; deeper unsigned sets<br>notes: P unknowns per neuron; D exponential calibration increments; separate from Q=PNS. | C=(P−1)D [trace-bearing inference calls]<br>[§V-A p.9](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A p.9; no independent bound/value reported for this stage.<br>[§V-A p.9](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A p.9; no independent bound/value reported for this stage.<br>[§V-A p.9](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A p.9; no independent bound/value reported for this stage.<br>[§V-A p.9](https://arxiv.org/pdf/2503.19142) |
| activation threshold bisection<br>dimensions: insurance first layer 1200 parameters<br>precision: 55 bisection steps ≥3 decimal digits; ~20 steps mean error <1%<br>hardware: SGX-Step setup<br>target: first-layer weights/biases; deeper unsigned sets<br>notes: P unknowns/neuron,N neurons,S bisection depth; excludes general physical failure costs. MNIST100480 parameters /1180765 calls is extrapolation, not completed recovery. | Q=P·N·S [trace-bearing inference calls]<br>[§IV-C p.7; §V-A pp.9–10](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §IV-C p.7; §V-A pp.9–10; no independent bound/value reported for this stage.<br>[§IV-C p.7; §V-A pp.9–10](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §IV-C p.7; §V-A pp.9–10; no independent bound/value reported for this stage.<br>[§IV-C p.7; §V-A pp.9–10](https://arxiv.org/pdf/2503.19142) | ~10 seconds/input trace [seconds per input trace]<br>[§IV-C p.7; §V-A pp.9–10](https://arxiv.org/pdf/2503.19142) |
| linear solve / deeper convergence sets<br>target: first-layer weights/biases; deeper unsigned sets<br>notes: Deeper layers not fully solved; no general end-to-end exact recovery theorem. | NR<br>Reviewed §V-A–B pp.9–11; no independent bound/value reported for this stage.<br>[§V-A–B pp.9–11](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A–B pp.9–11; no independent bound/value reported for this stage.<br>[§V-A–B pp.9–11](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A–B pp.9–11; no independent bound/value reported for this stage.<br>[§V-A–B pp.9–11](https://arxiv.org/pdf/2503.19142) | NR<br>Reviewed §V-A–B pp.9–11; no independent bound/value reported for this stage.<br>[§V-A–B pp.9–11](https://arxiv.org/pdf/2503.19142) |

### arxiv-2610.33671: [Extraction meets Distillation - cryptanalytic techniques to recover parameters from a Deep Neural Network](https://arxiv.org/abs/2610.33671)

Oracle / 预言机: Labels plus privileged logits/gradients, hidden activations and victim parameters in evaluated pipeline.

Scope / 范围: Combines assisted partial direction recovery with label-based reconstruction. Privileged prefixes, scaling/acceptance and sign walks remain; a complete reconstructed classifier and high sampled agreement do not establish label-only end-to-end or exact parameter extraction. / 将有内部信息辅助的部分方向恢复与标签学习重建组合；仍使用真实前缀、缩放/验收及符号游走信息。得到完整分类器和较高采样一致率不证明仅标签端到端或精确参数提取。

Assumptions / 假设: Known architecture and activation; evaluated pipeline retains privileged true prefixes, acceptance/scaling and sign-walk information. Six synthetic victims and two CIFAR-10 models; evaluation protocols kept separate.

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| 有内部信息辅助的方向获取（阶段 1）<br>notes: Range over 48 seeded synthetic-victim runs; privileged margins, gradients, activations and scalar parameter reads are additional, heterogeneous channels. Never a total hard-label-only attack budget. | NR [oracle_calls]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§3.4 Table 1, pp.13–14; §7.8, pp.35–36](https://arxiv.org/pdf/2610.33671v1) | NR [arithmetic_operations]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§3.4 Table 1, pp.13–14; §7.8, pp.35–36](https://arxiv.org/pdf/2610.33671v1) | 704,964–12,027,750 labels per seeded run [oracle_calls]<br>[§3.4 Table 1, pp.13–14; §7.8, pp.35–36](https://arxiv.org/pdf/2610.33671v1) | NR [wall_clock]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§3.4 Table 1, pp.13–14; §7.8, pp.35–36](https://arxiv.org/pdf/2610.33671v1) |
| 标签学习重建（阶段 3）<br>notes: Phase-3 repeated per-input requests over the six synthetic victims; 15 batch calls is not 15 queries. Uses assisted extraction artifacts; agreement is not parameter identity. The §7 six-victim batch duration of 14 min 19 s includes both search arms and reporting, not full extraction runtime or a controlled speedup. | NR [oracle_calls]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§7 pp.24–26; §7.7–7.8 pp.32–36](https://arxiv.org/pdf/2610.33671v1) | NR [arithmetic_operations]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§7 pp.24–26; §7.7–7.8 pp.32–36](https://arxiv.org/pdf/2610.33671v1) | 57,000–211,024 joint-fit; 29,024–96,024 split-fit label requests [oracle_calls]<br>[§7 pp.24–26; §7.7–7.8 pp.32–36](https://arxiv.org/pdf/2610.33671v1) | NR [wall_clock]<br>No independent cost for this stage reported in the cited methods/results; null is not zero.<br>[§7 pp.24–26; §7.7–7.8 pp.32–36](https://arxiv.org/pdf/2610.33671v1) |

## 有限精度与可行性 (1)

### eprint-2026-1943: [Finite-Precision Error Analysis of Cryptanalytic Model Extraction](https://eprint.iacr.org/2026/1943)

Oracle / 预言机: finite-precision numeric oracle.

Scope / 范围: local error analysis; not new end-to-end extraction

Assumptions / 假设: single switch; accurate prefix/recovery matrices; conditioning and downstream sensitivity

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| local four-evaluation directional difference<br>target: local error analysis; not new end-to-end extraction<br>notes: Reuse separate; not critical point search/full attack. Relative error ≤ S_Q μ_R κ₂(M̃) u_O/h; μ_R=1/&#124;cᵣη&#124;. | 4 evaluations/direction; 4m evaluation terms for m directions [oracle evaluations]<br>[Theorem1 pp.14–15](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed Theorem1 pp.14–15; no independent bound/value reported for this stage.<br>[Theorem1 pp.14–15](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed Theorem1 pp.14–15; no independent bound/value reported for this stage.<br>[Theorem1 pp.14–15](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed Theorem1 pp.14–15; no independent bound/value reported for this stage.<br>[Theorem1 pp.14–15](https://eprint.iacr.org/2026/1943.pdf) |
| finite precision evaluation<br>precision: float32/float64<br>target: local error analysis; not new end-to-end extraction<br>notes: κ₂=√((1+&#124;cosθ&#124;)/(1−&#124;cosθ&#124;)); no universal bit threshold; larger h trades rounding vs multiple crossings. | NR<br>Reviewed §4 pp.20–24; §5.1 Proposition3 p.26; no independent bound/value reported for this stage.<br>[§4 pp.20–24; §5.1 Proposition3 p.26](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed §4 pp.20–24; §5.1 Proposition3 p.26; no independent bound/value reported for this stage.<br>[§4 pp.20–24; §5.1 Proposition3 p.26](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed §4 pp.20–24; §5.1 Proposition3 p.26; no independent bound/value reported for this stage.<br>[§4 pp.20–24; §5.1 Proposition3 p.26](https://eprint.iacr.org/2026/1943.pdf) | NR<br>Reviewed §4 pp.20–24; §5.1 Proposition3 p.26; no independent bound/value reported for this stage.<br>[§4 pp.20–24; §5.1 Proposition3 p.26](https://eprint.iacr.org/2026/1943.pdf) |
| new sign/output-layer extraction<br>target: local error analysis; not new end-to-end extraction | NA<br>This work does not introduce this extraction stage.<br>[Theorem1; §4–5](https://eprint.iacr.org/2026/1943.pdf) | NA<br>This work does not introduce this extraction stage.<br>[Theorem1; §4–5](https://eprint.iacr.org/2026/1943.pdf) | NA<br>This work does not introduce this extraction stage.<br>[Theorem1; §4–5](https://eprint.iacr.org/2026/1943.pdf) | NA<br>This work does not introduce this extraction stage.<br>[Theorem1; §4–5](https://eprint.iacr.org/2026/1943.pdf) |

## 防御与适应性评价 (2)

### arxiv-2509.16546: [Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks](https://arxiv.org/abs/2509.16546)

Oracle / 预言机: training defense plus existing extraction evaluator.

Scope / 范围: neuron similarity regularization; measured attack resistance

Assumptions / 假设: geometric sampling model; secure operationally means attack failed within48h, not universal safety

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| regularized training / tuning<br>target: neuron similarity regularization; measured attack resistance<br>notes: Measured inference overhead0; training cost independent and NR; selected configurations accuracy change<1%. | NR<br>Reviewed §3.2 Theorem1 p.5; §3.3 p.7; no independent bound/value reported for this stage.<br>[§3.2 Theorem1 p.5; §3.3 p.7](https://arxiv.org/pdf/2509.16546) | NR<br>Reviewed §3.2 Theorem1 p.5; §3.3 p.7; no independent bound/value reported for this stage.<br>[§3.2 Theorem1 p.5; §3.3 p.7](https://arxiv.org/pdf/2509.16546) | NR<br>Reviewed §3.2 Theorem1 p.5; §3.3 p.7; no independent bound/value reported for this stage.<br>[§3.2 Theorem1 p.5; §3.3 p.7](https://arxiv.org/pdf/2509.16546) | NR<br>Reviewed §3.2 Theorem1 p.5; §3.3 p.7; no independent bound/value reported for this stage.<br>[§3.2 Theorem1 p.5; §3.3 p.7](https://arxiv.org/pdf/2509.16546) |
| baseline attack evaluation<br>dimensions: MNIST784-16×8-1(s2)<br>target: neuron similarity regularization; measured attack resistance<br>notes: 4 extraction seeds; accuracy drop0.92 percentage points for associated defense;48h cutoff is not proof. | NR<br>Reviewed Table1 p.8; no independent bound/value reported for this stage.<br>[Table1 p.8](https://arxiv.org/pdf/2509.16546) | NR<br>Reviewed Table1 p.8; no independent bound/value reported for this stage.<br>[Table1 p.8](https://arxiv.org/pdf/2509.16546) | 5.65×10^6 [numeric oracle calls]<br>[Table1 p.8](https://arxiv.org/pdf/2509.16546) | signature 1.12×10^4 s; sign80.37 s [seconds]<br>[Table1 p.8](https://arxiv.org/pdf/2509.16546) |
| new critical-point/signature/sign extraction algorithm<br>target: neuron similarity regularization; measured attack resistance | NA<br>This work does not introduce this extraction stage.<br>[§3; Table1](https://arxiv.org/pdf/2509.16546) | NA<br>This work does not introduce this extraction stage.<br>[§3; Table1](https://arxiv.org/pdf/2509.16546) | NA<br>This work does not introduce this extraction stage.<br>[§3; Table1](https://arxiv.org/pdf/2509.16546) | NA<br>This work does not introduce this extraction stage.<br>[§3; Table1](https://arxiv.org/pdf/2509.16546) |

### mit-2026-rounding: [Output Rounding Is Not a Free Defense Against Cryptanalytic Neural Network Extraction](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf)

Oracle / 预言机: known-spacing rounded numeric outputs.

Scope / 范围: useful approximate extraction of small ReLU models

Assumptions / 假设: course report; relative loss<0.5 on20000 held-out Gaussian probes

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| quantization crossing / derivatives / clustering / final least squares<br>target: useful approximate extraction of small ReLU models<br>notes: No independent stage bounds. | NR<br>Reviewed §4 Alg.1 pp.5–7; no independent bound/value reported for this stage.<br>[§4 Alg.1 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed §4 Alg.1 pp.5–7; no independent bound/value reported for this stage.<br>[§4 Alg.1 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed §4 Alg.1 pp.5–7; no independent bound/value reported for this stage.<br>[§4 Alg.1 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed §4 Alg.1 pp.5–7; no independent bound/value reported for this stage.<br>[§4 Alg.1 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| exhaustive / meet-in-middle signs<br>target: useful approximate extraction of small ReLU models | NR<br>Reviewed §4.3 pp.5–7; no independent bound/value reported for this stage.<br>[§4.3 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | exponential sign search (no explicit exponent given) [operations]<br>[§4.3 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed §4.3 pp.5–7; no independent bound/value reported for this stage.<br>[§4.3 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed §4.3 pp.5–7; no independent bound/value reported for this stage.<br>[§4.3 pp.5–7](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=32<br>dimensions: 80-40-1<br>precision: rounding N=32<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error 0.12; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 7.7M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=20<br>dimensions: 80-40-1<br>precision: rounding N=20<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error 0.11; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 9.0M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=18<br>dimensions: 80-40-1<br>precision: rounding N=18<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error 0.35; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 12.2M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=16<br>dimensions: 80-40-1<br>precision: rounding N=16<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error 0.68; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 31.5M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=8<br>dimensions: 80-40-1<br>precision: rounding N=8<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error 0.74; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 47.8M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |
| single-seed rounded model N=4<br>dimensions: 80-40-1<br>precision: rounding N=4<br>target: useful approximate extraction of small ReLU models<br>notes: Relative output error FAIL; query growth does not imply improvement. | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | 46.1M [rounded numeric oracle calls]<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) | NR<br>Reviewed Table2 p.9; no independent bound/value reported for this stage.<br>[Table2 p.9](https://65610.csail.mit.edu/2026/reports/cryptanalytic_nn_extract.pdf) |

## 相关可辨识性与学习理论 (8)

### arxiv-1807.05185: [Model Reconstruction from Model Explanations](https://arxiv.org/abs/1807.05185)

Oracle / 预言机: function plus input gradient; alternative membership simulation.

Scope / 范围: bias-free shallow ReLU equivalent function

Assumptions / 假设: h≤d; independent weight rows; probability≥1−δ; failure reported

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| gradient jumps / signs linear system: total<br>target: bias-free shallow ReLU equivalent function<br>notes: Alg.1a random line bisection,Alg.1b rank-h matrix/2h system; not arbitrary deep theorem. | O(h log(h/δ)) [function-and-gradient oracle calls]<br>[Theorem1 p.3; §3 pp.4–5](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Theorem1 p.3; §3 pp.4–5; no independent bound/value reported for this stage.<br>[Theorem1 p.3; §3 pp.4–5](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Theorem1 p.3; §3 pp.4–5; no independent bound/value reported for this stage.<br>[Theorem1 p.3; §3 pp.4–5](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Theorem1 p.3; §3 pp.4–5; no independent bound/value reported for this stage.<br>[Theorem1 p.3; §3 pp.4–5](https://arxiv.org/pdf/1807.05185) |
| gradient simulated via values: total<br>target: bias-free shallow ReLU equivalent function | O(dh log(h/δ)) [membership calls]<br>[Appendix C](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Appendix C; no independent bound/value reported for this stage.<br>[Appendix C](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Appendix C; no independent bound/value reported for this stage.<br>[Appendix C](https://arxiv.org/pdf/1807.05185) | NR<br>Reviewed Appendix C; no independent bound/value reported for this stage.<br>[Appendix C](https://arxiv.org/pdf/1807.05185) |

### arxiv-2105.09673: [An Exact Poly-Time Membership-Queries Algorithm for Extraction a three-Layer ReLU Network](https://arxiv.org/abs/2105.09673)

Oracle / 预言机: exact real membership queries.

Scope / 范围: depth2/depth3 equivalent function including possible affine term

Assumptions / 假设: δ-regular; depth3 d1≤d; nonzero relevant top derivatives; real arithmetic

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| single critical point<br>target: depth2/depth3 equivalent function including possible affine term | O(log(1/δ)) [membership calls]<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) |
| local affine<br>target: depth2/depth3 equivalent function including possible affine term | d+1 [membership calls]<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) |
| hyperplane<br>target: depth2/depth3 equivalent function including possible affine term | O(d) [membership calls]<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) |
| convexity / critical test<br>target: depth2/depth3 equivalent function including possible affine term | O(1) [membership calls]<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §3.2; no independent bound/value reported for this stage.<br>[§3.2](https://arxiv.org/pdf/2105.09673) |
| depth2 total<br>target: depth2/depth3 equivalent function including possible affine term<br>notes: C_Q oracle latency; mixed T kept distinct from pure operation count. | O(d₁log(1/δ)+d₁d) [membership calls]<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | T=O((d₁log(1/δ)+d₁d)C_Q+d²d₁) [mixed oracle time + local arithmetic]<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; no independent bound/value reported for this stage.<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; no independent bound/value reported for this stage.<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) |
| positive-orthant restriction total<br>target: depth2/depth3 equivalent function including possible affine term | O(dd₁log(1/δ)+d₁d) [membership calls]<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | T includes d²d₁² plus oracle time [mixed oracle time + local arithmetic]<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; no independent bound/value reported for this stage.<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; no independent bound/value reported for this stage.<br>[§2 Theorems1–3](https://arxiv.org/pdf/2105.09673) |
| depth3 total<br>target: depth2/depth3 equivalent function including possible affine term | poly(d,d₁,d₂,log(1/δ)) [membership calls]<br>[§2 Theorems1–3; §3.5](https://arxiv.org/pdf/2105.09673) | poly(d,d₁,d₂,log(1/δ)) time [conditional real-arithmetic time]<br>[§2 Theorems1–3; §3.5](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; §3.5; no independent bound/value reported for this stage.<br>[§2 Theorems1–3; §3.5](https://arxiv.org/pdf/2105.09673) | NR<br>Reviewed §2 Theorems1–3; §3.5; no independent bound/value reported for this stage.<br>[§2 Theorems1–3; §3.5](https://arxiv.org/pdf/2105.09673) |

### arxiv-2211.04589: [Finite Sample Identification of Wide Shallow Neural Networks with Biases](https://arxiv.org/abs/2211.04589)

Oracle / 预言机: function values / finite differences.

Scope / 范围: known-width shallow parameters

Assumptions / 假设: sphere-random weights; bounded bias; M1–M3 learnability; m log²m=O(D²)

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| finite-difference Hessian<br>target: known-width shallow parameters<br>notes: Derived composition: Nh Hessians and O(D^n) order-n derivative primitive, n=2; not new theorem. | Derived / 推导: O(Nh D²) [function calls]<br>[G2 p.5; Alg.1 p.6](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed G2 p.5; Alg.1 p.6; no independent bound/value reported for this stage.<br>[G2 p.5; Alg.1 p.6](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed G2 p.5; Alg.1 p.6; no independent bound/value reported for this stage.<br>[G2 p.5; Alg.1 p.6](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed G2 p.5; Alg.1 p.6; no independent bound/value reported for this stage.<br>[G2 p.5; Alg.1 p.6](https://arxiv.org/pdf/2211.04589) |
| direction/sign/bias initialization and refinement: total<br>target: known-width shallow parameters<br>notes: Wider D<m<D² global convergence is not uniform efficient polynomial runtime; numerical/α conditioning and propagated direction errors retained. | O(Dm²log²m) [function calls]<br>[Theorem1 p.2; Theorem2 pp.5–6](https://arxiv.org/pdf/2211.04589) | polynomial only in m=O(D) regime (no explicit exponent) [operations]<br>[Theorem1 p.2; Theorem2 pp.5–6](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed Theorem1 p.2; Theorem2 pp.5–6; no independent bound/value reported for this stage.<br>[Theorem1 p.2; Theorem2 pp.5–6](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed Theorem1 p.2; Theorem2 pp.5–6; no independent bound/value reported for this stage.<br>[Theorem1 p.2; Theorem2 pp.5–6](https://arxiv.org/pdf/2211.04589) |
| random tanh empirical phases<br>dimensions: D50,m1000<br>hardware: Tesla P100<br>target: random tanh shallow parameters<br>notes: Reported maxima/total bound, not sum of maxima for a single run. | NR<br>Reviewed §5 pp.10–11; no independent bound/value reported for this stage.<br>[§5 pp.10–11](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed §5 pp.10–11; no independent bound/value reported for this stage.<br>[§5 pp.10–11](https://arxiv.org/pdf/2211.04589) | NR<br>Reviewed §5 pp.10–11; no independent bound/value reported for this stage.<br>[§5 pp.10–11](https://arxiv.org/pdf/2211.04589) | Hessian+weights max112s; bias max180s; each total<5min [seconds / minutes]<br>[§5 pp.10–11](https://arxiv.org/pdf/2211.04589) |

### arxiv-2304.12794: [Expand-and-Cluster: Parameter Recovery of Neural Networks](https://arxiv.org/abs/2304.12794)

Oracle / 预言机: numeric input/output / teacher logits.

Scope / 范围: parameter recovery under activation symmetries

Assumptions / 假设: overparameterized students; population identifiability ≠ finite sample optimization guarantee

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| expansion selection / student training / layer freeze / fine-tune<br>hardware: V10032G<br>target: parameter recovery under activation symmetries<br>notes: Not actual per-model elapsed time. Applied budgets25k epochs,10k per layer,15k deep fine-tune;150 synthetic teachers,ρ4 succeeded118; application logits RMSE~10^-4. | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3 p.17; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3 p.17](https://arxiv.org/pdf/2304.12794) | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3 p.17; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3 p.17](https://arxiv.org/pdf/2304.12794) | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3 p.17; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3 p.17](https://arxiv.org/pdf/2304.12794) | synthetic budget3h gradient flow +6–12h BFGS; up to60min fine-tune [protocol budget hours/minutes]<br>[§5 Fig.3 p.5; Appendix A.6.2–3 p.17](https://arxiv.org/pdf/2304.12794) |
| cluster cached student vectors<br>target: parameter recovery under activation symmetries<br>notes: Reuses dataset; complete local operation bound NR. | 0 additional [teacher calls]<br>[§5 Fig.3 p.5; Appendix A.6.2–3](https://arxiv.org/pdf/2304.12794) | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3](https://arxiv.org/pdf/2304.12794) | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3](https://arxiv.org/pdf/2304.12794) | NR<br>Reviewed §5 Fig.3 p.5; Appendix A.6.2–3; no independent bound/value reported for this stage.<br>[§5 Fig.3 p.5; Appendix A.6.2–3](https://arxiv.org/pdf/2304.12794) |

### arxiv-2312.04675: [Reverse Engineering Deep ReLU Networks An Optimization-based Algorithm](https://arxiv.org/abs/2312.04675)

Oracle / 预言机: numeric input/output samples.

Scope / 范围: exploratory local hyperplane optimization / architecture conjecture

Assumptions / 假设: §5 main conjecture; detailed experiments deferred; higher-order convexity unresolved

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| sampling / local functions / weight optimization / structure<br>target: exploratory local hyperplane optimization / architecture conjecture<br>notes: All Q/T and full runtime/model size/success statistics NR; convexity alone does not prove unique minimum. | NR<br>Reviewed §3–5; §5 p.7; no independent bound/value reported for this stage.<br>[§3–5; §5 p.7](https://arxiv.org/pdf/2312.04675) | NR<br>Reviewed §3–5; §5 p.7; no independent bound/value reported for this stage.<br>[§3–5; §5 p.7](https://arxiv.org/pdf/2312.04675) | NR<br>Reviewed §3–5; §5 p.7; no independent bound/value reported for this stage.<br>[§3–5; §5 p.7](https://arxiv.org/pdf/2312.04675) | NR<br>Reviewed §3–5; §5 p.7; no independent bound/value reported for this stage.<br>[§3–5; §5 p.7](https://arxiv.org/pdf/2312.04675) |
| independent sign recovery<br>target: exploratory local hyperplane optimization / architecture conjecture | NA<br>This work does not introduce this extraction stage.<br>[§3–5](https://arxiv.org/pdf/2312.04675) | NA<br>This work does not introduce this extraction stage.<br>[§3–5](https://arxiv.org/pdf/2312.04675) | NA<br>This work does not introduce this extraction stage.<br>[§3–5](https://arxiv.org/pdf/2312.04675) | NA<br>This work does not introduce this extraction stage.<br>[§3–5](https://arxiv.org/pdf/2312.04675) |

### arxiv-2402.04084: [Provably learning a multi-head attention layer](https://arxiv.org/abs/2402.04084)

Oracle / 预言机: independent uniform {±1}^{k×d} samples plus real layer outputs.

Scope / 范围: attention/output composite matrices with distributional squared-error guarantee

Assumptions / 假设: m heads; §4 nondegeneracy; fixed m polynomial in k,d; no unique Q/K/V factor recovery

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| attention learning total<br>target: attention/output composite matrices with distributional squared-error guarantee<br>notes: Mean Frobenius squared error≤(kd)^−Ω(m); no phase allocation. Theorem1.3/§11 lower-bound construction has different nondegeneracy conditions. | N=(kd)^{Θ(m)}+poly(m,k,d)√log(1/δ) [random samples]<br>[Theorem1.2; §2; §5–10](https://arxiv.org/pdf/2402.04084) | T=(kd)^{O(m³)}log(1/δ) [algorithm time]<br>[Theorem1.2; §2; §5–10](https://arxiv.org/pdf/2402.04084) | NR<br>Reviewed Theorem1.2; §2; §5–10; no independent bound/value reported for this stage.<br>[Theorem1.2; §2; §5–10](https://arxiv.org/pdf/2402.04084) | NR<br>Reviewed Theorem1.2; §2; §5–10; no independent bound/value reported for this stage.<br>[Theorem1.2; §2; §5–10](https://arxiv.org/pdf/2402.04084) |
| ReLU critical/signature/sign/last-linear stages<br>target: attention/output composite matrices with distributional squared-error guarantee | NA<br>This work does not introduce this extraction stage.<br>[§2; §5–10](https://arxiv.org/pdf/2402.04084) | NA<br>This work does not introduce this extraction stage.<br>[§2; §5–10](https://arxiv.org/pdf/2402.04084) | NA<br>This work does not introduce this extraction stage.<br>[§2; §5–10](https://arxiv.org/pdf/2402.04084) | NA<br>This work does not introduce this extraction stage.<br>[§2; §5–10](https://arxiv.org/pdf/2402.04084) |

### arxiv-2411.07536: [Model Stealing for Any Low-Rank Language Model](https://arxiv.org/abs/2411.07536)

Oracle / 预言机: conditional random continuation samples at arbitrary history.

Scope / 范围: rank-S sequence distribution TV approximation

Assumptions / 假设: alphabet O,length T,TV≤η with probability≥1−η; not Transformer weights

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| conditional sampling / bases / KL projection: total<br>target: rank-S sequence distribution TV approximation | poly(S,O,T,1/η) [conditional sampling queries]<br>[Definition1.2; Theorem1.3 pp.3–4; §3](https://arxiv.org/pdf/2411.07536) | poly(S,O,T,1/η) [algorithm time]<br>[Definition1.2; Theorem1.3 pp.3–4; §3](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Definition1.2; Theorem1.3 pp.3–4; §3; no independent bound/value reported for this stage.<br>[Definition1.2; Theorem1.3 pp.3–4; §3](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Definition1.2; Theorem1.3 pp.3–4; §3; no independent bound/value reported for this stage.<br>[Definition1.2; Theorem1.3 pp.3–4; §3](https://arxiv.org/pdf/2411.07536) |
| representation primitive<br>target: rank-S sequence distribution TV approximation | poly(S,O,T,1/γ) [conditional sampling queries]<br>[Lemma3.7](https://arxiv.org/pdf/2411.07536) | poly(S,O,T,1/γ) [algorithm time]<br>[Lemma3.7](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Lemma3.7; no independent bound/value reported for this stage.<br>[Lemma3.7](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Lemma3.7; no independent bound/value reported for this stage.<br>[Lemma3.7](https://arxiv.org/pdf/2411.07536) |
| generation after learned description<br>target: rank-S sequence distribution TV approximation | 0 additional [original-model calls]<br>[Theorem1.3 pp.3–4](https://arxiv.org/pdf/2411.07536) | poly(S,O,T,log(1/η)) [time per generated sample]<br>[Theorem1.3 pp.3–4](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Theorem1.3 pp.3–4; no independent bound/value reported for this stage.<br>[Theorem1.3 pp.3–4](https://arxiv.org/pdf/2411.07536) | NR<br>Reviewed Theorem1.3 pp.3–4; no independent bound/value reported for this stage.<br>[Theorem1.3 pp.3–4](https://arxiv.org/pdf/2411.07536) |
| ReLU signature/sign/output-layer recovery<br>target: rank-S sequence distribution TV approximation | NA<br>This work does not introduce this extraction stage.<br>[§3 and subsequent proof](https://arxiv.org/pdf/2411.07536) | NA<br>This work does not introduce this extraction stage.<br>[§3 and subsequent proof](https://arxiv.org/pdf/2411.07536) | NA<br>This work does not introduce this extraction stage.<br>[§3 and subsequent proof](https://arxiv.org/pdf/2411.07536) | NA<br>This work does not introduce this extraction stage.<br>[§3 and subsequent proof](https://arxiv.org/pdf/2411.07536) |

### arxiv-2511.20312: [Data Augmentation Techniques to Reverse-Engineer Neural Network Weights from Input-Output Queries](https://arxiv.org/abs/2511.20312)

Oracle / 预言机: teacher numeric responses to augmented input.

Scope / 范围: training/Expand-and-Cluster recovery of512-hidden teacher

Assumptions / 假设: softplus(x)+sigmoid(4x); empirical only;1024 hidden stopped due RAM, not impossibility

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| augmentation collection: original MNIST failed<br>dimensions: 512 hidden,~407k parameters<br>target: training/Expand-and-Cluster recovery of512-hidden teacher<br>notes: original MNIST failed | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | 60000 [teacher numeric calls]<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) |
| augmentation collection: appropriate noise: mean/max input-vector cosine distances2.53×10^-8/3.34×10^-7<br>dimensions: 512 hidden,~407k parameters<br>target: training/Expand-and-Cluster recovery of512-hidden teacher<br>notes: appropriate noise: mean/max input-vector cosine distances2.53×10^-8/3.34×10^-7 | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | 180000 [teacher numeric calls]<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) |
| augmentation collection: rotation/flip/wrong-amplitude noise failed<br>dimensions: 512 hidden,~407k parameters<br>target: training/Expand-and-Cluster recovery of512-hidden teacher<br>notes: rotation/flip/wrong-amplitude noise failed | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | 180000 [teacher numeric calls]<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Table1 p.3; no independent bound/value reported for this stage.<br>[Table1 p.3](https://arxiv.org/pdf/2511.20312) |
| cached student training / clustering / fine-tune<br>dimensions: N30 students<br>hardware: V100/A100;512GB RAM limit<br>target: training/Expand-and-Cluster recovery of512-hidden teacher<br>notes: Local cost remains; steps=epochs×dataset/batch; unified wall-clock NR. | 0 additional [teacher calls]<br>[Appendix p.8](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Appendix p.8; no independent bound/value reported for this stage.<br>[Appendix p.8](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Appendix p.8; no independent bound/value reported for this stage.<br>[Appendix p.8](https://arxiv.org/pdf/2511.20312) | NR<br>Reviewed Appendix p.8; no independent bound/value reported for this stage.<br>[Appendix p.8](https://arxiv.org/pdf/2511.20312) |

## 综述与阅读资源 (2)

### arxiv-2508.15031: [A Systematic Survey of Model Extraction Attacks and Defenses: State-of-the-Art and Perspectives](https://arxiv.org/abs/2508.15031)

Oracle / 预言机: survey; no original attack oracle.

Scope / 范围: terminology / literature navigation

Assumptions / 假设: Shared reading repository is not an executable attack

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| original extraction / theoretical and empirical performance<br>target: terminology / literature navigation | NA<br>This work does not introduce this extraction stage.<br>[survey scope and referenced attacks/defenses](https://arxiv.org/pdf/2508.15031) | NA<br>This work does not introduce this extraction stage.<br>[survey scope and referenced attacks/defenses](https://arxiv.org/pdf/2508.15031) | NA<br>This work does not introduce this extraction stage.<br>[survey scope and referenced attacks/defenses](https://arxiv.org/pdf/2508.15031) | NA<br>This work does not introduce this extraction stage.<br>[survey scope and referenced attacks/defenses](https://arxiv.org/pdf/2508.15031) |

### arxiv-2506.22521: [A Survey on Model Extraction Attacks and Defenses for Large Language Models](https://arxiv.org/abs/2506.22521)

Oracle / 预言机: survey; no original attack oracle.

Scope / 范围: terminology / literature navigation

Assumptions / 假设: Shared reading repository is not an executable attack

| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |
|---|---|---|---|---|
| original extraction / theoretical and empirical performance<br>target: terminology / literature navigation | NA<br>This work does not introduce this extraction stage.<br>[§4 attacks; §5 defenses; §6 evaluation](https://arxiv.org/pdf/2506.22521) | NA<br>This work does not introduce this extraction stage.<br>[§4 attacks; §5 defenses; §6 evaluation](https://arxiv.org/pdf/2506.22521) | NA<br>This work does not introduce this extraction stage.<br>[§4 attacks; §5 defenses; §6 evaluation](https://arxiv.org/pdf/2506.22521) | NA<br>This work does not introduce this extraction stage.<br>[§4 attacks; §5 defenses; §6 evaluation](https://arxiv.org/pdf/2506.22521) |

