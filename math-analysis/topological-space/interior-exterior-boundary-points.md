---
description: interior, exterior, boundary points
---

# 內點、外點、邊界點

## 簡介

拓撲空間中定義集合不需要使用距離函數，但是拓樸空間集合的內點、外點以及邊界點為度量空間的擴充，因此仍符合使用距離函數時的概念。

## 內點(interior points)

> $$(X, \mathcal{T})$$為拓樸空間，$$S \subseteq X$$。
>
> 給定$$a \in S$$，若存在$$a$$的開鄰域$$U$$使得$$U \subseteq S$$(即$$a \in U, ~U \in \mathcal{T}, ~U \subseteq S$$)，則稱$$a$$為$$S$$的內點。
>
> 所有$$S$$的內點稱為內點集$$\mathrm{int}(S)$$。可得$$\mathrm{int}(S) \subseteq S$$，因為$$\forall a \in \mathrm{int}(S), ~ a \in U, ~ U \in \mathcal{T}$$，則滿足此條件的所有$$U$$的聯集依定義仍為$$\mathcal{T}$$的元素且仍為$$S$$的子集，即$$\bigcup U \in \mathcal{T}$$且$$\bigcup U \subseteq S$$。

<mark style="color:red;">註：非空集合的內點集可能為空集合</mark>。

* 如實數上的單點集$$S=\{x\}$$，$$\mathrm{int}(S)=\emptyset$$。
* $$X$$的trivial topology$$\{\emptyset, X\}$$，因為$$X$$是唯一的非空開集合，所以任意不等於$$X$$的子集$$S$$的內點集均為空集合。

### 內點的性質

> $$(X, \mathcal{T})$$為拓樸空間，$$S, T \subseteq X$$。
>
> 1. 若$$S$$為$$X$$的開集合，則$$\mathrm{int}(S)=S$$。且$$\mathrm{int}(X)=X$$，$$\mathrm{int}(\emptyset)=\emptyset$$。
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
