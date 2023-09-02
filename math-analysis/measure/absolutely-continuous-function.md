---
description: absolutely continuous function
---

# 絕對連續函數

## 簡介

可微分函數為連續函數，但反之不成立。Lebesgue測度中證明了連續函數幾乎處處可微。

<mark style="color:blue;">而幾乎處處可微分函數中，有些函數在可微分的點導數值為0，但函數值不是常數(例如Cantor函數)，為了排除這一類函數，因此定義絕對連續函數</mark>。

絕對連續函數在機率空間中，可用於定義分佈函數(distribution function)與機率密度函數(probability density function)之間的關係。

[https://stats.stackexchange.com/questions/298293/absolutely-continuous-random-variable-vs-continuous-random-variable](https://stats.stackexchange.com/questions/298293/absolutely-continuous-random-variable-vs-continuous-random-variable)

## 絕對連續函數

> 定義：$$f: [a,b] \rightarrow \mathbb{R}$$為閉區間$$[a,b]$$上的絕對連續函數：
>
> $$\{[a_k, b_k]\}_{k=1}^n$$為$$[a,b]$$任意有限不相交的有限個開區間序列，$$(a_i, b_i) \cap (a_j, b_j )=\emptyset, ~\forall i \neq j$$。
>
> 若$$\displaystyle \forall \epsilon > 0, ~\exists \delta > 0 \ni \sum_{k=1}^n |b_k - a_k| < \delta \Rightarrow \sum_{k=1}^n |f(b_k) - f(a_k)|<\epsilon$$。

lipschitz條件⊆絕對連續函數⊆連續函數。

### 絕對連續函數類

* $$f$$在閉區間$$[a,b]$$ Lebesgue可積，則$$\displaystyle \int_{[a,b]} f(t)dt= F(x)$$為絕對連續函數。
* 在閉區間$$[a,b]$$滿足Lipschitz條件的函數。
* 在閉區間$$[a,b]$$導數有界的函數。
* 在閉區間$$[a,b]$$導數連續的函數。

### 滿足Lipschitz條件的函數為絕對連續函數

> $$f: [a,b] \rightarrow \mathbb{R}$$滿足Lipschitz條件，即$$\exists M \geq 0 \ni \forall x_1, x_2 \in [a,b], ~ |f(x_1) - f(x_2)| \leq M |x_1 - x_2|$$，則$$f$$在$$[a,b]$$絕對連續。
>
> [https://en.wikipedia.org/wiki/Lipschitz\_continuity](https://en.wikipedia.org/wiki/Lipschitz\_continuity)

<details>

<summary>proof</summary>

取$$[a,b]$$中任意有限個不相交的開區間$$(a_i, b_i), ~i=1,2,\dots, n$$。

由Lipschitz條件得$$\exists m_i \geq 0 \ni |f(a_i) - f(b_i)| \leq m_i|a_i - b_i|, ~ i=1,2,\dots, n$$

因此$$\forall \epsilon > 0$$ 取$$\delta = \frac{\epsilon}{\max(m_1, \dots, m_n)}$$，只要$$\sum_{i=1}^n |a_i -b_i| < \delta$$，

可得$$\sum_{i=1}^n |f(a_i - f(b_i)| \leq sum_{i=1}^m  |a_i - b_i| \leq \max(m_1, \dots ,m_n) \cdot \delta \leq \epsilon$$&#x20;

(QED)

</details>

#### 範例：絕對連續但不滿足Lipschitz條件的函數

$$f(x) = x^{1/2}$$

## 絕對連續函數是有界變差函數

\>

#### 範例：有界變差但非絕對連續函數

$$\displaystyle f(x) = \left\{ \begin{aligned} &0, &x = 0,\\ &x+1, &0 < x \leq 1 \end{aligned}  \right.$$，則$$f$$在$$[0,1]$$為單調遞增函數，因此為有界變差函數。

但$$f$$在$$0$$不連續，因此非絕對連續函數。

## 參考資料

* [https://zhuanlan.zhihu.com/p/545536763](https://zhuanlan.zhihu.com/p/545536763)
