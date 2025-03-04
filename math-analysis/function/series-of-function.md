# 函數級數

## 無窮序列函數級數的一致收斂

> 定義：給定定義在集合$$S$$的函數序列$$\{f_n\}$$。$$\forall x \in S$$，令$$\displaystyle s_n(x)=\sum_{k=1}^n f_k(x), ~n=1,2,\dots,$$。
>
> 若存在函數$$f$$使得$$s_n \rightarrow f$$在集合$$S$$一致收斂，則稱級數$$\sum_n f_n(x)$$在集合$$S$$一致收斂。
>
> 記為 $$\displaystyle \sum_{n=1}^\infty f_n(x) = f(x)$$ uniformly on $$S$$。

### 一致收斂級數的Cauchy條件

> $$\displaystyle \sum_{n=1}^\infty f_n(x) = f(x)$$ uniformly on $$S \Leftrightarrow\displaystyle \forall \epsilon > 0 ~ \forall x \in S~ \exists \sum_{k=n+1}^{n+p} |f_n(x)|< \epsilon, p=1,2,\dots,$$

### Weierstrass M-test

> 令$$\{M_n\}$$為非負實數序列且滿足$$0 \leq |f_n(x)| \leq M_n, ~n=1,2,\dots, ~\forall x \in S$$
>
> 則$$\displaystyle \sum_n f_n(x)$$在集合$$S$$一致收斂 $$\Leftrightarrow$$ $$\displaystyle \sum_n M_n$$收斂。

### 函數級數一致收斂則函數序列連續時收斂函數也連續

> 令$$\displaystyle \sum_n f_n(x) =f(x)$$在集合$$S$$一致收斂。若$$f_n$$在點$$x_0 \in S$$收斂，則$$f$$在點$$x_0$$也收斂。

若$$x_0$$為集合$$S$$的極限點，則可交換limt與sum的順序，即：$$\displaystyle \lim_{x \rightarrow x_0} \sum_{n=1}^\infty f_n(x) = \sum_{n=1}^\infty \lim_{x \rightarrow x_0} f_n(x)$$。

## 函數序列一致收斂與Riemann-Stieltjes積分

> 令$$\alpha$$在閉區間$$[a,b]$$為有界變差(bounded varation)函數。令實值函數序列$$\{f_n\}$$在閉區間$$[a,b]$$為Riemann可積($$(f_n \in R(\alpha), ~\forall n$$)。
>
> 假設在閉區間$$[a,b]$$，函數序列$$\{f_n\}$$一致收斂至函數$$f$$，且令$$\displaystyle g_n(x)=\int_a^x f_n(t)d\alpha(t),~ x \in [a,b], ~ n =1,2,3\dots$$，則可得：
>
> 1. $$f \in R(\alpha)$$ on $$[a,b]$$
> 2. $$g_n \rightarrow g$$在閉區間$$[a,b]$$一致收斂，$$\displaystyle g(x)=\int_a^x f(t) d\alpha(t)$$

此定理說明了$$\forall x \in [a,b]$$，<mark style="color:red;">在一致收斂時，極限可穿積分符號</mark>：$$\displaystyle \lim_{n \rightarrow \infty} \int_a^x f_n(t) d\alpha(t) = \int_a^x \lim_{n \rightarrow \infty} f_n(t) d \alpha(t)$$

## 函數級數一致收斂與Riemann-Stieltjes積分

> 令$$\alpha$$在閉區間$$[a,b]$$為有界變差函數，且假設$$\displaystyle \sum f_n(x)=f(x)$$在閉區間$$[a,b]$$一致收斂，$$f_n$$為實值函數且在閉區間$$[a,b]$$ Riemann可積($$f_n \in R(\alpha)$$)，則可得：
>
> 1. $$f \in R(\alpha)$$ on $$[a,b]$$
> 2. $$\displaystyle \int_a^x \sum_{n=1}^\infty f_n(t) d \alpha(t) = \sum_{n=1}^\infty \int_a^x f_n(t) d \alpha(t)$$一致收斂
>
> 註：<mark style="color:red;">上式說明一致收斂函數可逐項積分(uniformly convergent sereis can be integrated term by term)</mark>。但反之可逐項積分的函數序列不一定一致收斂。

### 範例：點態收斂函數序列可逐項積分

$$f_n=x^n,~ 0 \leq x \leq 1$$，可得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) =\left\{ \begin{aligned} &0, ~ 0 \leq x < 1 \\ & 1, ~ x = 1 \end{aligned} \right.$$為點態收斂。

函數序列的逐漸積分為$$\displaystyle \int_0^1 f_n(x) dx = \int_0^1 x^n dx = \frac{1}{n+1} \rightarrow 0 \text{ as } n \rightarrow \infty$$

而$$\displaystyle \lim_{n \rightarrow \infty} \int_0^1 f_n(x)dx = \int_0^1 f(x)dx = 0$$
