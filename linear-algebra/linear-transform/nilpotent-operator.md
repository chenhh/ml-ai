# 冪零算子\(nilpotent operator\)

* 冪零算子討論經有限次相同線性轉換後，可使得所有向量空間$$V$$中元素變為$$0$$的線性轉換。
* 投影算子討論的是經過一次投影後，則值域不再變化的算子。

## 冪零算子\(nilpotent operator\)

> 線性轉換$$T \in L(V,V)$$，若存在$$k \in \mathbb{N} \ni T^k=0 $$，即$$\forall v \in V, ~ v \in ker⁡(T^k )$$，則稱$$T$$為冪零算子\(nilpotent operator\) $$k^*=\arg\min_k\{T^k (v)=0, \forall v \in V, k \in \mathbb{N}\}$$為$$T$$的指標\(index\)。
>
> 矩陣$$A \in F^{N \times N}$$，若存在$$k \in \mathbb{N} \ni A^k=0$$，則稱$$A$$為冪零矩陣\(nilpotent matrix\)，且稱$$ k^{*} =\arg\min_k \{A^k=0,  k \in\mathbb{N}\}$$為$$A$$的指標\(index\)。

* 依定義得零矩陣為具指標1的冪零矩陣。
* 單位矩陣$$I^k \neq 0, ~\forall k \in \mathbb{N}$$，所以非冪零矩陣。

