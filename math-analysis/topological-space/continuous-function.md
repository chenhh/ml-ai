# 連續函數

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

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為函數滿足$$\forall S \subseteq X$$為開集合，$$f(S) \subseteq Y$$為開集合(不需1-1，onto或continous的假設)，則稱$$f$$為開對映。

考慮兩個拓樸，如果要描述兩集合相同，則存在一對一且映成的函數(兩集合元素完全1-1對映)，由於拓樸的元素為開集合，因此為連續函數(保證值域為開集合時，前像為開集合，類似映成的概念)，但這三個條件仍不足，還缺一個開集合一對一的概念，即定義域為開集合時，值域必為開集合的限制。如此才能夠保證$$X \leftrightarrow Y$$集合為同構，且$$\mathcal{T}_X \leftrightarrow  \mathcal{T}_Y$$也為同構。

如$$f: (X, \{ \emptyset, X\}  \rightarrow (X, \mathbb{P}(X))$$為identity map，在$$X$$中元素大於1個時，即使滿足一對一、映成且連續函數，仍不會將兩拓樸視為相同。

### 映成的連續函數相異集合的前像為相異的集合

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為映成的連續函數，則：
>
> $$\forall U_1, U_2 \subseteq Y$$為相異開集合，則$$f^{-1}(U_1) ,f^{-1}(U_2)$$為$$X$$的相異集合。
>
> 註：映成：$$\forall y \in Y ~\exists x \in X \ni f(x)=y$$。

### 一對一的開對映相異集合值域為相異集合

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為一對一的開對映，則：
>
> $$\forall S_1, S_2 \subseteq X$$為相異開集合，則$$f(S_1), f(S_2)$$為$$Y$$的相異集合。
>
> 註：一對一: $$f(x_1)=f(x_2) \implies x_1=x_2$$。

### 一對一且映成函數為開對映若且唯若反函數為連續函數

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為一對一且映成函數。若$$f$$為開對映若且唯若$$f$$的反函數為連續函數。

### 一對一且映成函數為連續函數若且唯若反函數為開對映

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為一對一且映成函數。若$$f$$為連續函數若且唯若$$f$$的反函數為開對映。

## 同胚(homeomorphism)

> $$X, Y$$為拓樸空間，若$$f: X \rightarrow Y$$一對一、映成、連續且為開對映函數，則稱$$f$$是$$X,Y$$之間的同胚。
>
> 如果兩個拓樸空間之間存在同胚，則稱為<mark style="color:red;">同胚拓樸空間(homeomorphic topological spaces)</mark>。
>
> 同胚是拓撲空間範疇中的同構；也就是說它們是保持給定空間的所有拓撲性質的對映。
>
> 從拓撲學的觀點來看，兩個空間是相同的。 <mark style="color:red;">拓撲空間是一個幾何物體，同胚就是把物體連續延展和彎曲，使其成為一個新的物體</mark>。

### 同胚的充要條件

> $$X, Y$$為拓樸空間，$$f: X \rightarrow Y$$為函數。
>
> 則$$f$$為同胚若且唯若$$f$$為一對一、映成且連續函數，$$f$$的反函數也為連續函數。

### 同胚為等價關係

> $$X, Y$$為拓樸空間，記$$X \sim Y$$為同胚拓樸空間。
>
> 則$$\sim$$為拓樸空間的等價關係：
>
> 1. $$X \sim X$$。
> 2. $$X \sim Y \iff Y \sim X$$。
> 3. $$X \sim Y, ~ Y \sim Z \implies X \sim Z$$。
