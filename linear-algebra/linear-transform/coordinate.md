# 座標化\(coordinate\)

## 簡介

座標化的功能在於將任意向量空間中的元素均使用向量的方法表示。如多項式空間，連續函數空間，只要給定基底，則函數即可表示為該基底下唯一的向量\(但可能為無窮維度的向量\)。

## 座標向量\(coordinate vector\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。
>
> 若$$v=a_1 b_1+a_2 b_2 +\dots+ a_N b_N$$，定義行向量$$x=\begin{bmatrix} a_1 \\ a_2 \\ \vdots\\ a_N\end{bmatrix}$$為向量$$v$$相對於基底$$B$$的座標向量（corrdinate vector of v relative to B），記為$$[v]_B$$。
>
> 因為向量可唯一表示為基底的線性組合，所以$$[v]_B$$存在唯一。

一般集合中的元素是無序的，但是向量為基底的元素之線性組合，若基底元素無序時，會造成對應的座標參數$$a_i$$ 不一致，因此要求基底為有序集合，即$$\{b_1,b_2,b_3\}$$與$$\{b_1,b_3,b_2 \}$$視為不同的基底。

範例

* $$V=\mathbb{R}^2, B=\{(1,0), (0,1)\} $$ \(standard basis\)
  * $$ v=(2,3)=2(1,0)+3(0,1), [v]_β=\begin{bmatrix} 2\\ 3\end{bmatrix}$$
* $$V=\mathbb{R}^2，B=\{(0,1), (1,0)\}  $$
  *  $$v=(2,3)=3(0,1)+2(1,0) ~ [v]_β=\begin{bmatrix} 3\\ 2\end{bmatrix}$$
* $$V=R_3 [x], B=\{1,(x−1), (x−1)^2 \}$$
  * $$f(x)=4+5x−7x^2=f(1)+f^{′}(x)(x−1)+\frac{f^{(2)}(1)}{2} (x−1)^2=2−9(x−1)−7(x−1)^2$$
  * 所以$$[f]_B=\begin{bmatrix} 2 \\ 9\\ 7 \end{bmatrix}$$

### 座標向量的性質

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。
>
> 則$$\forall a, b \in F, ~ u,v \in V$$：
>
> * \(座標向量為線性算子\)$$[au+bv]_B = a[u]_B + b[v]_B$$
> * \(座標向量唯一組\) $$u=v \Leftrightarrow [u]_B = [v]_B$$
> * \[給定基底，則所有元素有唯一座標\] $$\forall v \in V, \exists ! x \in F^{N \times 1} \ni [v]_B= x$$

Proof:

* 令$$u=\sum_{i=1}^N c_i b_i, ~ v=\sum_{i=1}^N d_i b_i $$
* 所以$$[u]_B=\begin{bmatrix} c_1 \\ c_2 \\ \vdots\ c_N \end{bmatrix}, ~[v]_B=\begin{bmatrix} d_1 \\ d_2 \\ \vdots \\ d_N\end{bmatrix}$$
* $$au+bv=a(\sum_{i=1}^N c_i b_i)+b(\sum_{i=1}^N d_i b_i)=\sum_{i=1}^N (ac_i+bd_i ) b_i $$
* 可得$$[au+bv]_B\begin{bmatrix}  ac_1 + bd_1 \\ ac_2 + bd_2 \\ \vdots \\ ac_N + bd_N\end{bmatrix}=a[u]_B+b[v]_B$$

 唯一性

* 取$$v=\sum_{i=1}^N x_i b_i $$，$$ x=\begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix} \in F^{ N\times 1}$$，所以$$[v]_B = \begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix} = x$$
* 若存在$$u \in  V \ni [u]_B=x$$，則 $$u=\sum_{i=1}^N x_i b_i=v$$
* 所以$$u=v$$，即座標向量的唯一性。\(QED\)

## 同構\(isomorphism\)



