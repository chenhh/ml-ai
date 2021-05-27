---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> $$(X,d)$$為度量空間，集合$$S \subseteq X$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$$$S^c \equiv X \setminus S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup \partial(S)$$。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。

* 在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。
* 由於閉集合的餘集是開集，許多性質可用De Morgan定理證明。

### 有限多個閉集合的聯集仍為閉集合

> $$A_n \subseteq X，~ n =1,2,\ldots, N$$為閉集合，則$$\cup_{n=1}^N A_n$$為閉集合。
>
> 註：無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$(A_1 \cup A_2)^c = A_1^c \cap A_2^c$$，因此$$A_1 \cup A_2 = (A_1^c \cap A_2^c )^c$$
* 同理可得 $$\cup_{n=1}^N A_n=A_1 \cup A_2 \cup \ldots \cup A_N = (A_1^c \cap A_2^c \cap \ldots \cap A_N^c)^c$$
* 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，可得$$\cup_{n=1}^N A_n$$為閉集合。\(QED\)

