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
> 2. \[<mark style="color:red;">內點集的單調性</mark>] 若$$S\subseteq T$$，則$$\mathrm{int}(S) \subseteq \mathrm{int}(T)$$。
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
> 1. \[<mark style="color:red;">閉集合的補集合等價於其外點集</mark>]$$S$$為閉集合⟺$$\mathrm{ext}(S)=S^c$$。\[$$S$$為開集合⟺$$\mathrm{int}(S)=S$$⟺$$S^c$$為閉集合，且$$\mathrm{ext}(S) = \mathrm{int}(S^c)$$]
> 2. \[<mark style="color:red;">外點集的單調性</mark>]$$S \subseteq T \implies \mathrm{ext}(T) \subseteq \mathrm{ext}(S)$$。
> 3. $$\mathrm{ext}(S)$$是所有與$$S$$不相交開集合的聯集，即$$\displaystyle \mathrm{ext}(S) = \bigcup_{\{U \in \mathrm{T} ~|~ U \cap S =\emptyset \}} U$$。
> 4. $$\mathrm{ext}(S)$$是所有與$$S$$不相交開集合中最大的<mark style="color:red;">開集合</mark>。即$$\mathrm{ext}(S) \in \mathcal{T}$$且若$$U \in \mathcal{T}, ~ U \cap S = \emptyset \implies U \subseteq \mathrm{ext}(S)$$。
> 5. $$\mathrm{int}(S) \subseteq \mathrm{ext}(\mathrm{ext}(S))$$。

<mark style="color:red;">註：無法得到</mark>$$\mathrm{ext}(\mathrm{ext}(S))=\mathrm{ext}(S)$$<mark style="color:red;">的結論</mark>。

#### 性質5等號不成立的範例

考慮$$\mathbb{R}$$的標準拓樸，任意非空的開區間$$(r,s)$$必定包含無理數與有理數，因此可得$$\mathrm{int}(\mathbb{Q})=\emptyset$$。$$\mathrm{ext}(\mathbb{Q})=\mathrm{int}(\mathbb{Q}^c)=\mathrm{int}(\mathbb{R-Q})＝\emptyset$$。因此$$\mathrm{ext}(\mathrm{ext}(\mathbb{Q}))=\mathrm{ext}(\emptyset)=\mathbb{R} \neq \mathrm{int}(\mathbb{Q})$$。

<details>

<summary>proof 5與範例</summary>

因為$$\mathrm{ext}(S) \subseteq S^c$$且由2得$$\mathrm{ext}(S^c) \subseteq \mathrm{ext}(\mathrm{ext}(S))$$由。由於$$\mathrm{ext}(S^c)=\mathrm{int}((S^c)^c)=\mathrm{int}(S)$$，因此可得$$\mathrm{int}(S) \subseteq \mathrm{ext}(\mathrm{ext}(S))$$。

(QED)

</details>

## 閉包(closure)

> $$(X, \mathcal{T})$$為拓樸空間，$$S \subseteq X$$。
>
> $$\forall a \in X$$，若$$a$$的任意開鄰域$$U$$均滿足$$U \cap S \neq \emptyset$$，則稱$$a$$為$$S$$的<mark style="color:red;">附著點(adherent point)</mark>。
>
> 所有$$S$$的附著點形成的集合稱為$$S$$的閉包，記為$$\mathrm{cl}(S)$$或$$\overline{S}$$。

註：閉包$$\overline{S}$$中的點是宇集合$$X$$中與$$S$$非常靠近的元素，因此可能包含不屬於$$S$$的元素，而相異宇集合可能得到不同的閉包。

由定義得$$\mathrm{int}(S) \subseteq S \subseteq \mathrm{cl}(S)$$。因為$$\forall x \in S$$，任意的開鄰域$$x \in U \in \mathcal{T}, ~U \subseteq S$$均可得$$U \cap S \neq \emptyset$$。

### 閉包的性質

> $$(X, \mathcal{T})$$為拓樸空間，$$S, T \subseteq X$$。
>
> 1. \[<mark style="color:red;">閉集合=>閉包</mark>]若$$S$$為$$X$$的閉集合，則$$\mathrm{cl}(S)=S$$且$$\mathrm{cl}(X)=X, ~\mathrm{cl}(\emptyset)=\emptyset$$。
> 2. $$S \subseteq T \implies \mathrm{cl}(S) \subseteq \mathrm{cl}(T)$$。
> 3. \[<mark style="color:red;">子集的閉包仍為子集</mark>]若$$T$$為$$X$$的閉集合，則$$S \subseteq T \iff \mathrm{cl}(S) \subseteq T$$。

