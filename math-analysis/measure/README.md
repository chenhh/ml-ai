# 測度(measure)

## 簡介

在此討論的是測度應具有的性質，只要符合(正)測度定義的函數均可視為測度。 (正)<mark style="color:red;">測度是將可測集合對映至</mark>$$[0,\infty]$$<mark style="color:red;">的函數(注意測度值可為無窮大)，符號測度的值域為</mark>$$[-\infty, \infty]$$<mark style="color:red;">)</mark>。測度在$$\mathbb{R}^n$$​中是對長度、面積與體積的抽象推廣。

一般測度如果沒有特別定義都是指正測度(可取值至無窮大)，如果為有限(正)測度則取值為實數值。因此討論時要考慮到測度無窮大時的性質。

在討論測度或證明時，重點在於為<mark style="background-color:green;">有限測度(如機率測度)，或σ有限測度，或一般(正)測度</mark>。之後還會討論取值為擴充實數的符號測度。

討論建構測度的步驟，首先是用外測度處理實數中任意的集合，取能夠覆蓋該集合的最小可數子集合的外測度做為該集合的外測度。但是並非所有的實數集合都滿足外測度的性質，實數中只有可測的集合可滿足外測度的性質，而實數中可測的集合為σ域。

若外測度用於量測可測集合內元素之值時，因為滿足可加性，此時外測度等價於測度。

## 測度(measure)

> 給定集合$$X$$，$$Σ$$為定義在$$X$$上的σ域(σ-field)。
>
> * 定義函數$$μ: \Sigma \rightarrow [0, \infty]$$（可為無窮大）滿足以下兩個條件時稱為測度：
>   * <mark style="color:blue;">\[空集合的測度為0</mark>] $$\mu(\emptyset)=0$$
>   * <mark style="color:blue;">\[countable additive, 可數可加性</mark>] $$\displaystyle \mu(\bigcup_{n=1}^{\infty}E_n) =\sum_{n=1}^{\infty}\mu (E_n), ~ E_n \in \Sigma$$且$$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$
>
> <mark style="color:red;">測度是測量給定集合的函數，定義域為</mark><mark style="color:red;">σ</mark><mark style="color:red;">-field(集合族)，而不是單純集合。因為可用選擇性公理從一般集合建構出不可測的集合，因此定義域必須為</mark><mark style="color:red;">σ</mark><mark style="color:red;">域才能避開不可測集合</mark>。不可測的集合在實際應用上幾乎不存在，因此定義σ域為了理論的嚴謹性。
>
> 由於測度的值域可為無窮大，因此在證明性質時也要考慮無窮大時是否滿足條件。
>
> 因為測度滿足可數可加性，則必滿足有限可加性(finite-additive)，反之不一定成立。\
> &#x20;$$\mu(\bigcup_{i=1}^n E_i) = \sum_{i=1}^n \mu(E_i)$$，$$E_i \in \Sigma$$且$$E_i \cap E_j = \phi~ \forall i \neq j$$。

函數$$f: E\rightarrow [-\infty, \infty]$$：定義域是在可測集合$$E$$中，如果任意由值域得到的前像$$f^{-1}$$集合均為$$\Sigma$$中的元素時，則稱為可測函數(measurable function)，否則為不可測函數。

由於測度的單調性，因此宇集合$$X$$為有最大測度值的集合。

如果滿足$$\displaystyle \mu(X)=1$$的條件時，稱為<mark style="color:red;">機率測度(probability measure)</mark>。

如果滿足$$\mu(X)<\infty$$時，稱為<mark style="color:red;">有限測度(finite measure)</mark>。

如果存在宇集合的可數分割，且分割的測度均為有限值，即$$\{E_n\}_{n \in \mathbb{N}} \in \Sigma$$且$$\bigcup_{n \in \mathbb{N}}E_n =X$$，$$\mu(E_n) < \infty$$，稱<mark style="color:red;">σ-</mark><mark style="color:red;">finite測度</mark>。

若集合$$N \in \Sigma$$且滿足$$\mu(N)=0$$，稱為<mark style="color:red;">零測集(null set)</mark>。

### 常見測度

在實數$$\mathbb{R}$$上常數的測度有<mark style="color:red;">Lebesgue measure (on Borel set)</mark>

* $$\mu([a,b])=\mu([a,b))=\mu((a,b])=\mu((a,b))=|b−a|$$。
* $$\mu([a,\infty))=\mu((a,\infty))=\mu((−\infty,b])=\mu((−\infty,b))=\infty$$。

