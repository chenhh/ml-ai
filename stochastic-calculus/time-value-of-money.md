---
description: time value of money
---

# 貨幣的時間價值

## 時間價值

貨幣的時間價值：今天的1元比一年後的一元價值高。

因為投資人可以利用這1美元做投資，如果要把錢交給他人，就要考慮利息(interest)。

假設利率$$r$$為常數，可分為單利(simple interest)與複利(compound interest)兩種基本類型。

複利還可分成離散複利(discretely compounded)與連續複利(continuously compounded)。

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

