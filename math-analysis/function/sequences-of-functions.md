---
description: sequences of functions
---

# 函數序列

## 簡介

* 點態收斂、逐點收斂(pointwise convergence)
* 一致收斂、均勻收斂(uniform convergence)
* 一致有界(uniformly bounded)
* 無窮序列函數級數的一致收斂
* Riemann-Stieltjes積分與一致收斂

## 函數數列的點態(逐點)收斂

給定同一定義域的實數(複數)函數數列$$\{f_n\}$$，若函數$$f$$滿足 $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x), ~ x \in S$$，則稱函數$$f$$為函數數列的極限函數(limit function)，且稱<mark style="color:red;">函數數列</mark>$$\{f_n\}$$<mark style="color:red;">逐點收斂至集合</mark>$$S$$。

#### 範例1

令$$f_n(x)=\frac{x^{2n}}{1+x^{2n}}, ~ x \in \mathbb{R}, ~ n \in \mathbb{N}$$,則$$\displaystyle \lim_{n \rightarrow \infty} f(x) = \left\{ \begin{aligned} 0 & \text{ if } |x| \leq 1, \\ \frac{1}{2} & \text{ if } |x| = 1 \\ 1 & \text{ if } |x| > 1 \end{aligned} \right.$$，由連續函數收斂至非連續函數(但為幾乎處處連續函數)。

![逐點收斂範例1](../../.gitbook/assets/Figure\_1-min.png)

#### 範例2

函數序列$$\displaystyle \lim_{n \rightarrow \infty} \int_0^1 f_n(x) dx \neq \int_0^1 \lim_{n \rightarrow \infty} f_n(x)dx$$

令$$f_n(x)=n^2x(1-x)^n, ~ \forall x \in \mathbb{R}$$

若$$0 \leq x \leq 1$$，則$$\displaystyle f(x) = \lim_{n \rightarrow \infty} f(x) = 0$$存在，所以$$\displaystyle \int_0^1 f(x) dx = 0$$

但是$$\displaystyle \int_0^1 f_n(x) dx = n^2 \int_0^1 x(1-x)^n dx = n^2 \int_0^1 (1-t)t^n dt= \frac{n^2}{(n+1)(n+2)}$$

可得 $$\displaystyle \lim_{n \rightarrow \infty }\int_0^1 f_n(x) dx = 1$$

## 一致收斂的定義

> 有二種常見的定義：令函數序列$$\{f_n\}$$在集合$$S$$內一致收斂至函數$$f$$：
>
> 1. $$\forall \epsilon > 0$$ $$\exists n_0 \in \mathbb{N}$$ (只依賴與於$$\epsilon$$的選擇，與$$x$$無關)$$\forall x \in S \ni |f_n(x) - f(x)|< \epsilon, ~\forall n \geq n_0$$
> 2. $$\displaystyle \forall \epsilon > 0, \exists n_0 \in \mathbb{N} \ni \sup_{x \in S}|f_n(x) - f(x)| < \epsilon~ \forall n \geq n_0$$
>
> 此處$$\epsilon$$的選擇是針定所有的點$$x$$均成立，與點態收斂中$$\epsilon$$可能依$$x$$變化不同。

<figure><img src="../../.gitbook/assets/pointwise_conv.jpg" alt=""><figcaption><p>點態收態，f與fn的距離在每一點x可能不同</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/uniform_conv.jpg" alt=""><figcaption><p>一致收斂，f與fn在定義域每一點都可保持在相同的距離內</p></figcaption></figure>

### 連續函數一致收斂後仍為連續函數

> 假設所有的函數$$f_n$$均在點$$c \in S ~ \forall n \in \mathbb{N}$$，若$$f_n$$一致收斂至函數$$f$$，則$$f$$也在點$$c \in S$$連續。
>
> 若$$c$$為集合$$S$$的極限點，可得$$\displaystyle \lim_{x \rightarrow c}\lim_{n \rightarrow \infty} f_n(x) =  \lim_{n \rightarrow \infty} \lim_{x \rightarrow c} f_n(x)$$
>
> 在一般度量空間$$(S,d)$$也成立

<details>

<summary>proof: 可分c為孤立點和極限點的情形</summary>

若$$c$$為孤立點，則點$$f$$在$$c$$必定連續。

若$$c$$為極限點，由一致連續假設得$$\forall \epsilon >0 \forall x \in S ~\exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x) |< \epsilon$$

