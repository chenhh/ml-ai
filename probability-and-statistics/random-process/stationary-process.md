---
description: 平穩過程
---

# 定態過程(stationary process)

時間序列討論的實數值離散隨機過程$$\{X_t, t \in T\}$$，即$$T=\mathbb{Z} \equiv \{0, \pm 1, \pm2, \dots,\}$$，且$$X_t(\omega) \in \mathbb{R}, ~\forall \omega \in \Omega$$。

## 定態過程

給定離散或連續隨機過程$$\{X_t, t \in T\}$$，<mark style="color:blue;">強定態過程要求聯合機率分佈與時間點</mark>$$t$$<mark style="color:blue;">無關(機率分佈非時變)，只與時間跨度有關，因此在平均值、變異數存在時(分佈可能不存在高階動差，如Cauchy分佈)，可得時間點</mark>$$t$$<mark style="color:blue;">(單變數)分佈的平均值、變異數為常數，而任兩個時間點間隨變數(聯合分佈)的共變異數與相關係數只與時間跨度</mark>$$h$$<mark style="color:blue;">有關</mark>。

常見的強定態過程為獨立同分佈(i.i.d.)的抽樣樣本，白噪音。

在一般應用中，聯合分佈機率分佈非時間的條件相當嚴格，因此通常<mark style="color:blue;">只要求隨機過程的平均值與變異數存在且非時變，且共變異數與相關係數只與時間跨度</mark>$$h$$<mark style="color:blue;">有關，稱為弱定態過程</mark>。

在機率分佈中，給定前四階動差(平均值、變異數、偏度、峰度)相對於只給定平均值與變異數，對於分佈的形狀誤差會更少(可由動差/特徵生成函數的性質得出)。而弱定態過程不要求偏度、峰度非時變，因此相對於強定態過程放寬了分佈非時變的限制。

<mark style="color:red;">均值與變異數存在的強定態過程必為弱定態過程(反之不一定成立，見範例)</mark>。由於分佈的均值必存在，因此有時只要求變異數(或二階動差$$\mathrm{E}(X_t^2) < \infty$$)存在。

| 屬性         | 強定態                       | 弱定態                                     |
| ---------- | ------------------------- | --------------------------------------- |
| 定義範圍       | 所有階的分佈（包括高維聯合分佈）          | 僅限於一階矩（均值）和二階矩（自協方差）                    |
| 嚴格性        | 更嚴格，涵蓋所有統計特性              | 更寬鬆，僅關注部分統計特性                           |
| 驗證難度       | 驗證所有階的分佈不變性非常困難，需要完整的分佈資訊 | 只需驗證均值和自協方差，相對容易                        |
| 應用範圍       | 主要用於理論研究                  | 廣泛應用於時間序列分析、訊號處理等實際問題                   |
| 關係         | 強定態必定是弱定態（但反之不一定成立）       | 弱定態不一定滿足強定態                             |
| 均值         | 恆定（隱含在分佈不變中）              | 必須顯式恆定                                  |
| 方差(變異數)    | 恆定且有限（隱含在分佈不變中）           | 必須顯式恆定且有限                               |
| 自協方差(自變異數) | 僅依賴時間差（隱含在分佈不變中）          | 必須顯式僅依賴時間差                              |
| 分佈形式       | 必須不變                      | <mark style="color:red;">不要求分佈不變</mark> |

### 強定態過程(strong stationary process)

> 隨機過程$$\{X_t, t \in T\}$$滿足以下條件時稱為強定態過程。
>
> 隨機過程的任意聯合分佈不隨時間變化(分佈非時變)。
>
> <mark style="color:blue;">強定態過程只要求分佈非時變，但不要求分佈的動差必須存在(動差可為</mark>$$\pm \infty$$<mark style="color:blue;">)</mark>。
>
> <mark style="color:red;">因為強定態過程中，動差不一定存在(如i.i.d. 的Cauchy隨機變數過程)，因此存在非弱定態過程的強定態過程</mark>。
>
> <mark style="color:blue;">當</mark>強定態過程的均值和變異數存在時，可得均值和變異數為常數，且共變異數和相關係數為時間跨度的函數<mark style="color:red;">。</mark>

即給定隨機過程任意兩個時間跨度相同的區間，其聯合分佈均相同。

<mark style="color:blue;">強定態過程條件非常嚴格，通常是人為製造的序列(如i.i.d.的樣本抽樣)</mark>。

