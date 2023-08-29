---
description: convergence in measure
---

# 測度收斂

## 測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若
>
> $$\forall \epsilon > 0$$，可得$$\displaystyle \lim_{n \rightarrow \infty}\mu( x \in E ~|~ |f_n(x) - f(x)| > \epsilon) = 0$$
>
> 則稱$$\{f_n\}$$依測度收斂至函數$$f$$。
>
> <mark style="color:blue;">注意此處的limit符號是在測度外，表示不限特定集合。如果等號在測度內為a.e.收斂</mark>。

<mark style="color:red;">註：測度收斂強調的是不收斂的點形成的集合測度為0，而不要求所有函數序列有在相同的集合中不收斂</mark>。

## 測度收斂的唯一性

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若在$$E$$上依測度收斂至$$f(x)$$與$$g(x)$$，則$$f(x) = g(x)$$ a.e. $$\forall x \in E$$。

## 幾乎處處收斂可保證測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列且$$\mu(E) < \infty$$(有限測度空間)。
>
> 若$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) \text{ a.e. on } E$$且$$f$$幾乎處處有限，則$$\{f_n\}$$依測度收斂至$$f$$。

## 依測度Cauchy序列(Cauchy sequence in measure)

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若$$\forall \epsilon > 0$$，若
>
> $$\displaystyle \lim_{m,n \rightarrow \infty}\mu( x \in E ~|~ |f_m(x) - f_n(x)| > \epsilon) = 0$$，則稱$$\{f_n(x)\}$$為$$E$$上的依測度Cauchy序列。

