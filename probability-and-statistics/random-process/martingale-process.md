# 平賭(鞅)過程(Martingale process)

在機率論中，Martingale 泛指一類特定的隨機過程。

## 平賭過程(martingale process)

> $$(\Omega, \mathcal{F}, \mathrm{P})$$為機率空間，$$\mathcal{F}_t$$為filitration(即$$\mathcal{F}_t \subseteq \mathcal{F}_{t+1}, ~\forall t$$均為sigma-field)。$$\{X(t), t \geq 0\}$$為隨機過程，當此隨機過程滿足以下條件時，稱為平賭過程。
>
> * \[可測條件]$$X(t)$$ is $$\mathcal{F}_t$$-measurable(或者說$$X(t)$$ adapted to $$F_t$$)，
> * \[可積分條件] $$\mathrm{E}(|X_t|) < \infty$$ 且
> * \[平賭性質]$$X(t) = \mathrm{E}(X(t+1)|\mathcal{F}_t)$$

* 可測條件指使用過去已發生的資訊$$\mathcal{F}_t$$ 即可量測目前的$$X(t)$$之測度值，且可積分條件限制$$|X(t)|$$的期望值有限。
* 平賭性質指給定目前已知的資訊$$\mathcal{F}_t$$，對於未來的變數$$X(t+1)$$的期望值等於目前的隨機變數$$X(t)$$；即無法使用已發生的資訊預測未來尚未發生的事件。

### 範例：丟公正銅板

考慮連續投擲一枚公平硬幣的遊戲：定義隨機變數$$Y_t$$為第$$t$$期丟銅板的結果。此遊戲中，每次投擲硬幣出現的結果之間彼此獨立。

$$Y(t) = \left\{ \begin{aligned} & +1 ~ \text{, head } \\ & -1 ~ \text{, tail } \end{aligned} \right.$$且$$\mathrm{P}(Y(t)=1) = \mathrm{P}(Y(t)=-1)=\frac{1}{2}$$。

定義隨機變數$$X(t)=Y(1)+\dots+Y(t)$$，且sigma-field $$F_t=\sigma(Y(1), \dots, Y(t)), ~ \forall t \geq 1$$。當$$X(0)=0$$時，其對應的$$\mathcal{F}_0=\{\empty, \Omega\}$$。

此時$$X(t)$$ 為平賭過程。

可積分條件：

$$\begin{aligned} \mathrm{E}(|X_t|) & = \mathrm{E}(|Y_1 + \dots + Y_t|) \\ 	&\leq \mathrm{E}(|Y_1|) + \dots + \mathrm{E}(|Y_t|) \\ 	& = t \left(\frac{1}{2} \times 1 + \frac{1}{2} \times |-1| \right) < \infty \end{aligned}$$

可測條件：由於$$\mathcal{F}_t=\sigma(Y_1,\dots, Y_t)~ \forall t \geq 1$$，因此$$X_t$$為$$F_t$$measurable。

平賭性質：$$\forall t \geq 1$$

$$\begin{aligned} \mathrm{E}(X_{t+1} | \mathcal{F}_t) & =  	\mathrm{E}(Y_1 + \dots + Y_{t+1} | \mathcal{F}_t) \\ 	& = (Y_1 + \dots + Y_t) + \mathrm{E}(Y_{t+1}|\mathcal{F}_t) \\ 	& = X_t + \mathrm{E}(Y_{t+1}) \\ 	& = X_t + (1/2 \times 1 + 1/2 \times (-1)) \\ 	& = X_t \end{aligned}$$

