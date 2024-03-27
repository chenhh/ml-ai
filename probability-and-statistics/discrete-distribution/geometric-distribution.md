---
description: geometric distribution
---

# 幾何分佈

參數$$N,p$$意義同二次分佈，如果需要知道嘗試多次，能取得第一次成功的機率，則為幾何分佈，如：射擊，首次擊中目標時的次數。有兩種型式：

* 在伯努利試驗中，得到第一次成功所需要的試驗次數$$X$$。$$X$$的值域是$$\{ 1, 2, 3, \ldots \}$$。
  * 如果每次試驗的成功機率是$$p$$，那麼$$k$$次試驗中，第$$k$$次才得到成功的機率是$$\mathrm{P}(X=k)=(1-p)^{k-1}p$$, $$k=1,2,\cdots$$。
* 在得到第一次成功之前所經歷的失敗次數$$Y = X − 1$$。$$Y$$的值域是$$\{0,1,2,3,\ldots\}$$。
  * $$\mathrm{P}(Y=k)=(1-p)^k p$$, $$k=0,1,2,\ldots,$$。

實際使用中指的是哪一個取決於慣例和使用方便。這兩種分布不應該混淆。前一種形式（$$X$$的分布）經常被稱作shifted geometric distribution；但是，為了避免歧義，最好明確地說明取值範圍。

### 分佈與統計量

* 隨機變數 $$X \sim G(p)$$
* 期望值 $$\mathrm{E}(X)=\frac{1}{p}$$
* 變異數 $$\mathrm{Var}(X)=\frac{1-p}{p^2}$$

### 幾何分布具有非記憶性的性質（Memoryless Property）

如果一個隨機變數呈幾何分布，它的條件機率遵循：$$\displaystyle \mathrm{P}(T>s+t\;|\;T>t)= \mathrm{P}(T>s) ~ \forall s, t  \in \mathbb{N}.$$
