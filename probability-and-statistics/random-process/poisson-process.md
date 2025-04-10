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
> * \[初始條件 ]$$N(0)=0$$，即在初始時刻沒有事件發生。
> * \[獨立增量性, independent Increments] 考慮不相交的時間區間$$(t_1,t_2 ], (t_2,t_3 ],\ldots ,(t_n,t_{n+1}]$$，則不相交區間的增量$$N({t_2})−N(t_1), N(t_3)-N(t_2),\ldots, N(t_{n+1}) - N(t_n)$$ 全為獨立。
> * \[定態增量 stationary Increments] 在任意長度為$$\tau$$ 的時間間隔內，發生事件的機率分佈相同。$$\forall 0 \leq s <t$$，$$N(t) = N(t)-N(0) \overset{d}{=} N(t+s) - N(s)$$。
> * \[增量為泊松分佈]：事件數服從 Poisson($$\lambda \tau$$) 分佈。 $$0\leq s <t$$，$$N(t) - N(s)  \sim Poisson(\lambda (t-s))$$為參數是$$\lambda(t-s)$$的泊松隨機變數(機率分佈僅於$$\tau=t-s$$有關，與起點$$s$$無關)。給定$$\lambda >0$$，得$$\mathrm{P}(N(t) - N(s) =k)= \frac{(\lambda(t-s))^ke^{-\lambda (t-s)}}{k!}, ~ k=0,1,2,\ldots$$.。

假想我們在一條公路上某點觀察通過這點的交通量。 令 $$N(t)$$ 為從時間 0 到時間$$t$$通過這點的汽車總數。 則

* \[初始條件]表示在時間 0 時，通過的車數是 0。&#x20;
* \[獨立增量條件]說在互不相交的時段內通過的車數是相互獨立的。&#x20;
* \[定態增量條件]說只要時段長度相同， 不同時段內通過的車數有相同的機率分佈。&#x20;
* \[增量為泊松分佈條件]$$N(t)$$有一個具有引數$$\lambda t$$的泊松分佈。

&#x20;如果觀察的全部時間不太長的話， 獨立增量條件和定態增量也是很合理的。 Poisson分佈條件在一般實測的交通量的紀錄也支援這一假定的。

### 小區間機率極限定義(微觀角度)

> 若一個計數過程$$\{N_t, t \geq 0\}$$  滿足以下四個條件時，稱為速度$$\lambda > 0$$的泊松過程：
>
> * \[初始條件] $$N(0)=0$$。
> * \[獨立增量性]同上。
> * \[定態增量]同上，但不假設增量為泊松分佈，而是用稀有事件假設。
> * 〔**\[稀有事件條件（Orderliness）] 在給定上面三條件時等價於泊松增量分佈條件。**
>   * 在極短時間$$\Delta t$$內，
>   * 不發生事件的機率：$$\mathrm{P}(N(\Delta t) =0) = 1-\lambda h + o(\Delta t)$$。
>   * 發生一次事件的機率與$$\Delta t$$成正比：$$\mathrm{P}(N(\Delta t) =1) = \lambda \Delta t + o(\Delta t)$$。
>   * 發生一次以上事件的機率可忽略，即：$$\mathrm{P}(N(\Delta t) \geq 2) = o (\Delta t)$$。
>   * 其中$$\displaystyle   f(t) = o(\Delta t) \equiv \lim_{ \Delta t \to 0}\frac{f(\Delta t)}{ \Delta t} = 0$$。

<mark style="color:red;">可證明在給定初始條件、獨立獨量性與定態增量條件下，增量為泊松分佈與稀有事件假設兩者等價</mark>。

<details>

<summary>proof: 增量為泊松分佈&#x3C;⇒ 稀有事件假設</summary>

增量為泊松分佈=> 稀有事件假設

給定$$\tau = t-s$$，已知$$\mathrm{P}(N(\tau)=k)=  \frac{(\lambda \tau)^ke^{-\lambda \tau}}{k!}, ~ k=0,1,2,\ldots$$

可得當$$k=0, 1$$時，由Taylor級數$$e^x=1+x+\frac{x^2}{2!}+\dots$$得：

* $$\mathrm{P}(N(\tau)=0)=e^{-\lambda \tau}=1-\lambda \tau + \frac{(\lambda \tau)}{2!} + \dots = 1- \lambda \tau + o(\tau)$$。
* $$\mathrm{P}(N(\tau)=1)=e^{-\lambda \tau}(\lambda \tau) = (\lambda \tau)(1- \lambda \tau + o(\tau))=\lambda \tau + o(\tau)$$。
* 所以$$\mathrm{P}(N(\tau) \geq 2) = 1 - \mathrm{P}(N(\tau) = 0 ) - \mathrm{P}(N(\tau) =1)=o(\tau)$$。

(QED)

稀有事件假設⇒ 增量為泊松分佈

在時間$$t+\tau$$發生事件$$k$$次，可拆解為區間$$[0,t)$$發生$$k$$次，且區間$$[t,t+\tau)$$區間發生$$0$$次；區間$$[0,t)$$發生$$k-1$$次，且區間$$[t,t+\tau)$$區間發生$$1$$次; 以此類推到區間$$[0,t)$$發生$$0$$次，且區間$$[t,t+\tau)$$區間發生$$k$$次的機率總和。

