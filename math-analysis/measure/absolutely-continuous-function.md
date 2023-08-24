---
description: absolutely continuous function
---

# 絕對連續函數

## 絕對連續函數

> 定義：$$f: [a,b] \rightarrow \mathbb{R}$$為閉區間$$[a,b]$$上的絕對連續函數：
>
> $$\{[a_k, b_k]\}_{k=1}^n$$為$$[a,b]$$任意有限不相交的有限個開區間序列，$$(a_i, b_i) \cap (a_j, b_j )=\emptyset, ~\forall i \neq j$$。
>
> 若$$\displaystyle \forall \epsilon > 0, ~\exists \delta > 0 \ni \sum_{k=1}^n |b_k - a_k| < \delta \Rightarrow \sum_{k=1}^n |f(b_k) - f(a_k)|<\epsilon$$。

lipschitz條件⊆絕對連續函數⊆連續函數。

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

### 範例：絕對連續但不滿足Lipschitz條件的函數

$$f(x) = x^{1/2}$$
