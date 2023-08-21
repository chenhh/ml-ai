# 可測簡單函數

## 非負可測簡單函數

> 定義：非負可測簡單函數
>
> 函數$$f(x): \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$為非負可測簡單函數，其定義域在分集合$$E_i \subseteq \mathbb{R}^n,~i=1,2,\dots, p$$分別為取值為$$c_i$$：
>
> $$\displaystyle f(x)=\sum_{i=1}^p c_i \chi_{E_i}(x)$$，$$\bigcup_{i=1}^p E_i = \mathbb{R}^n$$，$$E_i \cap E_j = \emptyset, ~\forall i \neq j$$。

<mark style="color:blue;">由定義可知簡單函數為值域個數為有限值的函數</mark>。

> 定義：非負可測簡單函數的積分
>
> 給定歐式空間上的σ域$$\Sigma$$，若集合$$E \in \Sigma$$，定義非負簡單函數在$$E$$的積分為：
>
> $$\displaystyle \int_E f(x) dx \equiv \sum_{i=1}^p c_i m(E \cap E_i)$$。
>
> 其中$$dx$$是$$\mathbb{R}^n$$上Lebesgue測度的標誌。
>
> 此處定義$$0 \cdot \infty = 0$$。

### 範例：Dirichlet函數的積分

$$\displaystyle  f(x)=\chi_{\mathbb{Q}}(x)=  \left\{ \begin{aligned} & 1,& ~ x \in \mathbb{Q} \\ & 0,& ~ x \notin \mathbb{Q}  \end{aligned} \right.$$

因此值域取值為0(無理數)或1(有理數)。而有理數集合為可數集，因此其測度為$$m(\mathbb{Q})=0$$，無理數集合的測度為$$\infty$$。

可得積分為$$\int_\mathbb{R} f(x)dx = 0 \cdot \infty + 1 \cdot 0 = 0$$。







##