<details>

<summary>proof 1</summary>

已知$$S \subseteq \mathrm{cl}(S)$$，要證明$$\mathrm{cl}(S) \subseteq S$$。

因為$$S$$為$$X$$的閉集合若且唯若$$S^c$$為開集合。因此改證明$$S^c \subseteq \mathrm{cl}(S)^c$$。

若$$x \in S^c$$，則存在開鄰域$$x \in U \in \mathcal{T}, U \subseteq S^c$$，因此$$U \cap S=\emptyset$$。

即$$x$$不是$$S$$的閉包點，因此$$x \in \mathrm{cl}(S)^c$$。

(QED)

因為$$X$$為$$X$$的閉集合，所以$$\mathrm{cl}(X)=X$$。

同理得$$\mathrm{cl}(\emptyset)=\emptyset$$。

(QED)

</details>

<details>

<summary>proof 2</summary>

取$$x \in \mathrm{cl}(S)$$，由定義任意開鄰域$$x \in U \in \mathcal{T}, ~ U \cap S\neq \emptyset$$。

因為$$S \subseteq T$$，所以$$U \cap T \neq \emptyset$$，因此可得$$x \in \mathrm{cl}(T)$$。

(QED)

</details>

<details>

<summary>proof 3</summary>

由1,2得$$S \subseteq T \implies \mathrm{cl}(S) \subseteq \mathrm{cl}(T) =T$$--(1)

若$$\mathrm{cl}(S) \subseteq T$$，因為$$S \subseteq \mathrm{cl}(S)$$可得$$S \subseteq T$$--(2)

由(1,2)得證

(QED)

</details>

### 閉包為所有閉集合的交集且為最小閉集合

> $$(X, \mathcal{T})$$為拓樸空間，$$S\subseteq X$$。
>
> 1. 閉包$$\mathrm{cl}(S)$$為所有包含$$S$$閉集合的交集且為閉集合。$$\displaystyle \mathrm{cl}(S) = \bigcap_{\{ E^c \in \mathcal{T} ~|~ S \subseteq E \}} E$$。
> 2. 閉包$$\mathrm{cl}(S)$$為所有包含$$S$$閉集合中最小的閉集合。即$$\mathrm{cl}(S)$$為閉集合，$$E$$為閉集合且$$S \subseteq E$$，則$$\mathrm{cl}(S) \subseteq E$$.&#x20;
> 3. 若$$C$$為$$X$$的閉集合滿足$$S \subseteq C$$，且對於閉集合$$Z$$若滿足$$S \subseteq Z$$且$$C \subseteq Z$$，則$$C =\mathrm{cl}(S)$$。

可整得閉包$$\mathrm{cl}(S)$$<mark style="color:red;">⟺</mark> 所有包含$$S$$閉集合的交集且為包含$$S$$最小的閉集合。

<details>

<summary>proof </summary>

proof 1

令$$\displaystyle C = \bigcap_{\{ E^c \in \mathcal{T} ~|~ S \subseteq E \}} E$$。

由於每個$$E$$均為閉集合且$$S \subseteq E$$，由閉集合的任意交集仍為閉集合得$$C$$為閉集合且$$S \subseteq C$$。

由\[閉包的性質3]得$$S \subseteq C \implies \mathrm{cl}(S) \subseteq C$$--(1)。

\[反證法]證明$$C \subseteq \mathrm{cl}(S)$$。

令$$x \notin \mathrm{cl}(S)$$，表示存在開鄰域$$x \in U \in \mathcal{T}, ~ U \cap S =\emptyset$$，即$$U \subseteq S^c$$，等價於$$S \subseteq U^c$$。

因此存在閉集合$$U^c$$滿足$$S \subseteq U^c$$但$$x \notin U^c$$，因此$$x \notin C$$--(2)

由(1,2)得$$C =\mathrm{cl}(S)$$。

(QED)

proof 2

由1得$$\mathrm{cl}(S)$$為閉集合且$$S \subseteq \mathrm{cl}(S)$$。因此$$\mathrm{cl}(S)$$為包含$$S$$的閉集合。

若$$S \subseteq E$$且$$E$$為閉集合，由1得$$\mathrm{cl}(S)=C \subseteq E$$

