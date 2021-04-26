# 數列\(sequence\)

## 收斂與發散數列

> definition: 收斂數列
>
> $$ {a_n} \subseteq \mathbb{R}$$ and $$\lim_{n \rightarrow \infty} a_n = a \Leftrightarrow   \forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n -a| < \epsilon\ \forall n \geq n_0$$
>
> 如果$${a_n}$$不是收斂數列\(convergent sequence\)，則為發散數列\(divergent sequence\)。

![&#x6536;&#x6582;&#x6578;&#x5217;&#x6703;&#x5728;&#x6536;&#x6582;&#x503C;&#x9644;&#x8FD1;&#x8D8A;&#x7E2E;&#x8D8A;&#x8FD1;](../.gitbook/assets/limit_sequence-min.png)

### 收斂數列的四則運算仍為收斂數列

$$\lim_{n \rightarrow \infty} a_n = a$$  and $$\lim_{n \rightarrow \infty} b_n = b$$both are convergent sequences.

* $$ \forall s, t \in \mathbb{R}$$,$$ \lim_{n \rightarrow \infty} (s a_n + t b_n) =  sa + tb$$
* $$\lim_{n \rightarrow \infty} (a_n b_n) = ab$$
* $$\lim_{n \rightarrow \infty} \frac{a_n}{b_n} = \frac{a}{b}, \ \text{ if } b \neq 0$$

可由收斂數列的定義簡單得出。

### 收斂數列的子數列必為收斂數列

> $$\lim_{n \rightarrow \infty} a_n = a$$converge $$\Rightarrow$$$$\lim_{i \rightarrow \infty} a_{n_i}=a$$converge
>
> 反向不成立，因為子數列可能是從發散數列中得出。

proof:

$$\lim_{n \rightarrow \infty} a_n = a$$ converge $$ \Leftrightarrow $$$$\forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n - a| < \epsilon, \ \forall n \geq n_0$$

take $$i \geq n_0$$then $$n_i \geq i \geq n_0 \Rightarrow |a_{n_i} - a|<\epsilon$$ \(QED\)

### 數列奇數項與偶數項收斂至同一值，則數列數斂

> $$\lim_{n \rightarrow \infty} a_{2n} = a$$and $$\lim_{n \rightarrow \infty} a_{2n+1} = a$$ $$\Rightarrow $$$$\lim_{n \rightarrow \infty} a_n = a$$

proof:

$$ \forall \epsilon > 0 \  \exists n_0 \in \mathbb{N} \ni |a_{2n} - a| < \epsilon,  \forall 2n \geq n_0$$and $$ \exists n_1 \in \mathbb{N} \ni |a_{2n+1} - a| < \epsilon,  \forall 2n+1 \geq n_1$$

take $$n_3=2n_0+2n_1+1$$ then $$|a_n - a| < \epsilon\  \forall n \geq n_3$$\(QED\)

## 有界數列 \(bounded sequence\)

> definition: 有界數列
>
> if $$\exists M \in \mathbb{R} \ni a_n \leq M , \forall n$$then $$\{ a_n \}$$be a bounded sequence.



### 



