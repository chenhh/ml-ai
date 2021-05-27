---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> $$(X,d)$$為度量空間，集合$$S \subseteq X$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$$$S^c \equiv X \setminus S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup d(S)$$。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。

* 在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。
* 由於閉集合的餘集是開集，許多性質可用De Morgan定理證明。

### 閉集合包含其所有極限點

> * $$S \subseteq X$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。
> * $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$$$\forall r > 0~ \exists y \in S \setminus \{x\} \ni y \in N_r(x)$$
> * 而$$S$$所有極限點形成為集合為導集合$$d(S)$$

proof &gt;= \(閉集合的補集不包含集合的極限點\)

* 令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。
* 依開集合定義可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，因此$$ \exists r >0 \ni N_r(x) \cap S = \phi$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 \(QED\)。

proof &lt;=

* 令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni N_r(x) \cap S = \emptyset$$，因此$$x$$不是$$S$$的附著點。
* 可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合\(QED\)。

### 有限多個閉集合的聯集仍為閉集合

> $$A_n \subseteq X，~ n =1,2,\ldots, N$$為閉集合，則$$\cup_{n=1}^N A_n$$為閉集合。
>
> 註：無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$(A_1 \cup A_2)^c = A_1^c \cap A_2^c$$，因此$$A_1 \cup A_2 = (A_1^c \cap A_2^c )^c$$
* 同理可得 $$\cup_{n=1}^N A_n=A_1 \cup A_2 \cup \ldots \cup A_N = (A_1^c \cap A_2^c \cap \ldots \cap A_N^c)^c$$
* 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，可得$$\cup_{n=1}^N A_n$$為閉集合。\(QED\)

### 可數無限個閉集合的交集仍為閉集合

> $$A_n \subseteq X, ~ \ n \in \mathbb{N}$$為閉集合，則 $$\cap_{n =1}^\infty A_n$$為閉集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$\cap_{n=1}^\infty A_n=(A_1 \cap A_2 \cap \ldots )=(A_1^c \cup A_2^c \cup \ldots )^c$$
* 因為[可數無限個開集點的聯集仍是開集合](open-set.md#ren-yi-ke-shu-wu-xian-ge-kai-ji-he-de-lian-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，因此$$\cap_{n=1}^\infty A_n$$ 為閉集合。\(QED\)

### 開集合與閉集合的差集的性質

> $$A,B \subseteq X$$，若$$A$$為開集合，$$B$$為閉集合，則$$A\setminus B$$為開集合，$$B \setminus A$$為閉集合。

* $$A\setminus B = A \cap B^c $$，因為[有限個開集合的任意交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，因此為開集合。
* $$B\setminus A = B \cap A^c$$，因為可數無限個閉集合的交集仍為閉集合，因此為閉集合。

## 閉包（closure）

> $$S\subseteq X$$，$$d(S)$$為集合$$S$$的導集合（所有極限點的集合），定義閉包$$\overline{S} = S \cup d(S)$$。
>
> * $$d(S) = \{ x \in X | \forall r > 0, \ N_r(x) \cap S \setminus \{ x \} = \emptyset \}$$
> * 極限點$$x \in X$$不一定是$$S$$的元素。
>
> 定義2：$$\overline{S}=\cap\{ F \subseteq X | S \subset F \text{ and } F \text{ is closed set}  \}$$，即閉包為包含$$S$$的最小閉集合。

### 閉集合等於其閉包

> $$S \subseteq X$$為閉集合 $$\Leftrightarrow$$$$S= \overline{S}=S \cup d(S)$$

proof =&gt; 

* 因為 [閉集合包含其所有極限點](closed-set.md#bi-ji-he-bao-han-qi-suo-you-ji-xian-dian)，可得$$d(S) \subseteq S$$，所以$$\overline(S) = S \cup d(S) = S$$ \(QED\)

proof &lt;=

* 令$$x \in \overline{S}$$為極限點，則$$x$$為$$S$$或$$d(S)$$的極限點。
* 若$$x \in S$$，因為$$d(S)$$為所有$$S$$極限點的集合，因此$$x \in d(S)$$，所以$$x \in \overline{S}$$。
* 若$$x \in d(S)$$，因為$$d(S)$$為閉集合，所以$$d(S) \subseteq \overline{S}$$，可得$$x \in \overline{S}$$
* 所以$$S=\overline{S}$$包含所有極限點，因此$$S$$為閉集合。\(QED\)

### 導集合的性質

> $$d(S)$$為$$S$$的導集合，$$d(T)$$為$$T$$的導集合，閉包$$\overline{S}=S \cup d(S)$$，則
>
> 1. $$d(S)$$為閉集合，且$$d(d(S)) \subseteq d(S)$$
> 2. $$S \subseteq T \Rightarrow d(S) \subseteq d(T)$$
> 3. $$d(S \cup T)= d(S) \cup d(T)$$
> 4. $$d(\overline{S})=d(S)$$
> 5. $$\overline{S}$$為包含$$S$$的最小閉集合。