因為所有的函數序列均在$$c$$連續，因此存在開球$$B(c, r)$$滿足$$\forall x \in B(c,r) \cap S$$, $$|f_{n_0}(x) - f_{n_0}(c)| < \epsilon$$

由於 $$|f(x)-f(c)| \leq |f(x) - f_{n_0}(x)| + |f_{n_0}(x) - f_{n_0}(c)| + |f_{n_0}(c) - f(c)|$$

且當$$x \in B(c,r) \cap S$$可得$$|f(x) - f(c)|< 3 \epsilon$$ (QED)

</details>

## 一致有界(uniformly bounded)

> 函數$$\{f_n\}$$在集合$$S$$稱為一致有界若存在常數$$M > 0, |f_n(x)| \leq M, ~ \forall x \in S, \forall n \in \mathbb{N}$$。

一致有界對所有$$x \in S$$以及對所有$$f_n$$有共同的上下界。



### 一致收致且個別函數有界時可得一致有界

> 令$$\{f_n\} \rightarrow f$$ 在集合$$S$$一致收斂，且$$f_n, ~\forall n \in \mathbb{N}$$在$$S$$上有界，則$$f_n$$在集合$$S$$一致有界。

## 一致收斂的Cauchy條件

> 令$$\{f_n\}$$為定義在集合$$S$$上的函數序列。
>
> 函數序列$$f_n \rightarrow f$$在$$S$$一致收斂 $$\Leftrightarrow$$ $$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni |f_m(x)-f_n(x)|<\epsilon, ~\forall m,n >n_0$$
>
> 在一般度量空間$$(S,d)$$中也成立

<details>

<summary>proof</summary>

\=> 令$$f_n \rightarrow f$$在點$$S$$上一致收斂，由定義得$$\forall \epsilon >0, ~\forall x \in S, ~\exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x)| < \epsilon/2, ~ \forall n > n_0$$

同樣田定義可得 $$|f_m (x) - f(x) | < \epsilon/2, ~ \forall m > n_0$$

合併上述兩式得$$\forall x s\in S, ~|f_m(x)-f_n(x)|<\epsilon$$ (QED)

<=

由Cauchy條件得$$\forall x \in S, ~\{f_n(x)\}$$收斂，令$$\displaystyle f(x)=\lim_{n \rightarrow \infty} f_n(x),~ x \in S$$。

當$$\epsilon>0$$，$$\forall x \in S$$，由Cauchy條件可得$$|f_n(x) - f_{n+k}(x)|  < \epsilon/2, ~k=1,2,\dots$$

因此$$\displaystyle$$$$\displaystyle \lim_{k \rightarrow \infty }|f_n(x) - f_{n+k}(x)| = |f_n(x) - f(x)|  < \epsilon/2$$

因此$$\forall n > n_0$$，$$\forall x \in S$$，可得$$|f_n(x) - f(x) | < \epsilon$$ (QED)

</details>

## 無窮序列函數級數的一致收斂

> 定義：給定定義在集合$$S$$的函數序列$$\{f_n\}$$。$$\forall x \in S$$，令$$\displaystyle s_n(x)=\sum_{k=1}^n f_k(x), ~n=1,2,\dots,$$。
>
> 若存在函數$$f$$使得$$s_n \rightarrow f$$在集合$$S$$一致收斂，則稱級數$$\sum_n f_n(x)$$在集合$$S$$一致收斂。
>
> 記為 $$\displaystyle \sum_{n=1}^\infty f_n(x) = f(x)$$ uniformly on $$S$$。

