# 測度(measure)

## 簡介

在此討論的是測度應具有的性質，只要符合測度定義的函數均可視為測度。 <mark style="color:red;">測度是將集合對映至正實數的函數</mark>。測度在$$\mathbb{R}^n$$​中是對長度、面積與體積的推廣。

## 測度(measure)

> 給定集合$$X$$，$$Σ$$為定義在$$X$$上的[sigma-field](set/field-and-sigma-field.md#sigmafieldsigmaalgebra-yu-ke-ce-kong-jian)。
>
> *   定義函數$$μ: \Sigma \rightarrow [0, \infty]$$（可為無窮大）滿足以下兩個條件時稱為測度：
>
>     * &#x20;<mark style="color:blue;">\[空集合的測度為0</mark>] $$\mu(\emptyset)=0$$
>     * &#x20;<mark style="color:blue;">\[countable additive, 互斥集合聯集的測度等於各別集合測度的加總</mark>] $$\displaystyle \mu(\cup_{n=1}^{\infty}E_n) =\sum_{n=1}^{\infty}\mu (E_n), ~ E_n \in \Sigma$$且$$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$
>
>
> * <mark style="color:red;">測度是測量給定集合的函數</mark>。
> * 由於測度的值域可為無窮大，因此在證明性質時也要考慮無窮大時是否滿足條件。

* 測度的定義域是在$$\Sigma$$上，而不是在原始的集合$$X$$，因為如果從$$X$$取出任意的結果$$\omega$$，可依公理建構出不可測的集合$$E$$，但是不可測的集合在實際應用上幾乎不存在，為了理論的嚴謹性，所以要求測度的定義域是在可測的集合，即$$\Sigma$$中的任意集合。
* 同理函數$$f: X\rightarrow \mathbb{R}$$雖然定義域是在一般集合$$X$$中，但是如果任意由值域得到的前像$$f^{-1}$$集合均為$$\Sigma$$中的元素時，則稱為可測函數，否則為不可測函數。
* 註：測度之值在此定義為正實數，但之後可放寬為任意實數(如負值)或複數。
* **註: 只要再加上第三個條件**$$\displaystyle \sum_{n=1}^\infty \mu( E_n) =1$$**的條件時，則為機率測度**。

#### 範例&#xD;

* 在實數$$\mathbb{R}$$上常數的測度有<mark style="color:red;">Lebesgue measure</mark>&#x20;
  * $$\mu([a,b])=\mu([a,b))=\mu((a,b])=\mu((a,b))=|b−a|$$。
  * &#x20;$$\mu([a,\infty))=\mu((a,\infty))=\mu((−\infty,b])=\mu((−\infty,b))=\infty$$
* 自然數或整數上的測度有<mark style="color:red;">counting measure</mark> $$\mu([1,2,3,4,5])=\#([1,2,3,4,5])=5$$。
* 平面空間$$\mathbb{R}^2$$ 上的測度為<mark style="color:red;">面積</mark>。
* 立體空間$$\mathbb{R}^3$$ 的測度為<mark style="color:red;">體積</mark>。
* 函數空間的情形較為複雜，因此並非所有函數都存在測度函數可量測其值，因此必須先定義出可測函數後，才可定義測度。
* Dirac measure: 令$$x_0 \in X$$, $$\delta(x_0, E)=\left\{  \begin{align} &1, \text{ if } x_0 \in E \\ &0, \text{ otherwise} \end{align} \right.$$

### 測度的可加性

> * \[可加性 ,additive] $$\forall E,F \in Σ$$, $$E \cap F=\emptyset \Rightarrow \mu( E ∪F)=\mu(E)+\mu(F)$$
> * \[有限可加性 finitely additive] $$\forall E_1,E_2,\ldots,E_n \in \Sigma$$, $$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$ $$\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i)= \sum_{i=1}^n \mu(E_i)$$>

* 由測度的定義可直接得出。

### 子集合與補集的測度

> * \[<mark style="color:blue;">子集合的測度</mark>] $$\forall E, F \in \Sigma,  E \subseteq F \Rightarrow \mu (E) \leq \mu(F)$$​
> * <mark style="color:red;">可得集合的大小與測度值有單調的關係</mark>。

proof:

* 因為$$E \subseteq F$$，可得 $$F = E \cup (F -E)$$。
* 由測度定義得 $$\mu(F) = \mu (E) + \mu (F-E)$$且$$\mu(F-E) \geq 0$$。
* 因此$$\mu(E) \leq \mu(F)$$ (QED)

> * <mark style="color:blue;">\[補集的測度]</mark> $$\forall E, F \in \Sigma, E \subseteq F$$且$$\mu(F) < \infty$$，則$$\mu(F -E) = \mu(F) - \mu(E)$$
> * $$\mu(F)$$必須是有限值才有意義。

### 測度的次可加性

證明同上。

> * \[<mark style="color:blue;">次可加性 ,sub-additive</mark>] $$\forall E,F \in \Sigma, ~\mu(E \cup F) \leq \mu(E)+\mu(F)$$
> * \[<mark style="color:blue;">有限次可加性, finitely sub-additive</mark>] $$\forall E_1,E_2, \ldots,E_n \in \Sigma$$$$\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i ) \leq \sum_{i=1}^n\mu(E_i )$$
> * \[<mark style="color:blue;">可數次可加性, countable sub-additive</mark>] $$\forall E_1,E_2, \ldots \in \Sigma$$$$\Rightarrow \mu(\cup_{i=1}^\infty E_i ) \leq \sum_{i=1}^\infty \mu(E_i)$$>

