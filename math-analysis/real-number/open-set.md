---
description: open and closed set
---

# 開集合(open set)

## 簡介

定義開集合或閉集合，需要用到距離的概念，因此至少需要定義集合中兩點的度量(metric)。 由於度量在$$\mathbb{R}^n$$與$$\mathbb{R}$$在開集與閉集兩者性質通用，因此直接以$$\mathbb{R}^n$$定義。

## 度量函數(metric function)

> 集合$$\mathbb{R}^n$$的函數$$d: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$ 滿足以下三個條件時，稱為度量函數。
>
> * <mark style="color:red;">\[非負性]</mark> $$\forall x, y \in \mathbb{R}^n, ~ d(x,y) \geq 0$$, 且$$d(x,y) =0 \Leftrightarrow x=y$$。
> * <mark style="color:red;">\[交換性]</mark> $$\forall x, y \in \mathbb{R}^n, ~ d(x, y) = d(y, x)$$。
> * <mark style="color:red;">\[三角不等式]</mark> $$\forall x, y, z \in \mathbb{R}^n, ~ d(x,y) \leq d(x, z) + d(z, y)$$。

歐式空間常用的度量函數為$$\displaystyle d(x,y)=\lVert x-y \rVert = (\sum_{i=1}^n (x_i - y_i)^2)^{1/2}$$。

距離函數為$$d(x,y)$$只要滿足上述定義即可，因此不一定是以$$a$$為中心的圓形，可能是菱形或是方形。$$d(a,b)=|a−b|$$為菱形。

## 開球(open ball)

> 令點$$x \in \mathbb{R}^n$$且半徑$$r > 0$$
>
> * $$B_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) < r \}$$ 是以$$x$$為圓心，半徑為$$r$$開球 (open ball with center $$x$$ and radius $$r$$)。
> * $$\overline{B_r}(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) \leq r \}$$ 是以$$x$$為圓心，半徑為$$r$$閉球 (closed ball with center $$x$$ and radius $$r$$)。
> * $$S_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) =r \}$$ 是以$$x$$為圓心，半徑為$$r$$的球面 (sphere with center $$x$$ and radius $$r$$)。

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
>
> * $$x$$為集合$$S$$的內點若存在$$r >0 \ni B_r(x) \subseteq S$$。
> * <mark style="color:blue;">集合</mark>$$S$$<mark style="color:blue;">所有的內點形成的集合記為</mark>$$S^0$$。

鄰域為開集合，因為所有的元素均為內點。

如果$$x$$為孤立點時($$\exists r>0 \ni B_r(x) \cap S =\{x\}$$)，此時$$B_r(x)$$包含了許多不屬於$$S$$中的元素，因此$$B_r(x) \not \subseteq S$$，因此<mark style="color:red;">孤立點不是內點</mark>。

### 內點集必為集合的子集

> $$\forall S \subseteq \mathbb{R}^n$$, 可得$$S^0 \subseteq S$$。
>
> 註：<mark style="color:red;">當</mark>$$S^0=S$$<mark style="color:red;">時，則</mark>$$S$$<mark style="color:red;">為開集合</mark>。

<details>

<summary>proof: 由內點定義直接證明</summary>

令$$p \in S^0$$，由內點定義得$$\exists r > 0 \ni N_r(p) \subseteq S$$。 因為$$\forall p \in S^0$$均滿足上述的性質，因此得$$S^0 \subseteq S$$ (QED)

</details>

### 歐式空間的內點為極限點

> 給定集合$$S\subseteq \mathbb{R}^n$$，內點$$x \in S$$（$$\exists r > 0 \ni B_r(x) \subseteq S$$）， 則$$x$$為$$S$$的極限點（$$\forall r > 0,~ B_r(x) \cap S - \{x\} \neq \emptyset$$）。
>
> 註：一般拓墣空間不一定成立。
>
> 反過來說，<mark style="color:red;">如果</mark>$$x$$<mark style="color:red;">不是極限點時，則不是內點</mark>。
>
> <mark style="color:red;">孤立點不是極限點，因此孤立點不是內點</mark>。

<details>

<summary>proof: 極限點必定和集合有無窮多個交點</summary>

當$$x \in S$$為內點時，則$$\exists r > 0 \ni B_r(x) \subseteq S$$包含了$$S$$的無窮多個元素，

即使扣除掉點$$x$$，$$B_r(x)$$與$$S$$的交集也不是空集合，因此$$x$$為極限點。(QED)

