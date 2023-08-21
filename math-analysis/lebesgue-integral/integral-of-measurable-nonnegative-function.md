---
description: The Lebesgue integral of a measurable nonnegative function
---

# 非負可測函數的積分

## 非負可測函數的積分

> 函數$$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數，定義函數$$f$$在集合$$E$$上的積分為：$$\displaystyle \int_E f(x)dx = \sup_{h(x) \leq f(x), \forall x \in E} \left\{  \int_E h(x)dx ~| ~ h(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+} \text{ is simple non-negative function } \right\}$$此處定義的積分值可為$$\infty$$。
>
> <mark style="color:red;">若</mark>$$\displaystyle \int_E f(x)dx < \infty$$<mark style="color:red;">，則稱</mark>$$f$$<mark style="color:red;">在集合</mark>$$E$$<mark style="color:red;">可積，或稱</mark>$$f(x)$$<mark style="color:red;">為集合</mark>$$E$$<mark style="color:red;">上的可積函數</mark>。

此處是由切非負簡單函數的值域，當值域切的越細時，$$h(x)$$能夠越接近$$f(x)$$，此時積分值也會隨之變大，當切分到極限時，若簡單函數的積分值有限時，則$$f$$為可積分函數。

### 非負可測函數若被可積函數控制時為可積分函數

> $$f(x), g(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數。
>
> 若$$f(x) \leq g(x) ~ \forall x \in E$$，則$$\displaystyle \int_E f(x) dx \leq \int_E g(x) dx$$。
>
> 注意：此處積分值可能為$$\infty$$。即$$f(x), g(x)$$可能不是可積分函數。
>
> <mark style="color:red;">如果</mark>$$g(x)$$<mark style="color:red;">為</mark>$$E$$<mark style="color:red;">的可積分函數，則</mark>$$f(x)$$<mark style="color:red;">為</mark>$$E$$<mark style="color:red;">的可積分函數</mark>。

<details>

<summary>proof</summary>



令$$h(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$為非負簡單函數，且$$h(x) \leq f(x)~ \forall x \in E$$。

則由$$f(x) \leq g(x)$$可得$$h(x) \leq g(x) ~ \forall x \in E$$。

由積分定義得$$\displaystyle \int_E h(x) \leq \int_E g(x) dx$$。

而$$\displaystyle \int_E f(x) dx = \sup_{h(x) \leq f(x)}\{ \int_E h(x) dx\} \leq \int_E g(x) dx$$

如果$$g(x)$$在$$E$$可積分，依定義得$$\int_E g(x) dx < \infty$$，因此$$\int_E f(x) dx < \infty$$，即$$f(x)$$在$$E$$可積分 (QED)。

</details>

## 非負可測且值域有限的函數在有限測度集合上可積分

> $$f(x), g(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數。
>
> <mark style="color:red;">如果</mark>$$f(x)$$<mark style="color:red;">在</mark>$$E$$<mark style="color:red;">有界，且</mark>$$m(E) < \infty$$<mark style="color:red;">，則</mark>$$f(x)$$<mark style="color:red;">為</mark>$$E$$<mark style="color:red;">的可積分函數(有限值域的函數在有限測度集合可積分)</mark>。

<details>

<summary>proof</summary>

簡單函數$$h(x)=\sum_{i=1}^p a_i \chi_{A_i}(x), ~ \bigcup_{i=1}^p A_i = E, ~ A_i \cap A_j = \emptyset ~ \forall i \neq j$$

如果$$f(x)$$在$$E$$上有界，則簡單函數$$h(x)$$的在$$E$$的值域有上界，即$$a_i < \infty, \forall i$$。

因為積分值為$$\displaystyle \int_E h(x) dx \equiv \sum_{i=1}^p a_i m(E \cap A_i)$$

當$$m(E) < \infty$$且$$a_i< \infty$$時，可保證$$\displaystyle \int_E h(x) dx < \infty$$。

因此可得$$\displaystyle \int_E f(x) dx = \sup_{h(x) \leq f(x)}{ \int_E h(x) dx} < \infty$$ (QED)

</details>
