---
description: measurable set
---

# 可測集合

## 可測集合定義

> 給定集合$$E\subseteq S$$，若對於任意的集合$$A \subseteq S$$均滿足：$$m^{*}(A) = m^{*}(A\cap E) + m^{*}(A \cap E^c)$$，則稱$$E$$為可測集合(Caratheodory measurable set)。

若$$E$$為可測集合，則對於任意集合$$A$$，且$$E \cap A=\empty$$，由定義可得：$$m^{*}(E \cup A) = m^{*}((E \cup A) \cap E) + m^{*}(( E\cup A) \cap E^c)=m^{*}(E) + m^{*}(A)$$

## 可測集合的充分必要條件

> 若$$E$$為可測集合，則對於任意的集合$$A$$，必須滿足$$m^{*}(A) \geq m^{*}(A\cap E) + m^{*}(A \cap E^c)$$
>
> 此不等式在$$m^{*}(A)=\infty$$時也成立。

proof:

由於$$A=(A \cap E) \cup(A \cap E^c)$$且外測度滿足次可加性，因此性質$$m^{*}(A) \leq  m^{*}(A \cap E) + m^{*}(A \cap E^c)$$必定成立。

因此要證明$$m^{*}(A) = m^{*}(A\cap E) + m^{*}(A \cap E^c)$$只要證明$$m^{*}(A) \geq m^{*}(A\cap E) + m^{*}(A \cap E^c)$$即可。(QED)

## 零測度與可數集合均為可測集合

> 可數集合的外測度為0，因此只須證明0測度集合為可測集合。

proof:&#x20;

令$$E$$為外測度為0的集合，$$A$$為任意集合。

因為$$A\cap E \subseteq E$$且$$A \cap E^c \subseteq A$$ ，由外測度的單調性可得：$$m^{*}(A \cap E) \leq m^{*}(E) =0$$ 且 $$m^{*}(A \cap E^c) \leq m^{*}(A)$$

因此 $$m^{*}(A) \geq m^{*}(A \cap E^c) = 0 + m^{*}(A \cap E^c) = m^{*}(A \cap E) + m^{*}(A \cap E^c)$$ (QED)

## 可測集合的有限聯集仍為可測集合



## 可測集合的可數聯集仍為可測集合



## 實數上任意區間均為可測集合



## 可測集合經平移後仍為可測集合
