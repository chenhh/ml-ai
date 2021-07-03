# 投影算子\(projection operator\)

## 簡介

$$T^2=T$$稱為投影算子可理解為若將向量$$V$$投影到$$P$$後，再做一次相同（投影）轉換仍為向量$$P$$時，此性質與空間向量投影性質相同，如下圖。

$$T^2=T\Rightarrow T^3=T(T^2 )=T^2=T$$，由數學歸納法可得$$T^N=T, N \geq 2$$。

![&#x5411;&#x91CF;V&#x6295;&#x5F71;&#x5F8C;&#x70BA;&#x5411;&#x91CF;P](../../.gitbook/assets/projection.gif)

## 投影算子\(projection operator\)

> * 線性轉換$$T \in L(V,V)$$，若$$T^2=T$$，則稱$$T$$為$$V$$上的一個投影算子，或稱冪等算子\(idempotent operator\)。
> * 矩陣$$A \in F^{N \times N}$$，若$$A^2=A$$，則稱$$A$$為投影矩陣\(projection matrix\)或稱冪等矩陣\(idempotent matrix\)。

* 若$$T^2=T$$，則$$R(T^2 )=R(T)$$，即值域相等，但反之未必成立  。
  * 取$$A=\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$$，$$T=L_A    $$
  * $$R(T)=R(L_A )=CS(A)=span \left\{ \begin{bmatrix}  2 \\ 0\end{bmatrix} \right\}$$
  * $$R(T^2)=R(L_A^2 )=CS(A^2)=span \left\{ \begin{bmatrix}  4 \\ 0\end{bmatrix} \right\}$$

		○ ∴R\(T^2 \)=R\(T\), but T≠T^2.

	• T^2=T時，T為映成\(onto\)函數



