---
description: autoregressive moving average model
---

# ARMA

## ARMA(p,q)模型

> 為了簡化符號，考慮$$y_t$$為均值為0的序列：
> $$\displaystyle y_t = b_1 y_{t-1} + \dots b_py_{t-p} + \epsilon_t + c_1 \epsilon_{t-1} + \dots c_q\epsilon_{t-q} ~ \epsilon_t, \sim \text{WN}(0, \sigma^2)$$

令落後多項式：
* $$ B(L) = 1-b_1L - b_2L^2 -\dots - b_p L^p $$
* $$ C(L) = 1+c_1L + c_2L^2 + \dots + c_q L^q $$

則ARMA(p,q)可寫成： $$ \displaystyle B(L)y_t = C(L)\epsilon_t $$

### 定態條件

> 給定$$ \displaystyle B(L)y_t = C(L)\epsilon_t $$，若$$B(z)=0$$的根均落於單位圓之外，則$$y_t$$為定態。

若$$y_t$$為定態，則ARMA(p,q)可改寫為MA($$\infty$$)如下：
$$ \displaystyle  
\begin{aligned}
y_t & = B(L)^{-1} C(L)\epsilon_t \\
    & = \left(\frac{1+c_1L + c_2L^2 + \dots + c_q L^q}{1-b_1L - b_2L^2 -\dots - b_p L^p} \right) \epsilon_t \\
    & = H(L) \epsilon_t \\
    & = \epsilon_t + h_1\epsilon_{t-1} + h_2\epsilon_{t-2} + \dots \\
    & = MA(\infty)
\end{aligned}
$$

其中$$h_0=1$$，且$$\sum_{j=0}^\infty |h_j| < \infty$$可得$$y_t$$為定態序列。
