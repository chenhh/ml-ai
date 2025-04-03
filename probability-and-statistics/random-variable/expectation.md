---
description: expectation
---

# 期望值

## 期望值

離散隨機變數$$X$$的pmf為 $$P(X=x_i) =p_i, \ i \in \mathbb{N}$$。若$$\displaystyle \sum_{i=1}^{\infty} |x_i| p_i < \infty$$(有限值時)，則$$X$$的期望值為$$\displaystyle \mathrm{E}(X) \equiv \sum_{i=1}^{\infty} x_i p_i$$。此處$$0 \leq p_i \leq 1, \forall i$$

連續隨機變數的pdf為$$f(x), \forall x \in \mathbb{R}$$，若$$\displaystyle \int_{-\infty}^{\infty}|x|f(x) < \infty$$，則期望值為$$\displaystyle \mathrm{E}(X) \equiv \int_{-\infty}^{\infty} x f(x)dx$$，此處$$f(x)$$可能大於1。

而pdf期望值的Stieltjes積分形式為 $$\displaystyle \mathrm{E}(X) \equiv\int_{-\infty}^{\infty} xdF(x)$$。

期望值的不偏估計式為 $$\displaystyle \hat{\mu_X} = \frac{1}{n} \sum_{i=1}^n x_i$$。

### 隨機變數函數的期望值

> * $$\displaystyle \mathrm{E}(u(X))=\sum_{i=1}^\infty u(x_i) p_i$$
> * $$\displaystyle \mathrm{E}(u(X))=\int_{-\infty}^{\infty} u(x)f(x)dx$$

### 期望值為線性算子

> 給定$$a_1, a_2,\dots, a_n \in \mathbb{R}$$，隨機變數$$X_1, X_2, \dots, X_n$$：
>
> $$\mathrm{E}(a_1X_1 + a_2 X_2 )=a_1 \mathrm{E}(X_1) + a_2 \mathrm{E}(X_2)$$。
>
> $$\displaystyle \mathrm{E}(\sum_{i=1}^n a_i X_i) = \sum_{i=1}^n a_i \mathrm{E}(X_i)$$。
>
> $$g_1, g_2$$為兩函數，若$$\mathrm{E}(g_1(X)), \mathrm{E}(g_2(X))$$存在，則$$\mathrm{E}( ag_1(X)+ bg_2(X)+c) = a\mathrm{E}(g_1(x)) + b \mathrm{E}(g_2(x))+c$$

$$\mathrm{E}(g(X)) = \begin{cases} &\sum_{i=1}^n g(x_i) f(x_i), \text{ 離散r.v. }, \\ & \int_{-\infty}^{\infty} g(x) f(x)dx, \text{ 連續r.v.}. \end{cases}$$

### 期望值與單調函數的性質

$$g_1, g_2$$為兩函數，使得期望值$$\mathrm{E}(g_1(X)), \mathrm{E}(g_2(X))$$存在，則：

* $$\forall x \in \mathbb{R}, g_1(x) \geq 0 \Rightarrow \mathrm{E}(g_1(x)) \geq 0$$
* $$\forall x \in \mathbb{R}, g_1(x) \geq g_2(x) \Rightarrow \mathrm{E}(g_1(x)) \geq \mathrm{E}(g_2(x))$$
* $$\forall x \in \mathbb{R}, a \leq g_1(x) \leq b \Rightarrow a \leq \mathrm{E}(g_1(x)) \leq b$$

### 有界的隨機變數必存在期望值

> 隨機變數$$X$$稱為有界(bounded)若$$\exists M > 0 \ni \mathrm{P}(|X| \leq M ) = 1$$。

## Theorem：期望值變換

> 若$$\displaystyle \int_{-\infty}^{\infty} |g(x)|dF(x) < \infty$$，則$$\mathrm{E}(g(X))$$存在且$$\displaystyle\mathrm{E}(g(X))= \int_{-\infty}^{\infty}g(x)dF(x)$$

## Theorem：加法算子與期望值算子的交換性

> * $$X_1, X_2,\ldots$$為非負值的隨機變數，則 $$\displaystyle \operatorname{E}( \sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty} \operatorname{E}(X_i)$$
> * 對任意的$$X_1, X_2, \ldots$$，若$$\displaystyle \sum_{i=1}^{\infty} \operatorname{E}(|X_i|) < \infty$$，則$$\displaystyle\operatorname{E}(\sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty}\operatorname{E}(X_i)$$
