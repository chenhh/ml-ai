# 時間序列性質

## 基本概念

給定時間序列$$\{y_t\}_{t=1}^T$$，$$y_t$$為第$$t$$期的資料(純量或向量)。

$$y_{t-k}$$稱為$$y_t$$<mark style="color:red;">落後</mark>$$k$$<mark style="color:red;">期(kth lag)</mark>的資料。

$$\Delta y_t \equiv y_t - y_{t-1}$$稱為$$y_t$$的<mark style="color:red;">一階差分</mark>。

註：$$\begin{aligned} \Delta \ln y_t &= \ln y_t - \ln y_{t-1} \\ & \approx  \left[ \ln y_{t-1} + \frac{1}{y_{t-1}}(y_t - y_{t-1})  \right] - \ln y_{t-1} \\ & =  \frac{y_t - y_{t-1}}{y_{t-1}}   \end{aligned}$$

當$$y_t$$變動不大時，$$\Delta \ln y_t$$是變動量的良好近似值，經常用於報酬率的計算。

在時間序列分析中，使用滯後運運算元（lag operator）有幾個重要的原因：

1. 簡化模型表示。用$$L$$可以簡潔地表示過去值，而不必每次都寫出$$X_{t-1}, X_{t-2},\dots$$。
2. 捕捉時間依賴性。
3. 分析時間序列的動態特性。
4. 模型識別和診斷。

##



## 動差(moment)

隨機樣本的均數與變異數，<mark style="color:blue;">一般條件下會隨時間變化(時變）</mark>，即：

* $$\mathrm{E}(y_t) \equiv \mu_t \equiv \overline{y}_t$$
  * 樣本均數： $$\frac{1}{T} \sum_{t=1}^T y_t$$
* $$\mathrm{Var}(y_t)\equiv \sigma_t^2$$
  * 樣本變異數(不偏)： $$\frac{1}{T-1}\sum_{t=1}^T (y_t - \overline{y}_t)^2$$

因為時間序列中的資料，過去與未來的資料不一定為獨立同分佈，具有相關性，可用自我共變異函數(autocovariance function)與自我相關函數(autocorrelation function, ACF)來計算序列的相關。

### k階自我共變異函數

> 給定時間序列$$\{y_t\}_{t=-\infty}^{\infty}$$且具有有限的變異數$$\mathrm{Var}(y_t) < \infty$$, 則其$$k$$階自我共變異函數定義為：
>
> $$\gamma(t,k)=\mathrm{Cov}(y_t, y_{t-k})=\mathrm{E}(y_t-\mu_t)(y_{t-k} - \mu_{t-k})$$
>
> 由定義可得　$$\gamma(t,0)=\mathrm{Cov}(y_t,y_t)=\mathrm{Var}(y_t)\equiv \sigma_t^2$$
>
> 樣本共變異數 \[[stackexchange: Question about sample autocovariance function](https://stats.stackexchange.com/questions/56238/question-about-sample-autocovariance-function)]：
>
> * $$\frac{1}{T-k} \sum_{t=1}^{T-k} (y_t-\overline{y}_{t})(y_{t-k}-\overline{y}_{t})$$
> * $$\frac{1}{T} \sum_{t=1}^{T-k} (y_t-\overline{y}_{t})(y_{t-k}-\overline{y}_{t})$$

### k階自我相關係數

> $$\rho(t,k)=\frac{\mathrm{Cov}(y_t, y_{t-k})}{\sigma_t \sigma_{t-k}}$$.
>
> 自我相關係數越高，則稱此序列的持續性越大(persistent)

