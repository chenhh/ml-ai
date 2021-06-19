# 單調數列\(monotonic sequence\)

## 單調數列\(monotonic sequence\)

> $$(X,d)$$為度量空間，$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列，則：
>
> * 遞增數列\(increasing sequence\)：$$\forall i \leq j, ~ a_i \leq a_j  $$
> * 嚴格遞增數列\(strictly increasing sequence\)：$$\forall i \leq j, a_i<a_j  $$
> * 遞減數列\(decreasing sequence\)：$$∀i \leq j, a_i \geq a_j  $$
> * 嚴格遞減數列\(strictly decreasing sequence\)：$$\forall i \leq j, a_i>a_j  $$

## 有界數列 \(bounded sequence\)

> $$(X,d)$$為度量空間, $$\{a_n \}$$為一數列，則：
>
> * 有上界序列：$$\exists b \in X \ni \forall n \in \mathbb{N}, ~ a_n \leq b$$
> * 有下界序列：$$\exists a \in X \ni \forall n \in \mathbb{N},~ a_n \geq a$$
> * 有界序列：$$\exists m \in X\ni \forall n \in \mathbb{N}, ~ |a_n |\leq m$$
>
> 註：實數中的有界序列必落在一有界區間中。

### 收斂數列必為有界數列

> $$\{a_n\}$$為一序列且$$\displaystyle \lim_{n \rightarrow \infty}⁡ a_n =a \Leftrightarrow \{a_n\}$$有界 \(上界或下界\)
>
> 反之有界數列不一定成立，如$$\{a_n = \sin(n\pi)\}$$為有界數列$$|a_n| \leq 1$$，但不收斂。

Proof:

* $$\displaystyle \lim_{n \rightarrow \infty} a_n=a \Leftrightarrow \forall \epsilon>0 ~ \exists n_0 \in \mathbb{N}  \ni |a_n−a|<\epsilon ~ \forall n \geq n_0$$
* 所以 $$|a_n | \leq |a_n−a|+|a|<|a|+ϵ$$
* 令$$m=|a_1 |+|a_2 |+\cdots +|a_{n−1} |+|a|+\epsilon$$
* 可得 $$\forall n \in \mathbb{N},  ~|a_n |≤m$$ \(QED\)

