---
description: minmax theorem
---

# 最小－最大定理

## 簡介

Von Neumann首先證明了最小－最大minimax定理，該定理保證了雙線性函數的最大-最小不等式相等。\


> theorem: minmax thoerem
>
> 令$$\Delta_M, ~\Delta_N$$為兩個有限行動集合的機率單純形，函數$$f: \Delta_M \times \Delta_N \rightarrow \mathbb{R}$$為雙線性(bilinear function)函數，則函數$$f$$存在鞍點(saddle point)滿足：
>
> $$\displaystyle \max_{\mathbf{x} \in \Delta_M} \min_{\mathbf{y} \in \Delta_N} f(\mathbf{x}, \mathbf{y}) = \min_{\mathbf{y} \in \Delta_N} \max_{\mathbf{x} \in \Delta_M}f(\mathbf{x}, \mathbf{y})$$

在雙人賽局$$\Gamma$$中，上式可表示為矩陣式如下：

$$\displaystyle \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2 = \min_{\mathbf{s}_2 \in \Delta(\mathcal{A}_2)} \max_{\mathbf{s}_1 \in \Delta(\mathcal{A}_1)} \mathbf{s}_1^\top \mathbf{U}_1 \mathbf{s}_2$$

此最大最小值稱為<mark style="color:red;">賽局的價值（value of the game)</mark>。賽局的雙方都可採取行動防止對方獲得比此價值更高的報酬。
