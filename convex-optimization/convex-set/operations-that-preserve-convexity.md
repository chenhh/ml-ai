---
description: operations that preserve convexity
---

# 保凸運算

## 簡介

可用凸集構造出其它凸集。常用保凸運算如下：

* 交集
* 仿射函數
* 透射函數(perspective function)
* 線性分式函數(linear-fractional function)

## 交集(intersection)

> 若$$S_1, S_2$$為凸集合，則$$S_1 \cap S_2$$也是凸集合。
>
> 若$$\{ S_i\}, ~i\in \mathbb{N}$$為凸集合，則$$\cap_{i\in \mathbb{N}}S_i$$為凸集合。(註空集合為凸集合)。
>
> 閉凸集合$$S$$為包含該集合之半空間的交集， $$S=\bigcap \{ H ~|~ H \text{ halfspace }, S \subseteq  H\}$$。

例：

* 多面體(polyhedra)為多個半空間與超平面的交集。
* 正半定錐可寫為$$\bigcap_{z \neq 0}\left\{  X \in \mathbb{S}^n ~|~ z^{\top} X z \geq 0\right\}$$為無限多個半空間的交集。

## 仿射函數(affine function)

> $$f: \mathbb{R}^n \rightarrow \mathbb{R}^m, ~ f(x)=Ax+b, ~ A \in \mathbb{R}^{m \times n}, ~ b \in \mathbb{R}^m$$為仿射函數。
>
> 若$$S \in \mathbb{R}^n$$為凸集合，則映射集(image)$$f(S) =\{f(x)~|~ x \in S\}$$為凸集合。
>
> 若$$g: \mathbb{R}^k \rightarrow \mathbb{R}^n$$為仿射函數，則前像(pre-image) $$g^{-1}(S)=\{x | f(x)=S\}$$為凸集合。

* <mark style="color:red;">多面體(polyhedron}</mark> $$\{x ~|~ Ax \preceq b, Cx=d\}   =\{x~|~ f(x) \in \mathbb{R}_{+}^m \times \{0\}\}$$可表示以函數$$f(x)＝(b-aX, d-Cx)$$時，第一象限(含x,y軸與原點)的前像。
* <mark style="color:red;">線性矩陣不等式的解集合</mark>為凸集合，為正半定錐在仿射函數的前像。
  * 不等式：$$A(x)=x_1 A_1 + \dots + x_n A_n \preceq B$$，$$B, A_i \in S^m$$　（m階對稱矩陣）。
  * 解集合$$\{x~|~ A(x) \preceq B\}$$凸集合，為仿射函數$$f(x)=B-A(x), f: \mathbb{R}^n \rightarrow S^m$$的前像。

### 縮放與平移(scaling and translation)

若$$S \in \mathbb{R}^n$$為凸集合，$$c \in \mathbb{R}, a \in \mathbb{R}^n$$，則

* 縮放：$$cS=\{cx~|~ x \in S\}$$為凸集合。
* 平移：$$S+a=\{x+a~|~ x \in S\}$$為凸集合。

### 投影(projection)

<mark style="color:red;">一個凸集在其某些座標上的投影仍然是凸集</mark>。

若$$S \in \mathbb{R}^m \times \mathbb{R}^n$$為凸集合，則$$T=\{x_1 \in \mathbb{R}^m ~|~ (x_1, x_2) \in S, \text{ for some } x_x \in \mathbb{R}^n \}$$為凸集合。

### 和集(sum of two sets)

<mark style="color:red;">兩個凸集合的和集仍為凸集合</mark>。

兩個集合的和定義為：$$S_1+S_2 = \{x+y~|~ x \in S_1, y \in S_2\}$$。

若$$S_1, S_2$$為凸集合，則和集$$S_1+S_2$$也為凸集合。

範例：卡式積 $$S_1 \times S_2 = \{ (x_1, x_2) ~|~ x_1 \in S_1, x_2 \in S_2\}$$，其映射集由線性函數$$f(x_1, x_2)=x_1+x_2$$得出。若$$S_1, S_2$$為凸集合，則映射集為和集，所以為凸集合。

### 部份和集(partial sum of sets)

$$S_1, S_2 \in \mathbb{R}^n \times \mathbb{R}^m$$，定義$$S=\{(x, y_1+y_2) ~|(x, y_1) \in S_1, ~(x,y_2) \in S_2 \}$$，其中$$x \in \mathbb{R}^n, y_i \in \mathbb{R}^m$$。

當$$m=0$$時，部分和集等價於為兩集合的交集。

當$$n=0$$時，部分和集等價於和集。

<mark style="color:red;">因此當</mark>$$S_1, S_2$$<mark style="color:red;">為凸集合時，部分和集</mark>$$S$$<mark style="color:red;">為凸集合</mark>。

### 雙曲錐(hyperbolic cone)

雙區錐　$$H=\{x ~|~ x^\top P x \leq (c^\top x)^2, ~ c^\top x \geq 0\}$$，$$P \in S_{+}^n$$為n階非負對稱矩陣，$$c \in \mathbb{R}^n$$，則$$H$$為凸集合。

因為$$H$$是仿射函數$$f(x)=(P^{1/2}x, c^\top x)$$，二次錐$$\{(z,t) ~|~ z^\top z \leq t^2, t \geq 0\}$$的前像。

### 橢圓(ellipsoid)

橢圓$$E=\{x~|~ (x-x_c)^\top P^{-1} (x-x_c) \leq 1\}, P \in S_{++}^n$$為單位圓$$\{u ~|~ \|u\|_2 \leq 1\}$$在函數$$f(u)=P^{1/2}u+x_c$$的值域。

橢圓也是單位圓在函數$$g(x)=P^{-1/2}(x-x_c)$$的前像。

