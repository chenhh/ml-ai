# 機率測度\(probability measure\)

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