</details>

### 內點的性質

> 給定集合$$A,B \subseteq \mathbb{R}^n$$，則
>
> 1. $$A\subseteq B \Rightarrow A^0 \subseteq B^0$$
>    * 反之不成立，考慮孤立點不為內點的情形。$$A=\{0\} \cup [1,2]$$, $$B=[0.5, 2.5]$$, $$A^0=(1,2),~ B^0=(0.5, 2.5)$$可得 $$A^0 \subset B^0$$但$$A \nsubseteq B$$。
> 2. $$(A\cap B)^0=A^0 \cap B^0$$
> 3. $$A^0 \cup B^0 \subset (A \cup B)^0$$
> 4. $$A^0=\mathbb{R}^n-\overline{\mathbb{R}^n-A}$$，$$\overline{\mathbb{R}^n-A}$$為$$\mathbb{R}^n-A$$的閉包（closure）。
> 5. $$(\mathbb{R}^n-A)^0=\mathbb{R}^n-\overline{A}$$
> 6. $$((A)^0)^0=A^0$$
> 7. $$\displaystyle (\bigcap_{i=1}^nA_i)^0=\bigcap_{i=1}^n A_i^0, ~ A_i \subseteq \mathbb{R}^n$$
> 8. $$\displaystyle (\bigcap_{i=1}^{\infty} A_i)^0 \subseteq \bigcap_{i=1}^{\infty} A_i^0, ~ A_i \subseteq \mathbb{R}^n$$
> 9. $$\displaystyle \bigcup_{i=1}^{\infty} A_i^0 \subseteq \bigcup_{i=1}^{\infty} A_i^0, ~ A_i \subseteq \mathbb{R}^n$$
> 10. 若$$A$$在$$\mathbb{R}^n$$中為開集合或閉集合，令$$A^b$$為$$A$$的邊界集，則$$(A^b)^0=\emptyset$$，
> 11. 若$$A^0=B^0=\emptyset$$，則$$A$$在$$\mathbb{R}^n$$為閉集合，則$$(A \cup B)^0=\emptyset$$

<details>

<summary>proof: 1</summary>

令$$x \in A^0$$，由內點定義得$$\exists r > 0 \ni N_r(x) \subseteq A$$。

因為$$A \subseteq B$$，所以 $$N_r(x) \subseteq B$$，因此$$x \in B^0$$ (QED)

</details>

<details>

<summary>proof: 2</summary>

令$$x \in (A\cap B)^0$$, 由內點定義得$$\exists r > 0 \ni N_r(x) \subseteq (A\cap B)$$。

因此$$N_r(x) \subseteq A$$ 且 $$N_r(x) \subseteq B$$。(QED)

</details>

<details>

<summary>proof: 3</summary>

令$$x \in A^0 \cup B^0$$，依內點定義$$\exists r_1 >0 \ni B_{r_1}(x) \subseteq A$$， 或$$\exists r_2 > 0 \ni B_{r_2} (x) \subseteq B$$。

取$$r = \min{r_1, r_2}$$, 可得\$$B\_r(x) \subseteq (A \cup B) (QED)

</details>

<details>

<summary>proof: 4</summary>



</details>

## 不相交集與非重疊集

> $$A, B \in \subseteq \mathbb{R}^n$$
>
> 定義若$$A \cap B = \empty$$，則稱$$A, B$$為<mark style="color:red;">不相交集</mark>。
>
> 定義若內點集$$A^0 \cap B^0 = \empty$$，則稱$$A, B$$為<mark style="color:red;">非重疊集</mark>。

非重疊集的邊界點可能相交，如$$A=[0,1]~B=[1,2]$$，則$$A^0=(0,1)~B^0=(1,2),~A^0\cap B^0=\empty$$。

## 外點(exterior point)

> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
>
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \subseteq \mathbb{R}^n - S$$。
> * <mark style="color:blue;">集合</mark>$$S$$<mark style="color:blue;">所有的外點形成的集合記為</mark>$$S^e$$。&#x20;
>
> 註：邊界點$$x$$的任意開球至少有一點在集合$$S$$內，且至少有一點在集合$$S^c$$。

## 外點集為集合補集的內點集

> $$\forall S \subseteq \mathbb{R}^n$$, $$S^e = (\mathbb{R}^n - S)^0$$ 且 $$S^e \subseteq \mathbb{R}^n - S$$。

<details>

<summary>proof: 由定義直接證明</summary>



