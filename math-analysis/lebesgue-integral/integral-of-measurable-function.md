# 一般可測函數的積分

## 可測函數的積分

> def: $$f(x): E \rightarrow \mathbb{R}, ~ E \subseteq \mathbb{R}^n$$是可測函數，若積分：$$\displaystyle \int_E f^{+}(x) dx, \int_E f^{-}(x)dx$$至少有一個是有限值時，則定義$$\displaystyle \int_E f(x) dx = \int_E f^{+}(x) dx - \int_E f^{-}(x)dx$$為$$f$$在集合$$E$$上的積分。
>
> 如果$$f^{+}$$與$$f^{-}$$均為可積分函數時，則稱$$f$$為在$$E$$上可積分函數。
>
> 定義在$$E$$上可積分函數的集合為$$L(E)$$。

* 因為$$|f|=f^{+} + f^{-}$$，因此在$$f$$可測的條件下，$$f$$可積分$$\Leftrightarrow$$$$|f|$$可積分。
* $$f$$可積分時，可得$$\displaystyle \left|\int_E f(x) dx \right| \leq \int_E |f(x)|dx$$。

## 有界可測函數在有限測度集合可積分

> $$f$$在集合$$E$$為有界可測函數($$\exists 0 \leq M < \infty \ni |f(x)|\leq M, ~\forall x \in E$$)，且$$m(E) < \infty$$，則$$f \in L(E)$$。

## 控制收斂定理(dominated control theorem, DCT)

> 給定可積分函數序列$$f_k \in L(E), ~ k \in \mathbb{N}$$，且函數序列點態(或幾乎處處)收斂: $$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x) \text{ a.e.} x \in E$$。
>
> 若存在$$E$$上的可積分函數$$F(x)$$滿足$$|f_k(x)| \leq F(x) \text{ a.e. } ~ x \in E, ~ k \in \mathbb{N}$$，
>
> 則：$$\displaystyle \lim_{k \rightarrow \infty} \int_E f_k(x) = \int_E f(x)dx$$。
>
> 註：通常稱$$F(x)$$為函數序列$$\{f_k(x)\}$$的控制函數。



