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
> 所有$$S$$的內點稱為內點集$$\mathrm{int}(S)$$。

<mark style="color:red;">註：非空集合的內點集可能為空集合</mark>。

* 如實數上的單點集$$S=\{x\}$$，$$\mathrm{int}(S)=\emptyset$$。
* $$X$$的trivial topology$$\{\emptyset, X\}$$，因為$$X$$是唯一的非空開集合，所以任意不等於$$X$$的子集$$S$$的內點集均為空集合。