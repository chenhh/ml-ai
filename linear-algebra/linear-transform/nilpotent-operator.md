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
  * $$A=\begin{bmatrix} 0 & 1 & 2\\    0 & 0 & 3\\ 0 & 0 & 0  \end{bmatrix} $$
* 若$$T$$為冪零算子，且$$B$$為$$V$$的一組基底，則$$[T]_B^k = [T^k]_B=[0]_B=0$$，即$$[T]_B$$為冪零矩陣。

### 冪零算子的性質

> 線性轉換$$T \in L(V,V)$$，則下列敘述等價
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

##  下移矩陣

> 定義$$S_k=\begin{bmatrix} 0 & 0 & 0&\dots & 0 \\ 1 & 0 & 0 & \dots & 0 \\    0 & 1& 0 & \ddots & 0 \\  0 & 0 &1 & \dots & 0 \\\end{bmatrix}_{k \times k}$$，為$$k$$階下移矩陣，$$[S_k]_{ij}=1, ~\forall i=j+1$$且$$ [S_k]_{ij}=0, ~\forall i\neq j+1$$。
>
> 即$$S_k$$ 為只有主對角線左斜下方第一排為1，其餘為0的$$k\times k$$方陣。
>
> 定義$$S_k$$ 的轉置矩陣$$S_k^\top=\begin{bmatrix} 0 & 1 & 0&\dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\    0 & 0& 0 & \ddots & 1 \\  0 & 0 &0 & \dots & 0 \\\end{bmatrix}_{k \times k}$$ 為$$k$$階上移矩陣

### 下移矩陣為冪零矩陣

* $$S_4 = \begin{bmatrix}    0 & 0 & 0 & 0 \\   1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$，$$S_4^2=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}$$，$$S_4^3=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{bmatrix}$$，$$S_4^4=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
* 可得到$$S_k$$ 下移矩陣為具有指標$$k$$的冪零矩陣。

## 局部冪零、局部可逆

> 線性轉換$$T \in L(V,V)$$，$$W$$為$$T$$-不變子空間 \($$W$$為子空間且$$T(W) \subseteq W$$\)
>
> * 若$$T_W$$ 為冪零算子，則稱$$T$$在$$W$$上局部冪零\(locally nilpotent on W\)
> * 若$$T_W$$ 為可逆算子，則稱$$T$$在$$W$$上局部可逆\(locally invertible on W\)

* 取$$W=ker⁡(T)$$為$$T$$不變子空間。因為$$\forall v \in W, T(v)=0
* 若$$T$$為冪零算子，則$$V$$為最大冪零區。
* 若$$T$$為可逆算子，則$$V$$為最大可逆區。

### 一般線性轉換核空間會越來越大，值域會越來越小

> 線性轉換$$T \in L(V,V)$$，則
>
> * $$ker⁡(T^i ) \subseteq ker(T^{i+1}),\  \forall i \in \mathbb{N}$$
> * $$R(T^i ) \supseteq R(T^{i+1} ),\  \forall i \in \mathbb{N}$$

Proof:

* $$\forall v \in ker⁡(T^i ),~ T^i (v)=0$$
* $$T^{i+1} (v)=T(T^i (v))=T(0)=0$$
* 所以$$v \in ker⁡(T^{i+1} )$$  \(QED\)
* $$\forall v \in R(T^{i+1} )~\exists u \in V \ni v=T^{i+1} (u)$$
* $$v=T^i (T(u)), ~T(u) \in V$$
* 所以$$v \in R(T^i )$$  \(QED\)

### 核空間經線性轉換後不再增大時，值域經線性轉換也不會縮小

> 線性轉換$$T \in L(V,V), k \in \mathbb{N}$$，則：
>
> $$ ker⁡(T^k )=ker⁡(T^{k+1} )$$若且唯若$$R(T^k )=R(T^{k+1} )

Proof:

* By [rank-nullity theorem](kernel-space-and-image.md#wei-du-ding-li-sylvester-1st-law-or-dimension-theorem-ranknullity-theorem),
* 因為$$T^k \in L(V,V)$$，所以$$\dim⁡(V)=nullity(T^k )+rank(T^k ) $$。
* 因為$$T^{k+1} \in L(V,V)$$，所以$$\dim⁡(V)=nullity(T^{k+1} )+rank(T^{k+1} )
* 若$$ker⁡(T^k )=ker⁡(T^{k+1} ) \Leftrightarrow nullity(T^k )=nullity(T^{k+1})$$\[因為$$ker⁡(T^k )$$為$$ker⁡(T^{k+1} )$$的子空間\] $$\Leftrightarrow rank(T^k )=rank(T^{k+1} )\Leftrightarrow R(T^k )=R(T^{k+1} )$$\[因為$$R(T^{k+1} )$$為$$R(T^k )$$的子空間\] \(QED\)


