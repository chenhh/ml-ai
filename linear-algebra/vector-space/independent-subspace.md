# 獨立子空間\(independent subspace\)

## 獨立子空間

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令$$W_1, W_2, \dots, W_k$$為$$V$$的子空間。
>
> 若$$W_i \cap \sum_{j \neq i} W_j = \{0\}, \forall i =1,2,\dots, k$$，則稱$$W_1, W_2, \dots, W_k$$為獨立子空間。
>
> * 註：子空間必須包含0向量，因此交量至少有一個0向量。
> * $$W_i \cap \sum_{j \neq i} W_j =\{0\}$$的定義是避免$$W_i$$可以由其它子空間線性組合而成。

* $$K=2$$時，$$W_1,W_2$$ 為獨立子空間指$$W_1 \cap W_2=\{0\}$$。
* $$K=3, ~W_1,W_2,W_3$$ 為獨立子空間指
  * $$W_1 \cap (W_2+W_3 )=\{0\}$$
  * $$W_2 \cap (W_1+W_3 )=\{0\}$$
  * $$W_3 \cap (W_1+W_2 )=\{0\}$$
* 若$$W_i\cap W_j=\{0\}, ~\forall i \neq j$$時，稱$$W_1,W_2, \dots ,W_k$$ 兩兩獨立\(pairwise independence\)。 所以獨立子空間保證兩兩獨立

$$K \geq 3$$時，兩兩獨立未必保證獨立子空間。

* 例如$$V=\mathbb{R}^3$$

  * $$W_1=\{(x,0,0)|x \in \mathbb{R}\}=span(\{(1,0,0)\})$$
  * $$W_2=\{(0,y,0)| y \in \mathbb{R}\}=span(\{(0,1,0)\})$$
  * $$W_3=\{(x,x,0)|x \in \mathbb{R}\}=span(\{(1,1,0)\})$$
  * $$W_1,W_2,W_3$$ 為兩兩獨立，但不是獨立子空間，因$$W_3 \cap (W_1+W_2 )=span\{(1,1,0)\} \cap span\{(1,0,0),(0,1,0)\}=span{(1,1,0)}≠{0}$$

### 獨立子空間彼此之間無法生成

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令$$W_1, W_2, \dots, W_k$$為$$V$$的子空間。則以下條件等價：
>
> 1. $$W_1, W_2, \dots, W_k$$為獨立子空間。
> 2. 令$$w_i \in W_i, \forall i$$，若$$w_1+w_2+\dots + w_k=0$$，則$$w_1=w_2=\dots =w_k=0$$
> 3. $$\dim(W_1+W_2+\dots+W_k) =\dim(W_1)+\dim(W_2)+\dots + \dim(W_k)$$

註：非獨立子空間的[和空間維度](sum-space.md#he-kong-jian-de-wei-du)為$$\dim(W_1 +W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$。而獨立子空間$$W_1 \cap W_2 = \{0\}$$，因此$$\dim(W_1 \cap W_2) = 0$$。

## 直和\(direct sum\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令$$W_1, W_2, \dots, W_k$$為$$V$$的獨立子空間。若$$V=W_1 +W_2 + \dots + W_k$$為和空間，則稱$$W_1, W_2, \dots, W_k$$形成$$V$$的直和，記為$$V = W_1 \oplus W_2 \oplus \dots \oplus W_k$$。

### 立體空間為x、y、z軸的直和

$$V=\mathbb{R}^3$$

* $$W_1=\{(x,0,0)|x \in \mathbb{R}\}=span\{(1,0,0)\} $$
* $$W_2=\{(0,y,0|y \in \mathbb{R}\}=span\{(0,1,0)\} $$
* $$W_3=\{(0,0,z)|z \in \mathbb{R}\}=span\{(0,0,1)\} $$
* $$W_1+W_2+W_3=span\{(1,0,0), (0,1,0), (0,0,1)\}=\mathbb{R}^3=V $$
* $$W_1\cap(W_2+W_3 )=\{0\}$$
* $$W_2 \cap (W_1+W_3 )=\{0\}$$
* $$W_3\cap (W_1+W_2 )=\{0\}$$
* 所以$$V=W_1 \oplus W_2 \oplus W_3$$

### 任何一個方陣必可表示成一個對稱矩陣與斜對稱矩陣之和

* $$V \in F^{N \times N}$$
* $$W_1=\{A \in V|A^{\top}=A\}$$
* $$W_2=\{A \in V|A^{\top}=−A\}$$
* 則$$W_1,W_2$$ 為$$V$$的子空間，且$$V=W_1 \oplus W_2$$
  * $$V=W_1+W_2    $$
  * $$\forall A \in V, A=\frac{A+A^{\top}}{2}+\frac{A−A^{\top}}{2}$$
  * 因為$$\left( \frac{(A+A^\top}{2}\right)^{\top}=\frac{A^\top+A}{2} \in W_1$$，$$\left( \frac{(A-A^\top}{2}\right)^{\top}=\frac{A^\top-A}{2} \in W_2$$
  * 所以$$A \in W_1+W_2    $$
  * 而$$\forall A \in W_1 \cap W_2$$，可得$$A \in W_1$$且$$ A \in W_2    $$
  * 即同時滿足$$A^\top=A$$且$$A^\top=−A$$，可得$$A=−A \Rightarrow 2A=0 \Rightarrow A=0 $$
  * 所以$$W_1 \cap W_2=\{0\}$$





### 







