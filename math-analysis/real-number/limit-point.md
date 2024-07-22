---
description: limit point, adherent point
---

# 極限點(limit point)

## 簡介

極限點為集合的去心鄰域，而附著點為(含心)鄰域的概念，有些教科書只定義極限點。

<mark style="color:red;">集合內的元素，若非極限點時，則為孤立點</mark>。

集合內的元素全為極限點時，稱為<mark style="color:red;">完全集(perfect)</mark>。

## 附著點(adherent point)

> $$S \subseteq \mathbb{R}^n$$, $$x \in \$$$$x \in \mathbb{R}^n$$滿足 $$\forall r > 0, B_r(x) \cap S \neq \empty$$, 稱點$$x$$為為集合$$S$$的附著點。

* 由定義得$$x$$為集合$$S$$的附著點時，可得$$\forall \epsilon > 0, ~ \exists y \in S \ni d(x,y)<\epsilon$$。
* $$x$$為集合$$S$$附著點，<mark style="color:blue;">但</mark> $$x$$<mark style="color:blue;">不必為</mark>$$S$$<mark style="color:blue;">的元素</mark>，例如邊界點。
* 因為$$x$$的任意開球$$B_r (x)$$均包含集合$$S$$至少一個元素，因此$$x$$為$$S$$中的元素或在$$S$$的邊界點上。
* 若$$x$$在集合$$S$$的邊界點外（外點），則$$\exists r>0 \ni N_r (x) \cap S=\emptyset$$。

#### 範例

* 實數區間$$(a,b), [a,b], (a,b], [a,b)$$中的所有點都是附著點，而邊界點$$\{a,b\}$$也是附著點，但不一定為區間內的元素。

## 孤立點（isolated point）

> 集合$$S \subset \mathbb{R}^n$$，如果點$$x\in S$$且滿足 $$\exists r > 0 \ni B_r(x) \cap S = \{x\}$$，則稱$$x$$為孤立點。
>
> 若不是孤立點，則$$B_r(x) \cap S$$為不可數集合。

* 孤立點是存在$$x$$的某一個開球滿足條件即可。
* 由定義知<mark style="color:blue;">孤立點不是內點</mark>。因為若$$\exists r>0 \ni B_r (x) \subseteq S$$，可得$$B_r (x)\cap S=B_r (x) \neq \{x\}$$。
* 由定義知<mark style="color:blue;">孤立點不是極限點</mark>。因為極限點必定和集合相交無限多點，而孤立點只有和集合交於一點。
* 因為$$B_r (x) \cap S$$集合中只有一個點時，表示$$x$$附近沒有任何元素，即為孤立點。
  * 例如 $$S=\{1/n, \forall n \in \mathbb{N}\}$$，則$$S$$內的每一點都是孤立點。
  * 例如$$S=\{0\} \cup [1,2]$$，則0為孤立點。
  * 但$$S=\{0\} \cup \{ ,1, 1/2, 1/3,\ldots\}$$中，0不是孤立點，因為可以找到任意接近0的元素，但每一個$$1/k$$都是孤立點。

### 孤立點集合為可數集合

> • $$S \subseteq \mathbb{R}^n$$, 令$$Q$$為$$S$$中孤立點形成的集合，則$$Q$$為可數(有限或無限)集合。

<details>

<summary>proof: 以孤立點定義直接建構集合</summary>

若$$S$$中的孤立點為有限個，則$$Q$$為可數有限集合。

令$$S$$中孤立點個數為無限多個，考慮$$x \in S$$為孤立點，即 $$\exists r > 0 \ni N_r(x) \cap S =\{ x\}$$。

因為$$Q$$為孤立點的集合, 令$$r_1=\min⁡\{r >0~|~ \forall x \in Q, N_r (x) \cap S=\{x\}\}$$, 且令滿足此最小半徑的點為$$x_1$$， 則此點必定唯一，否則違反孤立點的定義。

從$$Q - \{x_1\}$$的集合中，可得$$r_2=\min \{ r>0 | \forall x \in Q - \{x_1\}, N_r (x) \cap S=\{x\} \}$$ 且令滿足此最小半徑的點為$$x_2$$。

以此類推，可得$$Q$$中的點與自然數集合$$\mathbb{N}$$有一對一的關係，因此$$Q$$為可數集合。 (QED)

</details>

### 歐式空間中孤立點是邊界點

> 給定集合$$S \subseteq \mathbb{R}^n$$，點$$x \in S$$為孤立點（$$\exists r >0 \ni B_r(x) \cap S = \{x\}$$）， 則$$x$$為邊界點（$$\forall r>0 , B_r(x) \cap S \neq \emptyset$$ 且 $$B_r(x) \cap S^c \neq \emptyset$$）

