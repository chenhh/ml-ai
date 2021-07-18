# Jordan form

## 簡介

* Jordan form是判斷矩陣$$A$$與$$B$$是否相似\($$A \sim B \equiv \exists P \text{ invertiable } \ni AP=PB$$\)的唯一充要條件。
* 所有方陣都唯一存在Jordan form（依定義可能為上移或下移矩陣），比可對角化矩陣性質適用範圍更大。
* Jordan form矩陣$$J$$的形狀與原始矩陣$$A$$的大小相同。
* 如果線性轉換$$T$$的所有特徵根的代數重數（特徵向量的重根數）均為1\($$m(\lambda_i )=1, \forall i$$\)，即此線性轉換可對角化，則此線性轉換的Jordan form為特徵根形成的對角矩陣$$D$$。因此可對角化矩陣為Jordan form的特例。

## 0特徵根與核空間的關係

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N<\infty$$。
>
> 若$$\dim⁡(\bigcup_{i=1}^\infty  ker⁡(T^i ) )=M$$，則：
>
> 1. 若$$M=0$$，則0不為$$char_T (x)$$的根\(因為$$ker⁡(T^i )=\{0\}, \forall i$$，因此$$T$$可逆，所以$$T$$的所有特徵根均不為0\)   。
> 2. 若$$M \geq 1$$，則0為$$char_T (x)$$的$$M$$重根。

Proof \(1\):

* 令$$W_1=\bigcup_{i=1}^\infty  ker⁡(T^i )  $$
* 根據kernel chain theorem，存在最小正整數$$k$$使得$$W_1=ker⁡(T^k )$$
* 令$$W_2=R(T^k)$$，則根據fitting引理得$$V=ker⁡(T^k ) \oplus R(T^k )=W_1 \oplus W_2$$
* 因為$$m=0$$，得$$\dim⁡(ker⁡(T^k ) )=0$$，因此$$ker⁡(T^k )=\{0\}$$。
* 因為$$\{0\} \subseteq ker⁡(T) \subseteq ker⁡(T^k )=\{0\}$$
* 所以$$k=1$$，得$$ker⁡(T)=\{0\}$$
* 因此$$T$$為可逆函數，即$$\det⁡(T) \neq 0$$，得$$char_T (0)=\det⁡(T−0I) \neq 0$$
* 所以0不為$$T$$的特徵根 \(QED\)

Proof \(2\)

* 取$$B_1,B_2$$ 分別為$$W_1,W_2$$ 的基底，因為$$V=ker⁡(T^k ) \oplus R(T^k )$$，所以$$V$$的基底$$b=b_1 \cup B_2$$  \(直和空間的性質\)
* 根據直和空間與$$T$$不變子空間的性質與fitting引理得$$[T]_B=\begin{bmatrix} A_1 & 0 \\ 0 & A_2 \end{bmatrix}$$，$$ A_1=[T_{w_1} ]_{B_1}$$ 為冪零矩陣，$$A_2=[T_{w_2} ]_{B_2}$$ 為可逆矩陣  。
* $$char_(A_1 ) (x)=\det⁡(A_1−xI)=(−1)^M x^M$$
* $$g(x)=char_(A_2 ) (x)=det⁡(A_2−xI) $$
* 因為$$A_2$$為可逆矩陣，所以$$A_2$$ 不含0的特徵根，即$$g(0) \neq 0$$。
* $$char_T (x)=\det⁡(T - xI)=\begin{vmatrix} A_1 - xI & 0 \\0 & A_2 - xI \end{vmatrix}=(−1)^M x^M g(x) $$
* 因為$$g(0) \neq 0$$，所以0為$$char_T (x)=0$$的$$M$$重根 \(QED\).

## 特徵方程式的重根性質

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N<\infty$$，則：
>
> * $$\lambda$$不為$$char_T (x)$$的根$$\Leftrightarrow$$0不為$$char_{T− \lambda I} (x)$$的根。
> * $$\lambda$$為$$char_T (x)$$的$$M$$重根$$\Leftrightarrow $$0為$$char_{T− \lambda I} (x)$$的$$M$$重根。

Proof:

* $$\lambda$$不為$$char_T (x)$$的根$$\Leftrightarrow char_T (\lambda)=\det⁡(T−\lambda I) \neq 0\Leftrightarrow char_(T−\lambda I) (0)=\det⁡(T−\lambda I−0I) \neq 0$$$$\Leftrightarrow 0$$不為$$char_(T−\lambda I) (x)$$的根 \(QED\)
* $$\lambda$$為$$char_T (x)$$的$$M$$重根$$\Leftrightarrow \det⁡(T−xI)=(x−\lambda)^M g(x), g(λ) \neq 0\Leftrightarrow \det⁡(T−(y+\lambda)I)=y^M h(y), y=(x−\lambda), h(0) \neq 0\Leftrightarrow \det⁡((T−\lambda I)−yI)=y^M h(y)$$$$\Leftrightarrow 0$$為$$char_{T−\lambda I} (x)$$的$$M$$重根 \(QED\)

