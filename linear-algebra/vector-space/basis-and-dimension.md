# 基底與維度(basis and dimension)

## 基底與維度

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令集合$$B \subseteq V$$滿足：
>
> * $$span(B) = V$$（向量空間$$V$$的所有元素均可用$$B$$內的元素線性組合而成）
> * $$B$$為線性獨立集合。
>
> 則稱$$B$$為$$V$$為一組基底，且集合$$B$$內的元素個數為$$V$$的（整數）維度。

* 基底集合不唯一，但是向量空間的維度唯一（即基底集合雖然不相同，但元素個數相同）。
* $$\dim⁡(V)<\infty$$時，稱為有限維度向量空間（finite-dimensional vector space），否則為無限維度向量空間（infinite-dimensional vector space）  ，線性代數中只討論有限維度向量空間，泛函分析才會討論無限維向量空間。

標準基底


* $$N$$維歐式空間，$$V=F^N, B=\{e_1,e_2,\dots,e_N \}, e_1=(1,0,0,\dots), e_2=(0,1,0,\dots),e_N=(0,0,⋯,0,1), \dim⁡(F^N )=N$$
* $$N$$階多項式函數空間，$$V=F_N [x] ，B=\{1,x,x^2,\dots,x^N \}, \dim⁡(F_N [x])=N+1$$
* 多項式函數空間，$$V=F[x], B=\{1,x,x^2,x^3,\dots\},\dim⁡(F(x))=\infty$$
* 矩陣空間，$$V=F^{M\times N}, B=\{E_{ij}, 1\leq i \leq M, 1\leq j \leq N\},\dim⁡(F^{M \times N} )=MN$$
* 實數(複數)空間，$$V=F, b=\{1\},\dim⁡(F)=1$$
* 色彩空間中, $$V=\text{RGB-color}, \dim⁡(V)=3$$
* 零空間，$$V=\{0\}，B=\{\emptyset\}，\dim⁡(\{0\})=0$$，這是唯一一個維度為0的空間。

歐式空間$$V$$定義在體$$\mathbb{R}$$或$$\mathbb{C}$$時維度不同如下表：

| $$V$$            | $$F$$          | 向量空間 | 維度     |
| ---------------- | -------------- | ---- | ------ |
| $$\mathbb{C}^N$$ | $$\mathbb{C}$$ | 是    | $$N$$  |
| $$\mathbb{R}^N$$ | $$\mathbb{R}$$ | 是    | $$N$$  |
| $$\mathbb{C}^N$$ | $$\mathbb{R}$$ | 是    | $$2N$$ |
| $$\mathbb{R}^N$$ | $$\mathbb{C}$$ | 否    | 無定義    |

### 向量空間所有元素可用基底參數唯一表示

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$B=\{ v_1, v_2,\dots, v_N\} \subseteq  V$$，則集合$$B$$為$$V$$的基底若且唯若$$\forall v \in V$$, $$v$$可唯一表示成$$B$$中向量的線性組合。
>
> 此定理證明了只要給定向量空間的基底，則元素的座標（參數）唯一決定。

Proof =>

* $$\forall v \in V, span(B)=V \Rightarrow v \in span(B)$$
* 假設$$v=\sum_{i=1}^N a_i v_i =\sum_{i=1}^N b_i v_i$$
* 因為 $$0=v−v=\sum_{i=1}^N (a_i−b_i )v$$  ，且$$B$$為線性獨立集合。
* 所以$$a_i−b_i=0, \forall i \Rightarrow a_i=b_i,  \forall i$$ (QED)

Proof: <=

* $$\forall v \in V$$，$$v$$為$$B$$中元素的線性組合，所以$$span(B)=V$$-- (1)
* 若$$a_1 v_1+a_2 v_2+\dots +a_N v_N=0$$
* 因為$$0=0v_1+0v_2+ \dots +0v_N$$ 且$$0 \in V$$是$$B$$中的唯一表示法，
* 因為$$B$$為線性獨立集-- (2)
* 由(1)(2)得$$B$$為$$V$$的基底 (QED)

### 線性相依元素可由線性獨立集生成

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S \subseteq V$$為線性獨立集，且$$u \in V -S$$，則$$S \cup \{u\}$$為線性相依集若且唯若$$u \in span(S)$$。
>
> 線性相依元素可由線性獨立集生成，反過來線性相依集去除掉線性相依的元素後，可變成線性獨立集。

