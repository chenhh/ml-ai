# 向量空間

線性代數討論的是有限維度的向量空間，而泛函分析才討論無限維度的向量空間。

## 向量空間\(vector space\)

令$$V$$為非空集合，$$F$$為體\(field\)，定義兩運算$$+$$與$$\cdot$$如下：

* $$+ : V \times V \rightarrow V$$為一函數，稱為向量加法（vector addition）。
* $$\cdot F \times V \rightarrow V$$為一函數，稱為純量積（scalar product）。
* 滿足$$\forall x,y \in V$$，存在唯一$$x+y \in V$$且
* $$\forall c \in F$$，存在唯一$$cx \in V$$

若向量加法與純量積滿足以下8個性質時，稱$$V$$為定義在體$$F$$上的向量空間。

1. 向量加法交換性： $$\forall x,y \in V, x+y=y+x$$
2. 向量加法結合性：$$\forall x,y,z \in V, (x+y)+z=x+(y+z)$$
3. 向量加法單位元素：$$\exists 0 \in V \ni \forall x \in V,~ x+0=0=0+x=x$$
4. 向量加法反元素：$$\forall x \in V,~  \exists −x \in V \ni x+(−x)=(−x)+x=0$$
5. 純量積對向量加法分配性：$$\forall c \in F, ~x,y \in V, ~c\cdot(x+y)=c \cdot x+c \cdot y$$
6. 純量積對純量加法分配性：$$\forall c_1, c_1 \in F, x \in V, (c_1+c_2)\cdot x=c_1 \cdot x+ c_2 \cdot x$$
7. 純量乘法對純量積結合性：$$\forall c_1, c_2 \in F, ~ x \in V, (c_1 c_2)\cdot x=c_1 \cdot (c_2 x)$$
8. 單位純量積之單位元素：$$\forall x  \in V, ~1\cdot x=x$$

### 常見性質

* $$\forall x \in V, ~ 0 \cdot v = 0$$
* $$\forall c \in F, ~ c\cdot 0 = 0$$
* $$\forall c \in F, ~ x \in V, ~ (-c)x =c(-x)=-(cx) $$
* $$\forall x, y,z \in V$$，若$$x+z=y+z$$，則$$x=y$$

## 常見向量空間

### 歐式空間\(Euclidean space\)

* $$V=\mathbb{R}^N \text{ or } \mathbb{C}^N$$
* 向量加法：$$\mathbf{x} + \mathbf{y} = (x_1 + y_2, x_2+y_2, \dots, x_N + y_N)$$。
* 純量積：$$c \mathbf{x} = (c x_1, cx_2, \dots, cx_N)$$。

| 集合$$V$$ | 體$$F$$ | 是否為向量空間 |
| :--- | :--- | :--- |
| $$\mathbb{C}^N$$ | $$\mathbb{C}$$ | 是 |
| $$\mathbb{R}^N$$ | $$\mathbb{R}$$ | 是 |
| $$\mathbb{C}^N$$ | $$\mathbb{R}$$ | 是 |
| $$\mathbb{R}^N$$ | $$\mathbb{C}$$ | 否 |

### 矩陣空間\(matrix space\)

* $$V= F^{M \times N} $$
* 向量加法：$$\mathbf{A} + \mathbf{B} = [a_{ij}]+[b_{ij}]=[a_{ij}+b_{ij}] \in F^{M \times N}$$。
* 純量積：$$c\mathbf{A}= [c\cdot a_{ij}] \in F^{M \times N}$$。

### 多項式空間\(polynomial space\)

* $$V=F[x] $$為定義在$$F$$上的多項式函數，degree可為$$n < \infty$$或$$\infty$$。
* 向量加法：函數 $$(f+g)(x) = f(x) + g(x)$$。
* 純量積：$$(c\cdot f)(x) = c \cdot f(x)$$。

### 函數空間\(function space\)

* $$V= F(X,Y)$$為定義域在集合$$X$$，值域在集合$$Y$$的函數集合。
* 向量加法與純量積同多項式空間。



