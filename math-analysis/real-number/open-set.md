---
description: open and closed set
---

# 開集與閉集

## 簡介

定義開集合或閉集合，需要用到距離的概念，因此至少需要定義集合中兩點的度量(metric)。
由於$$\mathbb{R}^n$$與$$\mathbb{R}$$在開集與閉集兩者性質通用，因此直接以$$\mathbb{R}^n$$定義。

## 度量函數(metric function)
> 集合$$\mathbb{R}^n$$的函數$$d: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$
> 滿足以下三個條件時，稱為度量函數。
> * [非負性] $$\forall x, y \in \mathbb{R}^n, ~ d(x,y) \geq 0$$, 且$$d(x,y) =0 \Leftrightarrow x=y$$。
> * [交換性] $$\forall x, y \in \mathbb{R}^n, ~ d(x, y) = d(y, x)$$。
> * [三角不等式] $$\forall x, y, z \in \mathbb{R}^n, ~ d(x,y) \leq d(x, z) + d(z, y)$$。

歐式空間常用的度量函數為$$d(x,y)=\lVert x-y \rVert = (\sum_{i=1}^n (x_i - y_i)^2)^{1/2}$$。 

距離函數為$$d(x,y)$$只要滿足上述定義即可，因此不一定是以$$a$$為中心的圓形，可能是菱形。$$d(a,b)=|a−b|$$或是其它形狀。
* 鄰域為開集合，因為所有的元素均為內點

## 開球(open ball)
> 令點$$x \in \mathbb{R}^n$$且半徑$$r > 0$$
> * $$B_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) < r \}$$ 是以$$x$$為圓心，半徑為$$r$$開球
>   (open ball with center $$x$$ and radius $$r$$)。
> * $$\overline{B_r}(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) \leq r \}$$ 是以$$x$$為圓心，半徑為$$r$$閉球
>   (closed ball with center $$x$$ and radius $$r$$)。
> * $$S_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y)  r \}$$ 是以$$x$$為圓心，半徑為$$r$$的球面
>   (sphere with center $$x$$ and radius $$r$$)。

實數$$\mathbb{R}$$
* 開球$$B_r(x)$$即為開區間$$(x-r, x+r)$$。
* 閉球$$\overline{B_r}(x)$$即為閉區間$$[x-r, x+r]$$。
* 球面$$S_r(x)$$即為兩個點的集合$$\{x-r, x+r\}$$。

平面$$\mathbb{R}^2$$
* 開球$$B_r(x)$$為$$x$$為圓心，半徑為$$r$$的圓的內部。
* 閉球$$\overline{B_r}(x)$$為$$x$$為圓心，半徑為$$r$$的圓形區域。
* 球面$$S_r(x)$$為$$x$$為圓心，半徑為$$r$$的圓周。

## 內點(interior point)
> 令$$S \subseteq \mathbb{R}^n$$且$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的內點若存在$$r >0 \ni B_r(x) \subseteq S$$。
> * 集合$$S$$所有的內點形成的集合記為$$S^0$$。

### 內點集為集合的子集
> $$\forall S \subseteq \mathbb{R}^n$$, 可得$$S^0 \subseteq S$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

### 歐式空間中，內點一定是極限點

> 給定集合$$S\subseteq \mathbb{R}^n$$，內點$$x \in S$$（$$\exists r > 0 \ni N_r(x) \subseteq S$$），
> 則$$x$$為$$S$$的極限點（$$\forall r > 0  N_r(x) \cap S - \{x\} \neq \emptyset$$）。
>
> 註：一般拓墣空間不一定成立。

<details>

<summary>proof:  </summary>

* 當$$x \in S$$為內點時，則$$\exists r > 0 \ni N_r(x) \subseteq S$$包含了$$S$$的無窮多個元素，
* 即使扣除掉點$$x$$，$$N_r(x)$$與$$S$$的交集也不是空集合，因此$$x$$為極限點。(QED)

</details>

### 內點的性質