Proof =>

* 因為$$S \cup \{u\}$$為線性相依集，
* 所以存在$$v_1,v_2, \dots ,v_k \in S \cup \{u\}$$，$$a_1,a_2, \dots ,a_k \in F$$不全為$$0$$使得$$a_1 v_1+a_2 v_2+\dots +a_k v_k=0$$。
* 因為$$S$$為線性獨立集，令$$v_1,v_2, \dots ,v_k$$ 中至少一個元素為$$u$$，不失一般性令$$v_1=u$$
* 所以$$a_1 \neq 0$$可得 $$u=\frac{−1}{a_1}  (a_2 v_2+ \dots+a_k v_k ) \in span(S)$$ (QED)

Proof <=

* 因為$$u \in span(S)$$，
* 所以存在$$v_1,v_2, \dots ,v_k\in S$$，$$a_1,a_2, \dots ,a_k \in F$$使得$$u=a_1 v_1+a_2 v_2+\dots+a_k v_k$$
* 移項後得$$a_1 v_1+\dots+a_k v_k−u=0$$
* 因為$$u \notin S$$，因此$$u \neq v_i, ~i=1,2,\dots,k$$
* 所以$$S \cup \{u\}$$為線性相依集 (QED)

### 生成集在刪除線性相依元素後仍然為生成集

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$span(S) =V$$，若$$S$$不為線性獨立集，則存在$$u \in S$$使得$$span(S - \{u\}) = V$$。
>
> * 註：可知若$$S$$生成V，但$$S$$不為線性獨立集，則存在$$u_1 \in S \ni S−\{u_1\}$$仍然生成$$V$$。
>   * 同理，若$$S−\{u_1\}$$仍不為線性獨立集，則存在$$u_2 \in S−\{u_1\} \ni S−\{u_1,u_2\}$$仍然生成$$V$$。
>   * 以此類推，最後必存在$$u_1,u_2,\dots,u_m \in S \ni S−\{u_1,u_2,\dots,u_m \}$$生成$$V$$且為線性獨立集，即為基底。
>   * 若$$\dim⁡(V)=N, ~|S|=K$$，則$$S$$中可拿掉$$N-K$$個向量形成$$V$$的基底。>

Proof:

* 若$$S$$為線性相依集，則存在$$v_1, \dots ,v_k \in S$$， $$a_1, \dots,a_k \in F$$不全為0使得 $$a_1 v_1+\dots +a_k v_k=0$$。
* 不失一般性令$$a_1 \neq 0$$，取$$u=v_1$$
* 則$$u=v_1=\frac{−1}{a_1} (a_2 v_2+\dots +a_k v_k ) \in span(S−\{u\})$$
* 因為$$S$$生成$$V$$，所以$$S−\{u\}$$仍然生成$$V$$ (QED)

### 線性獨立集(但無法生成整個向量空間)聯集非其生成集的元素後仍為線性獨立集

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$span(S) \neq V$$，則存在$$u \in V- span(S) \ni span(S) \cup \{u\}$$為線性獨立集。
>
> * 註：若$$S$$為線性獨立集，但$$S$$不生成V，則存在$$u_1 \notin S \ni S \cup \{u_1\}$$仍為線性獨立集。
>   * 同理，若$$S \cup \{u_1\}$$仍不生成$$V$$，則存在$$u_2 \notin S \cup \{u_1\} \ni S \cup \{u_1,u_2 \}$$仍為線性獨立集。
>   * 以此類推，最後必存在$$u_1,u_2, \dots ,u_m \notin S \ni S \cup \{u_1,u_2, \dots ,u_m \}$$為線性獨立集且生成$$V$$，即基底。
>   * 若$$\dim⁡(V)=N, |S|=K$$，則$$S$$中可加入$$N-K$$個向量形成$$V$$的基底。>

Proof：