自然數或整數上的測度為<mark style="color:red;">計數測度</mark>(<mark style="color:red;">counting measure)。令</mark>$$X=\mathbb{N}$$，$$\Sigma=2^{\mathbb{N}}$$， $$\mu: \Sigma \rightarrow [0, \infty]$$。$$\mu(E)=\begin{cases}  |E|, & E \text{ 為有限集 }\\  \infty, & E \text{ 為無限集 } .  \end{cases}$$

* $$\mu([1,2,3,4,5])=\#([1,2,3,4,5])=5$$。
* $$\mu(\mathbb{N})=\infty$$
* 令$$E_n=\{n\}$$，可得$$\mu(E_n)=1$$且$$\mathbb{N}=\bigcup_{n\in\mathbb{N}} E_n$$，因此$$\mu$$為σ-有限測度。

平面空間$$\mathbb{R}^2$$ 上的測度為<mark style="color:red;">面積</mark>。

立體空間$$\mathbb{R}^3$$ 的測度為<mark style="color:red;">體積</mark>。

函數空間的情形較為複雜，因此並非所有函數都存在測度函數可量測其值，因此必須先定義出可測函數後，才可定義測度。

<mark style="color:red;">Dirac測度：</mark> 令$$x_0 \in X$$, $$\delta(x_0, E)=\left\{ \begin{aligned} &1, \text{ if } x_0 \in E \\ &0, \text{ otherwise} \end{aligned} \right.$$，稱為$$x_0$$處的點質量(point mass at x0)。此測度非平移不變，即$$\delta(x_0, E) \neq \delta(x_0, y+E)$$。

## 零測集(measure zero set, null set)

> 定義集合$$S \subseteq \mathbb{R}$$ 的Lebesgue測度為0( measure zero)若
>
> * 對任意$$\epsilon >0$$，存在集合$$S$$可數的開區間覆蓋，且這些可數開區間覆蓋的總長度小於$$\epsilon$$。(註：Haine-Borel定理：實數上的有界閉區間(緊緻集)必可被有限開區間覆蓋)。
> *>   令$$F_k=(a_k, b_k) \subset \mathbb{R}, ~ k \in \mathbb{N}$$  為集合$$S$$的可數開區間覆蓋，則$$\displaystyle \forall \epsilon >0 , ~ S \subseteq \bigcup_{k \in \mathbb{N}} (a_k, b_k)$$ 且 $$\displaystyle \sum_{k \in \mathbb{N}} (b_k - a_k) < \epsilon$$。
> * 即$$S$$為零測集若$$S$$為測度(長度)任意小的開區間聯集之子集合（即不論多小的開區集之聯集，S均為此聯集的子集合）>

* <mark style="color:blue;">註：因為在(Tom M. Aposotol)基礎分析沒有定義測度與其性質，因此使用此Lebesgue測度任意小時，使用夾擠收斂來描述集合測度為0時應該有的性質</mark>。
* 給定測度空間$$(X, \Sigma, m)$$，則零測集$$S \in \Sigma$$滿足$$m(S)=0$$。
* 空集合$$\emptyset$$為零測集。但也存在非空集的測度為0。
* 實數的有限或可數無限子集都是零測集。自然數集合和有理數集合都是實數集的可數無限子集，因此它們是零測集。Cantor集是一個不可數的零測集。
* 可數零測集的聯集仍為零測集。
* 零測集的可測子集為零測集。
* [https://en.wikipedia.org/wiki/Null\_set](https://en.wikipedia.org/wiki/Null\_set)

## 測度的有限可加性

> 給定測度函數$$μ: \Sigma \rightarrow [0, \infty]$$：
>
> * <mark style="color:red;">\[可加性 ,additive]</mark> $$\forall E,F \in Σ$$, $$E \cap F=\emptyset \Rightarrow \mu( E ∪F)=\mu(E)+\mu(F)$$
> * <mark style="color:red;">\[有限可加性 finitely additive]</mark> $$\forall E_1,E_2,\ldots,E_n \in \Sigma$$, $$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$ $$\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i)= \sum_{i=1}^n \mu(E_i)$$
> * 註：因為是直接用測度定義得證，因此即使有任一集合的測度值為無窮大時也成立。會得到$$\infty=\infty$$的結果。

<details>

<summary>proof: 由測度定義可得出</summary>

proof: 有限可加性

令$$E_1, \dots, E_n, \phi, \phi, \dots$$集合兩兩互斥

$$\displaystyle \begin{aligned} \mu(\cup_{i=1}^n E_i) & = \mu(\cup_{i=1}^\infty E_i) \\ & = \sum_{i \in \mathbb{N}} \mu(E_i) \\ & = \sum_{i=1}^n \mu(E_i) + \sum_{i=n+1}^ \infty \mu(\phi) \\ & = \sum_{i=1}^n \mu(E_i) \end{aligned}$$

(QED)

</details>

### 範例：有限可加性不一定為可數可加性

令$$\omega$$為自然數$$\mathbb{N}$$的非主超濾子(non-principal ultrafilter)。

定義 $$\mu(A)=\begin{cases}  0, & A \cap \mathbb{N} \notin \omega, \\  1, & A \cap \mathbb{N} \in \omega.  \end{cases}$$，則$$\mu$$為有限可加性。

但若令$$A_n=\{0,1,\dots, n\}$$，則$$\forall n \in \mathbb{N}, \mu(A_n)=0$$。

但$$\mu(\bigcup_{n \in \mathbb{N}} A_n)=\mu(\mathbb{N})=1$$，即$$\mu(\bigcup_{n \in \mathbb{N} A_n} \neq \sum_{n\in \mathbb{N}}\mu(A_n)$$。

### 測度單調性與補集的測度

> * \[<mark style="color:blue;">測度單調性</mark>] $$\forall E, F \in \Sigma, E \subseteq F \implies \mu (E) \leq \mu(F)$$​
> * <mark style="color:red;">集合的大小與測度值有單調的關係</mark>。
> * 註：因為是直接用測度定義得證，因此即使有任一集合的測度為無窮大時也成立。會得到$$\infty \leq \infty$$的結果。
> * 註：反向不一定成立，即$$\nu(E) \leq \nu(F) \;\not\!\!\!\implies E \subseteq F$$。

<details>

<summary>proof：拆解為互斥的集合</summary>

因為$$E \subseteq F$$，可得 $$F = E \cup (F -E)$$。

由測度定義得 $$\mu(F) = \mu (E) + \mu (F-E)$$

如果$$\mu(E) < \infty$$，因為$$\mu(F-E) \geq 0$$，可得$$\mu(E) \leq \mu(F)$$。--(1)

如果$$\mu(E) =\infty$$，因為$$\infty + c = \infty$$，$$c \in [0, \infty]$$，所以$$\mu(E)=\mu(F)$$。--(2)

如果$$\mu(F)=\infty$$，顯然$$\mu(E) \leq \mu(F)$$--(3)

由(1,2,3)得$$\mu(E) \leq \mu(F)$$ (QED)

</details>

#### 範例：測度較大的集合不一定是子集合

$$E=[1,3]$$，$$F=[4,7]$$。$$\mu(F)=3, \mu (E)=2$$，但$$E \cap F=\emptyset$$。

> * <mark style="color:blue;">\[補集的測度]</mark> $$\forall E, F \in \Sigma, E \subseteq F$$且$$\mu(F) < \infty$$，則$$\mu(F -E) = \mu(F) - \mu(E)$$
> * $$\mu(F) < \infty$$必須是有限值得到$$\mu(E)<\infty$$，否則無法移項得到等式。

<details>

<summary>proof: 拆解成互斥的集合</summary>

因為$$E \subseteq F$$，得 $$F = E \cup (F -E)$$。

由測度定義得 $$\mu(F) = \mu (E) + \mu (F-E)$$且$$\mu(F-E) \geq 0$$。

因為$$\mu(F)<\infty$$，所以上式可同減$$\mu(E)$$得$$\mu(F-E)=\mu(F)-\mu(E)$$。

(QED)

</details>

## 測度的次可加性

> * \[<mark style="color:blue;">次可加性 ,sub-additive</mark>] $$\forall E,F \in \Sigma, ~\mu(E \cup F) \leq \mu(E)+\mu(F)$$，等號成立於$$E \cap F=\emptyset$$。
> * \[<mark style="color:blue;">有限次可加性, finitely sub-additive</mark>] $$\forall E_1,E_2, \ldots,E_n \in \Sigma\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i ) \leq \sum_{i=1}^n\mu(E_i )$$
> * \[<mark style="color:blue;">可數次可加性, countable sub-additive</mark>] $$\displaystyle \forall E_1,E_2, \ldots \in \Sigma \Rightarrow \mu(\bigcup_{i=1}^\infty E_i ) \leq \sum_{i=1}^\infty \mu(E_i)$$
> * 註：因為是直接用測度定義得證，因此即使有任一集合的測度為無窮大時也成立。

<details>

<summary>proof: 次可加性，拆解為互斥的集合</summary>

* $$E \cup F = E \cup (F - E)$$
* 由測度定義得 $$\mu(E \cup F) = \mu(E) + \mu(F-E)$$
* 因為$$F-E \subseteq F$$可得$$\mu(F-E) \leq \mu(F)$$
* 因此 $$\mu(E \cup F) \leq \mu (E) +\mu(F)$$ (QED)

</details>

<details>

<summary>proof: 可數次可加性，拆解為互斥的集合</summary>

* 令$$F_1=E_1, ~F_2=E_2−E_1, ~F_3=E_3−(E_1 \cup E_2 ), \ldots , F_n=E_n−(E_1 \cup \ldots \cup E_{n−1} )$$
* 可得$$F_n$$ 為$$E_n$$ 的子集合 ($$F_n \subseteq E_n$$ )，且$$\{F_n\} \subseteq \Sigma$$為互斥的集合序列 $$F_i \cap F_j=\emptyset, ~ \forall i \neq j$$ 。
* $$\displaystyle \mu(\bigcup_{i=1}^\infty E_i )=\mu(\bigcup_{i=1}^\infty F_i )=\sum_{i=1}^\infty \mu(F_i ) \leq \sum_{i=1}^\infty \mu(E_i )$$ (QED).

</details>

## 有限測度與σ有限測度

> 如果對任意可測集合滿足$$\mu(E)<\infty$$ ，則稱$$\mu: \Sigma \rightarrow [0, \infty)$$為<mark style="color:red;">有限測度（finite measure）</mark>。
>
> 註：一般有限測度是指對宇集合的測度為有限值，即$$\mu(X) <\infty$$。因為測度有單調性，因此$$\forall E \subseteq X, ~0 \leq \mu(E) \leq \mu(X) <\infty$$。

$$\mu(\mathbb{R})=\infty$$，因此實數的長度不是有限測度。

<mark style="color:blue;">所有的機率測度都是有限測度</mark>，因為$$\mu(\Omega) =1$$。

> \[<mark style="color:red;">σ有限測度</mark>] $$\exists \{E_n \}\subseteq \Sigma, ~ X=\bigcup_n E_n \ni \mu(E_n )< \infty, ~ \forall n$$。
>
> 但不要求$$\mu(X)<\infty$$。只要求$$X$$的可數分割中，每一個分割集的測度有限即可。
>
> 由定義可知<mark style="color:blue;">有限測度</mark>⊆<mark style="color:blue;">σ有限測度</mark>。因為若$$\mu(X)<\infty$$，則其任意可測子集$$\mu(E) < \infty$$。

實數的長度不是有限測度，<mark style="color:blue;">但是</mark>σ<mark style="color:blue;">有限測度</mark>，因為可將實數拆解為多個有限長度的線段的聯集。$$\mathbb{R} = \cdots \cup [-n, -n+1] \cup \cdots \cup[-1,1]\cup [1,2]\cup \cdots \cup [n, n+1] \cup \cdots$$且$$\mu([n, n+1])=1, \forall n$$。

<mark style="color:blue;">一般常用的測度大多為σ有限測度</mark>。如Lebesgue測度($$\mathbb{R}^n$$)，計數測度。

## 非互斥集合聯集與交集測度之和等於各別集合測度之和(排容原理)

> 給定測度函數$$μ: \Sigma \rightarrow [0, \infty]$$，
>
> $$\forall E,F \in \Sigma \Rightarrow \mu(E \cup F)+\mu(E \cap F)=\mu(E)+\mu(F)$$
>
> 有限或一般測度時均成立。

<details>

<summary>proof: 拆解為互斥的集合</summary>

$$E \cup F=E \cup (F−E)$$

所以 $$\mu(E \cup F)=\mu(E)+\mu(F−E)$$

若$$\mu(E \cap F)=\infty$$，因為$$E \cap F \subseteq E \cup F$$，所以$$\mu(E \cup F)=\infty$$

若$$\mu(E \cap F)< \infty$$, $$\mu(F−E)=\mu(F−(E\cap F))=\mu(F)−\mu(E\cap F)$$

$$\mu(E \cup F)= \mu(E)+\mu(F)−\mu(E\cap F)$$ (QED)

</details>

## <mark style="background-color:red;">遞增集合極限的測度(測度的連續性，continuity of measure)</mark>

> 給定測度函數$$μ: \Sigma \rightarrow [0, \infty]$$
>
> $$\displaystyle \forall E_1,E_2, \ldots \in \Sigma, ~ E_i \subseteq E_j, ~\forall i \leq j \Rightarrow \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )=\mu(\bigcup_{n \in \mathbb{N}} E_n)$$
>
> * 因為$$\Sigma$$內最大的集合為宇集合$$X$$，因此遞增集合最多和宇集合一樣大。
> * 遞增集合序列極限的測度等於所有集合聯集的測度。
> * <mark style="color:red;">如果</mark>$$\mu(E_1)=\infty$$<mark style="color:red;">，此性質仍然成立</mark>。

