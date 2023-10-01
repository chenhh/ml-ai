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

##

##

## 有界可測函數在有限測度集合可積分

> $$f$$在集合$$E$$為有界可測函數($$\exists 0 \leq M < \infty \ni |f(x)|\leq M, ~\forall x \in E$$)，且$$m(E) < \infty$$，則$$f \in L(E)$$。

## 可積分函數性質

> 給定$$f,g: E \rightarrow \mathbb{R}$$為可測函數，若：
>
> 1. $$(f^2+g^2)^{1/2}$$為可積分函數，則$$f,g$$為可積分函數。
> 2. 若$$f^2, g^2$$為可積分函數，則$$fg$$為可積分函數。
> 3. 若$$f,g$$為可積分函數，則$$\max(f,g)$$與$$\min(f,g)$$為可積分函數。

## 控制收斂定理(dominated control theorem, DCT)

> 給定可積分函數序列$$f_k \in L(E), ~ k \in \mathbb{N}$$，且函數序列點態(或幾乎處處、測度)收斂: $$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x) \text{ a.e.} x \in E$$。
>
> 若存在$$E$$上的可積分函數$$F(x)$$滿足$$|f_k(x)| \leq F(x) \text{ a.e. } ~ x \in E, ~ k \in \mathbb{N}$$，
>
> 則：$$\displaystyle  \lim_{k \rightarrow \infty} \int_E |f_k(x) - f(x)|dx \Rightarrow  \lim_{k \rightarrow \infty} \int_E f_k(x) = \int_E f(x)dx$$。
>
> 註：通常稱$$F(x)$$為函數序列$$\{f_k(x)\}$$的控制函數。
>
> <mark style="color:green;">也稱為Bounded convergence theorem, BCT</mark>。

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

## 可測函數若幾乎處處被可積函數控制則可積分

> 令$$f,g: E \rightarrow \mathbb{R}$$為可測函數，若$$|f| \leq g \text{ a.e. }$$且$$g$$在$$E$$可積分($$\int_E g(x)dx < \infty$$)，則$$f$$在$$E$$可積分($$\int_E f(x)dx < \infty$$)

## 本性(本質)有界函數(essentially bounded function)

> $$f: E \rightarrow \mathbb{R}$$稱為本性有界函數，若存在常數$$c < \infty$$使得函數幾乎處處有界$$|f(x)| \leq c, ~ x \in E$$。$$c$$稱為函數$$f$$在$$E$$的本性上界(essential upper bound)。
>
> 本性上界集合中的最大下界稱為函數$$f$$在$$E$$的本性上確界，即$$\displaystyle  \begin{aligned} \mathrm{ess} \sup_{x \in E} |f| &= \inf\{ c \in \mathbb{R}~|~ m(\{x ~|~ |f(x)| > c\})=0\} \\ &	= \inf\{ c \in \mathbb{R}~|~ m(f^{-1}(c, \infty) \cup f^{-1}(-\infty, -c))=0\} \end{aligned}$$。
>
> 若為空集時則$$\displaystyle  \mathrm{ess}\sup_{x \in E} |f| = \emptyset$$。
>
> [\[Lp空間\]詳細討論](../lp-space/#ben-xing-ben-zhi-you-jie-han-shu-essentially-bounded-function)。

## 可積分函數與可測且本性有界函數的乘積為可積分函數

> $$f$$為可積分函數且$$g$$為可測且本性有界函數，則$$fg$$為可積分函數。

因為$$|fg| \leq c |f| \text{ a.e. }$$且$$c|f|$$可積分，由DCT可得$$fg$$可積分。

## 可測且本性有界函數若集合測度有限則可積分

> $$f: E \rightarrow \mathbb{R}$$為可積分函數且在$$F \subseteq E$$本性有界。若$$m(F) < \infty$$，則$$\displaystyle \int_F f(x) dx < \infty$$。

因為函數$$|\chi_F f | \leq c \chi_F$$且$$c < \infty$$，$$c\chi_F$$為可積分函數，由\[可測函數若幾乎處處被可積函數控制則可積分]得$$f$$在$$F$$可積分。



