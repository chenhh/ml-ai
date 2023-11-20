---
description: topological space
---

# 拓樸空間

## 簡介

度量空間$$(X,d)$$，開集合$$E$$包含了所有內點(內點$$x$$必定存在半徑$$r>0$$使得開球$$B_r(x)\subseteq E$$為子集)，且可數個開集合的聯集仍為開集合，有限個開集合的聯集仍為開集合。

而拓樸空間使用開集合的性質，定義了更一般化的空間。<mark style="color:red;">只使用開集合的聯集與交集性質定義拓樸(topology)，而不需使用度量</mark>$$d$$。

拓撲空間賦予「一點附近」這個概念的抽象數學結構，由此可以定義出如收斂、連通、連續等概念。

給定開集合$$E$$後，定義補集$$E^c$$為閉集合。<mark style="color:blue;">但是集合</mark>$$S$$<mark style="color:blue;">可能是開集合、閉集合、同時為開/閉集合(如空集合和宇集合)、不是開或閉集合(如實數上的半開區間)</mark>。

## 拓樸(topology)

> 給定非空集合$$X$$，拓樸$$\mathcal{T}$$為滿足以下條件的集合族(開集合公理):
>
> 1. \[空集合/宇集合均同時為開/閉集合]$$\emptyset \in \mathcal{T}$$、$$X \in \mathcal{T}$$。
> 2. \[任意集合聯集的封閉性]$$E_i \in \mathcal{T}, \forall i \in I$$，$$I$$為指標集合(有限或無限，不一定可數)，則聯集仍為拓樸中的元素，$$\bigcup_{i \in I} E_i \in \mathcal{T}$$。
> 3. \[有限集合交集的封閉性]$$E_i \in \mathcal{T}, i=1,2,\dots,n$$，則有限交集仍為拓樸中的元素$$\bigcap_{i=1}^n E_i \in \mathcal{T}$$。等價於$$E_1, E_2 \in \mathcal{T} \implies E_1 \cap E_2 \in \mathcal{T}$$。
>
> 註：由於開集合的補集為閉集合，也可以用閉集合定義。但兩者不是對宇集合的分割，有些集合(如空間集和宇集合)同時為開集合與閉集合，且有些集合(如實數上的半開區間)不是開集合也不是閉集合。
>
> 註：<mark style="color:red;">任意集合(包含可數與不可數)的聯集的條件比可數集合的聯集條件更一般化</mark>。

$$(X, \mathcal{T})$$<mark style="color:red;">稱為拓樸空間</mark>，且稱元素$$E \in \mathcal{T}$$為<mark style="color:red;">開集合(</mark><mark style="color:blue;">此處的開集合是滿足公理存在</mark>$$\mathcal{T}$$<mark style="color:blue;">的元素，不需距離函數的定義</mark>)。

