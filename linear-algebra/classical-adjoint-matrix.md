# 古典伴隨矩陣\(classical adjoint matrix\)

## 古典伴隨矩陣\(classical adjoint matrix\)

> 給定矩陣$$A= [a_{ij}] \in F^{N \times N}$$，定義伴隨矩陣$$adj(A)=[cof(a_{j|i})]$$。

#### 範例 

* $$A = \begin{bmatrix} 3 &-2 & 1 \\ 5 & 6 & 2 \\    1 & 0 & -3\end{bmatrix}$$
  * $$cof(a_{11}) = (-1)^{1+1}\begin{vmatrix}  6 & 2 \\ 0  & -3 \end{vmatrix} = -18$$
  * $$cof(a_{12}) = (-1)^{1+2}\begin{vmatrix}  5 & 2 \\ 1  & -3 \end{vmatrix} = 17$$
* 依此類推可得 $$adj(A)= \begin{bmatrix} -18 & -6 & -10 \\17 & -10 & -1 \\ -6 & -2 & 28  \end{bmatrix}$$

### 伴隨矩陣與行列式的關係

> 給定矩陣$$A= [a_{ij}] \in F^{N \times N}$$，則$$A \cdot adj(A) = adj(A) \cdot A = \det(A) \cdot I_n$$



