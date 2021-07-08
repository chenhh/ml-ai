# 最小平方解\(least square solution\)

## 簡介

* 矩陣$$A \in F^{M \times N} , A=\begin{bmatrix} A_{:1} & \dots & A_{:N}\end{bmatrix},~ A^{\mathrm{H}}=  \begin{bmatrix} \overline{A_{:1}^\top} \\ \vdots \\ \overline{A_{:N}^\top}\end{bmatrix} = \begin{bmatrix} A_{:1}^{\mathrm{H}} \\ \vdots \\ A_{:N}^{\mathrm{H}}\end{bmatrix}$$
* $$A^{\mathrm{H}}A =  \begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} &  \dots &A_{:1}^{\mathrm{H}}A_{:N} \\  \vdots & \ddots & v\dots \\ A_{:N}^{\mathrm{H}}A_{:1} & \dots & A_{:N}^{\mathrm{H}}A_{:N}  \end{bmatrix} \in F^{N \times N}$$稱為正規矩陣（normal matrix）。
* 例如：$$A=\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{bmatrix}$$，$$A^{\mathrm{H}}=\begin{bmatrix} \overline{a_{11}} & \overline{a_{21}} & \overline{a_{31}} \\ \overline{a_{12}} & \overline{a_{22}} & \overline{a_{32}} \end{bmatrix}$$，$$A^{\mathrm{H}}A=\begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} & A_{:1}^{\mathrm{H}}A_{:2} \\ A_{:2}^{\mathrm{H}}A_{:1} & A_{:2}^{\mathrm{H}}A_{:2}  \end{bmatrix}$$
* 給定矩陣$$A \in F^{M \times N}$$行向量獨立，但不必正交，則向量$$b \in F^{M \times 1}$$投影到$$CS(A) =\{Ax| x\in F^{N \times 1}\}$$的投影向量為$$\mathrm{proj}_{CS(A)} (b)=A(A^{\mathrm{H}} A)^{−1} A^\mathrm{H} b$$。
* 如果將$$A$$的獨立行向量先做Gram-Schmidt正交化得正交基底後，再將$$b$$投影到各基底得到合成向量可得到與$$\mathrm{proj}_{CS(A)} (b)$$相同之值。
* 而$$x^{*} \in \mathbb{C}^{N \times 1}$$為$$x^{*}=\arg\min_x{\|Ax-b\|}$$的最佳解$$\Leftrightarrow A^{\mathrm{H}}Ax=A^{\mathrm{H}}b$$之解。

## 正規矩陣的基本子空間與性質

> 令矩陣$$A \in F^{M \times N}$$，則：
>
> 1. $$ker(A^{\mathrm{H}}A) =ker(A)=\{x \in F^{N \times 1} | Ax=0\}$$
> 2. $$rank(A^{\mathrm{H}}A) = rank(A)$$\(只有rank相同，但值域不相同\)
> 3. $$Lker(A^{\mathrm{H}}A) = Lker(A)$$
> 4. 矩陣$$A$$行向量線性獨立$$\Leftrightarrow A^{\mathrm{H}} A$$為可逆矩陣。
> 5. 矩陣$$A$$列向量線性獨立$$\Leftrightarrow A^{\mathrm{H}} A$$為可逆矩陣。
>
> 註：
>
> * 矩陣$$A \in F^{M \times N}$$ 的行向量獨立$$\Leftrightarrow rank(A)=\dim⁡(CS(A))=\dim⁡(RS(A))=N=\dim⁡(F^{1 \times N}) )\Leftrightarrow A$$的列向量生成$$F^{1 \times N}$$。
> * 矩陣$$A \in F^{M \times N}$$ 的列向量獨立$$\Leftrightarrow rank(A)=\dim⁡(RS(A))=\dim⁡(CS(A))=M=\dim⁡(F^{M\times 1} )\Leftrightarrow A$$的行生成$$F^{M \times 1}$$。

Proof \(1\)=&gt;

* $$\forall x \in ker⁡(A^\mathrm{H} A)$$，可得$$(A^\mathrm{H} A)x=0$$，因此$$x^\mathrm{H} A^\mathrm{H} Ax=0=x^\mathrm{H} 0=0$$
* 由標準內積得$$(Ax)^{\mathrm{H}} (Ax)=0\Rightarrow\langle Ax,Ax \rangle = \|Ax\|^2=0 $$
* 因為$$ \|Ax\|^2=0 \Rightarrow Ax=0 \Rightarrow x \in ker⁡(A)$$\(QED\)

 &lt;=

* $$\forall x \in ker⁡(A)$$，可得$$Ax=0 A^{\mathrm{H}} Ax=A^{\mathrm{H}} 0=0 \Rightarrow x \in ker⁡(A^{\mathrm{H}} A)$$
* 因為$$ker⁡(A^{\mathrm{H}} A) \subseteq ker⁡(A)$$且$$ker⁡(A) \subseteq ker⁡(A^{\mathrm{H}} A)$$  ，所以$$ker(A^{\mathrm{H}} A)=ker⁡(A)$$  \(QED\)

Proof \(2\)

