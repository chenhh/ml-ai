---
description: minmax theorem
---

# 最小－最大定理

## 簡介

Von Neumann首先證明了最小－最大(minimax)定理，該定理保證了雙線性函數的最大-最小不等式相等。\


## minimax thoerem

### 函數型式

$$\mathbf{X} \subset \mathbb{R}^n, \mathbf{Y} \subset \mathbb{R}^m$$為閉(緊緻)凸集合。若$$f: \mathbf{X \times Y} \rightarrow \mathbb{R}$$為連續函數且滿足：

* $$f(\cdot, y): X \rightarrow \mathbb{R}$$在給定任意$$y$$​值時均為凹函數且
* $$f(x,\cdot): Y \rightarrow \mathbb{R}$$​在給定任意$$x$$​時均為凸函數。

滿足上述條件常見函數如：

* $$f(x,y)=x^\top \mathbf{A} y, ~ A \in \mathbb{R}^{n \times m}$$，賽局理論常見。
* $$f(x,y)=y^2 - x ^2$$​

則可得$$\displaystyle \max_{x \in \mathbf{X}} \min_{{y} \in \mathbf{Y}} fx,y) = \min_{{y} \in \mathbf{Y}} \max_{x \in \mathbf{X}}f(x, y)$$



![f(x,y)=y\*\*2 - x\*\*2](../.gitbook/assets/Saddle\_point.svg-min.png)

### 賽局理論型式

> 令$$\Delta_M, ~\Delta_N$$為兩個有限行動集合的機率單純形(simplex)，函數$$f: \Delta_M \times \Delta_N \rightarrow \mathbb{R}$$為雙線性(bilinear function)函數，則函數$$f$$存在鞍點(saddle point)滿足：
>
> $$\displaystyle \max_{\mathbf{x} \in \Delta_M} \min_{\mathbf{y} \in \Delta_N} f(\mathbf{x}, \mathbf{y}) = \min_{\mathbf{y} \in \Delta_N} \max_{\mathbf{x} \in \Delta_M}f(\mathbf{x}, \mathbf{y})$$

在雙人賽局$$\Gamma$$中，上式可表示為矩陣式如下：

$$\displaystyle \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2 = \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2$$

此最大最小值稱為<mark style="color:red;">賽局的價值（value of the game)</mark>。<mark style="color:red;">賽局的雙方都可採取行動防止對方獲得比此價值更高的報酬</mark>。

&#x20;如果雙方的報酬矩陣$$\mathbf{U}_1, \mathbf{U}_2$$滿足$$\mathbf{U}_1 + \mathbf{U}_2=\mathbf{0}$$時，稱為雙人零和賽局(zero-sum game)，通常可簡寫報酬矩陣為$$\mathbf{U}$$。

範例

![雙人零和賽局，賽局價值為５](<../.gitbook/assets/minmax\_game-min (1).png>)

## Sion's minmax theorem

> 令$$\mathbb{X , Y }$$均為線性拓樸空間的閉(緊緻)凸集合，且函數$$f: \mathbb{X \times Y} \rightarrow \mathbb{R}$$滿足：
>
> 1. 對於固定的$$y \in \mathbb{Y}$$, $$f(x,y)$$為上半連續(upper semi-continuous)且在$$\mathbb{X}$$為擬凹(quasi-concave)函數。
> 2. 對於固定的$$x \in \mathbb{X}$$，$$f(x,y)$$​為下半連續(lower semi-cjontinuous)且在$$\mathbb{Y}$$​為擬凸(quasi-convex)函數。
>
> 則可得 $$\displaystyle \sup_{x \in \mathbb{X}} \inf_{y \in \mathbb{Y}} f(x,y) = \inf_{y \in \mathbb{Y}} \sup_{x \in \mathbb{X}} f(x,y)$$​

準凸函數和準凹函數是凸函數和凹函數的弱化條件，而上半連續與下半連續是連續函數的弱化條件，因此適用的函數範圍更廣。



<mark style="color:red;">最大最小定理意味著，對於任何一個對手的策略</mark>$$s_2$$，<mark style="color:red;">玩家總是有一個對應的策略</mark>$$s_1(s_2)$$<mark style="color:red;">可保証玩家的報酬為定值。因此就存在一個通用的</mark>$$s_1^{*}$$，<mark style="color:red;">可對應對手的任意策略</mark>$$s_2$$<mark style="color:red;">都有效</mark>。

