# 線性模型

## 簡單線性回歸(simple linear regression)

預測值和單個預測變量之間存在線性關係。請注意，觀測值不在直線上，而是散佈在直線上。

線性回歸模型中，由資料反推得到的模型參數$$(\beta_0, \beta_1)$$滿足觀測值到直線的距離的平方誤差最小，即$$\min \sum_t(\hat{y}_t-y_t)^2$$。

* $$y_t=\beta_0 +\beta_1x_t+\epsilon_t$$
* 也常寫成$$y_t=\alpha +\beta x_t+\epsilon_t$$
* 其中$$\beta_$$$$\beta_0 ~\text{or} ~ \alpha$$稱為截距(intercept)，$$\beta_1$$稱為斜率(slope)，$$\epsilon_t \sim WN(0, \sigma^2)$$為均值為0，且相同變異數的白噪音。
