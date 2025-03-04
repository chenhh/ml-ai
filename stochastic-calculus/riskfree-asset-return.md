---
description: compounded return
---

# 無風險資產報酬

## 時間價值

貨幣的時間價值：今天的1元比一年後(未來)的1元價值高。

因為投資人可以利用這1美元做投資，如果要把錢交給他人，就要考慮利息(interest)。

假設利率$$r$$為常數，可分為單利(simple interest)與複利(compound interest)兩種基本類型。

複利還可分成離散複利(discretely compounded)與連續複利(continuously compounded)。

## 單利(simple interest)

一定量的資金(<mark style="color:red;">本金</mark> $$P$$, principal)存入銀行，將得到<mark style="color:red;">利息(interest)</mark>。

單利是只考慮利息由本金產生的情況，假設年利率$$r >0$$，

* 一年後的利息為$$rP$$，因此投資組合的價值為$$v_{(p),1}=P+rP=(1+r)P$$。
* 兩年後為$$v_{(p), 2}=(1+r)P + rP=(1+2r)P$$。
* $$n$$年後為$$v_{(p), n}=(1+nr)P$$。
* 如果以天計息時，每日利息為$$\frac{r}{365}P$$，因此$$n$$日後的利息為$$\frac{nr}{365}P$$。

因此得$$t \in \mathbb{R}^{+} ~ v_{(p),t}=(1+tr)P$$，其中$$t=1$$為一年。$$(1+tr)$$為<mark style="color:red;">成長因子(growth factor)</mark>。

如果是在時間$$s<t$$開始投資，則在$$t$$時的價值為$$v_{(p), t}=(1+(t-s)r)P$$。

#### 範例

本金150元，存款20天，年利率8%的單利，則20天後的價值為$$v_{(p), 20/365}=(1+20/365\times 0.08)\times 150=150.66$$。

#### 範例

本金$$P$$存入銀行91天，以8%單利計息，期末拿回1000元，則$$(1+91/365 \times 0.08)\times P =1000$$，$$P=980.44$$。

### 離散複利

假設在銀行存入1元，利率為$$r$$，每年付利息一次，則一年後可得：$$1\times(1+r)$$元。

兩年後可得$$1 \times (1+r)^2$$元。以上為離散複利的概念。

### 連續複利

如果每年複利$$m$$次，且每期利率為$$r/m$$，則一年後可得$$(1+\frac{r}{m})^m$$元。

考慮$$\displaystyle \lim_{m \rightarrow \infty} (1+\frac{r}{m})^{m}=e^{m \log(1+\frac{r}{m})} \approx e^r$$。

同理在$$t$$年後可得$$e^{rt}$$元，此為連續複利的概念。

連續複利也可用微分方程得到。假設時間$$t$$在銀行的存款為$$M(t)$$元，而經過一小段時間$$dt$$後，銀行存款變為$$M(t+dt)$$元，而這段時間存款變化量為：$$M(t+dt)-M(t) \approx \frac{dM}{dt}dt+ \dots$$。

而利息與本金$$M$$，利率$$r$$和時間間隔$$dt$$成比例，因此$$\frac{dM}{dt}dt = rM(t) dt$$。

可得常微分方程$$\frac{dM}{dt}=rM(t)$$，因此可得$$M(t)=M(0)e^{rt}$$。

## 複利(compounded return)

複利有兩種形式：離散與連續複利。

#### 離散複利

假設在銀行存入$$p$$元，年利率為$$r$$，每年付息，則$$n$$年後總額為$$p(1+r)^n$$元。

如果每年複利$$m$$次，且每期依利率$$\frac{r}{m}$$支付，則$$n$$年後總額為：$$p(1+\frac{r}{m})^{mn}$$

#### 連續複利

$$\displaystyle e^x = \lim_{m \rightarrow \infty} \left(1+\frac{x}{m} \right)^m$$

如果支付利息次數增加，上式可改寫為：$$\displaystyle \lim_{m \rightarrow \infty} p\left(1+\frac{r}{m} \right)^{mn}=e^{mn \log (1+\frac{r}{m})} \approx e^{nr}$$

## 報酬(return)

第$$t$$日資產價格為$$S_t$$，則第$$t$$日至$$t+1$$日報酬率(不考慮除權息)為$$r_t = \frac{S_{t+1}}{S_t}-1$$。

也可用連續複利方式計算$$r_t \approx \log\frac{S_{t+1}}{S_t}$$

收集$$M$$日的報酬可得均值與標準差為：

* $$\displaystyle \overline{r} = \frac{1}{M} \sum_{t=1}^M r_t$$
* $$\displaystyle \hat{\sigma}=\left( \frac{1}{M-1} \sum_{t=1}^M (r_t - \overline{r})\right)^{1/2}$$

通常日報酬率的均值會比標準差小很多，因此日交易資料中的噪音很大。

<mark style="color:red;">為了建模，假設報酬率符合常態分佈(實證研究中分佈通常不是常態分佈)，因此可將報酬率視為隨機變數</mark>$$r_t \sim N(\overline{r}, \hat{\sigma})$$。