&#x20;(QED)

</details>

### 閉包為閉集合的等價條件&#x20;

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> 1. $$S$$為$$X$$的閉集合⟺$$S=\mathrm{cl}(S)$$。
> 2. $$\mathrm{cl}(\mathrm{cl}(S))=\mathrm{cl}(S)$$。 \[因為$$\mathrm{cl}(S)$$為$$X$$的閉集合，由1得證]

<details>

<summary>proof</summary>

⇒  由\[<mark style="color:red;">閉集合=>閉包</mark>]得證。

⇐ 給定$$S=\mathrm{cl}(S)$$，因為閉包$$\mathrm{cl}(S)$$為所有包含$$S$$閉集合的交集且為閉集合，所以$$S$$為閉集合。

(QED)

</details>

### 閉包、外點集與內點集的關係

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> 則$$\mathrm{cl}(S)=\mathrm{ext}(S)^c = \mathrm{int}(S^c)^c$$。

<mark style="color:blue;">註：可用此等式做為閉包的定義，證明閉包的性質</mark>。

<details>

<summary>proof</summary>

因為$$\mathrm{ext}(S)$$為開集合，所以$$\mathrm{ext}(S)^c$$為閉集合。

因為$$\mathrm{ext}(S) \subseteq S^c$$，所以$$S=(S^c)^c \subseteq \mathrm{ext}(S)^c$$。

由於閉包$$\mathrm{cl}(S)$$為所有包含$$S$$閉集合中最小的閉集合，因此$$\mathrm{cl}(S) \subseteq \mathrm{ext}(S)^c$$--(1)

若$$x \in \mathrm{ext}(S)^c$$，即$$x \notin \mathrm{ext}(S)$$，由定義得對於$$x$$的任意開鄰域$$U$$不滿足$$U \subseteq S^c$$，即$$U \cap S \neq \emptyset$$，因此$$x \in \mathrm{cl}(S)$$--(2)

由(1,2)得$$\mathrm{cl}(S) = \mathrm{ext}(S)^c$$

(QED)

因為$$\mathrm{ext}(S) = \mathrm{int}(S^c)$$。所以$$\mathrm{ext}(S)^c = \mathrm{int}(S^c)^c$$

(QED)

</details>

## 稠密集(sense set)

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> 若$$\mathrm{cl}(S)=X$$，則稱$$S$$在$$X$$上稠密(S dense in X)，也稱$$S$$為$$X$$的稠密集。

稠密是和閉包有關的概念。<mark style="color:blue;">閉包是指宇集合</mark>$$X$$<mark style="color:blue;">中與集合</mark>$$S$$<mark style="color:blue;">非常接近的元素集合。而稠密是指宇集合</mark>$$X$$<mark style="color:blue;">上所有的點都和</mark>$$S$$<mark style="color:blue;">很接近</mark>。

範例：<mark style="color:red;">有理數</mark>$$\mathbb{Q}$$<mark style="color:red;">是實數</mark>$$\mathbb{R}$$<mark style="color:red;">的稠密集</mark>，即$$\mathrm{cl}(\mathbb{Q})=\mathbb{R}$$。

範例：也可以修改宇集合為較小的集合，如$$(1,2)$$為$$[1,2]$$的稠密集。

## 邊界點(boundary point)

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> $$\forall a \in X$$，若$$a$$的任何開鄰域$$a \in U \in \mathcal{T}$$滿足$$U \cap S \neq \emptyset,~ U \cap S^c \neq \emptyset$$則稱$$a$$為$$S$$的邊界點。
>
> 所有$$S$$的邊界點形成的集合記為$$\mathrm{bd}(S)$$或$$\partial S$$。

### 邊界點與內點、外點、閉包的分割性質

