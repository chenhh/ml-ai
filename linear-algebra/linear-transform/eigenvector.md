# 特徵向量(eigenvector)

## 特徵根、特徵向量(eigenvalue, eigenvector)

> 線性轉換$$T \in L(V,V)$$，純量$$\lambda \in F$$。
>
> 若存在非零向量$$v∈V \ni T(v)=\lambda v$$> （矩陣式為$$Ax = \lambda x$$），則稱
>
> * $$\lambda$$為相對於$$T$$的特徵根(eigenvalue or characteristic value)，
> * 且$$v$$為相對於$$T$$的特徵向量(eigenvector or characteristic vector)
> * $$T$$可能有多個特徵根，不同的特徵根對應不同的特徵向量。
>
> 在[可對角化的充要條件](diagonal.md#ke-dui-jiao-hua-de-chong-yao-tiao-jian)中，可得線性轉換（矩陣）的特徵向量可視為線性空間的（正交）基底。

![特徵根與特徵值](../../.gitbook/assets/eigenvector-min.png)

![相異特徵向量彼此正交](../../.gitbook/assets/eigenvetor-orthogonal-min.png)

### 對於同一個特徵值之特徵向量的任意線性組合，若不為零向量時，仍為相對於該特徵值的特徵向量

> 線性轉換$$T \in L(V,V),  \lambda \in F$$為$$T$$的特徵根。
>
> * 若$$v$$為$$T$$相對於$$\lambda$$的特徵向量，則$$cv, 0\neq c \in F$$也為$$T$$相對於$$\lambda$$的特徵向量。
> * 若$$v_1,v_2$$ 為$$T$$相對於$$\lambda$$的特徵向量且$$v_1+v_2\neq 0$$，則$$v_1+v_2$$ 也為$$T$$相對於$$\lambda$$的特徵向量。

Proof:

* 因為$$T(v)=\lambda, v\neq 0$$
* 所以$$T(cv)=cT(v)=c\lambda v=\lambda (cv), cv\neq 0$$ (QED)
* 因為$$T(v_1 )=\lambda v_1,~ T(v_2 )=\lambda v_2$$
* 所以$$T(v_1+v_2 )=T(v_1 )+T(v_2 )=\lambda (v_1+v_2 ), ~v_1+v_2 \neq 0$$ (QED)

## 算子的行列式與跡數

> 線性轉換$$T \in L(V,V)$$，$$B=\{b_1,b_2, \dots, b_N\}$$為$$V$$的一組基底。$$[T]_B=\begin{bmatrix}  [T(b_1)]_B & [T(b_2)]_B & \dots & [T(b_N)]_B \end{bmatrix}$$`。`
>
> * 定義$$\det⁡(T)=\det⁡([T]_B )$$
> * 定義$$tr(T)=tr([T]_B )$$

* 若$$B, R$$為$$V$$的兩組基底，則$$[T]_B \sim [T]_R$$  (相似矩陣，存在可逆矩陣$$P\ni PA=PB$$)，因此$$\det⁡ ([T]_B )=\det⁡([T]_R)$$。同理$$tr([T]_B )=tr([T]_R )$$。

### 特徵根的充要條件

> 線性轉換$$T \in L(V,V),  \lambda \in F$$ ，則：
>
> * $$\lambda$$為$$T$$的特徵根若且唯若$$\det⁡(T−\lambda I)=0$$
> * 給定$$V$$的基底$$B$$, $$T−\lambda I \equiv [T−\lambda I]_B=[T]_B−\lambda [I]_B$$

Proof:

* $$\lambda$$為$$T$$的特徵根$$\Leftrightarrow \exists x \neq 0 \ni T(x)=\lambda x \Leftrightarrow x \neq 0, T(x)−\lambda x=0\Leftrightarrow x \neq 0 (T−\lambda I)x=0 \Leftrightarrow ker⁡(T−\lambda I)\neq \{0\}\Leftrightarrow T−\lambda I \text{ not invertible} \Leftrightarrow \det(T - \lambda I) = 0$$(QED)

## 特徵多項式(characteristic polynomial)

> 線性轉換$$T \in L(V,V),  \lambda \in F$$ 為特徵根，定義$$f(x)=\det(T - \lambda I)$$為$$T$$的特徵多項式，記為$$char_T(x)$$。
>
> 因此$$\lambda$$為$$T$$的特徵根若且唯若$$\lambda$$為$$char_T(x)$$的根。

### 可分解(split over F)

> 多項式$$f(x) \in F(x)$$，若$$f(x)$$可完全分解成佈於$$F$$的一次因式乘積，稱$$f(x)$$在$$F$$中可分解(split over F)。

例如：

* $$f(x)=x^2+3x+2=(x+1)(x+2)$$在$$\mathbb{R}$$中可分解  。
* $$f(x)=x^2+1=(x+i)(x−i)$$在$$\mathbb{C}$$中可分解  。
* $$f(x)=x^2+1$$在$$\mathbb{R}$$中不可分解  。

## 特徵空間(eigenspace)

> 線性轉換$$T \in L(V,V),  \lambda \in F$$ 為特徵根。
>
> * 定義$$\begin{align} V(\lambda) & =\{v \in V|T(v)=\lambda v\} \\ & =\{v \in V|(T− \lambda I)(v)=0\} \\ &=ker⁡(T−\lambda I) \end{align}$$為$$T$$相對於$$\lambda$$的特徵空間。
> * 前面已證明過相對$$\lambda$$的特徵向量之線性組合，在不為零向量時 ，仍為相對$$\lambda$$的特徵向量，**因此**$$V(\lambda)$$**可視為由相對於**$$\lambda$$**之特徵向量線性組合生成的空間**。>

* $$\lambda$$為$$T$$的特徵根若且唯若$$V(\lambda) \neq \{0\}$$。
* $$\begin{align} V(\lambda) & =\{x \in F^{N \times1} |T(x)=\lambda x\} \\ & =\{x \in F^{N \times 1} |(T−\lambda I)x=0\} \\ &=ker⁡(T−\lambda I) \end{align}$$
* 所以$$x$$為$$T$$的特徵向量若且唯若$$x \in V(\lambda)−\{0\}$$。

#### 範例

* $$A=\begin{bmatrix} 2 & 1 & 0 \\ 0 & 1 & -1 \\ 0 & 2 & 4\end{bmatrix}$$
* $$\det⁡(A−\lambda I)=0$$得$$\lambda=2,3$$
* $$V(2)=ker⁡(A−2I)=ker \left(\begin{bmatrix} 0 & 1 & 0 \\ 0 & -1 & -1 \\ 0 & 2 & 2\end{bmatrix}\right)=span\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}\right\}$$
* $$V(3)=ker⁡(A−3I)=ker \left(\begin{bmatrix} -1 & 1 & 0 \\ 0 & -2 & -1 \\ 0 & 2 & 1\end{bmatrix}\right)=span\left\{ \begin{bmatrix} -1 \\ -1 \\ 2 \end{bmatrix}\right\}$$

