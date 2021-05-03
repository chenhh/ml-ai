# 偏序集或全序集

## 偏序集\(partial order set\)

> $$S\neq \emptyset$$，令關係$$R: S \rightarrow S$$為具有反身性、反對稱性與遞移性的二元關係，則$$R$$為一偏序關係\(partial order relation\)。
>
> * 反身性\[reflexive\] $$\forall x \in S, xRx$$
> * 反對稱性\[anti-symmetric\] $$\forall x,y\in S, \ xRy \land yRx \Rightarrow x=y$$
> * 遞移性\[transitive\] $$\forall x,y,z\in S, \ xRy \land yRz \Rightarrow xRz$$
>
> 稱$$(S,R)$$為偏序集。
>
> 偏序集即定義二元關係R使得集合S內，**部分元素**可比較大小即成立。但集合內可能存在無法比較大小的元素。

* 例：$$(S,R)=(\mathbb{R}^2, \preceq)$$ \(element ordering\)
* 例:  $$(S,R)=(\mathbb{N}, \leq)$$
* 例：$$(S,R)= (\text{set}, \subseteq)$$

### 相容\(comparable\)

> 令$$(S, \leq)$$為一偏序集，$$x,y\in S$$且$$x \neq y$$，若$$x \leq y$$與$$ y \leq x$$恰有一成立，則稱$$x$$與$$y$$相容，否則稱$$x$$與$$y$$不相容\(incomparable\)。

由定義知偏序集中，相容的兩個元素即為可以比較大小的兩個元素。

## 全序集\(total order set\)

> 令$$(S, \leq)$$為一偏序集，若$$S$$中任意兩元素均相容，則稱$$\leq$$為全序關係，且$$(S, \leq)$$為全序集。

由定義知全序集中，任意兩個元素均可以比較大小。

