# 正規算子、自伴算子\(normal operator, self-adjoint operator\)

##  正規算子、正規矩陣\(normal operator, normal matrix\)

> * 線性轉換$$ T \in L(V,V)$$，且$$T^∗$$為伴隨算子（$$\langle T(x),y \rangle=\langle x, T^∗ (y)\rangle, ~\forall x,y \in V$$），若$$T^∗ T=TT^∗$$，則稱$$T$$為正規算子。
> * $$A \in F^{N \times N}，若A^\mathrm{H} A=AA^\mathrm{H}$$，則稱$$A$$為正規矩陣。
>
> 在[最小平方解](least-square-solution.md#jian-jie)有討論過正規矩陣的性質。

### 正規算子特徵向量空間特性\(必要條件\)

> 線性轉換$$T \in L(V,V)$$，$$T$$為正規算子則：
>
> 1. （轉換後長度相同） $$\|T(v)\|=\|T^∗ (v)\|,  ~\forall v \in V$$。
> 2. $$\forall c \in F$$， $$T−cI$$為正規算子。
> 3. （特徵向量不變）若$$\lambda$$為$$T$$的特徵根，且$$v$$為$$T$$相對於$$\lambda$$的特徵向量，則$$v$$為$$T^∗$$ 相對$$\overline{\lambda}$$的特徵向量。
> 4. （相異特徵根之特徵向量必正交）若$$\lambda_1,\lambda_2$$ 為$$T$$的兩個相異特徵根，且$$v_1,v_2$$ 分別為$$T$$相對於$$\lambda_1,\lambda_2$$ 的特徵向量，則$$v_1 \bot v_2$$。

> 矩陣$$A \in F^{N \times N}$$ 為正規矩陣時可得：
>
> 1. $$\|Ax\|=|A^\mathrm{H} x\|,~\forall x \in F^{N \times 1}$$   。
> 2. $$\forall c \in F, ~A−cI$$為正規矩陣。
> 3. 若$$\lambda$$為$$A$$的特徵根，且$$v$$為$$A$$相對於$$\lambda$$的特徵向量，則$$v$$為$$A^\mathrm{H}$$ 相對$$\overline{\lambda}$$的特徵向量。
> 4. 若$$\lambda_1,\lambda_2$$ 為$$A$$的兩個相異特徵根，且$$v_1,v_2$$ 分別為$$T$$相對於$$\lambda_1,\lambda_2$$ 的特徵向量，則$$v_1 \bot v_2$$。

Proof \(1\):

* $$\|T(v)\|^2=\langle T(v),T(v) \rangle= \langle v,T^∗ T(v) \rangle$$\[根據伴隨算子定義\]$$=\langle v,TT^∗ (v) \rangle $$\[正規算子定義\]$$= \langle T^∗ (v),T^∗ (v)\rangle =\|T^∗ (v)\|^2$$。
* 所以$$\|T(v)\|=\|T^∗ (v)\|$$  \(QED\)

Proof \(2\):

* $$(T−cI)^∗ (T−cI)=(T^∗−\overline{c}I)(T−cI)=TT^∗−cT^∗−\overline{c}T+|c|^2 I=T^∗ T−cT^∗−\overline{c}T+|c|^2 I=(T−cI)(T^∗−\overline{c}I)=(T−cI) (T−cI)^∗$$ \(QED\)

Proof \(3\)

* $$T(v)=\lambda v, v\neq 0 \Rightarrow (T−\lambda I)(v)=0$$
* 由\(2\)知$$T−cI$$為正規算子，再由\(1\)得$$0=\|(T−\lambda I)(v) \|=\|(T−\lambda I)^∗ (v)\|=\|(T^∗\overline{\lambda}I)(v)\|=\|T^∗ (v)−\overline{\lambda}(v)\|$$
* $$T^∗ (v)−\overline{\lambda}(v)=0 \Rightarrow T^∗ (v)=\overline{\lambda}(v)$$，因此$$v$$為$$T^∗$$ 相對$$\overline{\lambda}$$的特徵向量 \(QED\).

Proof \(4\)

* $$T(v_1 )=\lambda_1 v_1, ~T(v_2 )=\lambda_2 v_2, ~v_1,v_2 \neq 0$$
* $$\lambda_1 \langle v_1,v_2 \rangle= \langle \lambda_1 v_1,v_2 \rangle=\langle T(v_1 ),v_2 \rangle =\langle v_1,T^∗ (v_2) \rangle=\langle v_1, \overline{\lambda_2}v_2 \rangle=λ_2 \langle v_1,v_2 \rangle$$
* $$\Rightarrow (\lambda_1−\lambda_2 )\langle v_1,v_2 \rangle=0$$
* 因為$$\lambda_1 \neq \lambda_2 \Rightarrow \langle v_1,v_2 \rangle=0$$，即$$v_1 \bot v_2$$  \(QED\)

## 自伴算子、斜自伴算子\(self-adjoint operator, skew self-adjoint operator\)

> * 線性轉換$$T \in L(V,V)$$，若$$T^∗=T$$，則稱$$T$$為自伴算子\(self-adjoint operator\)。
> * 線性轉換$$T\in L(V,V)$$，若$$T^∗=−T$$，則稱$$T$$為斜自伴算子\(skew self-adjoint operator\)。

### 自伴算子的特性

> 線性轉換$$T\in L(V,V)$$為自伴算子，則：
>
> 1. $$T$$為正規算子（自伴算子為正規算子的子集合）。
> 2. $$T$$的相異特徵根對應之特徵向量必正交。
> 3. $$T$$的特徵根皆為實數。
> 4. $$T$$的特徵多項式在$$\mathbb{R}$$可分解。
> 5. $$\det⁡(T) \in \mathbb{R}$$。

### Hermitian\(symmetric\)矩陣的特性

> 矩陣$$A \in \mathbb{C}^{N \times N }$$ Is Hermitian matrix \($$A^\mathrm{H}=A$$\)，\(若$$A \in \mathbb{R}^{N\times N}$$，則$$A^\top＝A$$\)則：
>
> 1. $$A$$為正規矩陣 \(∵$$A^\mathrm{H} A=AA=AA^\mathrm{H}，A^\top A=AA=AA^\top$$ \)。
> 2. $$A$$的相異特徵根對應之特徵向量必正交\(∵Hermitian \(symmetric\) matrix為正規矩陣\)。
> 3. $$A$$的特徵根均為實數。
> 4. $$A$$的特徵多項式在$$\mathbb{R}$$可分解 \(由\(3\)成立\)。
> 5. $$A$$的主對角項元素皆為實數 \(因為$$[A^\mathrm{H} ]_{ii}=[A]_{ii} \Leftrightarrow (\overline{A^\top}) ]_{ii}=[A]_{ii}\Leftrightarrow [\overline{A} ]_{ii}=[A]_{ii},~ i=1,2,\dots,N$$\)
> 6. $$\det⁡(A) \in \mathbb{R}$$ \($$\det⁡(A)=\det⁡(A^\mathrm{H} )=\overline{\det⁡(A^\top)} = \overline{\det(A)}$$\)