</details>

## 邊界點(boundary point)

> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
>
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \cap {R}^n \neq \empty$$且 $$B_r(x) \cap {R}^n - S \neq \empty$$。
> * 集合$$S$$所有的邊界點形成的集合記為$$S^b$$。

### 集合與其補集的邊界集相同

> $$\forall S \subseteq \mathbb{R}^n$$, $$S^b = (\mathbb{R}^n - S)^b$$。

<details>

<summary>proof: 由定義直接證明</summary>



</details>

### 邊界集合的性質

> 1. $$A \subset B$$不一定可得$$A^b \subset B^b$$。
> 2. $$A^b \cup B^b$$不一定可得 $$(A \cup B)^b$$。
> 3. $$A^b \cap B^b$$不一定可得 $$(A \cap B)^b$$。
> 4. $$\emptyset^b=\emptyset$$
> 5. $$\mathbb{Q}^b=\mathbb{R}$$

例如：

$$A=[1,2]$$的閉區間，$$A^b=\{1,2\}$$，$$B=[0,3]$$的閉區間，$$B^b=\{0,3\}$$

$$A \subseteq B$$但$$A^b \not \subset B^b$$

$$(A \cup B)^b = \{0,3\}$$, $$A^b \cup B^b=\{0,1,2,3\}$$

$$(A \cap B)^b = \{1,2\}$$, $$A^b \cap B^b = \emptyset$$

* 實數$$\mathbb{R}$$中，有理數$$\mathbb{Q}$$與無理數$$\mathbb{R - Q}$$的內部都是空集合，邊界都是$$\mathbb{R}$$。

### 有理數集和無理數集的內點集均為空集合，且邊界集均為實數

> * $$\mathbb{Q}^0 = \empty$$, $$(\mathbb{R} - \mathbb{Q})^0 = \empty$$
> * $$\mathbb{Q}^b = (\mathbb{R} - \mathbb{Q})^b = \mathbb{R}$$

<details>

<summary>proof: 有理數和無理數的稠密性得內點集均為空集且邊界集均為實數</summary>

取$$x \in \mathbb{Q}$$，由有理數的稠密性得任兩個有理數之間均存在無理數。

因此不存在$$r > 0$$使得$$B_r(x) \subseteq \mathbb{Q}$$。 所以$$\mathbb{Q}^0 = \empty$$。 (QED)

由邊界集定義與有理數稠密性可得$$\forall x \in \mathbb{Q}, ~\forall r>0$$, $$N_r(x) \cap \mathbb{Q} \neq \empty$$ 且 $$N_r(x) \cap (\mathbb{R}-\mathbb{Q}) \neq \empty$$。 因此 $$\mathbb{Q}^b = \mathbb{R}$$。 (QED)

同理由無理數的稠密性得$$(\mathbb{R} - \mathbb{Q})^0 = \empty$$ 且 $$(\mathbb{R} - \mathbb{Q})^b = \mathbb{R}$$。 (QED)

</details>

## 內點集、外點集、邊界集為歐式空間的分割(三一律)

> $$\forall S \subseteq \mathbb{R}^n$$
>
> * $$S^0 \cap S^e = \empty$$, $$S^0 \cap S^b = \empty$$, $$S^b \cap S^e = \empty$$。
> * $$S^0 \cup S^e \cup S^b= \mathbb{R}^n$$。

<details>

<summary>proof:</summary>

$$\forall S \subset \mathbb{R}^n$$，有以下的性質

* $$S^0 \subseteq S$$
* $$S^e = (\mathbb{R}^n - S)^0$$
* $$S^e \subseteq \mathbb{R}^n - S$$
* $$S^0 \cap S^e = \emptyset$$
* $$S^0 \cap S^b = \emptyset$$
* $$S^e \cap S^b = \emptyset$$
* $$S^0 \cup S^e \cup S^b = \mathbb{R}^n$$

因此點$$x \in S^0,~ x \in S^e, ~ x \in S^b$$只能有一個成立。 (QED)

</details>

## 開集合(open set)

> $$\forall S \subseteq \mathbb{R}^n$$，若$$S$$內每個點均為$$S$$的內點， 即$$\forall x \in S,~ \exists r > 0 \ni B_r(x) \subseteq S$$，則稱$$S$$為開集合。
>
> 依內點集的定義為$$S^0=S$$時，$$S$$為開集合。

