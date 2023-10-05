---
description: >-
  The Lebesgue integral of a bouned measurable function over a set of finite
  measure
---

# 2.a有界可測函數在有限測度集的積分

## 簡介

包含了有界可測簡單函數與一般函數的積分。

## 簡單函數

> 可測實數值簡單函數$$f: E \rightarrow \mathbb{R}$$具有有限個相異的函數值$$c_1, c_2, \dots, c_n$$可表示成：
>
> $$f(x) = \sum_{i=1}^n c_i \chi_{E_i}(x)$$，$$E_i = f^{-1}(c_i)=\{x \in E ~|~ f(x)=c_i\}$$。
>
> 註：此處$$c_i \in \mathbb{R} \equiv (-\infty, \infty)$$，因此$$f(x)\neq \infty, ~\forall x \in E$$。

由於函數的定義為一對一或多對一，因此給定$$c_i \neq c_j$$的前像$$f^{-1}(c_i) \neq f^{-1}(c_j)$$必定會得到互斥的前像。

## 簡單函數在有限測度集的積分

> 給定可測實數值簡單函數$$f: E \rightarrow \mathbb{R}$$，若$$m(E)<\infty$$，則定義積分$$\displaystyle \int_E f = \sum_{i=1}^n c_i m(E_i)$$。

因為$$c_i \in \mathbb{R}, \forall i$$且$$m(E)<\infty$$，因此可得$$\displaystyle \int_E f<\infty$$必定可積分。

## 積分的線性與單調性

> 令$$f,g: E \rightarrow \mathbb{R}$$且$$m(E)<\infty$$，則$$\forall a, b\in \mathbb{R}$$：
>
> * $$\displaystyle \int_E (af+bg)=a\int_E f + b \int_E g$$。
> * 若$$f \leq g$$ on $$E$$，則$$\displaystyle \int_E f \leq \int_E g$$

## 有界實值函數在有限測度集的積分

> 定義：有界實值函數在有限測度集的上/下積分
>
> $$f: E \rightarrow \mathbb{R}$$，$$f$$有界(即$$\exists M\geq 0 \ni |f(x)|\leq M, ~\forall x \in E$$)且$$m(E)<\infty$$。
>
> 定義上/下Lebesgue積分：
>
> * $$\displaystyle \overline{\int_E f}=\sup \left\{ \int_E h ~|~ h\text{ is simple and } h \leq f \text{ on } E\right\}$$。
> * $$\displaystyle \underline{\int_E f}=\inf \left\{ \int_E h ~|~ h\text{ is simple and } f \leq h \text{ on } E\right\}$$。
>
> 因為$$f$$是有界函數，因此上/下積分存在，且由簡單積分單調性得：$$\displaystyle \underline{\int_E f} \leq \overline{\int_E f} < \infty$$。
>
> <mark style="color:red;">定義：有界實值數在有限測度集的積分</mark>
>
> 有界實值函數$$f$$在有限測度集$$E$$為Lebesgue可積分若且唯若其上積分等於下積分。
>
> $$\displaystyle \int_E f<\infty \Leftrightarrow \underline{\int_E f} = \overline{\int_E f}$$

### 有界實值函數定義在閉有界區間則Riemann積分值等於Lebesgue積分值

> $$f: [a,b] \rightarrow \mathbb{R}$$且$$f$$有界。
>
> 若$$f$$在閉區間$$[a,b]$$Riemann可積，則$$f$$在閉區間$$[a,b]$$Lebesgue可積。
>
> 註：反之不一定成立。

### 有界可測實值函數若定義在有限測度集則必定可積分

> $$f: E \rightarrow \mathbb{R}$$為可測函數，$$f$$有界(即$$\exists M\geq 0 \ni |f(x)|\leq M, ~\forall x \in E$$)且$$m(E)<\infty$$。
>
> 則$$f$$必定可積分，即$$\displaystyle \int_E f < \infty$$。
>
> <mark style="color:blue;">註：可測函數不可省略，因並非所有有界實值函數都可積分</mark>。

## 參考資料

