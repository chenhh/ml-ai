# Gram-schmidt正交化

Gram-schmidt正交化的功能是將一個任意集合轉換成正交集合（所有元素彼此正交）。

$$QR$$分解可將矩陣$$A$$的行向量經Gram-Schmidt正交化過程變為正交行向量形成的矩陣$$Q$$，以及相對應的參數矩陣$$R$$。

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
> * $$u_j = v_j - \sum_{j=1}^K \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j, ~ 2 \leq j \leq K$$ （新的正交向量是由原始向量減去投影在其它正交向量的成份後得出）
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

## QR分解

> 矩陣$$A \in F^{M \times N}$$且$$rank(A)=k$$，
>
> 則$$A$$可分解為$$A=Q_0R_0$$\(unnormalized\)。
>
> * $$Q_0 \in F^{M \times N}$$ 行\(column\)向量形成正交集，具$$k$$個非零行，$$N-k$$個零行。
> * $$R_0 \in F^{N \times N}$$ 為上三角矩陣，且對角線元素均為1。
>
> $$A$$可分解為$$A=QR$$\(normalized\)
>
> * $$Q \in F^{M\times K}$$ 為行向量形成單範正交集（因為$$rank(A)=k$$，即只有$$k$$行為線性獨立集。）
> * $$R \in F^{K \times N}$$ 為上三角矩陣。

Proof:

* 令$$A=\begin{bmatrix} v_1  & v_2 & v_N \end{bmatrix}\in F^{M \times N}$$
* 因為$$rank(A)=k$$，不失一般性令$$\{v_1,v_2,\dots,v_k \}$$為線性獨立集且  $$v_j \in span\{v_1,\dots,v_k \},~ j=k+1,\dots,N$$\(即前k行為線性獨立集，第k+1至N行為線性相依集\)
* 利用Gram-Schmidt正交化過程對所有行向量$$v_1,\dots,v_N$$ 正交化得$$u_1,\dots,u_N$$  。
* $$u_j=v_j−a_{1j} u_1−a_{2j} u_2−\dots−a_{(j−1)j }u_{(j−1)}, ~j=1,2,⋯,k $$ 
* $$u_j=v_j−a_{1j} u_1−a_{2j} u_2−\dots−a_{kj} u_k, ~ j=k+1,\dots,N $$
* $$a_{ij}=\frac{\langle v_j,u_i \rangle}{ \langle u_i,u_i \rangle} ,~i=1,2,\dots,j−1,~ j=1,2,\dots,k $$。
* $$a_{ij}=0,~ i=1,2,\dots,j−1,~ j=k+1,\dots,N $$
* 注意$$u_{k+1}=u_{k+2}=\dots=u_N=0$$
* 所以$$v_j=a_{1j} u_1+a_{2j} u_2+\dots+a_{j−1}j u_{j−1}+u_j, ~j=1,2,\dots,k  $$
* $$v_j=a_{1j} u_1+a_{2j} u_2+\dots+a_{kj} u_k+u_j, ~j=k+1,\dots,N$$
* $$A=\begin{bmatrix} u_1 & u_2  & \dots &u_N\end{bmatrix} \begin{bmatrix} 1& a_{12}  & a_{13} & \dots &a_{1N} \\ 0& 1& a_{23}  &  \dots &a_{2N} \\ 0 & 0 & 1 & \dots & a_{3N} \\ \vdots & \vdots &\vdots &\ddots &\vdots \\   0 & 0 & 0 &\dots & 1 \end{bmatrix}  =Q_0R_0$$
* 因為$$u_{k+1}=u_{k+2}=\dots=u_N=0$$
* $$A=\begin{bmatrix} u_1 & u_2  & \dots &u_k\end{bmatrix} \begin{bmatrix} 1& a_{12}  & a_{13} & \dots & a_{1_k} & \dots  &a_{1N} \\ 0& 1& a_{23}  &  \dots & a_{2_k} & \dots &a_{2N} \\ 0 & 0 & 1 & \dots& a_{3_k} & \dots & a_{3N} \\ \vdots & \vdots &\vdots &\ddots &\vdots&\ddots &\vdots \\   0 & 0 & 0 & \dots & 1 &\dots & a_{k_N} \end{bmatrix} \\ = \begin{bmatrix} \frac{u_1}{\|u_1\|} & \frac{u_2}{\|u_2\|}  & \dots &   \frac{u_K}{\|u_K\|} \end{bmatrix} \\ \begin{bmatrix} \|u_1\|& a_{12}\|u_1\|  & a_{13}\|u_1\| & \dots & a_{1_k}\|u_1\| & \dots  &a_{1N}\|u_1\| \\ 0 & \| u_2\|& a_{23}\|u_2\|  &  \dots & a_{2_k} \| u_2\| & \dots &a_{2N}\| u_2\| \\ 0 & 0 & \|u_3\| & \dots& a_{3_k}\|u_3\| & \dots & a_{3N}\|u_3\| \\ \vdots & \vdots &\vdots &\ddots &\vdots&\ddots &\vdots \\   0 & 0 & 0 & \dots & \|u_K\| &\dots & a_{KN}\| u_K\| \end{bmatrix}  $$\(QED\)

