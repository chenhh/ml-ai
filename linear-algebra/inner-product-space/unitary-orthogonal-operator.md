# 么正\(正交\)算子\(unitary \(orthogonal\) operator\)

##  么子算子、正交算子

> 線性轉換$$T \in L(V,V)$$，$$T^{*}$$為伴隨算子，若$$T^∗ T=I$$，則：
>
> * 當體$$F$$為複數$$\mathbb{C}$$時稱么正算子\(unitary operator\)。
> * 當體$$F$$為實數$$\mathbb{R}$$時稱正交算子\(orthogonal operator\)。
>
> 矩陣$$A \in F^{N \times N}$$
>
> * 當$$A^\mathrm{H} A=I_N$$時，稱$$A$$為么正矩陣\(unitary matrix\)。
> * $$A^\top A=I_N$$時，稱$$A$$為正交矩陣\(orthogonal matrix\)。

* $$A$$為么正矩陣$$\Leftrightarrow A^{−1}=A^\mathrm{H}$$。
* $$A$$為正交矩陣$$\Leftrightarrow A^{−1}=A^\top$$。

### 正交矩陣的性質

> 矩陣$$A \in \mathbb{C}^{N \times N}$$ \(或$$A \in \mathbb{R}^{N \times N}$$\)為么正矩陣（正交矩陣），則：
>
> 1. $$A$$為正規矩陣\($$A^\mathrm{H} A=I_N=AA^\mathrm{H}$$，$$A^\top A=I_N=AA^\top$$ \)。
> 2. $$A$$的相異特徵根對應的特徵向量必正交 （因為么正\(正交\)矩陣為正規矩陣）。
> 3. $$A$$的特徵根$$\lambda$$滿足$$|\lambda|=1$$。
> 4. $$|\det⁡(A)|=1$$ \($$\det⁡(AA^\mathrm{H} )=\det(A) \overline{\det(A)}=det⁡(I_N)=1$$\)

Proof \(3\):

* $$\exists x \neq 0 \ni Ax=\lambda x$$
* 得$$x^\mathrm{H} A^\mathrm{H} Ax=x^\mathrm{H} I_N x=x^\mathrm{H} x=\|x\|^2$$。
* 且$$x^\mathrm{H} A^\mathrm{H} Ax=(Ax)^\mathrm{H} (Ax)=\|Ax\|^2=\| \lambda x\|^2=|\lambda |^2 \|x\|^2$$
* 所以$$\|x\|^2=|\lambda|^2 \|x\|^2$$且$$\|x\|^2\geq 0$$，得$$|\lambda|^2=1$$，所以$$|\lambda|=1$$ \(QED\)

### 零算子對所有向量的內積為零

> 向量空間$$V$$定義在$$\mathbb{C}$$上，線性轉換$$T \in L(V,V)$$，則：
>
> * 若$$\langle T(x),y\rangle=0, ~\forall x,y \in V$$，則$$T=0$$（即$$\forall x \in V, T(x)=0$$）
> * 若$$\langle T(x),x \rangle=0, ~x \in V$$，則$$T=0$$。
>
> 註：若$$\langle x, y \rangle =0, ~ \forall y \in V$$，則$$x=0$$，或者$$\forall x \in V$$，則$$y=0$$，即只有0向量與所有向量的內積為0。

Proof \(1\)

* 因為$$\langle T(u),v \rangle=0,~ \forall u,v \in V$$
* 令$$v=T(u)$$，得$$\langle T(u), T(u)\rangle=0,~\forall u \in V$$
* 所以$$T(u)=0, \forall u \in V$$，即$$T=0$$ \(QED\)

Proof \(2\):

* $$\forall u,v \in V,  \langle T(u),u\rangle=\langle T(v),v \rangle=\langle T(u+v), u+v\rangle=0$$
* 所以$$0=\langle T(u+v),u+v \rangle= \langle T(u)+T(v),u+v \rangle=\langle T(u),u\rangle+\langle T(u),v\rangle+\langle T(v),u \rangle+\langle T(v),v \rangle=\langle T(u),v\rangle+\langle T(v),u \rangle$$−−\(a\)
* 因為$$\forall u,v\in V$$，$$\langle T(u),v\rangle=0$$，得$$0=\langle T(iu),v \rangle+\langle T(v),iu \rangle=\langle iT(u),v \rangle+\langle T(v),iu \rangle=i\langle T(u),v \rangle−i \langle T(v),u\rangle \Rightarrow  \langle T(u),v \rangle−\langle T(v),u \rangle=0$$−−\(b\)
* \(a\)\(b\)相加得$$2 \langle T(u),v \rangle =0 \Rightarrow T=0$$ \(QED\)

