---
description: >-
  The Lebesgue integral of a bouned measurable function over a set of finite
  measure
---

# 2.a有界可測函數在有限測度集的積分

## 簡介

包含了有界可測簡單函數與一般函數的積分。

## (可測)簡單函數

> 可測實數值簡單函數$$f: E \rightarrow \mathbb{R}$$具有有限個相異的函數值$$c_1, c_2, \dots, c_n$$可表示成：
>
> $$f(x) = \sum_{i=1}^n c_i \chi_{E_i}(x)$$，$$E_i = f^{-1}(c_i)=\{x \in E ~|~ f(x)=c_i\}$$。
>
> 註：此處$$c_i \in \mathbb{R} \equiv (-\infty, \infty)$$，因此$$f(x)\neq \infty, ~\forall x \in E$$。<mark style="color:red;">但</mark>$$f(x)$$<mark style="color:red;">不一定有界</mark>。

<mark style="color:blue;">由於函數的定義為一對一或多對一，因此給定</mark>$$c_i \neq c_j$$<mark style="color:blue;">的前像</mark>$$f^{-1}(c_i) \cap f^{-1}(c_j)=\emptyset$$<mark style="color:blue;">必定會得到互斥的前像</mark>。

## 簡單函數在有限測度集的積分

> 給定可測實數值簡單函數$$f: E \rightarrow \mathbb{R}$$，若$$E$$為有限測度集，即$$m(E)<\infty$$，則定義積分$$\displaystyle \int_E f = \sum_{i=1}^n c_i m(E_i)$$。

因為$$c_i \in \mathbb{R}, \forall i$$且$$m(E)<\infty$$，因此可得$$\displaystyle \int_E f<\infty$$必定可積分。

## 積分的線性與單調性

> 令可測實數值簡單函數$$f,g: E \rightarrow \mathbb{R}$$且$$E$$為有限測度集，即$$m(E)<\infty$$，則$$\forall a, b\in \mathbb{R}$$：
>
> * $$\displaystyle \int_E (af+bg)=a\int_E f + b \int_E g$$。
> * 若$$f \leq g$$ on $$E$$，則$$\displaystyle \int_E f \leq \int_E g$$

<details>

<summary>proof: 將<span class="math">E</span>做分割，以f,g在分割的取值得證。</summary>

proof 1: 線性

因為$$f,g$$為簡單函數，在$$E$$上為有限個取值。

將集合$$E$$做$$n$$個分割，令$$E_i=\{x \in E~|~ f(x)=c_i\}=\{x \in E ~|~ g(x)=d_i\}$$

則$$E_i \cap E_j=\emptyset, ~\bigcup_{i=1}^n E_i=E$$。

可得$$\displaystyle \int_E f = \sum_{i=1}^n c_i m(E_i)~ \int_E g = \sum_{i=1}^n d_i m(E_i)$$。

因此$$\begin{aligned} \displaystyle \int_E (af+bg) & =\sum_{i=1}^n (ac_i + bd_i) m(E_i) \\  & = a \sum_{i=1}^n c_i m(E_i) + b \sum_{i=1}^n d_i m(E_i) \\ & = \int_E f + b \int_E g   \end{aligned}$$

(QED)

proof: 單調性

因為$$f \leq g$$ on $$E$$，令$$h =g-f\geq 0$$ on $$E$$。

則由線性得$$\displaystyle \int_E g - \int_E f = \int_E g-f = \int_E h \geq 0$$

(QED)

</details>

## 有界實值函數在有限測度集的積分

> 定義：有界實值函數在有限測度集的上/下積分
>
> $$f: E \rightarrow \mathbb{R}$$，$$f$$有界(即$$\exists M\geq 0 \ni |f(x)|\leq M, ~\forall x \in E$$)且$$E$$為有限測度集，即$$m(E)<\infty$$。
>
> 定義上/下Lebesgue積分：
>
> * $$\displaystyle \overline{\int_E f}=\sup \left\{ \int_E h ~|~ h\text{ is simple and } h \leq f \text{ on } E\right\}$$。
> * $$\displaystyle \underline{\int_E f}=\inf \left\{ \int_E h ~|~ h\text{ is simple and } f \leq h \text{ on } E\right\}$$。
>
> <mark style="color:red;">因為</mark>$$f$$<mark style="color:red;">是有界函數，因此上/下積分存在</mark>，且由簡單積分單調性得：$$\displaystyle -\infty<\underline{\int_E f} \leq \overline{\int_E f} < \infty$$。
>
> <mark style="color:red;">定義：有界實值數在有限測度集的積分</mark>
>
> 有界實值函數$$f$$在有限測度集$$E$$為Lebesgue可積分若且唯若其上積分等於下積分。
>
> $$\displaystyle m(E)<\infty,~ \int_E f<\infty \Leftrightarrow \underline{\int_E f} = \overline{\int_E f}$$