> $$a$$為$$S$$的邊點界，則$$a$$為$$S$$的附著點($$a$$在$$S$$的閉包中)，且$$a \notin \mathrm{int}(S)$$。
>
> * \[邊界點包含附著點]$$a \in \mathrm{bd}(S) \implies a \in \mathrm{cl}(S)$$。\[因為$$U$$為任意開鄰域且$$U \cap S \neq \emptyset$$]
> * \[邊界點不是內點] $$a \in \mathrm{bd}(S) \implies a \notin \mathrm{int}(S)$$。\[因為不存在開鄰域$$U \ni U \subseteq S$$]
> * \[邊界點為閉包去除內點]\
>   $$\begin{aligned} \mathrm{bd}(S) & = \mathrm{cl}(S) - \mathrm{int}(S) \\  &=\mathrm{cl}(S) \cap \mathrm{int}(S)^c \\  & = \mathrm{ext}(S)^c \cap \mathrm{int}(S)^c \\  & = X - (\mathrm{ext}(S) \cup \mathrm{int}(S))  \end{aligned}$$。
> * \[邊界點加上內點為閉包]\
>   $$\begin{aligned} & \mathrm{bd}(S) \cup  \mathrm{int}(S) \\  &= [\mathrm{cl}(S) \cap \mathrm{int}(S)^c] \cup  \mathrm{int}(S) \\  & = \mathrm{cl}(S) \cap \mathrm{int}(S) \\  & = \mathrm{cl}(S)  \end{aligned}$$
> * $$\mathrm{bd}(S) = \mathrm{cl}(S) \cap \mathrm{cl}(S^c)$$。

上式即表示可將<mark style="color:red;">閉包</mark>$$\mathrm{cl}(S)$$<mark style="color:red;">分割成邊界</mark>$$\mathrm{bd}(S)$$<mark style="color:red;">與內點</mark>$$\mathrm{int}(S)$$<mark style="color:red;">兩部份。</mark>

同理可將<mark style="color:red;">宇集合</mark>$$X$$<mark style="color:red;">分割成內點</mark>$$\mathrm{int}(S)$$<mark style="color:red;">、外點</mark>$$\mathrm{ext}(S)$$<mark style="color:red;">與邊界點</mark>$$\mathrm{bd}(S)$$<mark style="color:red;">三部份</mark>。

即使$$S \neq X$$，其邊界集也可能是$$X$$。因為$$\mathrm{bd}(S)=\mathrm{cl}(S) - \mathrm{int}(S)$$，當$$\mathrm{bd}(S)=X$$時，等價於$$\mathrm{cl}(S)=X$$且$$\mathrm{int}(S)=\emptyset$$。

因此當$$S$$在$$X$$稠密時且$$S$$的內點為空集合時，則$$S$$的邊界點為$$X$$。如$$\mathrm{bd}(\mathbb{Q})=\mathbb{R}$$。

邊界集也可能為空集合，表示$$\mathrm{cl}(S)=\mathrm{int}(S)$$。但是$$\mathrm{int}(S) \subseteq S \subseteq \mathrm{cl}(S)$$，因此等同於$$S=\mathrm{cl}(S)=\mathrm{int}(S)$$。即$$S$$同時為閉集合也為開集合，稱為<mark style="color:red;">閉開集(clopen set)</mark>。

<details>

<summary>proof</summary>

因為$$a \in \mathrm{bd}(S)$$時，$$a$$的任何開鄰域$$a \in U \in \mathcal{T}$$滿足$$U \cap S \neq \emptyset$$，所以$$a \in \mathrm{cl}(S)$$。

(QED)

同理，$$a$$的任何開鄰域$$a \in U \in \mathcal{T}$$滿足$$U \cap S^c \neq \emptyset$$，表示不存在任何開鄰域$$a \in U \in \mathcal{T}$$滿足$$U \subseteq S$$，因此$$a \notin \mathrm{int}(S)$$。

(QED)

</details>

### 邊界點的性質

> $$(X, \mathcal{T})$$為拓樸空間且$$S \subseteq X$$。
>
> * $$\mathrm{bd}(S)$$是$$X$$的閉集合($$\mathrm{bd}(S)^c$$為開集合)。
> * $$\mathrm{bd}(S)=\mathrm{bd}(S^c)$$。
> * \[閉集合包含邊界點] $$S$$為$$X$$的閉集合⟺$$\mathrm{bd}(S) \subseteq S$$。
> * \[開集合不含邊界點] $$S$$為$$X$$的開集合⟺$$\mathrm{bd}(S) \cap S = \emptyset$$。
> * $$\mathrm{bd}(\mathrm{int}(S)) \subseteq \mathrm{bd}(S)$$。
> * $$\mathrm{bd}(\mathrm{cl}(S)) \subseteq \mathrm{bd}(S)$$。
> * $$\mathrm{bd}(\mathrm{bd}(S)) \subseteq \mathrm{bd}(S)$$。
> * $$\mathrm{bd}(\mathrm{bd}(\mathrm{bd}(S))) = \mathrm{bd}(\mathrm{bd}(S))$$。