令$$n$$維的機率分佈為：$$F_{X_1, \dots, X_n}(x_1, \dots, x_n) = \mathrm{P}(\omega \in \Omega ~|~ X_1 \leq x_1, \dots, X_h \leq x_n)$$，$$x_i \in \mathbb{R}$$。

* 1階強定態過程滿足$$F_{X_1}(x_1) = F_{X_{1+h}}(x_1), ~ \forall h$$
* 2階強定態過程滿足$$F_{X_1, X_2}(x_1, x_2) = F_{X_{1+h}, X_{2+h}}(x_1, x_2), ~ \forall h$$
* n階強定態過程滿足$$F_{X_1, \dots, X_n}(x_1, \dots,x_n) = F_{X_{1+h},\dots, X_{n+h}}(x_1, \dots,x_n), ~ \forall h$$

<mark style="color:red;">對於任意</mark>$$n$$<mark style="color:red;">，均為n階強定態過程的隨機過程稱為強定態過程</mark>。

由定義可知，n階強定態過程中，當$$m \leq n$$時，可得m階強定態過程。

### 強定態的過程的均值與變異數為常數，共變異數和相關係數為跨度的函數

給定隨機過程$$\{Z_t, t \in T\}$$，定義

* 均值為$$\mu_t = \mathrm{E}(Z_t)$$。
* 變異數$$\sigma_t^2 = \mathrm{E}(Z_t - \mu_t)^2  = \mathrm{E}(Z_t^2) - \mu_t^2$$。
* 共變異數$$\gamma(i, j)=\mathrm{E}(Z_i - \mu_i)(Z_j - \mu_j)$$。
* 相關係數$$\rho(i,j)=\frac{\gamma(i,j)}{\sigma_i, \sigma_j}$$

由於強定態過程$$\{X_t, t\in T\}$$的(聯合)分佈非時變，

* <mark style="color:blue;">假設平均值存在</mark>$$\mathrm{E}(|X_t|)<\infty$$，可得平均值$$\mu_t=\mu, ~\forall t \in T$$為常數。
* <mark style="color:blue;">假設二階動差存在</mark>$$\mathrm{E}(X_t^2)<\infty$$，可得變異數$$\sigma_t^2 = \sigma^2, ~\forall t \in T$$為常數。

由n階聯合分佈非時變得$$F_{X_1, X_2}(x_1, x_2) = F_{X_{1+h}, X_{2+h}}(x_1, x_2), ~ \forall h$$：

* 共變異數$$\gamma(i,j)=\gamma(i+h, j+h), ~\forall i,j,h$$
* 相關係數$$\rho(i,j)=\rho(i+h, j+h), ~\forall i,j,h$$

整理可得當$$i=t-h, j=t$$或$$i=t, j=t+h$$：

* $$\gamma(i,j)=\gamma(t-h, t)=\gamma(t, t+h)=\gamma_h$$ 為時間跨度$$h$$的函數。
* $$\rho(i,j)=\rho(t-h, t)=\rho(t, t+h)=\rho_h$$ 為時間跨度$$h$$的函數。

整理得當強定態過程的均值和變異數存在時，可得均值和變異數為常數，且共變異數和相關係數為時間跨度的函數<mark style="color:red;">。</mark>

### 弱定態過程(weak stationary process)

> 隨機過程$$\{X_t, t \in T\}$$滿足前2階動差(均值/變異數)存在，且時間跨度$$h$$的共變異數與相關係數非時變時，稱為弱定態過程。
>
> 1. \[期望值存在且為定值] $$\mathrm{E}(|X_t|) <\infty$$且$$\mathrm{E}(X_t) =\mu, ~\forall t\in T$$。
> 2. \[變異數存在且為定值] $$\mathrm{E}(X_t^2) <\infty$$且$$\sigma_t^2 =\sigma, ~\forall t\in T$$
> 3. \[共變異數為時間跨度的函數] $$\gamma(i, j)=\gamma_h$$。
> 4. \[相關係數為時間跨度的函數] $$\rho(i, j)=\gamma_h$$。
>
> <mark style="color:red;">一般討論的定態過程都是指弱定態過程(二次定態過程)</mark>。
>
> 因為只要求前2階動差(均值/變異數)存在，分佈的形狀不唯一(因兩分佈相等若且唯若動差生成函數相等)，因此<mark style="color:red;">分佈可為時變</mark>。
>
> <mark style="color:blue;">任意的強定態過程不一定是弱定態過程，因為強定態過程的動差不一定存在，如i.i.d.的Cauchy隨機變數形成的過程。</mark>
>
> <mark style="color:blue;">如果強定態過程中，平均值和變異數存在時，則為弱定態過程。</mark>

