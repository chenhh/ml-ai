# 定態過程(stationary process)

## 定態過程

給定離散或連續隨機過程$$\{X_t, t \in T\}$$

### 強定態過程(strong stationary process)

> 隨機過程$$\{X_t, t \in T\}$$滿足以下條件時稱為強定態過程。
>
> $$\forall h > 0$$，$$(X_t, X_{t+1}, \dots, X_{t+h})$$的聯合分佈與$$t$$無關，只與時間跨度$$h$$有關。

即給定隨機過程任意兩個時間跨度相同的區間，其聯合分佈均相同。

<mark style="color:blue;">強定態過程條件非常嚴格，通常是人工抽取獨立同分佈樣本時才會成立</mark>。

### 弱定態過程(weak stationary process)

> 隨機過程$$\{X_t, t \in T\}$$滿足以下條件時稱為弱定態過程。
>
> 1. \[期望值為定值] $$\mathrm{E}(X_t) = c$$。
> 2. \[有限變動] $$\mathrm{E}(X_t^2) < \infty$$。
> 3. \[變異程度只與時間跨度有關] $$\mathrm{E}(X_t X_{t+h})=g(h)$$。也可寫成$$\mathrm{Cov}(X_t, X_{t+h})=g(h)$$。
>
>
>
> <mark style="color:red;">一般討論的定態過程都是指弱定態過程(二次定態過程)</mark>。

令$$\mathrm{E}(X_t)=c$$，則$$\mathrm{Cov}(X_t, X_{t+h})=\mathrm{E}(X_t X_{t+h})- \mathrm{E}(X_t) \mathrm{E}(X_{t+h}) = \mathrm{E}(X_t X_{t+h}) - c^2$$。因此條件3中期望值和共變異數只與$$h$$有關概念可通用。

弱定態過程滿足：

1. 隨機過程中隨時間變化時，只要求均值與變異數不變。
2. 若$$X_t$$為常態分佈時，因為常態分佈的性質，弱定態過程會滿足強定態過程的條件。

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