> 給定集合$$A,B \subseteq \mathbb{R}^n$$，則
>
> 1. $$A\subset B \Rightarrow A^0 \subset B^0 $$
>    * 反之不成立，考慮孤立點不為內點的情形。$$A=\{0\} \cup [1,2]$$, $$B=[0.5, 2.5]$$, $$A^0=(1,2),~ B^0=(0.5, 2.5)$$可得 $$A^0 \subset B^0$$但$$A \nsubseteq B$$。
> 2. $$(A\cap B)^0=A^0 \cap B^0$$
> 3. $$A^0 \cup B^0 \subset (A \cup B)^0$$
> 4. $A^0=\mathbb{R}^n-\overline{\mathbb{R}^n-A}$$，$$\overline{\mathbb{R}^n-A}$$為$$\mathbb{R}^n-A$$的閉包（closure）。
> 5. $$(\mathbb{R}^n-A)^0=\mathbb{R}^n-\overline{A}$$
> 6. $$((A)^0)^0=A^0$$
> 7. $$\displaystyle (\bigcap_{i=1}^nA_i)^0=\bigcap_{i=1}^n((A_i)^0), ~ A_i \subseteq \mathbb{R}^n$$
> 8. $$\displaystyle (\bigcap_{i=1}^{\infty} A_i)^0 \subseteq \bigcap_{i=1}^{\infty}((A_i^0), ~ A_i \subseteq \mathbb{R}^n$$
> 9. $$\displaystlyle \bigcup_{i=1}^{\infty} A_i^0 \subseteq \bigcup_{i=1}^{\infty} A_i^0, ~ A_i \subseteq \mathbb{R}^n$$
> 10. 若$$A$$在$$\mathbb{R}^n$$中為開集合或閉集合，令$$A^b$$為$$A$$的邊界集，則$$(A^b)^0=\emptyset$$，
> 11. 若$$A^0=B^0=\emptyset$$，則$$A$$在$$\mathbb{R}^n$$為閉集合，則$$(A \cup B)^0=\emptyset$$



## 外點(exterior point)
> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \subseteq \mathbb{R}^n - S$$。
> * 集合$$S$$所有的外點形成的集合記為$$S^e$$。
> 註：邊界點$$x$$的任意開球至少有一點在集合$$S$$內，且至少有一點在集合$$S^c$$。

## 外點集為集合補集的內點集
> $$\forall S \subseteq \mathbb{R}^n$$, $$S^e = (\mathbb{R}^n - S)^0$$ 且 $$S^e \subseteq \mathbb{R}^n - S$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

## 邊界點(boundary point)
> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \cap {R}^n \neq \empty$$且  $$B_r(x) \cap {R}^n - S \neq \empty$$。
> * 集合$$S$$所有的邊界點形成的集合記為$$S^b$$。

### 集合與其補集的邊界集相同
> $$\forall S \subseteq \mathbb{R}^n$$, $$S^b = (\mathbb{R}^n - S)^b$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>


### 有理數集和無理數集的內點集均為空集合，且邊界集均為實數

<details>

<summary>proof:  </summary>

</details>


## 內點集、外點集、邊界集為歐式空間的分割
>  $$\forall S \subseteq \mathbb{R}^n$$
> * $$S^0 \cap S^e = \empty$$, $$S^0 \cap S^b = \empty$$, $$S^b \cap S^e = \empty$$。
> * $$S^0 \cup S^e  \cup S^b= \mathbb{R}^n $$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

## 開集合(open set)
>  $$\forall S \subseteq \mathbb{R}^n$$，若$$S$$內每個點均為$$S$$的內點，
>   即$$\forall x \in S,~ \exists r > 0 \ni B_r(x) \subseteq S $$，則稱$$S$$為開集合。

由定義知開集合不包含單點(孤立點)。

### 開球為開集合
> $$B_r(x) \mathbb{R}^n$$為開球, 則$$$B_r(x)$$為開集合。

<details>

<summary>proof: 由定義直接證明</summary>

令$$y \in B_r(x)$$, 則$$d(x,y)< r$$。

令$$h = r - d(x,y) > 0$$，取$$ p \i \mathbb{R}^n$$且$$d(x, p) < h$$。

由三角不等式得$$d(x,p) \leq d(x,y) + d(y,p) < d(x,y) + r -(d,xy) <r$$。

因此$$p \in B_r(x)$$為內點，由定義得$$B_r(x)$$為開集合 (QED)

</details>


### 空集合與歐式空間為開集合(同時也為閉集合)
<details>

<summary>proof: 由定義直接證明</summary>

</details>

### 任意開集合的聯集仍為開集合
> $$S_i, i=1,2,\dots, \infty$$為開集合，則$$\bigcup_{i=1}^\infty S_i$$為開集合。 

<details>

<summary>proof:</summary>

</details>

### 有限個開集合的交集仍為開集合
> $$S_i, i=1,2,\dots, n$$為開集合，則$$\bigcap_{i=1}^n S_i$$為開集合。
> 註：可數個開集合的交集可能為閉集合。

<details>

<summary>proof:</summary>

</details>


#### 範例：無限個開集合的交集可能為閉集
$$ \forall n \in \mathbb{N}, ~ (-\frac{1}{n}, \frac{1}{n})$$均為開集合，

但是$$\displaystyle \lim_{n \rightarrow \infty} (-\frac{1}{n}, \frac{1}{n}) = \{0\}$$。


### 開集合等價於內點集
> $$S \subseteq \mathbb{R}^n$$為開集合 $$\Leftrightarrow ~ S=S^0$$

<details>

<summary>proof:

</summary>

</details>

### 開集合可表示為可數個開球的聯集
> 令$$\empty \neq S \subseteq \mathbb{R}^n$$，
> 則$$S$$為開集合 $$\Leftrightarrow$$ S可表示為可數個$$\mathbb{R}^n$$中開球的聯集。
> 註：此處$$S$$可為有界或無界的開集合。
> * <= 可數個開集合的聯集仍為開集合

<details>

<summary>proof:

</summary>

</details>

#### 實數中的每個非空開集合可表示成可數個兩兩不相交的開區間(有限或無限)的聯集

<details>

<summary>proof:

</summary>

</details>