令$$\mathrm{E}(X_t)=c$$，則$$\mathrm{Cov}(X_t, X_{t+h})=\mathrm{E}(X_t X_{t+h})- \mathrm{E}(X_t) \mathrm{E}(X_{t+h}) = \mathrm{E}(X_t X_{t+h}) - c^2$$。因此條件3中期望值和共變異數只與$$h$$有關概念可通用。

弱定態過程中：

1. 只要求聯合分佈的均值與變異數不變，因此分佈可為時變。
2. <mark style="color:red;">若</mark>$$X_t$$<mark style="color:red;">為常態分佈時，因為常態分佈的性質，弱定態過程會滿足強定態過程的條件</mark>。

### 範例：週期函數

考慮時間序列$$X_t = A \sin (\omega t + \theta)$$，其中

* $$A$$為均值0，變異數1的隨機變數。
* $$\theta \sim U(-\pi, \pi)$$均勻分佈的隨機變數，且與$$A$$獨立。

可得：

$$\mathrm{E}(X_t)=\mathrm{E}(A) \mathrm{E}(\sin(\omega t + \theta)) = 0 \cdot \mathrm{E}(\sin(\omega t + \theta)) = 0$$。

$$\begin{align} \displaystyle \mathrm{E}(X_t X_{t+h})  &= \mathrm{E}(A^2 \sin(\omega t + \theta) \sin(\omega(t+h)+\theta) ) \\ &= \frac{1}{2} \cos(\omega h) - \mathrm{E}(A^2) \mathrm{E}\left\{ 1/2 \cos(\omega h) - \cos (\omega (2t+h)+2\theta) \right\} \\  &= 1/2 \cos(\omega h) - 1/2 \mathrm{E}(\cos(\omega(2t+h)+2\theta)) \\ &= 1/2 \cos(\omega h) - 1/2 \int_{-{\pi}}^{\pi} \cos(\omega(2t+h+2\theta)) \cdot \frac{1}{2 \pi}d\theta \\ &= 1/2 \cos(\omega h) - \frac{1}{8 \pi} [\sin(\omega(2t+h)+2\theta)]_{-\pi}^\pi \\ & = \frac{1}{2} \cos(\omega h)  \end{align}$$

只與$$h$$有關。

因此為弱定態隨機過程。

### 範例：弱定態但非強定態隨機過程

令$$\{Z_t\}$$為交替由標準常態分佈$$N(0,1)$$與雙值離散均勻分佈$$\{-1,1\}$$的隨機過程。

由常態分佈和均勻分佈可得$$\mathrm{E}(Z_t)=0, ~ \mathrm{E}(Z_t^2)=1, ~\forall t$$。

$$\mathrm{E}(Z_t Z_s)=\begin{cases}0, & \text{ if } t \neq s, \\ 1 & \text{ if } t= s\end{cases}$$

且$$\rho(t,s)=\frac{\mathrm{E}(Z_t Z_s)}{\sqrt{\mathrm{E}(Z_t^2)} \sqrt{\mathrm{E}(Z_s^2)}} = \begin{cases}0, & \text{ if } t \neq s, \\ 1 & \text{ if } t= s\end{cases}$$

因此為弱定態隨機過程，但是此過程的分佈不固定，因此不是強定態隨機過程。



### 範例: AR(1)模型

> $$X_t = c X_{t-1} + \epsilon_t$$,  $$\epsilon_t \sim \text{i.i.d} (0, \sigma^2)$$為獨立同分佈的白噪音。
>
> 即$$\mathrm{E}(\epsilon_t \epsilon_s)=0, ~ \forall s \neq t$$且  $$\mathrm{E}(\epsilon_t^2)=\sigma^2$$。
>
> * 當$$|c| > 1$$時，為非定態過程。
> * 當$$c=1$$時，為隨機漫步過程。
> * 當$$|c|<1$$時，為弱定態過程。

&#x20;將離散隨機過程展開得：

$$\begin{aligned}  X_t & = c X_{t-1} + \epsilon_t \\     & = c(c X_{t-2}+ \epsilon_{t-1}) + \epsilon_t \\     & = c^2 X_{t-2} + c \epsilon_{t-1} + \epsilon_t \\     & \vdots \\     & = c^t X_0 + c^{t-1} \epsilon_{1} + c^{t-2} \epsilon_{2} + \dots + \epsilon_t \end{aligned}$$

