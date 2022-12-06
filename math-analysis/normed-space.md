---
description: normed space
---

# 賦範空間(normed space)

範數最先由向量模長中推廣，從向量模長這一特殊的例子推廣更一般線性空間中的範數。因此，需將範數最本質的特點提煉出來，即：非負、正定、正齊次（數乘）和三角不等式（正齊次由線性空間性質決定）。以上四個性質相互獨立，無法互相推導，作為定義線性空間中的範數的最基本性質。

從範數公理性的四個性質，不難得到其與距離空間的四個性質是等價的。也就是說，<mark style="color:red;">**範數滿足距離的定義**</mark>，賦範空間也是一類特殊的距離空間，該距離空間距離函數由範數誘導。

![賦範空間為度量空間的特例](../.gitbook/assets/250px-Mathematical\_Spaces-min.png)

## 賦範向量(線性)空間

> 令$$X$$義定義在體$$F$$上的向量空間（線性空間），如果函數$$\| \cdot\|: X \rightarrow \mathbb{R}$$滿足$$\forall u,v \in X, c\in F$$：
>
> * $$\| v\| \geq 0$$且$$\| v \| = 0 \Leftrightarrow v=0$$
> * $$\| cv\| = |c| \|v\|$$
> * $$\|u+v\| \leq \|u\| + \|v\|$$
>
> 則稱$$X$$為賦範線性空間，$$\| \cdot\|$$為範數。
>
> 如果定義距離函數$$d(x,y)=\|x-y\|$$，稱為<mark style="color:red;">由範數誘導的度量(metric induced by norm)</mark>，因此賦範空間必為度量空間。

#### 常見的賦範線性空間

<mark style="color:red;">歐式空間</mark>$$\mathbb{R}^n, ~n < \infty$$與$$\|x\|=(|x_1|^2+|x_2|^2+\dots +|x_n|^2)^{\frac{1}{2}}$$。

* 註：在計算範數時，元素取絕對值的原因是若元素為複數時，取絕對值才是表示向量的長度，而實數在冪次方為奇數時也需要保留避免負數的影響。

<mark style="color:red;">連續函數空間</mark>$$C[0,1]$$，

* $$\displaystyle \|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$$，範數為函數在$$x\in[0,1]$$的最小上界值。
* $$\displaystyle \|f\|_1 = \int_0^1 |f(x)|dx$$，範數為函數在$$x\in[0,1]$$的積分值。

### 線性轉換

> 賦範線性空間$$(X, \|\cdot\|), (Y, \|\cdot\|)$$，映射$$T: X\rightarrow Y$$稱為線性轉換（算子）若滿足：
>
> 1. $$\forall u,v \in X, a,b \in F$$，$$T(ax+by)=aT(x)+bT(y)$$
> 2. $$\forall c \geq 0, \forall x \in X$$，$$\|Tx\| \leq c\|x\|$$
>
> 所有滿足條件2的常數$$c$$之最小值稱為$$T$$的範數，記為$$\|T\|$$，可得 $$\displaystyle \|T\|=\sup_{\|x\|=1}\|Tx\|=\sup_{\|x\|\leq 1} \|Tx\|=\sup_{x \neq 0} \frac{\|Tx\|}{\|x\|}$$。

### 線性轉換的性質

> 賦範線性空間$$(X, \|\cdot\|), (Y, \|\cdot\|)$$，映射$$T: X\rightarrow Y$$稱為有界線性變換（算子），則以下條件等價：
>
> * $$T$$在某一點連續；
> * $$T$$在所有點連續；
> * $$T$$有界；
> * $$S \subseteq  X$$為有界集，則$$T(S) \subseteq Y$$為有界集。

## 完備賦範空間(Banach)空間

> 若賦範空間$$(X, \| \cdot\|)$$中，範數$$\| \cdot\|$$誘導的距離函數$$d(x,y)$$是完備的度量空間$$(X,d)$$時，則稱$$(X,\|\cdot\|)$$為完備賦範空間。
>
> 完備賦範空間稱為Banach空間。

例如：

* 歐式空間$$(\mathbb{R}^n, \|x\|_2)$$為完備賦範空間。
* 連續函數空間$$(C[a,b], d_1(f,g)), ~ d_1(f,g)=\sup_{a \leq x \leq b}|f(x)-g(x)|$$為完備賦範空間。
*

## Lp空間

> * $$C[a,b]$$是定義域為實數區間$$[a,b]$$上連續函數全體所成的集合。
> * 定義範數 $$\displaystyle \| f\|_p = \bigg( \int (f)^pdx \bigg)^{\frac{1}{p}}, ~ 1 \leq p \leq \infty$$
> * 距離為$$d(f,g)=\| f -g \|_p$$
>
> 成為一個賦範空間。但該賦範空間是不完備，即連續函數可能（點態）收斂為不連續函數。

