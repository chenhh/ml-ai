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





>