proof:

* $$E \cup F = E \cup (F - E)$$
* 由測度定義得 $$\mu(E \cup F) = \mu(E) + \mu(F-E)$$
* 因為$$F-E \subseteq F$$可得$$\mu(F-E) \leq \mu(F)$$
* 因此 $$\mu(E \cup F) \leq \mu (E) +\mu(F)$$ (QED)

Proof:

* 令$$F_1=E_1, ~F_2=E_2−E_1, ~F_3=E_3−(E_1 \cup E_2 ), \ldots , F_n=E_n−(E_1 \cup \ldots \cup E_{n−1} )$$
* 可得$$F_n$$ 為$$E_n$$ 的子集合 ($$F_n \subseteq E_n$$ )，且$$\{F_n\} \subseteq \Sigma$$為互斥的集合序列 $$F_i \cap F_j=\emptyset, ~ \forall i \neq j$$  。
* $$\displaystyle \mu(\bigcup_{i=1}^\infty E_i )=\mu(\bigcup_{i=1}^\infty F_i )=\sum_{i=1}^\infty \mu(F_i )  \leq \sum_{i=1}^\infty \mu(E_i )$$   (QED).

### 有限測度與sigma有限測度

> 如果對宇集合可得$$\mu(X)<\infty$$> ，則稱$$\mu$$為<mark style="color:red;">有限測度（finite measure）</mark>。

* $$\mu(\mathbb{R})=\infty$$，因此實數的長度不是有限測度。
* <mark style="color:blue;">所有的機率測度都是有限測度</mark>，因為$$\mu(\Omega) =1$$。

> \[<mark style="color:blue;">sigma-finite measure</mark>] $$\exists \{E_n \}\subseteq \Sigma, ~ X=\bigcup_n E_n  \ni \mu(E_n )< \infty, ~ \forall n$$

* 實數的長度不是有限測度，<mark style="color:blue;">但實數的長度是sigma有限測度</mark>，因為可將實數拆解為多個有限長度的線段的聯集。$$\mathbb{R} = \cdots \cup [-n, -n+1] \cup \cdots \cup[-1,1]\cup [1,2]\cup \cdots \cup [n, n+1] \cup \cdots$$且$$\mu([n, n+1])=1, \forall n$$。

### 非互斥集合聯集與交集測度之和等於各別集合測度之和(排容原理)

> $$\forall E,F \in \Sigma \Rightarrow \mu(E \cup F)+\mu(E \cap F)=\mu(E)+\mu(F)$$

Proof:

* $$E \cup F=E \cup (F−E)$$
* 所以 $$\mu(E \cup F)=\mu(E)+\mu(F−E)$$
* 若$$\mu(E \cap F)=\infty$$，因為$$E \cap F \subseteq E \cup F$$，所以$$\mu(E \cup F)=\infty$$
* 若$$\mu(E \cap F)< \infty$$, $$\mu(F−E)=\mu(F−(E\cap F))=\mu(F)−\mu(E\cap F)$$
* $$\mu(E \cup F)= \mu(E)+\mu(F)−\mu(E\cap F)$$ (QED)

### 遞增集合極限的測度(可穿過極限符號)

> * $$\displaystyle \forall E_1,E_2, \ldots  \in \Sigma, ~ E_i \subseteq E_j, ~\forall i \leq j \Rightarrow \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$
> * 因為$$\Sigma$$內最大的集合為宇集合$$X$$，因此遞增集合最多和宇集合一樣大。
> * 如果$$\mu(E_1)=\infty$$，此性質仍然成立。

proof:

