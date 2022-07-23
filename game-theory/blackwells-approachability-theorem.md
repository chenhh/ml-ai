---
description: 可接近性理論
---

# Blackwell's Approachability Theorem

## 簡介

對抗性預測的歷史始於數學家David Blackwell和James Hannan的開創性工作。接近性理論起源於Blackwell的工作，並與Hannan的工作同時被發現。 幾十年來，人們對一般凸賽局中的遺憾最小化和Blackwell可接近性之間的關係並不完全瞭解。通常的想法是，事實上，Blackwell可接近性是一個更強的概念。在這一章中，<mark style="color:red;">我們表明可接近性和線上凸最佳化在強烈的意義上是等價的：兩者的演算法是等價的，而且沒有計算效率的損失</mark>。

有時更自然的是，賽局的報酬函數採取向量的形式，其元素代表不同的目標值，如利潤、風險等。具有不相同標準的賽局被稱為多標準賽局或具有向量報酬函數的賽局。單一目標最佳化問題的最優解，即最大解或最小解，是在實數上，因此很容易找出來。這一重要特徵對於確定向量最佳化問題的最優解是無效的，主要是因為向量空間中的次序一般是部分次序(partial order)而不是全序(total order)。因此Von-Neumann的最大最小化定理不能直接適用於向量報酬賽局。

