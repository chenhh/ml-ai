# 雙線性型式(bilinear form)

## 雙線性(函數)型式

> $$V$$為定義在體$$F$$的向量空間，函數$$f: V \times V \rightarrow F$$滿足$$\forall x,y,z \in V, a,b \in F$$：
>
> * $$f(ax+by,z)=af(x,z)+bf(y,z)$$
> * $$f(x,ay+bz)=af(x,y)+b(x,z)$$
>
> 則稱$$f$$為$$V$$上的雙線性函數。令$$B(V)$$為$$V$$上所有雙線性函數所形成的集合。
>
> 此為雙變數函數$$f(x,y)$$的線性算子形式。

* 例如$$A\in F^{N \times N}, V=F^{N \times 1}$$，定義$$f(x,y)=y^{\top}Ax$$或$$f(x,y)=x^{\top}Ax \in B(V), \forall x, y \in V$$

### 雙線性函數形成向量空間

> 雙線性函數$$f \in B(V)$$，則$$f(x, 0)=(0,x)=0, \forall x \in V$$。
>
> 定義$$B(V)$$上的加法與純量積為：
>
> * $$\forall f_1, f_2 \in B(V), (f_1+f_2)(x,y)=f_1(x,y)+f_2(x,y)$$
> * $$\forall f \in B(V), c \in F, ~(cf)(x,y) = cf(x,y)$$
>
> 則$$B(V)$$滿足向量空間的定義（包含0向量與任意線性組合的所有元素）。

### Sesqui型式

> $$V$$為定義在體$$F$$的向量空間，函數$$f: V \times V \rightarrow F$$滿足$$\forall x,y,z \in V, a,b \in F$$：
>
> * $$f(ax+by, z)=af(x,z)+bf(y,z)$$
> * $$f(x, ay+bz)=\overline{a}f(x,y)+\overline{b}f(x,z)$$
>
> 則稱$$f$$為$$V$$上的sesqui型式，或是簡稱為型式。> 令$$F(V)$$為$$V$$上所有sesqui型式函數所成的集合。>

> 同雙線性型式定義加法與純量積，則$$F(V)$$也為向量空間（包含0向量與任意線性組合的所有元素）。>

* 當$$F=\mathbb{R}$$時，雙線性型式等於Sesqui型式。
*   當$$F = \mathbb{C}$$時，$$B(V) \cap F(V) = \{0\}$$

    * 若$$f \in B(V) \cap F(V)$$
    * 則$$f(x,y)=f(x, i(−i)y)=i(x,(−i)y)$$\[因為$$f \in β(V)]=i^2 f(x,y)$$\[因為$$f \in F(V)]=−f(x,y)$$
    * 可得$$f(x,y)=−f(x,y)$$，所以$$f(x,y)=0,  \forall x,y \in V$$。



#### 範例

*   &#x20;$$A \in \mathbb{C}^{N \times N}, V=\mathbb{C}^{N \times 1}$$，定義$$f:V \times V \rightarrow F$$，$$f(x,y)=y^\mathrm{H} Ax,~ \forall x,y \in V$$，則$$f(x,y) \in F(V)$$。

    * $$\forall a,b \in F, x,y \in V$$
    * $$f(ax+by,z)=z^\mathrm{H} A(ax+by)=az^\mathrm{H} Ax+bz^\mathrm{H} Ay=af(x,z)+bf(y,z)$$
    * $$f(x,ay+bz)=(ay+bz)^\mathrm{H} Ax＝（\overline{a}y^\mathrm{H}+\overline{b}z^\mathrm{H} ）Ax=\overline{a}y^\mathrm{H} Ax+\overline{b}z^\mathrm{H} Ax=\overline{a} f(x,y)+ \overline{b} f(x,z)$$
    * 所以$$f \in F(V)$$



### Sesqui型式函數與線性轉換的對應關係

> $$V$$為定義在體$$F$$的內積空間，$$f \in F(V)$$為Sesqui型式，則唯一存在線性轉換$$T \in L(V,V)$$使得$$f(x,y)=\langle T(x), y \rangle~ \forall x,y \in V$$

Proof:

