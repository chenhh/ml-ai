# 有限集與無限集

## 有限集與無限集 \(finite and infinite set\)

> $$\forall k \in \mathbb{N}$$, let $$\mathbb{N}_k \equiv \{1,2,\ldots, k\}$$
>
> 若存在$$k \in \mathbb{N} \ni A \sim \mathbb{N}_k$$\(集合$$A$$等價於$$\mathbb{N}_k$$\)，則稱$$A$$為有限集合，且包含$$k$$個元素。
>
> 若$$A$$不是有限集，則$$A$$為無限集。

根據定義，若$$A\sim \mathbb{N}_k$$為非空有限集，則存在一對一且映成的函數$$f: \mathbb{N}_k \rightarrow A$$使得$$A=\{ f(1), f(2), \ldots, f(k)\}$$。

### 有限集的子集必為有限集

若$$A$$為有限集，則對$$A$$的元素個數使用數學歸納法可證明。

* $$A=\emptyset$$，因為$$A$$只有空集合的子集，為有限集。
* 令$$A\sim \mathbb{N}_1$$，則$$A$$只有兩個子集，$$\emptyset$$與$$A$$，兩者均為有限集
* 假設對含有$$k$$個元素的每個有限集均成立。
* 令$$B\subseteq A$$，若$$ k+1 \notin B$$，則$$B\subseteq \mathbb{N}_k$$，因此$$B$$為有限集。
* 若$$k+1 \in B$$，令$$C=B \setminus \{k+1\}$$，則$$C \subseteq \mathbb{N}_k$$，即$$C$$為有限集。而$$B = C \cup \{ k+1 \}$$，所以$$B$$為有限集。
* 可得$$A$$有$$k+1$$個元素時的子集為有限集。
* 依數學歸納法可得有限集的子集為有限集。\(QED\)。

### 有限集不會等價於任意真子集

一樣使用數學歸納法證明。

* 若$$A \sim \mathbb{N}_1$$，則$$A$$只有一個真子集$$\emptyset$$，但$$A$$不是空集合，所以兩者不等價。
* 假設對於所有含有$$k$$個元素的每個有限集合均不等價於任意真子集。
* 令$$|A|=k+1$$，因為$$A\sim \mathbb{N}_{k+1}$$，所以$$A$$的每個真子集等價於$$\mathbb{N}_{k+1}$$的某個真子集。
* \[反證法\] 

### 自然數為無限集

> 1. $$\forall a, b \in \mathbb{N}$$且$$a \neq b$$ 則 $$\mathbb{N}_a$$與$$\mathbb{N}_b$$不等價。
> 2. $$\mathbb{N}$$為\(可數\)無限集，則$$\mathbb{N}$$與$$\mathbb{N}_k, \forall k \in \mathbb{N}$$不等價。

1.  不失一般性 令$$a<b$$，則$$\mathbb{N}_a \subset \mathbb{N}_b$$且$$\mathbb{N}_b$$為有限集，因此兩者不等價 \(QED\)。
2. \[反證法\]

* 令$$E$$為所有正偶數形成的集合，則$$E \subset \mathbb{N}$$。
* 令函數$$f: \mathbb{N} \rightarrow E$$, $$f(n)=2n, \forall n \in \mathbb{N}$$，則$$f$$為一對一且映成的函數。
* 依定義$$\mathbb{N} \sim E$$，但是有限集不會等價於其任意真正集，因此$$\mathbb{N}$$為無限集 \(QED\)。

### 無限集的充分必要條件

> * $$A$$為無限集 $$\Leftrightarrow$$存在$$f: \mathbb{N} \rightarrow A$$為一對一函數。\[集合A的勢大於自然數\]
> * $$A$$為無限集 $$\Leftrightarrow$$$$A$$與其真子集等價。\[$$ \exists B\subset A \ni A \sim B$$\]

## 可數集合 \(countable set\)

> 集合$$S$$與自然數集合$$\mathbb{N}$$存在單射\(一對一\)關係時，則該集合為可數集。
>
> 如果$$S$$與$$\mathbb{N}$$是一對一且滿射關係時，則$$S$$為無限可數集。

* 可數集合可分為有限個元素\(有限集\)或是無限集\(無限可數集\)。
* 最小的無限集合為自然數，為可數無限集合。

## 不可數\(無限\)集合\(uncountable \(infinite\) set\)

> 不是可數集的無限集稱為**不可數集**。不可數集合與自然數集合$$\mathbb{N}$$不存在一對一且映成的關係，而且**不可數集合嚴格大於自然數集合的勢**$$\aleph_0$$。

不可數集合必為無限集合。

## 無限集合 \(infinite set\)

> 無限集合是由無限個元素組成的集合。

> * 它有至少一個真子集和它等勢。
> * 存在自然數集合到它的\(子集\)的單射\(一對一函數\)。

無限集可分為可數集與不可數集。

無限集合有至少一個真子集合它等勢，其中一個例子是整數集合$$\mathbb{Z}$$與自然數集合$$\mathbb{N}$$等勢，兩者間存在一對一且映成的函數$$f=\Bigg\{ \begin{align}& \frac{n}{2} &,& n \text { is even} \\ &-\frac{n-1}{2} &,& n \text { is odd} \\ \end{align} $$

![&#x81EA;&#x7136;&#x6578;&#x8207;&#x6574;&#x6578;&#x70BA;&#x7B49;&#x50F9;&#x7684;&#x96C6;&#x5408;](../../.gitbook/assets/natural_integer_mapping.png)

## 可數集合的無限子集合仍為可數集

proof:

* 令$$S$$為可數集，且$$E \subset S$$。
* 因為$$S$$為可數集，將$$S$$內的相異元素由小至大排列，形成數列$$\{s_n\}$$。
* 建構數列 $$\{n_k\}$$如下：
  * 令$$n_1$$



## 實數上有限區間的實數集合不可數





