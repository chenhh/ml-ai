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

#### 範例

考慮一雙人賽局，玩家1, 2的行動集合分別為$$\mathcal{A}_1=\{r_1, r_2, r_3\}$$, $$A_2 =\{c_1, c_2 \}$$, 而對應的混合策略機率分別為$$\mathbf{s}_1=\{p_1, p_2, p_3\}$$與$$\mathbf{s}_2=\{q_1, q_2\}$$。

* 可得玩家1使用混合策略$$\mathbf{s}_1$$​的期望報酬為：$$p_1 q_1 u_1(r_1, c_1) + p_1 q_2 u_1(r_1, c_2) + p_2 q_1 u_1(r_2, c_1) + p_2 q_2 u_1 (r_2, c_2 ) + p_3 q_1 u_1(r_3, c_1) + p_3 q_2 u_1 (r_3, c_2)$$
* 同理可得玩家2使用混合策略$$\mathbf{s}_2$$的期望報酬為：$$p_1 q_1 u_2(r_1, c_1) + p_1 q_2 u_2(r_1, c_2) +  p_2 q_1 u_2(r_2, c_1) + p_2 q_2 u_2(r_2, c_2) +  p_3 q_1 u_2(r_3, c_1) + p_3 q_2 u_2(r_3, c_2)$$

### 賽局的過程

在一場多人賽局中，理性的玩家$$i$$​選擇一行動$$a_i \in \mathcal{A}_i$$以最大化自已的報酬$$u_i(a_i, \mathbf{a}_{-i})$$。

在這個賽局中，有兩個或更多的玩家；行動是玩家的決策變數；報酬函數是玩家從賽局中獲得的效用水平，它是所有玩家行動的函數，也是每個玩家真正關心的問題。

<mark style="color:red;">分析賽局的目的是根據賽局的規則來預測賽局的結果，均衡(equilibrium)是賽局的解決方案</mark>。均衡反映了賽局中玩家的行為模式和策略互動。非合作賽局中的納許均衡和合作賽局中的相關均衡都是賽局理論中最重要的概念。

* <mark style="color:red;">**非合作賽局(non-cooperative game)**</mark>是指玩家無法達成有約束力的協議。在非合作賽局的過程中，每個玩家在選擇策略時沒有串通或共識。他們只是選擇對自己最有利的策略，而不考慮其他人的利益。非合作賽局理論主要研究在利益相互影響的情況下，賽局者如何選擇策略以實現利益最大化，即策略選擇問題，它強調的是個體理性。
* <mark style="color:red;">**合作賽局(cooperative game)**</mark>不討論理性個體如何實現合作的過程，而是直接討論合作的結果和利潤的分享。

一個賽局可以依不同角度被分為兩個方面。首先是<mark style="color:red;">玩家的行動順序</mark>。從這個角度來看，可以被分為靜態賽局和動態賽局。

* <mark style="color:red;">靜態賽局</mark>，例如剪刀石頭布，<mark style="color:blue;">是指玩家在同一時間選擇行動</mark>，或者後一個玩家不知道前一個玩家採取了什麼具體行動，以正常（矩陣）形式表達的靜態賽局被稱為策略賽局。
* <mark style="color:red;">動態賽局</mark>，例如圍棋賽局，<mark style="color:blue;">是指棋手的行動是有順序的</mark>，後棋手可以觀察到前棋手選擇的行動，這種賽局通常以廣義（樹狀）形式表達。

第二個角度是<mark style="color:red;">玩家對其他玩家的特徵、策略空間和報酬函數的瞭解</mark>。從這個角度來看，賽局可以分為<mark style="color:red;">完全（完美）資訊賽局</mark>和<mark style="color:red;">不完全資訊賽局</mark>。

* 完全資訊賽局是指每個賽局者對所有其他賽局者的特徵、策略空間和報酬函數都有准確的瞭解。
* 如果賽局中的資訊不是完美的，那麼它就是不完全資訊賽局。

當這兩種觀點結合起來時，有四種不同的賽局類型，即：

* 完全資訊靜態賽局、
* 完全資訊動態賽局、
* 不完全資訊靜態賽局和
* 不完全資訊動態賽局。

與上述四種賽局類型相對應的是均衡的四個概念，分別是納許均衡、子賽局完美納什均衡、貝式-納許均衡和完美貝式-納許均衡。

投資組合選擇問題可以被表述為一個完全資訊重復的靜態賽局。

### 多期賽局的符號定義

考慮賽局$$\Gamma$$經過了離散的局數$$t=1,2,\dots$$，

* 時間$$t$$時，玩家$$i$$與其它玩家的<mark style="color:red;">行動方案</mark>為$$\mathbf{a}_t = (a_{i,t}, \mathbf{a}_{-i, t}) \in \mathcal{A}_i \times \mathcal{A}_{-i}$$。
* 時間$$t$$時，玩家$$i$$的<mark style="color:red;">報酬</mark>為$$u_i(a_{i,t}, \mathbf{a}_{-i, t})$$，且該玩家到時間$$t$$​的<mark style="color:red;">平均報酬</mark>為$$\overline{u_i(a_{i,t}, \mathbf{a}_{-i, t})} = \frac{1}{t} \sum_{\tau=1}^t u_i(a_{i,\tau}, \mathbf{a}_{-i, \tau})$$。
* <mark style="color:red;">時間</mark>$$t$$<mark style="color:red;">的歷史(history)</mark>，為賽局開始至時間$$t$$時，所有玩家所採取的行動方案$$\mathbf{h}_t=(\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_t) \in \mathcal{A}^t$$。
* <mark style="color:red;">玩家</mark>$$i$$<mark style="color:red;">在時間</mark>$$t$$<mark style="color:red;">的混合策略</mark>，會參考$$t-1$$的歷史，即$$\mathbf{s}_{i,t} \equiv \mathbf{s}_{i,t}(\mathbf{h}_{t-1}) \in \Delta(\mathcal{A}_i)$$。
* 而玩家$$i$$在時間$$t$$實際<mark style="color:red;">採取行動</mark>$$a_p$$<mark style="color:red;">的機率</mark>為$$\mathbf{s}_{i,t}[a_p]$$。
* 玩家$$i$$在時間$$t$$的<mark style="color:red;">策略軌跡(strategic trajectory)</mark>為$$\mathbf{s}_{i,1:t}=\{\mathbf{s}_{i,1}, \mathbf{s}_{i,2}, \dots, \mathbf{s}_{i,t} \} \equiv  \{ \mathbf{s}_{i,1}, \mathbf{s}_{i,1}(\mathbf{h}_1), \dots, \mathbf{s}_{i,t}(\mathbf{h}_{t-1}) \}$$會在單純形$$\Delta(\mathcal{A}_i)$$ 中形成一條路徑。
