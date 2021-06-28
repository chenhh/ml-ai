# 線性轉換

## 線性映射\(轉換\)\(linear mapping or linear transform\)

> 令$$V,W$$為定義在體$$F$$的向量空間，若函數$$T: V \rightarrow W$$滿足：
>
> * $$\forall x,y \in V, ~ T(x+y)= T(x)+T(y)$$
> * $$\forall c \in F, ~ T(cx)= cT(x)$$
>
> 則稱$$T$$為$$V$$至$$W$$的線性映射。
>
> 令$$V$$至$$W$$所有線性映射形成的集合為$$L(V,W)$$。
>
> * 當$$W=V$$時，稱$$T$$為$$V$$上的線性算子\(linear operator\)。
>   * 例如極限、微分等均為線性算子。
> * 當$$W=F$$時，稱$$T$$為$$V$$上的線性泛函\(linear functional\)。
>   * 例和積分、熵為線性泛函。

* $$T:F^{N \times N} \rightarrow F^{N \times N}$$  定義為$$T(A)=A^\top$$，則$$T$$為線性算子。
* $$T_0:V \rightarrow W$$，$$T_0 (v)=0,  \forall v \in V$$為線性映射，稱為零映射函數\(zero mapping function\)。
* $$I_V:V \rightarrow V$$，$$I_V (v)=v,  \forall v \in V$$為線性映射，稱為單位映射函數\(identity mapping function\)。

## 常見平面線性映射

以下線性轉換$$T$$的矩陣表示法均以平面標準基底$$B=\{e_1,e_2\}$$表示。

### 旋轉\(rotation\)

* $$T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$$
* $$T(x,y)=(x \cos⁡ \theta−y \sin\theta, x \sin⁡ \theta +y \cos\theta )$$
* $$T \begin{bmatrix}x \\ y \end{bmatrix} = \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta\end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix}$$
* 為平面上繞原點逆時鐘旋轉$$\theta$$的線性算子。

### 鏡射\(reflection\)

* 對$$x$$軸鏡射，$$T \begin{bmatrix}x \\ y \end{bmatrix} = \begin{bmatrix}  1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix}$$
* 對$$y$$軸鏡射，$$T \begin{bmatrix}x \\ y \end{bmatrix} = \begin{bmatrix}  -1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix}$$

### 投影\(projection\)

* 對$$x$$軸投影，$$T \begin{bmatrix}x \\ y \end{bmatrix} = \begin{bmatrix}  1 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix}$$
* 對$$y$$軸投影，$$T \begin{bmatrix}x \\ y \end{bmatrix} = \begin{bmatrix}  0 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix}$$

## 線性映射的必要條件

> 若$$T \in L(V,W)$$為線性映射，則以下條件必須全部成立：
>
> 1. $$T(0)= 0$$
> 2. $$\forall v \in V, T(-v)=-T(v)$$
> 3. $$\forall v_1, v_2 \in V, T(v_1-v_2)= T(v_1)- T(v_2)$$
>
> 註：以上條件只要一個不成立時，$$T$$不是線性映射；但是條件均成立時，不保證$$T$$為線性映射。

Proof:

*  $$0+T(0)=T(0)=T(0+0)=T(0)+T(0) \Rightarrow T(0)=0$$。
* 因為$$T(cv)=cT(v)$$，令$$c=−1$$，則$$T(−v)=−T(v)$$。
* $$T(v_1−v_2 )=T(v_1+(−v_2 ))=T(v_1 )+T(−v_2 )=T(v_1 )−T(v_2 )$$

### 線性映射的充要條件

> 若$$T$$為由向量空間$$V$$至$$W$$的映射（函數），則以下條件等價：
>
> * $$T$$為線性映射。
> * $$\forall a,b \in F，~ u,v \in V $$，可得$$T(au+bv)=aT(u)+bT(v)$$。

### 給定定義域基底之線性映射的唯一性

> 令$$T,U \in L(V,W)$$為兩線性映射，且$$B=\{ b_1, b_2, \dots, b_N\}$$為向量空間$$V$$的基底，則$$T=U$$若且唯若$$T(b_i) = U(b_i), ~ i=1,2,\dots, N$$
>
> 註：如果要證明$$T=U$$，應該要滿足$$\forall v \in V, T(v)=U(v)$$，但因為$$V$$的所有元素均可用$$B$$生成，因此只要證明$$T(b_i) = U(b_i)$$即可。

Proof =&gt; 顯然成立

Proof &lt;= 

* $$\forall v \in V, v=\sum_{i=1}^N a_i b_i , \forall a_i \in F$$
* 所以$$T(v)=T(\sum_{i=1}^N a_i b_i )=\sum_{i=1}^N a_i T(b_i)=\sum_{i=1}^N a_i U(b_i ) =U(\sum_(i=1)^N a_i b_i=U(v)$$ \(QED\)

### 當線性映射的定義域基底決定後，則整個線性映射唯一決定

### 

> 令$$V,W$$為定義在體$$F$$的向量空間，$$B=\{b_1, b_2,\dots, b_N\}$$為向量空間$$V$$的基底。對於$$W$$中的任意向量$$w_1, w_2, \dots, w_N$$，均存在唯一的線性轉換$$T \in L(V,W)$$使得$$T(b_i) = w_i, ~i=1,2,\dots, N$$。

proof: 

* 定義函數$$ T:V \rightarrow W$$
* 因為$$B$$為$$V$$的基底，所以$$\forall v \in V,  ~v=a_1 b_1+a_2 b_2+ \dots +a_N b_N, ~ \forall a_i \in F$$
* 定義 $$T(v)=a_1 w_1+a_2 w_2+\dots+a_N w_N$$
* 因為基底集合內元素線性獨立
* 所以$$\forall i=1,2,\dots ,N$$ ，可得$$b_i=0b_1+0b_2+\dots+0b_{i−1}+b_i+0b_{i+1}+\dots+0b_N$$
* 因此$$T(b_i)=0w_1+0w_2+\dots+0w_{i−1}+w_i+0w_{i+1}+\dots +0w_N=w_i$$

要證明$$T$$為線性函數

* $$\forall a ,c \in F,~ u,v \in V$$令$$ u=\sum_{i=1}^N a_i b_i, ~ v=\sum_{i=1}^N c_i b_i $$
* 所以$$T(u)=\sum_{i=1}^N a_i w_i, ~ T(v)=\sum_{i=1}^N c_i w_i $$ 
* 因為$$au+cv=a(\sum_{i=1}^N a_i b_i)+c(\sum_{i=1}^N  c_i b_i)=\sum_{i=1}^N (aa_i+cc_i )  b_i$$
* 所以$$T(au+cv)=\sum_{i=1}^N (aa_i+cc_i )  w_i=aT(u)+bT(v)$$

證明$$T$$的唯一性

* 若存在$$T, U \in L(V,W)$$使得$$T(b_i)=w_i$$且$$U(b_i)=w_i$$
* 由給定基底之線性映射的唯一性得$$T=U$$。\(QED\)。

