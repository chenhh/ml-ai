# 機率測度\(probability measure\)

* 出象\(outcome\)$$\omega$$為樣本空間$$\Omega$$的一個元素。
* 而樣本空間的任一子集稱為事件\(event\)，$$E \subseteq \Omega$$，因此事件中包含了許多的出像。
* sigma-field $$\mathcal{F}$$為滿足特定條件的事件集合的集合。
* 隨機變數$$X: \mathcal{F} \rightarrow \mathbb{R}$$為函數，將sigma-field中的元素\(事件\)，映射到實數值。因此給定實數值$$a$$，可得前像為事件集合的集合，可得$$X^{-1}(a) \in \mathcal{F}$$。
* 機率測度$$P$$量測的是滿足某個實數值$$a$$的前像\(事件集合的集合, $$X^{-1}(a)$$\)發生的機率。

給定機率空間為$$(\Omega, \mathcal{F}, P)$$

* $$\forall X \in \mathcal{F}, P(X^c)=1 - P(X)$$
* $$\forall X \in \mathcal{F}, 0 \leq P(X) \leq 1$$
* $$P(\emptyset)=0$$
* $$P(Y \cap X^c)=P(Y) - P(X \cap Y)$$
* $$P(X \cup Y) = P(X) + P(Y) - P(X \cap Y)$$
* If $$X \subseteq Y$$ then $$P(Y \setminus X) = P(Y) - P(X)$$ and $$P(X) \leq P(Y)$$
* \[Bonferroni inequality\] $$P(X \cap Y) \geq P(X) + P(Y) -1$$
* 令事件$$X_1, X_2, \ldots$$為$$\Omega$$的分割\(partition\)，即$$X_i \cap X_j = \emptyset,\ \forall i \neq j$$且 $$\cup_{i \in \mathbb{N}} X_i = \Omega$$，則$$P(Y) = \sum_{i \in \mathbb{N}} P(Y \cap X_i), \forall Y \in \mathcal{F}$$。
* \[Boole inequality\] $$P(\cup_{ i \in \mathbb{N}} X_i) \leq  \sum_{i \in \mathbb{N}} P(X_i)$$



## Q: 出象、事件、sigma-field、機率測度的關係為何？