註：$$A \in \mathbb{C}^{N \times N}$$ 為對稱矩陣不保證$$A$$為正規矩陣。

* $$A=\begin{bmatrix} i & i \\ i & 1\end{bmatrix} = A^\top$$，$$A^\mathrm{H}A=\begin{bmatrix}  2 & 1-i \\ 1+i & 2 \end{bmatrix} \neq \begin{bmatrix}  2 & 1+i \\ 1-i  & 2 \end{bmatrix} = AA^\mathrm{H}$$

Proof \(3\):

* 令$$\lambda$$為$$A$$的特徵根，則$$\exists x \neq 0 \ni Ax=\lambda x$$
* 可得$$x^\mathrm{H} Ax=x^\mathrm{H}  \lambda x=\lambda x^\mathrm{H} x=\lambda \|x\|^2$$
* 而$$x^\mathrm{H} Ax=x^\mathrm{H} A^\mathrm{H} x=(Ax)^\mathrm{H} x=(\lambda x)^\mathrm{H} x=\overline{\lambda }x^\mathrm{H} x=\overline{\lambda }\|x\|^2$$
* 所以$$\lambda \|x\|^2= \overline{\lambda }\|x\|^2$$
* 因為$$\|x\|^2>0$$，因此$$\lambda = \overline{\lambda}$$，所以特徵根$$\lambda $$為實數 \(QED\)