##  廣義特徵空間的性質

> 線性轉換$$T \in L(V,V), ~\dim⁡(V)=N<\infty$$。
>
> $$\lambda$$為$$T$$的特徵根，$$W=\bigcup_{i=1}^\infty  ker⁡((T−\lambda I)^i ),~\dim⁡(W)=M$$，則：
>
> * $$\lambda$$為$$char_T (x)$$的$$M$$重根，即$$m(\lambda)=M$$\(重根數$$m(\lambda)$$等於特徵向量空間$$K(\lambda)$$的維度\)  。
> * $$(T−\lambda I)_W$$ 為冪零算子  。

Proof:

* 因為$$T−\lambda I \in L(V,V)$$，根據前述定理將$$T$$換成$$T−\lambda I$$得0為$$char_{T−λI} (x)=0$$的$$M$$重根。
* 所以$$\lambda$$為$$char_T (x)=0$$的$$M$$重根，即$$m(\lambda)=M$$ \(QED\)
* 由kernel chain theorem可知$$(T−\lambda I)_W$$ 為冪零算子 \(QED\)

## 給定特徵根之廣義特徵空間及廣義特徵向量\(generalized eigenspace and eigenvector\)

> 線性轉換$$T \in L(V,V)$$，$$\lambda$$為$$T$$的特徵根。
>
> * 定義$$K(\lambda)=\bigcup_{i=1}^\infty  ker⁡((T−\lambda I)^i )$$為$$T$$相對於$$\lambda$$的廣義特徵空間\(generalized eigenspace\)  。
> * 一般的特徵空間是$$V(\lambda)=ker(T-\lambda I)$$，為$$K(\lambda)$$的特例，可得$$V(\lambda) \subseteq K(\lambda)$$。
>   *  也可定義成 $$K(\lambda)=\{v \in V|(T−\lambda I)^p (v)=0 \}$$, for some $$p \in \mathbb{N}$$。
> *  若$$0\neq v \in K(\lambda)$$，則稱$$v$$為$$T$$相對於$$λ$$的廣義特徵向量\(generalized eigenvector\)
>   * 也可定義為$$(T−\lambda I)^p (v)=0$$，for some $$p \in \mathbb{N}$$。

> $$A \in F^{N \times N}$$, $$\lambda$$為$$A$$的特徵根。
>
> * 定義$$K(\lambda )=\bigcup_{i=1}^\infty  ker⁡((A−\lambda I)^i )$$為$$A$$相對於$$\lambda$$的廣義特徵空間  。
> * 若$$0 \neq x \in K(\lambda)$$，則稱$$x$$為$$A$$相對於$$\lambda$$的廣義特徵向量。

* 若$$0 \neq v \in V(\lambda)$$，即$$v$$為$$T$$相對於$$\lambda$$的特徵向量，因為$$V(\lambda) \subseteq K(\lambda) \Rightarrow v \in K(\lambda)$$，即$$v$$為$$T$$相對於$$\lambda$$的廣義特徵向量。
* 假設$$\dim⁡(V)=N  $$

  * 由kernel chain theorem知$$ker⁡(T−\lambda I) \subseteq ker⁡〖(T−\lambda I)^2 \subseteq \dots$$
  * 且存在最小正整數$$k \ni ker⁡((T−\lambda I)^k )=ker⁡((T−\lambda I)^{k+1} )=\dots$$
  * 所以$$K(\lambda)=\bigcup_{i=1}^\infty  ker⁡((T−\lambda I)^i )=ker⁡((T−\lambda I)^k )=ker⁡((T−\lambda I)^{k+1} )=\dots$$
  * 因為$$k \leq N$$，所以$$K(\lambda)=ker⁡((T−\lambda)^N )$$

### 廣義特徵空間為向量空間且為T不變子空間

> 線性轉換$$T \in L(V,V)$$，$$\lambda$$為$$T$$的特徵根，則：
>
> * $$K(\lambda)$$為$$V$$的子空間 \($$\forall u,v \in K(\lambda), c \in F \Rightarrow cu+v \in K(\lambda)$$\)
> * $$K(\lambda)$$為$$T$$不變子空間\($$T(K(\lambda)) \subseteq K(\lambda)$$\)

>

### 

### 













