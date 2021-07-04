# 冪零算子\(nilpotent operator\)

* 冪零算子討論經有限次相同線性轉換後，可使得所有向量空間$$V$$中元素變為$$0$$的線性轉換。
* 投影算子討論的是經過一次投影後，則值域不再變化的算子。

## 冪零算子\(nilpotent operator\)

> 線性轉換$$T \in L(V,V)$$，若存在$$k \in \mathbb{N} \ni T^k=0 $$，即$$\forall v \in V, ~ v \in ker⁡(T^k )$$，則稱$$T$$為冪零算子\(nilpotent operator\) $$k^*=\arg\min_k\{T^k (v)=0, \forall v \in V, k \in \mathbb{N}\}$$為$$T$$的指標\(index\)。
>
> 矩陣$$A \in F^{N \times N}$$，若存在$$k \in \mathbb{N} \ni A^k=0$$，則稱$$A$$為冪零矩陣\(nilpotent matrix\)，且稱$$ k^{*} =\arg\min_k \{A^k=0,  k \in\mathbb{N}\}$$為$$A$$的指標\(index\)。

* 依定義得零矩陣為具指標1的冪零矩陣。
* 單位矩陣$$I^k \neq 0, ~\forall k \in \mathbb{N}$$，所以非冪零矩陣。
* 若$$A$$為$$N \times N$$嚴格上三角（下三角）矩陣，則$$A^N=0$$。
  * $$A=\begin{bmatrix} 0 & 1 & 2\\    0 & 0 & 3\\ 0 & 0 & 0  \end{bmatrix} $$    ，$$A^2=\begin{bmatrix} 0 & 0 & 3\\    0 & 0 & 0\\ 0 & 0 & 0  \end{bmatrix} $$，$$A^3=\begin{bmatrix} 0 & 0 & 0\\    0 & 0 & 0\\ 0 & 0 & 0  \end{bmatrix} $$
* 若$$T$$為冪零算子，且$$B$$為$$V$$的一組基底，則$$[T]_B^k = [T^k]_B=[0]_B=0$$，即$$[T]_B$$為冪零矩陣。

### 冪零算子的性質

> 線性轉換$$T \in L(V,V)$$，則下列敘述等價：
>
> 1. $$T$$為具有指標$$k$$的冪零算子
> 2. $$T^k=0$$且$$T^{k−1} \neq 0$$。
> 3. $$ker⁡(T^K )=V$$，$$ker(T^(k−1) ) \neq V$$
> 4. $$\forall v \in V, T^k (v)=0$$且$$\exists u \in V \ni T^(k−1) (u) \neq 0$$

### 冪零矩陣與可逆矩陣

> 若$$A \in F^{N \times N}$$ 為冪零矩陣，則$$I−A$$為可逆矩陣。

Proof:

* 因為$$A$$為冪零矩陣，所以$$\exists k \in \mathbb{N}\ni A^k=0$$
* 所以$$(I−A)(I+A+A^2+\dots+A^{k−1})=I−A^k=I$$ \(QED\)

##  下\(上\)移矩陣

> • 定義$$S_k=\begin{bmatrix} 0 & 0 & 0&\dots & 0 \\ 1 & 0 & 0 & \dots & 0 \\    0 & 1& 0 & \ddots & 0 \\  0 & 0 &1 & \dots & 0 \\\end{bmatrix}_{k \times k}$$，為$$k$$階下移矩陣，$$[S_k]_{ij}=1, ~\forall i=j+1$$且$$ [S_k]_{ij}=0, ~\forall i\neq j+1$$。
>
> 	• 即S\_k 為只有主對角線左斜下方第一排為1，其餘為0的k×k方陣。
>
> • 定義S\_k 的轉置矩陣S\_k^T==\[■8\(0&1&0&0@0&0&1&0@0&⋰&0&1@0&0&0&0\)\]\_\(k×k\) 為k階上移矩陣