<details>

<summary>proof: 拆解為互斥的集合</summary>

若存在$$n_0 \in \mathbb{N} \ni \mu(E_{n_0})=\infty$$，則可得$$\displaystyle \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )=\infty$$

&#x20;考慮所有集合測度均為有限值，即$$\mu(E_n)<\infty, ~\forall n \in \mathbb{N}$$

$$\displaystyle \lim_{n \rightarrow \infty}⁡ E_n=\bigcup_{n=1}^\infty E_n=E_1 \cup (E_2−E_1 )\cup (E_3−E_2 )\cup \ldots$$

所以$$\begin{align} \displaystyle \mu(\lim_{n \rightarrow \infty}⁡ E_n ) & =\mu(\bigcup_{n=1}^\infty E_n) \\ &=\mu(E_1 )+\mu(E_2−E_1 )+\mu(E_3−E_2 )+\ldots \\ & =\lim_{n \rightarrow \infty}⁡\{\mu(E_1 )+\mu(E_2−E_1 )+\mu(E_3−E_2 )+\\ &\ldots+\mu(E_n−E_{n−1} )\} -- (1)\end{align}$$

因為$$E_1, E_2-E_1, \ldots, E_n - E_{n-1}$$為兩兩互斥的集合，且$$E_1 \cup(E_2-E_1) \cup \ldots \cup (E_n - E_{n-1})= E_n$$

