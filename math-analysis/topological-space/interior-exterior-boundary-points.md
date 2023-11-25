---
description: interior, exterior, boundary points
---

# 內點、外點、邊界點

## 簡介

拓撲空間中定義集合不需要使用距離函數，但是拓樸空間集合的內點、外點以及邊界點為度量空間的擴充，因此仍符合使用距離函數時的概念。

## 內點(interior point)

> $$(X, \mathcal{T})$$為拓樸空間，$$S \subseteq X$$(只限定$$S$$為$$X$$的子集合)。
>
> 給定$$a \in S$$，若存在$$a$$的開鄰域$$U$$為$$S$$的子集(即$$a \in U \in \mathcal{T}, ~U  \subseteq S$$)，則稱$$a$$為$$S$$的<mark style="color:red;">內點</mark>。
>
> 所有$$S$$的內點稱為<mark style="color:red;">內點集</mark>$$\mathrm{int}(S)$$。可得$$\mathrm{int}(S) \subseteq S$$，因為$$\forall a \in \mathrm{int}(S), ~ a \in U \in \mathcal{T}$$，則滿足此條件的所有$$U$$的任意聯集依定義仍為$$\mathcal{T}$$的元素，因此為開集合且聯集後仍為$$S$$的子集，即$$\bigcup U \in \mathcal{T}$$且$$\bigcup U \subseteq S$$。

<mark style="color:red;">註：內點集 ⟺ 開集合</mark> 。

<mark style="color:red;">註：內點集為集合</mark>$$S$$<mark style="color:red;">的最大開集合</mark>。

<mark style="color:red;">註：非空集合的內點集可能為空集合</mark>。

* 如實數上的單點集$$S=\{x\}$$，$$\mathrm{int}(S)=\emptyset$$。
* $$X$$的trivial topology$$\{\emptyset, X\}$$，因為$$X$$是唯一的非空開集合，所以任意不等於$$X$$的子集$$S$$的內點集均為空集合。

### 內點的性質

> $$(X, \mathcal{T})$$為拓樸空間，$$S, T \subseteq X$$。
>
> 1. \[<mark style="color:red;">開集合=>內點集等於集合</mark>] 若$$S$$為$$X$$的開集合，則$$\mathrm{int}(S)=S$$。且$$\mathrm{int}(X)=X$$，$$\mathrm{int}(\emptyset)=\emptyset$$。
> 2. 若$$S\subseteq T$$，則$$\mathrm{int}(S) \subseteq \mathrm{int}(T)$$。
> 3. 若$$S$$為$$X$$的開集合，則$$S \subseteq T \iff S \subseteq \mathrm{int}(T)$$。

<details>

<summary>proof1: 已知int(S)為S的子集，要證反方向</summary>

已知$$S$$為$$X$$的開集合，因此$$S \in \mathcal{T}$$，且$$\forall a \in S$$, $$S$$為$$a$$的開鄰域且滿足$$S \subseteq S$$，即$$a$$為$$S$$的內點，所以$$a \in \mathrm{int}(S)$$。

因此$$S \subseteq \mathrm{int}(S)$$，依定義$$\mathrm{int}(S)\subseteq S$$，因此$$S=\mathrm{int}(S)$$。

(QED)

因為$$X \in \mathcal{T}$$為開集合，因此$$\mathrm{int}(X)=X$$。

同理$$\emptyset \in \mathcal{T}$$為開集合，因此$$\mathrm{int}(\emptyset)=\emptyset$$。

(QED)

</details>

<details>

<summary>Proof 2: 由鄰域直接證明</summary>

$$\forall a \in \mathrm{int}(S)$$，由定義得存在$$a$$的開鄰域$$U \ni U \subseteq S$$。因為$$S \subseteq T$$，所以$$U \subseteq T$$，因此$$a \in \mathrm{int}(T)$$。

(QED)

</details>

<details>

<summary>proof 3</summary>

因為$$S$$為$$X$$的開集合，若$$S \subseteq T$$，由1,2得$$S=\mathrm{int}(S) \subseteq \mathrm{int}(T)$$--(1)

若$$S \subseteq \mathrm{int}(T)$$，因為$$\mathrm{int}(T) \subseteq T$$，所以$$S \subseteq T$$--(2)

由(1,2)得證(QED)

</details>

### 內點集為所有開集合的聯集且為最大開集合

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> 1. \[<mark style="color:red;">內點集為所有開集合的聯集且為開集合</mark>]$$\mathrm{int}(S)$$是所有包含於$$S$$的開集合之聯集，所以內點集為開集合，即$$\displaystyle \mathrm{int}(S)=\bigcup_{ \{U \in \mathcal{T} ~|~ U \subseteq S\}} U$$。
> 2. \[<mark style="color:red;">內點集為最大的開集合</mark>]$$\mathrm{int}(S)$$是包含於$$S$$內最大的開集合，即$$\mathrm{int}(S) \in \mathcal{T}$$且若$$U \in \mathcal{T}, U \subseteq S \implies U \subseteq \mathrm{int}(S)$$。