Blackwell\[首次研究了具有向量報酬函數的零和賽局，他提供了兩人零和重覆賽局的可接近性定理。Shapley和Rigby介紹了向量賽局的均衡點的概念，他們提到賽局的報酬函數大多是向量值函數的形式。

<mark style="color:red;">內部或外部遺憾最小化問題的一個共同特點是，它們可以被寫成某些向量報酬賽局中精心選擇的目標集的可接近性的一個具體案例</mark>。

## Minmax理論

> 給定雙人賽局，玩家1,2的行動集合分別有$$r,s$$個行動，
>
> * 玩家1的混合策略為$$\mathbf{p}=(p_1, p_2, \dots, p_r) \in \mathbf{P}, ~p_i \geq 0, ~ \sum p_i = 1$$。
> * 玩家2的混合策略為$$\mathbf{q}=(q_1, q_2, \dots, q_s) \in \mathbf{Q}, ~q_j \geq 0, ~ \sum q_j = 1$$。
> * $$m(i,j) \in \mathbb{R}$$為玩家1,2分別採取行動$$i,j$$時，玩家1的報酬(零和遊戲，所以玩家2的報酬為$$-m(i,j)$$)。
>
> 則存在$$\mathbf{p} \in \mathbb{R}_{+}^r, ~ \mathbf{q} \in \mathbb{R}_{+}^s, ~ v \in \mathbb{R}$$ 滿足$$\sum_{i=1}^r p_i m(i, j) \geq v \geq \sum_{j=1}^s q_j m(i,j), ~ \forall i, j$$
>
> * 即玩家1存在一混合策略可保證報酬大於等於$$v$$。
> * 玩家2也存在一混合策略可保證損失不會超過$$v$$。

$$\forall \epsilon > 0$$，在多期雙人零合賽局(報酬矩陣為$$M$$), 當$$t \rightarrow \infty$$，玩家1的報酬會以機率1大於$$v-\epsilon$$，而玩家2的損失會以機率1小於$$v+\epsilon$$。

## 向量報酬

<mark style="color:blue;">單一的混合策略不能確保向量報酬位於某個給定的集合中。然而，這並不排除一個漸進的概念，如果我們允許賽局無限期地重復，並詢問是否存在一種策略來確保平均報酬向量位於某個集合中，或者至少在歐氏距離上接近它。這正是Blackwell提出的解決方案概念</mark>。

在實數中的雙人零和賽局，玩家1、2可依minmax定理逼近賽局的報酬$$v$$。<mark style="color:red;">而在向量報酬中，問題變成玩家1、2是否可逼近一個特定集合</mark>$$S$$。

現在考慮雙人向量(非零和)賽局中，$$m(i,j) \in \mathbb{R}^N$$為向量報酬的情形。報酬矩陣$$\mathbf{M}=[m(i,j)], ~1 \leq i \leq r, ~ 1 \leq j \leq s$$為$$r\times s$$的矩陣，矩陣中每個元素為$$N$$維的向量(或每個元素的實現值是$$\mathbb{R}^N$$中的一個封閉有界凸集$$X$$上之機率分佈所得出，即報酬是隨機變數)。

報酬矩陣$$\mathbf{M}$$中的$$r\times s$$個向量點，可形成$$\mathbb{R}^N$$空間中的(有界)凸包(bounded convex hull)，記為$$X \subseteq \mathbb{R}^N$$。或者說$$r\times s$$個點是閉凸集$$X$$​(不一定凸包)的元素。

玩家1使用混合策略$$f_n: (x_1, x_2, \dots, x_n) \rightarrow \mathbf{P}, ~x_i \in X$$，其中$$(x_1,x_2,\dots, x_n)$$為到第$$n$$期時已觀察到的報酬(或根據$$m(i,j)$$機率分佈的實現值)(history)。

而$$f_0$$因為沒有參考資料，所以為$$\mathbf{P}$$中的任意值，玩家1的混合策略為$$\{f_0, f_1(\mathbf{x}_1), f_2(\mathbf{x}_1, \mathbf{x}_2),f_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$。

同理玩家2的的混合策略為$$\{g_0, g_1(\mathbf{x}_1), g_2(\mathbf{x}_1, \mathbf{x}_2),g_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$

因此玩家1''



。令$$S \subseteq \mathbb{R}^N$$為任意集合。

## 向量報酬策略賽局

> $$N$$人向量報酬賽局$$\Gamma_{v}=(\mathcal{N}, (\mathcal{A}_i)_{ u \in \mathcal{N} }, (u_i)_{i \in \mathcal{N}})$$
>
> * $$\mathcal{N}$$為編號1到$$N$$的玩家集合。
> * $$\mathcal{A}_i$$為編號$$i$$​玩家的有限行動集合。
> * $$u_i: \prod_{i \in \mathcal{N}} \mathcal{A}_i \rightarrow \mathbb{R}^v$$為$$v$$​為的向量報酬函數。
>
> $$v=1$$時為傳統的賽局，以下考慮$$2 \leq v < \infty$$的賽局。

以下定義向量空間的操作與集合：

* $$\| x\|^2 = x^{\top} x$$為歐式空間的標準範數(standard norm)。
* $$d(x, \mathbb{S})=\inf_{y \in \mathbb{S}}d(x,y)$$為點$$x$$到集合$$\mathbb{S}$$的距離。
* 令$$\mathcal{U}$$為所有向量報酬$$u(a_1, a_2) \in \mathbb{R}^v, ~\forall a_1 \in \mathcal{A}_1, ~ a_2 \in \mathcal{A}_2$$形成的凸包(convex hull)。$$\mathbf{U}$$$$\in \mathbb{R}^{|\mathcal{A}_1| \times \mathcal{A}_2| \times v}$$為向量報酬矩陣。
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

![Blackwell適應性策略演算法](../.gitbook/assets/blackwell\_adaptive\_strategy-min.png)

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

![使用Blackwell adaptive strategy接近凸集合](../.gitbook/assets/b-set\_approachable-min.png)

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

* <mark style="background-color:red;">\[\*\*\*]Blackwell, David. "An analog of the minimax 一\$$theorem for vector payoffs." Pacific Journal of Mathematics 6.1 (1956): 1-8</mark>.
* <mark style="background-color:red;">Hannan, James. "Approximation to Bayes risk in repeated play." Contributions to the Theory of Games 3.2 (1957): 97-139</mark>.
* Abernethy, Jacob, Peter L. Bartlett, and Elad Hazan. "Blackwell approachability and no-regret learning are equivalent." Proceedings of the 24th Annual Conference on Learning Theory. JMLR Workshop and Conference Proceedings, 2011.
* \[可接近定理幾何性質] Spinat, Xavier. "A necessary and sufficient condition for approachability." Mathematics of operations research 27.1 (2002): 31-44.
* \[wiki][https://en.wikipedia.org/wiki/Minimax\_theorem](https://en.wikipedia.org/wiki/Minimax\_theorem)[\[wiki\] Minimax theorem](https://en.wikipedia.org/wiki/Minimax\_theorem)