因此$$\mu(E_1) + \mu(E_2 - E_1) + \ldots \mu(E_n - E_{n-1}) = \mu(E_n) -- (2)$$

由(1,2)得 $$\displaystyle \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$ (QED)

</details>

## <mark style="background-color:red;">遞減集合極限的測度(測度的連續性，continuity of measure)</mark>

> 給定測度函數$$μ: \Sigma \rightarrow [0, \infty]$$，
>
> $$\displaystyle \forall E_1,E_2, \ldots \in \Sigma, ~ E_i \supseteq E_j, ~\forall i \leq j$$且$$\exists n_0 \in \mathbb{N} \ni \mu(E_{n_0}) < \infty$$，則$$\displaystyle \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n ) = \mu(\cap_{n \in \mathbb{N}} E_n)$$
>
> * $$\exists n_0 \in \mathbb{N} \ni \mu(E_{n_0} )<\infty$$ 意思是某一個集合的測度有限，因為$$E_n$$為遞減集合，因此在$$n_0$$之後的集合之測度也為有限值，可避免所有的集合之測度均為無窮大的情況。
> * <mark style="color:red;">若</mark>$$\mu(E_n )=\infty ~\forall n$$<mark style="color:red;">，則此性質不成立</mark>。

<details>

<summary>proof: 拆解為互斥的集合</summary>

