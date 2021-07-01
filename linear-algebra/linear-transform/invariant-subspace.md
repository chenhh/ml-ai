# 不變子空間\(invariant subspace\)

## 不變子空間

> 線性轉換$$T \in L(V,V)$$，$$ W$$為$$V$$的子空間且滿足$$T(W) \subseteq W$$，則稱$$W$$為$$T$$-不變子空間\($$T$$-invariant subspace\)。
>
>  因為$$T$$是在相同空間做線性變換，不變子空間即轉換後，值域$$T(W)$$仍為定義域$$W$$子集合的集合。
>
> 證明$$W$$為$$T$$-不變子空間的方式為$$\forall w \in W \Rightarrow T(w) \in W$$。

* $$\{0\}, ~V, ~ker(T), ~R(T)$$ 均為$$T$$不變子空間。

  * $$\forall T \in L(V,V), T(0)=0∈\{0\}$$
  * $$\forall T \in L(V,V), T(V) \in V$$
  * $$ker⁡(T)=\{x \in V|T(x)=0\}, ~ T(ker⁡(A)) \subseteq ker⁡(A)$$
  * $$R(T)=\{T(x)| \forall x \in V\}, T(R(A)) \subseteq R(A)$$。





![&#x5E38;&#x898B;&#x4E0D;&#x8B8A;&#x5B50;&#x7A7A;&#x9593;](../../.gitbook/assets/invariant-subspace-min.png)

* 若$$W$$為$$T$$不變子空間，$$T$$在$$W$$上的限制函數$$T_w:W \rightarrow V$$定義為$$T_w (v)=T(v),  \forall v \in W$$\(與原始線性轉換$$T$$相同的函數，但定義域縮小為$$W$$\)，仍然為線性函數。
* 若$$W_1,\dots,W_k$$ 為$$T$$-不變子空間，則$$W_1\cap \dots \cap W_k$$ 與$$W_1+\dots+W_K$$ 均為$$T$$-不變子空間。
* $$T:F[x] \rightarrow F[x]$$為微分算子，$$W=F_n [x]$$，則$$W$$為$$T$$-不變子空間 \($$∵D(W)\subseteq W$$\)。

### 不變子空間之矩陣表示法

### 





