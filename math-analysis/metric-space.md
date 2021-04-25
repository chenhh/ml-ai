# 度量空間 \(metric space\)

## 距離函數與度量空間

> definition: distance function
>
> $$X$$為一集合，如果存在一實值函數 $$d(\cdot, \cdot): X \times X \rightarrow \mathbb{R}$$滿足 $$\forall x, y, z \in X$$
>
> 1. \[兩點間距離為正值\]$$d(x,y) \geq 0$$ and $$ d(x,y) = 0 \Leftrightarrow  x = y$$
> 2. \[對稱性\] $$d(x,y) = d(y,x)$$
> 3. \[三角不等式\] $$d(x,y) +d(y,z) \geq d(x, z)$$



> definition: metric space
>
> $$(X, d)$$稱為度量空間，也稱賦距空間，函數$$d$$為X上的一個度量\(距離\)函數。

## 常見度量空間

### Euclidean space

$$X=\mathbb{R}^n$$, $$d(x,y) = \| x - y\|_2$$

$$ X = \mathbb{R}^n$$, $$d(x,y)=\| x - y\|_1 = |x_1 -y_1 | + |x_2 -y_2| + \ldots +|x_n -y_n|$$

$$X = \mathbb{R}^n$$, $$d(x,y)=\| x- y\|_{\infty} =\max \{ |x_1-y_1|, |x_2 - y_2| , \ldots, |x_n - y_n| \}$$

### complex space

$$X = \mathbb{C}$$, $$d(z_1, z_2) = |z_1 - z_2|$$

### discrete space

$$X$$為任意非空集合, $$d(x,y) =   \{ \begin{align}  0, & \ \text { if } x = y \\ 1, &   \text{ if } x \neq y \\ \end{align}$$

### sub-metric space

$$(X, d)$$ is metric space, and $$ S \subset X$$, then $$ (S, d)$$is metric space.

e.g. rational number set $$\mathbb{Q}$$ and $$d(x,y) = |x -y|$$

### continuous function

$$X=C[a,b]$$為定義在實數區間$$[a,b]$$所有的連續實數值函數, $$d(f,g)=\sup\{ |g(t) - f(t)\ \vert | a \leq t \leq b\}$$，兩函數的距離為兩函數值在區間$$[a,b]$$的最大差值。

### continuous function with quadratic metric

$$X=C[a,b]$$, $$d(f,g)=( \int_a^b (f(t) - g(t))^2 dt)^{\frac{1}{2}}$$

### l2-metric

$$X=(x_1, x_2, \ldots, x_n, \ldots)$$be sequence of real numbers and $$\sum_{i=1}^\infty (x_i)^2 < \infty $$, $$d(x,y) =(\sum_{i=1}^\infty (x_i - y_i)^2)^{\frac{1}{2}}$$

### bounded sequence

$$X=(x_1, x_2, \ldots, x_n, \ldots)$$be sequence of real numbers and $$x_i< \infty \forall i$$, $$d(x,y)= \sup{ |x_i -y_i|} \ \forall i$$















