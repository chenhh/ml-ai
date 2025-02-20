---
description: 可接近性理論
---

# Blackwell's Approachability Theorem

## 簡介

對抗性預測的歷史始於數學家David Blackwell和James Hannan的開創性工作。接近性理論起源於Blackwell的工作，並與Hannan的工作同時被發現。 幾十年來，人們對一般凸賽局中的遺憾最小化和Blackwell可接近性之間的關係並不完全瞭解。通常的想法是，事實上，Blackwell可接近性是一個更強的概念。在這一章中，<mark style="color:red;">我們表明可接近性和線上凸最佳化在強烈的意義上是等價的：兩者的演算法是等價的，而且沒有計算效率的損失</mark>。

賽局的報酬函數採取向量的形式，其元素代表不同的目標值，如利潤、風險等。具有不相同標準的賽局被稱為多標準賽局或具有向量報酬函數的賽局。單一目標最佳化問題的最優解，即最大解或最小解，是在實數上，因此很容易找出來。這一重要特徵對於確定向量最佳化問題的最優解是無效的，主要是因為向量空間中的次序一般是部分次序(partial order)而不是全序(total order)。因此Von-Neumann的最大最小化定理不能直接適用於向量報酬賽局。

Blackwell首次研究了具有向量報酬函數的零和賽局，他提供了兩人零和重覆賽局的可接近性定理。Shapley和Rigby介紹了向量賽局的均衡點的概念，他們提到賽局的報酬函數大多是向量值函數的形式。

<mark style="color:red;">內部或外部遺憾最小化問題的一個共同特點是，它們可以被寫成某些向量報酬賽局中精心選擇的目標集的可接近性的一個具體案例</mark>。

## 最小最大理論(Minmax theorem)

> 給定<mark style="color:blue;">單期</mark>雙人零合賽局，玩家1,2的行動集合分別有$$r,s$$個(有限個)行動，
>
> * 玩家1(玩家)的混合策略為$$\displaystyle \mathbf{p}=(p_1, p_2, \dots, p_r) \in \mathbf{P}, ~p_i \geq 0, ~ \sum_{i=1}^r p_i = 1$$。
> * 玩家2(對手或環境)的混合策略為$$\displaystyle \mathbf{q}=(q_1, q_2, \dots, q_s) \in \mathbf{Q}, ~q_j \geq 0, ~ \sum_{j=1}^s q_j = 1$$。
> * $$m(i,j) \in \mathbb{R}$$為玩家1,2分別採取實際行動$$i,j$$時，玩家1的報酬\[支付，越高越好]\(payoff)(零和遊戲，所以玩家2的報酬為$$-m(i,j)$$)。
>
> 則存在$$\mathbf{p} \in \mathbb{R}_{+}^r, ~ \mathbf{q} \in \mathbb{R}_{+}^s, ~ v \in \mathbb{R}$$ 滿足$$\sum_{i=1}^r p_i m(i, j) \geq v \geq \sum_{j=1}^s q_j m(i,j), ~ \forall i, j$$。
>
> * 玩家1存在一混合策略可保證報酬大於等於$$v$$，不論對手使用任意策略。
> * 玩家2也存在一混合策略可保證損失不會超過$$v$$，不論對手使用任意策略。
> *   因此$$v$$稱為此賽局的報酬。
>
>

$$\forall \epsilon > 0$$，在多期雙人零合賽局(報酬矩陣為$$M$$), 當$$t \rightarrow \infty$$，玩家1的報酬會以機率1大於$$v-\epsilon$$，而玩家2的損失會以機率1小於$$v+\epsilon$$。

### 範例

玩家1有三個行動$$R=(r_1, r_2, r_3)$$個別行動採用的機率為$$\mathbf{p}=(p_1, p_2, p_3)$$；玩家2有兩個行動$$S=(s_1, s_2)$$個別行動採用的機率為$$\mathbf{q}=(q_1, q_2)$$。

<mark style="color:red;">雙人零和賽局並不一定有</mark><mark style="color:red;">**鞍點（saddle point）**</mark><mark style="color:red;">，但一定有</mark><mark style="color:red;">**混合策略的均衡解**</mark><mark style="color:red;">，這是由</mark> <mark style="color:red;"></mark><mark style="color:red;">**Minimax 定理**</mark> <mark style="color:red;"></mark><mark style="color:red;">保證的</mark>。

### 有鞍點範例(使用單純策略即可)

<table><thead><tr><th>R\S</th><th>s1</th><th>s2</th><th width="100">min M</th></tr></thead><tbody><tr><td><span class="math">r_1</span></td><td><span class="math">m(1,1)=-1</span></td><td><span class="math">m(1,2)=9</span></td><td>-1</td></tr><tr><td><span class="math">r_2</span></td><td><span class="math">m(2,1)=-3</span></td><td><span class="math">m(2,2)=5</span></td><td>-3</td></tr><tr><td><span class="math">r_3</span></td><td><span class="math">m(3,1)=-5</span></td><td><span class="math">m(3,2)=8</span></td><td>-5</td></tr><tr><td>max M</td><td>-1</td><td>9</td><td>minmax: -1</td></tr></tbody></table>

### 無鞍點範例(改為混合策略即可)

<table><thead><tr><th>R\S</th><th>s1</th><th>s2</th><th width="100">min M</th></tr></thead><tbody><tr><td><span class="math">r_1</span></td><td><span class="math">m(1,1)=3</span></td><td><span class="math">m(1,2)=-1</span></td><td>-1</td></tr><tr><td><span class="math">r_2</span></td><td><span class="math">m(2,1)=2</span></td><td><span class="math">m(2,2)=1</span></td><td>1</td></tr><tr><td><span class="math">r_3</span></td><td><span class="math">m(3,1)=0</span></td><td><span class="math">m(3,2)=4</span></td><td>0</td></tr><tr><td>max M</td><td>3</td><td>4</td><td></td></tr></tbody></table>

玩家1採取行動$$r_1$$時，不論對手採取任何行動，可得到的最少報酬為-1。同樣採取行動$$r_2, r_3$$時，分別可得到最高報酬為$$-3,-5$$。玩家希望在這些「最差情況」中選擇最好的策略。這就是 maximin 策略，因此會選行動$$r_1$$報酬$$\max(-1,-3,-5)=-1$$。

玩家2採取行動$$s_1,s_2$$時，不論對手採取任何行動，最大損失分別為$$-1, 9$$。因此對手希望在這些「最差情況」中選擇最好的策略，最多損失為$$\min(-1,9)=-1$$。

<mark style="color:blue;">多期(重複)賽局時，玩家1存在策略可保證平均報酬不會低於-1；同理而玩家2存在策略可保證平均損失不會大於-1</mark>。

賽局價值為-1，可得對於玩家1而且，集合$$S=\{x \geq t\}, ~ t \leq -1$$都是可接近集合，集合$$T=\{x \geq t\}, ~ t > -1$$都是可排除集合。



## 向量報酬的賽局(Blackwell, 1956)

<mark style="color:blue;">單一的混合策略不能確保向量報酬</mark>$$m(i,j) \in \mathbb{R}^N$$<mark style="color:blue;">位於某個給定的集合中。然而，如果我們允許無限期的賽局時，並詢問是否存在一種策略來確保平均報酬向量位於某個集合中，或者至少在歐氏距離上接近它。這正是Blackwell提出的解決方案概念</mark>。

