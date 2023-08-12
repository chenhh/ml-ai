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
> * 當$$|c| > 1$$時，為非定態過程。
> * 當$$c=1$$時，為隨機漫步過程。
> * 當$$|c|<1$$時，為弱定態過程。
>
>