> $$V,W$$為定義在體$$F$$上的向量空間，若存在函數$$T:V \rightarrow W$$滿足以下三個條件時，則$$V,W$$同構，記為$$V \cong W$$。
>
> * $$T$$為線性映射：$$\forall a,b \in F, ~ u, v \in V$$, $$T(au+bv)=aT(u)+bT(v)$$。
> * $$T$$為一對一函數：$$\forall u,v \in V$$, $$T(u) = T(v) \Rightarrow u=v$$。
> * $$T$$為映成函數：$$\forall w \in W ~ \exists v \in V \ni T(v)=w$$。
>
> 註：如果$$T$$為一對一且映成的函數，則兩集合等勢$$|V|=|W|$$，因此$$T^{-1}$$存在且為函數。此處還加上了$$T$$為線性映射的限制。

## 座標同構函數\(coordinate isomorphism\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。
>
> 定義座標同構函數$$c_B: V \rightarrow F^{N \times 1}$$, $$c_B(v)=[v]_B, ~\forall v \in V$$。
>
> 此定義是要將坐標表示法視為一函數來討論向量空間$$V$$與行空間的同構性。

* 很容易得到 $$c_B (v)$$為線性同構函數，即坐標表示法所在的$$F^{N×1}$$ 空間與向量空間$$V$$同構。
* \[線性\]:$$ c_B (au+bv)=[au+bv]_B=a[u]_B+b[v]_B=ac_B (u)+bc_B (v)$$  \[一對一\] 若 $$c_β (u)=c_β (v)$$，則$$[u]_B=[v]_B$$，因為向量可由基底唯一表示，所以$$u=v$$。
* \[映成\] $$ \forall x \in F^{N\times 1}$$，令$$ v=\sum_{i=1}^N x_i b_i \in V$$，所以$$c_B (v)=[v]_B=\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_N \end{bmatrix}=x$$

###  線性獨立集經同構函數轉換仍為線性獨立集

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底。$$c_B: V \rightarrow F^{N \times 1}$$為為座標同構函數。
>
> 令$$\{ v_1, v_2, \dots, v_K\} \subseteq  V$$為線性獨立集若且唯若$$\{c_B(v_1), c_B(v_2), \dots, c_B(v_K)\}$$為線性獨立集。
>
> * 註：因為基底是最大獨立集，因此$$K \leq N$$。
> * $$v_k$$是在$$V$$中的原始形式，而$$c_B(v_k)$$是使用基底$$B$$之後轉換形式。例如多項式可用泰勒展開式表示，歐式空間的點可變換基底表示。

Proof: =&gt;

* 若$$a_1 c_B (v_1 )+\dots +a_K c_B (v_K )=0$$，因為$$c_B$$為線性函數，得$$c_B( a_1 v_1+\dots+a_K v_K )=c_B (0)$$
* 因為$$c_B$$為一對一函數，所以$$a_1 v_1+\dots+a_K v_K=0$$
* 因為$$\{v_1,v_2,\dots,v_K \}$$為線性獨立集，所以$$a_1=\dots=a_K=0$$。
* 因此$$\{c_B (v_1 ),c_B (v_2 ),\dots,c_B (v_K )\}$$為線性獨立集 \(QED\)

Proof &lt;=

* 若$$ a_1 v_1+\dots+a_K v_K=0$$
* 因為$$c_B$$為線性函數，所以$$c_B( a_1 v_1+\dots+a_K v_K)=a_1c_B(v_1)+\dots + a_K c_B(v_k)= c_B(0)=0$$
* 因為$$\{c_B (v_1 ),c_B (v_2 ),\dots ,c_B (v_K )\}$$為線性獨立集 ，所以$$a_1=\dots=a_K=0$$
* 可得$$\{v_1,v_2,\dots,v_K \}$$為線性獨立集\(QED\)

## 轉移矩陣\(transition matrix from basis B to basis R in the same vector space\) 

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$B=\{b_1, b_2,\dots, b_N\}$$為$$V$$的基底，而$$R=\{r_1, r_2, \dots, r_N\}$$為$$V$$的另一組基底，則$$\forall v \in V, ~ [v]_R=[I_V]_B^R[v]_B$$。
>
> * $$[I_V]_B^R = [[b_1]_R, [b_2]_R, \dots, [b_N]_R] \in F^{N \times N}$$稱為由基底$$B$$至$$R$$的轉移矩陣（座標轉換矩陣）。
> * $$[b_i]_R \in F^{N \times 1}$$為基底向量$$b_i$$以基底$$R$$表示的座標向量。

