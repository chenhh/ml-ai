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

