# 微分均值定理（mean-value theorem）

## Rolle's定理

> 假設函數$$f$$在開區間$$(a,b)$$可微分（因為可微分必須連續，因此只要加上端點函數值連續條件即可）。若$$f(a)=f(b)=0$$，則存在點$$c \in (a,b) \ni f^′ (c)=0$$。

> 註：對於夠平滑的函數$$f$$，若在區間$$(a,b)$$經過兩次$$x$$軸，則必定存在回轉點$$c$$。

![Rolle定理](../../.gitbook/assets/rolle\_thm-min.png)

廣義Rolle's定理


> $$f:(a,b) \rightarrow  \mathbb{R}$$ 為$$(n+1)$$階可微函數，$$n \in \mathbb{N}$$。> 滿足$$f(b)=0$$，$$f(a)=f^′ (a)=\ldots=f^{(n)} (a)=0$$。
>
> 則存在 $$c \in (a,b) \ni f^{(n+1)} (c)=0$$

## 微分均值定理(mean value theorem)

> 函數$$f$$在開區間$$(a,b)$$可微分，則
>
> * $$∃t_0 \in (a,b)∋f(b)−f(a)=f^′ (t_0 )(b−a)$$
> * 常寫成 $$\frac{f(x+h)−f(x)}{ℎ}=f^′ (x+θh), \ 0<\theta <1$$

> 註：微分MVT敘述函數由點a進入，點b離開，則必在區間$$(a,b)$$的某一點$$c$$，其導數等於函數圖形上二點$$A=(a, f(a))$$, $$B=(b,f(b))$$連接AB的斜率。

![微分均值定理](../../.gitbook/assets/diff\_mvt-min.png)

* 線段AB的方程式為 $$y=\frac{f(b)−f(a)}{b−a}(t−a)+f(a)=\frac{f(b)−f(a)}{b−a}t+\frac{bf(a)−af(b)}{b−a}$$
* 令$$F(t) \equiv f(t)−y$$，則$$F(a)=F(b)=0$$。
* 由Rolle定理得 $$\exists t_0 \in [a,b] \ni F^′ (t_0 )=0$$ (QED)
