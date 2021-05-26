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







