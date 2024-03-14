---
description: 自協方差(autocovariance)/自相關(autocorrelation)函數
---

# 自共變異數/自相關函數

## 弱定態時間序列

給定弱定態過程$$\{X_t, ~t\in T\}$$，由定義得$$\mathrm{E}(X_t)=\mu<\infty$$，$$\mathrm{Var}(X_t)=\mathrm{E}(X_t - \mu)^2 = \sigma^2 < \infty$$均為常數，且共變異數$$\mathrm{Cov}(X_t, X_s)$$為時間跨度$$|t-s|$$的函數。

* $$\gamma_h = \mathrm{Cov}(X_t, X_s)=\mathrm{E}(X_t - \mu)(X_s - \mu)$$
* $$\rho_h = \frac{\mathrm{Cov}(X_t, X_{t+h})}{\sqrt{\mathrm{Var}(X_t)}\sqrt{\mathrm{Var}(X_{t+h})}}=\frac{\gamma_h}{\gamma_0}$$
* $$\gamma_0 = \mathrm{Var}(X_t)=\mathrm{Var}X_{t+h})$$