兩側取期望值可得：$$\mathrm{E}(X_t) = c^t \mathrm{E}(X_0)$$，如果已知$$X_0$$的實現值$$x_0$$，可寫成$$\mathrm{E}(X_t) = c^t x_0$$。

變異數為：

$$\displaystyle  \begin{aligned}  \mathrm{Var}(X_t) & = \mathrm{E}(X_t - \mathrm{E}(X_t))^2 \\     & = \mathrm{E}(c^{t-1} \epsilon_1 + c^{t-2} \epsilon_2 + \dots + \epsilon_t)^2 \\     & = c^{2(t-1)}\mathrm{E}(\epsilon_1^2) +c^{2(t-2)}\mathrm{E}(\epsilon_2^2) +  \dots + \mathrm{E}(\epsilon_t^2) \\     & = \sigma^2 \sum_{j=0}^{t-1} c^{2j} \end{aligned}$$

共變異數值：

$$\displaystyle  \begin{aligned}  \mathrm{Cov}(X_t, X_{t-s}) & = \mathrm{E}[(X_t - \mathrm{E}(X_t))(X_{t-s} - \mathrm{E}(X_{t-s})) ]  \\     & = \mathrm{E}[(c^{t-1}\epsilon_1 + c^{t-2}\epsilon_2 + \dots + \epsilon_t )                    (c^{t-s-1}\epsilon_1 + c^{t-s-2}\epsilon_2 + \dots + \epsilon_{t-s} ] \\     & = \sigma^2 \sum_{j=s}^{t-1} c^{2j-s} \end{aligned}$$

以下考慮$$t \rightarrow \infty$$的性質。

#### 當$$|c| > 1$$時

可得$$\mathrm{E}(X_t) \rightarrow \infty$$，同理$$\mathrm{Var}(X_t) \rightarrow \infty$$且$$\mathrm{Cov}(X_t, X_{t-s}) \rightarrow \infty$$不滿足定態性質。

#### 當$$c=1$$時

$$X_t = X_{t-1} + \epsilon_t$$為隨機漫步模型。在時間$$t$$時可得：

* $$\mathrm{E}(X_t) = x_0$$
* $$\mathrm{Var}(X_t) =\sigma^2 t$$
* $$\mathrm{Cov}(X_t , X_{t-s})=(t-s)\sigma^2$$

期望值為定值，但變異數和共變異數隨著$$t$$變化，不滿足定態性質。

#### 當$$|c| < 1$$時

考慮$$t \rightarrow \infty$$可得：

* $$\mathrm{E}(X_t) = 0$$為定值。
* $$\mathrm{Var}(X_t)= \lim_{t \rightarrow \infty }\sigma^2 (1+c^2 + \dots c^{2(t-1))}) = \frac{\sigma^2}{1-c^2}$$與$$t$$無關。
* $$\mathrm{Cov}(X_t, X_{t-1}) = \lim_{t \rightarrow \infty}c^2 (1+c^2 + \dots +c^{2(t-s-1)}) = \frac{\sigma^2 c^2}{1-c^2 }$$與$$t$$無關。

因此在這個條件下為定態過程。

## 判定資料序列是否為定態序列

| 方法             | 適用場景        | 優點                | 缺點          |
| -------------- | ----------- | ----------------- | ----------- |
| **視覺化**        | 初步直觀判斷趨勢和波動 | 簡單直觀              | 主觀性強        |
| **ADF 檢定**     | 檢測單位根（非定態性） | 廣泛使用              | 對趨勢定態可能誤判   |
| **KPSS 檢定**    | 檢測趨勢定態性     | 與 ADF 互補          | 需與 ADF 結合解讀 |
| **差分法**        | 處理非定態序列     | 直接改善定態性           | 可能過度差分      |
| **ACF/PACF 圖** | 觀察自相關結構     | 輔助判斷定態性和 ARIMA 模型 | 需經驗解讀       |

### **步驟 1：視覺化分析**

首先通過繪製時間序列圖來初步觀察資料的行為：

* **檢查均值是否穩定**：如果序列有明顯的趨勢（上升或下降），均值可能隨時間變化，非定態。
* **檢查方差是否穩定**：如果序列的波動幅度隨時間增大或縮小（例如越來越大的振盪），方差可能不恆定，非定態。
* **檢查週期性**：如果有明顯的季節性或週期性，可能需要進一步分析是否為定態（週期性本身不一定否定定態，但可能需要去除）。

