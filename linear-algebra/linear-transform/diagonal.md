# 對角化 (diagonal)

## 可對角化 (diagonalizable)

> 線性轉換$$T \in L(V,V)$$。
>
> * 若存在$$V$$的一組基底$$B$$使得$$[T]_B=D$$為對角矩陣，則稱$$T$$可對角化。
> * $$A\in F^{ N \times N}$$，若存在可逆矩陣$$P \in F^{N\ \times N}$$ 使得$$P^{−1} AP=D$$為對角矩陣，則稱$$A$$可對角化，且$$A$$與$$D$$相似。
> * &#x20;因此若$$A$$為可對角化矩陣，則$$A$$與對角矩陣$$D$$相似。

### 可對角化方陣必可分解為特徵向量矩陣與特徵根形成的對角矩陣&#xD;

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N$$且$$B$$為$$V$$的基底，則> ：
>
> * $$[T]_B$$ 為對角矩陣若且唯若基底$$B$$中的元素均為$$T$$的特徵向量>   。（特徵向量可做為基底）
> * $$A \in F^{N \times N}$$且$$P \in F^{N \times N}$$ 為可逆矩陣則>   $$P^{−1} AP=D$$為對角矩陣若且唯若$$P$$的行向量均為$$A$$的特徵向量>   。
> * 因要求$$P$$可逆，因此所有特徵向量必須線性獨立。
> * 若$$A$$的特徵向量並非全部線性獨立時，則$$A$$不可對角化。>

Proof:

* 令$$B=\{b_1,b_2,\dots,b_N \}$$為$$V$$的基底，所以$$b_i \neq 0, \forall i$$。
* 若$$[T]_B=D=diag\{\lambda_1, \lambda_2, \dots, \lambda_N\}$$，則$$T(b_1)=\lambda_1 b_1, \dots, T(b_N) = \lambda_N b_N$$，因此$$b_i$$為$$T$$相對於$$\lambda_i$$的特徵向量，反之也可得到相同結論(QED)。
* 令$$P=\begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix} \in F^{N \times N}$$
* &#x20;因為$$P$$為可逆矩陣，所以$$0 \neq v_i \in F^{N \times 1}, i=1,2,\dots ,N$$。
* $$P^{−1} AP=D=diag\{\lambda_1, \lambda_2, \dots, \lambda_N\} \Leftrightarrow AP=PD$$
* 得$$A\begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix}= \begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix}diag\{\lambda_1, \lambda_2, \dots, \lambda_N\}$$
* 因此$$\begin{bmatrix}Av_1 &A v_2 &  \dots Av_N \end{bmatrix} = \begin{bmatrix} \lambda_1 v_1 & \lambda_2 v_2 &  \dots \lambda_N v_N \end{bmatrix}$$  (QED)

### 可對角化的充要條件

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N$$。
>
> 令$$\lambda_1, \lambda_2, \dots, \lambda_r$$為$$T$$的相異特徵根，則以下條件等價：
>
> 1. $$T$$可對角化。
> 2. $$char_T (x)$$在$$F$$中可分解，且$$gm(\lambda_i )=m(\lambda_i ),~ i=1,2,\dots,r$$(代數重數等於幾可重數，只須檢驗$$m(\lambda_i ) \geq 2$$的特徵根其特徵空間維度是否相等即可)。>    可想成$$m(\lambda_i ) \geq 2$$的特徵根，因為在對角矩陣佔了$$m(\lambda_i )$$個元素，因此必須有相同數量個特徵向量才能形成可逆矩陣$$P$$。
> 3. $$V= V(\lambda_1) \oplus V(\lambda_2) \oplus \dots \oplus V(\lambda_r)$$為特徵空間的直和空間。

Proof (1)->(2)

