# 偏序集或全序集

## 偏序集(partial order set)

> $$S\neq \emptyset$$，令關係$$R: S \rightarrow S$$為具有反身性、反對稱性與遞移性的二元關係，則$$R$$為一偏序關係(partial order relation)。
>
> * 反身性\[reflexive] $$\forall x \in S, xRx$$
> * 反對稱性\[anti-symmetric] $$\forall x,y\in S, \ xRy \land yRx \Rightarrow x=y$$
> * 遞移性\[transitive] $$\forall x,y,z\in S, \ xRy \land yRz \Rightarrow xRz$$
>
> 稱$$(S,R)$$為偏序集。
>
> 偏序集即定義二元關係R使得集合S內，**部分元素**可比較大小即成立。但集合內可能存在無法比較大小的元素。

* 例：$$(S,R)=(\mathbb{R}^2, \preceq)$$ (element ordering)
* 例:  $$(S,R)=(\mathbb{N}, \leq)$$
* 例：$$(S,R)= (\text{set}, \subseteq)$$

### 相容(comparable)

> 令$$(S, \leq)$$為一偏序集，$$x,y\in S$$且$$x \neq y$$，若$$x \leq y$$與$$y \leq x$$恰有一成立，則稱$$x$$與$$y$$<mark style="color:red;">相容</mark>，否則稱$$x$$與$$y$$不相容(incomparable)。

由定義知偏序集中，<mark style="color:blue;">相容的兩個元素即為可以比較大小的兩個元素</mark>。

## 全序集(total order set)

> 令$$(S, \leq)$$為一偏序集，<mark style="color:red;">若</mark>$$S$$<mark style="color:red;">中任意兩元素均相容</mark>，則稱$$\leq$$為全序關係，且$$(S, \leq)$$為全序集。

由定義知全序集中，任意兩個元素均可以比較大小。

自然數集、整數集、有理數集、無理數集、實數集均為全序集。

## 小於(less than)

## 良序集(well order set)

> 令$$(S, \leq)$$為偏序集，$$\forall x,y \in S$$且$$x \neq y$$則 $$x < y$$。

> 若$$(S, \leq)$$為全序集，則$$S$$的任一非空子集合必含一最小元素時，為$$S$$為良序集。

## 三一律(trichotomy rule)

自然數集$$\mathbb{N}$$為良序集。

> $$x,y,z \in \mathbb{R}$$，則$$x > y, \ x=y,\ x< y$$恰有一成立。

## 集合有上(下)界(bounded above, below)

> $$(S,\leq)$$為偏序集，$$\emptyset \neq E \subseteq S$$為非空子集合。
>
> * 若$$\exists b \in S \ni \forall x \in E,\ x \leq b$$，稱$$b$$為集合$$E$$的上界。
> * 若$$\exists a \in S \ni \forall x \in E,\ a \leq x$$，稱$$a$$為集合$$E$$的下界。

上、下界不必為集合$$E$$中的元素，因為當$$E$$為度量空間中的開集合或非連續集合時，可能無法直接用集合內的元素定義上下界。

如$$E=\{x \in \mathbb{Q} | 0 \leq x^2 \leq 2 \}$$，$$E$$為有理數集合，而上界為$$\sqrt{2}$$是無理數。
