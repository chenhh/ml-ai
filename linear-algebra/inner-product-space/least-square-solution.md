# 最小平方解\(least square solution\)

## 簡介

* 矩陣$$A \in F^{M \times N} , A=\begin{bmatrix} A_{:1} & \dots & A_{:N}\end{bmatrix},~ A^{\mathrm{H}}=  \begin{bmatrix} \overline{A_{:1}^\top} \\ \vdots \\ \overline{A_{:N}^\top}\end{bmatrix} = \begin{bmatrix} A_{:1}^{\mathrm{H}} \\ \vdots \\ A_{:N}^{\mathrm{H}}\end{bmatrix}$$
* $$A^{\mathrm{H}}A =  \begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} &  \dots &A_{:1}^{\mathrm{H}}A_{:N} \\  \vdots & \ddots & v\dots \\ A_{:N}^{\mathrm{H}}A_{:1} & \dots & A_{:N}^{\mathrm{H}}A_{:N}  \end{bmatrix} \in F^{N \times N}$$稱為正規矩陣（normal matrix）。
* 例如：$$A=\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{bmatrix}$$，$$A^{\mathrm{H}}=\begin{bmatrix} \overline{a_{11}} & \overline{a_{21}} & \overline{a_{31}} \\ \overline{a_{12}} & \overline{a_{22}} & \overline{a_{32}} \end{bmatrix}$$，$$A^{\mathrm{H}}A=\begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} & A_{:1}^{\mathrm{H}}A_{:2} \\ A_{:2}^{\mathrm{H}}A_{:1} & A_{:2}^{\mathrm{H}}A_{:2}  \end{bmatrix}$$
* 而$$x^{*} \in \mathbb{C}^{N \times 1}$$為$$x^{*}=\arg\min_x{\|Ax-b\|}$$的最佳解$$\Leftrightarrow A^{\mathrm{H}}Ax=A^{\mathrm{H}}b$$之解。

## 正規矩陣的基本子空間

> 令矩陣$$A \in F^{M \times N}$$，則：
>
> 1. $$ker(A^{\mathrm{H}}A) =ker(A)=\{x \in F^{N \times 1} | Ax=0\}$$
> 2. $$rank(A^{\mathrm{H}}A) = rank(A)$$\(只有rank相同，但值域不相同\)
> 3. $$Lker(A^{\mathrm{H}}A) = Lker(A)$$
> 4. 矩陣$$A$$行向量線性獨立$$\Leftrightarrow A^{\mathrm{H}} A$$為可逆矩陣。
> 5. 矩陣$$A$$列向量線性獨立$$\Leftrightarrow A^{\mathrm{H}} A$$為可逆矩陣。

Proof \(1\)

 =&gt;

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



