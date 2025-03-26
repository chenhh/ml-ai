# 平賭(鞅)過程(Martingale process)

鞅是一種隨機過程，描述了一個序列的條件期望保持不變。簡單說，它像一個「公平遊戲」，未來期望值等於當前值。例如：賭徒的累計財富，若每次賭博期望收益為 0，則財富序列是鞅。

如果數列長期看起來一直在往上走（像子鞅）或往下掉（像超鞅），那可能就不是鞅。鞅應該是「晃來晃去」但平均不偏。

## 平賭過程(martingale process)

> $$(\Omega, \mathcal{F}, \mathrm{P})$$為機率空間，$$\mathcal{F}_t$$為filitration(即$$\mathcal{F}_t \subseteq \mathcal{F}_{t+1}, ~\forall t$$均為σ域)。$$\{X_t, t \geq 0\}$$為隨機過程($$t$$可為離散或連續)，當此隨機過程滿足以下條件時，稱為平賭過程。
>
> * \[可測條件]$$X_t$$ 為$$\mathcal{F}_t$$-可測(measurable)(或者說$$X_t$$ 適應於(adapted to) $$F_t$$)，即$$X_t$$的值僅依賴於截至第$$t$$步之前的所有資訊（歷史資訊）$$\mathcal{F}_t$$，而不能依賴未來的資訊。
> * \[可積分條件] $$\mathrm{E}(|X_t|) < \infty$$ ，鞅的期望值有限，確保鞅過程的數學操作（如求和或積分）是良定義的。(註：但$$X_t$$的取值可為$$\pm \infty$$，只要期望值有限即可，如常態分佈)。
> * \[平賭性質]$$\mathrm{E}(X_{t+1}|\mathcal{F}_t)=X_t$$或$$\mathrm{E}(X_t|\mathcal{F}_s)=X_s, \text{ a.s. }~ \forall s < t$$。鞅過程沒有系統性的增長或下降趨勢，波動純粹是隨機的。
>
> 註：有關會將鞅寫成$$\mathrm{E}(X_{t}|X_1, \dots, X_{s})=X_s$$，即隱含由$$X_1, \dots, X_s$$生成的σ域等於前$$s$$的所有資訊$$\mathcal{F}_s$$，即$$\sigma(X_1, \dots, X_s)=\mathcal{F}_s$$。

* 可測條件指使用過去已發生的資訊$$\mathcal{F}_t$$ 即可量測目前的$$X_t$$之測度值，且可積分條件限制$$|X_t|$$的期望值有限。
* 平賭性質指給定目前已知的資訊$$\mathcal{F}_t$$，對於未來的變數$$X_{t+1}$$的期望值等於目前的隨機變數$$X_t$$；也就是說，未來不會因為過去的結果而變得更好或更糟，期望值始終保持當前狀態。在給定目前資訊的情況下，下一步的期望值等於目前的值，無可預測的長期趨勢。
* 鞅收斂定理（Martingale Convergence Theorem）是鞅理論的核心結果之一，它指出在某些條件下，鞅過程會幾乎必然收斂到一個極限值。這一定理在分析隨機過程的長期行為時非常重要。

## 次鞅(sub-martingale)與超鞅(super-martingale)

> 如果$$\mathrm{E}(X_t|\mathcal{F}_s)\geq X_s$$稱為次鞅(sub-martingale)，表示期望值傾向增加(向上漂移)。
>
> 例如：
>
> * 在一個期望收益為正的賭博中，賭徒的財富。或者股票價格在牛市中的行為或累積的正收益。
> * 表示一個投資組合的價值，且市場整體趨勢是上升的。即使存在隨機波動，投資的期望收益可能隨時間增長，這種過程不是鞅，而是次鞅。
> * 生長中的人口數量（在一定條件下）。
>
> 如果$$\mathrm{E}(X_t|\mathcal{F}_s)\leq X_s$$稱為超鞅(super-martingale)，表示期望值傾向減少(向下漂移)。
>
> 例如：
>
> * 在一個期望收益為負的賭博中，賭徒的財富。
> * 由於折舊或損耗而價值下降的資產。
> * 疾病的傳播程度（在控制措施下）。
>
> <mark style="background-color:red;">次鞅和超鞅的定義幫助我們將隨機過程分類為「上升」、「下降」或「公平」，從而理解其內在結構</mark>。

