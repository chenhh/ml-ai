# 基底與維度\(basis and dimension\)

## 基底與維度

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令集合$$B \subseteq V$$滿足：
>
> * $$span(B) = V$$（向量空間$$V$$的所有元素均可用$$B$$內的元素線性組合而成）
> * $$B$$為線性獨立集合。
>
> 則稱$$B$$為$$V$$為一組基底，且集合$$B$$內的元素個數為$$V$$的（整數）維度。

* 基底集合不唯一，但是向量空間的維度唯一（即基底集合雖然不相同，但元素個數相同）。
* $$\dim⁡(V)<\infty$$時，稱為有限維度向量空間（finite-dimensional vector space），否則為無限維度向量空間（infinite-dimensional vector space）  ，線性代數中只討論有限維度向量空間，泛函分析才會討論無限維向量空間。

## 標準基底

* $$N$$維歐式空間，$$V=F^N, B=\{e_1,e_2,\dots,e_N \}, e_1=(1,0,0,\dots), e_2=(0,1,0,\dots),e_N=(0,0,⋯,0,1), \dim⁡(F^N )=N$$
* $$N$$階多項式函數空間，$$V=F_N [x] ，B=\{1,x,x^2,\dots,x^N \}, \dim⁡(F_N [x])=N+1$$
* 多項式函數空間，$$V=F[x], B=\{1,x,x^2,x^3,\dots\},\dim⁡(F(x))=\infty$$
* 矩陣空間，$$V=F^{M\times N}, B=\{E_{ij}, 1\leq i \leq M, 1\leq j \leq N\},\dim⁡(F^{M \times N} )=MN$$
* 實數\(複數\)空間，$$V=F, b=\{1\},\dim⁡(F)=1$$
* 色彩空間中, $$V=\text{RGB-color}, \dim⁡(V)=3$$
* 零空間，$$V=\{0\}，B=\{\emptyset\}，\dim⁡(\{0\})=0$$，這是唯一一個維度為0的空間。

歐式空間$$V$$定義在體$$\mathbb{R}$$或$$\mathbb{C}$$時維度不同如下表：

| $$V$$ | $$F$$ | 向量空間 | 維度 |
| :--- | :--- | :--- | :--- |
| $$\mathbb{C}^N$$ | $$\mathbb{C}$$ | 是 | $$N$$ |
| $$\mathbb{R}^N$$ | $$\mathbb{R}$$ | 是 | $$N$$ |
| $$\mathbb{C}^N$$ | $$\mathbb{R}$$ | 是 | $$2N$$ |
| $$\mathbb{R}^N$$ | $$\mathbb{C}$$ | 否 | 無定義 |

### 向量空間所有元素可用基底參數唯一表示

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$B=\{ v_1, v_2,\dots, v_N\} \subseteq  V$$，則集合$$B$$為$$V$$的基底若且唯若$$\forall v \in V$$, $$v$$可唯一表示成$$B$$中向量的線性組合。
>
> 此定理證明了只要給定向量空間的基底，則元素的座標（參數）唯一決定。

Proof =&gt;

* $$\forall v \in V, span(B)=V \Rightarrow v \in span(B)$$
* 假設$$v=\sum_{i=1}^N a_i v_i =\sum_{i=1}^N b_i v_i $$
* 因為 $$0=v−v=\sum_{i=1}^N (a_i−b_i )v$$  ，且$$B$$為線性獨立集合。
* 所以$$a_i−b_i=0, \forall i \Rightarrow a_i=b_i,  \forall i$$ \(QED\)

Proof: &lt;=

* $$\forall v \in V$$，$$v$$為$$B$$中元素的線性組合，所以$$span(B)=V$$-- \(1\)
* 若$$a_1 v_1+a_2 v_2+\dots +a_N v_N=0$$
* 因為$$0=0v_1+0v_2+ \dots +0v_N$$ 且$$0 \in V$$是$$B$$中的唯一表示法，
* 因為$$B$$為線性獨立集-- \(2\)
* 由\(1\)\(2\)得$$B$$為$$V$$的基底 \(QED\)

### 線性相依元素可由線性獨立集生成

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S \subseteq V$$為線性獨立集，且$$ u \in V -S$$，則$$S \cup \{u\}$$為線性相依集若且唯若$$ u \in span(S)$$。
>
> 線性相依元素可由線性獨立集生成，反過來線性相依集去除掉線性相依的元素後，可變成線性獨立集。