Proof:

* $$\forall v \in V$$，令$$v=\sum_{j=1}^N x_j b_j$$，得$$[v]_B=\begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix}$$
*  令$$ b_j=\sum_{i=1}^N p_{ij} r_i$$，因此$$[b_j]_R=\begin{bmatrix}  p_{1j} \\ \vdots \\ p_{Nj}\end{bmatrix}$$
* 因為$$\displaystyle v = \sum_{j=1}^N x_j b_j = \sum_{j=1}^N x_j \left(   \sum_{i=1}^N p_{ij} r_i\right) = \sum_{i=1}^N \left( \sum_{j=1}^N p_{ij} x_j\right) r_i$$
* 可得$$[v]_R = \begin{bmatrix} \sum_{j=1}^N p_{1j}x_j \\ \vdots \\ \sum_{j=1}^N p_{Nj}x_j\end{bmatrix} = \begin{bmatrix}  p_{11} & p_{12} & \dots & p_{1N}\\ \vdots & \vdots  & \ddots & \vdots \\ p_{N1} & p_{N2} & \dots & p_{NN} \end{bmatrix} \begin{bmatrix} x_1 \\ \vdots \\ x_N \end{bmatrix} =\begin{bmatrix} [b_1]_R & [b_2]_R& \dots & [b_N]_R \end{bmatrix} [v]_B$$

\(QED\)

#### 範例1

* $$V=\mathbb{R}^2, B=\{(1,0), (0,1)\}, R=\{(1,1), (1,−1)\}$$
* $$v=(2,4)  [v]_B=\begin{bmatrix} 2\\ 4\end{bmatrix}, [v]_R=\begin{bmatrix}3 \\ -1 \end{bmatrix}$$
* $$ [(1,0)]_R=\begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}, ~[(0,1)]_R= \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$
* 可得$$\begin{bmatrix} 3 \\-1 \end{bmatrix} = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & -0.5\end{bmatrix} \begin{bmatrix} 2 \\ 4\end{bmatrix}$$

#### 範例2



* $$V=R_2[x], ~ f(x)=3x^2 -4x+5$$
* $$B=\{ 1, x+1, (x+1)^2\}$$. $$R=\{1, x, x^2\}$$
* $$[f]_R=\begin{bmatrix} 5 \\ -4 \\ 3\end{bmatrix}$$
* 由泰勒展開式得$$\begin{align} f(x) & =f(-1)+f^{(1)}(x+1)+\frac{f^{(2)}(-1)}{2}(x+1)^2 \\ &=12- 10(x+1) + 3(x+1)^2 \end{align}$$
* 所以$$[f]_B=\begin{bmatrix} 12 \\ -10 \\ 3 \end{bmatrix}$$
* $$[1]_R = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$$, $$[x+1]_R=\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$, $$[(x+1)^2]_R=\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}$$
* 可得$$\begin{bmatrix} 5 \\ -4 \\ 3 \end{bmatrix}= \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 12 \\ -10 \\ 3 \end{bmatrix}$$

### 轉移矩陣必可逆\(在同一向量空間中\)

> $$[I_V]_B^R$$必為可逆矩陣且$$([I_V]_B^R)^{-1} = [I_V]_R^B$$
>
> * $$[I_V]_B^R = \begin{bmatrix} [b_1]_R & [b_2]_R & \dots [b_N]_R \end{bmatrix}$$
> * $$[I_V]_R^B = \begin{bmatrix} [r_1]_B & [r_2]_B & \dots [r_N]_B \end{bmatrix}$$
>
> 直觀的想法是同一空間中的元素，雖然使用不同基底時有各自的坐標向量，但是一定能換過去再換回來。
>
> * $$[v]_R = [I_V]_B^R [v]_B, ~[v]_B= [I_V]_R^B [v]_R$$
> * $$[v]_B=[I_V]_R^B[I_V]_B^R[v]_B$$
> * 可得$$[I_V]_R^B[I_V]_B^R=I_N$$

Proof:

