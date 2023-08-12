# 定態過程(stationary process)

## 離散定態過程

給定離散隨機過程$$\{X_t, t \in \mathbb{N}\}$$

### 強定態過程(strong stationary process)

> 離散隨機過程$$\{X_t, t \in \mathbb{N}\}$$滿足以下條件時稱為強定態過程。
>
> $$\forall h > 0$$，$$(X_t, X_{t+1}, \dots, X_{t+h})$$的聯合分佈與$$t$$無關，只與時間跨度$$h$$有關。

即給定隨機過程任意兩個時間跨度相同的區間，其聯合分佈均相同。

<mark style="color:blue;">強定態過程條件非常嚴格，通常是人工抽取獨立同分佈樣本時才會成立</mark>。

### 弱定態過程(weak stationary process)

> 離散隨機過程$$\{X_t, t \in \mathbb{N}\}$$滿足以下條件時稱為弱定態過程。
>
> 1. \[期望值為定值] $$\mathrm{E}(X_t) = c$$。
> 2. \[有限變動] $$\mathrm{E}(X_t^2) < \infty$$。
> 3. \[變異程度只與時間跨度有關] $$\mathrm{E}(X_t X_{t+h})=g(h)$$。也可寫成$$\mathrm{Cov}(X_t, X_{t+h})=g(h)$$。
