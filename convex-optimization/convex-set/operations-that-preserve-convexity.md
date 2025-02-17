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

### 縮放與平移(scaling and translation)

若$$S \in \mathbb{R}^n$$為凸集合，$$c \in \mathbb{R}, a \in \mathbb{R}^n$$，則

* 縮放：$$cS=\{cx~|~ x \in S\}$$為凸集合。
* 平移：$$S+a=\{x+a~|~ x \in S\}$$為凸集合。

### 投影(projection)

一個凸集在其某些座標上的投影仍然是凸集。

若$$S \in \mathbb{R}^m \times \mathbb{R}^n$$為凸集合，則$$T=\{x_1 \in \mathbb{R}^m ~|~ (x_1, x_2) \in S, \text{ for some } x_x \in \mathbb{R}^n \}$$為凸集合。

### 和集(sum of two sets)

兩個凸集合的和集仍為凸集合

兩個集合的和定義為：$$S_1+S_2 = \{x+y~|~ x \in S_1, y \in S_2\}$$。

若$$S_1, S_2$$為凸集合，則和集$$S_1+S_2$$也為凸集合。

例如：卡式積 $$S_1 \times S_2 = \{ (x_1, x_2) ~|~ x_1 \in S_1, x_2 \in S_2\}$$，其映射集由線性函數$$f(x_1, x_2)=x_1+x_2$$得出。若$$S_1, S_2$$為凸集合，則映射集為和集，所以為凸集合。