###  么正算子的性質

> 向量空間$$V$$定義在$$\mathbb{C}$$上，線性轉換$$T \in L(V,V)$$，則以下敘述等價：
>
> 1. $$T$$為么正算子（$$T^*T=I$$）
> 2. $$T$$保內積，即$$\langle T(x), T(y) \rangle = \langle x, y \rangle, ~\forall x, y \in V$$）
> 3. $$T$$保長度，即$$\| T(x)\| = \|x\|, ~ \forall x \in V$$。
> 4. 若$$B$$為$$V$$的單範正交基底，則$$T(B)$$也是$$V$$的單範正交基底。
>
> 註：么正算子可以視為空間上基底變換某個視角看資料，資料間的距離、長度均不變，只有資料的座標變了。

Proof \(1\)=&gt;\(2\)

* $$\forall x ,y \in V,  \langle T(x),T(y) \rangle=\langle T^∗ T(x),y \rangle=\langle I(x),y⟩= \langle x,y \rangle$$   \(QED\)

Proof \(2\)=&gt;\(3\)

* $$\forall x \in V,  \|T(x)\|^2=\langle T(x),T(x) \rangle=\langle x,x \rangle=\|x \|^2$$
* 因為$$\|T(x)\|^2=\|x\|^2  \text{ and } \|\cdot \| \geq 0 \Rightarrow \|T(x)\|=\|x\|$$ \(QED\)

Proof \(3\)-\(1\):

* $$\forall x  \in V,  \langle x ,x   \rangle= \|x \|^2=\|T(x)\|^2= \langle T(x),T(x) \rangle=\langle T^∗ T(x),x \rangle$$
* 所以$$\langle x,x \rangle−\langle T^∗ T(x),x \rangle=\langle x−T^∗ T(x),x \rangle=\langle (I−T^∗ T)(x),x \rangle=0$$
* 根據前述定理得$$I−T^∗ T=0$$，所以$$T^∗ T=I$$ \(QED\)

Proof \(2\),\(3\)&lt;=&gt;\(4\)

* 令$$B=\{b_1,\dots, b_N \},~b_i =1,~\forall i$$ 且$$\langle b_i,b_j \rangle=0, ~\forall i \neq j$$
* 因為$$T$$保長度，所以$$\|T(b_i )\|=1, ~\forall i$$
* 因為$$T$$保內積，所以$$\langle T(b_i ),T(b_j ) \rangle=\langle b_i, b_j  \rangle=0, ~\forall i \neq j$$
* 因此$$T(B)$$也為$$V$$的單範正交基底 \(QED\)

### 矩陣相等時，矩陣的二次式也相等

> 矩陣$$A,B \in F^{N \times N}$$，則以下條件等價：
>
> 1. $$A=B$$
> 2. $$y^\mathrm{H}Ax = y^\mathrm{H}Bx, ~\forall x, y\in F^{N \times 1}$$

Proof \(1\)=&gt;\(2\) 必定成立。

Proof \(2\)=&gt;\(1\):

* 令$$x=e_j,~y=e_i$$
* $$y^\mathrm{H} Ax=e_i^\mathrm{H} Ae_j=e_i^\mathrm{H} A_{:j}=(A)_{ij}, ~\forall i,j=,1,2\dots,N$$
* 同理$$y^\mathrm{H} Bx=(B)_{ij},~ \forall i,j=1,2, \dots,N$$
* 所以$$(A)_{ij}=(B)_{ij}, ~\forall i,j=1,2,\dots,N$$，可得$$A=B$$ \(QED\)

### 么正\(正交\)矩陣的性質

> 矩陣$$A \in \mathbb{C}^{N \times N}$$ （或$$A \in \mathbb{R}^{N\times N}$$），則下列敘述等價：
>
> 1. $$A$$為么正矩陣\($$A^\mathrm{H} A=I_N$$\)，\($$A$$為正交矩陣$$A^\top A=I_N$$\)  。
> 2. $$A$$保內積，即$$\langle Ax,Ay \rangle=\langle x,y \rangle, ~\forall x,y \in \mathbb{C}^{N \times 1}$$。
> 3. $$A$$保長度，即$$\|Ax\|=\|x\|, ~\forall x \in C^{N \times 1}$$。
> 4. 若$$B=\{b_1,\dots,b_N \}$$為$$V$$的單範正交基底，則$$\{Ab_1, \dots,Ab_N \}$$也為$$V$$的單範正交基底。
> 5. $$A$$的行向量為單範正交集。
> 6. $$A$$的列向量為單範正交集。

Proof \(1\)=&gt;\(2\):

