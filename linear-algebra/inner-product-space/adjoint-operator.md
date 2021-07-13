# 伴隨算子\(adjoint operator\)

##  伴隨算子\(adjoint operator\)

> 內積空間$$V$$定義在體$$F$$上，線性轉換$$T \in L(V,V)$$。
>
> 若存在線性轉換$$T^{*} : V \rightarrow V$$滿足$$\langle T(x), y \rangle = \langle x, T^{*}(y) \rangle, ~\forall x,y \in V$$，則稱$$T^{*}$$為$$T$$的伴隨算子（存在且唯一）。
>
> 也可表示為$$\langle x, T(y) \rangle= \langle T^{*}(x), y\rangle, ~\forall x,y \in V$$。
>
> * 此為Hermetian \(transpose\) matrix線性映射的版本。
> * 伴隨算子必定存在且唯一。
> * 內積算子必須滿足$$\langle x, y \rangle = \overline{\langle y,x \rangle}$$

* 若給定向量空間的基底$$B$$，且令$$A=[T]_B$$，則$$\langle [T]_B(x), y\rangle=\langle Ax, y\rangle=y^\mathrm{H} (Ax) =\overline{ x^\mathrm{H} (A^\mathrm{H}y)} = \langle A^\mathrm{H}y, x \rangle$$。

### 給定內積與單一向量時，另一向量的存在性與唯一性

> 內積空間$$V$$定義在體$$F$$上，線性泛函:$$f: V \rightarrow F$$，則存在唯一$$v \in V \ni f(u) = \langle u, v \rangle, \forall u \in V$$。（給定向量$$u$$，且$$f(u)$$之值已經知道時，則$$v \in V$$存在且唯一。）
>
> 如果$$v$$為單範正交基底中的元素，即$$\|v\|=1$$，則$$f(u)$$為將向量$$u$$投影到此基底元素的係數，$$f(u) = a = \frac{\langle u, v \rangle}{\langle v, v \rangle} = \langle u, v \rangle$$。

Proof:

* 令$$B=\{v_1,\dots,v_N \}$$為$$V$$的一組單範正交基底，取$$v=\sum_{i=1}^N \overline{f(v_i)}v_i$$
* 定義$$ g:V \rightarrow F, ~g(u)=\langle u,v \rangle,  \forall u \in V$$。
* 所以$$j=1,2,\dots,N, g(v_j )=\langle v_j,v\rangle=\langle v_j,\sum_{i=1}^N \overline{f(v_i) }v_i\rangle=\sum_{i=1}^N f(v_i )\langle v_j,v_i \rangle =\sum_{i=1}^N f(v_i )  \delta_{ij}=f(v_j )$$
* 因此可得$$g=f$$，證明了存在性。
* 若$$\exists v^′ \in V \ni f(u)=\langle u,v^′\rangle, \forall u \in V$$
* 可得$$\langle u,v\rangle= \langle u,v^′\rangle ,~ \forall u \in V$$
* 所以$$\langle v,u \rangle=\langle v^′,u\rangle ,~\forall u \in V$$
* 因此$$v=v^′$$，證明了唯一性 \(QED\)

###  伴隨算子存在唯一性

> 內積空間$$V$$定義在體$$F$$上，線性轉換$$T \in L(V,V)$$，則$$T$$的伴隨算子$$T^{*}$$存在且唯一。

proof:

* $$\forall v \in V$$，定義$$f:V \rightarrow F, f(u)=\langle T(u),v\rangle$$，則$$f$$為線性，證明如下。
* $$\forall a,b \in F, u_1,u_2 \in V$$
* $$f(au_1+bu_2 )=⟨T(au_1+bu_2 ),v⟩=\langle aT(u_1 )+bT(u_2 ),v \rangle =a\langle T(u_1 ),v\rangle +b \langle T(u_2 ),v \rangle=af(u_1 )+bf(u_2 )$$，所以$$f$$為線性。
* 根據前述定理，唯一存在$$v^′ \in V \ni f(u)=\langle u,v^′ \rangle, ~\forall v \in V$$。
* 因此$$\langle T(u),v \rangle= \langle u,v^′ \rangle, \forall u \in V$$。
* 定義$$T^∗:V \rightarrow V, T^∗ (v)=v^′$$，證明$$T^∗$$ 為線性如下。
* $$\forall a,b \in F, v_1,v_2 \in V$$
* $$\langle u, T^∗ (av_1+bv_2 ) \rangle= \langle T(u), av_1+bv_2 \rangle= \overline{a} \langle T(u),v_1 \rangle +\overline{b} \langle T(u),v_2 \rangle=\overline{a} \langle u,T^∗ (v_1) \rangle +\overline{b} \langle u,T^∗ (v_2)\rangle =\langle u, aT^∗ (v_1 )+bT^∗ (v_2 )\rangle,~ \forall u \in V$$，所以$$T^∗$$ 為線性。
* 證明$$T^∗$$ 唯一性
* 假設存在$$U:V \rightarrow V \ni  \langle T(u),v\rangle = \langle u, U(v)\rangle ,~ \forall u,v \in V$$。
* 所以$$\langle u,U(v) \rangle=\langle u, T^∗ (v)\rangle,~ \forall u,v \in V$$。
* $$\langle U(v),v \rangle=\langle T^∗ (v),u \rangle, ~\forall u,v \in V$$。
* 根據內積算子性質得所以$$U=T^∗$$，即$$T^∗$$ 唯一 \(QED\)

