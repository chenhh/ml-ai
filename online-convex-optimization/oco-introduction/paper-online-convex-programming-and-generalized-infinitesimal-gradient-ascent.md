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

不失一般性，令成本函數$$c_t(x) = g_t^\top x$$為線性函數。可得$$\nabla c_t(x_t)=g_t$$。

如果將$$c_t(x)$$全部換成$$g_t^\top x$$可得演算法的結果不變，接下來分析遺憾的部份。



因為$$c_t, ~\forall x \in F$$為凸函數，由凸函數的一階條件可得 $$c_t(x) \geq \nabla c_t(x_t)^\top (x-x_t)+c_t(x_t)$$。

令$$x^{*} \in F$$為靜態最佳解。可得$$c_t(x^{*}) \geq g^\top (x^{*}-x_t)+c_t(x_t)$$。

可得$$c_t(x_t) - c_t(x^{*}) \leq c_t(x_t) - (g_t^\top (x^{*} - x_t) + c_t(x_t)) \leq g_t^\top x_t - g_t^\top x^{*}$$。

因此用線性函數的遺憾至少和凸函數一樣多。





</details>



