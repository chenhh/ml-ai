# 數列\(sequence\)

## 有限數列與無限數列

> 給定有限集合$$\{1,2,\ldots, n\}$$，與定義在此集合的函數$$f$$，則$$\{f(1), f(2),\ldots, f(n)\}$$為有限數列（finite sequence）。

> 給定自然數集合$$\{1,2,\ldots \}$$與定義在此集合的函數$$f$$，則$$\{f(1), f(2), \ldots\}$$為無限數列（infinite sequence）。

## 子數列\(subsequence\)

> 令$$s=\{s_n\}$$為無限數列，令函數$$k: \mathbb{N} \rightarrow T, ~ T \subseteq \mathbb{N}$$且為嚴格遞增函數（若$$m <n$$，則$$k(m) < k(n)$$）。
>
> 則對所有大於1的整數$$n$$，合成函數$$(s \circ k)(n) = s_{k(n)} \equiv s_{kn}$$形成的序列$$\{s_{k(n)}\} \equiv \{s_{kn}\}$$稱為$$s$$的子數列。

* 子數列就是原本的數列，依原始數列的順序，任意取出的子集合形成的數列。

## 收斂與發散數列

> 實數版本
>
> * $$ \{a_n\}_{n \in \mathbb{N}} \subseteq \mathbb{R}$$ 稱為收斂數列若$$\displaystyle \lim_{n \rightarrow \infty} a_n = a \Leftrightarrow   \forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n -a| < \epsilon\ \forall n \geq n_0$$
> * 常寫為 $$a_n \rightarrow a$$ as $$n \rightarrow \infty$$
> * 如果$${a_n}$$不是收斂數列\(convergent sequence\)，則為發散數列\(divergent sequence\)。
>
> 度量空間
>
> * $$(X,d)$$為度量空間, $$\{a_n\}_{n \in \mathbb{N}} \subset X$$為一數列
> * $$\displaystyle \lim_{n \rightarrow \infty} a_n = a \Leftrightarrow   \forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni  d(a_n,a) < \epsilon\ \forall n \geq n_0$$

* 數列收斂的直觀意義，是不論我們要使$$a_n$$ 與$$a$$接近到任何程度，只要$$n$$值夠大時一定能夠辦到。給定接近的距離$$\epsilon$$後，只要過了第$$a_0,a_1,\ldots,a_{n_{0}−1 }$$ \(有限項\)之後，$$a_{n_0},a_{n_0+1},\ldots$$\(無窮項\)與$$a$$的距離均小於$$\epsilon$$。
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

### 收斂數列的子數列必為收斂數列且收斂至同一點

> $$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$收斂 $$\Rightarrow$$$$\displaystyle \lim_{i \rightarrow \infty} a_{n_i}=a$$收斂
>
> 反向不成立，因為子數列可能是從發散數列中得出。

proof:

$$\lim_{n \rightarrow \infty} a_n = a$$ converge $$ \Leftrightarrow $$$$\forall \epsilon > 0 \ \exists n_0 \in \mathbb{N} \ni |a_n - a| < \epsilon, \ \forall n \geq n_0$$

take $$i \geq n_0$$then $$n_i \geq i \geq n_0 \Rightarrow |a_{n_i} - a|<\epsilon$$ \(QED\)

### 收斂序列的值域有界且收斂至極限點

> 度量空間$$(X,d)$$中，$$\{ a_n\} \subseteq X$$為收斂數列，令 $$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$，且令$$T=\{a_1, a_2, \ldots\}$$為序列之值的集合，則
>
> * $$T$$為有界集合（$$\exists a_k \in T, M  >0  \ni T \subseteq N_M(a_k)$$ ）
> * $$a$$為$$T$$的附著點（$$\forall r>0, N_r(a)\cap T \neq \emptyset$$）
> * 當$$T$$為無窮集合時，$$a$$為極限點（$$\forall >0, N_r(a) - {a} \cap T \neq \emptyset$$）。

Proof:

* $$\displaystyle \lim_{n \rightarrow \infty}⁡a_n=a \Leftrightarrow \forall \epsilon>0 ~ \exists n_0 \in \mathbb{N} \ni d(a_n,a)<\epsilon, ~\forall n \geq n_0$$
* 當$$\epsilon=1$$時，取$$n_1$$ 為符合收斂條件的$$n_0$$。
* 則$$\forall n \geq n_1, \{a_n\} \subseteq N_r (a), r =1+\max \{ d(a,a_1 ), d(a,a_2 ),\ldots ,d(a,a_n )\}$$
* 而$$\forall \epsilon>0$$，均可得出此結果，因此值域集合$$T$$有界 \(QED\).
* 由收斂定義得 $$\forall \epsilon>0,  ~N_\epsilon (a) \cap T \neq \emptyset$$, 因此$$a$$為附著點. \(QED\)

### 數列奇數項與偶數項收斂至同一值，則數列數斂

> $$\displaystyle  \lim_{n \rightarrow \infty} a_{2n} = a$$且 $$\displaystyle  \lim_{n \rightarrow \infty} a_{2n+1} = a$$ $$\Rightarrow $$$$\displaystyle  \lim_{n \rightarrow \infty} a_n = a$$

proof:

$$ \forall \epsilon > 0 \  \exists n_0 \in \mathbb{N} \ni |a_{2n} - a| < \epsilon,  \forall 2n \geq n_0$$and $$ \exists n_1 \in \mathbb{N} \ni |a_{2n+1} - a| < \epsilon,  \forall 2n+1 \geq n_1$$

take $$n_3=2n_0+2n_1+1$$ then $$|a_n - a| < \epsilon\  \forall n \geq n_3$$\(QED\)

## 有界數列 \(bounded sequence\)

> $$\{ a_n \} \subseteq \mathbb{R}$$稱為有界數列若 $$\exists M \in \mathbb{R} \ni a_n \leq M , \forall n$$。



### 



