# 區間估計(interval estimation)

## 簡介

在估計方法中，點估計是針對未知參數$$\theta$$提供單一的推估值。而區間估計 （interval estimation）則著重在建立一個未知參數$$\theta$$可能出現的範圍 （區間） 。點估計的結果雖然較為明確，但區間估計則提供較具彈性的推估結果。

信賴係數與信賴區間


未知參數$$\theta$$ 的信賴區間 (confidence interval) 是參數空間中的某個具有隨機邊界的區間 $$(a,b)$$，而且這個區間包括$$\theta$$ 的機率為正值。

通常$$a , b$$ 是由$$\theta$$ 的某個點估計式$$\hat{\theta}$$所決定。$$\mathrm{P}(a \leq \theta \leq b)=r$$ 表示在信賴係數 (confidence coefficient) $$r$$之下，未知參數$$\theta$$的信賴區間為 $$(a,b)$$。即我們對於未知參數$$\theta$$ 會落在區間 $$(a,b)$$內有 $$(100\times r) \%$$的信心。

### 例：常態分佈，平均值未知，變異數已知

* $$X_1, X_2, \ldots, X_N \sim N(\mu, \sigma^2)$$, $$\mu$$ 未知，$$\sigma$$已知，求其95%的信賴區間。
* 已知 $$\frac{\sqrt{N} (\overline{x}_N - \mu)}{\sigma} \sim N(0,1)$$
* $$\displaystyle \mathrm{P} \bigg( -1.96 \leq \frac{\sqrt{N} (\overline{x}_N - \mu)}{\sigma}  \leq 1.96 \bigg) = 0.95$$
* 可得95%信賴區間為 $$(\overline{x}_N-1.96 \frac{\sigma}{\sqrt{N}}, ~ \overline{x}_N+1.96 \frac{\sigma}{\sqrt{N}})$$。

### 例：常態分佈，平均值與變異數均未知

* 已知$$\frac{\sqrt{N} (\overline{x}_N - \mu)}{\sigma} \sim  t(N-1)$$，令$$N=20$$
* $$\mathrm{P} ( -2.093\leq \frac{\sqrt{N} (\overline{x}_N - \mu) }{s_N} \leq  2.093) = 0.95$$
* 可得95%信賴區間為 $$(\overline{x}_N-2.093 \frac{s_N}{\sqrt{N}}, ~ \overline{x}_N+1.96 \frac{s_N}{\sqrt{N}})$$

