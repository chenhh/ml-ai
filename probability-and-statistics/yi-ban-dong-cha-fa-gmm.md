---
description: Generalized method of moments
---

# 一般動差法(GMM)

## 簡介

GMM）是統計學和計量經濟學中常用的一種半母數估計方法。

GMM的產生主要使用時機是最小平方法(OLS)的嚴格假設條件不成立時（例：解釋變數與誤差項有相關性），並且不知道資料的機率分佈，以致不能使用最大似然估計(MLE)模型參數時。GMM估計法具有一致性、漸近常態分佈，有效率等性質。

## 動差估計法(method of moments)

動差估計法是估計母體母數的方法。\[參考：[隨機變數的k次動差](moment-generating-function/#sui-ji-bian-shu-dekci-dong-cha-kth-moment)]

* 首先推導涉及感興趣的母數的母體動差（即所考慮的隨機變數的冪的期望值）的方程式。
* 然後取出一個樣本並從這個樣本估計母體動差。
* 接著使用樣本動差取代（未知的）母體動差，解出感興趣的母數。從而得到那些母數的估計。

假設隨機變數的分佈有$$k$$個參數$$\theta=(\theta_1, \dots, \theta_k)$$，分佈為$$f_X(x;\theta)$$，已經分佈函數$$k$$次動差的函數：

* $$\mu_1 \equiv \mathrm{E}(X)=g_1(\theta_1, \theta_2, \dots, \theta_k)$$
* $$\mu_2 \equiv \mathrm{E}(X^2)=g_2(\theta_1, \theta_2, \dots, \theta_k)$$
* ...
* $$a$$

若我們已經從樣本中獨立取出$$n$$​個樣本$$x_1, \dots, x_n$$，則樣本的$$k$$​個動差估計值為：$$\hat{\mu}_j =\frac{1}{n}\sum_{i=1}^n x_i^j, ~j=1,2,\dots, k$$。

將$$\hat{\mu}_j$$代入$$g_1,\dots, g_k$$，求解方程式可得$$\hat{\theta}_1,\dots, \hat{\theta}_k$$。

### 優點與缺點

動差法相當簡單，可以得到一致的估計值（在非常弱的假設下），盡管這些估計值往往是有偏差的。它是最大似然估計法的一個替代方法。

由於容易計算，動差法估計值可以作為似然方程解的第一個近似值，然後用牛頓-拉弗森法找到連續的改進近似值。通過這種方式，動差法可以協助尋找最大似然估計。

## 參考資料

* <mark style="background-color:red;">\[GMM原創論文] Hansen, Lars Peter (1982). "Large Sample Properties of Generalized Method of Moments Estimators". Econometrica. 50 (4): 1029–1054</mark>.
