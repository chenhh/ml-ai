# 點拓樸集

## 簡介

此為度量空間$$(X,d)$$的點拓樸集，與特定空間的點拓樸集，如$$\mathbb{R}^n$$相比性質較少，但是較為通用。

## 兩集合的距離

> $$A,B \subseteq X$$, $$d(A,B)=\inf \{ d(x,y)| \forall x \in A, ~ y \in B\}$$
>
> • 集合的距離為兩集合間最短的兩點間的距離。

### 兩集合間的距離不滿足三角不等式

* $$d(A,B) > d(A,C) + d(B,C)$$不滿足三角不等式。
* 但$$d(A,B) \leq d(A,C)+d(B,C)+d(C)$$成立



![](../../.gitbook/assets/set_distance.png)

## 點到集合的距離

> $$A \subseteq X$$, $$x \in X$$, $$d(x,A)=\inf d(x,y), ~\forall y \in A$$
>
>  點到集合的距離為點到集合最短兩點間的距離。

* 若$$A$$為閉集合，且$$x\notin A \Rightarrow d(x,A) >0$$

## 集合的直徑（diameter）

> $$S\subseteq X$$, $$d(S)=\sup\{ d(x,y), ~\forall x, y \in S \}$$
>
> $$S$$可為任意形狀的集合，集合$$S$$的直徑為集合中距離最遠兩點的長度。

* 集合的直徑可能為無窮大。例如$$ S=(a,\infty) \text{ or }  (−\infty,b) $$

![&#x96C6;&#x5408;&#x7684;&#x76F4;&#x5F91;&#x70BA;&#x96C6;&#x5408;&#x4E2D;&#x5169;&#x9EDE;&#x7684;&#x6700;&#x9577;&#x8DDD;&#x96E2;](../../.gitbook/assets/set_diameter-min.png)

## 有界集合（bounded set）

> 稱集合$$S$$為有界集合若滿足
>
> * $$\exists M\geq 0 , ~ y \in S \ni d(x,y) <M, \forall x \in S$$
> * 或 $$\exists M \geq 0 \ni  \sup d(x,y) < M, \forall x, y \in S$$
> * 或 $$\exists x \in S \exists r > 0 \ni S \subseteq N_r(S)$$

*  有界集合即集合中任意兩點的距離必定小於某個有限實數$$M$$。
* 無界集合即集合中存在兩點的距離為無窮大。因此必須是有界集合才可定義直徑。

## 鄰域（neighborhood）

> 給定點$$a\in S$$與半徑$$r > 0$$，則點$$a$$以$$r$$為半徑的鄰域（neighborhood of a with radius r）記為 $$N_a(r) \equiv N(a,r)=\{b \in S | d(a,b) < r\}$$

* 注意$$N_a (r)$$包含了以$$a$$為圓心，$$r$$為半徑中，所有屬於集合$$S$$中的點，但不包含圓周上的點。
* **鄰域的定義中使用**$$d(a,b)$$**，因此只要符合距離測度的函數即可**。所以鄰域不一定是以$$a$$為中心的圓形，可能是菱形$$d(a,b)=|a−b|$$或是其它形狀。

![&#x9130;&#x57DF;](../../.gitbook/assets/neighborhood.jpg)

## 內點（interior point）

> 稱點$$a \in S$$為集合$$S$$的內點若存在以$$a$$為中心的鄰域$$N_a(r)$$為$$S$$的子集合。$$\exists r > 0 \ni N_a(r) \subseteq S$$。
>
> 集合$$S$$中所有內點形成的集合記為$$int(S)$$

* 若點$$a$$恰好位於集合$$S$$的邊界上，則不存在符合上述定義的半徑$$r$$，因此不為內點；
* 反之若點$$a$$在集合$$S$$內，則一定可以找到滿足上述定義的半徑$$r$$

### 內點的性質

> 給定度量空間$$(X,d)$$與子集合$$A,B \subseteq X$$，則
>
> 1. $$A\subset B \Rightarrow int(A) \subset int(B)$$
> 2. $$int(A\cap B)=int(A) \cap int(B)$$
> 3. $$int(A) \cup int(B) \subset int(A \cup B)$$
> 4. $$int(A)=X-\overline{X-A}$$，$$\overline{X-A}$$為$$X-A$$的閉包（closure）。
> 5. $$int(X-A)=X-\overline{A}$$
> 6. $$int(int(A))=int(A)$$
> 7. $$int(\cap_{i=1}^nA_i)=\cap_{i=1}^n(int(A_i)), ~ A_i \subseteq X$$
> 8. $$int(\cap_{i=1}^{\infty} A_i) \subseteq \cap_{i=1}^{\infty}(int(A_i)), ~ A_i \subseteq X$$
> 9. $$\cup_{i=1}^{\infty} (int(A_i)) \subseteq int(\cup_{i=1}^{\infty} A_i), ~ A_i \subseteq X$$
> 10. 若$$A$$在$$X$$中為開集合或閉集合，令$$\partial(A)$$為$$A$$的邊界點，則$$int(\partial A)=\emptyset$$，
> 11. 若$$int(A)=int(B)=\emptyset$$，則$$A$$在$$X$$為閉集合，則$$int(A \cup B)=\emptyset$$

