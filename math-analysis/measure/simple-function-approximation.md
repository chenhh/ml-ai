# 簡單函數逼近可測函數

## 相關筆記

[集合的特徵函數](../set/characteristic-function.md)。

特徵函數在積分時，可將子集合轉換成函數計算。$$\int_E f\chi_{E_k} d\mu = \int_{E_k}fd\mu$$。

函數為實值函數與函數有界是不同概念，如$$x \in \mathbb{R}, ~f(x)=x$$為實值函數，但非不是有界函數。

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

## (可測)簡單函數(simple function)

> 令實值函數$$f: E \rightarrow \mathbb{R}$$，若$$S=\{y \in \mathbb{R}~|~ y=f(x), x \in E\}$$為有限集合時，$$E$$為可測集合且$$f$$為可測函數，則稱$$f$$為集合$$E$$上的簡單函數。
>
> 令$$f(x)$$的取值為$$c_1, c_2, \dots, c_n$$，且
>
> $$E_i =f^{-1}(c_i)=\{x \in E ~|~ f(x)=c_i\} \in \sigma(E)$$為可測集。可得$$c_i \neq c_j \Leftrightarrow E_i \cap E_j=\emptyset$$。且$$f$$為可測函數。
>
> <mark style="color:red;">註：定義在可測集上有限取值的函數為可測函數，才是簡單函數。</mark>
>
> 註：可測集合中的子集不一定是可測集。如實數為可測集，但Cantor集為不可測集。

若$$f$$為$$E$$上的簡單函數時，令$$f(x)$$的取值為$$c_1, c_2, \dots, c_n$$，可將集合$$E$$切為$$n$$個互斥分割$$E_1, \dots, E_n, ~ E_i \cap E_j = \emptyset$$。

$$E_i =f^{-1}(c_i)=\{x \in E ~|~ f(x)=c_i\}$$。

且$$f(x) = c_i, \forall x \in E_i$$，則可得$$\displaystyle f(x)=\sum_{i=1}^n c_i \chi_{E_i}(x), ~x \in E$$。

### 簡單函數的性質

> $$f,g$$為集合$$E$$的簡單函數：
>
> * $$f(x) \pm g(x)$$為$$E$$的簡單函數。
> * $$f(x)g(x)$$為$$E$$的簡單函數。
> * 若$$E_i, i=1,2,\dots, n$$均為可測集合，則$$f$$為可測函數。

## 存在可測簡單函數可夾擠有界可測實值函數

> 給定實值可測函數$$f: E \rightarrow \mathbb{R}$$且$$f$$有界(即$$\exists M\geq 0 \ni |f(x)|\leq M, ~ \forall x \in E$$)。
>
> 則$$\forall \epsilon >0$$，存在定義在集合$$E$$的可測簡單函數$$h_\epsilon,g_\epsilon$$滿足：
>
> $$h_\epsilon(x) \leq f(x) \leq g_\epsilon(x)$$且$$0 \leq g_\epsilon(x) - h_\epsilon(x) < \epsilon, ~\forall x \in E$$。
>
> <mark style="color:blue;">註：</mark>$$f$$<mark style="color:blue;">必須有界才能保證切值域時，兩點之間長度小於</mark>$$\epsilon$$ 。
>
> 因為函數$$f$$有界，因此將值域切$$n$$段，每段的長度均小於$$\epsilon$$。令其中第$$k$$段為$$I_k=[y_{k-1}, y_k)$$，取所有的$$y_{k-1}$$ 得簡單函數\$$\$$h\_\epsilon(x) = \sum\_{k=1}^n y\_{k-1} \chi\_{E\_k}(x)$$與$$g\_\epsilon(x) = \sum\_{k=1}^n y\_{k} \chi\_{E\_k}(x)$$夾擠$$f(x)\$$。

<details>

<summary>proof: 切割值域建立<span class="math">y_{k-1} \leq f(x) &#x3C;y_k</span>的簡單可測函數。</summary>

