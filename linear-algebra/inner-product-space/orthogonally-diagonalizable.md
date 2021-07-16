# 正交對角化 \(orthogonally diagonalizable\)

## 么正\(正交\)相似

> 矩陣$$A,B \in \mathbb{C}^{N \times N}$$，若存在一個么正矩陣$$P \in \mathbb{C}^{N \times N}$$（$$P^{\mathrm{H}}P=PP^{\mathrm{H}}=I_N$$）$$\ni P^{\mathrm{H}} AP=B$$，則稱$$A$$與$$B$$么正相似\(unitarily similar\)，或稱$$A$$與$$B$$么正等價\(unitarily equivalent\)。
>
> 矩陣$$A,B \in \mathbb{R}^{N \times N}$$，若存在一個正交矩陣$$P \in \mathbb{R}^{N\times N}$$（$$P^\top P=PP^\top=I_N$$）$$\ni P^\top AP=B$$，則稱$$A$$與$$B$$正交相似\(orthogonally similar\)，或稱$$A$$與$$B$$正交等價\(orthogonally equivalent\)。

###  么正\(正交\)相似為相似

> * 矩陣$$A$$與$$B$$么正相似，$$B=P^{\mathrm{H}} AP=P^{−1} AP$$，所以$$A$$與$$B$$相似。
> * 矩陣$$A$$與$$B$$正交相似，$$B=P^\top AP=P^{−1} AP$$，所以$$A$$與$$B$$相似。

## 么正\(正交\)對角化

> * 矩陣$$A \in \mathbb{C}^{N \times N}$$，若$$A$$與某個對角矩陣么正相似\($$PP^\mathrm{H}=I_N, P^\mathrm{H} AP=D$$\)，則稱$$A$$可么正對角化\(unitarily diagonalizable\)。
> * 矩陣$$A \in \mathbb{R}^{ N \times N}$$，若$$A$$與某個對角矩陣正交相似\($$PP^\top=I_N, P^T AP=D$$\)，則稱$$A$$可正交對角化\(orthogonally diagonalizable\)。
> * 線性轉換$$T \in L(V,V)$$，若存在$$V$$的一組單範正交基底$$B$$使得$$[T]_B$$ 為一對角矩陣，則稱$$T$$可么正對角化。
>
> ### 么正\(正交\)對角化為對角化
>
> * 矩陣$$ A \in \mathbb{C}^{N\times N}$$ 可么正對角化，則$$A$$可對角化。
> * 矩陣$$A \in \mathbb{R}^{N \times N}$$ 可正交對角化，則$$A$$可對角化。
> * 線性轉換$$T \in L(V,V)$$可么正對角化，則$$T$$可對角化。

Proof:

因為$$A=P^\mathrm{H} DP=P^{−1} DP,~ PP^\mathrm{H}=I_N$$，則$$P$$的行向量為$$A$$的特徵向量，且行向量形成單範正交集。\(QED\)

###  么正相似的性質

> 矩陣$$A,B \in \mathbb{C}^{N \times N}$$ 且$$A$$與$$B$$么正相似\($$P^\mathrm{H} AP=B, ~PP^\mathrm{H}=P^\mathrm{H} P=I_N$$\)，則：
>
> 1. $$A$$為正規矩陣\($$A^\mathrm{H} A=AA^\mathrm{H}$$\)$$\Leftrightarrow B$$為正規矩陣。
> 2. $$A$$為Hermitian matrix \($$A^\mathrm{H}=A$$\)$$\Leftrightarrow B$$為Hermitian matrix。
> 3. $$A$$為skew Hermitian matrix \($$A^\mathrm{H}=−A$$\)$$\Leftrightarrow B$$為skew Hermitian matrix。
> 4. $$A$$為正定矩陣\($$\forall 0 \neq x \in \mathbb{C}^{N \times 1},~ x^\mathrm{H} Ax>0$$\) $$\Leftrightarrow B$$為正定矩陣。
> 5. $$A$$為正半定矩陣\($$\forall 0\neq x \in \mathbb{C}^{N \times 1}, ~x^\mathrm{H} Ax\geq 0$$\)$$\Leftrightarrow B$$為正半定矩陣。
> 6. $$A$$為么正矩陣\($$A^\mathrm{H} A=AA^\mathrm{H}=I_N$$\)$$\Leftrightarrow B$$為么正矩陣。

