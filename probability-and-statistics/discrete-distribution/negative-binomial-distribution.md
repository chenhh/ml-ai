---
description: Negative binomial distribution
---

# 負二項分佈

「負二項式分佈」與「二項分佈」的區別在於：

* 二項分佈是固定試驗總次數$$N$$的獨立試驗中，成功次數$$k$$的機率分佈；
* 負二項分布是所有到成功$$r$$次時即終止的獨立試驗中，失敗次數$$k$$的機率分佈。

### 分佈與統計量

* 隨機變數$$X \sim NB(r, p)$$
* 機率質量函數$$f(k | r,p)≡\mathrm{P}⁡(X=k)=\binom{k+r-1}{k}p^k(1-p)^r, ~ k=-0,1,2,\ldots$$
  * 已知一個事件在Bernouli試驗中每次的出現機率是$$p$$，在一連串試驗中，一件事件剛好在第$$r+k$$次試驗出現第$$r$$次成功的機率。
  * 已確定第$$r+k$$次試驗為成功，所以第1次至第$$r+k-1$$次試驗所有可能的情形為$$r−1$$次成功與$$k$$次失敗試驗的排列組合個數，共有$$\binom{r+k-1}{k}$$種組合。
