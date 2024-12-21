---
description: 自協方差(autocovariance)/自相關(autocorrelation)函數
---

# 自共變異數/自相關函數

## 簡介

ACF 是一個完整的自相關函數，可為我們提供具有滯後值的任何序列的自相關值。簡單來說，它描述了該序列的當前值與其過去的值之間的相關程度。

直觀上來說，ACF 描述了一個觀測值和另一個觀測值之間的自相關，包括直接和間接的相關性資訊。

## 弱定態時間序列

給定弱定態過程$$\{X_t, ~t\in T\}$$，由定義得$$\mathrm{E}(X_t)=\mu<\infty$$，$$\mathrm{Var}(X_t)=\mathrm{E}(X_t - \mu)^2 = \sigma^2 < \infty$$均為常數，且共變異數$$\mathrm{Cov}(X_t, X_s)$$為時間跨度$$|t-s|$$的函數。

* $$\gamma_h = \mathrm{Cov}(X_t, X_s)=\mathrm{E}(X_t - \mu)(X_s - \mu)$$
* $$\rho_h = \frac{\mathrm{Cov}(X_t, X_{t+h})}{\sqrt{\mathrm{Var}(X_t)}\sqrt{\mathrm{Var}(X_{t+h})}}=\frac{\gamma_h}{\gamma_0}$$
* 令$$\gamma_0 = \mathrm{Var}(X_t)=\mathrm{Var}X_{t+h})$$

性質：

* $$\gamma_0=\mathrm{Var}(X_t)$$；$$\rho_0=1$$。
* $$|\gamma_h| \leq \gamma_0$$；$$|\rho_h| \leq 1$$。
  * 因為相關係數$$|\rho_h| = |\frac{\gamma_h}{\gamma_0}| \leq 1$$且$$\gamma_0 \geq 0$$，因此$$|\gamma_h| \leq \gamma_0$$。
* $$\gamma_h=\gamma_{-h}$$；$$\rho_h = \rho_{-h}, ~\forall h$$ 為偶函數(對稱於$$h=0$$)。
* 因為自相關係數為偶函數 ，因此一般只考慮$$h \geq 0$$之值，其圖表稱為相關圖(correlogram)。
* \[重要性質] $$\gamma_h, ~\rho_h$$有<mark style="color:red;">正半定(positive semidefinite)的性質</mark>，即$$\displaystyle \sum_{i=1}^n \sum_{j=1}^n a_i a_j \gamma_{|i -j|} \geq 0$$且$$\displaystyle \sum_{i=1}^n \sum_{j=1}^n a_i a_j \rho_{|i -j|} \geq 0$$。對於任意的時間點$$i, j \in T, \forall a_i \in \mathbb{R}, i=1,2,\dots, n$$。
* 如果將上式以矩陣形式表示，可得$$\Sigma = \begin{bmatrix}  \rho_{0} & \rho_{-1} & \dots & \rho_{1-n} \\ \rho_{1} & \rho_{0} & \dots & \rho_{2-n} \\ \vdots & \vdots & \vdots & \vdots \\ \rho_{n-1} & \rho_{n-2} & \vdots & \rho_{0}  \end{bmatrix}$$因為$$\rho_{i-j}=\rho_{j-i}$$且$$\rho_0 \geq 1$$，得$$\Sigma=\Sigma^{\top}$$為對角線為1的對稱矩陣。
* <mark style="color:blue;">可得滿足自共變異數/自相關係數的函數=>函數滿足正半定(positive semidefinite)的性質</mark><mark style="color:red;">。</mark>

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption><p>隨機變數的自相關係數圖(相關圖)</p></figcaption></figure>

