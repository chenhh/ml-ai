# 克羅內克乘積\(Kronecker product\)

## Kronecker product

Kronecker product是兩個任意大小的矩陣間的運算。

給定$$A \in \mathbb{R}^{m \times n}, B \in \mathbb{R}^{p \times q}$$，則	克羅內克乘積$$A \otimes B=\begin{bmatrix}  a_{11} B & \dots & a_{1n} B \\ \vdots & \ddots & \vdots \\ a_{m1}B & \dots & a_{mn}B \end{bmatrix} \in \mathbb{R}^{mp \times nq}$$

展開得：

$$A \otimes B = \begin{bmatrix}   a_{11}b_{11} & \dots & a_{11}b_{1q} & \dots & a_{1n}b_{11} & \dots & a_{1n} b_{1q} \\ \vdots & \ddots & \vdots & \ddots &\vdots & \ddots & \vdots \\ a_{11} b_{p1} & \vdots & a_{11}b_{pq} & \dots & a_{1n}b_{p1} & \dots & a_{1n} b_{pq}   \\ \vdots & \ddots & \vdots & \ddots &\vdots & \ddots & \vdots \\ a_{m1}b_{11} & \dots & a_{m1}b_{1q} & \dots & a_{mn}b_{11} & \dots & a_{mn} b_{1q} \\ \vdots & \ddots & \vdots & \ddots &\vdots & \ddots & \vdots \\ a_{m1} b_{p1} & \vdots & a_{m1}b_{pq} & \dots & a_{mn}b_{p1} & \dots & a_{mn} b_{pq}   \\  \end{bmatrix}$$

```python
import numpy as np 
A=np.array([[1,2],[3,4]]) 
B= np.array([[2],[3]) 
print (np.kron(A,B)) 

array([
	[ 2, 4], 
	[ 3, 6], 
	[ 6, 8], 
[ 9, 12]])
```

## 參考資料

Charles F. Van Loan, "[The ubiquitous Kronecker product,](https://doi.org/10.1016/S0377-0427%2800%2900393-9)", Journal of Computational and Applied Mathematics, Vol. 123, pp. 85-100, 2000.