$$\begin{aligned} \mathrm{P}(N(t + \tau) = k) &= \mathrm{P}(N(t)= k \land N(t + \tau) - N(t)= 0)  \\  &+  \mathrm{P}(N(t)= k-1 \land N(t + \tau) - N(t)= 1) \\  &+ \mathrm{P}(N(t)= k-2 \land N(t + \tau) - N(t)= 2) \\  &+  \dots \\  &+  \mathrm{P}(N(t)= 0 \land N(t + \tau) - N(t)= k) \\ \end{aligned}$$--(1)

因為區間$$[0,t), [t+\tau)$$不相交，由獨立增量條件得：$$\mathrm{P}(N(t)= k \land N(t + \tau) - N(t)= 0) =  \mathrm{P}(N(t)= k) \mathrm{P}(N(t + \tau) - N(t)= 0)$$--(2)

再由定態分佈得$$\mathrm{P}(  N(t + \tau) - N(t)= 0) = \mathrm{P}(  N(\tau)= 0)$$--(3)

整理(1)(2)(3)得：

$$\begin{aligned} \mathrm{P}(N(t + \tau) = k) &= \mathrm{P}(N(t)= k)\cdot \mathrm{P}(  N(t + \tau) - N(t)= 0) ) \\  &+  \mathrm{P}(N(t)= k-1) \cdot \mathrm{P}( N(t + \tau) - N(t)= 1)) \\  &+ \mathrm{P}(N(t)= k-2) \cdot \mathrm{P}( N(t + \tau) - N(t)= 2)) \\  &+  \dots \\  &+  \mathrm{P}(N(t)= 0) \cdot \mathrm{P}( N(t + \tau) - N(t)= k)) \\ \end{aligned}$$$$\begin{aligned} \mathrm{P}(N(t + \tau) = k) &= \mathrm{P}(N(t)= k)\cdot \mathrm{P}(   N(\tau)= 0) \\  &+  \mathrm{P}(N(t)= k-1) \cdot \mathrm{P}(  N(\tau)= 1) \\  &+ \mathrm{P}(N(t)= k-2) \cdot \mathrm{P}(  N(\tau)= 2) \\  &+  \dots \\  &+  \mathrm{P}(N(t)= 0) \cdot \mathrm{P}(  N(\tau)= k) \\ \end{aligned}$$--(4)

由稀有事件條件代入(4)得：

$$\begin{aligned} \mathrm{P}(N(t + \tau) = k) &= \mathrm{P}(N(t)= k)\cdot (1-\lambda \tau + o(\tau)) \\  &+  \mathrm{P}(N(t)= k-1) \cdot (\lambda \tau + o(\tau)) \\  &+ \mathrm{P}(N(t)= k-2) \cdot o(\tau) \\  &+  \dots \\  &+  \mathrm{P}(N(t)= 0) \cdot o(\tau) \\  & = \mathrm{P}(N(t)= k) - \lambda \tau \mathrm{P}(N(t)= k) + \lambda \tau  \mathrm{P}(N(t)= k-1) + o(\tau) \end{aligned}$$因為$$\tau \neq 0$$，在$$k\geq 1$$時移項得：

$$\frac{ \mathrm{P}(N(t+\tau)= k) - \mathrm{P}(N(t)= k) }{\tau} = -\lambda \mathrm{P}(N(t)= k) +  \lambda \mathrm{P}(N(t)= k-1)  + o(1)$$

取極限$$\tau \to 0$$得Kolmogorov方程式：

$$\begin{cases} \mathrm{P}^{'}(N(t)= k) &= -\lambda \mathrm{P}(N(t)= k) + \lambda \mathrm{P}(N(t)= k-1), \quad k = 1,2,\dots, \\ \mathrm{P}^{'}(N(t)= 0) &=  -\lambda \mathrm{P}(N(t)= 0) \end{cases}$$--(5)

解$$\mathrm{P}^{'}(N(t)= 0) =  -\lambda \mathrm{P}(N(t)= 0)$$得$$\log \mathrm{P}(N(t)= 0) = -\lambda t + c$$ 或$$\mathrm{P}(N(t)= 0)= c e^{-\lambda t}$$。

由初始條件$$\mathrm{P}(N(0)= 0)=1$$得$$c=1$$，因此$$\mathrm{P}(N(t)= 0) = e^{-\lambda t}$$--(6)

由數學歸納法解$$\mathrm{P}^{'}(N(t)= k) = -\lambda \mathrm{P}(N(t)= k) + \lambda \mathrm{P}(N(t)= k-1), \quad k = 1,2,\dots,$$

初始條件為$$\mathrm{P}(N(0)= k)=0, k \neq 0$$，可得$$\mathrm{P}(N(t)= k)=\frac{(\lambda t)^k}{k!}e^{-\lambda t}, k \in \mathbb{N}$$

(QED)

</details>

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



