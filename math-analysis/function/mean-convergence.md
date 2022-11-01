---
description: mean convergence
---

# 均值收斂

## 均值收斂定義

> 函數序列$$\{f_n\}$$在閉區間$$[a,b]$$均為Riemann可積分，且令函數$$f$$在閉區間$$[a,b]$$可積分。
>
> 則序列$$\{f_n\}$$滿足以下條件時，在閉區間$$[a,b]$$稱為均值收斂：
>
> $$\displaystyle \lim_{n \rightarrow \infty} \int_a^b |f_n(x) - f(x)|^2 dx = 0$$

註：均值收斂無法保證函數序列在$$[a,b]$$任一點的點態收斂。

### 一致收斂可保證均值收斂

> 函數序列$$\{f_n\}$$一致收斂至函數$$f$$且$$f_n,~\forall n \in \mathbb{N}$$在閉區間$$[a,b]$$均為Riemann可積時，則可得$$\displaystyle \lim_{n \rightarrow \infty} \int_a^b |f_n(x) - f(x)|^2 dx = 0$$

proof:

如果給定$$\epsilon >0$$，可得到不等式$$|f_n(x) - f(x)| < \epsilon ~ \forall x \in [a,b]$$均成立時，則可得$$\displaystyle \int_a^b |f_n(x) - f(x)|^2 dx \leq \epsilon^2 (b-a)$$&#x20;

兩邊取極限可得證(QED)

### 範例：均值收斂但非點態收斂

將閉區間$$[0,1]$$分成$$2^n$$等份，令$$I_{2n+k}$$為右端點為$$(k+1)/2^n$$的區間，$$k=0,1,2,\dots, 2^{n}-1$$。

可得區間$$I_1=[0,1]$$，$$I_2=[0, \frac{1}{2}]$$，$$I_3=[\frac{1}{2}, 1]$$，$$I_4=[0, \frac{1}{4}]$$，$$I_5=[\frac{1}{4}, \frac{1}{2}]$$，$$I_6=[\frac{1}{2}, \frac{3}{4}]$$以此類推。

定義函數序列$$f_n(x) =  \left\{ \begin{aligned} &1, ~ \text{ if } x \in I_n, \\ &0, ~ \text{ if } x \in [0,1] - I_n   \end{aligned} \right.$$

則$$\{f_n\}$$均值收斂至0。

因為$$\int_0^1|f_n(x)|^2dx$$之值為長度$$I_n$$，可得$$n \rightarrow \infty$$時，$$|I_n| \rightarrow \infty$$。

反之當$$x \in [0,1]$$，可得$$\displaystyle \limsup_{n \rightarrow \infty} f_n(x)=1$$且 $$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)=0$$，因此$$\{f_n\}$$在$$[0,1]$$任一點均不收斂。

## 均值收斂可得積分函數序列一致收斂

> 令函數序列在閉區間$$[a,b]$$均值收斂$$\displaystyle \lim_{n \rightarrow \infty} \int_a^b |f_n(x) - f(x)|^2 dx = 0$$。
>
> 令函數$$g$$在閉區間$$[a,b]$$Riemann可積，定義$$\displaystyle h(x)=\int_a^x f(t)g(t)dt$$, $$\displaystyle h_n(x)=\int_a^x f_n(t)g(t)dt, ~ x\in [a,b]$$
>
> 則可得$$h_n \rightarrow h$$在閉區間$$[a,b]$$一致收斂。​

<details>

<summary>proof: Cauchy-Schawarz不原式</summary>

$$\displaystyle 0 \leq \left(   \int_a^x |f(t) - f_n(t)||g(t)| dt \right)^2 \leq  \left(  \int_a^x |f(t) - f_n(t)|^2 dt \right)  \left( \int_a^x |g(t)|^2 dt  \right)$$--(1)

給定$$\epsilon >0$$可得$$n_0 \in \mathbb{N} \ni  \displaystyle \int_a^b |f(t) - f_n(t)|^2 dt < \frac{\epsilon^2}{A} ~ \forall n > n_0$$--(2)

$$\displaystyle A=1+ \int_a^b |g(t)|^2 dt$$

將(2)代入(1)中可得$$\forall n > n_0 ,~0 \leq ||h(x) - h_n(x)| < \epsilon, ~x \in [a,b]$$ (QED)

</details>

### 更一般化的條件

> 令函數序列$$f_n$$在閉區間均值收斂$$\displaystyle \lim_{n \rightarrow \infty} \int_a^b |f_n(x) - f(x)|^2 dx = 0$$且
>
> 函數序列$$g_n$$ 在閉區間均值收斂$$\displaystyle \lim_{n \rightarrow \infty} \int_a^b |g_n(x) - g(x)|^2 dx = 0$$
>
> 定義$$\displaystyle h(x)=\int_a^x f(t)g(t)dt$$, $$\displaystyle h_n(x)=\int_a^x f_n(t)g(t)dt, ~ x\in [a,b]$$
>
> 則可得$$h_n \rightarrow h$$在閉區間$$[a,b]$$一致收斂。