因為$$f$$為有界函數，令有界開區間包含函數值域，即$$f(E) \subseteq (c,d)$$且切割為$$c=y_0 < y_1<\dots<y_n=d$$。給定$$\epsilon > 0$$，此切割必須滿足$$y_k - y_{k-1}<\epsilon, ~ 1\leq k \leq n$$。

令$$I_k=[y_{k-1}, y_k)$$且$$E_k=f^{-1}(I_k), 1 \leq k \leq n$$為前像。

因為$$I_k$$為實數區間(Borel可測)，且$$f$$為可測函數，因此$$E_k$$為可測集。--(1)

定義在$$E$$上的簡單函數$$h_\epsilon, g_\epsilon$$為：

* $$h_\epsilon(x) = \sum_{k=1}^n y_{k-1} \chi_{E_k}(x)$$
* $$g_\epsilon(x) = \sum_{k=1}^n y_{k} \chi_{E_k}(x)$$

給定$$x \in E$$，因為$$f(E) \subseteq (c,d)$$，因此存在唯一的整數$$k \ni 1 \leq k \leq n$$滿足$$y_{k-1} \leq f(x) < y_k$$。

因此$$h_\epsilon(x) =y_{k-1} \leq f(x) <y_k = g_{\epsilon}(x)$$

由於$$y_k - y_{k-1}<\epsilon$$，因此$$h_\epsilon, g_{\epsilon}$$即為所求。

(QED)

</details>

## 存在遞增可測簡單函數可逼近非負可測函數

> $$f: E \rightarrow [0, \infty]$$為非負可測函數(函數值可為無窮大)，則存在遞增非負可測簡單函數序列：$$h_k(x) \leq h_{k+1}(x), k \in \mathbb{N}$$ 使得：$$\displaystyle \lim_{k \rightarrow \infty }h_k(x) =f(x), ~ x \in E$$。
>
> <mark style="color:red;">註：此處簡單函數逼近切</mark>$$f$$<mark style="color:red;">的值域(但可能有無限多個取值)</mark>。
>
> <mark style="color:red;">註：此逼近性質可用於定義非負可測函數的積分</mark>。

<figure><img src="../../.gitbook/assets/simple-function-approximation-min.png" alt="" width="286"><figcaption><p>simple function approximation</p></figcaption></figure>

<details>

<summary>proof：切值域直接建構遞增簡單函數序列</summary>

