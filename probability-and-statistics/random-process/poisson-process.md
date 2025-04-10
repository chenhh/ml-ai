# 泊松過程(Poisson process)

泊松過程（Poisson Process）是一種重要的計數隨機過程，用於描述在連續時間內事件發生的次數。

泊松過程是一系列離散事件的模型，事件之間的平均時間是已知的（確定的），但事件發生的確切時間是隨機的。一個事件的到來與之前的事件無關（事件之間的等待時間是無記憶的，且為指數分佈）。

重要的一點是我們知道事件之間的平均時間，但它們是隨機間隔的（隨機的）。故障之間是沒有相互聯絡的，但由於過程的隨機性，我們也可能在兩次故障之間間隔數年。

泊松過程符合以下標准（實際上許多以泊松過程為模型的現象並不完全符合這些標準)。

* 事件是相互獨立的。一個事件的發生並不影響另一個事件發生的機率。&#x20;
* 平均速率（每個時間段的事件）是恆定的。&#x20;
* 兩個事件不可能在同一時間發生。

最後一點--事件不是同時發生的--意味著我們可以把泊松過程的每個子區間看作是Bernouli試驗，也就是說，要麼成功，要麼失敗。

最經常討論的案例是給出的泊松過程的是公共汽車的到達（或火車或現在的Ubers）。然而，這並不是一個真正的泊松過程，因為到達的人數並不是相互獨立的。即使是不按時執行的公車系統，一輛公車是否遲到也會影響下一輛公車的到達時間。

## 泊松過程

* 計數過程定義強調分佈性質，便於計算機率。
* 小區間機率極限機率定義從微觀角度刻畫動態行為。
* 等待時間定義突出間隔時間的指數分佈和無記憶性。
* 條件均勻性定義則提供了事件時間點的分佈特性。

### 計數過程定義(基於事件次數分佈）

> 若一個計數過程$$\{N_t, t \geq 0\}$$  滿足以下三個條件時，稱為速度$$\lambda > 0$$的泊松過程：
>
> * \[初始條件 ]$$N(0)=0$$，即在初始時刻沒有事件發生。。
> * \[定態增量且為Poisson分佈, stationary Increments] 在任意長度為$$\tau$$ 的時間間隔內，發生事件的機率僅依賴於該間隔長度，而非時間起點，且事件數服從 Poisson 分佈。 $$s <t$$，計數增量$$N(t) - N(s)  \sim Poisson(\lambda (t-s))$$為參數是$$\lambda(t-s)$$的泊松隨機變數(j機率分佈僅於$$\tau=t-s$$有關，與起點$$s$$無關)。可得$$N(t) - N(s) \overset{d}{=} N(t-s)$$且 $$\mathrm{P}(N(t) - N(s) =k)= \frac{(\lambda(t-s))^ke^{-\lambda (t-s)}}{k!}, ~ k=0,1,2,\ldots$$.。
> * \[獨立增量性, independent Increments] 考慮不相交的時間區間$$(t_1,t_2 ], (t_2,t_3 ],\ldots ,(t_n,t_{n+1}]$$，則不相交區間的增量$$N({t_2})−N(t_1), N(t_3)-N(t_2),\ldots, N(t_{n+1}) - N(t_n)$$ 全為獨立。

### 小區間機率極限定義(微觀角度)

**\[稀有事件假設（Orderliness）]**

* 在極短時間$$\Delta t$$內，發生 一次以上 事件的機率可忽略，即：$$\mathrm{P}(N(\Delta t) \geq 2) = o (\Delta t)$$。
* 發生 一次事件的機率與$$\Delta t$$成正比：$$\mathrm{P}(N(\Delta t) =1) = \lambda \Delta t + o(\Delta t)$$。



### 事件間隔(等待)時間（Interarrival Times） 定義

> 泊松過程可以通過事件之間的等待時間來定義：

### 條件均勻性定義



> $$E(N(t)−N(s) )=\lambda(t−s)$$>

* &#x20;\[Taylor series] $$\displaystyle e^x = \sum_{k=0}^\infty \frac{x^k}{k!}=1+x+\frac{x^2}{2!}+\ldots = \sum_{k=1}^\infty \frac{x^{k-1}}{(k-1)!}$$
* $$\begin{aligned} \displaystyle \mathrm{E}(N(t)-N(s)) & =\sum_{k=0}^{\infty} k\cdot\mathrm{P}((N(t)-N(s))=k) \\ & = \sum_{k=0}^{\infty} k \frac{(\lambda(t-s))^ke^{-\lambda(t-s) }}{k!} \\ & =\lambda (t-s)e^{-\lambda (t-s)} \sum_{k=1}^\infty  \frac{\lambda ^{k-1}(t-1)^{k-1}}{(k-1)!} \\ & =\lambda (t-s)e^{-\lambda(t-s)}e^{\lambda(t-s)}\\ &= \lambda(t-s) \end{aligned}$$

&#x20;(QED)

> * $$\mathrm{E}((N(t)- N(s)^2)=\lambda^2(t-s)^2+\lambda (t-s)$$
> * $$\mathrm{Var}(N(t) - N(s))=\lambda (t-s)$$>

* $$\mathrm{Var}(X)  = \mathrm{E}(X^2) - (\mathrm{E}(X))^2$$
* $$\begin{aligned} \mathrm{Var}(N(t)-N(s)) & =\mathrm{E}((N(t)-N(s))^2) - (\mathrm{E}(N(t)-N(s)))^2 \\ &= \lambda^2 (t-s)^2 + \lambda (t-s) - \lambda^2 (t-s)^2\\ &=\lambda (t-s) \end{aligned}$$(QED)



![卜瓦松過程](../../.gitbook/assets/poisson-process-min.png)