$$\displaystyle \lim_{n \rightarrow \infty} \mu(E_n )$$ 在$$n_0$$之前的集合不會影響此值 。同樣$$\displaystyle \mu(\lim_{n \rightarrow \infty}E_n )$$在$$n_0$$ 之前的集合也不會影響此值，因此只要考慮$$n_0$$ 之後的集合即可。

$$E_{n_0}−E_n \in \Sigma$$ 且$$E_{n_0}−E_{n_0 + 1} \subseteq E_{n_0}−E_{n_0+2}$$為遞增的集合序列 。

所以$$\displaystyle \lim_{n \rightarrow \infty} \mu(E_{n_0 }−E_n )=\mu(\lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n ))$$

因為 $$\mu(E_{n_0} −E_n )=\mu(E_{n_0} )−\mu(E_n)$$ (兩者均為有限值)

所以 $$\displaystyle \lim_{n \rightarrow \infty} \mu(E_{n_0}−E_n )=\lim_{n \rightarrow \infty}⁡\mu(E_{n_0})−\lim_{n \rightarrow \infty} \mu(E_n )=\mu(E_{n_0})−\lim_{n \rightarrow \infty}\mu(E_n)$$

因為$$\{E_n\}$$為遞減集合序列，所以$$\displaystyle \lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n )=\bigcup_n (E_{n_0}−E_n )=E_{n_0}−\left(\bigcap_n E_n \right)$$

