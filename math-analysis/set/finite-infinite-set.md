# 有限集與無限集

有限集直觀上來說，就是集合內的元素可以一個一個數盡。無限多個元素表示我們無法一個一個的將元數盡。

![有限集、可數集、無限集、不可數集的關係](../../.gitbook/assets/finite\_countable\_set\_relation-min.png)

## 有限集與無限集 (finite and infinite set)

> $$\forall k \in \mathbb{N}$$, 令 $$\mathbb{N}_k \equiv \{1,2,\ldots, k\}$$
>
> 若存在$$k \in \mathbb{N} \ni A \sim \mathbb{N}_k$$(集合$$A$$等價於$$\mathbb{N}_k$$，兩者基數相同)，則稱$$A$$為<mark style="color:red;">有限集合</mark>，且包含$$k$$個元素 。
>
> 若$$A$$不是有限集，則$$A$$為無限集。
>
> <mark style="color:red;">空集合定義為有限集</mark>。

根據定義，若$$A\sim \mathbb{N}_k$$為非空有限集，則存在一對一且映成的函數$$f: \mathbb{N}_k \rightarrow A$$使得$$A=\{ f(1), f(2), \ldots, f(k)\}$$。

### 有限集的子集必為有限集

<details>

<summary>proof:使用數學歸納法即可證明</summary>

$$A=\emptyset$$，因為$$A$$只有空集合的子集，為有限集。

令$$A\sim \mathbb{N}_1$$，則$$A$$只有兩個子集，$$\emptyset$$與$$A$$，兩者均為有限集。

假設對含有$$k$$個元素的每個有限集均成立。

令$$B\subseteq A$$，若$$k+1 \notin B$$，則$$B\subseteq \mathbb{N}_k$$，因此$$B$$為有限集。

若$$k+1 \in B$$，令$$C=B \setminus \{k+1\}$$，則$$C \subseteq \mathbb{N}_k$$，即$$C$$為有限集。而$$B = C \cup \{ k+1 \}$$，所以$$B$$為有限集。

可得$$A$$有$$k+1$$個元素時的子集為有限集。

依數學歸納法可得有限集的子集為有限集。(QED)。

</details>

### 有限集不會等價於任意真子集

<details>

<summary>proof: 使用數學歸納法證明。</summary>

若$$A \sim \mathbb{N}_1$$，則$$A$$只有一個真子集$$\emptyset$$，但$$A$$不是空集合，所以兩者不等價。

\[歸納假設] 假設對於所有含有$$k$$個元素的每個有限集合均不等價於任意真子集。

令$$|A|=k+1$$，因為$$A\sim \mathbb{N}_{k+1}$$，所以$$A$$的每個真子集等價於$$\mathbb{N}_{k+1}$$的某個真子集。

\[反證法] 不失一般性，令$$A=\mathbb{N}_{k+1}$$，$$B\subset \mathbb{N}_{k+1}$$且$$B \sim \mathbb{N}_{k+1}$$，即存在一對一且映成的函數$$f: \mathbb{N}_{k+1} \rightarrow B$$。可分成$$B$$是否包含正整數$$k+1$$討論。

若$$k+1 \notin B$$，由假設知$$B \subset \mathbb{N}_{k+1}$$，去除一個元素仍為真子集，即$$B \setminus \{ f(k+1)\} \subset \mathbb{N}_{k+1}$$。

因為函數$$f$$為一對一且映成，去除掉一個元素後，仍為一對一且映成，變成$$f: \mathbb{N}_k \rightarrow B \setminus \{f(k+1)\}$$，可得$$B \setminus \{ f(k+1)\} \sim \mathbb{N}_k$$，但此與歸納假設矛盾。

若$$k+1 \in B$$且 $$f(k+1) = k+1$$，則$$B \setminus \{ (k+1)\} \subset \mathbb{N}_{k+1}$$，同上推論可得$$B \setminus \{ (k+1)\} \sim \mathbb{N}_k$$但此與歸納假設矛盾。

若$$k+1 \in B$$但$$f(k+1) \neq k+1$$，可定義函數$$g: B \rightarrow B$$使得;

* $$g(i) = i, \text{ if }i \neq k+1, i \neq f(k+1)$$
* $$g(i) = k+1, \text{ if } i = f(k+1)$$
* $$g(i) = f(k+1), \text{ if } i = k+1$$
* 則$$g$$為一對一且映成的函數，則合成函數$$g\circ f: \mathbb{N}_{k+1} \rightarrow B$$為一對一且映成的函數，同上推論可得與歸納假設矛盾的結果。

因此由數學歸納法可得有限集與不與其任何真子集等價 (QED)。

</details>

### 自然數為無限集