* 因為$$T$$可對角化 ，所以存在$$V$$的一組基底$$B \ni [T]_B=D$$為對角矩陣。
* 令$$D=diag\{ \lambda_1 I_{m_1}, \dots, \lambda_r I_{m_r}\}$$ ，其中$$m_1+\dots+m_r=N$$。
* 所以基底$$B$$中的元素是由$$T$$的特徵向量所組成。
* 令$$B=B_1 \cup B_2 \cup \dots \cup B_r$$，$$B_i=\{v_{i,1},⋯v_{i,m_i} \}$$為$$B$$中包含相對於特徵根$$\lambda_i$$之$$m_i$$個特徵向量，$$i=1,2,\dots,r$$。
* $$\begin{align}  char_T (x) & =char_D (x)\\ &=\det (diag\{ (\lambda_1-x)I_{m_1}, \dots, \lambda_r-x)I_{m_r} \})\\ &=(\lambda_1−x)^{m_1} (\lambda_2−x)^{m_2 }\dots (\lambda_r−x)^{m_r}  \end{align}$$
* 所以$$char_T (x)$$在$$F$$中可分解且$$m(\lambda_i )=m_i, ~i=1,2,\dots,r$$  。
* 因為已知$$gm(\lambda_i ) \leq m(\lambda_i)$$，只須證明$$m(\lambda_i )\leq gm(\lambda_i )$$。
* 因為$$B$$為線性獨立集，所以$$B_i$$ 為線性獨立集
* 因為$$B_i \subseteq V(\lambda_i )$$且基底為最大線性獨立集，所以$$m(\lambda_i )=m_i=|B_i |\leq \dim⁡(V(\lambda_i ))=gm(\lambda_i ), i=1,2,\dots, r$$ (QED)

Proof (2)->(3)

* 因為$$V(\lambda_1 ),\dots,V(\lambda_r )$$為獨立子空間，所以只須證明$$V=V(\lambda_1 )+\dots+V(\lambda_r )$$。
* 因為$$V(\lambda_i )$$為$$V$$的子空間，所以$$V(\lambda_1 )+\dots+V(\lambda_r$$ )為$$V$$的子空間，即$$V(\lambda_1 )+\dots+V(\lambda_r ) \subseteq V$$。
* 因此只要證明$$\dim(V)=\dim⁡(V(\lambda_1 )+\dots+V(\lambda_r ))$$  ($$W$$為$$V$$子空間且$$\dim⁡(W)=\dim(V)\Leftrightarrow W=V$$)
* 因為$$V(\lambda_1 ),\dots,V(\lambda_r )$$為獨立子空間
* $$\begin{align} \dim⁡(V(\lambda_1 )+\dots+V(\lambda_r )) &=\dim⁡(V(\lambda_1 ))+\dots+\dim⁡(V(\lambda_r ))\\ &=gm(\lambda_1 )+\dots+gm(\lambda_r )\\ &=m(\lambda_1 )+\dots+m(\lambda_r )\\&=\dim⁡(V) \end{align}$$ (QED)

Proof (3)->(1)

* 因為$$V=V(\lambda_1 ) \oplus V(\lambda_2 )\oplus \dots \oplus V(\lambda_r )$$，且$$V(\lambda_i )$$為$$T$$不變子空間。
* 令$$B_i$$ 為$$V(\lambda_i )$$的一組基底，所以$$B=B_1 \cup \dots\cup B_r$$ 為$$V$$的一組基底，且根據不變子空間的特性，可得
* $$[T]_B = diag\{A_1, \dots, A_k\}$$
  * $$A_i = [T_{V(\lambda_i)}]_{B_i}=diag\{\lambda_i, \dots, \lambda_i\}_{m_i \times m_i} = \lambda_i I_{m_i}$$
  * $$\dim(V(\lambda_i)) \equiv gm(\lambda_i)=m(\lambda_i), ~i=1,2,\dots, k$$
* 所以$$[T]_B=diag\{ \lambda_1 I_{m_1}, \dots \lambda_r I_{m_r}\}$$為對角矩陣 (QED)

#### 範例

* $$A=\begin{bmatrix}  0 & 0 & -2 \\ 1 & 2 & 1 \\ 1 & 0 & 3 \end{bmatrix}$$, $$char_A(x)=-(x-1)(x-2)^2$$
* 檢查$$\lambda=2$$
* $$rank(A-2I) = rank\begin{bmatrix}  -2 & 0 & -2 \\ 1 & 20& 1 \\ 1 & 0 & 1 \end{bmatrix} = 1$$
* 所以$$gm(2)=\dim(ker(A-2I))=3-1=2$$
* 且$$m(2)=2$$
* 所以$$A$$可對角化。

### 全相異特徵根矩陣必可對角化

> 矩陣$$A \in F^{N \times N}$$，若$$A$$有$$N$$個相異的特徵根，則$$A$$可對角化。
>
> 註：可對角化矩陣不一定有相異特徵根，只要相同的特徵根符合$$gm(\lambda_i )=m(\lambda_i )$$的條件即可。>

proof:

