# 二次變差(quadratic variation)

## 簡介

二次變差是研究隨機過程，特別是布朗運動性質的主要工具之一。

> 二次變差
>
> 函數$$f: [a,b] \rightarrow \mathbb{R}$$，給定區間$$[a,b]$$的分割$$P=\{x_0, x_1, \dots, x_n\}$$
>
> 定義二次變差為
>
> $$\displaystyle Q_f(a,b)=\lim_{\Delta x_n \rightarrow 0}\sum_{k=1}^n (\Delta f_k)^2$$，
>
> 其中$$\displaystyle \Delta x_n = \max_{1\leq k \leq n}(x_k - x_{k-1})$$，$$\Delta f_k = f(x_k) - f(x_{k-1})$$

同樣定義如果端點可變時，$$Q_f(x)\equiv  Q_f(a,x)$$為$$x$$的非遞減函數。

考慮$$p$$次以上的全變差，可得$$1 \leq p < q < \infty$$時，<mark style="color:red;">有限</mark>$$p$$<mark style="color:red;">次變差可保證有限</mark>$$q$$<mark style="color:red;">次變差</mark>。

## 連續函數若為有限一次變差，則二次變差為0

> $$f: [a,b] \rightarrow \mathbb{R}$$為連續函數，且為有限變差，即$$V_f(x) < \infty, ~ \forall x \in [a,b]$$。
>
> 則$$Q_f(x)=0$$。
>
> [https://math.stackexchange.com/questions/3246700/quadratic-variation-of-a-continuous-function](https://math.stackexchange.com/questions/3246700/quadratic-variation-of-a-continuous-function)

<details>

<summary>proof</summary>

$$\displaystyle  \begin{aligned} Q_f(x) & = \lim_{\Delta x_n \rightarrow 0} \sum_{k=1}^{n} (f(x_{k}) - f(x_{k-1}))^2 \\ & \leq \lim_{\Delta x_n \rightarrow 0} \max_{k} |(f(x_{k}) - f(x_{k-1})| \sum_{k=1}^{n}| f(x_{k}) - f(x_{k-1}) | \\ & \leq \lim_{\Delta x_n \rightarrow 0} \max_{k} |(f(x_{k}) - f(x_{k-1})| V_f(x)  \end{aligned}$$

因為$$f$$在閉區間$$[a,b]$$為連續函數，因此$$f$$為$$[0,x]$$為[一致連續函數](continuous-function.md#ding-yi-yu-wei-bi-ou-jian-de-lian-xu-han-shu-bi-wei-jun-yun-lian-xu-han-shu)。

所以$$\displaystyle \lim_{\Delta x_n \rightarrow 0} \max_{k} |(f(x_{k}) - f(x_{k-1})|=0$$

得$$0 \leq Q_f(x) \leq 0 \Rightarrow Q_f(x)=0$$ (QED)

</details>

## 二次共變差(quadratic covaration)

> 函數$$f, g: [a,b] \rightarrow \mathbb{R}$$，給定區間$$[a,b]$$的分割$$P=\{x_0, x_1, \dots, x_n\}$$
>
> 若極限存在時，定義二次共變差為：$$\displaystyle Q_{f,g}(a,b)=\lim_{\Delta x_n \rightarrow 0} \sum_{k=1}^n(\Delta f_k \Delta g_k)$$

定義如果端點可變時$$Q_{f,g}(x) \equiv Q_{f,g}(a,x)$$，為$$x$$的非遞減函數。

<mark style="color:red;">二次共變差滿足交換性</mark>，即$$Q_{f,g}(a,b) = Q_{g,f}(a,b)$$。

## 連續函數與有界變差函數的二次共變差為0

> $$f$$為連續函數，$$g$$為有界變差函數($$V_g(x) < \infty, \forall x \in [a,b]$$)，則$$V_{f,g}(a,b)=0$$

## 極化等式(polarization identity)

> $$Q_{f,g}(x) = \frac{1}{2}[Q_{f+g, f+g}(x) - Q_{f,f}(x) - Q_{g,g}(x)]$$