* 因為$$B$$為$$V$$的基底，所以$$b_1,b_2,\dots,b_N$$ 線性獨立。
* 因為線性獨立集經同樣函數轉換後仍為線性獨立集，因此$$c_R (b_1 ),\dots,c_R (b_N )$$也為線性獨立。
* 因此$$[I_V]_B^R = \begin{bmatrix} [b_1]_R & [b_2]_R & \dots [b_N]_R \end{bmatrix}$$行獨立，所以\[$$I_V ]_B^R$$ 可逆。 \(QED\)

#### 範例

* $$V=\mathbb{R}^2, ~B=\{(1,0), (0,1)\}, R=\{(1,1), (1,−1)\}$$
* $$v=(2,4)  [v]_B=\begin{bmatrix} 2 \\ 4\end{bmatrix}, ~ [v]_R=\begin{bmatrix} 3 \\ -1\end{bmatrix}$$
* $$(1,0)_R = \begin{bmatrix} 0.5 \\ 0.5\end{bmatrix}, (0,1)_R= \begin{bmatrix} 0.5 \\  -0.5\end{bmatrix}$$
* $$(1,1)_B =\begin{bmatrix} 1 \\ 1\end{bmatrix}, ~ (1,-1)_B=\begin{bmatrix} 1 \\ -1\end{bmatrix}$$
* $$[I_V]_B^R [I_V]_R^B=\begin{bmatrix} 0.5 & 0.5 \\ 0.5 & -0.5\end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}$$

## 線性轉換矩陣表示法簡介

* 因為線性轉換通常發生在兩個維度不同的向量空間中，只要給定一個向量空間的基底，則線性轉換的矩陣表示法唯一決定。
* 因此方型矩陣可視為在同一空間中，使用不同基底的線性轉換表示法；而非方型矩陣可視為不同空間中，線性轉換的表示法。
* 使用矩陣表示法的好處在於可以處理不同的向量空間\(如歐式空間-&gt;連續函數空間\)的轉換，因為向量空間上的任意元素均可座標化處理為向量，因此只要用矩陣即可完成轉換。

### 線性轉換矩陣表示法\(matrix representation\)

> 令線性轉換$$T \in L(V,W)$$，$$\dim(V)=N$$，其基底為$$B=\{b_1, b_2, \dots, b_N\}$$，$$\dim(W)=M$$，其基底為$$R=\{r_1, r_2, \dots, r_M\}$$。
>
> 定義轉換矩陣$$[T]_B^R=\begin{bmatrix} [T(b_1)]_R & T(b_2)]_R  & \dots & T(b_N)]_R\end{bmatrix} \in F^{M \times N}$$為線性轉換$$T$$相對於基底$$B$$與$$R$$的矩陣表示法。
>
> 當$$W=V$$時，且$$B=R$$，$$[T]_B^B$$簡記為$$[T]_B$$。

#### 範例

* $$T \left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \right)=\begin{bmatrix}x_2 \\ -5x_1 +13x_2 \\-7x_1 +16 x_2 \end{bmatrix}: \mathbb{R}^2 \rightarrow \mathbb{R}^3$$
* 如果$$\mathbb{R}^2,\mathbb{R}^3$$ 均使用標準基底時，$$[T]=\begin{bmatrix} 0 & 1 \\-5 & 13 \\-7 & 16 \end{bmatrix} $$
  * 取$$v=(1,1)$$, $$[v]_{\mathbb{R}^2} = \begin{bmatrix} 1 \\ 1\end{bmatrix}$$, $$[T(v)]_{\mathbb{R}^3} = \begin{bmatrix} 1 \\ 8 \\ 9\end{bmatrix}$$
  * $$\begin{bmatrix} 1 \\ 8 \\ 9\end{bmatrix} = \begin{bmatrix} 0 & 1 \\-5 & 13 \\-7 & 16\end{bmatrix} \begin{bmatrix} 1 \\ 1\end{bmatrix}$$

### 一般化的座標變換公式

> 令線性轉換$$T \in L(V,W)$$，$$\dim(V)=N$$，其基底為$$B=\{b_1, b_2, \dots, b_N\}$$，$$\dim(W)=M$$，其基底為$$R=\{r_1, r_2, \dots, r_M\}$$。
>
> 則$$\forall v \in V, [T(v)]_R = [T]_B^R[v]_B$$
>
> 當$$V=W$$時，$$[v]_R = [I_V]_B^R [v]_B$$，即取$$T=I_V$$。







