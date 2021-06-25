# 行列式\(determinant\)

## 高階行列式

> $$A=[a_{ij }] \in F^{N \times N}$$，則$$A$$的行列式$$det(A)$$可遞迴定義成
>
> * $$N=1,det⁡(A)=a_{11}$$
> * $$N \geq 2$$, $$\det(A) = \sum_{j=1}^N (-1)^{1+j} a_{1j} \det(A_{(1|j)})$$
> * $$A_{(1|j) }$$ 為A中去掉第1列\(row\)，第$$j$$行的$$(N-1) \times (N-1)$$子矩陣
>
> 可以從矩陣的任一列或行展開，只要該列或行中有越多的0，則計算量越少。
>
> 方陣才可以計算行列式。

$$A=\begin{bmatrix} 0 &1  &3 \\ -2 &-3 &  -5\\ 4 & -4& 4\end{bmatrix}$$

從第一列展開，得$$\det(A)= 0 \begin{vmatrix} -3 & -5 \\ -4 & 4  \end{vmatrix} - 1 \begin{vmatrix} -2 & -5 \\ 4 & 4  \end{vmatrix} +3 \begin{vmatrix} -2 & -3 \\ 4 & -4  \end{vmatrix}  =-1 \cdot (-8 + 20) + 3\cdot (8 + 12) =  48$$

從第二行展開，得

$$\det(A)= -1 \begin{vmatrix} -2 & -5 \\ 4 & 4 \end{vmatrix} -3 \begin{vmatrix} 0 & 3 \\ 4 & 4 \end{vmatrix} + 4 \begin{vmatrix} 0 & 3 \\ -2 & -5 \end{vmatrix} = -1 (-8 + 20) - 3(0 - 12) +4 (0 + 6) =48$$

## 餘因子\(factor\)

> 矩陣 $$A=[a_{ij} ] \in F^{N \times N}$$
>
> * 定義$$A$$的第$$(i,j)$$項餘因子為$$cof(a_{ij} )=(−1)^{i+j}  \det⁡(A_{(i|j) } )$$
> * $$A_{(i|j) }$$ 為$$A$$去掉第$$i$$列，第$$j$$行後的子矩陣。

## 行列式的性質

* $$\det⁡(r_{ij} (A))=−\det⁡(A)$$ \(矩陣第$$i,j$$列互換時，行列式為負值\)
* $$\det(r_i^{(k) } (A))=k \cdot \det⁡(A)$$  \(第$$i$$列乘以$$k \neq 0$$時，行列式變為$$k$$倍\)
* $$\det⁡(r_{ij}^{(k) } (A))=\det⁡(A)$$  \(第$$i$$列乘以$$k$$倍加至第$$j$$列時，行列式不變\)
* $$\det⁡(c_{ij} (A))=−\det⁡(A)$$ \(矩陣第$$i,j$$行互換時，行列式為負值\)
* $$\det⁡(c_i^{(k)} (A))=k\cdot \det⁡(A)$$  \(第$$i$$行乘以$$k \neq 0$$時，行列式變為$$k$$倍\)
* $$\det⁡(c_{ij}^{(k)} (A))=\det⁡(A)$$  \(第$$i$$行乘以$$k$$倍加至第$$j$$行時，行列式不變\)
* $$\det(AB) = \det(A)\det(B)$$ \(**方矩陣相乘的行列式等於個別矩陣行列式的乘法**\)
  * $$\det(A^2) = \det(AA)= (\det(A))^2$$
* 若$$A$$為可逆矩陣，則$$\det(AA^{-1})=\det(A)\det(A^{-1})=\det(I_N)=1$$，因此$$\det(A^{-1})=\frac{1}{\det(A)}$$。

## 轉置矩陣的行列式與原矩陣相同

> 矩陣 $$A=[a_{ij} ] \in F^{N \times N}$$，則$$\det(A) = \det(A^\top)$$

proof:

* 不失一般性，令行列式由第一列展開，則$$\displaystyle \det(A) = \sum_{j=1}^N (-1)^{1+j} a_{1j} \det(A_{(1|j)})$$
* 因為$$A^\top = [a_{ij}]^\top=[a_{ji}]$$，因此如果將$$A^\top$$的行列式由第一行展開時，得到的行列式會與$$A$$從第一列展開時相同 \(QED\)

## 行列式不為0為可逆矩陣的充要條件

> $$A=[a_{ij} ] \in F^{N \times N}$$，
>
> *  若$$A$$中任二行或是任二列相同時或$$rank(A)<N$$，則$$\det(A)=0$$。
> * $$A$$為可逆矩陣$$\Leftrightarrow$$ $$rank(A)=N \Leftrightarrow \det⁡(A) \neq 0$$
> * 若$$A$$為可逆矩陣，則$$\det(AA^{-1})=\det(A)\det(A^{-1})=\det(I_N)=1$$，因此$$\det(A^{-1})=\frac{1}{\det(A)}$$。

proof:

* 若$$A$$為可逆矩陣，則$$A$$經若干個基本列運算後，可得$$I_N$$
  * 即$$A$$可拆解成列基本矩陣的乘法，$$A=E_1 E_2\ldots E_K$$
  * $$\det⁡(A)=\det⁡(E_1 )\ldots \det⁡(E_K )$$
  * $$\because \det⁡(E_i ) \neq 0, ~\therefore \det⁡(A) \neq 0$$ \(QED\)
* 若$$A$$為不可逆矩陣，假設$$A$$經$$K$$次列運算後可得矩陣$$R$$

  * $$E_1 E_2 \ldots E_K A=R,  ~ rank(A)<N$$
  * $$R$$至少包含一個零列，即$$\det⁡(R)=0$$
  * $$ \therefore 0=\det⁡(R)=\det⁡(E_1 )  \det⁡(E_2 ) \ldots \det⁡(E_K )  \det⁡(A)$$
  * $$\because \det⁡(E_i ) \neq 0~ \therefore \det⁡(A)=0$$ \(QED\)





## 矩陣元素的行列式

> 矩陣$$A,B,C \in F^{M \times N}$$，則
>
> * $$\det \begin{bmatrix} A  &B \\ C & D\end{bmatrix}$$不一定等於$$\det(AD - BC)$$或$$\det(A)\det(D) - \det(C)\det(B)$$。
> * $$\det \begin{bmatrix} A  &B \\ 0 & D\end{bmatrix} = \det(A)\det(B)$$
> * $$\det \begin{bmatrix} A  &B \\ B & A\end{bmatrix} = \det(A+B)\det(A-B)$$

## Vandermonde矩陣

$$\displaystyle \det \begin{bmatrix}   1 & 1 &\dots & 1 \\ x_1 & x_2 & \dots &x_n \\  x_1^2 & x_2^2 & \dots  & x_n^2 \\    \vdots & \vdots & \vdots & \vdots \\  x_1^{n-1} & x_2^{n-1} & \dots & x_n^{n-1}   \end{bmatrix} = \prod_{1 \leq  i < j \leq n} (x_j - x_i)$$

例如：$$\begin{bmatrix} 1 & 1 & 1\\  a & b& c \\ a^2 & b^2 & c^2  \end{bmatrix} = (b-a) (c-a)(c-b)$$