### 斜自伴算子的特性

> 線性轉換$$T \in L(V,V)$$為斜自伴算子\($$T^∗=−T$$\)，則：
>
> 1. $$T$$為正規算子\(斜自伴算子為正規算子的子集合\)。
> 2. $$T$$的相異特徵根對應之特徵向量必正交。
> 3. $$T$$的特徵根皆為0或純虛數。

### skew Hermitian\(symmetric\)矩陣的性質

> 矩陣$$A \in \mathbb{C}^{N \times N}$$ Is skew Hermitian matrix \($$A^\mathrm{H}=−A$$\)，\(若$$A \in \mathbb{R}^{N \times N}$$，且$$A^\top＝−A$$\)則：
>
> 1. $$A$$為正規矩陣 $$(A^mathrm{H} A=−AA=A(−A)=AA^\mathrm{H}$$\)。
> 2. $$A$$的相異特徵根對應之特徵向量必正交 \(因為skew Hermitian \(symmetric\)矩陣為正規矩陣\)。
> 3. $$A$$的特徵根均為0或虛數。
> 4. $$A$$的主對角項元素均為0或純虛數。   \(因為$$[A^\mathrm{H} ]_{ii}=[−A]_{ii} \Leftrightarrow [\overline{A^\top}]_{ii}=[−A]_{ii} \Leftrightarrow [\overline{A} ]_{ii}=[−A]_{ii},~ i=1,2,\dots,N$$\)
> 5. 當$$N$$為偶數時，$$\det⁡(A) \in \mathbb{R}$$；當$$N$$為奇數時，$$\det⁡(A)=0$$或純虛數。

Proof \(3\):

* 令$$\lambda$$為$$A$$的特徵根，則$$\exists x \neq 0 \ni Ax=\lambda x$$。
* 得$$x^\mathrm{H} Ax=x^\mathrm{H} \lambda x=\lambda x^\mathrm{H} x=\lambda \|x\|^2$$。
* 而$$x^\mathrm{H} Ax=−x^\mathrm{H} A^\mathrm{H} x=−(Ax)^\mathrm{H} x=−(\lambda x)^\mathrm{H} x=-\overline{\lambda}x^\mathrm{H} x=−\overline{\lambda }\|x\|^2$$
* 所以$$\lambda \|x\|^2=−\overline{\lambda }\|x\|^2$$
* 因為$$\|x\|^2>0$$，可得$$\lambda = - \overline{\lambda}$$，因此特徵根$$\lambda$$為純虛數 \(QED\)

Proof\(5\):

* $$\det⁡(A)=\det⁡(−A^\mathrm{H} )=(−1)^N  \det⁡((\overline{A^\top}) )=(−1)^N  \overline{\det(A^\top)} = (-1)^N \overline{\det(A)}$$
* 當$$N$$為偶數時，$$\det⁡(A)=\overline{\det(A)}$$，因此$$\det(A) \in \mathbb{R}$$。
* 當$$N$$為奇數時，$$\det⁡(A)=-\overline{\det(A)}$$，因此$$\det(A)=0$$或純虛數 \(QED\)