[https://math.stackexchange.com/questions/2943834/approximation-of-measurable-function-via-simple-functions-proof](https://math.stackexchange.com/questions/2943834/approximation-of-measurable-function-via-simple-functions-proof)

$$\forall k \in \mathbb{N}$$，可將(值域)閉區間$$[0,k]$$分為$$k \cdot 2^k$$等長區間。

令其中第$$j$$個定義域區間為$$E_{k,j}=\{x \in E ~|~ \frac{j-1}{2^k} \leq f(x) < \frac{j}{2^k}\}, j=1,2,\dots, k2^k$$。<mark style="color:blue;">此時函數</mark>$$f$$<mark style="color:blue;">在此定義域的函數值最小值與最大值差距為</mark>$$\frac{1}{2^k}$$。(<mark style="background-color:red;">用於定義</mark>$$f(x)<\infty$$<mark style="background-color:red;">為有限值時的前像</mark>)

而函數值大於等於$$k$$的區間記為$$E_k=\{x \in E ~|~ f(x) \geq k\}$$。<mark style="background-color:red;">此集合是用於定義函數值為無窮大時的前像</mark>。

取(值域)函數序列：$$\displaystyle h_k(x)=\left\{ \begin{aligned} &\frac{j-1}{2^k}, & x \in E_{k,j} \\ &k, & x \in E_k \end{aligned} \right. ~j=1,2,\dots, k2^k, ~ k \in \mathbb{N}$$。

記$$\displaystyle h_k(x)=k \cdot \chi_{E_k}(x) + \sum_{j=1}^{k \cdot 2^k} \frac{j-1}{2^k}\chi_{E_{k,j}}(x), ~ x \in E$$。<mark style="color:blue;">因此該簡單函數的上限值為</mark>$$k$$<mark style="color:blue;">，而小於</mark>$$k$$<mark style="color:blue;">的值域切分成</mark>$$k\cdot 2^k$$<mark style="color:blue;">塊，每塊值域的長度為</mark>$$\frac{1}{2^k}$$。

因此$$h_k(x)$$都是非負可測簡單函數。

因為給定$$x \in E$$時，若$$f(x)$$落在$$E_{k,j}$$時，表示$$\frac{j-1}{2^k}\leq f(x) < \frac{j}{2^k}$$，若切分更細時，同樣的函數值$$f(x)$$會落在比$$E_{k,j}$$切分更細的集合，即$$\frac{m-1}{2^{k+1}}\leq f(x) < \frac{m}{2^{k+1}}$$，且$$\frac{j-1}{2^k} \leq \frac{m-1}{2^{k+1}}$$，因此可得$$h_k (x) \leq h_{h+1}(x) \leq f(x)$$，$$x \in E, ~ k \in \mathbb{N}$$ 為遞增函數序列。

若$$\forall x \in E$$，函數有界，即$$\exists M < \infty \ni f(x) \leq M$$，則當$$k > M$$時，可得$$f$$與$$h_k(x)$$的差值上限為$$2^{-k}$$，即$$0 \leq f(x) - h_{k}(x) \leq 2^{-k}, ~ x \in E$$。

若 $$f(x) = \infty$$，可得$$h_k(x) = k, k \in \mathbb{N}$$

因此$$\displaystyle \lim_{k \rightarrow \infty} h_k(x) = f(x), ~ \forall x \in E$$ (QED)

</details>

## 一般函數可測若且唯若存在可測簡單函數逼近一般函數(the simple approximation theorem)

> $$E$$為可測集合，$$f: E \rightarrow [-\infty, \infty]$$為可測函數<mark style="color:red;">若且唯若</mark>存在可測簡單函數序列$$\{h_k(x)\}$$使得$$|h_k(x)| \leq |f(x)|$$且有(<mark style="color:blue;">點態收斂</mark>) $$\displaystyle \lim_{k \rightarrow \infty} h_k(x) = f(x), ~ x \in E$$。
>
> 若$$f(x)$$有界，則上述為<mark style="color:blue;">均勻(一致)收斂</mark>，即$$\displaystyle \lim_{k \rightarrow \infty }\sup_{x\in E}\{f_k(x) - f(x)\}=0$$。
>
> <mark style="color:red;">註：此逼近性質可用於定義可測函數的積分</mark>。

<details>

<summary>proof：&#x3C;= 可測函數序列的極限仍為可測函數。<br>=>函數為正成份與負成分兩個非負函數之差，因此只要處理非負函數即可。</summary>

<= 因為$$\{h_k(x)\}$$為可測函數序列，且點態收斂至$$f$$，由\[可測函數序列的極限仍為可測函數]得$$f$$為可測函數。

\=> ($$f$$不必為有界函數, proof 1)

令$$f(x)=f^{+}(x) - f^{-}(x)$$，且$$f$$為可測函數，由\[存在遞增可測簡單函數可逼近非負可測函數]$$m_k(x)$$與$$n_k(x)$$滿足$$\displaystyle \lim_{k \rightarrow \infty }m_k(x)=f^{+}(x)$$與$$\displaystyle \lim_{k \rightarrow \infty }n_k(x)=f^{-}(x)$$ $$x \in E$$

由於$$h_k(x)=m_k(x) - n_k(x)$$為可測簡單函數，且由極限的線性性質得 $$\displaystyle \lim_{k \rightarrow \infty }m_k(x)-n_k(x)=f^{+}(x) - f^{-}(x)=f(x), ~ x \in E$$。 (QED )

\=> ($$f \geq 0$$不必為有界函數, proof 2)

不失一般性令且$$f \geq 0$$為非負可測函數。

定義$$E_n=\{x \in E~|~ f(x) \leq n\}, ~ n \in \mathbb{N}$$，則$$E_n$$為可測集合且$$f$$定義在$$E_n$$上為非負有界可測函數。

由\[存在可測簡單函數可夾擠有界可測實值函數]得給定$$\epsilon=1/n$$，存在定義在$$E_n$$上的簡單函數$$h_n$$與$$g_n$$滿足$$0 \leq h_n(x) \leq f(x) \leq g_n(x)$$--(1)，且$$0 \leq g_n(x)-h_n(x) < 1/n$$ on $$E_n$$--(2)。

(1)中同減$$h_n(x)$$後，由(2)可得$$0 \leq f(x)-h_n(x) \leq g_n(x)-h_n(x) <1/n$$ on $$E_n$$。--(3)

令$$h_n(x)=n \text{ if } f(x) > n$$，則$$h_n(x)$$可定義在$$E$$上。--(4)

由(3,4)得$$0 \leq h_n(x) \leq f(x), ~ \forall x \in E$$--(5)

* 若$$f$$為有界函數時，則存在$$N_0 \in \mathbb{N} \ni f(x)<N_0$$，由(3)得$$0 \leq f(x) - h_n(x) < 1/n, ~ \forall n \geq N_0$$，因此$$\displaystyle \lim_{n \rightarrow \infty }h_n(x)=f(x)$$。
* 若$$f(x)=\infty$$，由(4)得$$h_n(x)=n, \forall n$$，因此$$\displaystyle \lim_{n \rightarrow \infty }h_n(x)=f(x)$$ (QED)

\=> ($$f$$為有界函數)

若在集合$$E$$上函數值有限，即$$|f(x)| \leq M$$，則當$$k>M$$時，可得：

* $$\displaystyle \sup |f^{+}(x) - m_k(x)| \leq \frac{1}{2^k}, ~ x \in E$$
* $$\displaystyle \sup |f^{-}(x) - n_k(x)| \leq \frac{1}{2^k}, ~ x \in E$$

因此可得$$\displaystyle \begin{aligned} & \lim_{k \rightarrow \infty} \sup{(f(x)-(m_k(x) - n_k(x))} \\ & \leq \lim_{k \rightarrow \infty}\sup |f^{+}(x) - m_k(x)| + \lim_{k \rightarrow \infty}\sup |f^{-}(x) - n_k(x)| \\ & \leq \lim_{k \rightarrow \infty}\frac{1}{2^k} + \lim_{k \rightarrow \infty}\frac{1}{2^k} \\ & \leq 0 \end{aligned}$$

(QED)

</details>

## 支撐集(support set)

> 對於定義在$$E \subseteq \mathbb{R}^n$$的函數$$f(x)$$，定義$$\mathrm{supp}(f)=\{x \in E~|~ f(x)\neq 0\}$$為函數的支撐集。
>
> 如果$$\mathrm{supp}(f)$$有界\[$$\exists r >0, p \in \mathbb{R}^n \ni \mathrm{supp}(f) \subseteq B_r(p)$$]\(在歐式空間中等價於緊緻集合)，則稱函數$$f(x)$$是有緊緻支撐集的函數。

### 存在可測簡單函數且函數為有緊致支撐集逼近可測函數

> $$f: E \rightarrow \overline{\mathbb{R}}$$為可測函數，則存在可測簡單函數序列$$\{h_k(x)\}$$，且$$h_k(x)$$有緊緻支撐集，使得$$|h_k(x)| \leq |f(x)|$$且有 $$\displaystyle \lim_{k \rightarrow \infty} h_k(x) = f(x), ~ x \in E$$。

<details>

<summary>proof</summary>

$$\forall k$$令$$g_k(x) = h_k(x) \chi_{B_k(0)}(x), ~ x \in E$$

則$$g_k(x)$$仍為可測函數且有緊緻支撐集。

若$$x \in E$$，則存在$$k_0 \ni k \geq k_0$$時，$$x \in B_k(0)$$，此時可得 $$\displaystyle lim_{k \rightarrow \infty} g_k(x) = \lim_{k \rightarrow \infty} h_k(x) = f(x), ~ x \in E$$ (QED)

</details>
