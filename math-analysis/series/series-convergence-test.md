# 級數審斂法

## 篩審斂法\(screen test\)

> 若級數 $$\displaystyle \sum_{k=1}^\infty x_k$$ 收斂，則$$\displaystyle \lim_{n \rightarrow \infty} x_n=0 $$，反之不一定成立（極限為零不保證級數收斂）
>
> 反之，若$$\displaystyle \lim_{n \rightarrow \infty} x_n \neq 0$$，則級數$$ \displaystyle \sum_{k=1}^\infty x_k$$ 發散。

* 註：已知級數的收斂與發散與無窮項的尾部元素有關，因此若無窮項的元素不收斂至0的話，級數和無法收斂。
* 註： 存在發散級數$$\displaystyle \sum_{k=1}^\infty x_k$$ 且$$\displaystyle \lim_{n \rightarrow \infty} x_n =0 $$。

Proof:

* 若級數$$\displaystyle \sum_{k=1}^\infty x_k$$ 收斂，令$$S_n=x_1+x_2+⋯+x_n= \sum_{k=1}^n x_k  $$
* 則存在$$\displaystyle S \in \mathbb{R}  \ni \lim_{n \rightarrow \infty}⁡S_n =S $$
* $$\begin{align} \displaystyle  \therefore \lim_{n \rightarrow \infty}⁡x_n &= \lim_{n \rightarrow \infty}⁡(S_n−S_{n−1} )\\ &=\lim_{n \rightarrow \infty} S_n −\lim_{n \rightarrow \infty}⁡S_{n−1} \\&=S−S \\ &=0 \end{align}$$ \(QED\)

### 範例：極限值為0的發散級數

$$\displaystyle \sum_{k=1}^\infty \frac{1}{\sqrt{k}}$$發散，但是$$\displaystyle \lim_{n \rightarrow \infty} \frac{1}{\sqrt{n}}=0$$

* $$S_n=\sum_{k=}^n \frac{1}{\sqrt{k}}=1+\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{3}} + \cdots+ \frac{1}{\sqrt{n}} > \frac{1}{\sqrt{n}}+\frac{1}{\sqrt{n}}+\frac{1}{\sqrt{n}}+\cdots +\frac{1}{\sqrt{n}}=\frac{n}{\sqrt{n}}=\sqrt{n} $$
* 因此 $$\displaystyle \lim_{n \rightarrow \infty}S_n \geq \lim_{n \rightarrow \infty}\sqrt{n} = \infty$$發散。

## 正實數的遞減數列篩審斂法

> $$\{x_n \}$$為遞減數列且$$\forall n \in \mathbb{N}, ~x_n>0$$。
>
> 若$$\displaystyle \sum_{k=1}^\infty x_n$$ 為收斂級數，則$$\displaystyle \lim_{n \rightarrow \infty}⁡n x_n=0$$。

Proof:

* 令$$\displaystyle  \sum_{k=1}^\infty x_n =x<\infty$$ 且部份和 $$\displaystyle S_n=\sum_{k=1}^n x_n $$。
* 可得 $$\displaystyle \lim_{n \rightarrow \infty}⁡S_n =x= \lim_{n \rightarrow \infty}⁡ S_{2n }$$
* 因為$$S_{2n}−S_n=x_{n+1}+x_{n+2}+\ldots+x_{2n} \geq x_{2n}+x_{2n}+ \ldots +x_{2n}$$ （因為$$\{x_n \}$$是遞減數列，所以不等式成立）。
* 所以$$\displaystyle \lim_{n \rightarrow \infty}⁡(S_{2n}−S_n )=0=\lim_{n \rightarrow \infty}⁡(x_{n+1}+x_{n+2}+\ldots+x_{2n} ) \geq \lim_{n \rightarrow \infty}⁡n x_{2n} \geq0$$。
* 因此$$\displaystyle \lim_{n \rightarrow \infty}⁡n x_{2n}=0 \Rightarrow \lim_{n \rightarrow \infty}⁡2n x_{2n}=0$$
* 而且$$\{x_n\}$$是遞減數列, 所以$$\displaystyle x_{2n} \geq x_{2n+1} \Rightarrow (2nx_{2n} )\frac{2n+1}{2n} \geq (2n+1) x_{2n+1}\Rightarrow \lim_{n \rightarrow \infty}⁡(2n+1) x_{2n+1}=0$$
* 由奇位數子序列與偶位數子序列收斂則序列收斂的性質，因為$$\displaystyle \lim_{n \rightarrow \infty}⁡(2n+1) x_{2n+1}=0$$ 且$$\displaystyle \lim_{n \rightarrow \infty}2n x_{2n}=0$$ 所以可得 $$\displaystyle \lim_{n \rightarrow \infty}n x_n=0$$ \(QED\)

#### 範例

$$\displaystyle \sum_{k=2}^\infty \sin⁡\frac{\pi}{k}$$   發散。

* 因為$$\forall n=2,3,\ldots , ~ \sin⁡\frac{\pi}{n}>0$$ 且 $$\sin⁡ \frac{\pi}{n} > \sin⁡ \frac{π}{(n+1)}$$, 因此$$\{\sin⁡\frac{\pi}{n} \}$$為遞減數列。
* 由 $$\displaystyle \lim_{n \rightarrow \infty}⁡ n \sin⁡\frac{\pi}{n}=\pi \neq 0$$ 得 $$\displaystyle \sum_{k=2}^\infty \sin \frac{\pi}{k}$$   發散。

## Cauchy 審斂法

> • 級數$$\displaystyle \sum_{k=1}^\infty x_k$$ 收斂的充要條件為 $$\forall \epsilon>0 ~ \exists n_0 \in \mathbb{N} \ni \forall n>m \geq n_0, ~ |x_{m+1}+x_{m+2}+ \ldots +x_n |<\epsilon$$

註：級數收斂的必要條件是序列要收斂至0，而實數中的收斂數列必為Cauchy序列。

Proof:

* 因為級數$$\displaystyle\sum_{k=1}^\infty x_k$$   收斂的充要條件是其部份和數列$$\{S_n \}$$收斂。
* 而數列$$\{S_n \}$$收斂的充要條件是$$\{S_n\}$$  是Cauchy數列。
* 因此級數$$\displaystyle\sum_{k=1}^\infty x_k$$ 收斂的充要條件是$$\{S_n\}$$是Cauchy數列。
* 因為 $$S_n=\displaystyle\sum_{k=1}^n x_k $$
* 所以$$\{S_n \}$$是Cauchy數列\Leftrightarrow $$\forall \epsilon>0 ~ \exists n_0 \in \mathbb{N} \ni \forall n>m \geq n_0, ~|S_n - S_m| =  |x_{m+1}+x_{m+2}+ \ldots +x_n |<\epsilon$$ \(QED\).





