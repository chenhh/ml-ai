# 正\(半\)定算子\(positive \(semi\) definitive operator\)

## Hermitian矩陣二次式必為實數值

> 矩陣$$A \in \mathbb{C}^{N \times N}$$，則$$A^{\mathrm{H}}=A \Leftrightarrow x^{\mathrm{H}}Ax \in \mathbb{R}, ~\forall x \in C^{N \times 1}$$

Proof =&gt; \(證明$$ x^{\mathrm{H}}Ax \in \mathbb{R}$$等於證明$$x^{\mathrm{H}} Ax=\overline{x^{\mathrm{H}} Ax}$$\)

* $$\overline{x^{\mathrm{H}} Ax}=\overline{(x^{\mathrm{H}}Ax)^\top} = (x^{\mathrm{H}} Ax)^{\mathrm{H}} = x^{\mathrm{H}}A^{\mathrm{H}} (x^{\mathrm{H}})^{\mathrm{H}}=x^{\mathrm{H}}A^{\mathrm{H}}x$$\(QED\)

Proof &lt;= \(to prove $$A^\mathrm{H}=A$$等於證明$$y^\mathrm{H} A^\mathrm{H} x=y^\mathrm{H} Ax, ~\forall x,y \in \mathbb{C}^{N \times 1}$$\)

* $$\forall x,y \in \mathbb{C}^{N \times 1}$$, $$(x+y)^\mathrm{H} A(x+y)=x^\mathrm{H} Ax＋x^\mathrm{H} Ay＋y^\mathrm{H} Ax+y^\mathrm{H} Ay$$
* 因為$$x^\mathrm{H} Ax \in \mathbb{R}, ~y^\mathrm{H} Ay \in \mathbb{R}, ~(x+y)^\mathrm{H} A(x+y) \in \mathbb{R}$$
* $$\Rightarrow x^\mathrm{H} Ay+y^\mathrm{H} Ax \in \mathbb{R}$$
* $$\Rightarrow (x^\mathrm{H} Ay+y^\mathrm{H} Ax)^\mathrm{H}=x^\mathrm{H} Ay+y^\mathrm{H} Ax$$
* $$\Rightarrow y^\mathrm{H} A^\mathrm{H} x+x^\mathrm{H} A^\mathrm{H} y=x^\mathrm{H} Ay+y^\mathrm{H} Ax$$−−\(a\)
* 取$$x=ix$$代入\(a\)得
* $$y^\mathrm{H} A^\mathrm{H} (ix)+(ix)^\mathrm{H} A^\mathrm{H} y=(ix)^\mathrm{H} Ay+y^\mathrm{H} A(ix)$$
* $$\Rightarrow iy^\mathrm{H} A^\mathrm{H} x−ix^\mathrm{H} A^\mathrm{H} y=−ix^\mathrm{H} Ay+iy^\mathrm{H} Ax$$
* $$\Rightarrow y^\mathrm{H} Ax−x^\mathrm{H} Ay=−x^\mathrm{H} Ay+y^\mathrm{H} Ax$$−−\(b\)
* \(a\)+\(b\)得$$2y^\mathrm{H} A^\mathrm{H} x=2y^\mathrm{H} Ax$$
* 所以$$A^\mathrm{H}=A $$\(QED\)

###  自伴算子的雙變數線性算子必為實數值

> $$V$$為定義在$$\mathbb{C}$$的內積空間，線性轉換$$T \in L(V,V)$$，則：
>
> $$T$$為自伴算子（$$T^{*}=T$$）$$\Leftrightarrow$$$$\langle T(x), x \rangle \in \mathbb{R}, ~\forall x \in V$$。

Proof =&gt;

* $$\langle T(v),v \rangle= \langle v, T^∗ (v) \rangle= \overline{\langle T^∗ (v),v \rangle} =\overline{ \langle T(v),v \rangle}$$ 
* 所以$$\langle T(v),v \rangle=\overline{\langle T(v),v \rangle } \in \mathbb{R}$$

Proof &lt;=