* 由定義知開集合不包含單點(孤立點)。
* 實數的開集合為開區間$$(a,b)$$或者開區間的聯集$$\cup_{i=1}^\infty (a_i ,b_i)$$。

### 開球為開集合

> $$B_r(x) \subseteq \mathbb{R}^n$$為開球, 則$$B_r(x)$$為開集合。

<details>

<summary>proof: 由定義直接證明</summary>

令$$y \in B_r(x)$$, 則$$d(x,y)< r$$。

令$$h = r - d(x,y) > 0$$，取$$p \in \mathbb{R}^n$$且$$d(x, p) < h$$。

由三角不等式得$$d(x,p) \leq d(x,y) + d(y,p) < d(x,y) + r -d(x, y) <r$$。

因此$$p \in B_r(x)$$為內點，由定義得$$B_r(x)$$為開集合 (QED)

</details>

### 開集合等價於內點集

> $$S \subseteq \mathbb{R}^n$$為開集合 $$\Leftrightarrow ~ S=S^0$$

<details>

<summary>proof:</summary>

* <=

由內點集為集合的子集得 $$S^0 \subseteq S$$。

因為$$S = S^0$$，且$$S^0 \subseteq S$$，可得$$S \subseteq S^0$$。

即$$\forall x \in S$$均為內點，因此$$S$$為開集合 (QED)

* \=>

由內點集為集合的子集得 $$S^0 \subseteq S$$。

因為$$S$$為開集合，$$\forall x \in S$$均為內點，可得$$x \in S^0$$。

因此可得$$S = S^0$$ (QED)

</details>

### 空集合與歐式空間為開集合(同時也為閉集合)

<details>

<summary>proof: 由定義直接證明</summary>



</details>

### 任意開集合的聯集仍為開集合

> $$S_i, i \in I,$$為開集合，則$$\displaystyle \bigcup_{i \in I} S_i= S$$為開集合。
>
> 註：索引集合$$I$$可能是不可數集合或者是可數集合。

<details>

<summary>proof: 直接以開集合定義證明</summary>

令點$$x \in S$$，則存在$$n \in I \ni x \in S_{n}$$。

因為$$S_n$$為開集合，依定義得$$\exists r_n > 0 \ni B_{r_n}(x) \subseteq S_n$$。

因此可得$$B_{r_n}(x) \subseteq S$$，對於$$\forall x \in S$$均可得到此結果，因此$$S$$為開集合(QED)

</details>

### 有限個開集合的交集仍為開集合

> $$S_i, i=1,2,\dots, n$$為開集合，則$$\bigcap_{i=1}^n S_i = S$$為開集合。
>
> 註：可數個開集合的交集可能為閉集合。

<details>

<summary>proof: 由開集合定義直接證明</summary>

令點$$x \in S$$，對於$$i=1,2,\dots,n$$，依給定條件可得$$x \in S_i$$。

因為$$\forall i, ~ S_i$$為開集合，因此存在$$r_{x_i} > 0 \ni B_{r_{x_i}}(x) \subseteq S_i$$。

令$$r_x = \min\{ r_{x_i} ~|~ i=1,2,\dots, n\}$$, 則 $$B_{r_x}(x) \subsetq S_i, \forall i$$。

因對$$\forall x \in S$$均可得到上述結果，所以$$S$$為開集合(QED)

</details>

#### 範例：無限個開集合的交集可能為閉集

$$\forall n \in \mathbb{N}, ~ (-\frac{1}{n}, \frac{1}{n})$$均為開集合，但是$$\displaystyle \bigcap_{n=1}^\infty (-\frac{1}{n}, \frac{1}{n}) = \{0\}$$。

$$\forall a,b \in \mathbb{R}$$，$$\displaystyle [a,b]=\bigcap_{n=1}^\infty (a-\frac{1}{n}, b+\frac{1}{n})$$

### 開集合可表示為可數個開球的聯集

> 令$$\empty \neq S \subseteq \mathbb{R}^n$$， 則$$S$$為開集合 $$\Leftrightarrow$$ S可表示為可數個$$\mathbb{R}^n$$中開球的聯集。
>
> 註：此處$$S$$可為有界或無界的開集合。

<details>

<summary>proof: 反向&#x3C;=由可數個開集合的聯集仍為開集合可得證，因此只要證明=>方向即可</summary>



</details>

#### 實數中的每個非空開集合可表示成可數個兩兩不相交的開區間(有限或無限)的聯集

<details>

<summary>proof:</summary>



</details>
