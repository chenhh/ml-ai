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

## 實數中的有界單調數列必收斂

> $$\{a_n \}_{n \in \mathbb{N}} \subseteq \mathbb{R}$$為一有界單調數列，則$$\{a_n \}$$必定收斂至某一實數，即$$\displaystyle \lim_{n \rightarrow \infty} a_n =a \in \mathbb{R}$$
>
> * 若$$\{a_n\}$$為有上界遞增數列（$$a_1 \leq a_2 \leq \ldots \leq M$$），則$$\displaystyle \lim_{n \rightarrow \infty} a_n =\sup \{a_n | \forall n \in \mathbb{N}\}$$
> * 若$$\{a_n\}$$為有下界遞減數列（$$a_1 \geq a_2 \geq \cdots \geq N$$），則$$\displaystyle \lim_{n \rightarrow \infty} a_n =\inf\{a_n |\forall n \in \mathbb{N}\}$$
>
> 此定理告訴我們不必知道單調數列極限而能判定收斂數列的方法。

* 註: 由以下兩圖可知遞增（減）數列，因為有界數列，因此到了$$n \geq n_0$$的時候，可以上升（下降）的量就已經到達到了一個很小的範圍，此時就如同函數極限的定義一般，值域在一個很小的範圍$$\epsilon$$內變動，因此收斂。

Proof:

* 因為$$\{a_n\}$$有上界，由實數的最小上界性質\(非空有上界的集合必有最小上界\)得存在上確界 $$M=\sup\{a_n | n \in \mathbb{N}\} $$。
* 因為$$M$$為$$\{a_n\}$$的最小上界，由定義得$$\forall \epsilon>0~\exists n_0 \in \mathbb{N}   \ni M−\epsilon<a_{n_0}$$
* 取$$n \geq n_0$$ 時，$$M−\epsilon <a_{n_0} \leq a_n<M+\epsilon$$ \(QED\)



![&#x6709;&#x4E0A;&#x754C;&#x905E;&#x589E;&#x6578;&#x5217;&#x5FC5;&#x6536;&#x6582;](../../.gitbook/assets/increase-bounded-sequence-min.png)

![&#x6709;&#x4E0B;&#x754C;&#x905E;&#x6E1B;&#x6578;&#x5217;&#x5FC5;&#x6536;&#x6582;](../../.gitbook/assets/decrease-bounded-sequence-min.png)

### 有上\(下\)界收斂數列必存在收斂子數列

> $$\{a_n\}$$為有上（下）界收斂數列，且令$$\displaystyle \lim_{n \rightarrow \infty} a_n =a$$，則存在子數列$$\{a_{n_r} \}$$收斂至$$a$$，即$$\displaystyle \lim_{r \rightarrow \infty}⁡ a_{n_r}  =a$$。
>
> 註：只要為收斂收列，就存在收斂至同一點的子數列。

proof:

由[收斂數列的子數列必為收斂數列且收斂至同一點](./#shou-lian-shu-lie-de-zi-shu-lie-bi-wei-shou-lian-shu-lie-qie-shou-lian-zhi-tong-yi-dian)得證。\(QED\)

## 

