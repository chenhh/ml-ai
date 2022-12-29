---
description: compounded return
---

# 複利

## 複利(compounded interest return)

複利有兩種形式：離散與連續複利。

假設在銀行存入$$p$$元，年利率為$$r$$，每年付息，則$$n$$年後總額為$$p(1+r)^n$$元。

如果每年複利$$m$$次，且每期依利率$$\frac{r}{m}$$支付，則$$n$$年後總額為：$$p(1+\frac{r}{m})^{mn}$$

如果支付利息次數增加，上式可改寫為：$$\displaystyle \lim_{m \rightarrow \infty} p(1+\frac{r}{m})^{mn}=e^{mn \log (1+\frac{r}{m})} \approx e^{nr}$$

## 報酬(return)

第$$t$$日資產價格為$$S_t$$，則第$$t$$日至$$t+1$$日報酬率(不考慮除權息)為$$r_t = \frac{S_{t+1}}{S_t}-1$$。

收集$$T$$日的報酬可得均值與標準差為：

* $$\displaystyle \overline{r} = \frac{1}{T} \sum_{t=1}^T r_t$$
* $$\displaystyle \hat{\sigma}=\left( \frac{1}{T-1} \sum_{t=1}^T (r_t - \overline{r})\right)^{1/2}$$

通常日報酬率的均值會比標準差小很多，因此日交易資料中的噪音很大。

<mark style="color:red;">為了建模，假設報酬率符合常態分佈(實證研究中分佈通常不是常態分佈)，因此可將報酬率視為隨機變數</mark>$$r_t \sim N(\overline{r}, \hat{\sigma})$$。

若將取樣週期縮短，時間步長記為$$\delta t$$，則報酬率均值與時間步長成比例。

&#x20;









