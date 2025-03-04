---
description: moving average
---

# MA

## 移動平均模型:MA(q)

> MA(q)模型：
>
> $$y_t = \epsilon_t + c_1 \epsilon_{t-1} + \dots + c_q \epsilon_{t-q}, ~ \epsilon_t \sim \text{WN}(0, \sigma^2)$$

可用落後運算元改寫為$$y_t = (1 + c_1 L + c_2 L^2 +\dots + c_q L^q)\epsilon_t$$，令$$C(L)=(1+c_1L+\dots+c_qL^q)$$

無窮階MA模型可寫為$$MA(\infty)$$為$$\displaystyle y_t = \sum_{j=0}^\infty c_j \epsilon_{t-j}$$

同AR(p)模型，若$$\displaystyle \sum_{j=0}^\infty |c_j|< \infty$$(絕對可加)，則$$MA(\infty)$$為定態序列。

## MA(q)的可逆性(invertible)

> 如果$$C(z)=0$$的根均落於單位圓之外，則MA(q)序列可寫為$$\displaystyle \frac{1}{C(L)} y_t = \epsilon_t$$，且稱該序列具有可逆性。
