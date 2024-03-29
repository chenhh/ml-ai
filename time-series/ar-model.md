---
description: autoregressive model
---

# AR

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

$$\displaystyle \begin{aligned} y_t & = b_0 + b_1(b_0 + b_1 y_{t-2} + \epsilon_{t-1}) + \epsilon_t \\ & = b_0(1+b_1) + b_1^2 y_{t-2} + \epsilon_t + b_1 \epsilon_{t-1} \\ & = b_0(1+b_1 +b_1^2 + \dots) + (\epsilon_t + b_1 \epsilon_{t-1} + b_1^2 \epsilon_{t-2}+\dots) + \lim_{k \rightarrow \infty} b_1^k y_{t-k} \\ & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} + \lim_{k \rightarrow \infty} b_1^k y_{t-k} \end{aligned}$$

當$$|b_1| <1$$時，可得$$\displaystyle \lim_{k \rightarrow \infty} b_1^k y_{t-k} = 0$$

此時可得

$$\displaystyle \begin{aligned} y_t & = b_0 \sum_{j=0}^\infty b_1^j + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\ & = \frac{b_0}{ 1-b_1} + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \\ & = \mu + \sum_{j=0}^\infty b_1^j \epsilon_{t-j} \end{aligned}$$，其中$$\displaystyle \mu = \frac{b_0}{1-b_1}$$

<mark style="color:red;">可得AR(1)期望值為常數</mark>：

$$\displaystyle \begin{aligned} \mathrm{E}(y_t) & = \mathrm{E}(\mu) + \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j}) \\ & = \mathrm{E}(\mu) \\ & = \mu, ~ \forall t \end{aligned}$$

<mark style="color:red;">在</mark>$$|b_1|<1$$<mark style="color:red;">時，變異數收斂</mark>：

$$\displaystyle \begin{aligned} \gamma(0) &= \mathrm{Var}(y_t) \\ & = \mathrm{E}(y_t - \mu)^2 \\ & = \mathrm{E}(\sum_{j=0}^\infty b_1^j \epsilon_{t-j})^2 \\ & = \sum_{j=0}^\infty b_1^{2j} \mathrm{E}( \epsilon_{t-j})^2 \\ & = \sum_{j=0}^\infty b_1^{2j} \sigma^2 \\ & = \sigma^2 (1+ b_1^2 + b_1^4+\dots) \\ & = \frac{\sigma^2}{1-b_1^2} < \infty ~ \text{ if } |b_1| < 1 \end{aligned}$$

<mark style="color:red;">在</mark>$$|b_1|<1$$<mark style="color:red;">時，自我共變異數收斂</mark>：

$$\displaystyle \begin{aligned} \gamma(j) &= \mathrm{Cov}(y_t, y_{t-j}) \\ & = \mathrm{E}(y_t - \mu)(y_{t-j} - \mu) \\ & = \mathrm{E}[(\epsilon_{t}+b_1 \epsilon_{t-1}+b_1^2 \epsilon_{t-2}+\dots) (\epsilon_{t-j}+ b_1 \epsilon_{t-j-1}+ b_1^2 \epsilon_{t-j-2}+\dots)] \\ & = b_1^j \mathrm{E}(\epsilon_{t-j}\epsilon_{t-j}) + b_1^{j+1} b_1 \mathrm{E}(\epsilon_{t-j-1}\epsilon_{t-j-1}) + b_1^{j+2} b_1^2 \mathrm{E}(\epsilon_{t-j-2}\epsilon_{t-j-2}) + \dots \\ & = \sigma^2 b_1^j (1+b_1^2 +b_1^4 + \dots ) \\ & = \frac{\sigma^2 b_1^j}{1-b_1^2} < \infty \text{ if } |b_1| < 1 \end{aligned}$$

### 不考慮截距項的AR(1)

> $$x_t = b_1 x_{t-1} + \epsilon_t$$

有截距項同時減去$$\mu$$得：

$$y_t - \mu = b_0 - \mu + b_1 y_{t-1}+ \epsilon_t$$

