---
description: minmax theorem
---

# 最小－最大定理

## 簡介

Von Neumann首先證明了最小－最大(minimax)定理，該定理保證了雙線性函數的最大-最小不等式相等。\


> ### theorem: minmax thoerem
>
> 令$$\Delta_M, ~\Delta_N$$為兩個有限行動集合的機率單純形，函數$$f: \Delta_M \times \Delta_N \rightarrow \mathbb{R}$$為雙線性(bilinear function)函數，則函數$$f$$存在鞍點(saddle point)滿足：
>
> $$\displaystyle \max_{\mathbf{x} \in \Delta_M} \min_{\mathbf{y} \in \Delta_N} f(\mathbf{x}, \mathbf{y}) = \min_{\mathbf{y} \in \Delta_N} \max_{\mathbf{x} \in \Delta_M}f(\mathbf{x}, \mathbf{y})$$

在雙人賽局$$\Gamma$$中，上式可表示為矩陣式如下：

$$\displaystyle \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2 = \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2$$

此最大最小值稱為<mark style="color:red;">賽局的價值（value of the game)</mark>。賽局的雙方都可採取行動防止對方獲得比此價值更高的報酬。

&#x20;如果雙方的報酬矩陣$$\mathbf{U}_1, \mathbf{U}_2$$滿足$$\mathbf{U}_1 + \mathbf{U}_2=\mathbf{0}$$時，稱為雙人零和賽局(zero-sum game)，通常可簡寫報酬矩陣為$$\mathbf{U}$$。

範例

![雙人零和賽局，賽局價值為５](<../.gitbook/assets/minmax\_game-min (1).png>)

## Sion's minmax theorem

> 令$$\mathbb{X, Y}$$均為閉凸集合，且函數$$f: \mathbb{X \times Y} \rightarrow \mathbb{R}$$滿足：
>
> 1. 對於固定的$$y \in \mathbb{Y}$$, $$f(x,y)$$為上半連續(upper semi-continuous)且在$$\mathbb{X}$$為準凹(quasi-concave)函數。
> 2. 對於固定的$$x \in \mathbb{X}$$，$$f(x,y)$$​為下半連續(lower semi-cjontinuous)且在$$\mathbb{Y}$$​為準凸(quasi-convex)函數。
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
