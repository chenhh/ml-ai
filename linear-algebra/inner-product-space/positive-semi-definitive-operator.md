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