* $$\forall v \in V$$，定義$$g(u)=f(u,v), ~\forall u \in V$$，則$$g$$為線性函數。
* 因此得唯一存在$$v^′ \in V \ni g(u)=\langle u,v^′\rangle, ~\forall u \in V$$
*  定義 $$U:V \rightarrow V, ~U(v)=v^{′}$$
* 所以$$f(u, av_1+bv_2 )=\langle u, U(av_1+bv_2 ) \rangle, ~\forall a,b \in F, u,v_1,v_2 \in V$$
* 而且 $$f(u, av_1+bv_2 )=\overline{a} f(u,v_1 )+\overline{b} f(u,v_2 )=\overline{a} \langle u, U(v_1) \rangle +\overline{b} \langle u,U(v_2) \rangle= \langle u, aU(v_1 )+bU(v_2 ) \rangle$$
* 所以$$\langle u, U(av_1+bv_2 )\rangle=\langle u, aU(v_1 )+bU(v_2 )\rangle$$
* 可得$$U(av_1+bv_2 )=aU(v_1 )+bU(v_2 )$$，因此$$U$$為線性。
* 取$$T=U^{*}$$ ($$U$$的伴隨算子)，則$$f(u,v)=\langle u, U(v) \rangle=\langle U^{*} (u),v \rangle=\langle T(u),v \rangle, \forall u,v \in V$$，因此$$T$$存在。
* &#x20;唯一性
* 若存在$$T^{′} \in L(V,V)\ni f(u,v)=\langle T^{'} (u),v\rangle, \forall u,v \in V$$
* 可得$$\langle T(u),v \rangle= \langle T^{′}(u),v \rangle, ~\forall u,v \in V$$
* 所以$$\langle T(u)−T^{′} (u),v \rangle=0$$
* 因此$$T(u)−T^{′} (u)=0$$
* 所以$$T(u)=T^{′} (u), ~\forall u\in V$$
* 即$$T=T^{′}$$，所以$$T$$唯一。 (QED)

### 雙線性(函數)形式矩陣表示法

> 雙線性函數$$f\in B(V)$$或Sesqui型式函數$$f \in F(V)$$。
>
> 令向量空間$$V$$的有序基底$$B=\{b_1, b_2, \dots, b_N\}$$。
>
> 定義$$A \in F^{N \times N}$$，$$[A]_{ij} = f(b_j, b_i) \equiv \psi_B(f)$$為矩陣$$A$$為$$f$$相對於基底$$B$$的矩陣表示法。
>
> 也可定義$$[A]_{ij}=f(b_i,b_j )$$，此時矩陣與上述定義互為轉置。

#### 範例

* 函數$$f: \mathbb{R}^2 \times \mathbb{R}^2 \rightarrow \mathbb{R}$$，$$f \in B(V)$$為雙線性，$$f\left(  \begin{bmatrix} x_1 \\ y_1 \end{bmatrix}, \begin{bmatrix} x_2 \\ y_2 \end{bmatrix}   \right)=2x_1 y_1 + 3 x_1 y_2 + 4 x_2 y_1 - x_2 y_2$$。
* 取基底$$B=\left\{ b_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, b_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix} \right\}$$
* $$A=\psi_B(f) = \begin{bmatrix}  f(b_1, b_1) & f(b_2, b_1) \\ f(b_1, b_2) & f(b_2, b_2) \end{bmatrix} = \begin{bmatrix}  8 & 2 \\ 4 & -6 \end{bmatrix}$$
* 若取標準基底$$R=\{e_1, e_2\}$$
* $$B=\psi_R(f)=\begin{bmatrix}  f(e_1, e_1) & f(e_2, e_1) \\ f(e_1, e_2) & f(e_2, e_2)  \end{bmatrix} = \begin{bmatrix}  2 & 4 \\ 3 & -1 \end{bmatrix}$$

### 雙線性函數與矩陣空間同構

> $$V$$為定義在體$$F$$上的向量空間，$$\dim(V)=N$$，則雙線性函數$$B(V)$$與矩陣$$F^{N \times N}$$同構，且$$\dim(B(V))=N^2$$。
>
> 同理可得Sesqui型式$$F(V)$$與$$F^{N \times N}$$同構。

與Proof:

* 令$$B=\{b_1, \dots, b_N\}$$為$$V$$的一組基底
* 定義函數$$\phi:B(V) \rightarrow F^{N \times N}, ~ \phi(f)=\psi_B (f), \forall f\in B(V)$$
* 欲證明$$\phi$$為線性同構函數(線性、一對一、映成)
* (1) 線性
* $$\forall f,g \in B(V),~ a,b \in F$$
* $$(af+bg)(b_j,b_i )=af(b_j,b_i )+bg(b_j,b_i ), ~\forall i,j=1,2,\dots,N$$
* 可得$$(\psi_β (af+bg))_{ij}=a(\psi_B (f))_{ij}+b(\psi_B (g))_{ij}, ~\forall i,j=1,2,\dots,N$$
* $$\psi_B (af+bg)=a(\psi_B (f))+b(\psi_B (g))$$
* $$\phi(af+bg)=\psi_B (af+bg)=a(\psi_B (f))+b(\psi_B (g))=a\phi(f)+b\phi(g)$$
* 所以$$\phi$$為線性函數
* (2) 一對一函數 (只需證明$$ker⁡(\phi)=\{0\}$$)
* $$\forall f \in ker⁡(\phi) \Rightarrow \phi(f)=\psi_B (f)=0$$
* 固定$$b_i \in B$$,定義$$l_(b_i ):V→F$$, $$l_{b_i} (y)=f(b_i,y), ~\forall y \in V$$
* 所以$$l_{b_i} (b_j )=f(b_i,b_j )=0, \forall b_j \in B$$
* 可得 $$l_{b_i} (y)=0, ~\forall y \in V$$
* $$f(b_i,y)=l_{b_i} (y)=0, ~\forall y \in V, b_i \in B$$&#x20;
* $$\forall y \in V$$，定義$$r_y:V \rightarrow F, r_y (x)=f(x,y), ~\forall x \in V$$
* 因為$$r_y (b_i )=f(b_i,y)=0,  \forall b_i \in B$$
* 得$$r_y (x)=0, ~\forall x \in V$$
* 所以$$f(x,y)=r_y (x)=0, ~\forall x,y \in V$$
* 即$$f=0$$  ，所以$$ker⁡(\phi)=\{0\}$$
* (3)映成函數
* $$\forall A \in F^{N \times N}$$
* 考慮座標同構函數$$c_B:V \rightarrow F^{N \times 1}$$, $$c_B (x)=[x]_B$$
* 定義$$f: V \times V \rightarrow F$$, $$f(x,y)=[c_B (y)]^\top A[c_B (x)]$$
* 因為$$f \in B(v)$$
* 欲證$$\phi(f)=\psi_B(f)=A$$
* 因為$$c_B (b_i )=e_i$$，$$c_B (b_j )=e_j$$
* 所以$$f(b_j,b_i )=[c_B (b_i )]^\top A[c_B (b_j )]=e_i^\top Ae_j=e_i^\top A_{:j}=[A]_{ij}, \forall i,j=1,2,\dots,N$$
* 得$$\phi(f)=\psi_B (f)=A$$為映成函數 (QED).

## 對稱雙線性形式、Hermitian型式

> 雙線性形式$$f \in B(V)$$，若$$f(x,y)= f(y,x) ~\forall x,y \in V$$，則稱$$f$$為對稱雙線性形式（symmetric bilinear form）。
>
> Sesqui形式$$f \in F(V)$$，若$$f(x,y)=\overline{f(y,x)}, ~ \forall x, y \in V$$，則稱$$f$$為Hermitian形式。

* 令$$B=\{b_1,b_2,\dots,b_N \}$$為$$V$$的一組基底，$$A=\psi_B (f)$$
* 若$$f$$為對稱雙線性形式，則$$f(b_j,b_i )=f(b_i,b_j )$$，即$$[A]_{ij}=[A]_{ji}, ~\forall i,j$$，因此$$A$$為對稱矩陣。
* 若$$f$$為Hermitian形式，則$$f(b_j,b_i )=\overline{f(b_i,b_j)}$$，即$$[A]_{ij}=\overline{[A]_{ji}}, ~ \forall i,j$$，因此$$A$$為Hermitian形式。

## 正定型式

> 雙線性函數$$f\in B(V)$$或Sesqui型式函數$$f \in F(V)$$。
>
> 定義函數$$Q: V \rightarrow F$$，$$Q(x) = f(x,x) > 0, \forall x \neq 0$$，稱$$f$$為正定形式（positive definite form）。

## 二次型式

> 雙線性函數$$f\in B(V)$$或Sesqui型式函數$$f \in F(V)$$。
>
> 定義函數$$Q: V \rightarrow F$$，$$Q(x) = f(x,x)$$，稱$$Q$$為$$f$$的二次式(quadratic form associated with f)。

#### 範例

* $$f \in B(V)$$，$$f(x,y)=\frac{1}{4} (Q(x+y)−Q(x−y)), ~\forall x,y \in V$$
* $$\begin{align} &Q(x+y)−Q(x−y)  \\ &=f(x+y,x+y)−f(x−y,x−y) \\ &=[f(x,x)+f(x,y)+f(y,x)+f(y,y)]−[f(x,x)−f(x,y)−f(y,x)+f(y,y)] \\ &=2f(x,y)+2f(y,x) \\ &=2f(x,y)+2f(x,y) \\ &=4f(x,y) \end{align}$$