### 有界實值函數定義在閉有界區間則Riemann積分值等於Lebesgue積分值

> $$f: [a,b] \rightarrow \mathbb{R}$$且$$f$$有界。
>
> 若$$f$$在閉區間$$[a,b]$$Riemann可積，則$$f$$在閉區間$$[a,b]$$Lebesgue可積。
>
> 註：反之不一定成立。

### 有界可測實值函數若定義在有限測度集則必定可積分

> $$f: E \rightarrow \mathbb{R}$$為可測函數，$$f$$有界(即$$\exists M\geq 0 \ni |f(x)|\leq M, ~\forall x \in E$$)且$$E$$為有限測度集，即$$m(E)<\infty$$。
>
> 則$$f$$必定可積分，即$$\displaystyle \int_E f < \infty$$。
>
> <mark style="color:blue;">註：可測函數不可省略，因並非所有有界實值函數都可積分</mark>。

<details>

<summary>proof</summary>

令$$n \in \mathbb{N}$$，由\[一般函數可測若且唯若存在可測簡單函數逼近一般函數(the simple approximation theorem)]令$$\epsilon=1/n$$，則存在兩個定義在$$E$$簡單函數$$h_n,g_n$$m滿足：$$h_n \leq f \leq g_n \text{ on } E$$且$$0 \leq g_n -h_n \leq 1/n \text{ on } E$$。

由簡單函數積分的單調性與線性得：$$\displaystyle 0 \leq \int_E g_n - \int_E h_n =\int_E (g_n-h_n) \leq 1/n \cdot m(E)$$

由上積分與下積分定義得：

$$\displaystyle 0 \leq  \inf\left\{ \int_E g | g \text{ simple, and } g \geq f \right\} -  \sup\left\{ \int_E h | h \text{ simple, and } h \leq  f\right\}  \leq \int_E g_n - \int_E h_n \leq 1/n \cdot m(E)$$

上述不等式在$$\forall n \in \mathbb{N}$$且$$m(E) <\infty$$成立。

(QED)

</details>

## 積分線性與單調性

> $$f,g: E \rightarrow \mathbb{R}$$為有界可測實值函數，且定義域$$E$$的測度有限，即$$m(E)<\infty$$，則$$\forall a,b \in \mathbb{R}$$：
>
> * $$\displaystyle \int_E (af+bg) = a\int_E f + b \int_E g$$。
> * 若$$f \leq g \text{ on } E$$，則$$\displaystyle \int_E f \leq \int_E g$$。

## 互斥集合積分的可加性

> $$f: E \rightarrow \mathbb{R}$$為有界可測實值函數，且定義域$$E$$的測度有限，即$$m(E)<\infty$$。
>
> 若$$A,B \subseteq E$$且$$A \cap B = \emptyset$$，則：$$\displaystyle \int_{A \cup B} f = \int_A f + \int_B f$$。

## 函數積分的絕對值小於等於函數絕對值的積分

> $$f: E \rightarrow \mathbb{R}$$為有界可測實值函數，且定義域$$E$$的測度有限，即$$m(E)<\infty$$。
>
> 則：$$\displaystyle \left| \int_E f \right| \leq \int_E |f|$$。

## 函數序列一致收斂則積分序列也收斂

> $$f_n: E \rightarrow \mathbb{R}, ~ n \in \mathbb{N}$$為有界可測實值函數序列，且定義域$$E$$的測度有限，即$$m(E)<\infty$$。
>
> 若$$\{f_n\} \rightarrow f \text{ unif. on } E$$ ($$\displaystyle \lim_{n \rightarrow \infty} \sup_{x \in E}|f_n(x) - f(x)|=0$$)，則$$\displaystyle \lim_{n \rightarrow \infty} \int_E f_n = \int_E f$$。
>
> 註：之後會證明在pointwise a.e. 條件下，積分序列也會收斂。

## The bounded convergence theorem

> $$f_n: E \rightarrow \mathbb{R}, ~ n \in \mathbb{N}$$為有界可測實值函數序列，且定義域$$E$$的測度有限，即$$m(E)<\infty$$。
>
> 令$$\{f_n\}$$在集合$$E$$一致有界，即$$\exists M \geq 0 \ni |f_n(x)| \leq M, ~\forall x \in E, ~ \forall n$$。
>
> 若點態收斂 $$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=f(x) \text{ on } E$$，則$$\displaystyle \lim_{n \rightarrow \infty} \int_E f_n(x) = \int_E f(x)$$。



## 參考資料