* 因為$$span(S) \neq V$$，取$$u=V−span(S)$$，欲證$$span(S) \cup \{u\}$$為線性獨立集。
* 取$$v_1,v_2 \dots, v_k∈span(S) \cup \{u\}$$
* 若$$a_1 v_1+a_2 v_2+\dots+a_k v_k=0$$，則線性獨立集應只有$$a_1=a_2=\dots=a_k=0$$唯一解。
* $$u \neq v_i, ~i=1,2, \dots,k$$，因為$$S$$為線性獨立集，則$$a_i=0, ~\forall i$$
* 否則存在$$v_i=u$$ for some $$i \in \{1,2,\dots,k\}$$，不失一般性令$$v_1=u$$
* 所以$$a_1=0$$，仍可得到$$a_2 v_2+\dots +a_k v_k=0$$，即$$a_2=a_3=\dots=a_k=0$$
* 因此$$a_1=a_2=\dots=a_k=0$$
* 所以$$span(S) \cup \{u\}$$為線性獨立集(QED)

### Steinitz replacement theorem

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$span(S) = V, S=\{v_1, v_2, \dots, v_N\}$$。 令集合$$T=\{u_1, u_2, \dots, u_M\}, ~M \leq N$$為線性獨立集，則存在$$U \subseteq S, |U| = N-M \ni span(U \cup T) =V$$。
>
> 可將生成集$$S$$中部份（線性依相）元素，替換成其它線性獨立元素後，仍可生成向量空間$$V$$。&#x20;

Proof (數學歸納法):

* $$M=0$$時，  $$T=\emptyset$$，取$$U=S$$，則$$|U |=N$$，且$$U \cup T=S$$生成$$V$$。&#x20;
* 假設$$M=K$$成立。
* 考慮$$M=K+1$$  ，$$T=\{u_1,u_2, \dots ,u_{K+1} \}$$為線性獨立集，因此$$\{u_1,u_2,\dots,u_k \}$$也為線性獨立集。
* 由$$M=K$$的假設知存在$$\{v_{i_1},v_{i_2}, \dots ,v_{i_{n−k} } \} \subseteq S \ni  span(\{u_1,u_2, \dots ,u_k \} \cup \{v_{i_1} ,v_{i_2 }, \dots ,v_{i_{n−k}} \})=V$$
* 因為$$u_{k+1} \in V$$，所以存在$$a_1, \dots ,a_k,b_1,⋯,b_{n−k} \in F$$使得：
  * $$u_(k+1)=a_1 u_1+\dots+a_k u_k+b_1 v_{i_1}+ \dots b_{n−k} v_{i_{n−k}}$$
  * 其中$$b_1, \dots ,b_{n−k}$$不全為0，否則$$\{u_1,u_2, \dots ,u_{k+1} \}$$不為線性獨立集。
* 不失一般性令$$b_1 \neq 0$$，則$$v_{i_1}=\frac{−1}{b_1} (\sum_{i=1}^k a_i u_i−u_{k+1}+\sum_{j=2}^{n−k}b_j v_{i_j })$$，因此$$v_{i_1}  \in span(\{u_1, \dots ,u_{k+1} \} \cup \{v_{i_2}, \dots ,v_{i_{n−k}} \})$$。
* 取$$U=\{v_{i_2}, \dots ,v_{i_{n−k}} \}$$，則$$|U |=n−k−1=n−(k+1)$$。
* 因為$$span(\{u_1,u_2, \dots ,u_k \} \cup \{v_{i_1} ,v_{i_2} ),\dots ,v_{i_{n−k}} \})=V$$，所以$$span(U \cup T )=V$$，即$$M=K+1$$成立 (QED)

### 線性獨立集元素個數必小於等於生成集元素個數

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$span(S) = V$$，令$$T$$為$$V$$中線性獨立集合，則$$|T| \leq |S|$$。

Proof:

* 令$$|S|=N, |T |=M, T=\{u_1, \dots ,u_M \}$$
* 若$$M>N$$，取$$T_1=\{u_1,u_2,\dots,u_N \}$$為線性獨立集。
* 由Steinitz replacement theorem知存在$$S_1 \subseteq S \ni span(S_1 \cup T_1 )=V$$  ，其中$$|S_1 |=N−N=0, 即S_1= \emptyset$$。
* 因此$$span(S_1 \cup T_1 )=span(T_1 )=V$$
* 因為$$u_{M+1} \in V=span(T_1 )$$
* 所以$$u_{M+1} \in span\{u_1,u_2,⋯,u_M \}$$，此與$$T$$為線性獨立集矛盾，所以$$M \leq N$$ (QED)

