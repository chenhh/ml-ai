# 柯西數列\(Cauchy sequence\)

## 簡介

數列極限是否存在，依定義$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$必須要先知道收斂值$$a$$才可判定，而Cauchy數列只需知道數列中相鄰兩個元素間的距離是否足夠接近，即可判定數列是否收斂，而不需要知道收斂值。

## Cauchy數列

> $$(X,d)$$為度量空間，且$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列。若$$\forall \epsilon >0 ~ \exists n_0 \in \mathbb{N} \ni   d(a_n,a_m )<\epsilon ~ \forall n,m \geq n_0$$，則稱$$\{a_n\}$$為Cauchy序列。

* Cauchy序列的功能在於不須知道收斂值，只須檢定數列中元素的接近程度即可判別數列是否收斂。
* 任意度量空間中，由定或可得出收斂數列必為Cauchy數列。
* 實數空間中，因為實數的完備性，因此Cauchy數列必為收斂數列。反之一般的度量空間，必須是完備空間，才能夠保證Cauchy數列是收斂數列。

## 收斂數列必為Cauchy數列

> $$(X,d)$$為度量空間，且$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列。若$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$，則$$\{a_n\}$$為Cauchy數列。

* 任意度量空間中，由定義可得出收斂數列必為Cauchy數列。
* 實數空間中，因為實數的完備性，因此Cauchy數列必為收斂數列。反之一般的度量空間，必須是完備空間，才能夠保證Cauchy數列是收斂數列。

## Cauchy數列的子數列若收斂，則數列收斂至同一點

> $$\{a_n\}$$為Cauchy數列，若子數列$$\{a_{n_r} \}$$收斂，$$\displaystyle \lim_{r \rightarrow \infty} a_{n_r}  =a$$，則$$\displaystyle \lim_{n \rightarrow \infty} a_n =a$$。

* 度量空間中，[收斂數列的子數列必為收斂數列且收斂至同一點](./#shou-lian-shu-lie-de-zi-shu-lie-bi-wei-shou-lian-shu-lie-qie-shou-lian-zhi-tong-yi-dian)。反之必須要所有的子數列均收斂到同一點，才能保證原始數列收斂。**而Cauchy子數列簡化了此性質，只要Cauchy數列的子數列收斂，則可保證原數列收斂至同一點**。

Proof:

* $$\{a_n\}$$為Cauchy數列，且子數列$$\displaystyle \lim_{r \rightarrow \infty} a_{n_r} =a$$
* 由收斂定義得$$\forall \epsilon>0 ~ \exists n_1 \in \mathbb{N} \ni |a_{n_r}−a|<\epsilon, ~ \forall n \geq n_1 $$
* 因為$$\{a_n\}$$為Cauchy數列，所以$$\forall \epsilon>0 ~\exists n_2 \in \mathbb{N}   \ni |a_n−a_m |<\epsilon, ~\forall n,m \geq n_2$$
* 取$$n_0=n_1+n_2  $$
* 由三角不等式可得 $$|a_n−a| \leq |a_n−a_{n_0} |+|a_{n_0}−a|<\epsilon$$ \(QED\)

## 實數中的所有Cauchy數列都是有界數列

> $$\{a_n\} \subseteq \mathbb{R}$$為Cauchy數列，則$$\exists r > 0 \ni  |a_n| \leq r ~ ,\forall n$$

proof:

* 依Cauchy數列定義，給定$$\epsilon=1 ~\exists n_0 \in \mathbb{N} \ni |a_n−a_m |<1 ~\forall n,m \geq n_0 $$
* 因此當$$ n \geq n_0$$ 時，$$|a_n−a_{n_0} |<1 \Rightarrow |a_n |<|a_{n_0} |+1 $$
* 令$$r=\max \{|a_1 |, |a_2 |,\ldots,|a_{n_0−1} |, |a_{n_0} |+1\} $$
* 可得$$\forall n \in \mathbb{N}, ~ |a_n | \leq r$$
* 因此$$\{a_n\}$$為有界數列 \(QED\).