<details>

<summary>proof</summary>

proof 1

令$$\displaystyle V=\bigcup_{ \{U \in \mathcal{T} ~|~ U \subseteq S\}} U$$

$$\forall x \in \mathrm{int}(S)$$，依定義存在開鄰域$$x \in U \in \mathcal{T}, ~ U \subseteq S$$。因此得$$\mathrm{int}(S) \subseteq V$$ --(1)。

若$$x \in V$$，則存在$$U \in \mathcal{T} \ni U \subseteq S$$且$$x \in U$$，因此$$x \in \mathrm{int}(S)$$。所以$$V \subseteq \mathrm{int}(S)$$--(2)

由(1,2)得$$V = \mathrm{int}(S)$$&#x20;

(QED)

proof 2:

由1得$$\mathrm{int}(S)$$為開集合。

由定義可得$$\mathrm{int}(S) \subseteq S$$，即$$\mathrm{int}(S)$$為包含於$$S$$的開集合。--(3)

若$$U \subseteq S$$為開集合，由1得$$U \subseteq \mathrm{int}(S)$$--(4)

由(3,4)得$$\mathrm{int}(S)$$為最大的開集合。

(QED)

</details>

### 內點集為開集合的等價條件

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> 1. \[<mark style="color:red;">開集合等價於內點集</mark>]$$S$$為$$X$$的開集合⟺ $$S = \mathrm{int}(S)$$。\[由開集合=>內點集等於集合，且內點集為開集合得證]
> 2. \[<mark style="color:red;">內點集的內點集等於內點集</mark>]$$\mathrm{int}(\mathrm{int}(S))=\mathrm{int}(S)$$。\[由內點集$$\mathrm{int}(S)$$為開集合，且$$\mathrm{int}(S)$$開集合=>內點集等於集合$$\mathrm{int}(S) = \mathrm{int}(\mathrm{int}(S))$$得證]

## 外點(exterior point)

> $$(X, \mathcal{T})$$為拓樸空間，$$S \subseteq X$$(只限定$$S$$為$$X$$的子集合)。
>
> 對於$$a \notin S$$若存在開鄰域$$U$$滿足$$U \cap S = \emptyset$$(即$$a \in U \in \mathcal{T}, ~ U \cap S =\emptyset$$)，則稱$$a$$為$$S$$的<mark style="color:red;">外點</mark>。
>
> 所有$$S$$的外點稱為<mark style="color:red;">外點集</mark>$$\mathrm{ext}(S)$$。

由外點集定義得$$x \in \mathrm{ext}(S) \implies x \notin S \implies x \in S^c$$，因此$$\mathrm{ext}(S) \subseteq S^c$$且$$x \in U \in \mathcal{T}, ~ U \cap S=\emptyset,  \implies U \subseteq S^c$$。

<mark style="color:red;">因此可得</mark>$$S$$<mark style="color:red;">的外點集等於</mark>$$S^c$$<mark style="color:red;">的內點集</mark>，即$$\mathrm{ext}(S) = \mathrm{int}(S^c)$$。

### 外點的性質

> $$(X, \mathcal{T})$$為拓樸空間，$$S, T \subseteq X$$。
>
> 1. $$S$$為閉集合⟺$$\mathrm{ext}(S)=S^c$$。\[$$S$$為開集合⟺$$\mathrm{int}(S)=S$$⟺$$S^c$$為閉集合，且$$\mathrm{ext}(S) = \mathrm{int}(S^c)$$]
> 2. $$S \subseteq T \implies \mathrm{ext}(T) \subseteq \mathrm{ext}(S)$$。
> 3. $$\mathrm{ext}(S)$$是所有與$$S$$不相交開集合的聯集，即$$\displaystyle \mathrm{ext}(S) = \bigcup_{\{U \in \mathrm{T} ~|~ U \cap S =\emptyset \}} U$$。
> 4. $$\mathrm{ext}(S)$$是所有與$$S$$不相交開集合中最大的開集合。即$$\mathrm{ext}(S) \in \mathcal{T}$$且若$$U \in \mathcal{T}, ~ U \cap S = \emptyset \implies U \subseteq \mathrm{ext}(S)$$。
>
> <mark style="color:red;">註：無法得到</mark>$$\mathrm{ext}(\mathrm{ext}(S))=\mathrm{ext}(S)$$<mark style="color:red;">的結論</mark>。