應用：

**停時理論 (Stopping Time Theory)：**&#x8A31;多關於鞅的重要結果，例如可選停止定理（Optional Stopping Theorem），在適當的條件下可以推廣到次鞅和上鞅。這使得我們能夠分析在隨機時間停止的隨機過程的行為。

**不等式 (Inequalities)：**&#x4F8B;如 Doob 極大不等式（Doob's Maximal Inequality）和次鞅不等式（Submartingale Inequality），都是針對次鞅提出的。這些不等式提供了過程最大值的界限，是證明收斂性結果和研究隨機過程樣本路徑行為的重要工具。

**分解定理 (Decomposition Theorems)：**&#x44;oob 分解定理適用於次鞅和上鞅，允許我們將它們唯一地分解為一個鞅和一個可預測的遞增（對於次鞅）或遞減（對於上鞅）過程之和。這個分解有助於理解這些過程的底層結構。

**金融學 (Finance):** 用於模擬資產價格行為、投資組合價值和期權定價。例如，股票價格通常被建模為次鞅（假設沒有負的期望回報）。

* **次鞅**：在無套利市場中，折現後的資產價格通常是鞅。但在現實市場中，未折現的價格可能是一個次鞅，因為它包含了正的期望回報（如風險溢價）。
* **超鞅**：某些耗損過程（如保險公司的儲備金）可能是一個超鞅，因為隨著時間推移，儲備金期望減少。

### 範例：丟公正銅板

考慮連續投擲一枚公平硬幣的遊戲：定義隨機變數$$Y_t$$為第$$t$$期丟銅板的結果。此遊戲中，每次投擲硬幣出現的結果之間彼此獨立。

