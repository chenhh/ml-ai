# Black-Scholes方程式

## Black-Scholes隨機方程式

> $$ \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 \frac{\partial^2 V}{\partial S^2} + \gamma S \frac{\partial V}{\partial S} - \gamma V = 0 $$

其中:
* $$ S \equiv S(t) $$為標的資產在時間$$t$$的價格。
* $$ V \equiv V(S,t) $$為資產$$S$$在時間$$t$$選擇權$$V$$的價格。
* $$ \sigma^2$$為標的資產價格歷史波動率(historical volatility)，或者已經$$V$$時反推得到的隱含波動率(implied volatility)。
* $$ \gamma$$為無風險報酬(risk-free return)。