右側同時加減$$b_1\mu$$可得$$y_t - \mu = b_0 - \mu +b_1\mu + b_1(y_{t-1} - \mu ) + \epsilon_t$$

整理後可得：

$$\displaystyle \begin{aligned} y_t - \mu & = b_0 - (1-b_1)\mu + b_1 (y_{t-1} - \mu) + \epsilon_t \\ & = b_0 - (1-b_1) \frac{b_0}{1-b_1} + b_1 (y_{t-1} - \mu) + \epsilon_t \\ & = b_1(y_{t-1} - \mu) + \epsilon_t \end{aligned}$$

<mark style="color:red;">即沒有截距項的AR(1)序列為一個去掉均值的序列，即</mark>$$\mathrm{E}(x_t) = \mathrm{E}(y_t) - \mu = 0$$。

## AR(1)模型參數估計

$$\displaystyle \hat{b_1} = \frac{\hat{\mathrm{Cov}}(y_t, y_{t-1})}{\hat{\mathrm{Var}}(y_t)} = \frac{\sum_{t=2}^T(y_t - \overline{y})(y_{t-1}-\overline{y})}{\sum_{t=2}^T (y_t - \overline{y})^2}$$

## AR(1)之衝擊反應函數(impulse response function, IRF)

IRF可了解動態體系內的內生變，因此外生變動(impulse)的反應(response)。

AR(1)中，衝擊反應函數指給定外生衝擊$$\epsilon_t$$的一次變動下，此模型序列對應的動態變化。

AR(1)可寫為：

$$y_t = \mu + (\epsilon_t + b_1 \epsilon_{t-1} + b_1^2 \epsilon_{t-2} + \dots ) + \lim_{k \rightarrow \infty} b_1^k y_{t-k}$$

所以：

$$y_{t+j} = \mu + (\epsilon_{t+j} + b_1 \epsilon_{t+j-1} + b_1^2 \epsilon_{t+j-2} + \dots ) + \lim_{k \rightarrow \infty} b_1^k y_{t-k}$$

假設在第$$t$$期時有一外生衝擊$$\epsilon_t=1$$，而對於$$\epsilon_{t+j}=0, \forall j \neq 0$$，則定義衝擊反應函數$$\Psi(j)$$如下：

$$\displaystyle \Psi(j)=\frac{\partial y_{t+j}}{\partial \epsilon_t} = b_1^j$$

因此AR(1)中，$$\Psi(0)=1, ~ \Psi(1)=b_1, ~ \Psi(2)=b_1^2, ~ \dots, \Psi(j)=b_1^j$$。

* 可得在$$|b_1|<1$$時，AR(1)序列的$$y_t$$的IRF會收斂至0。以經濟學解釋為模型受到外生衝擊之後，最後會回到穩定均衡狀態；反之若$$|b_1| >1$$，即AR(1)非定態，則$$y_t$$的IRF會發散到無窮大。
* 如果$$b_1$$為正值，則IRF會單調的收斂或發散；
* 如果$$b_1$$為負值，則IRF會以鋸齒狀收斂或發散；

## p階自我迴歸模型: AR(p)

> $$y_t = b_0 + b_1 y_{t-1}+ \dots + b_p y_{t-p} + \epsilon_t$$
>
> 以落後運算元表示為$$(1-b_1 L - b_2 L - \dots - b_p L)y_t = b_0 + \epsilon_t$$
>
> $$\epsilon_t ~ \text{WN}(0, \sigma^2)$$
>
> 定態的條件為$$b(z)=1-b_1z-b_2z^2 - \dots - b_pz^p = 0$$多項式根(可能為複數或負值)的範數大於1(落於單位圓之外)
>
> 如果多項式的有任一根的範數$$=1$$，則稱序列有單根(unit root)。
>
> 如果多項式為爆炸的序列(有任一根的範數$$<1$$)或是為單根，則為非定態序列。

