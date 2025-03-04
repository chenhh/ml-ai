# 線性模型

## 簡單線性回歸(simple linear regression)

預測值和單個預測變量之間存在線性關係。請注意，<mark style="color:red;">觀測值不在直線上，而是散佈在直線上</mark>。

線性回歸模型中，由資料$$\{x_t, y_t\}_{t=1}^T$$,  $$x_t \in \mathbb{R}^n,~y_t \in \mathbb{R}$$反推得到的模型參數$$(\beta_0, \beta_1)$$滿足觀測值到直線的距離的平方誤差最小，即$$\min \sum_t(\hat{y}_t-y_t)^2$$--(1)。

* $$y_t=\beta_0 +\beta_1x_t+\epsilon_t$$
* 也常寫成$$y_t=\alpha +\beta x_t+\epsilon_t$$
* 其中$$\beta_0 ~\text{or} ~ \alpha$$稱為截距(intercept)，$$\beta_1$$稱為斜率(slope)，$$\epsilon_t \sim WN(0, \sigma^2)$$為均值為0，且相同變異數的白噪音。
* <mark style="color:red;">註：線性指的是參數</mark>$$\beta$$<mark style="color:red;">與變數</mark>$$x_t$$<mark style="color:red;">之間的關係，因此模型也可為</mark>$$x_t^2$$<mark style="color:red;">或其它變形</mark>$$g(x_t)$$。

迴歸線擬合資料的程度越高，殘差越小 (平均而言)。當我們透過資料擬合迴歸線時，有些誤差為正數，有些為負數。也就是說，有些實際值會大於預測值 (出現在迴歸線上方)，而有些實際值則會小於預測值 (出現在迴歸線下方)。<mark style="color:red;">衡量整體誤差的方法是將誤差平方加法，並找到一條能將平方誤差和降到最低的迴歸線，即如(1)所示</mark>。

## 微積分解法



## 正交投影解法

\[[最小平方解](../linear-algebra/inner-product-space/least-square-solution.md)]



## 參考資料

* [\[數學傳播\]最小平方法與迴歸分析](https://web.math.sinica.edu.tw/mathmedia/HTMLarticle18.jsp?mID=41303)

