---
description: simple (linear) regression analysis
---

# 簡單迴歸分析

## 古典迴歸假設

* 誤差項為均值0，變異數齊一(非時變)$$\sigma^2$$的常態分佈，即$$\epsilon_t \sim N(0, \sigma^2)$$。$$\mathrm{E}(\epsilon_t)=0$$，$$\mathrm{Var}(\epsilon_t)=\sigma^2$$。
* 誤差項無自我相關，$$\mathrm{Cov}(\epsilon_t, \epsilon_s)=0, ~ \forall t \neq s$$。
* 解釋變數$$X$$不是隨機變數(可控制或者可預測的變數)，假設其值在相異樣本中固定不變，則$$\mathrm{E}(\epsilon_t X_s) = X_s \mathrm{E}(\epsilon_t)=0, ~\forall t, s$$。
* 假設$$\frac{1}{T}\sum_{t=1}^T(X_t - \overline{X})^2 \neq 0, < \infty$$為非零的有限值，即要求$$X_t$$不可全為相同的數值。
* 假設$$\displaystyle \lim_{T \rightarrow \infty} \frac{1}{T}\sum_{t=1}^T(X_t - \overline{X})^2  < \infty$$。

## 線性迴歸模型

簡單線性迴歸方程式，指模式中僅包含一個應變數與一個自變數。 此處的<mark style="color:red;">「線性」指的是係數與自變數(可做變數變換)的關係為線性形式(可以用向量內積表示)</mark>，而自變數可為高階次方($$x^n)或函數($$$$\log(x)$$。

迴歸分析的<mark style="color:red;">目的</mark>是期望瞭解自變數的數值或改變量對於應變數產生(影響程度)的數值或改變量。

自關數與應變數的線性關係依Pearson相關係數可$$\rho$$分為：負相關($$-1 \leq \rho < 0$$)，不相關($$\rho =0$$), 正相關($$0 < \rho \leq 1$$)。

給定資料集$$\{ (Y_1, X_1), (Y_2, X_2), \dots, (Y_t, X_t) \dots (Y_T, X_T)\}$$，假設模型如下：

$$
Y_t = \beta_0 + \beta_1 X_t + \epsilon_t
$$

* $$Y_t$$：應變數(dependent variable)、被解釋變數、內生變數、反應變數、響應變數。為研究的目標變數，其取值可被觀測且隨自變數的變化而變化。
* $$X_t$$：自變數(independent variable），又稱獨立變數、解釋變數（explanatory variable）、外生變數。 可由研究者選擇、控制、研究，且能獨立變化而影響或引起其他變數變化的條件或因素。
* $$\epsilon_t$$：隨機干擾項(stochastic disturbance)、誤差項(error term)。
* $$\beta_0, \beta_1$$ 未知的迴歸係數。

注意:

* 自變數與應變數為相關關係(correlation)，不可推論為因果關係。
* 每組資料假設為獨立同分佈(i.i.d.)。
* <mark style="color:red;">需要估計的參數有</mark>$$\beta_0, \beta_1, \sigma^2$$。

誤差項需滿足三大假設:

1. 常態性(Normality) : 若母體資料呈現常態分配(Normal Distribution)，則誤差項也會呈現同樣的分配。可採用常態機率圖(normal probability plot) 或Shapiro-Wilk常態性檢定做檢查。
2. 獨立性(Independency) : 誤差項之間應該要相互獨立，否則在估計迴歸係數時會降低統計的檢定力。可以藉由Durbin-Watson test來檢查。
3. 變異數同質性(Constant Variance) : 變異數若不相等會導致自變數無法有效估計依變數。可以藉由殘差圖(Residual Plot)來檢查。

如果樣本資料是依時間先後排項，則稱為<mark style="color:red;">時間序列(time-series)資料</mark>，下標$$t$$代表時間。 如果樣本資料是某個特定時間點，針定特定地區或群體的資料，稱為<mark style="color:red;">橫斷面(cross-section)資料</mark>，下標$$t$$代表觀察對象。 如果資料包含上述兩種性質時，須使用兩個下標$$i, t$$代表觀察對象與時間。 其中變數$$(Y_t, X_t)$$為可收集到的資料，但$$\epsilon_t$$無法觀察到，只能用模型計算得出。

### 應變數為常態分佈隨機變數

給定獨立樣本資料集$$\{ (Y_1, X_1), (Y_2, X_2), \dots, (Y_t, X_t) \dots (Y_T, X_T)\}$$，迴歸模型$$Y_t = \beta_0 + \beta_1 X_t + \epsilon_t$$，且$$\epsilon_t ~ N(0, \sigma^2)$$為白噪音，$$X_t$$不是隨機變數。

由常態分佈的性質得$$Y_t$$為$$\epsilon_t$$的函數且為常態分佈$$Y_t \sim N(\beta_0+\beta_1X_t, \sigma^2)$$：

* $$\mathrm{E}(Y_t)=\mathrm{E}(\beta_0+\beta_1 X_t + \epsilon_t)=\beta_0 + \beta_1 X_t$$。
* $$\mathrm{Var}(Y_t)=\mathrm{E}(Y_t - \mathrm{E}(Y_t))^2=\mathrm{E}(\epsilon_t^2)=\sigma^2$$。
* $$\mathrm{Cov}(Y_s, Y_t)=\mathrm{E}[(Y_t - \mathrm{E}(Y_t))(Y_s - \mathrm{E}(Y_s))]=\mathrm{E}(\epsilon_t \epsilon_s)=0$$。
* $$Y_t$$為平均數受$$X_t$$的影響，且相異$$Y_t$$為獨立的隨機變數。

### 估計式與殘差

令$$\beta_i$$的估計值為$$\hat{\beta_i}, ~i=0,1$$，則$$\hat{Y}_t=\hat{\beta}_0+\hat{\beta}_1X_t$$代表樣本迴歸直線，$$\hat{Y}_t$$為實際值$$Y_t$$的預測值或配適值(fitted value)。

殘差(residual)為$$e_t = Y_t - \hat{Y}_t$$，可得$$Y_t = \hat{\beta}_0 + \hat{\beta}_1X_t + e_t=\hat{Y}_t+e_t$$。

## 參數估計方法

* 最小平方估計法(least squares estimation)，也稱最小平方法(ordinary least square, OLS)：最小化觀測值$$Y_t$$與平均值$$\mathrm{E}(Y_t)$$或條件平均值$$\mathrm{E}(Y_t|X_t)$$的離差平方和。
* 最佳線性不偏估計法(best linear unbiased estimation，BLUE)。
* 最大概似估計法(maximum likelihood estimation, MLE)。

### OLS

$$\displaystyle  \begin{aligned} \min_{\beta_0, ~\beta_1} S &= \sum_{t=1}^T (Y_t - \mathrm{E}(Y_t))^2 \\     & = \sum_{t=1}^T (Y_t - \beta_0 - \beta_1X_t)^2  \end{aligned}$$

上式為無限制式的凸函數，因此極值出現在一階微分為0之處：

$$\displaystyle  \begin{aligned} \frac{\partial S}{\partial \beta_0} &= -2 \sum_{t=1}^T (Y_t - \beta_0 - \beta_1 X_t) = 0  \\ \frac{\partial S}{\partial \beta_1} &= -2 \sum_{t=1}^T X_t(Y_t - \beta_0 - \beta_1 X_t) = 0   \end{aligned}$$

整理可得最小平方標準式(least square normal equations)：

$$\displaystyle  \begin{aligned} \sum_{t=1}^T Y_t &= \hat{\beta}_0 T +\hat{\beta}_1 \sum_{t=1}^T X_t \\ \sum_{t=1}^T X_t Y_t &= \hat{\beta}_0 \sum_{t=1}^T X_t +\hat{\beta}_1 \sum_{t=1}^T X_t^2 \\  \end{aligned}$$

其中$$\hat{\beta}_0, \hat{\beta}_1$$差示由樣本得到估計值，非模型真值。

令殘差$$e_t = Y_t - \hat{Y}_t$$，上式可改寫成：

$$\displaystyle  \begin{aligned} \sum_{t=1}^T e_t &= 0 \\ \sum_{t=1}^T X_te_t &= 0 \\  \end{aligned}$$

解聯立方程式可得：

$$\displaystyle  \begin{aligned} \hat{\beta}_1 = \frac{T\sum_{t=1}^T X_t Y_t - \sum_{t=1}^T X_t \sum_{t=1}^T Y_t  }{T \sum_{t=1}^T X_t^2 - (\sum_{t=1}^T X_t)^2} =  \frac{\sum_{t=1}^T (X_t - \overline{X})(Y_t - \overline{Y})}{\sum_{t=1}^T (X_t - \overline{X})^2}  \end{aligned}$$。

$$\displaystyle  \begin{aligned} \hat{\beta}_0 = \overline{Y} - \hat{\beta}_1 \overline{X}  \end{aligned}$$。

<mark style="color:red;">因此樣本迴歸直接必會通過(</mark>$$\overline{X}, \overline{Y}$$<mark style="color:red;">)這一點</mark>。

註：上式也可用線性代數的[正交投影矩陣](../linear-algebra/inner-product-space/least-square-solution.md)的到相同的結果。



### Libreoffice迴歸分析

{% embed url="https://help.libreoffice.org/6.4/zh-CN/text/scalc/01/statistics_regression.html?DbPAR=CALC" %}

設定回歸類型。有三種類型可用:

「線性回歸」: 找到一條形如「y = a·x + b」的直線, 其中「a」是斜率, b是與資料最匹配的截距。

「對數回歸」: 找到與資料最匹配的形如「y = a·ln(x) + b」的對數曲線, 其中「a」為斜率, b 為截距, ln(x) 為「x」的自然對數。

「冪回歸」: 找到形如「y = a·x^b」的冪曲線, 其中「a」是係數, b 是與資料最匹配的冪。