> 1. $$\forall a, b \in \mathbb{N}$$且$$a \neq b$$ 則 $$\mathbb{N}_a$$與$$\mathbb{N}_b$$不等價。
> 2. $$\mathbb{N}$$為(可數)無限集，則$$\mathbb{N}$$與$$\mathbb{N}_k, \forall k \in \mathbb{N}$$不等價。

<details>

<summary>proof: 有限集不等價。</summary>

1. 不失一般性 令$$a<b$$，則$$\mathbb{N}_a \subset \mathbb{N}_b$$且$$\mathbb{N}_b$$為有限集，因此兩者不等價 (QED)。

</details>

<details>

<summary>proof:[反證法]</summary>

令$$E$$為所有正偶數形成的集合，則$$E \subset \mathbb{N}$$。

令函數$$f: \mathbb{N} \rightarrow E$$, $$f(n)=2n, \forall n \in \mathbb{N}$$，則$$f$$為一對一且映成的函數。

依定義$$\mathbb{N} \sim E$$，但是有限集不會等價於其任意真正集，因此$$\mathbb{N}$$為無限集 (QED)。

</details>



## 可數與不可數集合 (countable and uncountable set)

> * 集合$$S$$與自然數集合$$\mathbb{N}$$存在單射(一對一)關係時，則該集合為可數集。因此有限集為可數集。
> * 如果$$S$$與$$\mathbb{N}$$是一對一且映成關係時，則$$S$$為無限可數集。
> * 如果$$S$$不是可數集時，則為不可數集。

可數集合可分為有限個元素(有限集)或是無限集(無限可數集)。

最小的無限集合為自然數，為可數無限集合。

## 不可數(無限)集合(uncountable (infinite) set)

> 不是可數集的無限集稱為**不可數集**。不可數集合與自然數集合$$\mathbb{N}$$不存在一對一且映成的關係，而且**不可數集合嚴格大於自然數集合的勢**$$\aleph_0$$。

不可數集合必為無限集合。

## 無限集合 (infinite set)

> <mark style="color:red;">無限集合是由無限個元素組成的集合，分為可數集與不可數集</mark>。

### 無限集的充要條件

### 無限集的充分必要條件

> * [存在自然數集合到它的(子集)的單射(一對一函數)] $$A$$為無限集 $$\Leftrightarrow$$ 存在 $$f: \mathbb{N} \rightarrow A$$為一對一函數。[集合$$A$$的勢大於等於自然數]
> * [無限集有至少一個真子集和它等勢] $$A$$為無限集 $$\Leftrightarrow A$$與其真子集等價。\[$$\exists B\subset A \ni A \sim B$$]

<details>

<summary>proof: <=數學歸納法 </summary>

* =>
若 $$\mathbb{N}$$至$$A$$ 存在一對一函數$$f: \mathbb{N} \rightarrow A$$。
則$$f: \mathbb{N} \rightarrow f(\mathbb{N})$$ 為一對一且映成的函數。
可得 $$\mathbb{N} \sim f(\mathbb{N})$$, 因此f(\mathbb{N}) 為無限集。
由於 $$f(\mathbb{N}) \subseteq A$$，因此 $$A$$為無限集。 (QED)

* <= 
若$$A$$為無限集。因此$$A \neq \empty$$。
選 $$x_1 \in A$$，因為 $$A$$與 $$\mathbb{N}_1$$不等價，所以 $$A - \{x_1\} \neq \empty$$。
再選 $$ x_2 \in A - \{x_1\}$$，則$$x_1$$與$$x_2$$為不同元素。
以此方法可在$$A$$中選出$$k$$個相異元素$$x_1, x_2, \dots, x_k$$。
因為$$A$$與 $$\mathbb{N}_k$$不等價，所以$$A-\{x_1, x_2, \dots, x_k\} \neq \empty$$。
由數學歸納法，可在$$A$$中得出子集$$\{x_k ~|~ k \in \mathbb{N}\}$$. 
且當$$k \neq l$$，可得$$x_k \neq x_l$$。
因此可定義函數$$f: \mathbb{N} \rightarrow A$$, $$f(k)=x_k$$為一對一函數(QED). 

</details>

<details>

<summary>proof: </summary>
* =>

* <=

</details>