* $$\displaystyle  \lim_{n \rightarrow \infty}⁡ E_n=\bigcup_{n=1}^\infty E_n=E_1 \cup (E_2−E_1 )\cup (E_3−E_2 )\cup \ldots$$
* 所以$$\begin{align} \displaystyle \mu(\lim_{n \rightarrow \infty}⁡ E_n )   & =\mu(\bigcup_{n=1}^\infty E_n) \\ &=\mu(E_1 )+\mu(E_2−E_1 )+\mu(E_3−E_2 )+\ldots \\ & =\lim_{n \rightarrow \infty}⁡\{\mu(E_1 )+\mu(E_2−E_1 )+\mu(E_3−E_2 )+\\ &\ldots+\mu(E_n−E_{n−1} )\} -- (1)\end{align}$$
* 因為$$E_1, E_2-E_1, \ldots, E_n - E_{n-1}$$為兩兩互斥的集合，且$$E_1 \cup(E_2-E_1) \cup \ldots \cup (E_n - E_{n-1})= E_n$$
* 因此$$\mu(E_1) + \mu(E_2 - E_1) + \ldots \mu(E_n - E_{n-1}) = \mu(E_n) -- (2)$$
* 由(1,2)得 $$\displaystyle \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$ (QED)

### &#x20;遞減集合極限的測度(可穿過極限符號)

> $$\displaystyle \forall E_1,E_2, \ldots  \in \Sigma, ~ E_i \supseteq E_j, ~\forall i \leq j$$且$$\exists n_0 \in \mathbb{N}, \mu(E_{n_0}) < \infty$$，則$$\displaystyle \lim_{n \rightarrow \infty }⁡ \mu(E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$
>
> * $$\exists n_0 \in \mathbb{N}  \mu(E_{n_0} )<\infty$$  意思是某一個集合的測度有限，因為$$E_n$$為遞減集合，因此在$$n_0$$之後的集合之測度也為有限值，可避免所有的集合之測度均為無窮大的情況。
> * 若$$\mu(E_n )=\infty ~\forall n$$，則此性質不成立。

Proof

* $$\displaystyle \lim_{n \rightarrow \infty} \mu(E_n )$$  在$$n_0$$之前的集合不會影響此值  。同樣$$\displaystyle \mu(\lim_{n \rightarrow \infty}E_n )$$在$$n_0$$ 之前的集合也不會影響此值，因此只要考慮$$n_0$$ 之後的集合即可。
* $$E_{n_0}−E_n \in \Sigma$$ 且$$E_{n_0}−E_{n_0 + 1} \subseteq E_{n_0}−E_{n_0+2}$$為遞增的集合序列&#x20;  。
* &#x20;所以$$\displaystyle \lim_{n \rightarrow \infty} \mu(E_{n_0 }−E_n )=\mu(\lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n  ))$$
* 因為 $$\mu(E_{n_0} −E_n )=\mu(E_{n_0} )−\mu(E_n)$$ (兩者均為有限值)
* 所以 $$\displaystyle \lim_{n \rightarrow \infty} \mu(E_{n_0}−E_n )=\lim_{n \rightarrow \infty}⁡\mu(E_{n_0})−\lim_{n \rightarrow \infty} \mu(E_n )=\mu(E_{n_0})−\lim_{n \rightarrow \infty}\mu(E_n)$$
* &#x20;因為$$\{E_n\}$$為遞減集合序列，所以$$\displaystyle \lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n )=\bigcup_n (E_{n_0}−E_n )=E_{n_0}−\left(\bigcap_n E_n \right)$$
* $$\displaystyle A−\lim_{n \rightarrow \infty}E_n =(A−E_1 ) \cup (A−E_2 ) \cup \ldots =(A \cap E_1^c )\cup (A \cap E_2)^c )\cup \ldots =A−(\cap_n E_n )$$
* 所以$$\displaystyle \mu(\lim_{n \rightarrow \infty}⁡(E_{n_0}−E_n ) )=\mu(E_{n_0 }−(\bigcap_n E_n ))=\mu(E_{n_0} )− \mu(\cap_n E_n )$$
* $$\displaystyle \mu(E_{n_0} )−\lim_{n \rightarrow \infty}  \mu(E_n )= \mu(E_{n_0} )−\mu(\bigcap_n E_n )$$
* $$\displaystyle  \lim_{n \rightarrow \infty}\mu(E_n )=\mu(\bigcap_n E_n )=\mu(\lim_{n \rightarrow \infty}⁡E_n )$$ (QED)

#### 範例

* $$E_n=[0, 1+\frac{1}{n}] \subseteq \mathbb{R}$$為遞減的集合
* $$\mu(E_n )=1+\frac{1}{n  }$$
* $$\displaystyle \lim_{n \rightarrow \infty}E_n = \lim_{n \rightarrow \infty}⁡[0, 1+\frac{1}{n}]=[0,1]$$
* 所以 $$\displaystyle \mu(\lim_{n \rightarrow \infty} E_n )=1$$
* 而$$\displaystyle  \lim_{n \rightarrow \infty} \mu(E_n )= \lim_{n \rightarrow \infty}⁡(1+\frac{1}{n})=1$$











