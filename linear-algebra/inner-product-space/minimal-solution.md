# 極小解(minimal solution)

## 極小解(minimal solution)

> 矩陣$$A \in F^{M \times N}$$，向量$$b \in F^{M \times 1}$$ 且$$Ax=b$$有解。
>
> 令$$s$$為$$Ax=b$$的其中一個解，且$$Ax=b$$的其它解為$$u$$，若滿足$$\|s\| \leq \|u\|$$時，稱$$s$$為$$Ax=b$$的極小解。
>
> 極小解即為所有解集合中，範數（長度）最小者，因此若$$Ax=b$$有解時，極小解必定存在。

### 極小解唯一存在性

> 1. 唯一存在$$s \in R(A^\mathrm{H} ) \ni s$$為$$Ax=b$$的極小解。
> 2. 若$$u$$滿足$$(AA^\mathrm{H} )u=b$$，則$$s=A^\mathrm{H} u$$。

Proof (1):

* 令$$W=R(A^\mathrm{H} )$$，則$$W^\bot=ker⁡(A)$$
* 令$$x_0$$為$$Ax=b$$的一個解
* 因為$$F^{N \times 1}=W \oplus W^\bot$$
* 所以$$\exists s \in W, y \in W^\bot \ni x_0=s+y$$
* $$b=Ax_0=A(s+y)=As+Ay=As+0=As$$
* 所以$$s$$為$$Ax=b$$之解
* &#x20;令$$v$$為$$Ax=b$$的解
* 則$$v=s+u$$, for some $$u \in ker⁡(A)=W^\bot$$
* 所以$$\|v\|^2=\|s+u\|^2=\|s\|^2+\|u\|^2 \geq \|s\|^2$$
* 當$$\|v\|=\|s\|$$時，$$u=0=v=s$$
* 所以$$s$$為唯一極小解(由$$x$$投影在$$A$$的行向量所產生)。(QED)

Proof (2):

* 令$$u$$滿足$$(AA^\mathrm{H} )u=b$$
* 所以$$v=A^\mathrm{H} ~ u \in W$$為$$Ax=b$$的某一解，得$$v−s \in W$$
* 因為$$A(v−s)=Av−As=b−b=0$$
* 所以$$v−s \in ker⁡(A)=W^\bot$$
* 因此$$v−s \in W \cap W^\bot=\{0\}$$
* 所以$$v−s=0$$，得$$s=v=A^\mathrm{H} u$$。(QED)

#### 範例

* $$A=\begin{bmatrix}  1 & 2 & 1\\ 1 & -1 & 2 \\ 1 & 5 & 0 \end{bmatrix}$$，$$b=\begin{bmatrix} 4 \\ -11 \\ 19  \end{bmatrix}$$
* 解$$A A^\top x=b$$得 $$x=\begin{bmatrix}  1-2x_3 \\ -2 + x_3 \\ x_3 \end{bmatrix}$$
* 取$$u=\begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix}$$為上式其中一解，則$$A^\top u=\begin{bmatrix} -1 \\ 4 \\ -3\end{bmatrix}$$為極小解。
