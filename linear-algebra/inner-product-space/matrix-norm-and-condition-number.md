# 矩陣的長度與條件數\(matrix norm and condition number\)

## 矩陣的長度

> 矩陣$$A \in F^{M \times N}$$，定義$$A$$的範數$$\|A\|=\max_{x \neq 0}\left\{  \frac{\|Ax\|}{\|x\|} \right\} = \max_{\|x\|=1} \|Ax\| 。$$
>
> 註：
>
> * 任意矩陣$$A\in F^{M \times N}$$的長度\(2-norm\)等於其[奇異值分解\(SVD\)的最大奇異值](singular-value-decomposition.md#ju-zhen-de-chang-du-wei-zui-da-de-qi-yi-zhi)$$\sigma_{\max}$$。
> * 對稱矩陣$$A \in F^{N \times N}$$的長度\(2-norm\)等於$$A^\mathrm{H}A$$最大特徵根的平方根，即$$\sqrt{\lambda_{\max}(A^{\mathrm{H}}A)}$$。

由於向量的長度可為$$p$$-norm，$$p=1,2,\dots,\infty$$, 所以矩陣的長度也有相同的定義：

* $$\|A\|_p=\max_{x \neq 0}\left\{  \frac{\|Ax\|_p}{\|x\|_p} \right\}$$
* $$\|x\|=1$$得$$\|Ax\| = \frac{\|Ax\|}{\|x\|}$$，所以$$\max_{\|x\|=1}\|Ax\| \leq \max_{x \neq 0}\frac{\|Ax\|}{\|x\|}$$--\(a\)
* $$\forall x \in F^{N \times 1}$$, $$x \neq 0$$且$$\left\|\frac{x}{\|x\|}\right\|=\mathbf{1}$$，所以$$\frac{\|Ax\|}{\|x\|} = \frac{A \left\|\frac{x}{\|x\|}\right\|}{\left\|\frac{x}{\|x\|}\right\|} = \left\| A\frac{x}{\|x\|}\right\|$$，可得$$ \max_{x \neq 0}\frac{\|Ax\|}{\|x\|} \leq \max_{\|x\|=1}\|Ax\|$$--\(b\)
* 由\(a,b\)得$$\|A\|=\max_{x \neq 0}\left\{  \frac{\|Ax\|}{\|x\|} \right\} = \max_{\|x\|=1} \|Ax\| 。$$

### 矩陣乘法的長度小於長度的乘法

> 矩陣$$A \in F^{M \times N}, B \in F^{N \times P}$$，則：
>
> * $$\|Ay\| \leq \|A\| \|y\|, ~\forall y \in F^{N \times 1}$$
> * $$\|AB\| \leq \|A\| \|B\|$$

### 矩陣的範數空間\(norm space\)

> $$V=F^{M \times N}$$為向量空間，則矩陣的長度$$\|\cdot \|$$為$$V$$上的範數，即：
>
> * $$\forall A \in F^{M \times N}$$，$$\|A\| \geq 0$$且$$\|A\|=0 \Leftrightarrow A=0$$。
> * $$\forall c \in F, A \in F^{M \times N}$$，$$\|cA\|=|c|\|A\|$$。
> * $$\forall A, B \in F^{M \times N}$$，$$\|A+B\| \leq \|A\| + \|B\|$$。

### 矩陣長度求值

> 矩陣$$A \in F^{M \times N}$$，則：
>
> * $$\|a\|_1= \max_{1 \leq i \leq N} \sum_{i=1}^M |a_{ij}|$$（將每一行取絕對值相加後，取數值最大的那一行）
> * $$\|A\|_\infty=\max_{1 \leq i \leq M} \sum_{j=1}^M |a_{ij}|$$（將每一列取絕對值相加後，取數值最大的那一列）
> * $$\|A\|_2 = \sqrt{\lambda_{\max}(A^\mathrm{H}A)} = \sigma_{\max} \geq0$$（矩陣$$A$$長度等於$$A^{\mathrm{H}}A$$最大特徵值的平方值且等於$$A$$的最大奇異值）

