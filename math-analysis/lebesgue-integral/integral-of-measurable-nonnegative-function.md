---
description: The Lebesgue integral of a measurable nonnegative function
---

# 非負可測函數的積分

## 非負可測函數的積分

> 函數$$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數，定義函數$$f$$在集合$$E$$上的積分為：$$\displaystyle \int_E f(x)dx = \sup_{h(x) \leq f(x), \forall x \in E} \left\{  \int_E h(x)dx ~| ~ h(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+} \text{ is simple non-negative function } \right\}$$此處定義的積分值可為$$\infty$$。
>
> <mark style="color:red;">若</mark>$$\displaystyle \int_E f(x)dx < \infty$$<mark style="color:red;">，則稱</mark>$$f$$<mark style="color:red;">在集合</mark>$$E$$<mark style="color:red;">可積，或稱</mark>$$f(x)$$<mark style="color:red;">為集合</mark>$$E$$<mark style="color:red;">上的可積函數</mark>。

此處[非負可測函數是用簡單函數$$h(x)$$逼近](../measure/simple-function-approximation.md)。

由切非負簡單函數的值域，當值域切的越細時，$$h(x)$$能夠越接近$$f(x)$$，此時積分值也會隨之變大，當切分到極限時，若簡單函數的積分值有限時，則$$f$$為可積分函數。

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

### 非負可測且值域有限的函數在有限測度集合上可積分

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

### 非負可測函數於可測子集的積分

> $$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數。
>
> 若$$A \subseteq E$$為可測子集合，則可得：$$\displaystyle \int_A f(x) dx = \int_E f(x) \chi_A(x) dx$$。
>
> 注意：此處積分值可能為$$\infty$$，即$$f$$可能在集合$$A$$上非可積分函數。

<details>

<summary>proof</summary>

令$$h(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$為非負簡單函數，且$$h(x) \leq f(x)~ \forall x \in A$$。

由積分定義得$$\displaystyle \int_A f(x) dx = \sup_{h(x) \leq f(x), ~ \forall x \in A} \int_A h(x) dx$$

因為$$\displaystyle  \chi_A(x)= \left\{ \begin{aligned} 1 &, \text{ if } x \in A, \\ 0 &, \text{ if } x \notin A, \end{aligned} \right.$$，

因此可改寫為$$\displaystyle \begin{aligned}  \sup_{h(x) \leq f(x), ~ \forall x \in A} \int_A h(x) dx & =  \sup_{h(x)\chi_A(x) \leq f(x)\chi_A(x), ~ \forall x \in E} \int_A h(x) dx \\ & = \int_E f(x)\chi_A(x) dx  \end{aligned}$$

(QED)

</details>

### 非負可測函數幾乎處處為0若且唯若積分值為0

> $$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可測函數。
>
> 可得$$f(x) = 0, \text{ a.e. on } E$$$$\Leftrightarrow$$$$\displaystyle \int_E f(x)dx =0$$。
>
> 註：$$f(x) = 0, \text{ a.e. on } E$$即$$\exists F \subseteq E \ni f(x)=0, \forall x \in E-F$$且$$m(F)=0$$。

<details>

<summary>proof</summary>

\=>

令$$h(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$為非負簡單函數，且$$h(x) \leq f(x)~ \forall x \in E$$。

$$h(x)=\sum_{i=1}^p a_i \chi_{A_i}(x), ~ \bigcup_{i=1}^p A_i = E, ~ A_i \cap A_j = \emptyset ~ \forall i \neq j$$。

$$\displaystyle \int_E h(x) dx \equiv \sum_{i=1}^p a_i m(E \cap A_i)$$

因為$$\exists F \subseteq E \ni f(x)=0, \forall x \in E-F$$且$$m(F)=0$$。

可改寫為$$F \cup F^c = E$$。

由集合分配率得$$(F\cup F^c) \cap A = (F \cap A) \cup (F^c \cap A)$$且$$(F \cap A) \cap (F^c \cap A) = \emptyset$$

由測度定義得$$m((F \cap A) \cup (F^c \cap A)) = m(F \cap A) + m(F^c \cap A)$$

因為$$m(F)=0$$且$$m(F \cap A) \leq m(F)$$，所以$$m(F\cap A) = 0$$。

因此$$m((F \cap A) \cup (F^c \cap A)) = m(F^c \cap A)$$ -- (1)

由(1)可得$$\displaystyle \int_E h(x) dx = \int_{F \cup F^c} h(x) dx = \sum_{i=1}^p a_i m(F^c \cap A_i)$$--(2)

$$\displaystyle  \begin{aligned} \int_{F \cup F^c} f(x) dx & = \sup_{h(x) \leq f(x), ~ x \in E}\{ \int_{F \cup F^c} h(x) dx\}  \\  & = \sup_{h(x) \leq f(x), ~ x \in F^c}\{ \int_{F^c} h(x) dx\}    \end{aligned}$$--(3)

因為$$f(x) =0$$且$$h(x) \leq f(x) ~ \forall x \in F^c$$，因此可得(3) =0 (QED)

<=

令集合$$E_k = \{x \in E~|~ f(x) > 1/k\}$$。

可得$$\displaystyle \frac{1}{k} \cdot m(E_k) = \int_{E_k} \frac{1}{k} dx \leq \int_{E_k} f(x) dx \leq \int_E f(x)dx = 0$$

因此$$m(E_k)=0, k=1,2,\dots$$

因為$$\displaystyle \{x \in E ~|~ f(x) > 0\} = \bigcup_{k=1}^\infty E_k$$

由遞增集合序列的可測性得$$\displaystyle \lim_{k \rightarrow \infty }m(E_k) = m(\bigcup_{k=1}^\infty E_k)=0$$ (QED)

</details>

## 非負可積函數幾乎處處有限

> $$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$在集合$$E \subseteq \mathbb{R}^n$$為非負可積函數，即$$\displaystyle \int_E f(x)dx < \infty$$。
>
> 則$$f(x)$$在$$E$$幾乎處處有限，即$$\exists E \subseteq F \ni f(x) < \infty, ~\forall x \in E-F$$且$$m(F)=0$$。
>
> <mark style="color:blue;">註：簡單的說，如果函數可積分，則函數值為無窮大的定義域集合的測度必須為0</mark>。

<details>

<summary>proof: 遞減函數序列極限等於交集</summary>

令$$E_k=\{x \in E ~|~ f(x) > k\}$$

因為$$E_k \supseteq E_{k+1}$$為遞減集合序列，因此$$\displaystyle \lim_{k \rightarrow \infty} E_k = \{x \in E ~|~ f(x)=\infty\}=\bigcap_{k=1}^\infty E_k$$.&#x20;

對於每個$$k$$，可得不等式$$\displaystyle k \cdot m(E_k) \leq \int_{E_k} f(x) dx \leq \int_E f(x) dx < \infty$$

因此可得$$\displaystyle \lim_{k \rightarrow \infty }m(E_k)=0$$ (QED)

</details>

## Beppo Levi非負遞增函數序列的積分

> 令非負可測且在集合$$E$$上遞增的函數序列$$f_1(x) \leq f_2(x) \leq \dots \leq f_k(x) \leq \dots~, \forall x \in E$$.，
>
> 且函數序列(點態)收斂：$$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x), ~ \forall x \in E$$，
>
> 則可得$$\displaystyle \lim_{k \rightarrow \infty} \int_E f_k(x) dx = \int_E f(x)dx$$。
>
>
>
> <mark style="color:red;">註：對於非負可測函數序列，極限與積分的次序可交換</mark>。
>
>