<details>

<summary>proof: 歐式空間可分為內點、邊界點、外點三類，而孤立點不是內點，也不是外點，因此為邊界點。</summary>

因為$$x\in S$$ 因此$$\forall r > 0, ~ x \in (B_r(x) \cap S)$$ 至少包含一點$$x$$ -- (1)

因為$$x \in S$$，但是$$x$$不是內點，所以$$\forall r >0, ~ B_r(x) \cap S^c \neq \empty$$ -- (2)

由(1,2)得$$x$$為邊界點(QED)

</details>

#### 範例：邊界點不一定是孤立點

例如$$S=[1,2]$$，邊界點集$$S^b=\{1,2\}$$，但都不是孤立點。

## 極限點(limit point)

> 集合$$S \subset \mathbb{R}^n$$，若點$$x\in \mathbb{R}^n$$滿足$$\forall r >0, \ni B_r(x) \cap S - \{x\} \neq \empty$$, 則稱點$$x$$為集合$$S$$的極限點。
>
> 極限點和附著點的差異在於極限點為去心鄰域和集合的交集不為空。

### 極限點必存在數列收斂在該點

> 集合$$S \subset \mathbb{R}^n$$，且 $$a \in \mathbb{R}^n$$為集合$$S$$的極限點。
>
> 則存在數列$$\{a_n\} \subseteq S$$ 滿足 $$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$。

<details>

<summary>proof: 直接建構</summary>

令$$a$$為集合$$S$$的極限點，由定義得$$\forall r > 0, B_r(a) \cap S - \{a\} \neq \empty$$。

因此$$\forall n \in \mathbb{N}$$，令半徑$$r = \frac{1}{n}$$，取點$$a_n \in B_r(a)$$。

可得$$d(a_n, a) < \frac{1}{n}$$

因此$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$ (QED)

</details>

## 導集合（derived set）

> 導集合$$S^d$$為集合$$S$$所有極限點形成的集合。
>
> $$S^d=\{x \in \mathbb{R}^n ~|~ \forall r >0, B_r(x) \cap S - \{ x\}\neq \emptyset \}$$

* 導集合$$d(S)$$和[閉包](closed-set.md#bi-bao-closure)$$\overline{S} = S \cup d(S)$$有重要的關聯性，參考[導集合的性質](closed-set.md#dao-ji-he-de-xing-zhi)。
* <mark style="color:blue;">導集合為閉集合</mark>。
* \[可數無限集有極限點] $$S=\{ \frac{1}{n}, \ n \in \mathbb{N}\}$$，則$$0$$為$$S$$的極限點。
* $$x_n=(-1)^n \frac{n}{n+1}$$極限不存在，但有兩個極限點-1與1。

![極限點為序列聚集之處](../../.gitbook/assets/800px-Rational\_sequence\_with\_2\_accumulation\_points\_svg.png)

## 完美集合（perfect set）

> $$S \subseteq \mathbb{R}^n$$稱為完全集合，若此集合等於其導集合，即$$S=S^d$$。
>
> 由定義得完全集合$$S$$內全部的元素均為極限點。

由下面的性質可知<mark style="color:red;">**完全集合為不含孤立點的閉集合**</mark>。但閉集合不一定是完全集，如包含孤立點的閉集合。

### 完美集合若且唯若集合不含孤立點且為閉集合

由 $$S=d(S)$$ 得$$S$$包含其所有極限點，因此完美集合$$S$$為閉集合。

若$$x \in S$$為孤立點，則 $$\exists r >0 \ni N_r(x) \cap S \setminus \{ x\} =\emptyset$$

但因為$$S=d(S)$$，因此$$\forall x \in S, N_r(x) \cap S \setminus \{x\} \neq \emptyset$$

所以$$S$$中不含孤立點。(QED)

### Cantor-Bendixon定理

> $$F \subseteq X$$ 為不可數閉集合，則可將$$F$$分解為$$F=A \cup B$$，$$A$$完美集合，$$B$$為可數集合。
>
> Note: 此定理說明<mark style="color:red;">**任意閉集合可分解為不含孤立點的閉集合與可數集合的聯集**</mark>。

<details>

<summary>proof</summary>

因為$$F$$為不可數集合, 因此存在$$x \in F$$為其凝聚點。令$$T$$為$$F$$所有凝聚點形成的集合。

由凝聚點的性質，得$$T$$為閉集合且$$T$$不含孤立點，且$$F \setminus T$$為可數集合。

令$$A=T$$, $$B=F \setminus T$$ 得證 (QED)

</details>
