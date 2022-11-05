---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> 集合$$S \subseteq \mathbb{R}^n$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S^c \equiv \mathbb{R}^n - S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup S^d$$。
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S$$包含其所有極限點(附著點)。

在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。

由於閉集合的餘集是開集，許多性質可用De-Morgan定理證明。

實數上常見的閉集合為閉區間$$[a,b]$$，在$$n$$維空間則為閉球$$[a_1, b_1] \times [a_2, b_2] \times \cdots \times [a_n, b_n]$$。


### 閉集合包含其所有極限點
> * $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$ $$\forall r > 0~ \exists y \in S -\{x\} \ni y \in B_r(x)$$
> * 令$$S$$所有極限點形成為集合為導集合$$S^d$$ (derived set)

<details>

<summary> proof: 閉集合的補集不包含原集合的極限點 </summary>

proof >= 

令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。

依開集合定義可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，

因此$$\exists r >0 \ni B_r(x) \cap S = \empty$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 (QED)。

proof <=

令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni B_r(x) \cap S = \empty$$，因此$$x$$不是$$S$$的附著點。

可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合(QED)。

</details>


### 有限多個閉集合的聯集仍為閉集合

> $$E_i \subseteq \mathbb{R}^n，~ i =1,2,\dots, N$$為閉集合，則$$\displaystyle \bigcup_{i=1}^N E_i$$為閉集合。
>
> 註：(可數或不可數)無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。

<details>

<summary> proof: DeMorgan定理 </summary>

 $$E_i$$為閉集合，則依定義$$E_i^c$$為開集合。

 由DeMorgan定理知 $$(E_1 \cup E_2)^c = E_1^c \cap E_2^c$$，因此$$E_1 \cup E_2 = (E_1^c \cap E_2^c )^c$$

 同理可得 $$\cup_{i=1}^n E_i=E_1 \cup E_2 \cup \dots \cup E_n = (E_1^c \cap E_2^c \cap \dots \cap E_n^c)^c$$

 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，
 且開集合的補集為閉集合，可得$$\displaystyle \bigcup_{i=1}^n E_i$$為閉集合。(QED)

</details>

### 無限個閉集合的交集仍為閉集合

> $$E_i \subseteq \mathbb{R}^n, ~ \ i \in I$$為閉集合，則 $$\displaystyle \cap_{i \in I} E_i$$為閉集合。
> 
> 指標集合$$I$$可能為可數集合或是不可數集合。

<details>

<summary> proof: DeMorgan定理 </summary>

因為$$E_i$$為閉集合，依定義$$E_i^c$$為開集合。

由DeMorgan定理知 $$\cap_{i \in I} E_i=(\cup_{i \in I} E_i^c)^c$$

因為[開集點的聯集仍是開集合](open-set.md#ren-yi-ke-shu-wu-xian-ge-kai-ji-he-de-lian-ji-reng-shi-kai-ji-he)，
而開集合的補集為閉集合，因此$$\cap_{i \in I} E_i$$ 為閉集合。(QED)

</details>



