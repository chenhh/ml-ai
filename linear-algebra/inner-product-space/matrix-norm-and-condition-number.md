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
> * $$\|A\|_1= \max_{1 \leq i \leq N} \sum_{i=1}^M |a_{ij}|$$（將每一行取絕對值相加後，取數值最大的那一行）
> * $$\|A\|_\infty=\max_{1 \leq i \leq M} \sum_{j=1}^M |a_{ij}|$$（將每一列取絕對值相加後，取數值最大的那一列）
> * $$\|A\|_2 = \sqrt{\lambda_{\max}(A^\mathrm{H}A)} = \sigma_{\max} \geq0$$（矩陣$$A$$長度等於$$A^{\mathrm{H}}A$$最大特徵值的平方值且等於$$A$$的最大奇異值）

### 對稱矩陣長度為矩陣的最大特徵根

> 矩陣$$A \in \mathbb{R}^{ N \times N}$$為對稱矩陣\($$A^\top =A$$\)，$$\lambda_1, \lambda_2, \dots, \lambda_N$$為$$A$$的特徵根，則$$\|A\|_2=\max\{|\lambda_1|, \lambda_2|, \dots, |\lambda_N|\}$$。

Proof:

* $$\|A\|_2= \sqrt{λ_{\max} (A^\mathrm{H} A)}$$且$$A^\top=A$$
* 所以$$\|A\|_2=\sqrt{\lambda_{\max} (A^2 )}=\max⁡\{|\lambda_1 |,|\lambda_2 |,\dots,|\lambda_N |\}$$  \(QED\)

## 矩陣條件數\(condition number of matrix\)

> 矩陣$$A \in F^{N \times N}$$ 為可逆矩陣，定義$$A$$的條件數$$cond_p(A)=\|A\|_p\|A^{-1}\|_p$$。

### 矩陣條件數為最大特徵根與最小特徵根比值的平方根

> 矩陣$$A \in F^{N \times N}$$ 為可逆矩陣，$$\lambda_1 \leq \lambda_2 \leq \dots \leq  \lambda_N$$為矩陣$$A$$的特徵根，則：$$cond_2(A)=\sqrt{\frac{\lambda_N}{\lambda_1}}$$。
>
> 矩陣$$A \in F^{N \times N}$$ 為可逆矩陣且為對稱矩陣，$$\lambda_1| \leq |\lambda_2| \leq \dots \leq |\lambda_N|$$矩陣$$A$$的特徵根，則$$cond_2(A)=\frac{|\lambda_N|}{|\lambda_1|}$$。

### 病態（良好）條件\(ill \(well\) condition\)

> $$A \in F^{N \times N}$$，•
>
> * 若$$A$$中元素相對小的改變會造成在解$$Ax=b$$時造成相對大的改變時，稱$$A$$為病態條件（ill-condition）。
> * 若$$A$$中元素相對小的改變會造成在解$$Ax=b$$時造成相對小的改變時，稱$$A$$為良好條件（well-condition）。

考慮線性系統$$Ax=b$$，令$$x^∗$$ 為$$Ax=b$$的真正解答，而$$\hat{x}=x^∗+\Delta x$$為$$Ax=b$$的計算值。若要估計相對誤差$$\frac{\| \Delta x\|}{\|x\|}$$， 

* 令$$\hat{b} = A \hat{x}=b+\Delta b$$
* 所以$$b + \Delta b=A \hat{x} = A(x^*+\Delta x)=Ax+A\Delta x = b + A\Delta x$$
* 可得 $$A \Delta x = \Delta b$$

### 用輸出值的誤差估計解答的誤差關係式

> 矩陣$$A \in F^{N \times N}$$ 為可逆矩陣，則：
>
> * $$\frac{1}{cond(A)} \frac{\| \Delta b \|}{\|b\|} \leq \frac{\|\Delta x\|}{\|x\|} \leq cond(A) \frac{\| \Delta b \|}{\|b\|}$$
> * 所以$$\frac{1}{cond(A)} \frac{\| \Delta b \|}{\|b\|}  \leq cond(A) \frac{\| \Delta b \|}{\|b\|}$$
> * 整理得$$cond(A)^2 \geq 1$$，即$$cond(A) \geq 1$$。

* 因此當$$cond(A) \rightarrow 1$$時，$$\frac{\| \Delta b\|}{\|b\|}$$ 與$$\frac{\| \Delta x\|}{\|x\|}$$會很近似，因此$$\Delta x$$小變動不會造成輸出值有太大的變化，此時A為well-condition。
* 反之當$$cond(A)$$很大時，稍為調整輸入出就會造成輸出值相當大的變化，此時A為ill-condition。

