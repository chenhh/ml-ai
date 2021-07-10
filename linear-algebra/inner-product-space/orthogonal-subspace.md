# 正交子空間\(orthogonal subspace\)

## 正交子空間\(不同子空間的任意元素內積值為零\)

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

* $$\forall w_i \in W_i$$，若$$ w_1+w_2+\dots+w_k=0$$
* 則 $$\forall i=1,2, \dots ,k$$，$$0=\langle w_i,0 \rangle= \langle w_i, w_1+w_2+\dots+w_K  \rangle =\langle w_i,w_1 \rangle+\langle w_i,w_2 \rangle+\dots+\langle w_i,w_K \rangle=\langle w_i,w_i \rangle \Rightarrow w_i=0$$ \(QED\)

### 矩陣基本子空間的正交子空間

> 矩陣$$A \in F^{M \times N}$$，$$ker(A)=\{x \in F^{N \times 1} | Ax=0\}$$，$$R(A) =\{Ax \in F^{M \times 1}| \forall x \in F^{N \times 1}\}$$則：
>
> 1. $$R(A^\mathrm{H})^\bot = ker(A)$$
> 2. $$R(A)^\bot = ker(A^\mathrm{H})$$
> 3. $$ker(A)^\bot = R(A^\mathrm{H})$$
> 4. $$ker(A^\mathrm{H})^\bot = R(A)$$

