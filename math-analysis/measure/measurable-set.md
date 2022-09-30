---
description: measurable set
---

# 可測集合

## 可測集合

> 給定集合$$E$$，若對於任意的集合$$A$$均滿足：$$m^{*}(A) = m^{*}(A\cap E) + m^{*}(A \cap E^c)$$，則稱$$E$$為可測集合(measurable set)。

若$$E$$為可測集合，則對於任意集合$$A$$，且$$E \cap A=\empty$$，可得：$$m^{*}(E \cup A) = m^{*}((E \cup A) \cap E) + m^{*}(( E\cup A) \cap E^c)=m^{*}(E) + m^{*}(A)$$

## 可測集合的充分必要條件

> 若$$E$$為可測集合，則對於任意的集合$$A$$，必須滿足$$m^{*}(A) \geq m^{*}(A\cap E) + m^{*}(A \cap E^c)$$
>
> 此不等式在$$m^{*}(A)=\infty$$時也成立。

proof:

由於$$A=(A \cap E) \cup(A \cap E^c)$$且外測度滿足次可加性，因此性質$$m^{*}(A) \leq  m^{*}(A \cap E) + m^{*}(A \cap E^c)$$必定成立。

因此要證明$$m^{*}(A) = m^{*}(A\cap E) + m^{*}(A \cap E^c)$$只要證明$$m^{*}(A) \geq m^{*}(A\cap E) + m^{*}(A \cap E^c)$$即可。(QED)

## 零測度與可數集合均為可測集合