**工具**：

* 時間序列圖（Time Series Plot）。
* 移動平均圖：計算區域性均值，觀察是否隨時間漂移。

**例子**：

* 如果資料是$$[1, 2, 3, 4, 5, 6]$$，明顯有線性趨勢，非定態。
* 如果資料是$$[1, -1, 2, -2, 1, -1]$$，看起來像隨機波動，可能接近定態。

### **步驟 2：分割資料檢查統計量**

將時間序列分成幾段（例如前半段和後半段），計算每段的均值和方差：

* **均值**：如果各段均值差異顯著，說明均值不穩定。
* **方差**：如果各段方差差異很大，說明方差不恆定。

**方法**：

* 計算整體均值 $$\bar{X} = \frac{1}{n}$$和分段均值。
* 計算整體方差 $$s^2 = \frac{1}{n-1} \sum (X_t - \bar{X})^2$$和分段方差。
* 用簡單的統計檢驗（如 t 檢驗或 F 檢驗）比較分段均值和方差是否一致。

**例子**：

* 資料$$[1, 2, 1, 10, 11, 12]$$：
  * 前三個：均值 ≈ 1.33，方差 ≈ 0.33；
  * 後三個：均值 ≈ 11，方差 ≈ 1；
  * 均值和方差變化明顯，非定態。

### **步驟 3：自相關分析**

弱定態要求自協方差只與時間差$$h$$有關。通過計算自相關函式（ACF, Autocorrelation Function）來檢查：

* **計算 ACF**：$$\rho(h) = \frac{Cov(X_t, X_{t+h})}{Var(X_t)}$$。
* **觀察模式**：
  * 如果 ACF 在$$h = 0$$時為 1，且隨著$$h$$增加快速衰減到 0，可能是定態(短期相關性）。
  * 如果 ACF 衰減很慢或有週期性波動，可能暗示趨勢或非定態（長期相關性）。

**工具**：

* ACF 圖：繪製自相關係數隨滯後$$h$$的變化。
* 偏自相關函式（PACF）：進一步確認是否存在 AR 結構。

**例子**：

* 白噪音 $$[1, -1, 2, -2]$$的 ACF 在$$h > 0$$時接近 0，可能是定態。
* 隨機遊走$$X_t = X_{t-1} + \epsilon_t$$的 ACF 衰減極慢，非定態。

#### 頻譜分析 定態序列：頻譜密度平滑。

非定態序列：可能出現明顯的趨勢或季節性峰值。

### **步驟 4：統計檢驗**

視覺化和簡單統計量只能提供初步判斷，正式判定需要統計檢驗。以下是常用檢驗：

**1. ADF 檢驗（Augmented Dickey-Fuller Test）**

* **目的**：檢驗是否存在單位根（單位根意味非定態）。
* **假設**：
  * 虛無假設$$H_0$$​：序列有單位根（非定態）。
  * 對立假設$$H_1$$​：序列無單位根（定態或趨勢定態）。
* **結果**：如果 p 值 < 0.05，拒絕$$H_0$$​，認為可能是定態。
* **注意**：ADF 可以檢測趨勢或漂移，需指定模型（無常數、有常數、有趨勢）。

**2. KPSS 檢驗（Kwiatkowski-Phillips-Schmidt-Shin Test）**

* **目的**：直接檢驗定態性。
* **假設**：
  * $$H_0$$：序列是定態的。
  * $$H_1$$​：序列非定態。
* **結果**：如果 p 值 < 0.05，拒絕 $$H_0$$​，認為非定態。
* **與 ADF 配合**：ADF 檢驗單位根，KPSS 檢驗水平定態，二者互補。

**3. PP 檢驗（Phillips-Perron Test）**

* 類似 ADF，但對序列依賴性和異方差更穩健。

**工具**：

* 使用統計軟體（如 R 的 tseries 包，Python 的 statsmodels）計算。

### **步驟 5：處理非定態**

如果序列被判定為非定態，可以嘗試轉換：

* **差分**：$$\Delta X_t = X_t - X_{t-1}$$​，去除趨勢。
* **對數變換**：$$\log(X_t)$$，穩定方差。
* **去趨勢/去季節性**：擬合線性模型或季節分解後分析殘差。

再對轉換後的序列重複以上步驟。



