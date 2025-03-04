# 正交子空間(orthogonal subspace)

## 正交子空間(不同子空間的任意元素內積值為零)

> 內積空間$$V$$定義在體$$F$$上，若$$W_1, W_2$$為$$V$$的子空間，且$$\langle w_1, w_2 \rangle, ~\forall w_1 \in W_1, ~w_2 \in W_2$$，稱$$W_1, W_2$$為正交子空間。
>
> 若$$W_1, \dots, W_K$$為$$V$$的子空間，且任意兩個子空間彼此正交（$$W_i \bot W_j, \forall i \neq j$$），則稱$$W_1, \dots W_K$$為正交子空間。

#### 範例：立體空間

* $$V=\mathbb{R}^3$$，$$W_1 =\{ (x,0,0) | x \in \mathbb{R}\}$$，$$W_2=\{ (0,y,0) | y \in \mathbb{R}\}$$，$$W_3=\{(0,0,z)| z \in \mathbb{R}\}$$，則$$W_1, W_2, W_3$$為正交子空間。

### 正交子空間必為獨立子空間

> 內積空間$$V$$定義在體$$F$$上，若$$W_1, \dots, W_K$$為$$V$$的正交子空間，則$$W_1, \dots, W_K$$為獨立子空間。
>
> 因此正交子空間為獨立子空間的子集合。

Proof:

* $$\forall w_i \in W_i$$，若$$w_1+w_2+\dots+w_k=0$$
* 則 $$\forall i=1,2, \dots ,k$$，$$0=\langle w_i,0 \rangle= \langle w_i, w_1+w_2+\dots+w_K  \rangle =\langle w_i,w_1 \rangle+\langle w_i,w_2 \rangle+\dots+\langle w_i,w_K \rangle=\langle w_i,w_i \rangle \Rightarrow w_i=0$$ (QED)

### 矩陣基本子空間的正交子空間

> 矩陣$$A \in F^{M \times N}$$，$$ker(A)=\{x \in F^{N \times 1} | Ax=0\}$$，$$R(A) =\{Ax \in F^{M \times 1}| \forall x \in F^{N \times 1}\}$$則：
>
> 1. $$R(A^\mathrm{H})^\bot = ker(A)$$
> 2. $$R(A)^\bot = ker(A^\mathrm{H})$$
> 3. $$ker(A)^\bot = R(A^\mathrm{H})$$
> 4. $$ker(A^\mathrm{H})^\bot = R(A)$$

Proof (1)

* $$\forall x \in ker⁡(A), Ax=0$$
* $$\forall y \in R(A^\mathrm{H} ), y=A^H z$$ for some $$z \in F^{M \times 1}$$
* $$\langle x,y\rangle =\langle x,A^\mathrm{H} z\rangle=(A^\mathrm{H} z)^\mathrm{H} x=z^\mathrm{H} Ax=z^\mathrm{H} 0=0$$
* 所以$$ker⁡(A) \bot R(A^\mathrm{H} )$$，得$$ker⁡(A) \subseteq R(A^\mathrm{H} )^\bot$$
* 因為$$\dim⁡(ker⁡(A) )=N−\dim⁡(R(A))=N−rank(A)=N−rank(A^\mathrm{H} )=N−\dim⁡(R(A^\mathrm{H} ))$$
* 因為$$R(A^\mathrm{H} )$$與$$R(A^\mathrm{H} )^\bot$$ 為$$F^{N \times 1}$$ 的子空間，所以$$\dim⁡(R(A^\mathrm{H} ))＋\dim⁡(R(A^\mathrm{H} )^\bot )=N$$
* 得$$\dim⁡ (R(A^\mathrm{H} )^\bot )=N−\dim⁡(R(A^\mathrm{H} ))=\dim⁡(ker⁡(A))$$
* 所以$$ker⁡(A)=R(A^\mathrm{H} )^\bot$$  (QED).

Proof (2)

* 因為$$R((A^\mathrm{H} )^\mathrm{H} )^\bot=ker⁡(A^\mathrm{H} )$$
* 所以$$R(A)^\bot=ker(A^\mathrm{H} )$$  (QED)

Proof (3)

* 因為$$R(A^\mathrm{H} )^\bot=ker(A)$$
* 所以$$R(A^\mathrm{H} )^{\bot \bot}=(ker⁡(A) )^\bot$$
* 因此$$R(A^\mathrm{H} )=ker⁡(A)^\bot$$  (QED)

Proof (4)

* 因為$$R(A)^\bot=ker(A^\mathrm{H} )$$
* 所以$$R(A)^{\bot \bot}=ker⁡(A^\mathrm{H} )^\bot$$
* 得$$R(A)=ker⁡(A^\mathrm{H} )^\bot$$  (QED)

### 聯立方程式之解存在的充要條件

> 矩陣$$A \in \mathbb{R}^{M \times N}$$，向量$$b  \in \mathbb{R}^{M \times 1}$$，則：
>
> $$Ax=b$$有解 $$\Leftrightarrow \forall y \in \mathbb{R}^{M \times 1}, ~ A^\top y=0 \ni b^\top y=0$$

Proof =>:

* 因為$$Ax=b$$有解，所以$$b \in R(A)$$
* 若$$y$$滿足$$A^\top y=0$$，則$$y \in ker⁡(A^\top )=R(A)^\bot$$
* 因此$$\langle y,b\rangle=0$$，即$$b^\top y=0$$ (QED)

Proof <=:

* $$\forall y \in ker⁡(A^\top ), b^\top y=\langle y,b \rangle=0$$，得$$\langle b,y\rangle=0, ~\forall y \in ker⁡(A^\top )$$
* 所以$$b \in ker⁡(A^\top)^\bot =R(A)$$，即$$Ax=b$$有解 (QED)

