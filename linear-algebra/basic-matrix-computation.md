# 矩陣基本計算

## 矩陣基本計算

## 矩陣\(matrix\)

> $$A=[a_{ij}]\in F^{M \times N}, F \text{ is field}$$

* 當$$F = \mathbb{R}$$時為實數矩陣\(real matrix\)
* 當$$F=\mathbb{C}$$時為複數矩陣\(complex matrix\)

### 矩陣相等

> $$A=B\in F^{M\times N} \Leftrightarrow A=[a_{ij}]\in F^{M \times N}, B=[b_{ij}]\in F^{M \times N}, a_{ij} = b_{ij}, \forall i, j$$

兩個矩陣相等，即矩陣的尺寸必須相同，且兩個矩陣內對應位址的元素完全相等時才成立。

### 矩陣加減法

> $$A=[a_{ij}], B=[b_{ij}], C=[c_{ij}]\in F^{M \times N}$$.
>
> $$C = A \pm B \Leftrightarrow c_{ij} = a_{ij} \pm b_{ij}, \forall i, j$$.

兩個矩陣尺寸必須相等才能進加減法計算。而矩陣加減法是兩矩陣對應位址的元素相加減。

### 矩陣純量積

> $$A=[a_{ij}], C=[c_{ij}]\in F^{M \times N}, \alpha \in F$$.
>
> $$C=\alpha A \Leftrightarrow c_{ij} = \alpha a_{ij}, \forall i, j$$.

純量對於矩陣的乘法，會作用在矩陣的所有元素上。

### 矩陣乘法

> $$A=[a_{ij}] \in F^{M \times N}, B=[b_{ij}] \in F^{N \times P}, C=[c_{ij}]\in F^{M \times P}$$.
>
> $$C = AB \Leftrightarrow c_{ij} = \sum_{k=1}^N a_{ik}b_{kj}, \forall i,j$$.

## 矩陣計算性質

$$A,B, C\in F^{M\times N}, a,b\in F $$ 可得

* $$A+B = B+A$$
* $$(A+B)+C = (A+B)+C$$
* $$ A+O = A = O+A$$
* $$A+(-A) = O = (-A) + A$$
* $$(a+b)A = aA+ bA$$
* $$(ab)A = a(bA)$$
* $$a(A+B) = aA + aB$$
* $$(-1)A = -A$$
* $$0A = O$$
* $$aO = O$$

矩陣大小不同時

* $$(AB)C = A(BC), \ A\in F^{M\times N}, B\in F^{N\times P}, C\in F^{P \times Q}$$
* $$A(B \pm C) = AB \pm AC, \ A\in F^{M\times N}, B, C\in F^{N\times P}$$
* $$ (A \pm B) C = AC \pm BC,\ A,B \in F^{M \times N}, C \in F^{N\times P}$$
* $$ A I_N=A, A\in F^{M\times N} $$
* $$I_M A = A,\ A \in F^{M\times N}$$
* $$a(AB)=(aA)B=A(aB), \ A\in F^{M \times N}, B \in F^{N \times P}, a \in F$$

### 注意

* $$AB$$不保證等於 $$BA$$
* $$A^n =0$$不保證 $$A=0$$。如$$ A=\begin{bmatrix} 0 & 0 \\ 0 & 1  \end{bmatrix}$$
* $$A^2 = A$$不保證 $$A=I$$。如 $$A=\begin{bmatrix} 1 & 0 \\ 0 & 0  \end{bmatrix}$$
* $$A \neq O$$且 $$B \neq O$$不保證 $$AB \neq O$$。如$$ A= \begin{bmatrix} 0 & 0 \\ 1 & 0  \end{bmatrix}, B=\begin{bmatrix} 0 & 0 \\ 2 & 0  \end{bmatrix}, AB=O$$
* $$AB=AC$$且 $$A \neq O$$不保證 $$B=C$$，即不具消去性。如 $$A=\begin{bmatrix} 1 & 0 \\ 2 & 0  \end{bmatrix}, B=\begin{bmatrix} 1 & 2 \\ 0 & 0  \end{bmatrix}, C=\begin{bmatrix} 1 & 2 \\ 1 & 1  \end{bmatrix}$$
* $$(A+B)^2 = A^2 + 2AB + B^2$$只在  $$AB=BA$$時成立。

## 轉置\(transpose\)、共軛轉置\(conjugate transpose\)矩陣

> * $$A = [a_{ij}]\in F^{M\times N}$$
> * transpose $$A^{\top} = [b_{ij}] \in F^{N \times N}, b_{ij} = a_{ji}, \ \forall i, j$$
> * conjugate transpose $$ A^{\mathrm {H}} = [b_{ij}] \in F^{N \times M}, b_{ij} = \overline{a_{ji}}, \forall i, j$$

可得 $$A^{\mathrm{H}} = \overline{A}^{\top} = \overline{A^{\top}}$$

性質：

* $$(aA \pm bB)^{\top} = aA^{\top} \pm bB^{\top}$$
* $$(A^{\top})^{\top} = A$$
* $$ (AB)^{\top} = B^{\top} A^{\top}$$
* $$(aA \pm bB)^{\mathrm{H}} = aA^{\mathrm{H}} \pm bB^{\mathrm{H}}$$
* $$(A^{\mathrm{H}})^{\mathrm{H}} = A$$
* $$ (AB)^{\mathrm{H}} = B^{\mathrm{H}} A^{\mathrm{H}}$$