在實數報酬中的雙人零和賽局，玩家1、2可依最小最大定理逼近賽局的報酬$$v$$。<mark style="color:red;">而在向量報酬中，問題變成玩家1、2是否可逼近一個特定集合</mark>$$S$$(分一般集合與凸集合兩種情形討論)。

現在考慮雙人向量(非零和)賽局有限個行動中，$$m(i,j) \in \mathbb{R}^N$$為向量報酬的情形。報酬矩陣$$\mathbf{M}=[m(i,j)], ~ i \in \{1,2,\dots, r\}, ~ j \in \{1,2,\dots, s\}$$為$$r\times s$$的矩陣，矩陣中每個元素為$$N$$維的向量(<mark style="color:blue;">Blackwell論文中定義的是更一般化的形式，即每個元素</mark>$$m(i,j)$$<mark style="color:blue;">是(離散或連續)機率分佈，其定義域為一個封閉有界凸集</mark>$$X \in \mathbb{R}^N$$，值域為實數區間$$[0,1]$$<mark style="color:blue;">，因此當玩家1,2在時間</mark>$$t$$<mark style="color:blue;">採取行動</mark>$$i,j$$<mark style="color:blue;">時得到的報酬</mark>$$m(i,j)$$<mark style="color:blue;">是由分佈</mark>$$m(i,j)$$<mark style="color:blue;">所決定的隨機向量</mark>$$x_t$$)。

如果考慮每一個隨機向量$$m(i,j)$$的期望值$$\overline{m}(i,j)$$或簡寫為$$m(i,j)$$時，則報酬矩陣$$\mathbf{M}$$中的$$r\times s$$個向量點，可形成$$\mathbb{R}^N$$空間中的(有界)凸包(bounded convex hull, 為包含這些向量點的最小閉集合)，記為$$X \subseteq \mathbb{R}^N$$。或者說$$r\times s$$個點是閉凸集$$X$$​(不一定凸包)的元素。<mark style="color:blue;">注意此</mark>$$r\times s$$<mark style="color:blue;">個點並非均為凸包</mark>$$X$$<mark style="color:blue;">的端點，有些點是位於集合內部非端點</mark>。

玩家1使用混合策略序列$$f_{0:n} \equiv \{f_0, f_1(x_1), \dots, f_n(x_1, \dots, x_n)\}, ~f_n: (x_1, x_2, \dots, x_n) \rightarrow \mathbf{P}, ~x_i \in X$$，其中$$(x_1,x_2,\dots, x_n)$$為到第$$n$$期時已觀察到的報酬(或根據$$m(i,j)$$機率分佈的實現值)(history)。註：此處在第$$n$$期決策時，參考的是過去的所有資料(包含當期)，而不是Markov性質只參考前一期的資料。