* $$\forall x,y \in V, \langle T(x+y),x+y \rangle=\langle T(x)+T(y),x+y \rangle= \langle T(x),x \rangle +\langle T(x),y \rangle + \langle T(y),x \rangle+ \langle T(y),y \rangle$$
* 因為$$\langle T(x),x \rangle \in \mathbb{R}$$，$$\langle T(y),y \rangle  \in \mathbb{R}$$，$$\langle T(x+y),x+y \rangle \in \mathbb{R}$$
* $$\Rightarrow \langle T(x),y⟩+⟨T(y),x \rangle \in \mathbb{R}$$
* $$\Rightarrow \overline{\langle T(x),y \rangle +\langle T(y),x \rangle}= \langle T(x),y \rangle+ \langle T(y),x\rangle$$
* 而 $$\overline{\langle T(x),y \rangle+ \langle T(y),x \rangle}=\langle y,T(x) \rangle + \langle x,T(y) \rangle$$
* $$\Rightarrow  \langle y,T(x) \rangle+ \langle x,T(y) \rangle= \langle T(x),y \rangle+ \langle T(y),x \rangle$$−−\(a\)
* 取$$x=ix$$代入\(a\)得
* $$\langle y,T(ix) \rangle+\langle ix,T(y) \rangle= \langle T(ix),y \rangle +\langle T(y),ix \rangle$$
* $$\Rightarrow  \langle y, iT(x) \rangle+ \langle ix, T(y) \rangle = \langle iT(x),y \rangle+ \langle T(y),ix \rangle$$
* $$\Rightarrow −i \langle y,T(x) \rangle+i \langle x,T(y) \rangle =i \langle T(x),y \rangle −y \langle T(y),x \rangle$$
* $$\Rightarrow − \langle y,T(x) \rangle+ \langle x,T(y) \rangle = \langle T(x),y \rangle− \langle T(y),x \rangle$$−−\(b\)
* \(a\)+\(b\)得$$2 \langle x,T(y) \rangle=2 \langle T(x),y \rangle$$
* $$\Rightarrow \langle x,T(y) \rangle= \langle T(x),y \rangle= \langle x,T^∗ (y) \rangle$$
* $$\Rightarrow  \langle T(y),x \rangle = \langle T^∗ (y),x \rangle, \forall x,y \in V$$
* $$\Rightarrow T(y)=T^∗ (y), \forall y \in V$$
* 所以$$T=T^∗$$ \(QED\)

## 矩陣的二次式\(quadratic form\)

> * 矩陣$$A \in \mathbb{C}^{N \times N}$$，定義$$A$$的二次式\(quadratic form\)為$$Q(x)=x^\mathrm{H} Ax, ~\forall x \in \mathbb{C}^{N \times 1}$$。
> * 矩陣$$A \in \mathbb{R}^{N \times N}$$，定義$$A$$的二次式\(quadratic form\)為$$Q(x)=x^\top Ax, ~\forall x \in \mathbb{R}^{N \times 1}$$。

#### 範例

* $$A=\begin{bmatrix}    1 & 2 & 3 \\  2 & 3 & 4 \\  3 & 4 & 5\end{bmatrix}$$，$$x=\begin{bmatrix} x \\y \\z \end{bmatrix}$$
* $$Q(x)=x^\top A x = \begin{bmatrix} x & y &z \end{bmatrix} \begin{bmatrix}    1 & 2 & 3 \\  2 & 3 & 4 \\  3 & 4 & 5\end{bmatrix} \begin{bmatrix} x \\ y \\z \end{bmatrix} = x^2 +3y^2+5z^2+4xy+6xz $$
*  對照二次式展開的形式與矩陣$$A$$的參數可發現，主對角線$$[A]_{ii},~ i=1,2,3$$分別為$$x^2,y^2,z^2$$ 的係數，而$$[A]_{ij}$$ 分別是$$x$$中第$$i$$個元素與第$$j$$個元素相乘的係數。

## 正\(半\)定算子

> * 線性轉換$$T \in L(V,V)$$，若$$T$$為自伴算子（$$T^∗=T$$）且（$$\langle T(v) ,v \rangle >0,~\forall v \neq 0$$），則稱$$T$$為正定算子\(positive definite operator\)  。
> * 矩陣$$A \in \mathbb{C}^{N \times N}$$，若$$A$$為Hermitian matrix \($$A^\mathbb{H}=A$$\)且$$Q(x)=x^\mathrm{H} Ax>0, ~\forall x \neq 0$$，則稱$$A$$為正定矩陣  。
> * 線性轉換$$T \in L(V,V)$$，若$$T$$為自伴算子\($$T^∗=T$$\)且$$\langle T(v),v \rangle \geq 0, ~\forall v \in V$$，則稱$$T$$為正半定算子\(positive semi-definite operator\)  。
> * 矩陣$$A \in \mathbb{C}^{N \times N}$$，若$$A$$為Hermitian matrix \($$A^\mathrm{H}=A$$\)且$$Q(x)=x^\mathrm{H} Ax \geq 0, ~\forall x \in \mathbb{C}^{N \times 1}$$，則稱$$A$$為正半定矩陣  。

