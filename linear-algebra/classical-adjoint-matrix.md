# 古典伴隨矩陣\(classical adjoint matrix\)

## 古典伴隨矩陣\(classical adjoint matrix\)

> 給定矩陣$$A= [a_{ij}] \in F^{N \times N}$$，定義伴隨矩陣$$adj(A)=[cof(a_{j|i})]$$。

#### 範例 

* $$A = \begin{bmatrix} 3 &-2 & 1 \\ 5 & 6 & 2 \\    1 & 0 & -3\end{bmatrix}$$
  * $$cof(a_{11}) = (-1)^{1+1}\begin{vmatrix}  6 & 2 \\ 0  & -3 \end{vmatrix} = -18$$
  * $$cof(a_{12}) = (-1)^{1+2}\begin{vmatrix}  5 & 2 \\ 1  & -3 \end{vmatrix} = 17$$
* 依此類推可得 $$adj(A)= \begin{bmatrix} -18 & -6 & -10 \\17 & -10 & -1 \\ -6 & -2 & 28  \end{bmatrix}$$

### 伴隨矩陣與行列式的關係

> 給定矩陣$$A= [a_{ij}] \in F^{N \times N}$$，則$$A \cdot adj(A) = adj(A) \cdot A = \det(A) \cdot I_N$$

proof:

* 由伴隨矩陣的定義得$$A \cdot adj(A) = \begin{vmatrix} \det(A) & 0 & 0 \\0 & \vdots & 0 \\ 0 & 0 & \det(A)\end{vmatrix} = \det(A) \cdot I_N$$。\(QED\)

### 可逆矩陣的伴隨矩陣

> 給定可逆矩陣$$A= [a_{ij}] \in F^{N \times N}$$ 則
>
> * $$A^{-1}= \frac{adj(A)}{\det(A)}$$
> * $$\det(adj(A)) = (\det(A))^{N-1} \neq0$$ \(可逆\)
>
> 註：可用伴隨矩陣快速求出反矩陣。

* 因為$$A \cdot adj(A) = adj(A) \cdot A = \det(A) \cdot I_N$$且$$\det(A) \neq 0$$\(因為$$A$$可逆\)。
* 移項可得$$A \cdot  \frac{adj(A)}{\det(A)} = \frac{adj(A)}{\det(A)} \cdot A = I_N$$\(QED\)
* 因為$$\det(A \cdot adj(A)) = \det(\det(A) \cdot I_N)$$
* 可得$$\det(A) \cdot \det(adj(A)) = (\det(A))^N$$ 
* 若$$A$$為可逆矩陣，則$$\det(adj(A)) = (\det(A))^{N-1}$$ \(QED\)

### 矩陣可逆若且唯若伴隨矩陣可逆

> $$A= [a_{ij}] \in F^{N \times N}$$可逆若且唯若 $$adj(A)$$可逆。

proof =&gt; 由 可逆矩陣的伴隨矩陣得出 \(QED\)

proof &lt;=

* $$A \cdot adj(A) = adj(A) \cdot A = \det(A) \cdot I_N$$
* 可得 $$A=\det(A) (adj(A))^{-1}$$
* 若$$\det(A) = 0$$時，$$A=0$$，得$$adj(A)=0$$矛盾
* 因此$$det(A) \neq 0 $$，即$$A$$為可逆矩陣  \(QED\)

