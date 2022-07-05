---
description: 戰略賽局
---

# 策略賽局(strategic game)

## 多人單期策略賽局

> $$N$$人策略賽局$$\Gamma$$包含了三個基本元素：玩家、行動集合與支付函數(payoff function)。可寫成三元元組 $$\Gamma=(\mathcal{N}, (\mathcal{A_i})_{i \in \mathcal{N}}, (u_i)_{i \in \mathcal{N}})$$，
>
> * $$\mathcal{N}$$：為編號$$1 \sim N$$(或$$0 \sim N-1$$)的<mark style="color:red;">有限玩家（players)</mark>形成的集合。
> * $$\mathcal{A}_i$$：為玩家$$i$$的<mark style="color:red;">有限行動集合(action set)</mark>。(如果是無限行動集合，則報酬函數的定義域也必須是無限集合)。
> * $$u_i: \prod_{i\in \mathcal{N}} \mathcal{A}_i \rightarrow \mathbb{R}$$為玩家$$i$$的<mark style="color:red;">報酬函數(payoff function)</mark>，必須參考到其它玩家的所有行動才能得值。

由三元元組可定義：

* <mark style="color:red;">行動方案集合(set of action profiles)</mark>: $$\mathcal{A} = \prod_{i \in \mathcal{N}} \mathcal{A}_i$$為所有玩家的行動集合所形成的宇集合。
* 定義行動方案內的<mark style="color:red;">行動方案（action profile)</mark>為$$\mathbf{a} =(a_i)_{i \in \mathcal{N}}$$，而$$\mathbf{a}_{-i} =(a_j)_{j \in \mathcal{N},~ j \neq i}$$為行動方案中，除了玩家$$i$$的行動$$a_i$$之外，其餘玩家採取的所有行動。
* 因此<mark style="color:red;">賽局</mark>$$\Gamma$$<mark style="color:red;">的報酬函數</mark>$$u_\Gamma: \mathcal{A} \equiv \mathcal{A}_i \times \mathcal{A}_{-i} \rightarrow \mathbb{R}^N$$，而$$u_\Gamma(a_i, \mathbf{a}_{-i}) \in \mathbb{R}^n$$為玩家$$i$$採取行動$$a_i$$，且其它玩家們採取行動$$\mathbf{a}_{-i}$$時的報酬向量(payoff vector)。
* 玩家$$i$$<mark style="color:red;">行動的機率單純形</mark>$$\Delta (\mathcal{A}_i)$$的元素$$\mathbf{s}_i \in [0,1]^{|\mathcal{A}_i|}$$稱為玩家$$i$$的<mark style="color:red;">混合策略(mixed strategy)</mark>。
* 混合策略$$\mathbf{s}_i$$中，<mark style="color:red;">玩家</mark>$$i$$<mark style="color:red;">採取行動</mark>$$a_p$$<mark style="color:red;">的機率</mark>為$$\mathbf{s}_i[a_p] \geq 0$$, $$\displaystyle \Delta(\mathcal{A}_i) =\left\{ \mathbf{s}_i \in \mathbb{R}_+^{|\mathcal{A_i}|} ~\bigg| ~\sum_{p=1}^{|\mathcal{A_i}|} \mathbf{s}_i[a_p]=1 \right\}$$。
* 玩家$$i$$使用混合策略$$\mathbf{s}_i$$且其它玩家使用混合策略$$\mathbf{s}_{-i}$$的<mark style="color:red;">期望報酬</mark>為$$\displaystyle  u_i(\mathbf{s}_i, \mathbf{s}_{-i}) = \sum_{\mathbf{a} \in \mathcal{A}} \left( \prod_{j \in \mathcal{N}} \mathbf{s}_j[a_j] \right) u_i(\mathbf{a})$$。
* 如果玩家偏好某個行動，採取該行動的機率為１，則混合策略退化成<mark style="color:red;">單純策略(pure strategy)</mark>。&#x20;

例：

考慮一雙人賽局，玩家1, 2的行動集合分別為$$\mathcal{A}_1=\{r_1, r_2, r_3\}$$, $$A_2 =\{c_1, c_2 \}$$, 而對應的混合策略機率分別為$$\mathbf{s}_1=\{p_1, p_2, p_3\}$$與$$\mathbf{s}_2=\{q_1, q_2\}$$。

* 可得玩家1使用混合策略$$\mathbf{s}_1$$​的期望報酬為：$$p_1 q_1 u_1(r_1, c_1) + p_1 q_2 u_1(r_1, c_2) + p_2 q_1 u_1(r_2, c_1) + p_2 q_2 u_1 (r_2, c_2 ) + p_3 q_1 u_1(r_3, c_1) + p_3 q_2 u_1 (r_3, c_2)$$
* 同理可得玩家2使用混合策略$$\mathbf{s}_2$$的期望報酬為：$$p_1 q_1 u_2(r_1, c_1) + p_1 q_2 u_2(r_1, c_2) +  p_2 q_1 u_2(r_2, c_1) + p_2 q_2 u_2(r_2, c_2) +  p_3 q_1 u_2(r_3, c_1) + p_3 q_2 u_2(r_3, c_2)$$

### 多期賽局的符號定義
