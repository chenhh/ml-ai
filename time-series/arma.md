# ARIMA

## 簡介

數平滑和 ARIMA 模型是兩種最廣泛使用的時間序列預測方法，並為該問題提供了補充方法。<mark style="color:red;">指數平滑模型基於對數據趨勢和季節性的描述，而 ARIMA 模型旨在描述數據中的自相關</mark>。

在時間序列模型中，無法被固定趨勢或是季節性所解釋的部份，稱之為波動(cycles)或是稱做不規則部(irregular part)。假設此波動為定態，則常以線性的ARMA模型建模。

## 一階自我迴歸模型：AR(1)

> $$y_t = b_0 + b_1 y_{t-1}+\epsilon_t$$，
>
> 其中$$\epsilon_t \sim WN(0,\ \sigma^2)$$為白噪音且$$\mathrm{E}(\epsilon_t y_{t-j}) > 0, ~\forall j > 0$$，即誤差$$\epsilon_t$$只和當期的觀測值$$y_t$$有關。
>
> <mark style="color:red;">而AR(1)為定態的條件為</mark>$$|b_1| < 1$$。

將疊代展開得

$$\displaystyle \begin{aligned} y_t & = b_0 + b_1(b_0 + b_1 y_{t-2} + \epsilon_{t-1}) + \epsilon_t \\     & = b_0(1+b_1) + b_1^2 y_{t-2} + \epsilon_t + b_1 \epsilon_{t-1} \\     & = b_0(1+b_1 +b_1^2 + \dots) + (\epsilon_t + b_1 \epsilon_{t-1} + b_1^2 \epsilon_{t-2}+\dots) +      \lim_{k \rightarrow \infty} b_1^k y_{t-k} \\     & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} +  \lim_{k \rightarrow \infty} b_1^k y_{t-k} \end{aligned}$$

當$$|b_1| <1$$時，可得$$\displaystyle \lim_{k \rightarrow \infty} b_1^k y_{t-k} = 0$$

此時可得

$$\displaystyle \begin{aligned} y_t & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\     & = \frac{b_0}{ 1-b_1} + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\     & = \mu + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \end{aligned}$$，其中$$\displaystyle \mu = \frac{b_0}{1-b_1}$$

<mark style="color:red;">可得AR(1)期望值為常數</mark>：

$$\displaystyle \begin{aligned} \mathrm{E}(y_t) & = \mathrm{E}(\mu) + \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j}) \\      & = \mathrm{E}(\mu) \\      & = \mu, ~ \forall t   \end{aligned}$$

<mark style="color:red;">在</mark>$$|b_1|<1$$<mark style="color:red;">時，變異數收斂</mark>：

$$\displaystyle \begin{aligned} \gamma(0) &= \mathrm{Var}(y_t) \\     & = \mathrm{E}(y_t - \mu)^2 \\     & = \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j})^2 \\     & = \sum_{j=0}^\infty b_1^{2j} \mathrm{E}( \epsilon_{t-j})^2 \\     & = \sum_{j=0}^\infty b_1^{2j} \sigma^2 \\     & = \sigma^2 (1+ b_1^2 + b_1^4+\dots) \\     & = \frac{\sigma^2}{1-b_1^2} < \infty ~ \text{ if } |b_1| < 1  \end{aligned}$$

<mark style="color:red;">在</mark>$$|b_1|<1$$<mark style="color:red;">時，自我共變異數收斂</mark>：

$$\displaystyle \begin{aligned} \gamma(j) &= \mathrm{Cov}(y_t, y_{t-j}) \\     & = \mathrm{E}(y_t - \mu)(y_{t-j} - \mu) \\     & = \mathrm{E}[(\epsilon_{t}+b_1 \epsilon_{t-1}+b_1^2 \epsilon_{t-2}+\dots)                     (\epsilon_{t-j}+ b_1 \epsilon_{t-j-1}+ b_1^2 \epsilon_{t-j-2}+\dots)] \\     & = b_1^j \mathrm{E}(\epsilon_{t-j}\epsilon_{t-j}) +          b_1^{j+1} b_1 \mathrm{E}(\epsilon_{t-j-1}\epsilon_{t-j-1}) +          b_1^{j+2} b_1^2 \mathrm{E}(\epsilon_{t-j-2}\epsilon_{t-j-2}) + \dots \\     & = \sigma^2 b_1^j (1+b_1^2 +b_1^4 + \dots ) \\     & = \frac{\sigma^2 b_1^j}{1-b_1^2} < \infty \text{ if } |b_1| < 1  \end{aligned}$$

### 不考慮截距項的AR(1)

> $$x_t = b_1 x_{t-1} + \epsilon_t$$

有截距項同時減去$$\mu$$得：

&#x20;$$y_t - \mu = b_0 - \mu + b_1 y_{t-1}+ \epsilon_t$$

右側同時加減$$b_1\mu$$可得$$y_t - \mu = b_0 - \mu +b_1\mu + b_1(y_{t-1} - \mu ) + \epsilon_t$$

整理後可得：

$$\displaystyle  \begin{aligned} y_t - \mu & = b_0 - (1-b_1)\mu + b_1 (y_{t-1} - \mu) + \epsilon_t \\     & = b_0 - (1-b_1) \frac{b_0}{1-b_1} + b_1 (y_{t-1} - \mu) + \epsilon_t \\     & = b_1(y_{t-1} - \mu) + \epsilon_t \end{aligned}$$

<mark style="color:red;">即沒有截距項的AR(1)序列為一個去掉均值的序列，即</mark>$$\mathrm{E}(x_t) = \mathrm{E}(y_t) - \mu = 0$$。

## AR(1)模型參數估計

> $$\displaystyle \hat{b_1} = \frac{\hat{\mathrm{Cov}}(y_t, y_{t-1})}{\hat{\mathrm{Var}}(y_t)} =  \frac{\sum_{t=2}^T(y_t - \overline{y})(y_{t-1}-\overline{y})}{\sum_{t=2}^T (y_t - \overline{y})^2}$$
