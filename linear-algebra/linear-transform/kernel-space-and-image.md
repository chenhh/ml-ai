# 核空間及像集\(kernel space and image\)

## 直像與反像\(direct image and inverse image\)

> 線性轉換$$T \in L(V,W)$$，令集合$$S_1 \subseteq V$$，$$S_2 \subseteq W$$，則
>
> * $$T(S_1) =\{ T(v) | \forall v \in S_1 \}$$為集合$$S_1$$ 在$$T$$轉換後的直像\(direct image\)，或稱函數的值域\(range\)。
> * $$T^{-1}(S) = \{v \in V | T(v) = S_2\}$$為$$S_2$$在$$T$$轉換的前像\(inverse image, pre-image\)。
>
> $$T^{−1}$$ 並非指$$T$$可逆，只是一個符號，代表從$$W\rightarrow V$$的映射。 此定義可用於一般的函數，而非只是線性函數。

* 在[函數的映像與前象](../../math-analysis/set/function.md#han-shu-de-ying-xiang-yu-qian-xiang)中，若$$T$$為一對一函數時，$$S_1 = T^{−1} (T(S_1 ))$$。
* 若$$T$$為映成函數時，$$T(T^{−1} (S_2 )) = S_2$$ 。



![&#x76F4;&#x50CF;&#x8207;&#x524D;&#x50CF;](../../.gitbook/assets/image-preimage-min.png)

### 子空間經線性轉換後仍為子空間

> 線性轉換$$T \in L(V,W)$$，且$$V_s$$為$$V$$的子空間，$$W_s$$為$$W$$的子空間，則$$T(V_s)$$為$$W$$的子空間，$$T^{-1}(W_s)$$為$$V$$的子空間。
>
> 子空間的充要條件是空間內元素的任意線性組合仍在空間中（且包含0 向量）。而線性轉換可保持此性質。

proof:

* 因為$$0 = T(0) \in T(V_s)$$，所以$$T(V_s) \neq \emptyset$$。
* 因為$$T \in L(V,W)$$且$$V_s \subseteq V$$，所以$$\forall u, v \in T(V_s)$$存在$$x, y\in V \ni T(x)=u,  ~ T(y) = v$$。
* 因為$$V_s$$為$$V$$的子空間，所以$$\forall a,b \in F$$，$$ax+by \in V_s$$可得$$T(ax+by) \in T(V_s)$$。
* 依線性轉換定義可得 $$aT(x)+bT(y) \in T(V_s)$$，即$$au+bv \in T(V_s)$$。
* 所以$$T(V_s)$$為$$W$$的子空間。
* 同理可得$$T^{-1}(W_s)$$為$$V$$的子空間 \(QED\). 



