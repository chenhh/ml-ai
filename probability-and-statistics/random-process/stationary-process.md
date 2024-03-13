---
description: 平穩過程
---

# 定態過程(stationary process)

## 定態過程

給定離散或連續隨機過程$$\{X_t, t \in T\}$$，<mark style="color:blue;">強定態過程要求聯合機率分佈與時間點</mark>$$t$$<mark style="color:blue;">無關(機率分佈非時變)，只與時間跨度有關，因此在平均值、變異數存在時(分佈可能不存在高階動差，如Cauchy分佈)，可得時間點</mark>$$t$$<mark style="color:blue;">(單變數)分佈的平均值、變異數為常數，而任兩個時間點間隨變數(聯合分佈)的共變異數與相關係數只與時間跨度</mark>$$h$$<mark style="color:blue;">有關</mark>。

常見的強定態過程為獨立同分佈(i.i.d.)的抽樣樣本，白噪音。

在一般應用中，聯合分佈機率分佈非時間的條件相當嚴格，因此通常<mark style="color:blue;">只要求隨機過程的平均值與變異數存在且非時變，且共變異數與相關係數只與時間跨度</mark>$$h$$<mark style="color:blue;">有關，稱為弱定態過程</mark>。

在機率分佈中，給定前四階動差(平均值、變異數、偏度、峰度)相對於只給定平均值與變異數，對於分佈的形狀誤差會更少(可由動差/特徵生成函數的性質得出)。而弱定態過程不要求偏度、峰度非時變，因此相對於強定態過程放寬了分佈非時變的限制。

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
* 變異數$$\sigma_t^2 = \mathrm{E}(Z_t - \mu_t)^2$$。
* 共變異數$$\gamma(i, j)=\mathrm{E}(Z_i - \mu_i)(Z_j - \mu_j)$$。
* 相關係數$$\rho(i,j)=\frac{\gamma(i,j)}{\sigma_i, \sigma_j}$$

由於強定態過程$$\{X_t, t\in T\}$$的(聯合)分佈非時變，

* <mark style="color:blue;">假設平均值存在</mark>$$\mathrm{E}(|X_t|)<\infty$$，可得平均值$$\mu_t=\mu, ~\forall t \in T$$為常數。
* <mark style="color:blue;">假設二階動差存在</mark>$$\mathrm{E}(X_t^2)<\infty$$，可得變異數$$\sigma_t^2 = \sigma^2, ~\forall t \in T$$為常數。

由分佈非時變得：

* 共變異數$$\gamma(i,j)=\gamma(i+h, j+h), ~\forall i,j,h$$
* 相關係數$$\rho(i,j)=\rho(i+h, j+h), ~\forall i,j,h$$

整理可得當$$i=t-h, j=t$$：

* $$\gamma(i,j)=\gamma(t-h, t)=\gamma(t, t+h)=\gamma_h$$ 為時間跨度的函數。
* $$\rho(i,j)=\rho(t-h, t)=\rho(t, t+h)=\rho_h$$ 為時間跨度的函數。

整理得當強定態過程的均值和變異數存在時，可得均值和變異數為常數，且共變異數和相關係數為時間跨度的函數<mark style="color:red;">。</mark>

### 弱定態過程(weak stationary process)

> 隨機過程$$\{X_t, t \in T\}$$滿足任意$$n$$階的動差均存在且非時變時，稱為弱定態過程。
>
> 1. \[期望值存在且為定值] $$\mathrm{E}(|X_t|) <\infty$$且$$\mathrm{E}(X_t) =\mu, ~\forall t\in T$$。
> 2. \[變異數存在且為定值] $$\mathrm{E}(X_t^2) <\infty$$且$$\sigma_t^2 =\sigma, ~\forall t\in T$$
> 3. \[共變異數為時間跨度的函數] $$\gamma(i, j)=\gamma_h$$。
> 4. \[相關係數為時間跨度的函數] $$\rho(i, j)=\gamma_h$$。
>
> <mark style="color:red;">一般討論的定態過程都是指弱定態過程(二次定態過程)</mark>。
>
> <mark style="color:blue;">任意的強定態過程不一定是弱定態過程，如i.i.d.的Cauchy隨機變數形成的過程。</mark>
>
> <mark style="color:blue;">如果強定態過程中，平均值和變異數存在時，則為弱定態過程。</mark>

令$$\mathrm{E}(X_t)=c$$，則$$\mathrm{Cov}(X_t, X_{t+h})=\mathrm{E}(X_t X_{t+h})- \mathrm{E}(X_t) \mathrm{E}(X_{t+h}) = \mathrm{E}(X_t X_{t+h}) - c^2$$。因此條件3中期望值和共變異數只與$$h$$有關概念可通用。

弱定態過程中：

1. 只要求聯合分佈的均值與變異數不變，因此分佈可為時變。
2. <mark style="color:red;">若</mark>$$X_t$$<mark style="color:red;">為常態分佈時，因為常態分佈的性質，弱定態過程會滿足強定態過程的條件</mark>。

## 範例: AR(1)模型

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

####

