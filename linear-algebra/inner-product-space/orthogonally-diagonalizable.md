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

>

### 





