---
description: Martin Zinkevich, 2003，第一篇定義OCO的論文
---

# paper: Online convex programming and generalized infinitesimal gradient ascent

凸規劃(convex programming)包含了一個凸集合$$F \subseteq \mathbb{R}^n$$與凸成本函數$$c: F \rightarrow \mathbb{R}$$，其目標是找出極小值$$\displaystyle x^{*} =\argmin_{x \in F}c(x)$$。

在線凸規劃(online convex programming)中，凸集合$$F$$事先已知，但每一期給出決策點$$x_t$$之後，才知道當期的凸成本函數$$f_t$$形式，之後才能算出成本$$f_t(x_t)$$。

<mark style="color:red;">在本論文中，不對凸成本函數的分佈做假設，且也不對任意兩期凸成本函數的關聯性做假設</mark>。

<mark style="color:blue;">比較在線演算法性能時，是和離線(offline)演算法比較差值，越小越好(靜態遺憾，static regret)</mark>。此處離線演算法指的是已經事先知道$$f_1,\dots, f_T$$的所有的形式，離線演算法可找出點$$\displaystyle \argmin_{x \in F} \sum_{t=1}^T f_t(x)$$。此處的離線演算法是已經事先知道所有的結果才可計算得出。



> <mark style="color:red;">定義：凸集合(convex set)</mark>
>
> $$S \subset \mathbb{R}^n$$滿足以下條件時，稱為凸集合：
>
> $$\forall x,y \in S, ~ \lambda \in [0,1]~ \ni \lambda x +(1-\lambda)y \in S$$

> <mark style="color:red;">定義：凸函數(convex function)</mark>
>
> 實值函數$$f: F \rightarrow \mathbb{R}$$滿足以下條件時，稱為凸函數(開口向上, valley-shaped)：$$\forall x,y\in F, ~\lambda \in [0,1] ~\ni \lambda f(x)+(1-\lambda)f(y) \geq f(\lambda x + (1-\lambda )y)$$

> <mark style="color:red;">定義：凸規劃問題(convex programming problem)</mark>
>
> 可行解集合(feasible domain)為凸集合$$F\subseteq \mathbb{R}^n$$與凸成本函數$$c: F \rightarrow \mathbb{R}$$。
>
> 最佳解$$x = \argmin_{x \in F} c(x)$$ 必定存在，但不唯一。

> <mark style="color:red;">定義：在線凸規劃問題(online convex programming problem)</mark>
>
> 包含了可行解凸集合$$F \subseteq \mathbb{R}^n$$與無限個凸成本函數序列$$\{c_1, c_2,\dots\}$$，其中$$c_t :F \rightarrow \mathbb{R}$$均為凸函數。
>
> <mark style="color:blue;">在線凸規劃算法</mark>在時間$$t$$時，依據已實現的成本$$c_1(x_1),\dots, c_{t-1}(x_{t-1})$$決定當期的向量$$x_t \in F$$後，才可算出當期的成本$$c_t(x_t)$$。



令$$\|x\|=\sqrt{x \cdot x}$$，$$d(x,y)=\|x-y\|$$。論文的所有討論均隱含以下七個假設：

1. <mark style="color:blue;">可行解集合</mark>$$F$$<mark style="color:blue;">有界(bounded)。</mark>即存在$$N \in \mathbb{R} ~ \ni \forall x, y \in F, ~ d(x,y)\leq N$$。
2. <mark style="color:blue;">可行解集合</mark>$$F$$<mark style="color:blue;">為閉集合(closed set)，即包含所有極限點</mark>。對於所有的序列$$\{x_1, x_2,\dots\}$$，其中$$x_t \in F, \forall t$$，若存在$$x \in \mathbb{R}^n \ni \lim_{t \rightarrow \infty} x_t =x$$時，可得$$x \in F$$。
3. <mark style="color:blue;">可行解集合</mark>$$F$$<mark style="color:blue;">非空集合</mark>。即存在至少一個$$x \in F$$。
4. $$\forall t, c_t$$在$$F$$均為<mark style="color:blue;">可微分函數</mark>。
5. <mark style="color:blue;">函數梯度有界</mark>。存在$$N \in \mathbb{R}$$滿足$$\forall t , ~ \forall x \in F, ~ \| \nabla c_t(x) \| \leq N$$。
6. $$\forall t$$，給定$$x \in F$$，總是存在演算法<mark style="color:blue;">可算出梯度</mark>$$\nabla c_t(x)$$。
7. $$\forall y \in \mathbb{R}^n$$，總是存在<mark style="color:blue;">演算法可算出投影點(投影至可行解集合)</mark>$$P(y)=\argmin_{x \in F}d(x,y)$$。

## 貪婪投影演算法(greedy projection algorithm)