此原始定義因為需考慮所有的向量v計算後是否大於（等於）零，因此不容易判斷是否為正（半）定算子（正（半）定矩陣）。

$$T$$為自伴算子（$$A$$為Hermitian matrix）\)是正定算子的充分條件，否則二次式無法保證為實數。

### 正定矩陣的性質\(必要條件\)

> $$A \in \mathbb{C}^{N \times N}$$ 為正定矩陣，則：
>
> 1. $$A$$為正規矩陣\($$AA^\mathrm{H}=A^\mathrm{H} A$$\)   。
> 2. $$A$$的相異特徵根對應之特徵向量必定正交   。
> 3. $$A$$為正半定矩陣   。
> 4. $$A$$的所有特徵根均為正值\($$\lambda_i>0, ~i=1,2,\dots, N$$\)   。
> 5. $$A$$為可逆矩陣\($$A^{−1}$$ 存在\)   。
> 6. $$A$$的主對角項元素均為正值   。

Proof \(1\):

* 因為$$A$$為Hermitian矩陣，所以$$A$$為正規矩陣\(QED\)

Proof \(2\):

*  同\(1\)，因為$$A$$為正規矩陣，所以相異特徵根對應之特徵向量必正交 \(QED\)

Proof \(3\):

* 由定義可得$$\forall x\in V, x^\mathrm{H} Ax>0$$且$$ 0A^\mathrm{H} 0=0$$ \(QED\)

Proof \(4\):

* 令$$\lambda$$為$$A$$的特徵根，依定義得$$\exists x \neq 0 \ni Ax=\lambda x$$。
* 由正定矩陣的定義可得$$0<x^\mathrm{H} Ax=x^\mathrm{H} \lambda x= \lambda x^\mathrm{H} x=\lambda \|x\|^2  $$
* 因為$$x \neq 0$$，得$$\|x\|^2>0$$，所以$$\lambda>0$$ \(QED\)

Proof \(5\):

* 若$$A$$不為可逆矩陣，則$$ker⁡(A)\neq \{0\}$$，即$$\exists x \neq 0 \ni Ax=0$$，得$$x^\mathrm{H} Ax=x^\mathrm{H} 0=0$$\(與正定矩陣定義矛盾\)  。
*  因此$$A$$為可逆矩陣 \(QED\)

Proof \(6\):

* 取$$x=e_i \neq 0$$。
* 所以$$0<x^\mathrm{H} Ax=e_i^\mathrm{H} Ae_i=e_i^\mathrm{H} A_{:i}=(A)_{ii}, ~i=1,2,\dots,N$$ \(QED\)

### 正半定矩陣的性質\(必要條件\)

> $$A \in \mathbb{C}^{N \times N}$$ 為正半定矩陣，則：
>
> 1. $$A$$為正規矩陣\($$AA^\mathrm{H}=A^\mathrm{H} A$$\)   。
> 2. $$A$$的相異特徵根對應之特徵向量必定正交   。
> 3. $$A$$的所有特徵根均為非負值\($$\lambda_i \geq 0, ~\forall i$$\)   。
> 4. $$A$$的主對角項元素均為非負值   。

Proof \(1\)

* 因為$$A$$為Hermitian矩陣，所以$$A$$為正規矩陣\(QED\)

Proof \(2\):

* 同\(1\)，因為$$A$$為正規矩陣，所以相異特徵根對應之特徵向量必正交 \(QED\)

Proof \(3\):

* 令$$\lambda$$為$$A$$的特徵根，所以$$\exists x \neq 0 \ni Ax=\lambda x$$。
* 由正定矩陣的定義可得$$0 \leq x^\mathrm{H} Ax=x^\mathrm{H} \lambda x=\lambda x^\mathrm{H} x=\lambda \|x\|^2$$。
* 因為$$x \neq 0$$，所以$$\|x\|^2>0$$，得$$\lambda \geq 0$$ \(QED\)

Proof \(4\):

* 取$$x=e_i \neq 0$$。
* $$0<x^\mathrm{H} Ax=e_i^\mathrm{H} Ae_i=e_i^\mathrm{H} A_{:i}=[A]_ii,~ i=1,2,\dots,N$$ \(QED\)