* 例如AR(1)可得多項式為$$1 -b_1 z = 0$$, 其根為$$z=\frac{1}{b_1}$$，因此AR(1)為定態的條件為$$\displaystyle |\frac{1}{b_1}| > 1$$，即$$|b_1|<1$$。
* \[全為實根]例如AR(2)模型：$$y_t = 0.5 + 0.3y_{t-1} + 0.4y_{t-2} + \epsilon_t$$，多項式為$$1-0.3z-0.4z^2 =0$$, $$z=\frac{-3 \pm \sqrt{169}}{8}$$或$$\frac{5}{4}$$或$$-2$$，其範數均$$>1$$，因此為定態序列。
* \[共軛複根]例如AR(2)模型：$$y_t = 0.5 + 0.3y_{t-1}-0.4y_{t-2} + \epsilon_t$$, 多項式$$1-0.3z+0.4z^2=0$$, $$\displaystyle z=\frac{3}{8} \pm \frac{\sqrt{151}}{8}i$$, $$|z| = \sqrt{(\frac{3}{8})^2 + (\frac{\sqrt{151}}{8})^2}=\sqrt{2.5} > 1$$，因此為定態序列。

### AR(p)模型的定態條件

> 若AR(p)為定態序列， 則$$\sum_{i=1}^p b_i < 1$$。
>
> 若$$\sum_{i=1}^p |b_i| < 1$$，則AR(p)為定態序列。
>
> $$\sum_{i=1}^p b_i=1$$，則該序列至少存在一個單根(非定態)。

### AR(p)落後期數估計

AR(p)模型中，$$y_t = b_0 + b_1 y_{t-1} + \dots + b_p y_{t-p} + \epsilon_t$$是多元迴歸模型，解數變數為$$y_{t-1}, \dots, y_{t-p}$$， 因此參數$$b_1, \dots, b_p$$可用最小平方法估計，現在的問題是如何判定落後的期數$$p$$? 常用方法為AIC(Akaike information criterion)或 BIC(Bayesian information criterion)，則最佳的落後期 $$p^{*} = \argmin_{p=1,2,3,\dots} AIC(p) \text{ or } BIC(p)$$。

* $$\displaystyle AIC(p) = \log\left( \frac{\sum_{t=1}^T\hat{\epsilon}_t^2 }{T} \right) + (p+1) \frac{2}{T}$$
* $$\hat{\epsilon}_t=y_t - \hat{y}_t = y_t - (\hat{b}_0 + \hat{b}_1 y_{t-1} + \dots + \hat{b}_p y_{t-p} )$$為殘差(未解釋變異)。
* $$\displaystyle BIC(p) = \log\left( \frac{\sum_{t=1}^T\hat{\epsilon}_t^2 }{T} \right) + (p+1) \frac{\log T}{T}$$

BIC和AIC的差界僅在於懲罰項，只要$$T>8$$或$$\log T > 2$$，即BIC對於多增日一個變數落後期作為懲罰較AIC大，因此BIC傾向選擇一個落後期較少的模型。

理論上BIC所決定的落後期數$$p_{BIC}$$為真實落後期數$$p$$的一致估計式，但樣本較小時，AIC的表現較BIC佳。

### AR(p)模型的預測

為了簡化符號，假設AR(p)的均值為0，即$$y_t = b_1 y_{t-1} + b_2 y_{t-2} + \dots + b_p y_{t-p} + \epsilon_t$$。

$$
\displaystyle \begin{matrix} \underbrace{ \begin{bmatrix} y_t \\ y_{t-1} \\ \vdots \\ y_{t-p-1} \end{bmatrix} } \\ Y_t \in \mathbb{R}^{p \times 1} \end{matrix} = \begin{matrix} \underbrace{ \begin{bmatrix} b_1 & b_2 & \dots & b_{p-1} & b_p \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \vdots & \dots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{bmatrix} } \\ \Phi \in \mathbb{R}^{p \times p} \end{matrix} \begin{matrix} \underbrace{ \begin{bmatrix} y_{t-1} \\ y_{t-2} \\ \vdots \\ y_{t-p} \end{bmatrix} } \\ Y_{t-1} \in \mathbb{R}^{p \times 1} \end{matrix} + \begin{matrix} \underbrace{ \begin{bmatrix} \epsilon_t \\ 0 \\ \vdots \\ 0 \end{bmatrix} } \\ \epsilon_t \in \mathbb{R}^{p \times 1} \end{matrix}
$$

