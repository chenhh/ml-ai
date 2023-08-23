# 簡單函數逼近可測函數

## 相關筆記

[集合的特徵函數](../set/characteristic-function.md)。

## 特徵(指示)函數為可測函數

> 集合$$E$$的特徵(指示)函數為$$\chi_E(x)\equiv \mathbb{I}_E(x)= \left\{ \begin{aligned} &1 ~ \text{ if } x \in E, \\ &0 ~ \text{ if } x \notin E \end{aligned} \right.$$
>
> 則$$E$$為可測集合$$\Leftrightarrow \chi_E$$為可測函數。

<details>

<summary>proof: 以定義直接證明</summary>

proof =>:

取$$S \in \mathbb{B}(\mathbb{R})$$，可得$$\chi_E^{-1}(S) = \left\{ \begin{aligned} & X,~ \text{ if } 0, 1 \in S, \\ & E,~ \text{ if } 1 \in S, ~ 0 \notin S, \\ & E^c,~ \text{ if } 1 \notin S, ~ 0 \in S, \\ & \empty, ~ \text{ otherwise } \end{aligned} \right.$$

也可用$$\chi_E^{-1}((-\infty, c))= \left\{ \begin{aligned} & \empty,~ \text{ if } c < 0, \\ & E^c,~ \text{ if } 0 \leq c < 1, \\ & E \cup E^c,~ \text{ if } c \geq 1, \end{aligned} \right.$$

因為$$X, E, E^c, \empty \in \Sigma$$，所以$$\chi_E$$為可測函數 (QED)。

proof <=:

$$\chi_E^{-1}((1/2, \infty))=\{ x\in X ~|~ \chi_{E}(x) > 1/2 \}=E \in \Sigma$$ (QED)

</details>

### 集合序列上極限的特徵函數(可穿過limsup符號)

> 令$$\{E_n\}$$為集合序列，且$$\displaystyle E^{*}=\limsup_{n \rightarrow \infty} E_n \equiv \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k$$，則：
>
> $$\displaystyle \chi_E^{*}(x)=\limsup_{n \rightarrow \infty} \chi_{E_n}(x)$$

## 簡單函數(simple function)

> 令$$f: E \rightarrow \mathbb{R}, ~ E \subseteq \mathbb{R}^n$$，若$$S=\{y \in \mathbb{R}~|~ y=f(x), x \in E\}$$為有限集合時，則稱$$f$$為集合$$E$$上的簡單函數。
>
> <mark style="color:red;">註：簡單函數就是值域為有限取值的函數。例如離散型的隨機變數</mark>。

若$$f$$為$$E$$上的簡單函數時，可將集合$$E$$切為$$p$$個分割$$E_1, \dots, E_p, ~ E_i \cap E_j = \emptyset$$。

且$$f(x) = c_i, \forall x \in E_i$$，則可得$$\displaystyle f(x)=\sum_{i=1}^p c_i \chi_{E_i}(x), ~x \in E$$。

### 簡單函數的性質

> $$f,g$$為集合$$E$$的簡單函數：
>
> * $$f(x) \pm g(x)$$為$$E$$的簡單函數。
> * $$f(x)g(x)$$為$$E$$的簡單函數。
> * 若$$E_i, i=1,2,\dots, p$$均為可測集合，則$$f$$為可測函數。

## 遞增可測簡單函數逼近非負可測函數

> $$f: E \rightarrow \mathbb{R}^{+}$$為非負可測函數，則存在遞增非負可測簡單函數序列：$$h_k(x) \leq h_{k+1}(x), k \in \mathbb{N}$$ 使得：$$\displaystyle \lim_{k \rightarrow \infty }h_k(x) =f(x), ~ x \in E$$
>
> <mark style="color:red;">註：此處簡單函數逼近切</mark>$$f$$<mark style="color:red;">的值域(但可能有無限多個值)</mark>。

<details>

<summary>proof</summary>

$$\forall k \in \mathbb{N}$$，可將閉區間$$[0,k]$$分為$$k \cdot 2^k$$等長區間。

令其中第$$j$$個區間為$$E_{k,j}=\{x \in E ~|~ \frac{j-1}{2^k} \leq f(x) < \frac{j}{2^k}\}, j=1,2,\dots, k2^k$$。

而函數值大於等於$$k$$的區間記為$$E_k=\{x \in E ~|~ f(x) \geq k\}$$。

取函數序列：$$\displaystyle  	h_k(x)=\left\{ 	\begin{aligned} 	&\frac{j-1}{2^k}, & x \in E_{k,j} \\ 	&k, & x \in E_k 	\end{aligned} 	\right. 	~j=1,2,\dots, k2^k, ~ k \in \mathbb{N}$$。





</details>

## 可測簡單函數逼近可測函數

> $$f: E \rightarrow \mathbb{R}$$為可測函數，則存在可測簡單函數序列$$\{h_k(x)\}$$使得$$|h_k(x)| \leq |f(x)|$$且有 $$\displaystyle \lim_{k \rightarrow \infty} h_k(x) = f(x), ~ x \in E$$。
>
> 若$$f(x) < \infty$$，則上述為均勻(一致)收斂，即$$\displaystyle \sup_{x\in E}\{f_k(x) \neq f(x)\}=0$$。

