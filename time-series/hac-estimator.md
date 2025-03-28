---
description: heteroskedasticity and autocorrelation consistent estimator, 非均齊變異-序列相關一致估計量
---

# HAC估計量

## 簡介

在統計學和計量經濟學中，當我們使用線性迴歸模型$$y_t = X_t \beta + \epsilon_t$$時，經典的普通最小二乘法 (Ordinary Least Squares, OLS) 的有效性和我們對其係數估計的推斷的準確性，依賴於一些關鍵的假設。其中兩個重要的假設是：

1. **同方差性 (Homoskedasticity):** 誤差項$$\epsilon_t$$的變異數$$\mathrm{Var}(\epsilon_t)=\sigma^2$$對於所有觀察值都是恆定的。
2. **無自相關性 (No Autocorrelation):** 誤差項之間沒有相關性，$$\mathrm{Cov}(\epsilon_t, \epsilon_s)=0, ~ t \neq s$$。

然而，在實際應用中，這些假設經常被違反。當誤差項的變異數不是恆定的（異方差性），或者誤差項之間存在相關性（自相關性）時，使用標準的 OLS 方法得到的係數估計仍然是無偏且一致的，但是其標準誤差的估計會變得有偏。這會導致我們在進行假設檢驗和構建信賴區間時得到錯誤的結論。

<mark style="background-color:red;">HAC估計器它們提供了一種穩健的方法來估計 OLS 係數的共變異數矩陣</mark>$$\hat{\beta}$$<mark style="background-color:red;">，即使誤差項既存在異方差性又存在自相關性</mark>。

### **異方差性 (Heteroskedasticity)**

* **定義:** 指的是迴歸模型中誤差項的變異數隨著解釋變數的變化而變化。
* **後果:** OLS 估計的係數仍然是無偏且一致的，但其標準誤差的估計是有偏的，通常會低估真實的標準誤差。這會導致我們更容易拒絕實際上為真的零假設（即更容易犯第一類錯誤）。
* **例子:** 在研究收入與支出之間的關係時，我們可能會發現，收入較高的人群的支出變異性也較大。

### **自相關性 (Autocorrelation):**

* **定義:** 指的是迴歸模型中的誤差項與其自身過去的值存在相關性。這在時間序列數據中尤其常見。
* **後果:** 與異方差性類似，OLS 估計的係數仍然是無偏且一致的，但其標準誤差的估計是有偏的。此外，OLS 估計可能不再是最佳線性無偏估計量 (Best Linear Unbiased Estimator, BLUE)。
* **例子:** 在分析股票價格的時間序列數據時，今天的股價變動可能與昨天的股價變動相關。

### **自相關一致性估計量 (Autocorrelation Consistent Estimator, AC Estimator):**

當我們懷疑或檢測到迴歸模型中存在自相關性時，我們可以使用自相關一致性估計量來獲得對係數標準誤差的一致估計。這些估計量旨在校正由於自相關性而產生的偏差。

### **異方差和自相關一致性估計量 (Heteroskedasticity and Autocorrelation Consistent Estimator, HAC Estimator):**

HAC 估計量是一種更廣泛的估計量，它能夠同時處理**異方差性**和**自相關性**的問題，而無需對這些問題的形式做出具體的假設。它們提供了一種穩健的方法來估計 OLS 係數的共變異數矩陣$$\hat{\beta}$$，即使誤差項既存在異方差性又存在自相關性。

HAC 估計量通過調整 OLS 估計量的共變異數矩陣的計算方式來實現一致性。它們通常基於對誤差項的長期變異數進行估計，這個估計考慮了潛在的異方差性和自相關性。常見的方法包括使用核函數和一個帶寬參數來估計這種長期變異數。

OLS 估計量的共變異數矩陣通常為：$$\mathrm{Var(\hat{\beta})}=(X^\top X)^{-1} X^\top \Omega X (X^\top X)^{-1}$$，其中$$\Omega = \mathrm{E}(\epsilon \epsilon^\top)$$是殘差的共變異數矩陣。在同變異數且無自相關的條件下，$$\Omega = \sigma^2 I$$。

但當存在異方差或自相關時，$$\Omega$$不再是對角矩陣，且需要估計。HAC 估計器通過非引數方法估計\
$$\Omega$$，得到一個一致的共變異數矩陣：$$\mathrm{Var}_{HAC}(\hat{\beta}) = (X^\top X)^{-1} \hat{\Omega}(X^\top X)^{-1}$$。

#### **常見的 HAC 估計量：**

* **Newey-West 估計量:** 這是一種廣泛使用的 HAC 估計量，專門設計用於處理時間序列數據中的自相關性，同時也對異方差性具有穩健性。它使用一個截斷核函數來加權不同滯後階數的樣本自協方差。
* **White 的異方差一致性估計量:** 這可以看作是 HAC 估計量的一個特例，它只處理異方差性，假設不存在自相關性。

Newey-West估計器在統計學和計量經濟學中用於提供迴歸型模型中，當該模型不滿足迴歸分析的標准假設時，參數為共變異數矩陣的估計。該估計器用於嘗試克服模型中誤差項的自相關（也稱為序列相關）和非均齊異(變異數為時變)，通常用於應用於時間序列資料的迴歸。

<mark style="color:red;">用時間序列數據估計的迴歸模型往往表現出自相關；也就是說，誤差項隨時間變化而相關</mark>。

#### **何時使用 HAC 估計量：**

* 當我們有理由相信迴歸模型的誤差項存在異方差性和/或自相關性時。
* 尤其在分析時間序列數據和面板數據時，自相關性是一個常見的問題，因此 HAC 估計量非常有用。
* 當我們不想對異方差性和自相關性的具體形式做出強假設時，HAC 估計量提供了一種非參數的方法。

#### **關鍵特點**

* **異方差穩健**：HAC 不假設殘差方差恆定，適用於任意形式的異方差。
* **自相關穩健**：通過核加權，HAC 考慮了殘差的時間相關性，並隨著樣本量增加一致估計真實協方差。
* **非引數性質**：不需要指定異方差或自相關的具體形式（如 AR(1)），只需選擇合適的核和頻寬。

## auto-regressive (AR)模型的假設

> $$AR(p)$$模型: $$y_c = c + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$$
>
> $$\mathrm{E}(y_t^4) < \infty$$且 $$\epsilon_t \sim WN(0, \sigma^2)$$為均齊變異(homoskedasticity)且不具序列相關。



## 參考資料

* [\[wikipedia\] Newey–West estimator](https://en.wikipedia.org/wiki/Newey%E2%80%93West_estimator)
* \[原創論文] [Newey, Whitney K., and Kenneth D. West. "A Simple, Positive Semi-definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix." Econometrica 55.3 (1987): 703-708](https://www.nber.org/system/files/working_papers/t0055/t0055.pdf).
* Newey, Whitney K., and Kenneth D. West. "Automatic Lag Selection in Covariance Matrix Estimation." The Review of Economic Studies (1994): 631-653.
* Andrews, Donald WK. "Heteroskedasticity and autocorrelation consistent covariance matrix estimation." Econometrica: Journal of the Econometric Society (1991): 817-858.
* Smith, Richard J. "Automatic positive semidefinite HAC covariance matrix and GMM estimation." Econometric Theory 21.1 (2005): 158-170.
