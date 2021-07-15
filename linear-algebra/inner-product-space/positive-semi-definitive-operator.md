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