無限集合有至少一個真子集合它等勢，其中一個例子是整數集合$$\mathbb{Z}$$與自然數集合$$\mathbb{N}$$等勢，兩者間存在一對一且映成的函數$$f=\Bigg\{ \begin{align}& \frac{n}{2} &,& n \text { is even} \\ &-\frac{n-1}{2} &,& n \text { is odd} \\ \end{align}$$

![自然數與整數為等價的集合](../../.gitbook/assets/natural\_integer\_mapping.png)

### 可數無限集合為無限集合的子集合

<details>

<summary> proof: 建構可數集合至無限集合的1-1函數。 </summary>

無限集合$$S$$可能為可數集合時滿足敘述，

令$$S$$為不可數集合。因此存在一對一函數$$f: \mathbb{N} \rightarrow S$$，可得數列$$\{f(n)\}_{ n \in \mathbb{N}} \ \subseteq S$$ (QED)

</details>

## 可數集合的子集合仍為可數集

<details>

<summary>proof: 直接證明</summary>

令$$S$$為(有限或無限)可數集，且$$E \subseteq S$$。

若$$E$$為有限集，則為可數集。

若$$E$$為無限集，則$$S$$為無限集。因為$$S$$為可數集，將$$S$$內的相異元素由小至大排列，形成數列$$\{s_1,s_2,\ldots\}$$。

* 定義函數$$k$$滿足條件:
  * $$k(1)$$之值為最小的正整數$$i_1$$使得$$s_{i_1} \in E$$。
  * $$k(2)$$為最小的正整數$$i_2$$，且$$i_2 > i_1$$使得 $$s_{i_2} \in E$$。
  * 依序得$$k(1), k(2), \ldots k(n-1)$$
  * 令$$k(n)$$為最小的正整數$$i_n$$, 且$$i_n > i_{n-1}$$使得$$s_{i_n} \in E$$。
  * 可得 $$n > (n-1) \Rightarrow k(n) > k(n-1)$$$$\forall n \in \mathbb{N}$$
  * 依此建構可得$$k: \mathbb{N} \rightarrow E$$為一對一且映成的函數，因此$$E \sim \mathbb{N}$$，則$$E$$為可數集 (QED)。

</details>

## 可數集合的聯集仍為可數集

> $$\forall n \in \mathbb{N}, \ S_n$$為可數集，則$$\cup_{n \in \mathbb{N}} S_n$$仍為可數集。

* 令$$S_n = \{n\}$$為具有單一整數的集合，則$$\cup_{n \in \mathbb{N}}S_n = \mathbb{N}$$

### 有理數集合為可數集

> * $$\forall n \in \mathbb{N}$$, $$S_n=\{ \frac{m}{n} | m \in \mathbb{Z} \}$$，則$$S_n \sim \mathbb{Z}$$，因此$$S_n$$為可數集。
> * $$\mathbb{Q}=\cup_{n\in \mathbb{N}} S_n$$，所以有理數集為可數集。

### 實數集合為不可數集合

因為$$[0,1]$$與$$\mathbb{R}$$兩集合等勢，因此只要證明$$[0,1]$$為不可數集合。

<details>

<summary>proof：反證法</summary>

假設$$[0,1]$$間的實數為可數集合，則可用數列$$\{s_n\}$$表示此集合，令$$s_n = 0.u_{n,1} u_{n,2} u_{n,3} \ldots$$，$$u_{n,i} \in \{ 0,1,\ldots, 9\}$$為無窮位數的小數。

令實數$$y=0.v_1 v_2 v_3 \ldots$$, $$v_n = \left\{ \begin{align} &1, \text{ if } u_{n,n} \neq 1, \\ &2, \text{ if } u_{n,n} = 1 \end{align} \right.$$

則$$y$$不與$$\{s_n\}$$中的任意值相同，如$$s_n=0.1999 \ldots \Rightarrow y=0.2000 \ldots$$

因此$$y \in [0,1]$$但$$y \notin \{s_n\}$$，即$$[0,1]$$是不可數集合 (QED)

</details>

### 二維整數的集合為可數集合

> $$\mathbb{Z}^+ =\{1,2,\ldots \}$$為正整數的集合，則$$\mathbb{Z}^{+} \times \mathbb{Z}^{+}$$為可數集合。

<details>

<summary>proof: 建構1-1函數</summary>

* 令函數$$f: \mathbb{Z}^{+} \times \mathbb{Z}^{+} \rightarrow \mathbb{Z}^{+}$$為$$f(m,n)=2^m 3^n$$，要證明$$f$$為一對一函數，即$$f(m_1, n_1)=f(m_2, n_2) \Rightarrow (m_1, n_1)=(m_2,n_2)$$。
* 若$$2^{m_1} 3^{n_1}=2^{m_2} 3^{n_2}$$，則$$2^{m_1 - m_2} 3^{n_1 - n_2}=1$$
* 因為$$gcd(2,3)=1$$，因此$$m_1-m_2=0$$且 $$n_1 - n_2=0$$, 即$$m_1=m_2$$且$$n_1 = n_2$$ (QED)

</details>
