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