若$$E$$為開集合，則$$E^c=X-E$$為<mark style="color:red;">閉集合</mark>。[https://math.stackexchange.com/questions/2152735/what-does-open-set-mean-in-the-concept-of-a-topology](https://math.stackexchange.com/questions/2152735/what-does-open-set-mean-in-the-concept-of-a-topology)

因此存在拓樸空間$$(X,\mathcal{T})$$中的開集合，但在度量空間$$(X,d)$$中不一定是開集合(注意兩空間的開集合(拓樸)定義不同)。

給定集合$$X$$，稱$$\mathcal{T}=\{\emptyset, X\}$$為<mark style="color:red;">trival topology (the weakest/coarsest  topology)</mark>或<mark style="color:red;">indiscrete topology(只有一個開集合</mark>$$X$$，<mark style="color:red;">其中的元素無法判定)</mark>。稱冪集合$$\mathcal{T}=\mathbb{P}(X)$$(所有子集合生成的集合)為<mark style="color:red;">discrete topology(the strongest/finest topology)(</mark>$$\forall x \in X$$<mark style="color:red;">均為開集合)</mark>。

對於集合$$X$$，可以生成相異的拓樸$$\mathcal{T}$$。因此在討論時要說明何種拓樸空間。一般的集合加上距離函數(度量)後的度量空間，即可定義拓樸$$\mathcal{T}=\{E \subseteq X ~|~ \forall x \in E, \exists r > 0 \ni B_r(x) \subseteq E\}$$。

若$$x \in X$$且$$x\in E \subseteq X, ~ E \in \mathcal{T}$$，則稱$$E$$為點$$x$$的<mark style="color:red;">開鄰域(open neighborhood</mark>)。

若$$A \subseteq X$$且$$A \subseteq E, E \in \mathcal{T}$$，稱$$E$$為集合$$A$$的<mark style="color:red;">開鄰域</mark>。

<mark style="color:red;">連續函數</mark>$$f: X \rightarrow Y$$的等價定義是任意開集合$$O \subseteq Y$$的前像$$f^{-1}(O) \subseteq X$$為開集合。



## 度量空間中的拓樸

度量空間$$(X,d)$$中開集合形成的拓樸稱為<mark style="color:red;">度量拓樸(metric topology)</mark>。

已知度量空間$$(X,d)$$，給定點$$x \in X$$與半徑$$r >0$$的<mark style="color:red;">開球(open ball</mark>)為：$$\displaystyle B_r(x)=\{ y\in X~|~ d(x,y) <r\}$$。

定義度量空間<mark style="color:red;">開集合</mark>$$O$$滿足：任取裡面的點$$x$$ ，都會有一個夠小的開球$$B_r(x)$$完全落在這個區域裡。即$$\forall x \in O, \exists r >0 \ni B_r(x) \subseteq O$$。

### 開集合的交集也是開集

$$O_1, O_2 \subseteq X$$為兩開集合，若$$x \in O_1 \cap O_2$$，由開集合定義得$$\exists r_1, r_2 >0 \ni B_{r_1}(x) \subseteq O_1, ~ B_{r_2}(x) \subseteq O_2$$。

取$$r=\min\{r_1, r_2\}$$可得$$B_r(x) \subseteq O_1 \cap O_2$$&#x20;

因此取有限個開集合的交集時仍為開集合(QED)

### 任意個開集的聯集也會是開集

令$$\mathcal{O} \subseteq X$$為開集合族，即$$O \in \mathcal{O} \implies \forall x \in O, ~\exists r >0 \ni B_r(x) \subseteq O$$。

取$$y \in \bigcup_{O \in \mathcal{O}} O$$，則$$y$$必定為開集合族中至少一個開集合$$O_s$$中的元素。

## 拓樸和σ代數的比較

集合$$X$$的σ代數$$\Sigma$$滿足：

1. $$\emptyset \in \Sigma$$。
2. $$\forall E \in \Sigma \implies E^c \in \Sigma$$。
3. \[可數聯集的封閉性]$$\forall E_i \in \Sigma, ~i \in \mathbb{N} \implies \bigcup_{i \in \mathbb{N}} E_i \in \Sigma$$。

由1,2可得$$X \in \Sigma$$。

由2,3得$$\displaystyle \overline{\bigcup_{i \in \mathbb{N}} E_i} = \bigcap_{i \in \mathbb{N}} E_i^c \in \Sigma$$，因此有限交集仍為σ代數中的元素。

<mark style="color:red;">因此可得若σ代數為可數時是拓樸。但是所有的σ代數不一定是拓樸</mark>。

### 範例: σ代數但不是拓樸

給定單點集$$\{x_0\}, 1 < x_0 <1$$與在開區間$$I=(0,1)$$的Borel集$$\mathcal{B}$$(σ代數)。

若$$\mathcal{B}$$滿足拓樸的條件，則單點集任意的聯集仍為Borel集中的元素\[因為拓樸中任意聯集具封閉性]。

但這也隱含了$$I=(0,1)$$中任意子集為Borel集(因為所有集合為均為單點集的聯集所形成)。

但是已知任意子集不一定是Borel集。因此Borel集不是拓樸。

[https://math.stackexchange.com/questions/51222/is-there-an-example-of-a-sigma-algebra-that-is-not-a-topology/932730#932730](https://math.stackexchange.com/questions/51222/is-there-an-example-of-a-sigma-algebra-that-is-not-a-topology/932730#932730)

[https://math.stackexchange.com/questions/932746/example-of-sigma-algebra-that-is-not-a-topology](https://math.stackexchange.com/questions/932746/example-of-sigma-algebra-that-is-not-a-topology)

## 拓樸的基底(basis of topology)

> 給定拓樸空間$$(X, \mathcal{T})$$，若$$\mathcal{B}$$是由$$\mathcal{T}$$中的一些開集合所組成的集合，且滿足$$\mathcal{T}$$中非空的開集合(元素)均可以$$\mathcal{B}$$中的開集合(元素)聯集，則稱$$\mathcal{B}$$為$$\mathcal{T}$$的基底(basis)。
>
> 註：類似向量空間的基底，基底元素間彼此線性獨立，而向量空間元素均可由基底線性組合而成。
>
> 註：基底不唯一但數量唯一。
>
> 一組基底可建構出唯一的拓樸<mark style="color:red;">。因此若兩個拓樸有相同的基底時，則兩個拓樸有相同的元素(開集合)，即兩拓樸相等</mark>。

實數的標準拓樸上的開集合是由開區間(open interval)(可能有無限多個)的聯集所組成。

在度量拓樸的開集合，也是由開球(open ball)聯集所得。這些建構拓樸的基本集合稱為基底(basis)。

<mark style="color:blue;">範例：度量拓樸中，所有半徑為有理數的開球為基底</mark>。

### 基底的必要條件

> 令$$\mathcal{B}$$為集合 $$X$$的一組基底，則$$\mathcal{B}$$滿足：
>
> 1. $$\displaystyle X = \bigcup_{S \in \mathcal{B}}S$$。
> 2. 若$$S_1, S_2 \in \mathcal{B}$$且$$x \in S_1 \cap S_2$$，則存在$$S \in \mathcal{B} \ni x \in S, ~ S \in S_1 \cap S_2$$。
>
> 反之如果$$\mathcal{B}$$為$$X$$中的集合族且滿足1,2的性質，則存在唯一的拓樸$$\mathcal{T}$$使得$$\mathcal{B}$$為$$\mathcal{T}$$的一組基底。

<details>

<summary>proof: 存在唯一的拓樸使得B為基底</summary>

存在性:

要證明存在性，首先定義$$\mathcal{T}$$。

因為$$\mathcal{B}$$為基底的定義是每個開集合都是$$\mathcal{B}$$中元素的聯集，因此$$\mathcal{T}$$自然可寫成$$\mathcal{B}$$中元素的聯集加上$$\emptyset$$。

定義$$\mathcal{T}$$為空集合$$\emptyset$$以及所有可寫成$$\mathcal{B}$$中元素的聯集形成的集合族。

已知$$\emptyset \in \mathcal{T}$$，且由$$X=\bigcup_{S \in \mathcal{B}}S$$得$$X \in \mathcal{T}$$--(1)。

因為$$\mathcal{T}$$中所有元素可寫成$$\mathcal{B}$$中一些元素的聯集，因為$$\mathcal{T}$$中一些元素可寫成$$\mathcal{B}$$中一些元素的聯集--(2)。

要證明$$T_1 \cap T_2 \cap \dots \cap T_n$$可寫成$$\mathcal{B}$$中一些元素的聯集。使用數學歸納法，只要證明$$n=2$$的情形即可。

假設$$T_1, T_2 \in \mathcal{T}$$，依定義存在指標集合$$I, J$$使得$$T_1 =\bigcup_{i\in I}S_i, ~ T_2 =\bigcup_{j \in J} S_j$$，其中$$S_i, S_j \in \mathcal{B}$$。

由聯集分配律得$$T_1 \cap T_2 = \bigcup_{i \in I, ~ j \in J} S_i \cap S_j$$。

$$\forall x \in S_i \cap S_j$$，因為$$S_i, S_j \in \mathcal{B}$$，由2得存在$$S_x \in \mathcal{B} \ni x \in S_x$$且$$S_x \subseteq S_i \cap S_j$$。

因此可得$$S_i \cap S_j = \bigcap_{x \in S_i \cap S_j} S_x$$--(3)

由1,2,3得$$\mathcal{T}$$為拓樸。(QED)

</details>

## 相對拓樸(relative topology)

> $$(X, \mathcal{T})$$為拓樸空間，$$Y \subseteq X$$，則:
>
> $$\mathcal{S}=\{H \subseteq Y ~|~ H= G \cap Y \text{ for some }G \in \mathcal{T}\}$$為$$Y$$的拓樸。
>
> 則$$(Y, \mathcal{S})$$稱為$$(X, \mathcal{T})$$的拓樸子空間。

範：區間$$[0, 1/2)$$為$$[0,1]$$的開子集(相對於$$[0,1]$$的標準拓樸)，因為$$[0,1/2)=(-1/2, 1/2) \cap [0,1]$$。

## 連續函數(continuous function)

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為函數。
>
> 若$$\forall O \subseteq Y$$為開集合且前像$$f^{-1}(O) \subseteq X$$也是開集合，則稱$$f$$為連續函數。

也可使用閉集合定義連續函數：$$\forall C \subseteq Y$$為閉集合，若前像$$f^{-1}(C) \subseteq X$$為閉集合，則稱$$f$$為連續函數。(由$$C$$為閉集合若且唯若$$Y-C$$為開集合得出)。

集合$$X$$上的identity函數$$f: X \rightarrow X$$有可能不是連續函數。(考慮集合上相異的拓樸)

依定義要證明$$f$$為連續函數，必須驗證所有$$Y$$的開集合的前像是否為開集合。可使用基底的概念降低複雜度。

### 連續函數若且唯若基底元素的前像為開集合

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為函數，$$\mathcal{B}$$為$$Y$$的一組基底。
>
> 則$$f$$為連續函數若且唯若$$\forall O \in \mathcal{B}, ~f^{-1}(U)$$為$$X$$的開集合。

<details>

<summary>proof</summary>

\=>

若$$f$$為連續函數，由定義得$$\forall O \in \mathcal{B}$$均為$$Y$$的開集合，因此$$f^{-1}(O)$$為$$X$$的開集合。

(QED)

<=

給定對於任意的$$O \in \mathcal{B}$$，$$f^{-1}(O)$$為$$X$$的開集合。

任取$$Y$$的開集合$$U$$，由於$$\mathcal{B}$$為$$Y$$的基底，存在指標集$$I$$與$$S_i \in \mathcal{B}, ~i \in I$$使得$$U=\bigcup_{i \in I} S_i$$。

由於$$f^{-1}(U)=\bigcup_{i \in I} f^{-1}(S_i)$$且$$f^{-1}(S_i)$$為開集合，因此$$f^{-1}(U)$$為開集合，所以$$f$$為連續函數。

(QED)

</details>

## 連續函數的合成函數為連續函數

> $$X,Y,Z$$為拓樸空間，$$f: X \rightarrow Y, ~ g: Y \rightarrow Z$$為函數。得合成函數$$g \circ f: X \rightarrow Z$$。
>
> 若$$f,g$$為連續函數，則$$g \circ f$$為連續函數。

## 開對映(open map)



## 參考資料

* [台灣師範大學數學系: 拓樸導論](https://www.google.com.tw/url?sa=t\&rct=j\&q=\&esrc=s\&source=web\&cd=\&cad=rja\&uact=8\&ved=2ahUKEwi3qabdvMqCAxWMd\_UHHSErAQMQFnoECAoQAQ\&url=https%3A%2F%2Fmath.ntnu.edu.tw%2F\~li%2FTopology%2FTopology.pdf\&usg=AOvVaw0RhUQulup4SZA2j3iomw4U\&opi=89978449)。
* [https://zh.wikipedia.org/zh-tw/%E6%8B%93%E6%89%91%E7%A9%BA%E9%97%B4](https://zh.wikipedia.org/zh-tw/%E6%8B%93%E6%89%91%E7%A9%BA%E9%97%B4)
* [https://en.wikipedia.org/wiki/Open\_set](https://en.wikipedia.org/wiki/Open\_set)

