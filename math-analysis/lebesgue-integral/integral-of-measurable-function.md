# 一般可測函數的積分

## 可測函數的積分

> def: 可積分函數(以非負可積函數定義)
>
> $$f(x): E \rightarrow \mathbb{R}, ~ E \subseteq \mathbb{R}^n$$是可測函數，若積分：$$\displaystyle \int_E f^{+}(x) dx, \int_E f^{-}(x)dx$$至少有一個是有限值時，則定義$$\displaystyle \int_E f(x) dx = \int_E f^{+}(x) dx - \int_E f^{-}(x)dx$$為$$f$$在集合$$E$$上的積分。
>
> 如果$$f^{+}$$與$$f^{-}$$均為可積分函數時，則稱$$f$$為在$$E$$上可積分函數。
>
> 定義在$$E$$上可積分函數的集合為$$L(E)$$
>
>
>
> def: 可積分函數(以Cauchy in mean函數序列定義)。
>
> $$f(x): E \rightarrow \mathbb{R}, ~ E \subseteq \mathbb{R}^n$$是可測函數，若存在可測(一般)簡單函數$$\{f_n(x)\}$$滿足以下條件時，稱$$f$$在$$E$$可積分：
>
> 1. $$\{f_n(x)\}$$為Cauchy sequence in mean，即$$\displaystyle \lim_{n,m \rightarrow \infty}\int_E |f_n(x) - f_m(x)|dx=0$$。
> 2. $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) \text{ a.e.}$$(弱化為測度收斂也成立)。

* 因為$$|f|=f^{+} + f^{-}$$，因此在$$f$$可測的條件下，$$f$$可積分$$\Leftrightarrow$$$$|f|$$可積分。
* $$f$$可積分時，可得$$\displaystyle \left|\int_E f(x) dx \right| \leq \int_E |f(x)|dx$$。

## 有界可測函數在有限測度集合可積分

> $$f$$在集合$$E$$為有界可測函數($$\exists 0 \leq M < \infty \ni |f(x)|\leq M, ~\forall x \in E$$)，且$$m(E) < \infty$$，則$$f \in L(E)$$。

## 控制收斂定理(dominated control theorem, DCT)

> 給定可積分函數序列$$f_k \in L(E), ~ k \in \mathbb{N}$$，且函數序列點態(或幾乎處處)收斂: $$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x) \text{ a.e.} x \in E$$。
>
> 若存在$$E$$上的可積分函數$$F(x)$$滿足$$|f_k(x)| \leq F(x) \text{ a.e. } ~ x \in E, ~ k \in \mathbb{N}$$，
>
> 則：$$\displaystyle  \lim_{k \rightarrow \infty} \int_E |f_k(x) - f(x)|dx \Rightarrow  \lim_{k \rightarrow \infty} \int_E f_k(x) = \int_E f(x)dx$$。
>
> 註：通常稱$$F(x)$$為函數序列$$\{f_k(x)\}$$的控制函數。

<details>

<summary>proof:使用Reverse Fatou's lemma得函數序列積分的上極限為0</summary>

proof :

因為$$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x) \text{ a.e.} x \in E$$，所以$$f$$為可測函數。

且由$$|f_k(x)| \leq F(x) \text{ a.e. } ~ x \in E, ~ k \in \mathbb{N}$$，可得$$|f(x)| \leq F(x) ~ \text{a.e.} x \in E$$。

由於$$|f|=f^{+}+f^{-}$$且\[非負可測函數若被可積函數控制(dominated)時為可積分函數]，可得$$f$$

為$$E$$上的可積分函數。

由三角不等式得$$|f-f_k| \leq |f|+|f_k| \leq 2F$$且點態收斂得$$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x) \text{ a.e.} \Rightarrow \lim_{k \rightarrow \infty} |f_k(x) - f(x)| = 0 \text{ a.e.} \Rightarrow \limsup_{k \rightarrow \infty} |f_k(x) - f(x)| = 0 \text{ a.e.}$$

因為$$f_k, f$$均可積分，由積分線性性質與單調性得：

$$\displaystyle \left| \int_E f dx -\int_E f_k dx  \right|  = \left| \int_E (f-f_k) dx  \right| \leq \int_E |f-f_k|dx$$

由Reverse Fatou's lemma得：$$\displaystyle \limsup_{n \rightarrow \infty} \int_E |f-f_k| dx \leq \int_E \limsup_{k \rightarrow \infty} |f-f_k|dx = 0$$

因此$$\displaystyle \limsup_{n \rightarrow \infty} \int_E |f-f_k| dx=0$$，得積分存在且為0，即$$\displaystyle \lim_{n \rightarrow \infty} \int_E |f-f_k| dx=0$$

由於$$\displaystyle \lim_{k \rightarrow \infty}\left| \int_E f dx -\int_E f_k dx  \right|  \leq \lim_{k \rightarrow \infty}  \int_E |f-f_k|dx = 0$$

可得：$$\displaystyle \lim_{k \rightarrow \infty} \int_E f dx =\int_E f_k dx$$ (QED)

</details>