#### 範例

$$A=\begin{bmatrix}  1& 3 & 5\\ 1 & 1 & 0 \\1 & 1& 2 \\ 1 & 3 & 3\end{bmatrix} = \begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix}$$

* $$u_1=v_1 =\begin{bmatrix}  1\\1 \\1\\ 1 \end{bmatrix}$$，$$\langle u_1, u_1\rangle=4$$
* $$u_2 = v_2 - \frac{\langle v_2, u_1\rangle}{\langle u_1, u_1\rangle} u_1=\begin{bmatrix}  1\\-1 \\-1\\ 1 \end{bmatrix}$$，$$\langle u_2, u_2\rangle=4$$
* $$u_3=v_3 -\frac{\langle v_3, u_1\rangle}{\langle u_1, u_1\rangle} u_1 - \frac{\langle v_3, u_2\rangle}{\langle u_2, u_2\rangle} u_2 =\begin{bmatrix}  1\\-1 \\1\\ -1 \end{bmatrix}$$，$$\langle u_3, u_3\rangle=4$$
* $$\left\{ \begin{align} u_1 &= v_1 \\ u_2 & =v_2 - 2u_1 \\ u_3 & = v_3 - \frac{5}{2} u_1 -\frac{3}{2}u_2 \end{align}   \right.$$
* 移項得$$\left\{ \begin{align} v_1 &= u_1 \\ v_2 & =2u_1 + u_2\\ v_3 & =  \frac{5}{2} u_1 +\frac{3}{2}u_2  +u_3\end{align}   \right.$$
* 所以$$A=\begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix} = \begin{bmatrix} u_1 & u_2 & u_3 \end{bmatrix}\begin{bmatrix} 1 & 2 & \frac{5}{2} \\ 0 & 1 &  \frac{3}{2} \\0 & 0 & 1\end{bmatrix} = \begin{bmatrix} \frac{u_1}{\|u_1\|} & \frac{u_2}{\|u_2\|} & \frac{u_3}{\| u_3\|} \end{bmatrix}\begin{bmatrix} \|u_1\| & 2 \|u_1\| & \frac{5}{2} \|u_1\| \\ 0 & \|u_2\| &  \frac{3}{2} \|u_2\|\\0 & 0 & \|u_3\|\end{bmatrix} = \begin{bmatrix} \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} &  -\frac{1}{2} \\\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \end{bmatrix}  \begin{bmatrix} 2 & 4 & 5 \\ 0 & 2 & 3\\ 0 & 0 & 2 \end{bmatrix} =QR$$