### 一致收斂級數的Cauchy條件

> $$\displaystyle \sum_{n=1}^\infty f_n(x) = f(x)$$ uniformly on $$S \Leftrightarrow$$$$\displaystyle \forall \epsilon > 0 ~ \forall x \in S~ \exists \sum_{k=n+1}^{n+p} |f_n(x)|< \epsilon, p=1,2,\dots,$$

### Weierstrass M-test

> 令$$\{M_n\}$$為非負實數序列且滿足$$0 \leq |f_n(x)| \leq M_n, ~n=1,2,\dots, ~\forall x \in S$$
>
> 則$$\displaystyle \sum_n f_n(x)$$在集合$$S$$一致收斂 $$\Leftrightarrow$$ $$\displaystyle \sum_n M_n$$收斂。

### 函數級數一致收斂則函數序列連續時收斂函數也連續

> 令$$\displaystyle \sum_n f_n(x) =f(x)$$在集合$$S$$一致收斂。若$$f_n$$在點$$x_0 \in S$$收斂，則$$f$$在點$$x_0$$也收斂。

若$$x_0$$為集合$$S$$的極限點，則可交換limt與sum的順序，即：$$\displaystyle \lim_{x \rightarrow x_0} \sum_{n=1}^\infty f_n(x) = \sum_{n=1}^\infty \lim_{x \rightarrow x_0} f_n(x)$$。

## 函數序列一致收斂與Riemann-Stieltjes積分

> 令$$\alpha$$在閉區間$$[a,b]$$為有界變差(bounded varation)函數。令實值函數序列$$\{f_n\}$$在閉區間$$[a,b]$$為Riemann可積($$(f_n  \in R(\alpha), ~\forall n$$)。
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

$$f_n=x^n,~ 0 \leq x \leq 1$$，可得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) =\left\{ \begin{aligned} &0, ~ 0 \leq x < 1 \\ & 1, ~ x = 1  \end{aligned} \right.$$為點態收斂。

函數序列的逐漸積分為$$\displaystyle \int_0^1 f_n(x) dx = \int_0^1 x^n dx = \frac{1}{n+1} \rightarrow 0 \text{ as } n \rightarrow \infty$$

而$$\displaystyle \lim_{n \rightarrow \infty} \int_0^1 f_n(x)dx = \int_0^1 f(x)dx = 0$$



## 有界收斂(bounded convergence)

> 定義：函數序列$$\{f_n\}$$在集合$$S$$若為點斂收斂(至$$f$$)且一致有界($$\exists M >0 \ni |f_n(x) \leq M~\forall x \in S$$)，則稱$$\{f_n\}$$有界收斂。

### Arzela theorem

> 函數序列$$\{f_n\}$$在閉區間$$[a,b]$$有界收斂，且所有的函數$$f_n$$在$$[a,b]$$均為Riemann可積分。
>
> 假設極限函數$$f$$在$$[a,b]$$也為Riemann可積分，則：
>
> $$\displaystyle \lim_{n \rightarrow \infty} \int_a^b f_n(x) dx = \int_a^b \lim_{n \rightarrow \infty}  f_n(x) dx = \int_a^b f(x) dx$$

註：存在$$\{f_n\}$$在$$[a,b]$$有界收斂且Riemann可積，但$$f$$在$$[a,b]$$不可積分。

### 範例：函數序列有界收斂且可積分但極限函數不可積分

令$$\{r_1, r_2,\dots\} \subseteq [0,1]$$為有理數集合，令$$f_n(x) =  \left\{ \begin{aligned} &1, ~\text{ if } x = r_k, ~k=1,2,\dots,n \\ &0, ~ \text{ otherwise } \end{aligned} \right.$$

可得$$\displaystyle \int_0^1 f_n(x)dx=0, ~ \forall n$$，但$$\lim_{n \rightarrow \infty} f$$在$$[0,1]$$不可Riemann積分(但可Lebesgue積分)。


