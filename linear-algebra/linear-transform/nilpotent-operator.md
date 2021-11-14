# 冪零算子(nilpotent operator)

* 冪零算子討論經有限次相同線性轉換後，可使得所有向量空間$$V$$中元素變為$$0$$的線性轉換。
* 投影算子討論的是經過一次投影後，則值域不再變化的算子。

## 冪零算子(nilpotent operator)

> 線性轉換$$T \in L(V,V)$$，若存在$$k \in \mathbb{N} \ni T^k=0$$，即$$\forall v \in V, ~ v \in ker⁡(T^k )$$，則稱$$T$$為冪零算子(nilpotent operator) $$k^*=\arg\min_k\{T^k (v)=0, \forall v \in V, k \in \mathbb{N}\}$$為$$T$$的指標(index)。
>
> 矩陣$$A \in F^{N \times N}$$，若存在$$k \in \mathbb{N} \ni A^k=0$$，則稱$$A$$為冪零矩陣(nilpotent matrix)，且稱$$k^{*} =\arg\min_k \{A^k=0,  k \in\mathbb{N}\}$$為$$A$$的指標(index)。

* 依定義得零矩陣為具指標1的冪零矩陣。
* 單位矩陣$$I^k \neq 0, ~\forall k \in \mathbb{N}$$，所以非冪零矩陣。
* 若$$A$$為$$N \times N$$嚴格上三角（下三角）矩陣，則$$A^N=0$$。
  * $$A=\begin{bmatrix} 0 & 1 & 2\\    0 & 0 & 3\\ 0 & 0 & 0  \end{bmatrix}$$    ，$$A^2=\begin{bmatrix} 0 & 0 & 3\\    0 & 0 & 0\\ 0 & 0 & 0  \end{bmatrix}$$，$$A^3=\begin{bmatrix} 0 & 0 & 0\\    0 & 0 & 0\\ 0 & 0 & 0  \end{bmatrix}$$
* 若$$T$$為冪零算子，且$$B$$為$$V$$的一組基底，則$$[T]_B^k = [T^k]_B=[0]_B=0$$，即$$[T]_B$$為冪零矩陣。

### 冪零算子的性質

> 線性轉換$$T \in L(V,V)$$，則下列敘述等價> ：
>
> 1. $$T$$為具有指標$$k$$的冪零算子
> 2. $$T^k=0$$且$$T^{k−1} \neq 0$$。
> 3. $$ker⁡(T^K )=V$$，$$ker(T^(k−1) ) \neq V$$
> 4. $$\forall v \in V, T^k (v)=0$$且$$\exists u \in V \ni T^(k−1) (u) \neq 0$$>

### 冪零矩陣與可逆矩陣

> 若$$A \in F^{N \times N}$$ 為冪零矩陣，則$$I−A$$為可逆矩陣。

Proof:

* 因為$$A$$為冪零矩陣，所以$$\exists k \in \mathbb{N}\ni A^k=0$$
* 所以$$(I−A)(I+A+A^2+\dots+A^{k−1})=I−A^k=I$$ (QED)

## &#x20;下移矩陣

> 定義$$S_k=\begin{bmatrix} 0 & 0 & 0&\dots & 0 \\ 1 & 0 & 0 & \dots & 0 \\    0 & 1& 0 & \ddots & 0 \\  0 & 0 &1 & \dots & 0 \\\end{bmatrix}_{k \times k}$$，為$$k$$階下移矩陣，$$[S_k]_{ij}=1, ~\forall i=j+1$$且$$[S_k]_{ij}=0, ~\forall i\neq j+1$$。
>
> 即$$S_k$$ 為只有主對角線左斜下方第一排為1，其餘為0的$$k\times k$$方陣。
>
> 定義$$S_k$$ 的轉置矩陣$$S_k^\top=\begin{bmatrix} 0 & 1 & 0&\dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\    0 & 0& 0 & \ddots & 1 \\  0 & 0 &0 & \dots & 0 \\\end{bmatrix}_{k \times k}$$ 為$$k$$階上移矩陣> 。