$$\forall x,y \in \mathbb{C}^{N \times 1},  \langle Ax,Ay \rangle= \langle x,A^\mathrm{H} Ay \rangle= \langle x,Iy \rangle= \langle x,y \rangle$$  \(QED\)

Proof \(2\)=&gt;\(3\)

$$\forall x \in \mathbb{C}^{N \times 1} , \|Ax\|^2=\langle Ax,Ax \rangle= \langle x,x \rangle=\|x\|^2 \Rightarrow \|Ax\|=\|x\|$$ \(QED\)

Proof \(3\)=&gt;1:

* $$\forall x, y \in \mathbb{C}^{N \times 1}$$，$$y^\mathrm{H}A^\mathrm{H} Ax = (Ay)^\mathrm{H} (Ax) = \langle Ax, Ay \rangle = \frac{1}{4} \sum_{k=1}^4 i^k \| Ax+ i^k Ay\|^2 = \frac{1}{4} \sum_{k=1}^4 i^k \| x + i^k y\|^2 = \langle x, y \rangle = y^\mathrm{H} x = y^\mathrm{H} I x$$
* 由矩陣相等時，矩陣的二次式也相等得$$A^\mathrm{H} A=I$$ \(QED\)

Proof \(5\) \(6\): 由$$A^\mathrm{H} A=I$$可知第$$i$$列\(行\)與第$$j$$列\(行\)在$$i \neq j$$時內積均為0，而在$$i=j$$時內積為1，因此為單範正交集 \(QED\).

## polar identity

> $$V$$為定義於體$$F$$的向量空間，則$$\forall x, y \in V$$：
>
> 1. 若$$F = \mathbb{R}$$，則$$\langle x,y\rangle = \frac{1}{4}\| x+y\|^2-\frac{1}{4} \|x-y\|^2$$
> 2. 若$$F = \mathbb{C}$$，則$$\langle x, y \rangle = \frac{1}{4}\sum_{k=1}^4 i^k\|x+i^ky\|^2$$
>
> [wiki: polarization identity](https://en.wikipedia.org/wiki/Polarization_identity).

Proof \(1\):

* $$\begin{align} &\frac{1}{4} \|x+y\|^2 −\frac{1}{4}\|x−y\|^2  \\&=\frac{1}{4} \langle x+y,x+y \rangle −\frac{1}{4} \langle x−y,x−y \rangle \\ &=\frac{1}{4} (\langle x,x \rangle+ \langle x,y \rangle+ \langle y,x \rangle+\langle y,y \rangle) \\ &−\frac{1}{4} (\langle x,x \rangle− \langle x,y \rangle− \langle y,x \rangle+ \langle y, y \rangle) \\ &=\frac{1}{2} \langle x,y \rangle+ \frac{1}{2} \langle y, x \rangle \\ &=\frac{1}{2} \langle x,y \rangle+ \frac{1}{2} \langle x,y \rangle \\ &= \langle x,y \rangle \end{align}$$  \(QED\)

Proof \(2\):

* $$  \begin{align} & \frac{1}{4} (i^4 \|x+y\|^2+i^2 \|x+i^2 y\|^2 ) \\ &=\frac{1}{4} (\|x+y\|^2−\|x−y\|^2 ) \\ &=\frac{1}{4} (\langle x+y,x+y \rangle− \langle x−y,x−y \rangle ) \\ &=\frac{1}{2} (\langle x,y \rangle +\langle x,y   \rangle ) \\ &=\frac{1}{2} (\langle x,y  \rangle+\overline{\langle x,y \rangle} ) \\ &=\mathrm{Re}( \langle x,y \rangle)  \end{align}$$

	• 1/4 \(i‖u+iv‖^2+i^3 ‖u+i^3 v‖^2 \)=1/4 \(i‖u+iv‖^2−i‖u−iv‖^2 \)=i/4 \(⟨u+iv, u+iv⟩−⟨u−iv,u−iv⟩\)=i/4 \(⟨u,u⟩−i⟨u,v⟩+i⟨v,u⟩−⟨v,v⟩−⟨u,u⟩−i⟨u,v⟩+i⟨v,u⟩+⟨v,v⟩\)=i/4 \(−2i⟨u,v⟩+2i⟨v,u⟩\)=i/4 \(−2i⟨u,v⟩+2i \(⟨u,v⟩ \) ̅ \)=1/2 \(⟨u,v⟩−\(⟨u,v⟩ \) ̅ \)=1/2 \(2i Im\(⟨u,v⟩\)\)=i Im\(⟨u,v⟩\)

	• ∴1/4 ∑\_\(k=1\)^4▒〖i^k ‖u+i^k v‖^2=〗 Re\(⟨u,v⟩\)+i Im\(⟨u,v⟩\)=⟨u,v⟩  \(QED\)















### 