$$Y(t) = \left\{ \begin{aligned} & +1 ~ \text{, head } \\ & -1 ~ \text{, tail } \end{aligned} \right.$$且$$\mathrm{P}(Y(t)=1) = \mathrm{P}(Y(t)=-1)=\frac{1}{2}$$。

定義隨機變數$$X(t)=Y(1)+\dots+Y(t)$$，且sigma-field $$F_t=\sigma(Y(1), \dots, Y(t)), ~ \forall t \geq 1$$。當$$X(0)=0$$時，其對應的$$\mathcal{F}_0=\{\empty, \Omega\}$$。

此時$$X(t)$$ 為平賭過程。

可積分條件：

$$\begin{aligned} \mathrm{E}(|X_t|) & = \mathrm{E}(|Y_1 + \dots + Y_t|) \\ 	&\leq \mathrm{E}(|Y_1|) + \dots + \mathrm{E}(|Y_t|) \\ 	& = t \left(\frac{1}{2} \times 1 + \frac{1}{2} \times |-1| \right) < \infty \end{aligned}$$

可測條件：由於$$\mathcal{F}_t=\sigma(Y_1,\dots, Y_t)~ \forall t \geq 1$$，因此$$X_t$$為$$F_t$$可測。

平賭性質：$$\forall t \geq 1$$

$$\begin{aligned} \mathrm{E}(X_{t+1} | \mathcal{F}_t) & =  	\mathrm{E}(Y_1 + \dots + Y_{t+1} | \mathcal{F}_t) \\ 	& = (Y_1 + \dots + Y_t) + \mathrm{E}(Y_{t+1}|\mathcal{F}_t) \\ 	& = X_t + \mathrm{E}(Y_{t+1}) \\ 	& = X_t + (1/2 \times 1 + 1/2 \times (-1)) \\ 	& = X_t \end{aligned}$$

### 鞅差的期望為零

> $$\{X_t\}$$為平賭過程，每一步的變化（差值）平均是零，這是鞅「不偏不倚」的證明。
>
> $$\forall s < t, \mathrm{E}(X_t - X_s | \mathcal{F}_s)= \mathrm{E}(X_t  | \mathcal{F}_s) - \mathrm{E}(X_s | \mathcal{F}_s) = X_s - X_s =0$$。
>
> 或 $$\mathrm{E}(X_{t+1} - X_t ~|~ \mathcal{F}_t)=0$$。

註：$$\mathrm{E}(X_s|\mathcal{F}_s) =X_s$$是更基本的性質，講的是「現在對現在」，任何適應$$\mathcal{F}_s$$的$$X_s$$\
都成立，不限於鞅。因為$$X_s$$是$$\mathcal{𝐹}_s$$的一部分(更精確的說，$$X_s$$的前像均為$$\mathcal{F}_s$$中的元素)，給定$$\mathcal{F}_s$$的資訊，$$X_s$$已經是確定的，沒什麼好「平均」的，直接就是它自己。

### 鞅的波動（變異數）可能會隨時間變大

> $$\{X_t\}$$為鞅過程，$$X_0=0$$且每步獨立變化，則$$\mathrm{Var}(X_n)=\sum_{i=1}^n \mathrm{Var}(X_i - X_{i-1})$$會累積變大。
>
> $$\mathrm{Var}(X_{t+1} ~|~ \mathcal{F}_t)= \mathrm{E}((X_{t+1}-X_t)^2 ~|~ \mathcal{F}_t)$$，鞅過程的波動性由其增量的變異數決定。

### 鞅的變換性質（Martingale Transforms）

> $$\{X_t\}$$為鞅過程，$$\{H_t\}$$是可預測過程(即$$H_t$$是$$\mathcal{F}_{t-1}$$可測)，則：
>
> $$(H\cdot X)_t = \sum_{i=1}^t H_i(X_i - X_{i-1})$$仍為鞅。

### 停止時間性質（可選停定理, Optional Stopping Theorem）

> 如果你在某個隨機時刻停下來（比如賭到破產或贏夠就走），平均來看，你的結果還是等於開始時的值。
>
> 假設$$\{X_t\}$$為平賭過程，$$T$$ 是一個有界停止時間（不會無限拖下去），則$$\mathrm{E}(X_T)=\mathrm{E}(X_0)$$。
>
> 這表示無論你選擇何時停止觀察，期望值仍然保持不變。

## Doob 分解

> 任何適應於過濾$$\{ \mathcal{F}_t\}$$ 的(離散時間)隨機過程$$\{X_t\}$$，且$$(\mathrm{E}(|X_n|) < \infty$$都可以唯一分解為一個鞅部分$$\{M_t\}$$和一個可預測過程 $$\{A_t\}$$：
>
> $$X_t = M_t + A_t$$
>
> * 鞅過程：$$\mathrm{E}(M_{t+1}| \mathcal{F}_t)=M_t$$。 表示隨機過程中的「公平性」或「無偏性」成分。
> * 可預測過程$$A_0=0$$且$$A_{t+1}$$是$$\mathcal{F}_t$$可測的(<mark style="color:blue;">不可寫成</mark>$$\mathcal{F}_{s}, \forall s< t+1$$<mark style="color:blue;">，因為這樣會得出</mark>$$\mathcal{F}_0$$<mark style="color:blue;">可測，即在必須在所有過去的時間</mark>$$s<t+1$$ <mark style="color:blue;">的信息下都是可確定的</mark>)。表示隨機過程中可以被提前預測的部分。它反映了隨機過程的「趨勢」或「漂移」，例如過程是否有系統性的增長或下降。
>
> <mark style="background-color:red;">因此，Doob 分解將隨機過程分為兩部分：一部分是無法預測的隨機波動，另一部分是可以提前預測的確定性趨勢</mark>。
>
> Doob分解的成立並不直接依賴於隨機過程$$\{X_t\}$$的具體分佈，而是取決於$$X_t$$可積、適應濾流以及離散時間三個條件下成立。
>
> 註：連續時間的隨機過程條件需要額外的正則條件才成立。

定義增量$$\Delta X_t = X_t - X_{t-1}$$，則可將$$X_t$$改為$$X_t = X_0 + \sum_{i=1}^t \Delta X_i$$。

增量可改寫為$$\Delta X_t = (\Delta X_t - \mathrm{E}(\Delta X_t| \mathcal{F_{t-1}})) + \mathrm{E}(\Delta X_t| \mathcal{F_{t-1}})$$

* $$\Delta X_t - \mathrm{E}(\Delta X_t| \mathcal{F_{t-1}})$$是鞅差序列，表示隨機波動。
* $$\mathrm{E}(\Delta X_t| \mathcal{F_{t-1}})$$是可預測的，表示確定性趨勢。

因此$$\displaystyle \begin{aligned} X_t & = X_0 + \sum_{i=1}^t \Delta X_i \\  & = \begin{matrix}  \underbrace{ \sum_{i=1}^t (\Delta X_i - \mathrm{E}(\Delta X_i| \mathcal{F_{i-1}})) } \\ M_t  \end{matrix}    + \begin{matrix}  \underbrace{  \sum_{i=1}^t \mathrm{E}(\Delta X_i| \mathcal{F_{i-1}})   } \\ A_t  \end{matrix}   \end{aligned}$$

### 可預測過程（predictable process）

隨機過程$$\{A_t\}$$為濾流$$\mathcal{F}_{t-1}$$可測(依定義$$\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq  \dots \mathcal{F}_{t-1}$$ )，稱為可預測過程。其定義確保$$A_t$$在時間$$t$$之前已經完全確定。<mark style="background-color:red;">可預測過程的定義是為了在處理隨機現象時，能夠嚴格地區分基於過去信息的行為和可能依賴於未來信息的行為</mark>。

* 它是鞅分解和其他理論構造的核心組成部分，提供隨機過程的分類工具。
* 它在隨機積分中確保了因果性(避免預知未來，或者說避免使用到未來的資料，而是基於過去信息的決策)和數學性質的保持。
* 它在應用領域（如金融）中反映了現實的決策過程。
* 它幫助區分隨機過程的不同行為，並在連續時間理論中有自然的推廣。

在隨機控制和濾波問題中，控制決策或估計通常只能基於過去的觀測信息。可預測過程自然地用於描述這些基於歷史的策略或估計。控制在時間$$t$$的動作$$A_t$$必須是基於時間$$t−1$$ 或更早的信息。

在金融數學中，可預測過程用於描述交易策略或賭注策略。例如：在離散時間的市場模型中，投資者的持倉$$H_t$$​（在時間$$t$$的股票數量）必須基於截至時間$$t-1$$的信息（即$$\mathcal{F}_{t-1}$$可測），因為在時間$$t$$的價格變動尚未發生。

* <mark style="color:red;">這種「可預測性」反映了現實中交易的因果關係：你只能根據過去和當前的信息做出決策，而不能預知未來</mark>。
* 如果沒有可預測過程的概念，交易策略可能依賴未來的價格信息，這在現實中不可行，也會導致無風險套利（arbitrage）等不合理的結論。

範例：

* 常數過程：如果$$A_t=c$$(常數)，則$$A_n$$是$$\mathcal{F}_{t-1}$$可測(因為常數對於任σ域都可測)，因此為可預測過程。
* 確定性過程：$$A_t=n^2$$為不依於任何隨機性的確定性序列。
* 滯後適應過程 (Lagged Adapted Process)：$$\{X_t\}$$為$$\mathcal{F}_t$$適應過程，定義$$A_0$$為$$\mathcal{F}_0$$可測且$$\forall n \in \mathbb{N}, A_n = X_{n-1}$$，則$$A_n$$為可預測過程。
* 基於過去信息的決策 (Decisions Based on Past Information)：假設在時間$$t$$根據時間$$t−1$$的信息做出一個決策，這個決策可以用隨機變數$$A_t$$來表示。如果你的決策只基於$$\mathcal{F}_{t−1}$$中包含的信息，那麼$$A_t$$\
  就是可預測的。



## Doob最大值不等式（Maximal Inequalities）

> (?)$$\{X_t\}$$為平賭過程，令$$M_t = \max_{k \leq t} X_k$$，則：$$\mathrm{P}(M_t \geq a ) \leq \frac{\mathrm{E}(|X_t|)}{a}, ~\forall a > 0$$。
>
> 在$$L^p$$空間可表示為$$\displaystyle \| \max_{k \leq t} |X_k|\|_p \leq \frac{p}{p-1} \| X_t\|_p$$
>
> 這表明鞅的最大值受到其期望值的限制。
>
> 直觀意義 ：鞅的最大值不太可能遠離其初始值。

## 鞅收斂定理(martingale convergence theorem)

> 如果鞅的數值不會變得太大（有個上限），它長期會穩定下來，不會一直亂跳。
>
> 直觀想法：如果一個隨機過程的期望值在時間上保持穩定（鞅性質），並且該過程不會「爆炸」(發散)（有界性條件，變異數受控制），那麼該過程不可能無限振盪或發散，最終會收斂於某個穩定值。
>
> 關鍵分析工具：Doob 的分解和不等式，分析鞅的上下穿越次數，證明振盪有限。
>
> <mark style="background-color:red;">平賭收斂定理可以被視為隨機過程中的「單調收斂定理」或「有界收斂定理」的隨機版本</mark>。
>
> * **核心內容**：在一定條件下，鞅序列 $$\{X_t\}$$ 會隨著 $$t \to \infty$$ 幾乎必然（almost surely）收斂到某個有限極限。
> * **直觀解釋**：鞅的隨機波動不會無限增長，而是最終穩定下來，趨向某個值。
> *   Martingale Convergence Theorem 是分析隨機過程收斂性的強大工具，特別適用於研究長期行為或漸近性質。
>
>     鞅收斂定理有多個版本，以下是常見的版本：
>
>     1. $$L^1$$ **有界鞅（均值有界）**：
>        * **條件**：若$$\{X_t)\}$$是鞅，且$$\mathrm{E}(|X_t|) \leq C < \infty$$（均值有一致上界, uniform bounded）。
>        * **結論**：存在隨機變數$$X_\infty$$，使得 $$X_t \to X_\infty$$ 幾乎必然，且$$\mathrm{E}(|X_\infty|) < \infty$$。
>        * **例子**：若$$\{X_t\}$$是賭徒財富，總期望損益有界，則財富最終穩定。
>     2. $$L^2$$**有界鞅（變異數有界）**：
>        * **條件**：若$$\{X_t\}$$是鞅，且$$\mathrm{E}(X_t^2) \leq C < \infty$$（二階動差有一致上界）。
>        * **結論**：$$X_t \to X_\infty$$幾乎必然，且$$X_\infty$$ 在$$L^2$$ 中（變異數有限）。
>     3. $$L^p$$收斂：
>        * **條件**：若$$\{X_t\}$$是鞅，me 且$$L^p, ~p>1$$有界，即$$\sup_t \mathrm{E}(|X_t|^p)<\infty$$(期望有界)。
>        * **結論**：$$X_t \to X_\infty$$幾乎必然，且$$X_\infty$$ 在$$L^p$$ 中。
>
> 常見範例：簡單隨機漫步，如果隨機漫步的步長均值為0，則該過程是一個鞅。根據鞅收斂定理，若該過程有界，則它會收斂於某個隨機變數。

在實際應用中，有界性條件有助於提高模型的穩定性。例如：

* **金融數學**：資產價格通常被建模為有界的隨機過程，以避免不現實的無限價格。
* **物理系統**：有界性條件反映了系統的物理限制，例如能量或位置的限制