### 下移矩陣為冪零矩陣

* $$S_4 = \begin{bmatrix}    0 & 0 & 0 & 0 \\   1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$，$$S_4^2=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}$$，$$S_4^3=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{bmatrix}$$，$$S_4^4=\begin{bmatrix}    0 & 0 & 0 & 0 \\   0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
* 可得到$$S_k$$ 下移矩陣為具有指標$$k$$的冪零矩陣。  同理可得$$S_k^\top$$ 上移矩陣為具有指標$$k$$的冪零矩陣。

## 局部冪零、局部可逆

> 線性轉換$$T \in L(V,V)$$，$$W$$為$$T$$-不變子空間 ($$W$$為子空間且$$T(W) \subseteq W$$)
>
> * 若$$T_W$$ 為冪零算子，則稱$$T$$在$$W$$上局部冪零(locally nilpotent on W)>   。
> * 若$$T_W$$ 為可逆算子，則稱$$T$$在$$W$$上局部可逆(locally invertible on W)>   。

* 取$$W=ker⁡(T)$$為$$T$$不變子空間。因為$$\forall v \in W, T(v)=0$$，所以$$T_W=0$$為冪零，因此$$T$$在$$ker⁡(T)$$上必為局部冪零。
* 若$$T$$為冪零算子，則$$V$$為最大冪零區。  （$$\exists k \in \mathbb{N}, \forall v \in V, T^k(v)=0$$）
* 若$$T$$為可逆算子，則$$V$$為最大可逆區。

### 一般線性轉換核空間會越來越大，值域會越來越小

> 線性轉換$$T \in L(V,V)$$，則> ：
>
> * $$ker⁡(T^i ) \subseteq ker(T^{i+1}),\  \forall i \in \mathbb{N}$$
> * $$R(T^i ) \supseteq R(T^{i+1} ),\  \forall i \in \mathbb{N}$$>

Proof:

* $$\forall v \in ker⁡(T^i ),~ T^i (v)=0$$
* $$T^{i+1} (v)=T(T^i (v))=T(0)=0$$
* 所以$$v \in ker⁡(T^{i+1} )$$  (QED)
* $$\forall v \in R(T^{i+1} )~\exists u \in V \ni v=T^{i+1} (u)$$
* $$v=T^i (T(u)), ~T(u) \in V$$
* 所以$$v \in R(T^i )$$  (QED)

### 核空間經線性轉換後不再增大時，值域經線性轉換也不會縮小

> 線性轉換$$T \in L(V,V), k \in \mathbb{N}$$，則：
>
> $$ker⁡(T^k )=ker⁡(T^{k+1} )$$若且唯若$$R(T^k )=R(T^{k+1} )$$

Proof:

