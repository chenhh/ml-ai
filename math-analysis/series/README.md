# 級數\(series\)

## 簡介

實數中的級數為\(有限或無限\)數列的總和，可分為**收斂**與**發散級數**二類。

審斂法\(tests for convergence\)有：篩審斂法\(screen test\)，Cauchy審斂法，絕對值審斂法，正項級數審斂法，積分審斂法，比較審斂法，極限比較審斂法，交錯級數審斂法，Dirichlet審斂法，比值審斂法，根式審斂法。

## 級數與部份和

> 令 $$\{ x_n \} \subset \mathbb{R}$$為數列\(sequence\)，定義級數\(series\)為 $$\sum_{i=1}^{\infty} x_i = x_1 + x_2 + \ldots$$。定義部份和\(partial sum \) $$\displaystyle s_n  = \sum_{i=1}^n x_i = x_1 +x _2 + \ldots + x_n $$。

可定義部份和數列$$\{s_n \} \equiv \{ s_1, s_2, \ldots, s_n \ldots \}$$。則級數可用部份和分析是否收斂，即 $$\displaystyle \lim_{n \rightarrow \infty} s_n =  \lim_{n \rightarrow \infty} \sum_{i=1}^n x_i$$。

* 如果 $$\{ s_n \} $$收斂 \(convergence\)，則 $$\displaystyle \exists s \in \mathbb{R} \ni \lim_{n \rightarrow \infty} s_n = s$$
* 如果$$\{ s_n\}$$不收斂，則為發散\(divergence\)。
* 級數的極限值等於部份和的極限值.

  級數收斂等價於部份和序列收斂

### 收斂\(發散\)級數即使去除掉有限項仍為收斂\(發散\)級數

> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 收斂 $$ \Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$收斂
> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 發散 $$ \Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$發散
>
> 級數是否收斂\(發散\)不是依據前面有限項的部份和，而是無窮多項的元素和有關。

proof:=&gt;

* 令部份和  $$\displaystyle s_n = \sum_{i=1}^n x_i$$
* 因為$$\displaystyle \sum_{i=1}^{\infty} x_i$$收斂，令$$\displaystyle \lim_{ n \rightarrow \infty} s_n  = \lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i=s$$收斂。
* 因為$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i = \lim_{ n \rightarrow \infty}  \left(\sum_{i=1}^{k-1} x_i + \sum_{i=k}^n x_i \right) = \sum_{i=1}^{k-1} x_i +  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s$$
* 因此$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i =  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s -  \sum_{i=1}^{k-1} x_i$$收斂
* \(QED\)

proof: &lt;= 使用相同的方法可得證。\(QED\)

## 級數為線性算子

> 若 $$\displaystyle \sum_{k=1}^\infty x_k =a$$ 且 $$\displaystyle \sum_{k=1}^\infty y_k =b,  \forall s,t \in \mathbb{R}$$, 則：$$\displaystyle \sum_{k=1}^\infty (s\cdot x_k + t \cdot y_k) =s\cdot a + t \cdot b$$

proof:

* 因為$$\displaystyle \sum_{k=1}^n (sx_k + ty_k) =  s\cdot\sum_{k=1}^n x_k + t\cdot  \sum_{k=1}^n y_k$$
* 所以$$\begin{align} \displaystyle \lim_{ n \rightarrow \infty}  \sum_{k=1}^n (sx_k + ty_k) &= s\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n x_k + t\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n y_k \\&=  s a + tb \end{align}$$\(QED\)

