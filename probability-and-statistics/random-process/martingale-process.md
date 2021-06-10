# 平賭\(鞅\)過程\(Martingale process\)

## 平賭過程\(martingale process\)

> $$(\Omega, \mathcal{F}, \mathrm{P})$$為機率空間，$$\mathcal{F}_n$$為filitration。$$\{X(t), t \geq 0\}$$為隨機過程，當此隨機過程滿足以下條件時，稱為平賭過程。
>
> * $$X(t)$$ is $$\mathcal{F}_t$$-measurable, $$\mathrm{E}(|X_t|) < \infty$$ 且
> * $$X(t) = \mathrm{E}(X(t+1)|\mathcal{F}_t)$$

* 第一個條件指使用過去已發生的資訊$$\mathcal{F}_t$$ 即可量測目前的$$X(t)$$之測度值，且$$|X(t)|$$的期望值有限。
* 第二個條件指給定目前已知的資訊$$\mathcal{F}_t$$，對於未來的變數$$X(t+1)$$的期望值等於目前的隨機變數$$X(t)$$；即無法使用已發生的資訊預測未來尚未發生的事件。

