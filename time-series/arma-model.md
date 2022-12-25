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

## Wold representation定理

> 任何均值為0的定態時間序列 $$ \{y_t\} $$都能表示為：
> 
> $$ \displaystyle y_t = \sum_{j=0}^\infty c_j \epsilon_t = C(L)\epsilon_t $$

其中：
1. $$ \epsilon_t = y_y - \mathrm{Proj}(y_t~|~H_{t-1}) $$稱為干擾項(innovation)，是將序列$$y_t$$投影到H_t=S_p[y_t, y_{t-1}, \dots]的投影殘差。
2. $$ C(L) = 1+c_1L + c_2L^2 + \dots $$為落後多項式
3. $$ \displaystyle \sum_{j=0}^\infty c_j^2< \infty, ~ c_0=1 $$，即$$y_t$$為定態。
4. $$ \epsilon_t \sim \text{WN} (0,\sigma^2) $$
5. $$ C(z)=0 $$的根均落於單位圓之外，即 $$ y_t $$可逆。
6. Wold representation表示法有唯一性，即兩相異的定態時間序列不會有相同的$$\{c_j\}與$$\{\epsilon_t\}$$。

Wold representation說明了任意定態時間序列能以無窮多干擾項的線性線合表示之，但在實務上不可行，必須以 $$ \displaystyle \frac{B(L)}{C(L)} $$逼近之，即以ARMA(p,q)近似Wold representation。

## 預測評估

預測誤差：$$ \displaystyle e_{t+k, t} = y_{t+k} - \mathrm{E}_t(y_{t+k}) $$。

預測損失函數期望值：$$ \displaystyle \mathrm{E}(L(e_{t+k, t})) $$，其中：
1. 二次函數：$$ \displaystyle L(e_{t+k, t}) = e_{t+k, t}^2 $$, 損失稱為均方差(mean square error, MSE)
2. 絕對函數: $$ \displaystyle L(e_{t+k, t}) = |e_{t+k, t}|  $$
3. 效用函數: $$ \displaystyle L(e_{t+k, t}) = u(e_{t+k, t})  $$