> 演算法：
>
> 在集合$$F$$中任意選一初始向量$$x_1$$以及學習速率序列$$\eta_1, \eta_2,  \dots \in \mathbb{R}^{+}$$。
>
> 在時間$$t$$，已知當期的成本函數$$c_t$$後，使用梯度下降法決定下一期的向量，如果超出可行解集合範圍時，投影回可行解集合中：$$x_{t+1}=P(x_t - \eta_t \nabla c_t(x_t))$$

### 性能分析

> 定義：遺憾(regret)
>
> 給定演算法$$A$$與凸規劃問題$$\{F, \{c_1,c_2,\dots \} \}$$，若演算法$$A$$給出解序列$$\{x_1,x_2, \dots \}$$，則<mark style="color:blue;">演算法</mark>$$A$$<mark style="color:blue;">至時間</mark>$$T$$<mark style="color:blue;">的成本</mark>為$$C_A(T)=\sum_{t=1}^T c_t(x_t)$$。
>
> 而一<mark style="color:blue;">靜態可行解</mark>$$x \in F$$<mark style="color:blue;">至時間</mark>$$T$$<mark style="color:blue;">的成本</mark>為$$C_x(T)=\sum_{t=1}^T c_t(x)$$。
>
> 因此<mark style="color:red;">演算法</mark>$$A$$<mark style="color:red;">至時間</mark>$$T$$<mark style="color:red;">的遺憾(regret)</mark>為$$R_A(T)=C_A(T) - C_x(T)$$。

當時間$$T$$夠長時，離線演算法的優勢變少。若成本函數相對穩定時，則在線演算法很容易學習，離最佳解不會變動太遠。而若成本函數不穩定時，離散演算法因為選固定點無法反應大幅變動的成本。

<mark style="color:red;">本論文的目標是證明greedy projection algorithm的平均遺憾可以收斂至0</mark>。

令$$\| F\|= \max_{x,y\in F}d(x,y)$$為集合的半徑。$$\displaystyle \|\nabla c\|=\max_{x \in F, ~ t\in \{1,2,\dots\}} \| \nabla c_t(x)\|$$為梯度在可行解集合以及所有時間內的最大變化量。

> theorem
>
> 若學習速度$$\eta_t = \frac{1}{\sqrt{t}}$$時，則貪婪投影演算法的遺憾為：
>
> $$R_G(T) \leq \frac{\|F\|^2 \sqrt{T}}{2} + \left( \sqrt{T} - \frac{1}{2} \right) \| \nabla c \|^2$$\
> 可得$$\displaystyle \limsup_{T \rightarrow \infty} \frac{R_G(T)}{T} \leq 0$$。

<details>

<summary>proof of greedy projection algorithm's regret bound</summary>

不失一般性，令成本函數$$c_t(x) = g_t^\top x, ~g_t \in \mathbb{R}^n$$。可得$$\nabla c_t(x_t)=g_t$$。

如果將$$c_t(x)$$全部換成$$g_t^\top x$$可得演算法的結果不變，接下來分析遺憾的部份。



