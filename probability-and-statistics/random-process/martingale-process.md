# 平賭(鞅)過程(Martingale process)

在機率論中，Martingale 泛指一類特定的隨機過程。

鞅是一種隨機過程，描述了一個序列的條件期望保持不變。簡單說，它像一個「公平遊戲」，未來期望值等於當前值。

例子：賭徒的累計財富，若每次賭博期望收益為 0，則財富序列是鞅。

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

## 平賭收斂定理(martingale convergence theorem)

> * **核心內容**：在一定條件下，鞅序列 (Xn) (X\_n) (Xn​) 會隨著 n→∞ n \to \infty n→∞ 幾乎必然（almost surely）收斂到某個有限極限。
> * **直觀解釋**：鞅的隨機波動不會無限增長，而是最終穩定下來，趨向某個值。
> *   Martingale Convergence Theorem 是分析隨機過程收斂性的強大工具，特別適用於研究長期行為或漸近性質。
>
>     鞅收斂定理有多個版本，以下是常見的兩種：
>
>     1. **L1 L^1 L1 有界鞅（均值有界）**：
>        * **條件**：若 (Xn) (X\_n) (Xn​) 是鞅，且 E(∣Xn∣)≤C<∞ E(|X\_n|) \leq C < \infty E(∣Xn​∣)≤C<∞（均值有統一上界）。
>        * **結論**：存在隨機變數 X∞ X\_\infty X∞​，使得 Xn→X∞ X\_n \to X\_\infty Xn​→X∞​ 幾乎必然，且 E(∣X∞∣)<∞ E(|X\_\infty|) < \infty E(∣X∞​∣)<∞。
>        * **例子**：若 Xn X\_n Xn​ 是賭徒財富，總期望損益有界，則財富最終穩定。
>     2. **L2 L^2 L2 有界鞅（方差有界）**：
>        * **條件**：若 (Xn) (X\_n) (Xn​) 是鞅，且 E(Xn2)≤C<∞ E(X\_n^2) \leq C < \infty E(Xn2​)≤C<∞（二階矩有統一上界）。
>        * **結論**：Xn→X∞ X\_n \to X\_\infty Xn​→X∞​ 幾乎必然，且 X∞ X\_\infty X∞​ 在 L2 L^2 L2 中（方差有限）。

