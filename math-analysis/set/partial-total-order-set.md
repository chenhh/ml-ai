---
description: ordered set
---

# 序集

## 簡介

選擇公理與序集有緊密的關係，此處只討論<mark style="color:red;">偏序集(部份元素可比較大小)</mark>、<mark style="color:red;">全序集(集合內任意兩個元素可比較大小)</mark>與<mark style="color:red;">良序集(非空全序子集有最小元)</mark>。

實數集為最大的全序集。

## 偏序集(partial order set, poset)

> $$S\neq \emptyset$$，令關係$$R: S \rightarrow S$$為具有反身性、反對稱性與遞移性的二元關係，則$$R$$為一偏序關係(partial order relation)。
>
> * <mark style="color:blue;">反身性\[reflexive]</mark> $$\forall x \in S, xRx$$
> * <mark style="color:blue;">反對稱性\[anti-symmetric]</mark> $$\forall x,y\in S, \ xRy \land yRx \Rightarrow x=y$$
> * <mark style="color:blue;">遞移性\[transitive]</mark> $$\forall x,y,z\in S, \ xRy \land yRz \Rightarrow xRz$$
>
> 稱$$(S,R)$$為偏序集。
>
> 偏序集即定義二元關係R使得集合S內，**部分元素**可比較大小即成立。但集合內可能存在無法比較大小的元素。

* 例：$$(S,R)=(\mathbb{R}^2, \preceq)$$ (element ordering)
* 例:  $$(S,R)=(\mathbb{N}, \leq)$$
* 例：$$(S,R)= (\text{set}, \subseteq)$$

### 最大元與最小元(greatest element and least element)

> $$(X, \leq )$$為偏序集且$$Y \subseteq X$$，則
>
> * $$y$$為$$Y$$的最小元若$$y \in Y$$且不存在$$z \in Y \ni z < y$$。
> * $$y$$為$$Y$$的最大元若$$y \in Y$$且不存在$$z \in Y \ni y < z$$。
>
> <mark style="color:blue;">註：偏序集的最大元和最小元不唯一；而全序集的最大元和的最小元唯一</mark>。

例: $$X=\{\{1,2\}, \{2\}, \{2,3\}, \{2,3,4\}, \{5\}\}$$，關係為$$\subseteq$$，則$$\{2\}, \{5\}$$均為最小元，$$\{1,2\}, \{2,3,4\},\{5\}$$為最大元。

自然數$$\mathbb{N}$$有最小元0，最沒有最大元。

整數$$\mathbb{Z}$$沒有最小元與最大元。

### 上界與嚴格上界(upper bound)

> $$(X, \leq)$$為偏序集，且$$Y \subseteq X$$為子集合。令$$x \in X$$。
>
> * 如果$$\forall y \in Y$$滿足$$y \leq x$$，則稱元素$$x$$為集合$$Y$$的上界($$x$$可能為$$Y$$的元素)。
> * 如果元素$$x$$為集合$$Y$$的上界，且$$x \notin Y$$，則稱$$x$$為集合$$Y$$的嚴格上界；即$$\forall y \in Y, ~ y < x$$。

### 偏序集中存在良序子集且沒有嚴格上界

> $$(X,\leq)$$為偏序集，則存在$$Y \subseteq X$$為良序子集且$$x_0 \in X$$為$$Y$$的最小元，且$$Y$$沒有嚴格上界。

例：$$(\mathbb{R}^2, \leq)$$取$$Y=\{(p,q) \subseteq \mathbb{R}^2~|~p \geq 0, q \geq 0, p=q\}$$為第一象限$$x=y$$直線上的所有點，則最小元為$$(0,0)$$且沒有嚴格上界。

### 相容(comparable)

> 令$$(S, \leq)$$為一偏序集，$$x,y\in S$$且$$x \neq y$$，若$$x \leq y$$與$$y \leq x$$恰有一成立(不會出現$$x,y$$無法比較的情形)，則稱$$x$$與$$y$$<mark style="color:red;">相容</mark>，否則稱$$x$$與$$y$$不相容(incomparable)。

由定義知偏序集中，<mark style="color:blue;">相容的兩個元素即為可以比較大小的兩個元素</mark>。

## 全序集(total order set)

> 令$$(S, \leq)$$為一偏序集，<mark style="color:red;">若</mark>$$S$$<mark style="color:red;">中任意兩元素均相容</mark>，則稱$$\leq$$為全序關係，且$$(S, \leq)$$為全序集。

由定義知全序集中，任意兩個元素均可以比較大小。

<mark style="color:red;">自然數集、整數集、有理數集、無理數集、實數集均為全序集</mark>。

## 良序集(well order set)

> 定義：令$$(S, \leq)$$為偏序集，$$\forall x,y \in S$$且$$x \neq y$$則 $$x < y$$。

> 定義：若$$(S, \leq)$$為全序集，則$$S$$的任一非空子集合必包含最小元(素)時，為$$S$$為良序集。

<mark style="color:red;">註：自然數</mark>$$\mathbb{N}$$<mark style="color:red;">是良序集；但整數集</mark>$$\mathbb{Z}$$<mark style="color:red;">，有理數集</mark>$$\mathbb{Q}$$<mark style="color:red;">與實數集</mark>$$\mathbb{R}$$<mark style="color:red;">均非良序集</mark>。

## 三一律(trichotomy rule)

> $$x,y,z \in \mathbb{R}$$，則$$x > y, \ x=y,\ x< y$$恰有一成立。

## 集合有上(下)界(bounded above, below)

> $$(S,\leq)$$為偏序集，$$\emptyset \neq E \subseteq S$$為非空子集合。
>
> * 若$$\exists b \in S \ni \forall x \in E,\ x \leq b$$，稱$$b$$為集合$$E$$的上界；如果$$b \notin E$$，則為嚴格上界。
> * 若$$\exists a \in S \ni \forall x \in E,\ a \leq x$$，稱$$a$$為集合$$E$$的下界；如果$$a \notin E$$，則為嚴格下界。。

上、下界不必為集合$$E$$中的元素，因為當$$E$$為度量空間中的開集合或非連續集合時，可能無法直接用集合內的元素定義上下界。

如$$E=\{x \in \mathbb{Q} | 0 \leq x^2 \leq 2 \}$$，$$E$$為有理數集合，而上界為$$\sqrt{2}$$是無理數。



## Zorn lemma

> $$(S, \leq)$$為非空偏序集，如果$$S$$的所有全序子集$$E$$都有上界，則$$S$$至少含有一個最大元。

由偏序集中存在良序子集且沒有嚴格上界可證明。



## Hausdorff最大性原理

> $$(X,\leq )$$為偏序集，則存在$$X$$的全序子集$$Y$$，其依集合的包含關係為最大(即不存在$$X$$的其它全序子集$$Z$$使得$$Y \subseteq Z$$)
>
> <mark style="color:red;">註：Hausdorff最大性原理等價於Zorn lemma</mark>。
