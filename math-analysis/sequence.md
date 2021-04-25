# 數列\(sequence\)

## 收斂與發散數列

> \[收斂數列\]$$ {a_n} \subseteq \mathbb{R}$$ and $$\lim_{n \rightarrow \infty} a_n = a \Leftrightarrow   \forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n -a| < \epsilon\ \forall n \geq n_0$$
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

proof:

$$\lim_{n \rightarrow \infty} a_n = a$$ converge $$ \Leftrightarrow $$$$\forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n - a| < \epsilon, \ \forall n \geq n_0$$

take $$i \geq n_0$$then $$n_i \geq i \geq n_0 \Rightarrow |a_{n_i} - a|<\epsilon$$ \(QED\)

### 



