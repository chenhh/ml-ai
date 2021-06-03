---
description: inverse matrix
---

# 反矩陣

## 左反矩陣、右反矩陣（left, right inverse matrix）

> 給定矩陣$$ A \in F^{M \times N}$$
>
> * 若存在矩陣$$B \in F^{N \times M} \ni BA=I_N$$，稱$$B$$為$$A$$的左反矩陣。
> * 若存在矩陣$$C \in F^{ N \times M} \ni AC=I_M$$，稱$$C$$為$$A$$的右反矩陣。

* 左\(右\)反矩陣不一定存在。
* 若$$A$$存在左反矩陣，則$$N \leq M$$，因為矩陣秩的最大值為$$\min\{M,N\}$$。
* 若$$A$$存在右反矩陣，則$$N \geq M$$，原因同上。

## 反矩陣（inverse matrix）

> 給定矩陣$$A \in F^{N \times N}$$, 若存在$$B \in F^{N \times N}  \ni BA=AB=I_N$$，稱$$B$$為$$A$$的反矩陣。且稱$$A$$為可逆矩陣\(invertible matrix\)或非奇異矩陣\(non-singular matrix\)
>
> 註：只有方陣才有反矩陣。

* $$B$$為$$A$$的反矩陣$$\Leftrightarrow$$$$B$$為$$A$$的左反矩陣且為A的右反矩陣。

### 反矩陣的唯一性

> • 矩陣$$ A \in F^{N \times N}$$  可逆，則$$A$$的反矩陣存在且唯一，記作$$A^{−1}$$。

proof:

* 令$$B,C$$均為$$A$$的反矩陣，可得  $$AB=BA=I_N$$, $$AC=CA=I_N$$。
* $$∴B=BI_N=B(AC)=(BA)C=I_NC=C$$ \(QED\)

###  反矩陣的反矩陣為原矩陣

> 矩陣$$ A \in F^{N \times N}$$  可逆，• 則$$A^{−1}$$ 可逆，且$$(A^{−1} )^{−1}=A$$

* $$\because AA^{−1}=I_N=A^{−1}⋅A$$ \(QED\)

### 矩陣相乘的反矩陣

> 矩陣 $$A,B \in F^{N \times N}$$ 均為可逆，則$$AB$$可逆，且$$(AB)^{−1}=B^{−1} A^{−1}$$
>
> 可推廣至$$(A_1 A_2⋯A_k )^{−1}=A_K^{−1} A_{k−1}^{−1}\ldots A_2^{−1} A_1^{−1}$$

Proof:

* $$(AB)(B^{−1} A^{−1} )=A(BB^{−1} ) A^{−1}=AI_NA^{−1}=A⋅A^{−1}=I_N$$
* 同理 $$(B^{−1} A^{−1} )(AB)=I_N$$ \(QED\).



















