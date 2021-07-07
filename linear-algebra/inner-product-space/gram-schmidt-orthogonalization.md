# Gram-schmidt正交化

Gram-schmidt正交化的功能是將一個任意集合轉換成正交集合（所有元素彼此正交）。

## 正交基底的係數\(Fourier coefficient\)

> 內積空間$$V$$定義在體$$F$$，$$S=\{v_1, \dots, v_K\} \subseteq V$$為不含$$0$$向量的正交集（線性獨立集）。
>
> 若$$v=span(S)$$，令$$v=\sum_{i=1}^K c_i v_i$$，則係數$$c_j=\frac{\langle v, v_j \rangle}{\langle v_j, v_j\rangle}=\frac{\langle v, v_j \rangle}{\|v_j\|^2}, ~j=1,2,\dots, K$$。
>
> 註：Fourier級數是此方法求各基底或生成集的係數，所以上述方法得出的參數稱Fourier coefficient。
>
> 如果$$S$$為單範正交集時，因為$$\|v_j\|=1$$，所以$$c_j=\langle v, v_j \rangle$$。

proof:

* $$\langle v, v_j\rangle=\langle \sum_{i=1}^K c_i v_i, v_j\rangle = \sum_{i=1}^K c_i \langle v_i, v_j \rangle=c_j \langle v_j, v_j  \rangle$$
* 所以$$c_j=\frac{\langle v, v_j \rangle}{\langle v_j, v_j\rangle}=\frac{\langle v, v_j \rangle}{\|v_j\|^2}$$ \(QED\)

#### 範例

$$V=\mathbb{R}^3$$，$$S=\left\{x_1=\begin{bmatrix} 1\\1\\0\end{bmatrix} ,x_2=\begin{bmatrix} -1\\1\\2\end{bmatrix},  x_3=\begin{bmatrix} -1\\1\\2\end{bmatrix}  \right\}, ~x=\begin{bmatrix} 2\\3\\4\end{bmatrix} $$

* $$\langle x_1, x_2\rangle=0$$
* $$\langle x_1, x_3\rangle=0$$
* $$\langle x_2, x_3\rangle=0$$
* $$\|x_1\|^2=2$$，$$\langle x, x_1\rangle=5$$
* $$\|x_2\|^2=2$$，$$\langle x, x_2\rangle=3$$
* $$\|x_3\|^2=6$$，$$\langle x, x_1\rangle=9$$
* 所以$$S$$為正交集
* $$x=\frac{\langle x,x_1 \rangle }{\|x_1 \|^2}  x_1+\frac{\langle x,x_2 \rangle}{\|x_2 \|^2}  x_2+\frac{\langle x,x_3 \rangle}{\|x_3 \|^2}  x_3=\frac{5}{2} x_1+\frac{3}{3} x_2+\frac{9}{6} x_3$$

### 正交集必為線性獨立集

> 內積空間$$V$$定義在體$$F$$，$$S=\{v_1, \dots, v_K\} \subseteq V$$為不含$$0$$向量的正交集，則$$S$$為線性獨立集。
>
> 反之不一定成立，如$$S=\left\{ \begin{bmatrix} 1\\0\end{bmatrix}, \begin{bmatrix} 1\\1\end{bmatrix} \right\}$$在標準內積為線性獨立集，但不是正交集。

proof:

* 令$$c_1v_1 + \dots + c_K v_K=0$$
* 因為$$S$$為正交集，所以$$c_j=\frac{\langle0, v_j \rangle}{\langle v_j, v_j\rangle}=0~j=1,2,\dots, K$$
* 因此$$S$$為線性獨立集 \(QED\)

## Gram-Schmidt正交化過程

> 內積空間$$V$$定義在體$$F$$，$$S=\{v_1, \dots, v_K\} \subseteq V$$為線性獨立集。
>
> * 令$$u_1 = v_1$$
> * $$u_j = v_j - \sum_{j=1}^K \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j, ~ 2 \leq j \leq K$$
>
> 則$$\{u_1, u_2, \dots, u_K\}$$為不含0的正交集，且$$span\{u_1, u_2, \dots, u_K\}=span\{v_1, v_2, \dots, v_K\}$$。
>
> $$\{\frac{u_1}{\|u_1\|}, \frac{u_2}{\|u_2\|}, \dots, \frac{u_K}{\|u_K\|}\}$$為單範正交集。

如果$$S$$是線性相依集，則可前處理將$$S$$中線性相依的元素刪除至只剩線性獨立的元素。

### 範例：歐式空間

* $$H=span \left\{    x_1 = \begin{bmatrix} 1 \\ 0 \\1 \\ 0\end{bmatrix} , x_2 = \begin{bmatrix} 2 \\ 1 \\2 \\ 1\end{bmatrix}, x_3 = \begin{bmatrix} -1 \\ 2 \\-3 \\ 4\end{bmatrix}  \right\}$$
* $$u_1 = x_1= \begin{bmatrix} 1 \\ 0 \\1 \\ 0\end{bmatrix}$$
* $$u_2=x_2 - \frac{\langle x_2, u_1 \rangle}{\langle u_1, u_1 \rangle}u_1=\begin{bmatrix} 0 \\ 1 \\0 \\ 1\end{bmatrix}$$
* $$u_3 = x_3 -   \frac{\langle x_3, u_1 \rangle}{\langle u_1, u_1 \rangle}u_1 - \frac{\langle x_2, u_2 \rangle}{\langle u_2, u_2 \rangle}u_2 = \begin{bmatrix} 1 \\ -1 \\-1 \\ 1\end{bmatrix}$$
* $$\langle u_1, u_2 \rangle =\langle u_1, u_3 \rangle = \langle u_2, u_3 \rangle = 0$$

### 範例：連續函數空間

$$V=C[0,1]$$，$$F=\mathbb{R}$$，$$\langle f,g \rangle= \int_0^1f(x)g(x)dx$$

* $$S=span\{1,x^2, x^3\}$$
* $$u_1(x)=1$$，$$\langle u_1, u_1\rangle=1$$
* $$u_2(x)=x -\frac{\langle x_2, u_1 \rangle}{\langle u_1, u_1 \rangle}u_1 = x - \int_0^1 x dx=x - \frac{1}{2}$$
  * $$\langle u_2, u_2 \rangle=\int_0^1 (x- \frac{1}{2})^2dx=\frac{1}{12}$$
* $$u_3 = x_3 - \frac{\langle x_3, u_1 \rangle}{\langle u_1, u_1 \rangle}u_1 - \frac{\langle x_2, u_2 \rangle}{\langle u_2, u_2 \rangle}u_2 =x^2 - \int_0^1 x^2 dx -12\int_0^1x^2(x-\frac{1}{2})dx (x-\frac{1}{2})=x^2 -x +\frac{1}{6}$$

  * $$\langle u_3, u_3 \rangle=\int_0^1 (x^2- x+ \frac{1}{6})^2dx=\frac{1}{180}$$

  可得$$\{1, \sqrt{12}(x-\frac{1}{2}), \sqrt{180}(x_2 -x + \frac{1}{6}\}$$為單範正交基底。