* By [rank-nullity theorem](kernel-space-and-image.md#wei-du-ding-li-sylvester-1st-law-or-dimension-theorem-ranknullity-theorem),
* 因為$$T^k \in L(V,V)$$，所以$$\dim⁡(V)=nullity(T^k )+rank(T^k )$$。
* 因為$$T^{k+1} \in L(V,V)$$，所以$$\dim⁡(V)=nullity(T^{k+1} )+rank(T^{k+1} )$$。
* 若$$ker⁡(T^k )=ker⁡(T^{k+1} ) \Leftrightarrow nullity(T^k )=nullity(T^{k+1})$$\[因為$$ker⁡(T^k )$$為$$ker⁡(T^{k+1} )$$的子空間] $$\Leftrightarrow rank(T^k )=rank(T^{k+1} )\Leftrightarrow R(T^k )=R(T^{k+1} )$$\[因為$$R(T^{k+1} )$$為$$R(T^k )$$的子空間] (QED)

### 核空間經線性轉換後不再增大時，則不會再增大；值域經線性轉換不再縮小時，則不會再縮小

> 線性轉換$$T \in L(V,V), ~ k \in \mathbb{N}$$，則：
>
> * $$ker⁡(T^k )=ker⁡(T^{k+1} ) \Rightarrow ker⁡(T^{k+1} )=ker⁡(T^{k+2} )$$
> * $$R(T^k )=R(T^{k+1} )\Rightarrow R(T^{k+1} )=R(T^{k+2} )$$

Proof:

* 因為$$ker⁡(T^{k+1} ) \subseteq ker⁡(T^{k+2} )$$. 所以只需證明$$ker⁡(T^{k+1} )\supseteq ker⁡(T^{k+2} )$$
* $$\forall v \in ker⁡(T^{k+2} ), T^{k+2} (v)=T^{k+1} (T(v))=0\Rightarrow  T(v) \in ker⁡(T^{k+1} )$$
* 因為$$ker⁡(T^k )=ker⁡(T^{k+1} )\Rightarrow T(v) \in ker⁡(T^k ) \Rightarrow T^{k+1} (v)=T^k (T(v))=0\Rightarrow v \in ker⁡(T^{k+1} )$$  (QED).
* 因為$$R(T^k )=R(T^{k+1} )$$
* 所以$$ker⁡(T^k )=ker⁡(T^{k+1} )\Rightarrow ker⁡(T^{k+1} )=ker⁡(T^{k+2} )⇒R(T^{k+1} )=R(T^{k+2} )$$  (QED).

### &#xD;核空間與值域均為T的冪次不變子空間

> 線性轉換$$T \in L(V,V),~ k \in \mathbb{N}$$，則：
>
> * $$W=ker⁡(T^k )$$，$$W$$為$$T$$-不變子空間>   ($$\forall w \in W, T(w) \in W$$)
> * $$W=R(T^k )$$，$$W$$為$$T$$-不變子空間>

Proof:

* 因為$$W$$為$$V$$的子空間，只需證明$$T(W) \subseteq W$$。
* $$\forall v \in W=ker⁡(T^k ), T^k (v)=0$$
* 所以$$T^k (T(v))=T^{k+1} (v)=T(T^k (v))=T(0)=0$$
* 可得$$T(v) \in W$$ (QED)
* $$T(W)=T(R(T^k ))=R(T^{k+1} ) \subseteq R(T^K )=W$$ (QED)

## 核集鏈定理(kernel chain theorem)

> 線性轉換$$T \in L(V,V),~\dim⁡(V)<\infty$$，則以下敘述等價> ：
>
> 1. $$\{0\} \subseteq ker⁡(T)\subseteq ker⁡(T^2 )\subseteq \dots \subseteq ker⁡(T^i) \subseteq ker(T^{i+1} )\subseteq \dots \subseteq V$$
> 2. 存在最小正整數$$k$$使得$$ker⁡(T^k )=ker⁡(T^{k+1} )=ker⁡(T^{k+2} )=\dots$$（因為核集的上限為向量空間$$V$$）
> 3. $$\exists k \in \mathbb{N} \ni \bigcup_{i=1}^\infty  ker⁡(T^i )=ker⁡(T^k)$$
> 4. $$W=\bigcup_{i=1}^\infty  ker⁡(T^i )=ker⁡(T^k)$$為最大冪零區，且$$T_w$$ 的指標是$$k$$。>

> 此定理說明$$T$$的次方越大，則其核集越大（集合最小為$$\{0\}$$，最大為向量空間$$V$$，且為遞增集合），但到某一定的次方$$k$$後就不會增加。
>
> 矩陣$$A \in F^{ N \times N}$$
>
> * $$\{0\} \subseteq ker⁡(A) \subseteq ker⁡(A^2 ) \subseteq \dots \subseteq ker⁡(A^i ) \subseteq ker⁡(A^{i+1} )\subseteq \dots \subseteq F^{N \times 1}$$
> * $$\exists k \in \mathbb{N} \ni ker⁡(A^k )=ker⁡(A^{k+1} )=ker⁡(A^{k+2} )=\dots$$
> * $$\bigcup_{i=1}^\infty  ker⁡(A^i )=ker⁡(A^k)$$

Proof (1):  由: 一般線性轉換核空間會越來越大，值域會越來越小得證。(QED)

Proof (2):

* 由(1)知$$0 \leq \dim⁡(ker⁡(T) ) \leq \dim⁡(ker⁡(T^2 ) ) \leq \dots \leq \dim⁡(V)$$。
* 因為$$\dim⁡(ker⁡(T) ),\dim⁡(ker⁡(T^2 ) ),\dots$$可能有無限次線性轉換，但$$\dim⁡(V)$$為有限維度。
* 所以$$\exists k \in \mathbb{N} \ni \dim⁡(ker⁡(T^k))=\dim⁡(ker⁡(T^{k+1} ) )$$。
* 因為$$ker⁡(T^k)$$為$$ker⁡(T^{k+1})$$的子空間，且兩空間維度相同，因此$$ker⁡(T^k )$$=$$ker⁡(T^{k+1})$$
* 由核空間經線性轉換後不再增大時，則不會再增大  得$$ker⁡(T^k )=ker⁡(T^{k+1} )=ker⁡(T^{k+2} )=\dots$$ (QED)

Proof (3):

* 因為$$ker⁡(T)\subseteq  ker⁡(T^2 ) \subseteq \ dots \subseteq ker⁡(T^k )=ker⁡(T^{k+1} )=\dots$$
* 所以$$\bigcup_{i=1}^\infty  ker⁡(T^i )=ker⁡(T^k)$$ (QED)

## 像集鏈定理(image chain theorem)

> 線性轉換$$T \in L(V,V), ~\dim⁡(V)<\infty$$，則以下敘述等價> ：
>
> 1. $$V \supseteq R(T) \supseteq R(T^2 ) \supseteq \dots \supseteq R(T^i ) \supseteq R(T^{i+1} )\supseteq \dots \supseteq \{0\}$$
> 2. 存在最小正整數$$k$$使得$$R(T^k )=R(T^{k+1} )=R(T^{k+2} )=\dots$$
> 3. $$\bigcap_{i=1}^\infty R(T^i )=R(T^k)$$
> 4. $$W=\bigcap_{i=1}^\infty R(T^i )$$為最大可逆集。

> 此定理說明$$T$$的次方越大，則其像集（值域）越小，但到了某一定的次方後就不會再減少。
>
> 矩陣$$A\in F^{N \times N}$$
>
> * $$F^{N \times 1} \supseteq CS(A) \supseteq CS(A^2 ) \supseteq \dots \supseteq CS(A^i ) \supseteq CS(A^{i+1} )\supseteq \dots \supseteq \{0\}$$
> * $$\exists k \in \mathbb{N} \ ni CS(T^k )=CS(T^{k+1} )=CS(T^{k+2} )=\dots$$
> * $$\bigcap_{i=1}^\infty CS(A^i )=CS(A^k)$$

Proof (1):  由Theorem: 一般線性轉換核空間會越來越大，值域會越來越小得證。(QED)

Proof (2):

* 由(1)知$$\dim⁡(V) \geq \dim⁡(R(T)) \geq \dim⁡(R(T^2 ))\geq \dots \geq 0$$。
* 因為$$\dim⁡(R(T)),\dim⁡(R(T^2)),\dots$$有無限多次線性轉換，但$$\dim⁡(V)$$為有限值，所以$$\exists k \in \mathbb{N} \ ni \dim⁡(R(T^k ))=\dim⁡(R(T^{k+1} ))$$。
* 因為$$R(T^{k+1})$$為$$R(T^k)$$的子空間，且兩空間維度相等，所以$$R(T^k )=R(T^{k+1} )$$
* 因為值域經線性轉換不再縮小時，則不會再縮小  ，可得$$R(T^k )=R(T^{k+1} )=\dots$$ (QED)

Proof(3):

* 因為$$R(T) \supseteq R(T^2 ) \supseteq \dots \supseteq R(T^k )=R(T^{k+1} )= \dots$$
* 所以$$\bigcap_{i=1}^\infty R(T^i )=R(T^k)$$ (QED)

Fitting引理: 當核空間經線性轉換不再變大且值域不再變小時，則向量空間等於核空間與值域的直和


> 線性轉換$$T \in L(V,V), ~\dim⁡(V)<\infty$$，則存在最小正整數$$k$$使得$$V=ker⁡(T^k ) \oplus R(T^k )$$。
>
>> 當$$T^2=T ,~ker⁡(T^2 )=ker⁡(T)$$，即$$V=ker⁡(T)⊕R(T)$$

Proof:

* 因為核空間經線性轉換後不再增大時，值域經線性轉換也不會縮小
* 所以$$\exists k \in \mathbb{N} \ni ker⁡(T^k )=ker⁡(T^{k+1} )=\dots=ker⁡(T^{2k} )$$， $$R(T^k )=R(T^{k+1} )=\dots=R(T^{2k} )$$。
* 根據[Sylvester's 2nd law(向量空間V為線性轉換T的核空間與值域的直和](kernel-space-and-image.md#sylvesters-2nd-law-xiang-liang-kong-jianvwei-xian-xing-zhuan-huantde-he-kong-jian-yu-zhi-yu-de-zhi-he))  ， 只需證明$$ker⁡(T^k ) \cap R(T^k )=\{0\}$$。
* $$\forall  v  \in ker⁡(T^k ) \cap R(T^k )$$
* $$T^k (v)=0$$且$$\exists v \in V \ni v=T^k (u)$$。
* $$0=T^k (v)=T^k (T^k (u))=T^2k (u) \Rightarrow u \in ker⁡(T^{2k} )=ker⁡(T^k )$$所以$$v=T^k (u)=0$$可得$$ker⁡(T^k )\cap R(T^k )=\{0\}$$(QED)

### Fitting引理性質

> $$V=ker⁡(T^k ) \oplus R(T^k )$$，因為$$ker⁡(T^k)$$與$$R(T^k)$$均為$$T$$不變子空間，取$$B_1$$ 與$$B_2$$ 為個別的基底> 。

> 可得$$B=B_1 \cup B_2$$ 為$$V$$的基底，且根據不變子空間的性質得$$[T]_B= \begin{bmatrix}  [T_{ker(T^k)}]_{B_1} & 0 \\ 0 & [T_{R(T^k)}]_{B_2} \end{bmatrix}$$
>
> * 因為$$[T_{ker(T^k)}]_{B_1}$$ 為最大冪零區，所$$T_{ker⁡(T^k )}$$  為冪零算子，即$$[T_{ker⁡(T^k )} ]_{B_1}$$ 為冪零矩陣>   。
> * 因為$$[T_{R(T^k )}  ]_{B_2}$$ 為最大可逆區，所以$$T_{R(T^k )}$$為可逆算子，即$$[T_{R(T^k )}  ]_{B_2}$$ 為可逆矩陣>   。

#### 範例

* $$T: \mathbb{R}^3 \rightarrow \mathbb{R}^3$$，$$T(x,y,z)=(0,2x, 3z)$$
* 取標準基底$$R=\{e1_, e_2, e_3\}$$，得$$[T]_R=A=\begin{bmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 3  \end{bmatrix}$$，$$rank(A)=2$$。
* $$A^2=\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 9  \end{bmatrix}$$，$$A^3=A^2=\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 27  \end{bmatrix}$$
* 因為$$ker(A^2)=ker(A^3)$$，且$$R(A^2)=R(A^3)$$，所以$$\mathbb{R^3}=ker(A^2) \oplus R(A^2)$$。
* $$ker(A^2)=span\left\{  \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix},  \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \right\}$$，$$CS(A^2)=span\left\{ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\}$$
* 取基底$$B=R$$，則$$\begin{bmatrix} 0 & 0 \\ 0 & 2 \end{bmatrix}$$為冪零矩陣，$$\begin{bmatrix} 3 \end{bmatrix}$$為可逆矩陣。



## 冪零算子(矩陣)的必要條件

> 線性轉換$$T \in L(V,V)$$（或$$A \in F^{N \times N}$$）為冪零算子）$$\dim⁡(V)=N<\infty$$，則：
>
> * $$\det⁡(T)=0$$ （$$\det⁡(A^k )=(\det⁡(A) )^k =0$$）
> * $$T^N=O, ~k\leq N$$ （$$A^N=0$$） &#x20;
> * $$\lambda$$為$$T$$（或$$A$$）的特徵根，則〕$$\lambda=0$$ (特徵根全為0, $$char_T (x)=(−1)^N x^N$$；若特徵根全為0時，可由Caylay-Hamilton定理得出$$T$$為冪零算子)
> * 因$$A$$為可逆矩陣若且唯若$$A$$的特徵根皆不為0；因此冪零矩陣不為可逆矩陣。>

Proof (1):

* 取$$B$$為$$V$$的基底，所以$$\exists k \in \mathbb{N} \ni [T^k ]_B=([T]_B )^k=0$$。
* 因此$$\det⁡(([T]_B )^k )=\det⁡(0)=0$$
* 得$$\det⁡([T]_B )=0$$ (QED)

Proof 2:

* 由核集鏈定理可得$$\exists k \in \mathbb{N}\ni \bigcup_{i=1}^\infty  ker⁡(T^i )=ker⁡(T^k )$$為最大冪零區。
* 因為$$T$$的指標為$$k$$，且$$T^k=)，~k\leq N$$。
* 所以$$T^N=T^k \cdot T^{N−k}=0 \cdot T^{N−k}=0$$ (QED)

Proof 3:

* 因為$$\lambda$$ 為$$T$$的特徵根，所以$$\exists v \neq 0 \ni T(v)=\lambda v$$。
* 因為$$0=0(v)=T^k (v)=\lambda^k v$$
* 所以$$\lambda^k v=0, ~v \neq 0$$
* 因此$$\lambda=0$$ (QED)

### &#x20;指標k的冪零算子必存在k-1次線性轉換形成的線性獨立集

> 線性轉換$$T \in L(V,V)$$（或 $$A \in F^{N\times N}$$）為指標為$$k$$的冪零算子，
>
> 1. 存在$$v \in V,v \neq 0 \ni \{v,T(v), \dots ,T^{k−1} (v)\}$$為線性獨立集。
> 2. 若存在$$v \neq 0 \ni v \in ker⁡(T^k )−ker⁡(T^{k−1} )$$，則$$\{v,T(v),\dots,T^{k−1} (v)\}$$為線性獨立集。>

&#x20;proof (1)

* $$T^k=0$$且$$T^{k−1} \neq 0$$
* 所以$$ker⁡(T^k )=V$$且$$ker⁡(T^{k−1} ) \neq V$$
* 因此$$\exists 0\neq v \in ker⁡(T^k )−ker⁡(T^{k−1} ) \ni T^k (v)=0$$且 $$T^{k−1} (v) \neq 0$$。
* 同理$$v,T(v),T^2 (v),\dots,T^{k−1} (v) \neq 0$$且$$T^k (v)=T^{k+1} (v)=\dots=0$$。
* 若$$a_0 v+a_1 T(v)+\dots+a_{k−1} T^{k−1} (v)=0$$
* 可得$$T^{k−1} (a_0 v+a_1 T(v)+\dots+a_{k−1} T^{k−1} (v))=T^{k−1} (0)=0$$
* 所以$$a_0 T^{k−1} (v)+a_1 T^k (v)+\dots+a_{k−1} T^{2k−2} (v)=0$$
* 即$$a_0 T^{k−1} (v)=0 \Rightarrow a_0=0$$
* 同理可得$$a_0=a_1=a_2=\dots=a_{k−1}=0$$
* 因此$$\{v,T(v), \dots,T^{k−1} (v)\}$$為線性獨立集(QED)