$$\displaystyle A−\lim_{n \rightarrow \infty}E_n =(A−E_1 ) \cup (A−E_2 ) \cup \ldots =(A \cap E_1^c )\cup (A \cap E_2)^c )\cup \ldots =A−(\cap_n E_n )$$

所以$$\displaystyle \mu(\lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n ) )=\mu(E_{n_0 }−(\bigcap_n E_n ))=\mu(E_{n_0} )− \mu(\cap_n E_n )$$

$$\displaystyle \mu(E_{n_0} )−\lim_{n \rightarrow \infty} \mu(E_n )= \mu(E_{n_0} )−\mu(\bigcap_n E_n )$$

$$\displaystyle \lim_{n \rightarrow \infty}\mu(E_n )=\mu(\bigcap_n E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$ (QED)

</details>

#### 範例

$$E_n=[0, 1+\frac{1}{n}] \subseteq \mathbb{R}$$為遞減的集合

$$\displaystyle \lim_{n \rightarrow \infty}E_n = \lim_{n \rightarrow \infty}⁡[0, 1+\frac{1}{n}]=[0,1]$$

所以 $$\displaystyle \mu(\lim_{n \rightarrow \infty} E_n )=1$$

而$$\displaystyle \lim_{n \rightarrow \infty} \mu(E_n )= \lim_{n \rightarrow \infty}⁡(1+\frac{1}{n})=1$$

#### 範例：遞減集合序列，全部集合測度均為無窮大但極限集合測度為0

$$E_n=\{n, n+1, \dots,\}$$，且$$\mu$$為計數測度。

則$$\mu(E_n)=\infty, ~\forall n \in \mathbb{N}$$

但$$\cap_{n \in \mathbb{N}} E_n=\phi$$，因此$$\mu(\cap_n E_n)=0$$

## 集合序列上下極限的測度(Fatou lemma of measure)

> 令可測集合序列$$E_1, E_2,\dots \in \Sigma$$，且測度$$\mu: \Sigma \rightarrow [0, \infty]$$，則：
>
> 1. &#x20;$$\displaystyle \mu(\liminf_{n \rightarrow \infty} E_n) \leq \liminf_{n \rightarrow \infty} \mu(E_n)$$ 。\
>    左側為下極限集合的測度，取值為$$[0,\infty]$$；右側為數列下極限，取值可為$$[-\infty, \infty]$$。\
>    當我們求集合測度的下極限時，各個集合之間元素並不互相干擾，因此測度不會互相影響。但當我們求下極限集合的測度時，這個下極限集合，是經過互相干擾後的集合，因此其測度最好的情形為集合間不互相干擾。
> 2. &#x20;$$\displaystyle \mu(\limsup_{n \rightarrow \infty} E_n) \geq \limsup_{n \rightarrow \infty} \mu(E_n)$$ 若 $$\mu(\bigcup_{n=1}^\infty E_n)<\infty$$\
>    因為對任意集合序列可得：$$\displaystyle \liminf_{n \rightarrow \infty} E_n \subseteq \limsup_{n \rightarrow \infty} E_n$$
> 3. 在**有限測度**時，可得$$\displaystyle \mu(\liminf_{n \rightarrow \infty} E_n) \leq \liminf_{n \rightarrow \infty} \mu(E_n)  \leq \limsup_{n \rightarrow \infty} \mu(E_n) \leq  \mu(\limsup_{n \rightarrow \infty} E_n)$$
> 4. 在有限測度時，若$$\displaystyle \lim_{n \rightarrow \infty} E_n$$存在，且$$\displaystyle \mu(\bigcup_{n=1}^\infty E_n) < \infty$$則可得 $$\displaystyle \mu(\lim_{n \rightarrow \infty} E_n) = \lim_{n \rightarrow \infty} \mu(E_n)$$

<details>

<summary>proof 1: </summary>

令$$M_k\equiv \bigcap_{j=k}^\infty E_j \subseteq E_k~, k=1,2,\dots$$

可得$$M_1 \subseteq M_2 \subseteq M_3 \subseteq \dots$$為遞增集合序列，且$$\displaystyle \lim_{n \rightarrow \infty} M_n = \bigcup_{n=1}^\infty M_n$$

由continuity of measure(在$$\mu(M_1)=\infty$$時仍成立)可得$$\displaystyle \lim_{n \rightarrow \infty} \mu(⁡M_n )=\mu(\lim_{n \rightarrow \infty}⁡ M_n)=\mu(\bigcup_{n=1}^\infty M_n)$$--(1)

而$$\displaystyle \mu(\bigcup_{n=1}^\infty M_n)=\mu(\bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k)=\mu(\liminf_{n \rightarrow \infty}{E_n})$$--(2)

同理$$\displaystyle \lim_{n \rightarrow \infty} \mu(⁡M_n )= \lim_{n \rightarrow \infty} \mu(\bigcap_{k=n}^\infty E_k)$$--(3)

由(1,2,3)得$$\displaystyle \mu(\liminf_{n \rightarrow \infty}{E_n}) = \lim_{n \rightarrow \infty} \mu(\bigcap_{k=n}^\infty E_k)$$--(4)

由於$$\displaystyle \bigcap_{k=n}^\infty E_k \subseteq E_n$$，由測度單調性得$$\displaystyle \mu(\bigcap_{k=n}^\infty E_k) \leq \mu(E_n)$$

由(4)知$$\displaystyle \lim_{n \rightarrow \infty} \mu(\bigcap_{k=n}^\infty E_k)$$存在，但無法確定$$\displaystyle \lim_{n \rightarrow \infty} \mu(E_n)$$是否存在，但數列上下極限必定存在，因此可得$$\displaystyle \liminf_{n \rightarrow \infty }\mu(\bigcap_{k=n}^\infty E_k) \leq \liminf_{n \rightarrow \infty } \mu(E_n)$$--(5)

由於$$\displaystyle \liminf_{n \rightarrow \infty }\mu(\bigcap_{k=n}^\infty E_k) = \lim_{n \rightarrow \infty }\mu(\bigcap_{k=n}^\infty E_k)$$--(6)

從(4,5,6)可得$$\displaystyle \mu(\liminf_{n \rightarrow \infty} E_n) \leq \liminf_{n \rightarrow \infty} \mu(E_n)$$ (QED)

</details>

<details>

<summary>proof 4:</summary>

因為$$\displaystyle \lim_{n \rightarrow \infty} E_n$$存在，所以$$\displaystyle \limsup_{n \rightarrow \infty} E_n = \liminf_{n \rightarrow \infty} E_n$$

$$\displaystyle \limsup_{n \rightarrow \infty} \mu(E_n) \leq \mu(\limsup_{n \rightarrow \infty} E_n) = \mu(\liminf_{n \rightarrow \infty} E_n) \leq \liminf_{n \rightarrow \infty} \mu(E_n) \leq \limsup_{n \rightarrow \infty} \mu(E_n)$$--(1)

因為3得$$\displaystyle \mu(\liminf_{n \rightarrow \infty} E_n) \leq \liminf_{n \rightarrow \infty} \mu(E_n) \leq \limsup_{n \rightarrow \infty} \mu(E_n) \leq \mu(\limsup_{n \rightarrow \infty} E_n)$$--(2)

由(1,2)得$$\displaystyle \mu(\lim_{n \rightarrow \infty} E_n) = \lim_{n \rightarrow \infty} \mu(E_n)$$ (QED)

</details>

### 範例：集合序列上下極限的測度不等式成立

[https://math.stackexchange.com/questions/545215/why-is-there-inequality-in-fatous-lemma](https://math.stackexchange.com/questions/545215/why-is-there-inequality-in-fatous-lemma)

[https://zhuanlan.zhihu.com/p/318640829](https://zhuanlan.zhihu.com/p/318640829)

[https://en.wikipedia.org/wiki/Fatou's\_lemma#Examples\_for\_strict\_inequality](https://en.wikipedia.org/wiki/Fatou's\_lemma#Examples\_for\_strict\_inequality)

[https://www.zhihu.com/question/328909025](https://www.zhihu.com/question/328909025)

由積分的Fatou lemma得到的範例。

給定實數平面$$\mathbb{R}^2$$的集合序列$$E_n = \{[0, 1/n] \times [0,n], n \in \mathbb{N}\}$$與面積測度$$m$$。

隨著n增大，底變窄，高增大，但是$$E_n$$中的方塊面積總是為1。因此$$\displaystyle \lim_{n \rightarrow \infty} m(E_n)=\liminf_{n \rightarrow \infty} m(E_n)=1$$。

而在$$n \rightarrow \infty$$時，$$\displaystyle \liminf_{n \rightarrow \infty} E_n=\bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k$$

則可得$$\displaystyle m(\liminf_{n \rightarrow \infty} E_n) = 0 < 1 = \liminf_{n \rightarrow \infty} m (E_n)$$。



## <mark style="background-color:red;">The Borel-Cantelli lemma</mark>

> 給定測度函數$$μ: \Sigma \rightarrow [0, \infty]$$，令可測集合序列$$E_1, E_2,\dots \in \Sigma$$，且滿足$$\sum_{n=1}^\infty \mu(E_n) < \infty$$，則$$\displaystyle \mu(\limsup_{n \rightarrow \infty} E_n)=0$$或$$\displaystyle \mu(\liminf_{n \rightarrow \infty} E_n)=\infty$$
>
> $$\displaystyle \limsup_{n \rightarrow \infty} E_n =   \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k$$。上極限集內的元素存在於無窮多個集合中。因此若$$\displaystyle \mu(\limsup_{n \rightarrow \infty} E_n) \neq 0$$，即上極限集內的元素測度不為0，因為上極限元素存在於無窮多個集合中，因此無窮多個集合的測度均不為0，因此測度總和必定為無窮大。
>
> 更準確的說，如果無限多個集合的測度和為有限值，那麼包含於在無限多個集合中的子集的測度必為0，否則這無限多個集合每個測度都不小於$$\epsilon$$ ，總和為無窮大。
>
> 機率測度的解釋：如果所有(無窮個)事件$$E_n$$發生的機率(測度)總和是有限的，則這些事件有無限多個同時發生(無窮個交集)的機率(測度)為0。

<details>

<summary>proof:</summary>

由測度的可數次可加性得 $$\mu(\bigcup_{n=1}^\infty E_n) \leq \sum_{n=1}^\infty \mu(E_n) < \infty$$--(1)

&#x20;集合上極限的定義為$$\displaystyle \limsup_{n \rightarrow \infty} E_n = \bigcap_{n=1}^\infty  \bigcup_{k=n}^\infty E_k$$

令$$M_n=\cup_{k=n}^\infty E_k$$，可得$$M_1 \supseteq M_2\supseteq \dots$$為遞減集合序列

由continuity of measure且$$\mu(M_n)<\infty$$得$$\displaystyle \mu(\cap_{n =1}^\infty M_n)  = \lim_{n \rightarrow \infty }⁡ \mu(M_n )$$

因此$$\displaystyle \mu(\bigcap_{n =1}^\infty M_n) \equiv \mu(\bigcap_{n =1}^\infty \bigcup_{k=n}^\infty E_k) \equiv \mu(\limsup_{n \rightarrow \infty} E_n) =  \lim_{n \rightarrow \infty} \mu(M_n) \equiv \lim_{n \rightarrow \infty} \mu(\cup_{k=n}^\infty E_k)$$--(2)

由(1)得 $$\displaystyle \lim_{n \rightarrow \infty} \mu(\bigcup_{k=n}^\infty E_k) \leq \lim_{n \rightarrow \infty} \sum_{k=n}^\infty \mu(E_k)$$--(3)

因為$$\sum_{n=1}^\infty \mu(E_n) < \infty$$，由無窮級數的收斂條件可得$$\displaystyle \lim_{n \rightarrow \infty} \sum_{k=n}^\infty \mu(E_k)=0$$--(4)

由(2,3,4)得$$\displaystyle \mu(\limsup_{n \rightarrow \infty} E_n) \leq \lim_{n \rightarrow \infty} \sum_{k=n}^\infty \mu(E_k)=0$$ (QED)

</details>

## 測度空間(measure space)

> * $$(X, \Sigma, \mu)$$稱為測度空間。
> * 若$$\mu(X)<\infty$$，則$$(X, \Sigma, \mu)$$稱為有限測度空間。
> * 若存在可測集合$$E_i \in \Sigma, ~i \in \mathbb{N}$$且$$\mu(E_i) < \infty, \forall i$$，$$X =\bigcup_{i \in \mathbb{N}}E_i$$，則$$(X, \sigma, \mu)$$為σ有限測度空間。
> * 若$$E$$為零測集(null set)，且$$\forall E \subseteq  X, ~ E  \in \Sigma$$，則$$(X, \Sigma, \mu)$$稱為完備測度空間(complete measure space)。
>
>
