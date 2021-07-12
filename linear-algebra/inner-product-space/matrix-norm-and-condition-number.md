# 矩陣的長度與條件數\(matrix norm and condition number\)

## 矩陣的長度

> 矩陣$$A \in F^{M \times N}$$，定義$$A$$的範數$$\|A\|=\max_{x \neq 0}\left\{  \frac{\|Ax\|}{\|x\|} \right\} = \max_{\|x\|=1} \|Ax\| 。$$
>
> 註：矩陣$$A$$的長度\(2-norm\)等於其[奇異值分解\(SVD\)的最大奇異值](singular-value-decomposition.md#ju-zhen-de-chang-du-wei-zui-da-de-qi-yi-zhi)$$\sigma_{max}$$。

由於向量的長度可為$$p$$-norm，$$p=1,2,\dots,\infty$$, 所以矩陣的長度也有相同的定義：

* $$\|A\|_p=\max_{x \neq 0}\left\{  \frac{\|Ax\|_p}{\|x\|_p} \right\}$$
* $$\|x\|=1$$得$$\|Ax\| = \frac{\|Ax\|}{\|x\|}$$，所以$$\max_{\|x\|=1}\|Ax\| \leq \max_{x \neq 0}\frac{\|Ax\|}{\|x\|}$$--\(a\)
* $$\forall x \in F^{N \times 1}$$, $$x \neq 0$$且$$\left\|\frac{x}{\|x\|}\right\|=\mathbf{1}$$，所以$$\frac{\|Ax\|}{\|x\|} = \frac{A \left\|\frac{x}{\|x\|}\right\|}{\left\|\frac{x}{\|x\|}\right\|} = \left\| A\frac{x}{\|x\|}\right\|$$，可得$$ \max_{x \neq 0}\frac{\|Ax\|}{\|x\|} \leq \max_{\|x\|=1}\|Ax\|$$--\(b\)
* 由\(a,b\)得$$\|A\|=\max_{x \neq 0}\left\{  \frac{\|Ax\|}{\|x\|} \right\} = \max_{\|x\|=1} \|Ax\| 。$$