### 特徵空間為不變子空間

> 線性轉換$$T\in L(V,V), \lambda \in F$$為$$T$$的特徵根> 。
>
> 則特徵空間$$V(\lambda)$$為$$T$$-不變子空間(即$$T(V(\lambda))\subseteq V(\lambda))$$。
>
> 註：主成分分析(PCA)利用此性質，做到資料降維的功能。

Proof:

* 因為$$V(\lambda)=ker⁡(T−\lambda I)$$, 所以$$V(\lambda)$$為$$V$$的子空間  。
* 由特徵向量定義得$$\forall u \in V(\lambda), T(u)=\lambda u$$，可得$$T(T(u))=T(\lambda u)=\lambda T(u)$$。
* 因此$$T(u) \in V(\lambda)$$  ，即$$T(V(\lambda)) \subseteq V(\lambda)$$(QED).

### 相異特徵空間為獨立子空間

> 線性轉換$$T \in L(V,V)$$且$$\lambda_1, \lambda _2, \dots ,\lambda _K \in F$$為$$T$$的$$K$$個相異特徵根，則> ：
>
> * $$V(\lambda_1 ) ,V(\lambda_2 ),\dots,V(\lambda_K )$$為[獨立子空間](../vector-space/independent-subspace-direct-sum.md#du-li-zi-kong-jian-independent-subspace) （指$$V(\lambda_i )$$無法由其它子空間生成，$$V(\lambda _i) \cap \sum_{j \neq i}V(\lambda _j) = \{0\}$$，獨立子空間保證空間兩兩獨立）。
> * $$v_i$$ 為$$T$$相對於$$\lambda_i$$的特徵向量，$$i=1,2,\dots,K$$，則$$v_1,v_2,\dots,v_k$$ 為線性獨立。>

Proof: (數學歸納法)

* $$K=1$$時，$$V(\lambda_1$$)為獨立子空間成立。
* 令$$K=r-1$$時，$$V(\lambda_1 ),\dots,V(\lambda_{r−1} )$$為獨立子空間成立。即$$V(\lambda_i )\bigcap \sum_{j \neq i} V(\lambda_j ) =\{0\}, ~ \forall i=1,2 \dots,K$$。
* 考慮$$K=r$$時，取$$v_i \in V(\lambda_i ),~ i=1,2,\dots,r$$。
* 若$$v_1+v_2+\dots+v_r=0$$，則$$0=T(0)=T(v_1+v_2+\dots+v_r )=T(v_1 )+T(v_2 )+\dots+T(v_r )=\lambda_1 v_1+\lambda_2 v_2+\dots+\lambda_r v_r$$ --(1)
* 同乘$$\lambda_r$$得：$$v_1+v_2+\dots+v_r=0 \Rightarrow \lambda_r v_1+\lambda_r v_2+\dots+\lambda_r v_r=0$$ --(2)
* (1)−(2)得 $$(\lambda_1−\lambda_r ) v_1+(\lambda_2−\lambda_r ) v_2+\dots+(\lambda_{r−1}−\lambda_r ) v_{r−1}=0$$
* 因為$$V(\lambda_1 ),\dots,V(\lambda_{r−1} )$$為獨立子空間，且$$(\lambda_i−\lambda_r ) v_i \in V(\lambda_i ),~i=1,2,\dots,r−1$$
* 所以$$(\lambda_i−\lambda_r ) v_i=0, ~i=1,2,\dots,r−1$$
* 因為$$\lambda_i \neq \lambda_r, ~i=1,2,\dots,r−1$$
* 所以$$v_i=0, ~i=1,2,\dots,r−1$$代回(1)得$$v_r=0$$ (QED)

### 相似矩陣有相同的特徵根(特徵方程式)

> 矩陣$$A,B \in F^{N \times N}$$，若$$A,B$$相似($$∃P \in F^{N \times N}  \text{ invertible } \ni AP=PB$$)，則：> $$char_A (x)=char_B (x)$$，$$A,B$$有相同特徵根> 。
>
> 但反之不成立，如$$A=I, B=\begin{bmatrix} 1 & 0 \\ 1 & 1\end{bmatrix}$$有相同特徵根，但不是相似矩陣。

Proof:

$$char_B (x)=\det⁡(B−xI)=\det⁡(P^{−1} AP−xI)=\det⁡(P^{−1} AP−P^{−1} xIP)=\det⁡(P^{−1} (A−xI)P)=\det⁡(P^{−1} )  \det⁡(A−xI)  \det⁡(P)=\det⁡(A−xI)=char_A (x)$$ (QED)

### 矩陣左乘或右乘有相同特徵根

> 矩陣$$A,B \in F^{N \times N}$$，則$$AB, BA$$有相同特徵根。

Proof:

令$$\lambda$$為$$AB$$的特徵根

* Case1:$$\lambda=0$$
* $$0=\det⁡(AB−0I)=\det⁡(AB)=\det⁡(A)  \det⁡(B)=\det⁡(BA)=\det⁡(BA−0I)$$
* Case 2: $$\lambda \neq 0$$
* $$\exists x \neq 0 \ni ABx=\lambda x \Rightarrow BABx=\lambda Bx\Leftrightarrow BA(Bx)=λ(Bx)$$
* 若$$Bx=0$$則$$A0=\lambda x$$，即$$\lambda x=0$$，與$$\lambda neq 0, x neq 0$$的假設矛盾，所以$$Bx \neq 0$$
* $$\exists Bx\neq 0 \ni BA(Bx)=\lambda (Bx)$$，因此$$\lambda$$為$$BA$$的特徵根 (QED)

## 代數重數、幾何重數(algebraic multiplicity, geometric multiplicity)

> 線性轉換$$T\in L(V,V), \lambda \in F$$為$$T$$的特徵根> 。
>
> * 定義$$\lambda$$在特徵方程式$$char_T (x)$$中的重根數為$$\lambda$$的代數重數，或簡稱為重數，記為$$m(\lambda)$$。
> * 定義$$\dim⁡(V(\lambda))$$為$$\lambda$$的幾何重數，即$$V(\lambda)$$的基底元素個數，記為$$gm(\lambda)$$>   。

* $$A \in F^{N \times N}$$，$$\lambda$$為$$A$$的一個特徵根，則  ：
  * 相異特徵根最多$$N$$個，此時所有特徵根的代數重數均為1。
  * $$gm(\lambda)=\dim⁡(V(\lambda))=\dim⁡(ker⁡(A− \lambda I) )=N−rank(A−\lambda I)$$
* $$gm(\lambda)$$為$$V(\lambda)$$中，最大獨立集的個數，即相對於$$\lambda$$的最大線性獨立特徵向量個數。

### 特徵空間的維度必小於代數重根數

> 線性轉換$$T\in L(V,V), \lambda \in F$$為$$T$$的特徵根> ，$$\dim(V)=N$$，則$$gm(\lambda) \leq m(\lambda)$$。
>
> * 若$$\lambda$$為特徵根，則$$V(\lambda) \neq \{0\}$$，可得$$gm(\lambda)=\dim⁡(V(\lambda)) \geq 1$$。
> * 因為$$char_T (x)$$最多為$$N$$次多項式，因此最多$$N$$個相異根，所以$$m(\lambda) \leq N$$。
> * 整理可得$$1 \leq gm(\lambda) \leq m(\lambda) \leq N$$。>

Proof:

* 令$$gm(\lambda)=\dim⁡(V(\lambda))=k$$。
* 因為$$V(\lambda)$$為$$T$$不變子空間，所以存在$$V$$的一組基底$$B\ni [T]_B = \begin{bmatrix}A_1 & C \\ 0 & A_2 \end{bmatrix}$$，$$A_1=[T_{V(\lambda)}  ]_{B_1}$$ 且$$B_1$$ 為$$V(\lambda)$$的基底。
* 因為$$B_1\subseteq V(\lambda)$$且$$V(\lambda)$$中除了0向量外均為$$T$$相對於$$\lambda$$的特徵向量。  所以$$B_1$$ 中的元素均為$$T$$的特徵向量。
* 因為$$A_1=[T_{V(\lambda)}  ]_{B_1}=diag\{\lambda, \dots, \lambda\}_{k \times k}=\lambda I_k$$
* 所以$$\begin{align} char_T (x) & =\det⁡([T]_B−xI) \\ &=\det\begin{bmatrix}A_1 - xI_k & C \\ 0 & A_2 -xI_{N-k}\end{bmatrix} \\ & =\det(A_1 - xI_k)\det(A_2 - xI_{N-k}) \\ & = \det(\lambda I_k - xI_k)\det(A_2 - xI_{N-k}) \\ &= (\lambda -x)^k\det(A_2 - xI_{N-k}) \end{align}$$
* 所以$$\lambda$$在$$char_T (x)$$中的重根數至少為$$k$$，即$$m(\lambda) \geq k$$ (QED)

### 特徵根與行列式、軌跡的關係

> 假設$$char_A (x)$$在$$F$$可分解，其中$$\lambda_1, \dots, \lambda_N$$ 為矩陣$$A$$的$$N$$個特徵根，其未必全相異，則$$char_A (x)=(−1)^N (x−\lambda_1 )(x−\lambda_2 )\dots(x−\lambda_N )=(\lambda_1−x)\dots(\lambda_N−x)$$
>
> 可得
>
> * $$\det⁡(A)=\lambda_1 \lambda_2 \dots \lambda_N=\prod_{i=1}^N \lambda_i$$
> * $$tr(A)=\lambda_1+\lambda_2+⋯+\lambda_N=\sum_{i=1}^N \lambda_i$$&#x20;>

Proof:

* $$\det⁡(A)=char_A (0)=\lambda_1 \lambda_2 \dots \lambda_N$$。
* $$char_A (x)$$中，$$(−x)^{N−1}$$ 的係數為$$tr(A)$$ (QED)

## 可逆矩陣之特徵根均不為0

> 矩陣$$A \in F^{N \times N}$$，若$$char_A (x)$$在$$F$$中可分解，則> ：
>
> $$A$$為可逆矩陣$$\Leftrightarrow A$$的所有特徵根均不為0。

Proof:

* 令$$\lambda_1,\dots,\lambda_N$$ 為$$A$$的特徵根（部份相同或全相異均可。）
* 由[特徵根與行列式、軌跡的關係](eigenvector.md#te-zheng-gen-yu-hang-lie-shi-gui-ji-de-guan-xi)得$$\det⁡(A)=\lambda_1 \lambda_2 \dots \lambda_N$$
* 所以$$A$$為可逆矩陣$$\Leftrightarrow \det(A) \neq 0$$，即$$\det⁡(A)=\prod_{i=1}^N \lambda_i \neq 0$$ (QED)

## 反矩陣的特徵根

> 矩陣$$A \in F^{N \times N}$$為可逆矩陣，則$$\lambda$$為$$A$$相對於向量$$x$$的特徵根$$\Leftrightarrow$$$$\frac{1}{\lambda}$$為$$A^{-1}$$相對於向量$$x$$的特徵根。
>
> 註：$$A^{−1},A$$的特徵根未必相同，但有相同的特徵向量。

Proof =>:

* 因為$$A$$為可逆矩陣，所以所有特徵根$$\lambda \neq 0$$。
* $$Ax=\lambda x, x \neq 0$$，可得$$x=Ix=A^{−1} Ax=A^{−1} (\lambda x)= \lambda A^{−1} x$$
* 所以$$A^{−1} x = \frac{1}{\lambda}x$$ (QED)

Proof <=:同上。

## Paper: Eigenvectors from eigenvalues

[陶哲軒blog](https://terrytao.wordpress.com/2019/08/13/eigenvectors-from-eigenvalues/)

> 假設$$A$$為$$\mathbb{C}^{n \times n}$$ 的 Hermitian matrix（$$A^\mathrm{H}=A$$），矩陣的特徵值為$$\lambda_1, \lambda_2 ,\dots ,\lambda_n$$，對應到的單範特徵向量分別為$$v_i \in \mathbb{C}^{n \times 1}, ~\|v_i\|=1, ~i=1,2,\dots,n.$$
>
> &#x20;令$$v_{i,j}$$ 為第$$i$$個特徵向量中的第$$j$$個元素，則：
>
> * $$\displaystyle |v_{i,j}|^2 \prod_{k=1, k \neq i}^n(\lambda _i - \lambda _k) = \prod_{k=1}^{n-1}(\lambda_i - \lambda_k(M_j))$$
> * $$M_j \in \mathbb{C}^{(n-1) \times (n-1)}$$為為矩陣$$A$$刪去第$$j$$列與第$$j$$行後剩下部分形成的Hermitian matrix。

例如$$n=3$$，可得：$$|v_{1,2}|^2 (\lambda_1 - \lambda_2)(\lambda_1-\lambda_3)=(\lambda_1 - \lambda_1(M_2))(\lambda_1 - \lambda_2(M_2))$$



