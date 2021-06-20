# 柯西數列\(Cauchy sequence\)

## 簡介

數列極限是否存在，依定義$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$必須要先知道收斂值$$a$$才可判定，而Cauchy數列只需知道數列中相鄰兩個元素間的距離是否足夠接近，即可判定數列是否收斂，而不需要知道收斂值。

## Cauchy數列

> $$(X,d)$$為度量空間，且$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列。若$$\forall \epsilon >0 ~ \exists n_0 \in \mathbb{N} \ni   d(a_n,a_m )<\epsilon ~ \forall n,m \geq n_0$$，則稱$$\{a_n\}$$為Cauchy序列。

* Cauchy序列的功能在於不須知道收斂值，只須檢定數列中元素的接近程度即可判別數列是否收斂。
* 任意度量空間中，由定或可得出收斂數列必為Cauchy數列。
* 實數空間中，因為實數的完備性，因此Cauchy數列必為收斂數列。反之一般的度量空間，必須是完備空間，才能夠保證Cauchy數列是收斂數列。