* 因為$$1 \leq gm(\lambda_i ) \leq m(\lambda_i ) \leq N,  ~i=1,2,\dots,N$$
* 且$$m(\lambda_1 )+m(\lambda_2 )+\dots+m(\lambda_N )=N$$
* 所以$$gm(\lambda_i )=1=m(\lambda_i ), ~\forall i$$
* 因此$$A$$可對角化。(QED)

### 對角化範例

#### 矩陣

* $$A=\begin{bmatrix}  8 & 0 & 3\\ 2 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix}$$, $$char_A(x)=\det(A-xI)=-(x-2)^2(x-9)$$
* $$V(2) = ker(A-2I) = ker \begin{bmatrix}  6 & 0 & 3\\ 2 & 0 & 1 \\ 2 & 0 & 1 \end{bmatrix} = span \left\{  \begin{bmatrix} -1 \\ 0 \\ 2\end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} \right\}$$
* $$V(9) = ker(A-9I) = ker \begin{bmatrix}  -1 & 0 & 3\\ 2 & -7 & 1 \\ 2 & 0 & -6 \end{bmatrix} = span \left\{  \begin{bmatrix} 3 \\ 1 \\ 1\end{bmatrix}  \right\}$$
* 取$$P=\begin{bmatrix}  -1 & 0 & 3\\ 0 & 1 & 1 \\ 2 & 0 & 1 \end{bmatrix}$$，則$$P^{-1}AP=D= diag\{ 2, 2, 9\}$$。

#### 線性轉換

* $$T:F_2 [x]→F_2 [x]$$
* $$T(a_0+a_1 x+a_2 x^2 )=a_2+a_1+a_0 x^2$$
* 取基底$$B=\{1,x,x^2 \}$$，$$T(1)=x^2,T(x)=x, T(x^2 )=1$$
* $$A=[T]_B=[[T(b_1 )]_B,[T(b_2 )]_B,[T(b_3 )]_B ]=\begin{bmatrix}  0 & 0 & 1 \\ 0 & 1 & 0 \\1 & 0 & 0\end{bmatrix}$$
* $$char_A(x)=\det(A-xI)=-(x+1)(x-1)^2$$
* $$V(-1)=ker(A+I)=ker \begin{bmatrix}  1 & 0 & 1 \\ 0 & 2 & 0 \\1 & 0 & 1\end{bmatrix} = span\left\{ \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix} \right\}$$
* 因為$$\begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}  = [1-x^2]_B$$，所以$$1-x^2$$為$$T$$相對於$$-1$$的特徵向量。
* $$V(1)=ker(A-I)=ker \begin{bmatrix}  -1 & 0 & 1 \\ 0 & 0 & 0 \\1 & 0 & -1\end{bmatrix} = span\left\{ \begin{bmatrix} 1 \\ 0 \\ 1\end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}  \right\}$$
* $$\begin{bmatrix} 1 \\ 0 \\ 1\end{bmatrix} = [1+x^2]_B$$，$$\begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix}=[x]_B$$
* 所以$$1+x^2, x$$為$$T$$相對於$$1$$的兩個特徵向量。
* 即$$1-x^2, 1+x^2, x$$為$$T$$的三個線性獨立特徵向量。
* 取$$R=\{ 1-x^2, 1+x^2, x \}$$，則$$[T]_R = diag\{-1, 1, 1\}$$為對角矩陣。

## 函數以矩陣為參數

* 給定對角矩陣$$D=diag\{\lambda_1, \dots, \lambda_N\} = \begin{bmatrix}  \lambda_1 & 0 & \cdots & 0  \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_N \end{bmatrix}$$，可得$$D^k = diag\{\lambda_1^k, \dots, \lambda_N^k\}, ~\forall k \in \mathbb{N}$$。
* 對角矩陣線性性質$$\forall c,d \in F, ~cD+dI=diag\{c\lambda_1 + d, \dots, c\lambda_N +d\}$$。
* 則函數參數為矩陣時，$$f(D)=diag\{f(\lambda_1), \dots, f(\lambda_N)\}, ~\forall f \in F[x]$$，即把$$\lambda_1, \dots , \lambda_N$$代入多項式函數後，得到的值形成的對角矩陣。

### 對角矩陣函數可對角化

> 若矩陣$$A \in F^{N \times N}$$ 可對角化（$$P^{-1}AP=D$$），$$f(x)\in F[x]$$為多項式，則$$f(A)$$可對角化> 。

