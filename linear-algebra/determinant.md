# 行列式\(determinant\)

## 高階行列式

> $$A=[a_{ij }] \in F^{N \times N}$$，則$$A$$的行列式$$det(A)$$可遞迴定義成
>
> * $$N=1,det⁡(A)=a_{11}$$
> * $$N \geq 2$$, $$det(A) = \sum_{j=1}^N (-1)^{1+j} a_{1j} det(A_{(1|j)})$$
> * $$A_{(1|j) }$$ 為A中去掉第1列\(row\)，第$$j$$行的$$(N-1) \times (N-1)$$子矩陣
>
> 可以從矩陣的任一列或行展開，只要該列或行中有越多的0，則計算量越少

$$A=\begin{bmatrix} 0 &1  &3 \\ -2 &-3 &  -5\\ 4 & -4& 4\end{bmatrix}$$

從第一列展開，得$$det(A)= 0 \begin{vmatrix} -3 & -5 \\ -4 & 4  \end{vmatrix} - 1 \begin{vmatrix} -2 & -5 \\ 4 & 4  \end{vmatrix} +3 \begin{vmatrix} -2 & -3 \\ 4 & -4  \end{vmatrix}  =-1 \cdot (-8 + 20) + 3\cdot (8 + 12) =  48$$

從第二行展開，得

$$det(A)= -1 \begin{vmatrix} -2 & -5 \\ 4 & 4 \end{vmatrix} -3 \begin{vmatrix} 0 & 3 \\ 4 & 4 \end{vmatrix} + 4 \begin{vmatrix} 0 & 3 \\ -2 & -5 \end{vmatrix} = -1 (-8 + 20) - 3(0 - 12) +4 (0 + 6) =48$$

## 餘因子\(factor\)

> 矩陣 $$A=[a_{ij} ] \in F^{N \times N}$$
>
> * 定義$$A$$的第$$(i,j)$$項餘因子為$$cof(a_{ij} )=(−1)^{i+j}  det⁡(A_{(i|j) } )$$
> * $$A_{(i|j) }$$ 為$$A$$去掉第$$i$$列，第$$j$$行後的子矩陣。

