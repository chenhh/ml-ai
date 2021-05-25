# 數列\(sequence\)

## 收斂與發散數列

> $$ \{a_n\} \subseteq \mathbb{R}$$ 稱為收斂數列若$$\displaystyle \lim_{n \rightarrow \infty} a_n = a \Leftrightarrow   \forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n -a| < \epsilon\ \forall n \geq n_0$$
>
> 常寫為 $$a_n \rightarrow a$$ as $$n \rightarrow \infty$$
>
> 如果$${a_n}$$不是收斂數列\(convergent sequence\)，則為發散數列\(divergent sequence\)。

* 數列收斂的直觀意義，是不論我們要使$$a_n$$ 與$$a$$接近到任何程度，只要$$n$$值夠大時一定能夠辦到。
* 由於實數的完備性，若$$\displaystyle \lim_{n \rightarrow \infty}⁡a_n$$ 收斂，收斂值必為實數且唯一。

![&#x6536;&#x6582;&#x6578;&#x5217;&#x6703;&#x5728;&#x6536;&#x6582;&#x503C;&#x9644;&#x8FD1;&#x8D8A;&#x7E2E;&#x8D8A;&#x8FD1;](../.gitbook/assets/limit_sequence-min.png)

### 收斂數列的唯一性

> 度量空間$$(X,d)$$中，$$\{ a_n\} \subseteq X$$為收斂數列，若 $$\displaystyle \lim_{n \rightarrow \infty} a_n = p$$且 $$\displaystyle \lim_{n \rightarrow \infty} a_n=q$$，則$$p=q$$

* $$\because a_n \rightarrow p \Leftrightarrow d(a_n, p) \rightarrow 0 $$as $$n \rightarrow \infty$$
* $$\because a_n \rightarrow q \Leftrightarrow d(a_n, q) \rightarrow 0 $$as $$n \rightarrow \infty$$
* 因為distance function $$d$$滿足三角不等式，因此$$0 \leq d(p, q) \leq d(p, a_n) + d(q, a_n) \rightarrow 0$$ as $$ n \rightarrow \infty$$
* 所以$$p=q$$ \(QED\)

### 收斂數列的四則運算仍為收斂數列

$$\displaystyle  \lim_{n \rightarrow \infty} a_n = a$$  and $$\displaystyle \lim_{n \rightarrow \infty} b_n = b$$均為收斂數列，則

* $$ \forall s, t \in \mathbb{R}$$,$$\displaystyle  \lim_{n \rightarrow \infty} (s a_n + t b_n) =  sa + tb$$
* $$\displaystyle \lim_{n \rightarrow \infty} (a_n b_n) = ab$$
* $$\displaystyle  \lim_{n \rightarrow \infty} \frac{a_n}{b_n} = \frac{a}{b}, \ \text{ if } b \neq 0$$

可由收斂數列的定義簡單得出。

### 收斂數列的子數列必為收斂數列

> $$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$收斂 $$\Rightarrow$$$$\displaystyle \lim_{i \rightarrow \infty} a_{n_i}=a$$收斂
>
> 反向不成立，因為子數列可能是從發散數列中得出。

proof:

$$\lim_{n \rightarrow \infty} a_n = a$$ converge $$ \Leftrightarrow $$$$\forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n - a| < \epsilon, \ \forall n \geq n_0$$

take $$i \geq n_0$$then $$n_i \geq i \geq n_0 \Rightarrow |a_{n_i} - a|<\epsilon$$ \(QED\)

### 數列奇數項與偶數項收斂至同一值，則數列數斂

> $$\displaystyle  \lim_{n \rightarrow \infty} a_{2n} = a$$且 $$\displaystyle  \lim_{n \rightarrow \infty} a_{2n+1} = a$$ $$\Rightarrow $$$$\displaystyle  \lim_{n \rightarrow \infty} a_n = a$$

proof:

$$ \forall \epsilon > 0 \  \exists n_0 \in \mathbb{N} \ni |a_{2n} - a| < \epsilon,  \forall 2n \geq n_0$$and $$ \exists n_1 \in \mathbb{N} \ni |a_{2n+1} - a| < \epsilon,  \forall 2n+1 \geq n_1$$

take $$n_3=2n_0+2n_1+1$$ then $$|a_n - a| < \epsilon\  \forall n \geq n_3$$\(QED\)

## 有界數列 \(bounded sequence\)

> $$\{ a_n \} \subseteq \mathbb{R}$$稱為有界數列若 $$\exists M \in \mathbb{R} \ni a_n \leq M , \forall n$$。



### 