### 伴隨算子的另一種計算方式

> * 線性轉換$$T \in L(V,V)$$，則$$\langle u, T(v) \rangle= \langle T^∗ (u),v \rangle,~ \forall u,v \in V$$。
> * 矩陣$$A \in F^{N \times N}$$，$$\langle Ax, y \rangle = \langle x, A^\mathrm{H}y \rangle$$且$$\langle x, Ay \rangle = \langle A^\mathrm{H}y, x \rangle ~ \forall x \in F^{N \times 1}$$。

Proof:

* $$\langle u,T(v)\rangle=\overline{\langle⟨T(v),u⟩\rangle}=\overline{\langle v,T^∗ (u) \rangle}=\langle T^∗ (u),v \rangle$$  \(QED\)

proof:

* 
### 伴隨算子的矩陣表示法為Hermetian matrix

> 線性轉換$$T \in L(V,V)$$，$$B=\{b_1, b_2, \dots, b_N\}$$為$$V$$的一組單範正交基底，則：$$[T^*]_B=[T]_B^\mathrm{H}$$。
>
> 註：若$$B$$為非單範正交基底時，可經Gram-Schmidt正交化過程處理即可。

Proof:

* 令矩陣$$A=[T]_B, P=[T^∗ ]_B$$
* 根據單範正交基底的係數得$$T(b_j )=\sum_{i=1}^N \langle T(b_j ),b_i \rangle  b_i$$
* 所以$$[T(b_j )]_B = \begin{bmatrix}  \langle T(b_j), b_1 \rangle \\ \langle T(b_j), b_2 \rangle \\ \vdots \\ \langle T(b_j), b_N \rangle \end{bmatrix}$$
* 因此$$[A]_{ij}=\langle T(b_j ),b_i \rangle, ~\forall i,j=1,2, \dots,N$$
* 同理可得$$[P]_{ij}= \langle T^∗ (b_j ),b_i  \rangle, ~\forall i,j=1,2,\dots,N$$
* 所以$$[P]_{ij}=\langle T^∗ (b_j ),b_i \rangle=\overline{\langle b_i,T^∗ (b_j) \rangle}=\overline{\langle T(b_i), b_j \rangle} = \overline{A_{ji}} = (A^\mathrm{H})_{ij}$$
* 可得$$P=A^\mathrm{H}$$  \(QED\)

#### 範例

* 線性轉換$$T:\mathbb{C}^2 \rightarrow \mathbb{C}^2$$，$$T(x,y)=(2ix+3y, ~ x-y)$$
* 取$$\mathbb{C}^2$$的標準基底：$$B=\{e_1, e_2\}$$。
* $$T(e_1)=(2i, 1) = 2i \begin{bmatrix} 1 \\ 0  \end{bmatrix} + 1 \begin{bmatrix} 0 \\ 1\end{bmatrix}$$
* $$T(e_2) = (3, -1) = 3 \begin{bmatrix} 1 \\ 0 \end{bmatrix} + (-1) \begin{bmatrix} 0 \\ 1\end{bmatrix}$$
* 所以 $$[T]_B=\begin{bmatrix} 2i & 3 \\ 1 & -1 \end{bmatrix}$$
* $$[T^*]_B=[T]_B^\mathrm{H}=\begin{bmatrix} -2i & 1 \\ 3 & -1 \end{bmatrix}$$
* $$T^*(e_1)=(-2i, 3), ~T^*(e_2)=(1, -1)$$
* $$T^*(x,y)=xT^*(e_1)+yT^*(e_2)=(-2ix+y, 3x-y)$$