因此可將最大最小定理改寫如下：

> 令$$\Delta_M, \Delta_N$$為兩個有限行動集合的機率單純形，函數$$f: \Delta_M \times \Delta_N \rightarrow \mathbb{R}$$為雙線性(bilinear function)函數。
>
> 假設$$c \in \mathbb{R}$$為雙人零和賽局的價值，因此最大最小定理可改寫為：
>
> $$\begin{aligned} & \forall s_2 \in \Delta(A_2) \exists s_1(s_2) \in \Delta(A_1) \ni s_1^{\top} \mathbf{U} s_2 \geq c \\ & \Rightarrow \exists s_1^{*} \in \Delta(A_1) \ni \forall s_2 \in \Delta(A_2), s_1^*{\top} \mathbf{U} s_2 \geq c \end{aligned}$$

### 半連續(semi-continuous)

半連續可用於定義擴展實數，且是比連續函數更弱的性質。

* 擴展實數$$\overline{\mathbb{R}}=\mathbb{R} \cup \{-\infty, \infty \} = [-\infty, \infty]$$
* 註：實數$$x \leq  y$$​可寫成 $$\forall \epsilon > 0, x \leq y+ \epsilon$$。

函數$$f:X \rightarrow \mathbb{R}$$​在點$$x_0$$​連續：

* $$\forall \epsilon > 0, ~ \exists \delta >0 \ni |x-x_0|< \delta \Rightarrow  |f(x) - f(x_0)|<\epsilon$$
* 一個函數在一點連續的充要條件是它在該點既上半連續也下半連續。
* 由定義可知，當$$x$$​從左側或右側非常接近$$x_0$$​時，，可保證$$f(x) <f(x_0)$$且 $$f(x_0) < f(x)$$​，即$$f(x)$$​也會同時由上側或下側接近$$f(x_0)$$。

函數$$f: X \rightarrow \overline{\mathbb{R}}$$​在點$$x_0$$​上半連續：

* $$\displaystyle \limsup_{x \rightarrow x_0} f(x) \leq f(x_0)$$
* $$\forall \epsilon >0 ~ \exists \delta >0 \ni |x-x_0| < \delta \Rightarrow f(x)  < f(x_0)+\epsilon$$
* 當$$x$$從左側或右側接近$$x_0$$​時，只要夠接近，必定可得到$$f(x) < f(x_0)$$​的結果。

![函數f在點x0上半連續](../.gitbook/assets/Upper\_semi.png)

函數$$f: X \rightarrow \overline{\mathbb{R}}$$​在點$$x_0$$​下半連續：

* $$\displaystyle \liminf_{x \rightarrow x_0} f(x) \geq f(x_0)$$
* $$\forall \epsilon >0 ~ \exists \delta >0 \ni |x-x_0| < \delta \Rightarrow f(x_0) -\epsilon < f(x)$$
* 當$$x$$​從左側或右側接近$$x_0$$​時，只要夠接近，必定可得到$$f(x_0) < f(x)$$​的結果。

![函數f在點x0下半連續](../.gitbook/assets/Lower\_semi.png)

## 擬凸函式（Quasiconvex function）

令$$S \subseteq \mathbb{R}^n$$為凸集合，則$$f: S \rightarrow \mathbb{R}$$：

* 滿足此條件時稱為凸函數：$$\forall x,y \in S, 0 \leq c \leq 1, ~ f(cx+(1-c)y) \leq cf(x)+(1-c)f(y)$$​
* 滿足此條件時稱為凹函數：$$\forall x,y \in S, 0 \leq c \leq 1, ~ f(cx+(1-c)y) \geq cf(x)+(1-c)f(y)$$
* 滿足此條件時稱為擬凸函數：$$\forall x,y \in S, 0 \leq c \leq 1, ~ f(cx+(1-c)y) \leq  \max\{f(x), f(y)\}$$
* 滿足此條件時稱為擬凹函數：$$\forall x,y \in S, 0 \leq c \leq 1, ~ f(cx+(1-c)y) \leq  \min\{f(x), f(y)\}$$

## 參考資料

* John Von Neumann,  "Zur Theorie der Gesellschaftsspiele, " Mathematische annalen, pp. 295-310,  Vol. 100, 1928.
* Maurice Sion, "On general minimax theorems, " Pacific Journal of Mathematics, pp. 171-176, Vol. 8  No. 1, 1958.