而$$f_0$$因為沒有參考資料，所以為$$\mathbf{P}$$中的任意分佈$$\mathbf{p}=(p_1,\dots,p_r), ~\sum_{i=1}^r p_i=1$$，玩家1的混合策略序列為$$f_{0:n} \equiv \{f_0, f_1(\mathbf{x}_1), f_2(\mathbf{x}_1, \mathbf{x}_2),f_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$。

同理玩家2的的混合策略序列為$$g_{0:n} \equiv \{g_0, g_1(\mathbf{x}_1), g_2(\mathbf{x}_1, \mathbf{x}_2),g_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$

* 在初始$$n=0$$時，玩家1,2分別依混合策略$$f_0,g_0$$採取行動$$i_0,j_0$$，依機率分佈$$m(i_0,j_0)$$得到報酬實現值$$x_1$$。
* 之後玩家1,2分別依混合策略$$f_1(x_1), g_1(x_1)$$採取行動$$i_1, j_1$$，依報酬機率分佈$$m(i_1, j_1)$$得到報酬實現值$$x_2$$。
* 之後玩家1,2分別依混合策略$$f_2(x_1,x_2), g_2(x_1,x_2)$$採取行動$$i_2, j_2$$，依報酬機率分佈$$m(i_2, j_2)$$得到報酬實現值$$x_3$$，以此類推。

<mark style="background-color:red;">因此玩家1、2的混合策略</mark>$$(f,g)$$<mark style="background-color:red;">對序列以及報酬的機率分佈矩陣</mark>$$M$$<mark style="background-color:red;">​可決定向量報酬隨機變數</mark>$$x_1, x_2, \dots$$。

令$$S \subseteq \mathbb{R}^N$$為任意集合，$$\delta_n$$是平均向量報酬$$\sum_{i=1}^n x_i/n$$至集合$$S$$​的距離。依定義$$S \subseteq X$$才有意義(因為$$X$$中任意向量的均值必定還是在$$X$$中，所以討論$$X^c$$集合沒有意義)。

定義$$S$$​為使用在報酬矩陣$$M$$中玩家策略$$f^{*} \equiv f^{*}_{0:n}$$的<mark style="color:red;">可接近集合(approachable)</mark>若：

$$\forall \epsilon > 0~ \exists n_0 \in \mathbb{N} \ni$$$$\forall g ~ ,\mathrm{P}(\delta_n \geq \epsilon  \text{ for some } n \geq n_0 ) < \epsilon$$

* $$x_1,x_2, \dots, x_n$$​是由特定的玩家策略序列$$f^{*}$$與任意對手策略序列$$g \equiv g_{0:n}$$​所得到。
* 即只要賽局回合數$$n$$夠多，不論對手使用任意策略序列$$g$$​，平均報酬向量與集合的距離機率收斂至0。

稱$$S$$​為使用在報酬矩陣$$M$$​中對手特定策略序列$$g^{*}$$的<mark style="color:red;">可排除集合(excludable)</mark>若：

$$\exists d >0 \ni \forall \epsilon > 0, ~ n_0 \in \mathbb{N} \ni \forall f, ~\mathrm{P}(\delta_n \geq d ~ \forall n \geq n_0) > 1- \epsilon$$

* $$x_1, x_2,\dots, x_n$$​是玩家任意策略序列$$f_{0:n}$$​與對手特定策略$$g^{*}\equiv g^{*}_{0:n}$$所得到。
* 只要賽局回合數$$n$$​夠多，不論玩家使用任意策略$$f$$​，對手可用特定策略$$g^{*}$$使得平均報酬至集合的距離無法機率收斂。

Minimax定理($$N=1$$)以上述形式可改寫為：賽局價值$$v \in \mathbb{R}$$​，玩家與對手的混合策略$$p \in P,~ q \in Q$$，則

* 集合$$S=\{ x \geq t \}$$為可接近集合 $$\forall t \leq v$$且$$f:f_n\equiv p$$​.&#x20;
* 當$$t > v$$且$$g: g_n \equiv q$$​時，$$S$$​為可排除集合。

### 引理

由定義知<mark style="color:red;">可接近集合的超集合必為可接近集合(因為</mark>$$\delta_n$$<mark style="color:red;">距離可接近集合的長度必大於等於其超集合的長度)，且可排除集合的子集合仍為可排除集合</mark>。不存在同時為可接近且為可排除的集合。所以任意可接近集合$$S$$與可排除集合$$T$$的交集必為空集合，但是兩者並不是宇集合的分割。

由定義可知可接近(可排除)集合$$S$$的閉包$$\overline{S}$$也是可接近(可排除)集合，反之亦然，<mark style="color:red;">因此令</mark>$$S$$<mark style="color:red;">為閉集合</mark>。

若閉集合$$S$$​是報酬矩陣$$M^\top$$的可接近集合，則任何閉集合$$T$$​且與$$S$$​之交集為空時，在報酬矩陣$$M$$​中為可排除集合(why?)。idea: 將玩家與對手的角色對調時，報酬矩陣從$$M$$變為$$M^{\top}$$；此時若$$S$$為對手在報酬矩陣$$M^{\top}$$使用策略$$g^{*}$$相對於$$\forall f$$為可接近集合時，因為$$S$$的超集合仍為可接近集合，因此令$$T$$為與$$S$$不相交的閉集合；

### 可接近性的充份條件(sufficient condition)

#### 主要性質

$$x,y \in \mathbb{R}^N$$為相異兩點，而$$H$$為通過y且正交於線段$$xy$$的超平面，$$z \in \mathbb{R}^N$$為$$H$$上的任意點或者為$$x$$相對於$$H$$在另一側的任意點，那麼所有位於線段$$xz$$ 內部且充分接近 $$x$$ 的點都比 $$x$$ 更接近 $$y$$(由三角不等式得出)。此為可接近性的充分條件。

註：$$x$$為平均報酬，$$H$$為目標集合上任意點的切平面，如果玩家選定行為的下一期報酬$$z$$滿足上述性質，則可保證新的平均報酬往$$H$$方向前進。

{% tabs %}
{% tab title="plot" %}
<figure><img src="../.gitbook/assets/approachable_sufficient.png" alt="" width="432"><figcaption><p>可接近性的充分條件</p></figcaption></figure>
{% endtab %}

{% tab title="python" %}
```python
import matplotlib.pyplot as plt
import numpy as np

# 定義點 x 和 y
x = np.array([0, 0])
y = np.array([2, 2])

# 定義超平面 H
a = y[0] - x[0]
b = y[1] - x[1]
c = a * y[0] + b * y[1]

# 繪製點 x 和 y，並標記在旁邊，避免重疊
plt.plot(x[0], x[1], 'o')
plt.text(x[0] - 0.3, x[1] + 0.1, 'x', fontsize=12)  # 調整位置
plt.plot(y[0], y[1], 'o')
plt.text(y[0] + 0.1, y[1] - 0.2, 'y', fontsize=12)  # 調整位置

# 繪製超平面 H
x_h = np.array([y[0] - b, y[0] + b])
y_h = np.array([y[1] + a, y[1] - a])
plt.plot(x_h, y_h, '--')


# 繪製點 z，並標記在旁邊，避免重疊
z = np.array([y[0] - b / 2, y[1] + a / 2])
plt.plot(z[0], z[1], 'o')
plt.text(z[0] + 0.1, z[1] + 0.1, 'z', fontsize=12)  # 調整位置

# 繪製線段 xz
plt.plot([x[0], z[0]], [x[1], z[1]], '-')

# 繪製 "充分接近 x 的點"，並標記在旁邊，避免重疊
t = 0.2
x_near = x + t * (z - x)
plt.plot(x_near[0], x_near[1], 'o')
plt.text(x_near[0] - 0.3, x_near[1] - 0.2, 'near x', fontsize=12)  # 調整位置

# 繪製線段 xy
plt.plot([x[0], y[0]], [x[1], y[1]], '-')
plt.text((x[0] + y[0]) / 2 + 0.1, (x[1] + y[1]) / 2 + 0.1, 'xy', fontsize=12)  # 調整位置

# 繪製超平面 H 的標記，避免重疊
plt.text(x_h[1] + 0.2, y_h[1] - 0.1, 'H', fontsize=12)  # 調整位置


# 設定圖形標題和坐標軸標籤
plt.title('Hyperplane and Points')
plt.xlabel('x')
plt.ylabel('y')

# 調整坐標軸範圍，使得圖形更美觀
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# 顯示圖形
plt.grid()
plt.show()
```
{% endtab %}
{% endtabs %}

## 可接近性集合定理(存在性與充分條件)

> 定義矩陣$$\overline{M} \in \mathbb{R}^{r \times s \times N}$$，其第$$i,j$$個元素$$\overline{m}(i,j) \in \mathbb{R}^N$$為機率分佈$$m(i,j)$$的平均值。
>
> 對於$$\mathbf{P}$$中的任意分佈$$\mathbf{p}=(p_1,\dots,p_r), ~\sum_{i=1}^r p_i=1$$，定義$$\mathcal{R}(p)$$為$$s$$個點$$\sum_{i} p_{i=1}^r p_i \overline{m}(i,j), ~j=1,2,\dots,s$$形成的凸包(convex hull)，則可接近集合的充分條件如下：
>
> 令$$S$$為任意閉集合，若對於任意向量(點)$$x \notin S$$存在混合策略$$p(x) \in \mathbf{P}$$滿足$$y = \argmin d(x,S)$$為集合$$S$$中距離$$x$$最近點，存在超平面$$H$$經過$$y$$，$$H$$正交於線段$$xy$$且$$H$$將$$x$$與閉包$$\mathcal{R}(\mathbf{p})$$分為相異兩閱，則$$S$$為策略$$f:f_n$$的可接近集合，其中：
>
> $$f_n = \begin{cases} p(\overline{x}_n),& \text{ if } n > 0 \text { and } \overline{x}_n =(\frac{1}{n} \sum_{i=1}^n x_i) \notin S, \\ \text{ arbitrary,} & \text{ if } n = 0 \text{ or } \overline{x}_n \in S.  \end{cases}$$

<mark style="color:red;">註：因為只有假設</mark>$$S$$<mark style="color:red;">為閉集合，因此</mark>$$S$$<mark style="color:red;">中距離</mark>$$x$$<mark style="color:red;">最近的點</mark>$$y$$<mark style="color:red;">不唯一</mark>。

想像你在玩一個遊戲，每次你離目標的距離（ $$\delta_n$$ ​ ）都有機會變小一點點（因為期望值減小），而且你不能跳太遠（變化有限）。雖然有時可能因為隨機性稍微偏離，但整體趨勢是越來越靠近目標。證明就像在說：只要你玩夠多次，距離幾乎一定會變得很小，偏離的機會微乎其微。

<details>

<summary>proof: 目標是證明平均報酬至集合的距離收斂至0，此處只證明到距離依賴於常數a(距離的上限值), b(兩次距離差值的上限),c(報酬集合X的大小)，還需要lemma</summary>

假設玩家使用滿足以上條件的策略，對手使用任意策略$$g$$，且$$x_1,x_2,\dots$$為已觀測到的報酬，令$$\overline{x}_n=(\frac{1}{n} \sum_{i=1}^n x_i) \notin S$$。

令$$y_n$$為集合$$S$$中距離$$\overline{x}_n$$最近的點(不唯一)，且$$u_n = y_n - \overline{x}_n$$(由$$\overline{x}_n$$為起點，往$$y_n$$方向的向量)，則$$\forall \overline{x}_n \notin S$$，可得$$\mathrm{E}(\langle u_n, x_{n+1} \rangle ~|~ x_1, \dots, x_n) \geq \langle u_n, y_n \rangle$$--(1)

因為$$u_n = y_n - \overline{x}_n$$表示由$$\overline{x}_n$$出發，往$$y_n$$方向的向量，垂直於超平面$$H$$，而通過$$y_n$$的超平面$$H=\{z \in \mathbb{R}^N ~|~ \langle z-y_n, u_n \rangle  =0 \}$$。

因為假設$$\mathrm{E}(x_{n+1} |x_1, \dots, x_n) \in R(p)$$且$$R(p)$$必落在以$$H$$為界與$$x$$相異的兩側，即$$R(p) \in H^{(H)} =\{z \in \mathbb{R}^N ~|~ \langle z-y_n, u_n \rangle   \geq 0 \}$$

代入期望值得下式，注意只有$$x_{n+1}$$為隨機變數，$$y_n, u_n$$為定值，取期望值等於原值：

$$\begin{aligned} &\mathrm{E}(\langle x_{n+1}-y_n, u_n \rangle |x_1, \dots, x_n )   \geq 0 \\ &\mathrm{E}(\langle x_{n+1}, u_n \rangle |x_1, \dots, x_n ) - \mathrm{E}(\langle y_n, u_n \rangle |x_1, \dots, x_n )  \geq 0 \\ &\mathrm{E}(\langle x_{n+1}, u_n \rangle |x_1, \dots, x_n ) - \langle y_n, u_n \rangle  \geq 0 \\  & \mathrm{E}(\langle x_{n+1}, u_n \rangle |x_1, \dots, x_n )  \geq  \langle y_n, u_n \rangle  \end{aligned}$$

移項得$$\mathrm{E}(\langle x_{n+1} - y_n, u_n \rangle |x_1, \dots, x_n ) = \mathrm{E}(\langle u_n, x_{n+1} - y_n  \rangle |x_1, \dots, x_n )  \geq  0$$--(1)

也可解釋為$$\mathrm{E}(x_{n+1} |x_1, \dots, x_n) \in R(p$$)在向量$$u_n$$上的正交投影長度大於等於$$y_n$$在$$u_n$$上的正交投影。

***

令$$\delta_n=|\overline{x}_n-y_n|^2$$為點$$\overline{x}_n$$至集合$$S$$的距離平方，若$$\delta_n > 0$$，則

$$\delta_{n+1} =|\overline{x}_{n+1}-y_{n+1}|^2 \leq |\overline{x}_{n+1}-y_{n}|^2$$ ---(2.1) \
(因為$$\delta_{n+1}$$是點$$\overline{x}_{n+1}$$至集合$$S$$的最短距離，集合上其它點到$$\overline{x}_{n+1}$$長度均大於等於$$\delta_{n+1}$$)。

$$\begin{aligned} |\overline{x}_{n+1}- y_n|^2 &=  |(\overline{x}_{n+1}- \overline{x}_{n}) +(\overline{x}_{n}- y_n)|^2 \\ &= |\overline{x}_{n+1}- \overline{x}_{n}|^2 + 2 \langle \overline{x}_{n+1}- \overline{x}_{n},  \overline{x}_{n}- y_n \rangle + |\overline{x}_{n}- y_n|^2 \\ & = |\overline{x}_{n+1}- \overline{x}_{n}|^2 + 2 \langle \overline{x}_{n+1}- \overline{x}_{n},  \overline{x}_{n}- y_n \rangle + \delta_n  \end{aligned}$$--(2.2)

因為$$u_n = y_n - \overline{x}_n$$

所以$$\delta_{n+1} \leq  |\overline{x}_{n+1}- \overline{x}_{n}|^2 - 2 \langle \overline{x}_{n+1}- \overline{x}_{n},  u_n \rangle + \delta_n$$--(2)

***

因為$$\overline{x}_{n+1}- \overline{x}_{n} = (x_{n+1} - \overline{x}_{n})/(n+1)$$$$\begin{aligned}  & \overline{x}_{n+1} = \frac{n}{n+1} \overline{x}_{n} + \frac{1}{n+1} x_{n+1}  \\ &\overline{x}_{n+1} - \overline{x}_{n} = -\frac{1}{n+1}  \overline{x}_{n} + \frac{1}{n+1} x_{n+1}    \\ &\overline{x}_{n+1} - \overline{x}_{n} = \frac{1}{n+1} (x_{n+1}  - \overline{x}_{n})  \end{aligned}$$--(3.1)

(3.1)代回(2)的內積部分得：$$\begin{aligned} \langle \overline{x}_{n}-y_n, \overline{x}_{n+1} - \overline{x}_{n} \rangle &=   \langle -u_n, \frac{1}{n+1}(x_{n+1} - \overline{x}_{n})\rangle \\ &= -\frac{1}{n+1} \langle x_{n+1} - \overline{x}_{n}, u_n \rangle \\ &= -\frac{1}{n+1} \langle x_{n+1} -y_n + y_n - \overline{x}_{n}, u_n \rangle \\  &= -\frac{1}{n+1} \left( \langle x_{n+1}-y_n, u_n \rangle +  \langle y_n -\overline{x}_{n}, u_n \rangle \right)  \end{aligned}$$--(3.2)

，可得$$\langle \overline{x}_{n}-y_n, \overline{x}_{n+1} - \overline{x}_{n} \rangle =  \frac{\langle \overline{x}_{n}-y_n, {x}_{n+1} - y_n \rangle }{n+1} +   \frac{\langle \overline{x}_{n}-y_n, y_n - \overline{x}_{n} \rangle}{n+1}$$--(3)

***

因為假設$$X$$為有界集，由(3.1)得 $$|\overline{x}_{n+1}- \overline{x}_{n}|^2 \leq c/(n+1)^2$$，其中$$c$$是只依賴於集合$$X$$的大小的常數--(4)

***

由(2)與(1,3,4)，且將n改為n-1得

$$\mathrm{E}(\delta_n ~|~ \delta_1, \dots, \delta_{n-1})  \leq (1-\frac{2}{n})\delta_{n-1} + \frac{c}{n^2}, \text{ if } \delta_{n-1} >0$$ --(5)

$$\mathrm{E}(\delta_{n+1} ~|~ \delta_1, \dots, \delta_n)  \leq (1-\frac{2}{n+1})\delta_{n} + \frac{c}{(n+1)^2}, \text{ if } \delta_{n} >0$$ --(5')

方程式 (5) 的條件期望是基於$$\delta_1 ​ ,\delta_2 ​ ,\dots, \delta_{n-1}$$ ​ 而不是$$x_1 ​ ,x_2 ​ ,\dots,x_{n-1}$$ ​ ，是因為 ​ $$\delta_n=|\overline{x}_n-y_n|^2$$本身是 $$x_1 ​ ,x_2 ​ ,…,x_n$$ ​ 的函數，提供的資訊不變，所以條件期望可以簡化。

(5)的推導過程：

$$\delta_{n+1} \leq  |\overline{x}_{n+1}- \overline{x}_{n}|^2 - 2 \langle \overline{x}_{n+1}- \overline{x}_{n},  u_n \rangle + \delta_n$$--(2)

$$u_n = y_n - \overline{x}_n$$

$$\delta_n=|\overline{x}_n-y_n|^2= \langle u_n, u_n \rangle$$

$$|\overline{x}_{n+1}- \overline{x}_{n}|^2 \leq c/(n+1)^2$$--(4)

$$\langle  \overline{x}_{n+1} - \overline{x}_{n}, u_n \rangle =       \frac{1}{n+1} \left( \langle x_{n+1}-y_n, u_n \rangle +  \langle y_n -\overline{x}_{n}, u_n \rangle \right)$$

* $$\mathrm{E}(\langle x_{n+1} - y_n, u_n \rangle |\delta_1, \dots, \delta_n ) \geq 0$$

- 而$$\langle y_n - \overline{x}_n, u_n \rangle =  \langle u_n, u_n \rangle =\delta_n \geq  0$$

所以$$\begin{aligned}  & \mathrm{E}(\langle  \overline{x}_{n+1} - \overline{x}_{n}, u_n \rangle ~|~ \delta_1, \dots, \delta_n)  \\  &=         \frac{1}{n+1}  \mathrm{E}   \left(    \langle x_{n+1}-y_n, u_n \rangle + \delta_n    ~|~ \delta_1, \dots, \delta_n  \right)    \\  &=         \frac{1}{n+1}  \mathrm{E}   \left(    \langle x_{n+1}-y_n, u_n \rangle    ~|~ \delta_1, \dots, \delta_n  \right)  + \delta_n  \\  & \geq   \frac{1}{n+1}    \delta_n  \\    \end{aligned}$$--(5.1)

(5.1, 4)代回(2)後，取期望值得：

$$\begin{aligned} &\mathrm{E} \left( \delta_{n+1} ~|~ \delta_{1:n} \right) \\ & \leq   \mathrm{E} \left( \frac{c}{(n+1)^2}  ~|~ \delta_{1:n} \right)   - \mathrm{E} \left( 2 \langle \overline{x}_{n+1}- \overline{x}_{n},  u_n \rangle  ~|~ \delta_{1:n} \right)  + \mathrm{E} \left( \delta_n ~|~ \delta_{1:n}\right) \\ & \leq   \frac{c}{(n+1)^2} - \frac{2}{n+1}\delta_n + \delta_n \\ & =  \frac{c}{(n+1)^2} +(1-  \frac{2}{n+1} )\delta_n     \end{aligned}$$--(5)

***

且$$0 \leq \delta_n \leq a$$--(6)

方程式 (6) 是基於集合 X 的有界性和距離的非負性得出的結論。

這個不等式說明了$$\delta_n​=|\overline{x}_n - y_n|^2$$（即點$$\overline{x}_n​$$到集合$$S$$的距離的平方）是有界的。由於$$\delta_n​$$是距離的平方，它自然是非負的。上界$$a$$的存在是因為在賽局過程中，所有可能的點$$x_n$$都位於一個有界閉集$$X$$內，因此從任意點$$x_n$$到集合$$S$$的距離都是有限的，其平方同樣也是有限的。這表明無論賽局進行多少輪，$$x_n$$到$$S$$的距離都不會無限增大。

***

與$$|\delta_n - \delta_{n-1}| \leq \frac{b}{n}$$--(7)

此不等式則提供了相鄰兩次賽局之間$$\delta_n$$變化量的一個界限。

從方程式 (2) 和 (4) 的推導中可以看出，$$\delta_n$$ 的變化受到$$x_n$$ ​ 和$$x_{n+1}$$ ​的影響，而$$x_n$$ ​ 的變化是有界的（因為 $$X$$ 是有界的）。因此，$$\delta_n$$ ​ 的變化也必然受到限制。

考慮到每次決策後，新點$$x_{n+1}$$的選擇基於分佈$$m(i,j)$$，且該分佈定義在一個有界閉集$$X$$上，這意味著從$$x_n$$到$$x_{n+1}$$的變化不會過於劇烈。

更具體地說，隨著遊戲輪次$$n$$的增加，每次更新帶來的距離變化會逐漸減小。這是因為每一步移動的影響被分攤到了越來越大的$$n$$上，導致了$$∣\delta_n-\delta_{n-1}​∣$$與$$n$$成反比的關係。

只要再證明(5,6,7)中，給定a,b,c時，$$\delta_n$$可機率收斂至0(如以下lemma)。

</details>

### Lemma

> 隨機序列$$\delta_1, \delta_2, \dots,$$若滿足：
>
> * $$\mathrm{E}(\delta_n | \delta_1, \dots, \delta_{n-1}) \leq (1-\frac{2}{n})\delta_{n-1} + \frac{c}{n^2}, \text{ if } \delta_{n-1} >0$$，這表示每一步的「平均距離」會比前一步稍微減小一點，但會加上一個很小的正數$$c/n^2$$。
> * $$0 \leq \delta_n \leq a$$：距離不會是負的，也不會無限大，有一個上限a，避免劇烈跳動。。
> * $$|\delta_n - \delta_{n-1}| \leq \frac{b}{n}$$：這表示每一步的變化不會太大，隨著$$n$$增加，變化越來越小，避免劇烈跳動。
>
> 則只依賴於a,b,c的速率，以機率1收斂至0。
>
> 即$$\forall \epsilon >0, \exists n_0(a,b,c,\epsilon ) \in \mathbb{N} \ni$$ $$\forall \{\delta_n \}$$滿足以上三個條件時，可得機率收斂：$$\mathrm{P}(\delta_n \geq \epsilon \text{ for some } n \geq n_0 ) <\epsilon$$。
>
> 引理的目標是證明：隨機序列$$\delta_n$$ ​（例如平均點到集合$$S$$的距離平方）的收斂性。
>
> 對於任何小的正數$$\epsilon>0$$ ，我們可以找到一個足夠大的步數$$n_0$$ ​ （只取決於 𝜀 , 𝑎 , 𝑏 , 𝑐），使得在$$n \geq n_0$$​ 之後， $$\delta_n$$ ​ 超過$$\epsilon$$的機率非常小（小於 $$\epsilon$$）。這意味著 $$\delta_n$$ ​ 會穩定地變得很小(會以某種速度趨近於 0，而且這種趨近是「幾乎確定」的（機率為 1）)。

<details>

<summary>proof：主要分析<span class="math">\delta_n</span> 逼近於0後，如果有<span class="math">x_{n+1}</span>突然變大造成<span class="math">\delta_n</span>遠離0時的波動行為</summary>

令 $$n_0$$任意整數。要證明存在$$n_1 > n_0$$只依賴資$$n_0, \epsilon, a,c$$滿足$$\mathrm{P}(\delta_n \geq \epsilon/2 \text{ for } n_0 \leq n \leq n_1 ) < \epsilon/2$$。

#### <mark style="color:red;">構造輔助序列an分析逐漸收斂的行為</mark>

為了分析方便，定義了一個新序列 $$a_n$$ ​：將$$\delta_n$$ 從$$n_0$$開始(之前設為0)截斷為非負序列，並在$$\delta_n$$ 首次降為 0 後保持為 0。

$$a_n=\begin{cases}  &\delta_n,  ~\forall n \geq n_0 \text{ if } \delta_i > 0, ~\forall n_0 \leq i \leq n, \\  &0, \text{ otherwise }  \end{cases}$$

&#x20;因此$$a_n < \epsilon/2$$可得$$\delta_i < \epsilon /2$$，for some $$i, ~ n_0 \leq i \leq n$$。

這是在模擬「距離一直保持正的情況」，如果$$a_n$$變小，$$\delta_n$$也會變小。

由條件$$0 \leq \delta_n \leq a$$知$$a_{ n_0} \leq a$$且 $$\forall >n_0$$由條件1得

$$\mathrm{E}(a_n|a_{n_0}, \dots, a_{n-1}) \leq (1-\frac{2}{n})a_{n-1}+\frac{c}{n^2}$$。

使用重複期望值定理(Law of Total Expectation)

* 左側：$$\mathrm{E}(\mathrm{E}(a_n|a_{n_0}, \dots, a_{n-1}))=\mathrm{E}(a_n)$$
* 右側：$$\mathrm{E}((1-\frac{2}{n})a_{n-1}+\frac{c}{n^2})=(1-\frac{2}{n})\mathrm{E}(a_{n-1})+\frac{c}{n^2}$$
* 整理得$$\mathrm{E}(a_n) \leq (1-\frac{2}{n})\mathrm{E}(a_{n-1})+\frac{c}{n^2}$$

因為$$(1-\frac{2}{n})<1$$，每次期望值都會縮減一點，雖然有$$\frac{c}{n^2}$$的小增量，但隨著$$n$$ 變大，這個增量平方衰退變得微不足道。

這表示$$\mathrm{E}(a_n ​ )$$ 會隨著$$𝑛$$增加而趨近於 0（速度取決於$$n_0,𝑎 , 𝑐$$）。

#### 找到一個範圍 $$𝑛_0$$ ​ 到 $$𝑛_1$$ ​

選一個起始點$$n_0$$，然後再找一個$$n_1 > n_0$$使得在$$n_0, n_1$$之間，$$a_n \geq \epsilon /2$$的機率小於$$\epsilon/2$$。

這是因為$$\mathrm{𝐸} (a_n ​)$$ 會逐漸變小，當期望值夠小時， $$a_n \geq \epsilon/2$$ ​ 大於的機率也會很小。

即$$\mathrm{P}(a_{n_1}<\epsilon/2) > 1- \epsilon/2$$。

#### <mark style="color:red;">構造輔助序列z\_nk分析「突然變大」的可能性</mark>

現在考慮一種情況：如果$$\delta_n$$在某個點突然從小於$$\epsilon/2$$跳到大於$$\epsilon$$。

$$\forall n,k, ~n \leq k$$定義了另一個變數$$𝑧_{𝑛 𝑘}$$ ​ ，來追蹤這種「跳躍」的行為，並計算它變大的機率。

</details>

通過計算差值$$b_k=z_{nk}-z_{nk-1}$$，並利用條件（公式5 和 7），發現這種跳躍的期望值是負的（傾向於減小），而且變化有限。

#### 應用強大數定律（Theorem 2）

作者引用了自己之前證明的一個定律（Theorem 2），說的是：如果一個隨機變數序列的期望值每次都稍微減小一點，它最終不太可能累積到很大的值。

用這個定律，證明$$𝑧_{𝑛 𝑘}$$ ​ 超過$$\epsilon$$的機率會隨著$$n$$增加而變得非常小（呈指數衰減）。

把所有可能的情況加起來（例如$$\delta_n$$ ​ 一直大於 $$\epsilon/2$$ 或突然跳到$$\epsilon$$），總機率還是可以控制在小於$$\epsilon$$。

選一個夠大的$$n_0$$ ​ ，就能保證 $$\delta_n \geq \epsilon$$ 的機率小於$$\epsilon$$ 。

(QED)

### Theorem 2: 滿足條件的隨機變數序列機率收斂

> 假設有一個隨機變數序列 $$z_1 ​ ,z_2 ​ ,\dots$$滿足以下條件：
>
> 1. 範圍限制：每個$$|z_k| \leq 1$$，（變數的大小被限制在 $$[ − 1 , 1 ]$$內）。
> 2. 期望條件：對於每個$$k$$，條件期望滿足：$$\mathrm{E}(z_k ~|~ z_1, \dots, z_{k-1}) \leq -u \max(|z_k|~|~z_1, \dots, z_{k-1})$$，其中$$u>0$$為固定的正數。\
>    註：在給定歷史$$z_1 , … , z_{k − 1}$$下，$$z_k$$的條件期望不僅為負，且與歷史最大值成比例（比例為 $$−u$$）.&#x20;
>
> 則：
>
> $$\forall t \in \mathbb{R}$$，這個序列的累積和$$z_1+ \dots+z_k$$超過$$t$$的機率有上限：
>
> $$\mathrm{P}(z_1+\dots+z_k \geq t \text{ for some }k) \leq \left( \frac{1-u}{1+u} \right)^t$$\
> 註：部分和超過$$t$$ 的機率隨$$t$$指數衰減，速率由$$\frac{1-u}{1+u}$$控制。

這個定理說的是：如果一個隨機變數序列的每一步期望值都傾向於「往下拉」（負的方向），而且這種拉力與之前最大的變數大小成正比，那麼這個序列的累積和不太可能變得很大。

具體來說，累積和超過某個值$$𝑡$$的機率會隨著$$𝑡$$增加而快速減小（呈指數衰減）。這裡的$$\frac{1 - 𝑢}{1+u}$$ ​ 是一個小於 1 的數，所以當$$𝑡$$很大時，機率變得非常小。

<details>

<summary>proof</summary>

為了利用條件期望的負偏倚，定義一個指數形式的隨機變數$$M_k= \prod_{i=1}^k (1+\lambda z_i)$$

</details>

## 向量報酬策略賽局(Spinat, 2002)

> $$N$$人向量報酬賽局$$\Gamma_{v}=(\mathcal{N}, (\mathcal{A}_i)_{ i \in \mathcal{N} }, (u_i)_{i \in \mathcal{N}})$$
>
> * $$\mathcal{N}$$為編號1到$$N$$的玩家集合。
> * $$\mathcal{A}_i$$為編號$$i$$​玩家的有限行動集合。
> * $$u_i: \prod_{i \in \mathcal{N}} \mathcal{A}_i \rightarrow \mathbb{R}^v$$為$$v$$​為的向量報酬函數。
>
> $$v=1$$時為傳統的賽局，以下考慮$$2 \leq v < \infty$$的賽局。

以下定義向量空間的操作與集合：

* $$\| x\|^2 = x^{\top} x$$為歐式空間的標準範數(standard norm)。
* $$d(x, \mathbb{S})=\inf_{y \in \mathbb{S}}d(x,y)$$為點$$x$$到集合$$\mathbb{S}$$的距離。
  * 如果$$\mathbb{S}$$為凸集合時，則點$$y$$唯一，即$$\mathbb{S}$$中其它的點到點$$x$$的距離均大於點$$y$$至$$x$$的距離。
* 令$$\mathcal{U}$$為所有向量報酬$$u(a_1, a_2) \in \mathbb{R}^v, ~\forall a_1 \in \mathcal{A}_1, ~ a_2 \in \mathcal{A}_2$$形成的凸包(convex hull)。
* 令$$\mathbf{U}$$$$\in \mathbb{R}^{|\mathcal{A}_1| \times |\mathcal{A}_2| \times v}$$為向量報酬矩陣。
* $$\displaystyle \Delta(\mathcal{A}_i) =\left\{ \mathbf{s}_i \in \mathbb{R}_+^{|\mathcal{A_i}|} ~\bigg| ~\sum_{p=1}^{|\mathcal{A_i}|} \mathbf{s}_i[a_p]=1 \right\}$$為第$$i$$個玩家的混合策略集合。其中$$s_i[a_p]$$為玩家$$i$$採取行動$$a_p$$的機率。
* $$\mathcal{R}(s_1) = \left\{   \mathrm{conv}(s_1^\top \mathbf{U}  s_2) ~ |~ \forall s_2 \in \Delta(\mathcal{A}_2) \right\}$$為給定玩家的混合策略$$s_1$$​後，對手所有可能的混合策略報酬形成的凸包。
* 同理$$\mathcal{S}(s_2) = \left\{   \mathrm{conv}(s_1^\top \mathbf{U}  s_2) ~ |~ \forall s_1 \in \Delta(\mathcal{A}_1) \right\}$$為給定對手的混合策略$$s_2$$​，玩家所有的混合策略報酬形成的凸包。

### 可接近集合(approachable set)

> 雙人零和重複賽局$$\Gamma_v$$​中，集合$$S$$​滿足以下條件時，稱為可接近集合。
>
> * $$\begin{aligned} & \exists s_{1,t} \in \Delta(\mathcal{A}_1)~ \forall \epsilon > 0~ \forall \delta >0 ~ \exists t_0 \in   \mathbb{N} \ni \\  & \forall s_{2,t} \in \Delta(\mathcal{A}_2), \mathrm{P}(\sup_{t \geq t_0} d(\overline{u}_t, S) \geq \epsilon) \leq \delta  \end{aligned}$$
> * $$\overline{u}_t\equiv \overline{u_1(a_t)} = \frac{1}{t} \sum_{\tau=1}^t u_1(a_\tau)$$為玩家到時間$$t$$​的平均報酬。

此定義即玩家存在混合策略$$s_{1,t} \in \Delta(\mathcal{A}_1)$$使得不論對手使用任意策略$$s_{2,t} \in \Delta(\mathcal{A}_2)$$，玩家的平均報酬$$\overline{u}_t$$與集合$$S$$的距離在$$t \rightarrow \infty$$時幾乎確定為０，即$$\displaystyle \lim_{t \rightarrow \infty } d (\overline{u}_t, S) =0 ~ \text{ a.s. }$$。

<mark style="color:red;">由於玩家存在有上述性質的策略，因此當玩家使用此種策略時，最後與平均報酬距離為0的集合稱為可接近集合</mark>。

* 由定義可知，任何可接近集合的超集合也是可接近集合。
* 因為所有的報酬的平均值必定落在凸包$$\mathcal{U}$$​內，因此$$\mathcal{U}$$​為可接近集合。
* 由上述定義可定義可接近閉集合$$S \subseteq \mathcal{U}$$。

可接近定理可用幾何方式說明。令$$x,y \in \mathbb{R}^v$$為相異的兩點：

通過點$$y$$的超平面(hyperplane)為$$H_{xy} =\{z \in \mathbb{R}^v ~|~ w^\top z =c , ~ w=x-y \}$$。$$w=x-y$$為其法向量

可定義兩個半空間(half-spaces)

* &#x20;$$H_{xy}^{(H)} =\{z \in \mathbb{R}^v ~|~ w^\top z \geq c  \}$$
* $$H_{xy}^{(L)} =\{z \in \mathbb{R}^v ~|~ w^\top z \leq c  \}$$

定義$$x \in S^c$$，而點$$x$$投影到集合$$S$$的點為最近的點，即$$\mathrm{proj}_S(x) = \{y \in S ~|~ d(x,y) = d(x,S) \}$$。因為$$S$$​為閉集合，因此$$\mathrm{proj}_S(x)\neq \empty$$。

當$$S$$​為凸集合時，$$\mathrm{proj}_S(x)$$為唯一的點，令$$\mathrm{proj}_S(x)=y \in S, ~ \forall x \in S^c$$。

#### 定義：B-set

> 閉集合$$S$$​滿足以下Blackwell條件時，稱為B-set。
>
> $$\forall x \in S^c$$, $$\exists s_1 \in \Delta(\mathcal{A}_1)$$, $$\exists y \in \mathrm{proj}_S(x)$$ $$\ni$$$$H_{xy}$$ 可分隔點$$x$$與凸包$$\mathcal{R}(s_1)$$。
>
> 不失一般性，令$$x \in H_{xy}^{(H)}$$且$$\mathcal{R}(s_1) \subseteq H_{xy}^{(L)}$$.&#x20;
>
> 注意：$$S$$不必為凸集合。

![B-set為非凸集合的範例](../.gitbook/assets/b-set-min.png)

#### 定義：適應性策略(adaptive strategy)

> 給定B-set $$S$$，稱函數$$\phi: S^c \rightarrow \Delta(\mathcal{A}_1)$$為集合$$S$$的適應性策略若滿足 $$\forall x \in S^c$$, $$\exists y \in \mathrm{proj}_S(x) \ni  H_{xy}$$分離點$$x$$與凸包$$\mathcal{R}(\phi(x))$$。

### Blackwell可接近定理(approachability theorem, BAT)

> 1. 令$$S$$為閉集合。若$$S$$為​B-set，則$$S$$​為可接近集合。
> 2. 令$$S$$為閉凸集合。$$S$$為B-set，若且唯若$$S$$為可接近集合。
> 3. 令$$S$$為閉凸集合。若對於對手的任意策略$$s_2 \in \Delta(\mathcal{A}_2)$$​，玩家均存在對應的混合策略$$s_1(s_2) \in \Delta(\mathcal{A}_2)$$使得報酬$$u(s_1(s_2), s_2) \in S$$，則$$S$$為可接近集合。

proof (1,2的充分條件)：

Blackwell在論文中直接建立了適應性策略可接近B-set。

* 因為$$S$$為閉集合，且為B-set，下面演算法中，因為點$$\overline{u}_t$$和集合$$S$$的距離大於$$\epsilon$$，因此$$\overline{u}_t \in S^c$$。
* 因為$$S$$為B-set，$$\overline{u}_t \in S^c$$由定義得存在$$s_1^* \in \Delta(\mathcal{A}_1)$$且存在$$y_t \in \mathrm{proj}_S(\overline{u}_t)$$使得超平面$$H_{\overline{u}_t y_t}$$可分隔點$$\overline{u}_t$$與凸包$$\mathcal{R}(s_1^*)$$。
* 令$$s_{1,t+1} \equiv s_1^*$$必可使$$\overline{u}_{t+1}$$越來越接近$$S$$，即$$d(\overline{u}_t, S) \geq d(\overline{u}_{t+1}, S)$$。 (QED)

![Blackwell適應性策略演算法](../.gitbook/assets/blackwell_adaptive_strategy-min.png)

proof 2的必要條件：

因為$$S$$​為凸集合，因此任意點$$\overline{u}_t \in S^c$$投影至集合$$S$$​必為唯一一點，令$$y_t = \mathrm{proj}_S(\overline{u}_t)$$。

令方向向量$$w_t=\overline{u}_t-y_t$$，則通過點$$y_t$$且以$$w_t$$為法向量的超平面為$$H_{\overline{u}_t y_t} = \{ z \in \mathbb{R}^v ~|~ w_t^\top z = c \}$$。

因為$$S$$​為閉凸集合，根據supporting hyperplane theorem，集合$$S$$​必定為$$H_{\overline{u}_t y_t}$$形成的半空間的子集合，且$$\overline{u}_t$$必定落在與$$S$$相異的另一半空間。即$$S \subseteq  H_{\overline{u}_t y_t}^{(L)}$$且$$\overline{u}_t \in H_{\overline{u}_t y_t}^{(H)}$$。

對於可接近集合$$S$$​, 由定義得存在混合策略 $$s_{1,t}^{*} \in \Delta(\mathcal{A}_1)$$使得$$\displaystyle \forall s_{t,2} \in \Delta(\mathcal{A}_2), ~ \lim_{t\rightarrow \infty} d(\overline{u}_t, S) = 0$$ a.s.。

若凸包$$\mathcal{R}(s_{1,t}^{*}) \cap H_{\overline{u}_t y_t }^{(H)} \neq \empty$$，表示對手存在特定的混合策略$$s_{t,2}^{*}$$使得獎勵$$u(s_{1,t}^{*}, s_{2,t}^{*}) \in \mathcal{R}(s_{1,t}^{*}) \cap H_{\overline{u}_t y_t }^{(H)}$$，此時若對手持續使用此特定策略時，則$$\overline{u}_t$$無法接近集合$$S$$，與$$S$$為可接近的集合假設矛盾，因此可得$$\mathcal{R}(s_{1,t}^{*}) \in  H_{\overline{u}_t y_t }^{(L)}$$。

由於$$\overline{u}_t \in H_{\overline{u}_t y_t }^{(H)}$$，可得$$S$$為B-set (QED).&#x20;

proof 3:

令閉凸集合$$S$$位於半空間$$H^{(L)} = \{ x \in \mathbb{R}^v ~|~ w^\top x \leq c\}$$。

由給定的條件知 $$\forall s_2 \in \Delta(\mathcal{A}_2) \exists s_1(s_2) \in \Delta(\mathcal(A)_1) \ni u(s_1(s_2), s_2) \in S \subseteq H^{(L)}$$，即$$w^\top u(s_1(s_2), s_2) \leq c$$。

由純量版本的最大最小定理，可得$$\exists s_1^* \in \Delta(\mathcal{A}_1) \ni \forall s_2 \in \Delta(\mathcal{A}_2) , ~ w^\top u(s_1^{*}, u_2) \leq c$$，即凸包 $$\mathcal{R}(s_1^{*}) \subseteq H^{(L)}$$，此結論在任包含$$S$$的半空間$$H^{(L)}$$均成立。

令$$\overline{u}_t \in S^c$$，且$$S$$為凸集合，因此可得唯一投影點$$y_t = \mathrm{proj}_{S}(\overline{u}_t)$$。

使用Blackwell adaptive strategy，可得超平面$$H_{\overline{u}_t y_t} =\{   x \in \mathbb{R}^v ~|~ w_t^\top x = c \}$$，得對應的半空間$$S \subseteq H_{\overline{u}_t y_t}^{(L)}$$且$$\mathcal{R}(s_1^{*}) \subseteq H_{\overline{u}_t y_t}^{(L)}$$。

由上性質可得若玩家總是選擇混合策略$$s_{1,t+1}=s_1^{*}$$，則$$\mathcal{R}(s_{1,t+1)}) \subseteq H_{\overline{u}_t y_t}^{(L)}$$，因為$$\overline{u}_t \subseteq H_{\overline{u}_t y_t}^{(H)}$$，所以$$S$$為B-set。(QED)

![使用Blackwell adaptive strategy接近凸集合](../.gitbook/assets/b-set_approachable-min.png)

## Blackwell adaptive strategy收斂性分析

> Blackwell adaptive strategy(BAS)的收斂速率為$$O(\sqrt{\frac{1}{T}})$$

令$$y_t = \mathrm{proj}_S(\overline{u}_t)$$，使用BAS可得：

$$\displaystyle \begin{aligned} d(\overline{u}_{t+1}, S)^2 & \leq d(\overline{u}_{t+1}, y_t)^2 \\     & = \| \frac{t}{t+1}\overline{u}_t + \frac{1}{t+1}u(s_{1,t+1}, s_{2, t+1}) - y_t  \|^2 \\     & = \left(\frac{t}{t+1} \right)^2 \| \overline{u}_t - y_t\|^2 + \\     & \left(\frac{t}{t+1}\right)^2 \| u(s_{1,t+1}, s_{2, t+1}) - y_t \|^2 + \\     & \left(\frac{2t}{(t+1)^2} \right) (u_t - y_t)^\top (u(s_{1,t+1}, s_{2, t+1}) - y_t)  \end{aligned}$$

上式不等式成立是因為三角不等式；因為$$\overline{u}_t$$投影到集合$$S$$的距離，不大於其它在$$S$$上點$$y_t$$的距離。

因為$$\overline{u}_t$$與$$u(s_{1,t+1}, s_{2, t+1})$$位於超平面$$H_{\overline{u}_t y_t}$$的相異半空間，則方向向量$$\overline{u}_t -y_t$$與$$u(s_{1,t+1}, s_{2, t+1}) - y_t$$的夾角不小於$$\pi/2$$。

由歐式空間的標準內積$$x^\top y =\|x\| \|y\| \cos \theta$$且$$\theta > \pi/2$$可知上述不等式最後一行為負值。

因為$$d(\overline{u}_{t}, S) = d(\overline{u}_{t}, y_t)$$，不等式可改寫為：$$(t+1)^2 d(\overline{u}_{t}, S)^2 \leq t^2 d(\overline{u}_{t}, S)^2 + \|u(s_{1,t+1}, s_{2, t+1})- y_t\|^2$$

不失一般性，令$$S$$為單位圓的子集合，則$$\|u(s_{1,t+1}, s_{2, t+1})- y_t\|^2 = O(1)$$。

重複處理上式可得$$\begin{aligned} & T^2 d(\overline{u}_{T}, S)^2 \leq d(\overline{u}_{1}, S)^2 + O(T) \\ & \Rightarrow d(\overline{u}_{T}, S)^2 \leq O(\sqrt{\frac{1}{T}}) \end{aligned}$$(QED)

## 參考資料

* \[原始論文] David Blackwell, "[An analog of the minimax-theorem for vector payoffs](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-6/issue-1/An-analog-of-the-minimax-theorem-for-vector-payoffs/pjm/1103044235.pdf), " Pacific Journal of Mathematics, Vol. 6.1 pp. 1-8, 1956.
* <mark style="background-color:red;">Hannan, James. "Approximation to Bayes risk in repeated play." Contributions to the Theory of Games 3.2 (1957): 97-139</mark>.
* Jacob Abernethy, Peter L. Bartlett, and Elad Hazan, "Blackwell approachability and no-regret learning are equivalent," Proceedings of the 24th Annual Conference on Learning Theory. JMLR Workshop and Conference Proceedings, 2011.
* \[可接近定理幾何性質] Xavier Spinat, "A necessary and sufficient condition for approachability." Mathematics of operations research, Vol. 27, No. 1, pp. 31-44, 2002.
* \[wiki][https://en.wikipedia.org/wiki/Minimax\_theorem](https://en.wikipedia.org/wiki/Minimax_theorem)[\[wiki\] Minimax theorem](https://en.wikipedia.org/wiki/Minimax_theorem)
