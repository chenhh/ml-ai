# Black-Scholes方程式

## Black-Scholes隨機方程式

> 在時間$$t$$，資產與選擇權價格關係如下：
>
> $$\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 \frac{\partial^2 V}{\partial S^2} + \gamma S \frac{\partial V}{\partial S} - \gamma V = 0$$

其中:

* $$S \equiv S(t)$$為標的資產在時間$$t$$的價格，$$t$$以年(year)為單位。
* $$V \equiv V(S,t)$$為資產$$S$$在時間$$t$$選擇權$$V$$的價格。如果$$V$$為買權，則$$S$$上漲，$$V$$也會上漲；如果$$V$$為賣權，則$$S$$上漲，$$V$$會下跌。
* $$\sigma^2$$為標的資產價格歷史波動率(historical volatility)，或者已經$$V$$時反推得到的隱含波動率(implied volatility)。
* $$\gamma$$為年化無風險報酬(annualized risk-free return)。

