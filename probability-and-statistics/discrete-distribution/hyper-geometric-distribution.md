---
description: Hyper-geometric distribution
---

# 超幾何分布

它描述了由有限個物件中抽出$$n$$個物件，成功抽出$$k$$次指定種類的物件的機率（抽出不放回 （without replacement））。

假設袋子中有$$N$$個球，其中有$$K$$個白球，$$N-K$$個非白球，則從袋中隨機取$$n$$個球，每次取後不放回，令隨機變數$$X$$為取中白球的個數。

### 分佈與統計量

* 隨機變數$$X \sim H(N,K,n)$$
* 機率質量函數為 $$\mathrm{P}(X=x |N, K, n) =\frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}}, ~ \max\{0, n-N+k\} \leq x \leq \min \{n, k\}$$
  * &#x20;因為最多取$$n$$個球，且白球只有$$K$$個，所以x的上限為$$\min⁡\{n,K\}$$。
  * &#x20;取中非白球的數量$$n−x$$不能超過全部非白球數量$$N−K$$，即$$n−x \leq N−K \Rightarrow x \geq n−N+K$$。
* 期望值 $$\mathrm{E}(X) = \frac{nK}{N}$$
* 變異數 $$\mathrm{Var}(X) = \frac{nK(N-n)(N-K)}{N^2 (N-1)}$$