可寫成矩陣式(伴隨形式(companion form)、狀態空間表(state space representation))：$$Y_t = \Phi Y_{t-1} \epsilon_t$$。

若在時間$$t$$要預測未來$$j$$期資料時，可用$$\mathrm{E}(y_{t+j}) = \Phi^j Y_t$$，且可用對角化求$$\Phi^j=PD^{j}P^{-1}$$。

## Yule-Walker方程式

給定定態AR(p)模型：$$y_t = c + b_1 y_{t-1} + \dots + b_p y_{t-p} + \epsilon_t, ~ \epsilon_t \sim \text{WN}(0, \sigma^2)$$

兩側取期望值得：

$$
\displaystyle \begin{aligned} \mathrm{E}(y_t) &= c + b_1 \mathrm{E}(y_{t-1}) + \dots + b_p \mathrm{E}(y_{t-p}) \\ \mu & = c + b_1 \mu + \dots + b_p \mu \\ \mu & = \frac{c}{1-b_1 - b_2 - \dots - b_p} \\ \Rightarrow y_t - \mu &= b_1 (y_{t-1} - \mu) + \dots + b_p (y_{t-p} - \mu) + \epsilon_t \\ \Rightarrow B(L)(y_t - \mu) &= \epsilon_t \\ \Rightarrow y_t - \mu &= B(L)^{-1}\epsilon_t = \psi(L) \epsilon_t \end{aligned}
$$

因此可改寫AR(p)為 $$\displaystyle y_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$$

給定 $$(y_t - \mu) = b_1 (y_{t-1} - \mu) + \dots + b_p (y_{t-p} - \mu) + \epsilon$$

上式同乘$$(y_t -\mu)$$後取期望值得：

$$
\displaystyle \begin{aligned} \mathrm{E}((y_t - \mu)(y_t - \mu)) &= b_1 \mathrm{E}((y_{t-1} - \mu)(y_t - \mu)(y_t - \mu)) + \dots + b_p \mathrm{E}((y_{t-p} - \mu)(y_t - \mu)) + \mathrm{E}(\epsilon(y_t - \mu)) \\ \gamma(0) & = b_1 \gamma(1) + \dots +b_p \gamma(p) + \sigma^2 \end{aligned}
$$

如果同乘$$(y_{t-1} -\mu)$$後取期望值得：

$$
\displaystyle \gamma(1) = b_1 \gamma(0) + \dots +b_p \gamma(p-1)
$$

以此類推同乘$$(y_{t-p} -\mu)$$後取期望值得：

$$
\displaystyle \gamma(p) = b_1 \gamma(p-1) + \dots +b_p \gamma(0)
$$

將上述$$p$$個方程式除以$$\gamma(0)$$得：

$$
\displaystyle \begin{aligned} 1 &= b_1 \rho(1) + \dots + b_p \rho(p) + \frac{\sigma^2}{\gamma(0)} & -- (1)\\ \rho(1) &= b_1 + \dots + b_p \rho(p-1) &-- (2)\\ \vdots & \vdots & \\ \rho(p) &= b_1 \rho(p-1) + \dots + b_p &-- (3) \end{aligned}
$$

上式求解(2)到(3)間的$$p$$條方程式可得$$ho(1), \rho(2), \dots, \rho(p)$$之值，而(1,2,3)稱為Yule-Walker方程式。

由於$$\rho(j) = b_1 \rho(j-1) + b_2 \rho(j-2) + \dots + b_p \rho (j-p)$$，可根據$$ho(1), \dots, \rho(p)$$求得$$ho(p+1), \rho(p+2),\dots$$。

根據(1)，可得$$\displaystyle \rho(0) = \frac{\sigma^2}{1-b_1 \rho(1) - \dots - b_p \rho(p)}$$