## 二次式的應用

### 主軸定理(principal axis theorem)

> * $$A \in \mathbb{C}^{N \times N}$$ 為Hermitian matrix ($$A^\mathrm{H}=A$$)
>   * 則$$A$$的二次式$$Q(x)=x^\mathrm{H} Ax$$可化成$$Q(x)=\lambda_1 |y_1 |^2+\lambda_2 |y_2 |^2+\dots+\lambda_N |y_N |^2$$
>   * $$\lambda_1,\dots,\lambda_N$$ 為$$A$$的特徵根，$$y_1,y_2\dots,y_N \in \mathbb{C}$$。>

> * $$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣 ($$A^\top=A$$)
>   * 則$$A$$的二次式$$Q(x)=x^\top Ax$$可化成$$Q(x)=\lambda_1 |y_1 |^2+\lambda_2 |y_2 |^2+\dots+\lambda_N |y_N |^2$$
>   * $$\lambda_1, \dots,\lambda_N$$ 為$$A$$的特徵根，$$y_1,y_2, \dots,y_N \in \mathbb{R}$$。>

### 正定矩陣的轉換

>
>
> $$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣，$$x=\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\x_N\end{bmatrix}$$，$$Q(x)=x^\top Ax$$為二次式，若$$A$$為正定矩陣（$$A^\top A = AA\top =I_N$$），則：> $$\displaystyle \int_{-\infty}^{\infty} \dots \int_{-\infty}^{\infty} e^{-Q(x)}dx_1 \cdots dx_N =(\det(A))^{-\frac{1}{2}}\pi^{\frac{N}{2}}$$

### &#x20;Rayleigh quotient

> * $$A \in \mathbb{C}^{N \times N}$$ 為Hermitian矩陣($$A^\mathrm{H}=A$$)，$$x\neq 0$$, 定義$$\rho(x)=\frac{(Q(x))}{\|x\|^2}$$  稱為$$x$$之Rayleigh quotient, $$Q(x)=x^\mathrm{H} Ax$$為$$A$$的二次式。
> * $$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣($$A^\top=A$$)，$$x \neq 0$$，定義$$\rho(x)=\frac{Q(x)}{\|x\|^2}$$  稱為$$x$$之Rayleigh quotient。

* 若$$\|x\|=1$$，則$$\rho(x) = Q(x)$$
* $$\rho(x) = \frac{Q(x)}{\|x\|^2} = \frac{x^\mathrm{H}Ax}{x^\mathrm{H}x} = \frac{\langle Ax, x \rangle}{\langle x, x \rangle}$$

### Raleigh quotient與特徵向量

> * $$A \in \mathbb{C}^{N \times N}$$ 為Hermitian矩陣($$A^\mathrm{H}=A$$)，$$\lambda$$為$$A$$的特徵根，$$x$$為$$A$$相對於$$\lambda$$的特徵向量，則$$\rho(x)=\lambda$$。
> * $$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣($$A^\top=A$$)， $$\lambda$$為$$A$$的特徵根，則$$x$$為$$A$$相對於$$\lambda$$的特徵向量，則$$\rho(x)=\lambda$$。

因為$$\rho(x) = \frac{\langle Ax, x\rangle}{\langle x,x \rangle} =  \frac{\langle \lambda x, x\rangle}{\langle x,x \rangle}  =  \frac{ \lambda \langle x, x\rangle}{\langle x,x \rangle}  = \lambda$$(QED)

### Rayleigh principle (特徵根與二次式的關係)

> $$A \in \mathbb{C}^{N \times N}$$ 為Hermitian矩陣($$A^\mathrm{H}=A$$)， $$\lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_N$$ 為$$A$$的特徵根，則：
>
> * $$\lambda_1 \leq \rho(x) \leq \lambda_N$$
> * $$\max_{x \neq 0}⁡\rho(x)=\lambda_N$$
> * $$\min_{x \neq 0}⁡ \rho(x)=\lambda_1$$>

> $$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣($$A^\top=A$$)，$$\lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_N$$ 為$$A$$的特徵根，則：
>
> * $$\lambda_1 \leq \rho(x) \leq \lambda_N$$
> * $$\max_{x \neq 0}⁡\rho(x)=\lambda_N$$
> * $$\min_{x \neq 0}⁡ \rho(x)=\lambda_1$$
