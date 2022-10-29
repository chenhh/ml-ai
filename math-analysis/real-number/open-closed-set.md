---
description: open and closed set
---

# 開集與閉集

## 簡介

定義開集合或閉集合，需要用到距離的概念，因此至少需要定義集合中兩點的度量(metric)。
由於$$\mathbb{R}^n$$與$$\mathbb{R}$$在開集與閉集兩者性質通用，因此直接以$$\mathbb{R}^n$$定義。

## 度量函數(metric function)
> 集合$$\mathbb{R}^n$$的函數$$d: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}^{+}$$
> 滿足以下三個條件時，稱為度量函數。
> * [非負性] $$\forall x, y \in \mathbb{R}^n, ~ d(x,y) \geq 0$$, 且$$d(x,y) =0 \Leftrightarrow x=y$$。
> * [交換性] $$\forall x, y \in \mathbb{R}^n, ~ d(x, y) = d(y, x)$$。
> * [三角不等式] $$\forall x, y, z \in \mathbb{R}^n, ~ d(x,y) \leq d(x, z) + d(z, y)$$。

歐式空間常用的度量函數為$$d(x,y)=\lVert x-y \rVert = (\sum_{i=1}^n (x_i - y_i)^2)^{1/2}$$。

## 開球(open ball)
> 令點$$x \in \mathbb{R}^n$$且半徑$$r > 0$$
> * $$B_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) < r \}$$ 是以$$x$$為圓心，半徑為$$r$$開球
>   (open ball with center $$x$$ and radius $$r$$)。
> * $$\overline{B_r}(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y) \leq r \}$$ 是以$$x$$為圓心，半徑為$$r$$閉球
>   (closed ball with center $$x$$ and radius $$r$$)。
> * $$S_r(x) \equiv N_r(x) = \{ y \in \mathbb{R}^n ~|~ d(x,y)  r \}$$ 是以$$x$$為圓心，半徑為$$r$$的球面
>   (sphere with center $$x$$ and radius $$r$$)。

實數$$\mathbb{R}$$
* 開球$$B_r(x)$$即為開區間$$(x-r, x+r)$$。
* 閉球$$\overline{B_r}(x)$$即為閉區間$$[x-r, x+r]$$。
* 球面$$S_r(x)$$即為兩個點的集合$$\{x-r, x+r\}$$。

平面$$\mathbb{R}^2$$
* 開球$$B_r(x)$$為$$x$$為圓心，半徑為$$r$$的圓的內部。
* 閉球$$\overline{B_r}(x)$$為$$x$$為圓心，半徑為$$r$$的圓形區域。
* 球面$$S_r(x)$$為$$x$$為圓心，半徑為$$r$$的圓周。

## 內點(interior point)
> 令$$S \subseteq \mathbb{R}^n$$且$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的內點若存在$$r >0 \ni B_r(x) \subseteq S$$。
> * 集合$$S$$所有的內點形成的集合記為$$S^0$$。

### 內點集為集合的子集
> $$\forall S \subseteq \mathbb{R}^n$$, 可得$$S^0 \subseteq S$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

## 外點(exterior point)
> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \subseteq \mathbb{R}^n - S$$。
> * 集合$$S$$所有的外點形成的集合記為$$S^e$$。

## 外點集為集合補集的內點集
> $$\forall S \subseteq \mathbb{R}^n$$, $$S^e = (\mathbb{R}^n - S)^0$$ 且 $$S^e \subseteq \mathbb{R}^n - S$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

## 邊界點(boundary point)
> 令$$S \subseteq \mathbb{R}^n$$，若$$x \in \mathbb{R}^n$$。
> * $$x$$為集合$$S$$的外點若存在$$r >0 \ni B_r(x) \cap {R}^n \neq \empty$$且  $$B_r(x) \cap {R}^n - S \neq \empty$$。
> * 集合$$S$$所有的邊界點形成的集合記為$$S^b$$。

### 集合與其補集的邊界集相同
> $$\forall S \subseteq \mathbb{R}^n$$, $$S^b = (\mathbb{R}^n - S)^b$$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>

## 內點集、外點集、邊界集為歐式空間的分割
>  $$\forall S \subseteq \mathbb{R}^n$$
> * $$S^0 \cap S^e = \empty$$, $$S^0 \cap S^b = \empty$$, $$S^b \cap S^e = \empty$$。
> * $$S^0 \cup S^e  \cup S^b= \mathbb{R}^n $$。

<details>

<summary>proof: 由定義直接證明</summary>

</details>