由於&lt;=的證明只要把=&gt;的證明中的$$P$$改成$$P^\mathrm{H}$$,$$ P^\mathrm{H}$$ 改成$$P$$，因此只證明⇒

Proof \(1\) =&gt;

* $$A^\mathrm{H} A=AA^\mathrm{H}   B^\mathrm{H} B=(P^\mathrm{H} AP)^\mathrm{H} (P^\mathrm{H} AP)=P^\mathrm{H} A^\mathrm{H} PP^\mathrm{H} AP=P^\mathrm{H} A^\mathrm{H} AP=P^\mathrm{H}AA^\mathrm{H} P=P^\mathrm{H} APP^\mathrm{H}A^\mathrm{H} P=BB^\mathrm{H}$$\(QED\)

Proof \(2\):

* $$A^\mathrm{H}=A$$
* $$B^\mathrm{H}=(P^\mathrm{H} AP)^\mathrm{H}=P^\mathrm{H} A^\mathrm{H} P=P^\mathrm{H} AP=B$$ \(QED\)

Proof \(3\):

* $$A^\mathrm{H}=−A$$
* $$B^\mathrm{H}=(P^\mathrm{H} AP)^\mathrm{H}=P^\mathrm{H} A^\mathrm{H} P=−P^\mathrm{H}AP=−B$$ \(QED\)

Proof \(4\):

* $$\forall x \neq 0,~ x^\mathrm{H} Bx=x^\mathrm{H} P^\mathrm{H} APx=(Px)^\mathrm{H} A(Px)$$
* 因為$$P$$為可逆矩陣，所以$$Px \neq 0$$, 且$$A$$為正定矩陣
* 因此 $$x^\mathrm{H} Bx=(Px)^\mathrm{H} A(Px)>0$$ \(QED\)

Proof \(5\):

* $$\forall x\neq 0, x^\mathrm{H} Bx=x^\mathrm{H} P^\mathrm{H} APx=(Px)^\mathrm{H} A(Px)$$
* 因為$$A$$為正半定矩陣
* 所以 $$x^\mathrm{H} Bx=(Px)^\mathrm{H} A(Px) \geq 0$$ \(QED\)

Proof \(6\):

* $$A^\mathrm{H} A=I_N$$
* $$B^\mathrm{H} B=(P^\mathrm{H} AP)^\mathrm{H} (P^\mathrm{H} AP)=P^\mathrm{H} A^\mathrm{H} PP^\mathrm{H} AP=P^\mathrm{H} A^\mathrm{H} AP=P^\mathrm{H} IP=P^\mathrm{H} P=I_N$$ \(QED\)

###  正交相似的必要條件

> 矩陣$$A,B \in \mathbb{R}^{N \times N}$$， 且$$A$$與$$B$$正交相似\($$P^\top AP=B$$， $$PP^\top=P^\top P=I_N$$\) ，則：
>
> 1. $$A$$為symmetric matrix \($$A^\top=A$$\) $$\Leftrightarrow B$$為symmetric matrix。
> 2. $$A$$為skew symmetric matrix \($$A^\top=−A$$\) $$\Leftrightarrow B$$為skew symmetric matrix。
> 3. $$A$$為正交矩陣\($$A^\top A=AA^\top=I_N$$\)$$\Leftrightarrow B$$為正交矩陣。

由於&lt;=的證明只要把=&gt;的證明中的$$P$$改成$$P^\mathrm{H}$$，$$P^\mathrm{H}$$ 改成$$P$$，因此只證明⇒。

Proof \(1\):

* $$A^\top＝A$$
* $$B^\top=(P^\top AP)^\top=P^\top A^\top P=P^\top AP=B$$ \(QED\)

Proof \(2\):

* $$A^\top=−A$$
* $$B^\top=(P^\top AP)^\top=P^\top A^\top P=−P^\top AP=−B $$\(QED\)

Proof \(3\):

* $$A^\top A=I_N$$
* $$B^\top B=(P^\top AP)^\top (P^\top AP)=P^\top A^\top PP^\top AP=P^\top A^\top AP=P^\top P=I_N$$ \(QED\)

## Schur's theorem: 存在單範正交基底使得線性轉換為上三角矩陣

> 線性轉換$$T \in L(V,V)$$若$$char_T (x)$$在$$F$$中可分解，則存在$$V$$的一組單範正交基底$$B$$使得$$[T]_B$$ 為上三角矩陣。