## 最小生成集(minimal spanning set)，最大獨立集(maximal independent set)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$S \subseteq V$$。
>
> * 若$$span(S)=V$$是所有生成集合中元素個數最少者，稱$$S$$為向量空間$$V$$的最小生成集。
> * 若$$S$$為線性獨立集，且$$S$$為所有線性獨立集合中元素個數最多者，稱$$S$$為向量空間$$V$$的最大獨立集。

### 基底為向量空間的最小生成集且同時為最大獨立集

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$S \subseteq V$$，則：
>
> * $$S$$為向量空間$$V$$的基底若且唯若$$S$$是向量空間$$V$$的最小生成集。
> * $$S$$為向量空間$$V$$的基底若且唯若$$S$$是向量空間$$V$$的最大獨立集。

### 個數等於基底的生成集或是線性獨立集必為基底

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$\dim(V)=N$$，且$$S \subseteq V$$，$$\dim(S)=N$$，則：
>
> * $$S$$為線性獨立集若且唯若$$S$$為向量空間$$V$$的基底。
> * $$span(S) = V$$若且唯若$$S$$為向量空間$$V$$的基底。

* Proof (1) <= 由定義成立
* Proof (1) =>	• 需證明$$S$$為線性獨立集，反證法。
* 若$$S$$不為線性獨立集，則存在$$u \in S \ni span(S−\{u\})=V$$
* 因為$$\dim⁡(V)=N$$，因此最小生成集個數應為$$N$$個元素。
* 因此$$|S−\{u\}|=N−1$$不可能生成$$V$$，矛盾，因此$$S$$為線性獨立集 (QED)。
* Proof (2) <=由定義成立。
* Proof (2)=>  只需證明$$S$$生成$$V$$，反證法。
* 若$$S$$不生成$$V$$，則存在$$u \notin S \ni S \cup \{u\}$$仍為線性獨立集。
* 但$$|S \cup \{u\}|=N+1$$與$$V$$最大獨立集合個數$$N$$矛盾。
* 因此$$S$$生成$$V$$(QED)。

### 子空間與原空間維度相同時為相同的向量空間

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$W$$為$$V$$的子空間，則$$W=V$$若且唯若$$\dim(W) = \dim(V)$$。

Proof =>: 由定義成立。

Proof <=

* 取$$B$$為$$W$$的一組基底，可得$$B$$為$$W$$上的線性獨立集，因為$$W$$是$$V$$的子空間，因此$$B$$也是$$V$$上的線性獨立集。
* 因為$$|B|=\dim⁡(W)=\dim⁡(V)$$
* 線性獨立集$$B$$元素個數等於$$V$$基底個數，因此，$$B$$為$$V$$的一組基底。
* 可得$$V=span(B)=W$$ (QED)

## &#x20;矩陣可逆的充要條件

> $$A \in F^{N \times N}$$，若$$A$$為可逆矩陣，則下列均為充要條件：

1. $$ker(A) = \{0\}$$，$$\dim(ker(A))=0$$。
2. $$Lker(A) = \{0\}$$，$$\dim(LKer(A))=0$$。
3. $$A$$的行向量均為線性獨立，且為$$F^{N \times 1}$$的基底，可得$$CS(A) = F^{N \times 1}$$，$$\dim(CS(A))=N$$。
4. $$A$$的列向量均為線性獨立，且為$$F^{ 1\times N}$$的基底，可得$$RS(A) = F^{1 \times N}$$，$$\dim(RS(A))=N$$。
5. $$A$$[的所有特徵根均不為0](../linear-transform/eigenvector.md#ke-ni-ju-zhen-zhi-te-zheng-gen-jun-bu-wei-0)

* proof 1: 因為$$A$$可逆，可得$$Ax=0$$只有唯一解$$x=0$$，因此$$ker(A) = \{0\}$$(QED)
* proof 2: 因為$$A$$可逆，可得$$xA=0$$只有唯一解$$x=0$$，因此$$Lker(A) = \{0\}$$ (QED)
* proof 3:
* $$Ax = \begin{bmatrix} A_{:1} & \dots & A_{:N}\end{bmatrix} \begin{bmatrix}  x_1 \\ \vdots \\ x_N \end{bmatrix} = 0$$，因為$$A$$可逆，只有唯一解$$x=0$$，因此行獨立。(QED)

