# ARIMA

## 簡介

數平滑和 ARIMA 模型是兩種最廣泛使用的時間序列預測方法，並為該問題提供了補充方法。<mark style="color:red;">指數平滑模型基於對數據趨勢和季節性的描述，而 ARIMA 模型旨在描述數據中的自相關</mark>。

在時間序列模型中，無法被固定趨勢或是季節性所解釋的部份，稱之為波動(cycles)或是稱做不規則部(irregular part)。假設此波動為定態，則常以線性的ARMA模型建模。

## 一階自我迴歸模型：AR(1)

> $$y_t = b_0 + b_1 y_{t-1}+\epsilon_t$$，
>
> 其中$$\epsilon_t \sim WN(0,\ \sigma^2)$$為白噪音且$$\mathrm{E}(\epsilon_t y_{t-j}) > 0, ~\forall j > 0$$

將疊代展開得

$$\displaystyle \begin{aligned} y_t & = b_0 + b_1(b_0 + b_1 y_{t-2} + \epsilon_{t-1}) + \epsilon_t \\     & = b_0(1+b_1) + b_1^2 y_{t-2} + \epsilon_t + b_1 \epsilon_{t-1} \\     & = b_0(1+b_1 +b_1^2 + \dots) + (\epsilon_t + b_1 \epsilon_{t-1} + b_1^2 \epsilon_{t-2}+\dots) +      \lim_{k \rightarrow \infty} b_1^k y_{t-k} \\     & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} +  \lim_{k \rightarrow \infty} b_1^k y_{t-k} \end{aligned}$$

當$$|b_1| <1$$時，可得$$\displaystyle \lim_{k \rightarrow \infty} b_1^k y_{t-k} = 0$$

此時可得$$\displaystyle \begin{aligned} y_t & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\     & = \frac{b_0}{ 1-b_1} + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\     & = \mu + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \end{aligned}$$，其中$$\displaystyle \mu = \frac{b_0}{1-b_1}$$

取期望值可得$$\displaystyle \begin{aligned} \mathrm{E}(y_t) & = \mathrm{E}(\mu) + \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j}) \\      & = \mathrm{E}(\mu) \\      & = \mu, ~ \forall t   \end{aligned}$$，即期望值為常數。

變異數為：$$\displaystyle \begin{aligned} \gamma(0) &= \mathrm{Var}(y_t) \\     & = \mathrm{E}(y_t - \mu)^2 \\     & = \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j})^2 \\     & = \sum_{j=0}^\infty b_1^{2j} \mathrm{E}( \epsilon_{t-j})^2 \\     & = \sum_{j=0}^\infty b_1^{2j} \sigma^2 \\     & = \sigma^2 (1+ b_1^2 + b_1^4+\dots) \\     & = \frac{\sigma^2}{1-b_1^2} < \infty ~ \text{ if } |b_1| < 1  \end{aligned}$$