* $$A \in ℂ^{M \times N}$$，by rank-nullity theorem
* $$N=nullity(A)+rank(A)=\dim⁡(ker⁡(A) )+\dim⁡(CS(A))$$
* 因為$$A^{\mathrm{H}} A \in \mathbb{C}^{N \times N}$$，所以$$N=nullity(A^\mathrm{H} A)+rank(A^\mathrm{H} A)$$
* 因為$$ker⁡(A^\mathrm{H} A)=ker⁡(A) \Rightarrow nullity(A^\mathrm{H} A)=nullity(A)$$
* 可得 $$rank(A^\mathrm{H} A)=rank(A)$$ \(QED\)

proof\(4\):

* 因為矩陣$$A$$的行向量獨立$$\Leftrightarrow Ax=0$$只有$$x=0$$的解$$\Leftrightarrow ker⁡(A)=\{0\}$$
* 因此$$ker⁡(A^\mathrm{H} A)=\{0\}$$，可得$$A^\mathrm{H} A$$為可逆矩陣 \(QED\)

## 歐式空間標準內積正交投影至矩陣的行向量公式

> * 矩陣$$A \in \mathbb{C}^{M \times N}$$，且$$A$$行向量線性獨立（但不一定正交），考慮由$$A$$的行向量生成的向量空間$$W=CS(A) $$。
> * 給定向量$$b \in \mathbb{C}^{M \times 1}$$，則在歐式空間標準內積下，向量$$b$$投影至向量空間$$W$$之值為  $$\mathrm{proj}_W (b)=A(A^{\mathrm{H}} A)^{−1} A^\mathrm{H} b$$。
> * 因為矩陣$$A$$為的行向量線性獨立，所以$$A^\mathrm{H} A$$可逆，因此 $$(A^\mathrm{H} A)^{−1}$$ 必定存在，即$$A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b$$必定可求值  。

Proof:

* $$A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b=A[(A^\mathrm{H} A)^{−1} A^\mathrm{H} b]   \in CS(A)=W$$，所以向量$$b$$投影後的向量在空間$$W$$。
* 因為向量空間$$W$$由$$CS(A)$$生成，因此$$\forall w \in W, \exists x\in \mathbb{C}^{N \times1} \ni w=Ax$$，即空間$$W$$的元素可由$$A$$的行向量線性組合而成。
* 由於正交向量$$b−A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b$$應與$$W$$內的任意向量$$w$$內積值為0  。
* 因此$$\begin{aligned} &\langle b−A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b,~w\rangle  \\&=w^{\mathrm{H}} (b-A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b) \\ &=(Ax)^{\mathrm{H}} (b-A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b) \\ &=x^\mathrm{H} A^\mathrm{H} b−x^\mathrm{H} A^\mathrm{H} A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b \\ &=x^\mathrm{H} A^\mathrm{H} b−x^\mathrm{H} A^\mathrm{H} b\\ &=0  \end{aligned}$$
* 所以$$w$$與$$ b−A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b$$正交
* 因此$$\mathrm{proj}_W (b)= b−A(A^\mathrm{H} A)^{−1} A^\mathrm{H} b$$ \(QED\)

#### 範例：矩陣

* $$A=\begin{bmatrix} 1 & 1 \\2 & -1 \\-2 & 0 \\ 1 & 1\end{bmatrix}$$，$$b=\begin{bmatrix}1 \\ 2 \\3 \\4 \end{bmatrix}$$，因為矩陣$$A$$的行向量獨立，因此$$\mathrm{proj}_{CS(A)}(b)=A(A^\top A)^{-1} A^\top b=\begin{bmatrix}\frac{13}{10} \\ -\frac{2}{5} \\ - \frac{3}{5} \\ \frac{13}{10} \end{bmatrix}$$

使用Gram-Schmidt正交化

* $$\langle v_1, v_2 \rangle =1 -2 +0 +1=0$$，所以兩行向量正交。
* $$\mathrm{proj}_{CS(A)}(b)  = \frac{\langle b, v_1\rangle}{\|v_1\|^2}v_1 + \frac{\langle b, v_2\rangle}{\|v_2\|^2}v_2 = \frac{3}{10}\begin{bmatrix} 1  \\2  \\-2  \\ 1 \end{bmatrix} + \frac{3}{3}\begin{bmatrix}1 \\ -1 \\0 \\1 \end{bmatrix} = \begin{bmatrix}\frac{13}{10} \\ -\frac{2}{5} \\ - \frac{3}{5} \\ \frac{13}{10} \end{bmatrix}$$

#### 範例：歐式空間

* $$S=\{(x,y,z)| x+y+z=0\}$$為$$\mathbb{R}^3$$的子空間。
* 取標準基底，則$$S=span\left\{ \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ -1\end{bmatrix}\right\}$$
* 取$$A=\begin{bmatrix} 1 & 0 \\ 0  & 1\\ -1 &-1\end{bmatrix}$$，所以$$\mathrm{proj}_A\left(\begin{bmatrix} x \\y\\ z \end{bmatrix}\right) =  A(A^\top A)^{-1}A^\top \begin{bmatrix} x \\y\\ z \end{bmatrix} = \begin{bmatrix} \frac{2x-y-z}{3} \\ \frac{-x+2y-z}{3} \\ \frac{-x-y+2z}{3} \end{bmatrix}$$