因為$$c_t:F\rightarrow \mathbb{R}, ~\forall x \in F$$為凸函數，由[凸函數的一階條件](../../convex-optimization/convex-function/#yi-jie-tiao-jian-firstorder-condition)可得 $$c_t(x) \geq \nabla c_t(x_t)^\top (x-x_t)+c_t(x_t)$$。

令$$x^{*} \in F$$為靜態最佳解。可得$$c_t(x^{*}) \geq g_t^\top (x^{*}-x_t)+c_t(x_t)$$。

整理可得$$c_t(x_t) - c_t(x^{*}) \leq c_t(x_t) - (g_t^\top (x^{*} - x_t) + c_t(x_t)) \leq g_t^\top x_t - g_t^\top x^{*}$$。

因此用<mark style="color:blue;">線性函數的遺憾至少和凸函數一樣多</mark>。



$$\forall t$$，令$$y_{t+1} = x_t - \eta_t g_t$$，由演算法得$$x_{t+1} = P(y_{t+1})$$。

現在考慮在時間$$t$$時，不使用固定向量$$x^{*}$$的遺憾。

* $$y_{t+1} - x^{*} =  (x_t - x^{*}) - \eta_t g_t$$
* $$(y_{t+1} - x^{*})^2 =  (x_t - x^{*})^2 - 2 \eta_t (x_t - x^{*})^\top g_t + \eta_t^2 \|g_t\|^2$$

由於$$x_{t+1} \in F$$是$$y_{t+1} \in \mathbb{R}^n$$在$$F$$的投影點，由距離函數的三角不等式性質可得$$(y-x)^2 \geq (P(y) - x)^2$$。且由凸函數的一階條件可得$$\|g_t\| \leq \| \nabla c \|$$。

由此兩條件可得：

* $$(x_{t+1} - x^{*})^2  \leq (x_{t} - x^{*})^2 - 2 \eta_t (x_t - x^{*})^\top g_t + \eta_t^2 \|\nabla c\|^2$$
* $$(x_t - x^{*})^\top g_t \leq  \frac{1}{2 \eta_t} ((x_t - x^{*})^2 - (x_{t+1} - x^{*})^2) +  \frac{\eta_t}{2} \|  \nabla c\|^2$$

由regret定義得：

$$\displaystyle \begin{aligned} R_G(T) & = \sum_{t=1}^T (x_t - x^{*})^\top g_t \\   & \leq \sum_{t=1}^T \frac{1}{2 \eta_t} ((x_t - x^{*})^2 - (x_{t+1} - x^{*})^2)  + \frac{\eta_t}{2} \| \nabla c\|^2 \\   & \leq \frac{1}{2 \eta_1} (x_1 - x^{*})^2  - \frac{1}{2 \eta_T} (x_{T+1} - x^{*})^2 +      \frac{1}{2} \sum_{t=2}^T \left( \frac{1}{\eta_t} - \frac{1}{\eta_{t-1}} \right) (x_t - x^{*})^2 +      \frac{\|\nabla c \|^2}{2} \sum_{t=1}^T \eta_t \\   & \leq \| F\|^2 \left( \frac{1}{2 \eta_1} + \frac{1}{2} \sum_{t=2}^T \left(    \frac{1}{\eta_t} - \frac{1}{\eta_{t-1}}   \right) \right) + \frac{\| \nabla c \|^2}{2} \sum_{t=1}^T \eta_t \\   & \leq \| F\|^2 \frac{1}{2\eta_T} + \frac{\| \nabla c \|^2}{2} \sum_{t=1}^T \eta_t \end{aligned}$$令$$\eta_t = \frac{1}{\sqrt{t}}$$可得：

$$\displaystyle \begin{aligned} \sum_{t=1}^T \eta_t & = \sum_{t=1}^T \frac{1}{\sqrt{T}} \\     & \leq 1 + \int_{t=1}^T \frac{1}{\sqrt{t}} dt \\     & \leq 1 + [2\sqrt{t}]_{1}^T \\     & \leq 2 \sqrt{T} - 1 \end{aligned}$$

代回$$R_G(T)$$可得$$R_G(T) \leq \frac{\|F\|^2 \sqrt{T}}{2} + \left( \sqrt{T} - \frac{1}{2} \right) \| \nabla c \|^2$$(QED)

</details>

## 動態遺憾(dynamic regret)

前述的靜態遺憾是演算法$$A$$與固定點$$x^{*}$$累積成本差值，如果將固定點放寬為限定長度$$L$$的路徑的累積成本時，則為動態遺憾。

> 定義：路徑長度(path length)
>
> 向量序列$$x_1, \dots, x_T$$的長度為$$\sum_{t=1}^{T-1} d(x_t, x_{t+1})$$

定義集合$$\mathbb{S}(T,L)$$為$$T$$個向量，且路徑長度小於等於$$L$$的集合。

> 定義：動態遺憾(dynamic regret)
>
> 給定演算法$$A$$以及最大路徑長度$$L$$，則動態遺憾定義為：$$R_A(T,L) = C_A(T) - \min_{A^{'} \in \mathbb{S}(T,L)}C_{A^{'}}(T)$$

> theorem
>
> 若學習速度$$\eta$$為定值時，則貪婪投影演算法的動態遺憾滿足：
>
> $$R_G(T,L) \leq \frac{7 \|F\|^2}{4 \eta} + \frac{L \|F\|}{\eta} + \frac{T \eta \| \nabla c \|^2}{2}$$

## generalized infinitesimal gradient ascent (GIGA)

雙人重覆零和賽局可建模為在線線性規劃問題，且GIGA演算法為universal consistent。

令$$A,B$$分別為玩家和對手的<mark style="color:red;">(有限或無限)行動集合</mark>，$$A\times B$$為<mark style="color:red;">聯合行動(joint action)集合</mark>，<mark style="color:red;">效用函數</mark>$$u: A \times B \rightarrow \mathbb{R}$$越高越好。玩家和對手在時間$$t$$時，根據歷史已實現聯合行動集合決定當期的行動。

例如：和局賽局 $$A=\{a_1, a_2, a_3\}$$, $$B=\{b_1, b_2, b_3\}$$，$$u(a_1, b_1)=u(a_2, b_2)=u(a_3, b_3)=1$$，其於$$u(a_i, b_j)=0, \forall i \neq j$$。

令<mark style="color:red;">歷史(history)</mark>為聯合行動序列，$$H_t = (A\times B)_t$$為長度為$$t$$的行動序列集合。令$$H=\bigcup_{t=0}^\infty H_t$$為<mark style="color:red;">所有歷史的集合</mark>，且對於$$h \in H$$，定義$$|h|$$為<mark style="color:red;">歷史的長度</mark>。

例如$$h=\{(a_3,b_1), (a_1, b_2), (a_2, b_3), (a_2, b_2), (a_2, b_2)\}$$為一歷史。得$$h_3=(a_2, b_3)$$，$$h_{1,2}=b_1$$。

則<mark style="color:red;">歷史</mark>$$h$$<mark style="color:red;">的效用</mark>為$$\displaystyle u_{total}=\sum_{t=1}^{|h|}u(h_{t,1}, h_{t,2})$$。以上例計算得$$u_{total}(h)=2$$。

如果考慮<mark style="color:red;">玩家只使用固定行動</mark>$$a_2$$<mark style="color:red;">的歷史</mark>，定義如下：$$h_{ * \rightarrow a_2}=\{(a_2, b_1),(a_2, b_2), (a_2, b_3), (a_2, b_2), (a_2, b_2)\}$$。可得$$u_{total}(h_{* \rightarrow a_2})=3$$。

定義<mark style="color:red;">玩家不使用固定行動</mark>$$a$$<mark style="color:red;">，</mark>$$\forall h \in H$$<mark style="color:red;">的遺憾</mark>為：$$R_{*\rightarrow a} (h)=u_{total}(h_{* \rightarrow a}) -u_{total}(h)$$。以上例計算得$$R_{ *\rightarrow a_2}(h)=3-2=1$$。

遺憾可能為負值，如$$R_{ *\rightarrow a_1}(h)=1-2=-1$$。

定義<mark style="color:red;">最大遺憾(遺憾)</mark>為$$\displaystyle R(h)=\max_{a \in A}R_{ * \rightarrow a}(h)$$。以上例得$$R(h)=1$$。<mark style="color:blue;">由定義可知遺憾為歷史的函數，而與生成歷史的策略無關</mark>。

對於任意集合$$S$$，定義$$\Delta S$$為其上所有機率分佈的集合。對於分佈$$D$$與布林斷言$$P$$，定義$$Pr_{x \in D}[P(x)]$$為當$$P(x)$$為真時，$$x \in D$$的機率。

* 定義行為(behavior)$$\sigma :  H \rightarrow \Delta (A)$$為玩家由過去行動的歷史至下一個行動機率分佈的函數。
* 定義環境(environment)$$\rho: H \rightarrow \Delta(B)$$為對手由過去行動的歷史至下一個行動機率分佈的函數。
* 定義$$H_{\infty}=(A \times B)_{\infty}$$為無限歷史的集合。
* 定義$$F_{\sigma, \rho}\in \Delta(H_\infty)$$為玩家依據無限歷史與機率$$\sigma$$選擇行動，對手依據無限歷史與機率$$\rho$$選擇行動的機率分佈。
* $$\forall h \in H_\infty$$，定義$$h(t)$$為歷史$$h$$的前$$t$$個聯合行動。

> 定義：universal consistent
>
> 行為$$\sigma$$滿足以下條件時，為universal consistent:
>
> $$\forall \epsilon >0 ~ \exists T ~ \ni \forall \rho$$, $$Pr_{h \in F_{\sigma, \rho}}[\forall t > T, ~ \frac{R(h(t))}{t} > \epsilon] < \epsilon$$

一段時間後，平均遺憾值可能會降低。而這種隨時間收斂在所有環境中都是一致的。

### 將重複賽局建模為線上線性規劃

為了簡單起見，令$$A=\{1,2,\dots, n\}$$，在每個時間點，依行為$$\sigma$$的機率選取行動，定義$$F=\{x \in \mathbb{R}^n, ~x_i \geq 0, ~ \sum_{i=1}^n x_i = 1\}$$。

因此是考慮效用$$u$$而非成本$$c$$，所以是使用梯度上升而非下降。

> algorithm: GIGA
>
> 選定學習速率序列$$\{\eta_1, \eta_2, \dots \}$$。
>
> 給定任意初始點$$x_1 \in F$$，則$$\forall t$$
>
> 1. 依$$x_t$$的機率選擇行動，有$$x_{t,i}$$的機率選中行動$$i$$。
> 2. 觀察對手的行動$$h_{t,2}$$後，再計算 $$y_{t+1, i} = x_{t,i}+\eta_t u(i, h_{t,2})$$。$$x_{t+1}=P(y_{t+1})$$。\
>    其中$$P(y)=\argmin_{x \in F}d(x,y)$$。

> theorem:&#x20;
>
> 當$$\eta_t=\frac{1}{\sqrt{t}}$$時，GIGA為universally consistent。

