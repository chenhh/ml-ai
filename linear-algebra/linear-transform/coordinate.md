# 座標化\(coordinate\)

## 簡介

座標化的功能在於將任意向量空間中的元素均使用向量的方法表示。如多項式空間，連續函數空間，只要給定基底，則函數即可表示為該基底下唯一的向量\(但可能為無窮維度的向量\)。

## 座標向量\(coordinate vector\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。
>
> 若$$v=a_1 b_1+a_2 b_2 +\dots+ a_N b_N$$，定義行向量$$x=\begin{bmatrix} a_1 \\ a_2 \\ \vdots\\ a_N\end{bmatrix}$$為向量$$v$$相對於基底$$B$$的座標向量（corrdinate vector of v relative to B），記為$$[v]_B$$。
>
> 因為向量可唯一表示為基底的線性組合，所以$$[v]_B$$存在唯一。

一般集合中的元素是無序的，但是向量為基底的元素之線性組合，若基底元素無序時，會造成對應的座標參數$$a_i$$ 不一致，因此要求基底為有序集合，即$$\{b_1,b_2,b_3\}$$與$$\{b_1,b_3,b_2 \}$$視為不同的基底。

範例

* $$V=\mathbb{R}^2, B=\{(1,0), (0,1)\} $$ \(standard basis\)
  * $$ v=(2,3)=2(1,0)+3(0,1), [v]_β=\begin{bmatrix} 2\\ 3\end{bmatrix}$$
* $$V=\mathbb{R}^2，B=\{(0,1), (1,0)\}  $$
  *  $$v=(2,3)=3(0,1)+2(1,0) ~ [v]_β=\begin{bmatrix} 3\\ 2\end{bmatrix}$$
* $$V=R_3 [x], B=\{1,(x−1), (x−1)^2 \}$$
  * $$f(x)=4+5x−7x^2=f(1)+f^{′}(x)(x−1)+\frac{f^{(2)}(1)}{2} (x−1)^2=2−9(x−1)−7(x−1)^2$$
  * 所以$$[f]_B=\begin{bmatrix} 2 \\ 9\\ 7 \end{bmatrix}$$

### 座標向量的性質

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。
>
> 則$$\forall a, b \in F, ~ u,v \in V$$：
>
> * \(座標向量為線性算子\)$$[au+bv]_B = a[u]_B + b[v]_B$$
> * \(座標向量唯一組\) $$u=v \Leftrightarrow [u]_B = [v]_B$$
> * \[給定基底，則所有元素有唯一座標\] $$\forall v \in V, \exists ! x \in F^{N \times 1} \ni [v]_B= x$$

Proof:

* 令$$u=\sum_{i=1}^N c_i b_i, ~ v=\sum_{i=1}^N d_i b_i $$
* 所以$$[u]_B=\begin{bmatrix} c_1 \\ c_2 \\ \vdots\ c_N \end{bmatrix}, ~[v]_B=\begin{bmatrix} d_1 \\ d_2 \\ \vdots \\ d_N\end{bmatrix}$$
* $$au+bv=a(\sum_{i=1}^N c_i b_i)+b(\sum_{i=1}^N d_i b_i)=\sum_{i=1}^N (ac_i+bd_i ) b_i $$
* 可得$$[au+bv]_B\begin{bmatrix}  ac_1 + bd_1 \\ ac_2 + bd_2 \\ \vdots \\ ac_N + bd_N\end{bmatrix}=a[u]_B+b[v]_B$$

 唯一性

* 取$$v=\sum_{i=1}^N x_i b_i $$，$$ x=\begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix} \in F^{ N\times 1}$$，所以$$[v]_B = \begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix} = x$$
* 若存在$$u \in  V \ni [u]_B=x$$，則 $$u=\sum_{i=1}^N x_i b_i=v$$
* 所以$$u=v$$，即座標向量的唯一性。\(QED\)