> 此定理提供了計算$$f(A)$$的方法> ：
>
> * 首先將矩陣$$A$$對角化，得$$A=PDP^{−1}$$
> * 則$$f(A)=Pf(D) P^{−1}$$
>
> 如果$$A$$可對角化，則$$A^k=(PDP^{-1})^k=PD^kP^{-1}$$。
>
> 可推廣至Tayler series：
>
> * $$f(x)=e^x=\sum_{i=0}^\infty \frac{x^i}{i!}$$
> * $$e^A=Pe^DP^{-1} = P diag\{ e^{\lambda_1}, \dots, e^{\lambda_N} \}P^{-1}$$

Proof:

* 令$$f(x)=\sum_{i=0}^K a_i x^i$$
* 因為矩陣$$A$$可對角化，，所以存在可逆矩陣$$P \ni P^{−1} AP=D=diag\{\lambda_1, \dots, \lambda_N\}$$。
* 移項得$$A=PDP^{-1}$$
* $$\begin{align} f(A) & =\sum_{i=0}^K a_i A^i \\& =\sum_{i=0}^K a_i (PDP^{−1} )^i \\ &=\sum_{i=0}^K a_i PD^i P^{−1} \\ & =P(\sum_{i=0}^K a_i D^i) P^{−1} \\ &=Pf(D) P^{−1}  \end{align}$$ (QED).

同步對角化(simultaneously diagonal)


> 線性轉換$$T, U \in L(V,V)$$。若存在$$V$$的一組基底$$B \ni [T]_B=D_1$$ 為對角矩陣，且$$[U]_B=D_2$$ 也為對角矩陣，則稱$$T,U$$可同步對角化(simultaneously diagonalizable)>

> 矩陣$$A,B \in F^{N \times N}$$，若存在一可逆矩陣$$P\in F^{N \times N}  \ni P^{−1} AP=D_1$$ 為對角矩陣，且$$P^{−1} BP=D_2$$ 也為對角矩陣，則稱$$A,B$$可同步對角化。>

同步對角化討論的是兩個不同的矩陣$$A,B$$，可使用相同的特徵向量（但特徵值可能不完全相等）形成的可逆矩陣$$P$$做對角化。

* 若$$A,B$$可同步對角化，則$$A,B$$可對角化，反之未必成立。
* 若$$A$$或$$B$$不可對角化，則$$A,B$$不可同步對角化。
* 因此同步對角化為對角化的子集合。

### 可同步對角化的必要條件

> 線性轉換$$T,U\in L(V,V)$$，若$$T,U$$可同步對角化，則$$TU=UT$$。
>
> 矩陣$$A,B\in F^{N \times N}$$，若$$A,B$$可同步對角化，則$$AB=BA$$。>

$$A=\begin{bmatrix} 1& 0 \\ 0 & 1 \end{bmatrix}, ~B=\begin{bmatrix} 1 & 0 \\ 1 & 1\end{bmatrix}, AB=BA$$，但$$B$$不可對角化，因此$$A,B$$不可同步對角化。

Proof:

* 因為$$T,U$$可同步對角化
* 所以存在$$V$$的基底$$b \ni [T]_B=D_1, [U]_B=D_2$$均為對角矩陣。
* 所以$$[TU]_B=[T]_B [U]_B=D_1 D_2=D_2 D_1=[U]_B [T_B ]=[UT]_B$$
* 所以$$UT=UT$$(QED).

### 可同步對角化的充要條件

> * 線性轉換$$T,U \in L(V,V)$$，$$T,U$$皆可對角化>   ，則：
>   * $$T,U$$可同步對角化$$\Leftrightarrow TU=UT$$
> * 矩陣$$A,B \in F^{N \times N}$$，$$A,B$$皆可對角化>   ，則：
>   * $$A,B$$可同步對角化$$\Leftrightarrow AB=BA$$

Proof <=

* 為$$T$$可對角化，所以$$V=V(\lambda_1 )\oplus \dots \oplus V(\lambda_r )$$， $$\lambda_1, \dots, \lambda_r$$ 為$$T$$的相異特徵根  。
* 由特徵根定義得$$\forall v \in V(\lambda_i )\Rightarrow T(v)=\lambda_i v$$。
* 所以$$T(U(v))=U(T(v))=U(\lambda_i v)=\lambda_i U(v)\Rightarrow U(v) \in V(\lambda_i )$$
* 可得$$U(V(\lambda_i )) \subseteq V(\lambda_i )$$，即$$V(\lambda_i )$$為$$U$$不變子空間。
* 因為$$U$$可對角化，所以$$U_{V(\lambda_i )}$$  可對角化，即$$U$$可用$$T$$的特徵向量對做對角化，因此$$T,U$$可同步對角化(QED)。