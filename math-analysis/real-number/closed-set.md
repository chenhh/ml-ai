---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> 集合$$S \subseteq \mathbb{R}^n$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$$$S^c \equiv \mathbb{R}^n - S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup S^d$$。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點(附著點)。

在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。

由於閉集合的餘集是開集，許多性質可用De-Morgan定理證明。

實數上常見的閉集合為閉區間$$[a,b]$$，在$$n$$維空間則為閉球$$[a_1, b_1] \times [a_2, b_2] \times \cdots \times [a_n, b_n]$$。


### 閉集合包含其所有極限點
> * $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$$$\forall r > 0~ \exists y \in S -\{x\} \ni y \in B_r(x)$$
> * 而$$S$$所有極限點形成為集合為導集合$$S^d$$

<details>

<summary> proof:  </summary>

proof >= (閉集合的補集不包含原集合的極限點)

令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。

依開集合定義可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，

因此$$\exists r >0 \ni B_r(x) \cap S = \empty$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 (QED)。

proof <=

令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni B_r(x) \cap S = \empty$$，因此$$x$$不是$$S$$的附著點。

可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合(QED)。

</details>





