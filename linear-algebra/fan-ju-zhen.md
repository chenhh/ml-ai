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



