# 隨機漫步(random walk)

## 單一變數對稱隨機漫步

> $$X_0=0$$，$$X_t=\epsilon_1+\dots+\epsilon_t$$或者$$X_t=X_{t-1}+\epsilon_t$$
>
> 其中$$\mathrm{P}(\epsilon_t=1)=\mathrm{P}(\epsilon_t=-1)=\frac{1}{2}$$
>
> 且$$\epsilon_1, \dots, \epsilon_t$$獨立同分佈(i.i.d)。
>
> 滿足此條件的隨機過程$$X_t$$稱為單一變數對稱隨機漫步。

* $$\mathrm{E}(\epsilon_t)=0$$
* $$\mathrm{E}(\epsilon_t^2)=1$$
* $$\mathrm{Var}(\epsilon_t)=\mathrm{E}(\epsilon_t^2) - \mathrm{E}^2(\epsilon_t)=1$$

### 單一變數對稱隨機漫步的性質

1. $$\mathrm{E}(X_t)=0$$
2. $$\mathrm{Var}(X_t)=t$$
3. 若$$s <t$$，則$$X_s$$與$$X_t-X_s$$獨立。即$$\mathrm{P}(X_s, X_{t}-X_s)=\mathrm{P}(X_s) \mathrm{P}(X_{t}-X_s)$$
4. $$\displaystyle \mathrm{P}(X_t=k) = \begin{cases}  & \binom{t}{\frac{t+k}{2}} \left(\frac{1}{2}\right)^t ~&~ t+k \text{ is even and } -t \leq k \leq t \\ & 0   ~&~ t+k \text{ is odd or } |k| > t      \end{cases}$$\
   可視為丟$$t$$次公正銅板，出現$$u$$次正面，$$d$$次反面且$$u+d=t$$，$$u-d=k$$。



<details>

<summary>proof 期望值</summary>

$$\displaystyle  \begin{aligned} \mathrm{E}(X_t) & =\mathrm{E}(\epsilon_1 + \dots + \epsilon_t) \\     & = \mathrm{E}(\epsilon_1) + \dots + \mathrm{E}(\epsilon_t) \\     & = 0 + \dots 0 = 0   \end{aligned}$$

(QED)

</details>

<details>

<summary>proof: 變異數</summary>

$$\displaystyle  \begin{aligned} \mathrm{Var}(X_t) & =\mathrm{Var}(\epsilon_1 + \dots + \epsilon_t) \\     & = \mathrm{Var}(\epsilon_1) + \dots + \mathrm{Var}(\epsilon_t) ~ \because \epsilon_t \text{ independent }\\     & = 1 + \dots + 1 \\     & = t \end{aligned}$$

(QED)

</details>

<details>

<summary>proof: 增量獨立</summary>

$$X_s = \epsilon_1 + \dots +\epsilon_s$$

$$X_t - X_s = \epsilon_{s+1} + \dots +\epsilon_t$$

因為$$Y_i, Y_j, i \neq j$$獨立，所以$$X_s, ~X_t - X_s$$獨立。(QED)

</details>

## 單一變數非對稱隨機漫步

> $$X_0=0$$，$$X_t=\epsilon_1+\dots+\epsilon_t$$或者$$X_t=X_{t-1}+\epsilon_t$$
>
> 其中$$\mathrm{P}(\epsilon_t=1)=p, ~\mathrm{P}(\epsilon_t=-1)=1-p=q$$
>
> 且$$\epsilon_1, \dots, \epsilon_t$$獨立同分佈。
>
> 滿足此條件的隨機過程$$X_t$$稱為單一變數非對稱隨機漫步。

### 性質

* $$\mathrm{E}(\epsilon_t)=p-q$$。&#x20;
* $$\mathrm{E}(\epsilon^2)=p+q$$。
* $$\mathrm{Var}(\epsilon_t)=\mathrm{E}(\epsilon_t^2)-\mathrm{E}^2(\epsilon_t)=(p+q)-(p-q)^2=1-(p-q)^2$$
* $$\displaystyle \mathrm{E}(X_t)=\mathrm{E}(\epsilon_1+ \dots + \epsilon_t)=\sum_{i=1}^t \mathrm{E}(\epsilon_i)=t(p-q)$$。
* $$\displaystyle \mathrm{Var}(X_t)=\mathrm{Var}(\epsilon_1+ \dots + \epsilon_t)=\sum_{i=1}^t \mathrm{Var}(\epsilon_i) = t (1-(p-q)^2)$$
* \[增量獨立性]$$s < t$$，可得$$\mathrm{P}(X_s, X_{t-s})=\mathrm{P}(X_s)\mathrm{P}(X_{t-s})$$。

## 對稱隨機漫步為平賭過程

> $$X_t=X_{t-1}+\epsilon_t$$，
>
> $$\mathrm{P}(\epsilon_t=1)=, ~\mathrm{P}(\epsilon_t=-1)=1/2$$且$$\epsilon_1, \dots, \epsilon_t$$獨立同分佈。
>
> 則$$\displaystyle \mathrm{E}(X_{t+1} ~|~ \sigma(X_1, X_2, \dots, X_t)) = \mathrm{E}(X_{t+1} ~|~ X_1, X_2, \dots, X_t) = X_t$$

<details>

<summary>proof: 使用一般化的條件期望值定義</summary>

$$\displaystyle  \begin{aligned} \mathrm{E}(X_{t+1} ~|~ X_1, X_2, \dots, X_t)  &=  \mathrm{E}(X_t+ \epsilon_{t+1} ~|~ X_1, X_2, \dots, X_t) \\ & = \mathrm{E}(X_t~|~ X_1, X_2, \dots, X_t) + \mathrm{E}(\epsilon_{t+1} ~|~ X_1, X_2, \dots, X_t) \\ & = X_t + \mathrm{E}(\epsilon_{t+1}) \\ & = X_t + 0 \\ & = X_t   \end{aligned}$$

(QED)

</details>

### 平賭過程的期望值為常數

令集合$$I_t \equiv \{X_1, \dots, X_t\}$$，因為$$\mathrm{E}(X_{t+1}~|~ I_t)=X_t$$，由重覆期望值定理可得：$$\mathrm{E}(\mathrm{E}(X_{t+1}~|~I_t))=\mathrm{E}(X_{t+1}) = \mathrm{E}(X_t)$$。

依此遞迴下去可得$$\mathrm{E}(X_{t}) = \mathrm{E}(X_{t+1})=\dots = \mathrm{E}(X_{t+h}), ~ \forall t, h$$

移項可得$$\mathrm{E}(X_{t+h} -X_t)=0, h=1,2,\dots,$$

## 股價的隨機漫步模型(binomial model)

> 令初始時的股價為$$S_0$$，時間$$t$$的股價為$$S_t$$，在時間$$t+1$$時股價上漲為$$uS_t, ~ u \geq 1$$ 的機率為$$p$$，下跌為$$dSt, 0 < d <1$$的機率為$$q=1-p$$。
>
> <mark style="color:blue;">假設每一期股價上漲與下跌的機率不變</mark>。

在時間$$t=1$$的股價為：$$\displaystyle S_0 \Rightarrow \begin{cases} \mathrm{P}(S_1=uS_0)=p \\ \mathrm{P}(S_1=dS_0)=q \\ \end{cases}$$

定義Bernoulli隨機變數$$X_t = \begin{cases} u, & \text{ with prob. } p \\ d, & \text{ with prob } q \end{cases}$$$$t=1,2,\dots$$

因此時間$$t=1$$時股價可改寫為$$S_1=S_0X_1$$，且機率為$$\mathrm{P}(S_1=S_0u^rd^{1-r})=p^r q^{1-r}, ~r=0,1$$。

同理在$$t=2$$時，股價變動如下樹狀：

$$\displaystyle S_0 \Rightarrow \begin{cases} uS_0 \Rightarrow \begin{cases} u^2 S_0, \text{ with prob. } p^2 \\ ud S_0, \text{ with prob. } pq \\ \end{cases} \\ dS_0 \Rightarrow \begin{cases} ud S_0, \text{ with prob. } pq \\ d^2 S_0,\text{ with prob. } q^2  \\ \end{cases}  \\ \end{cases}$$

股價$$S_2=S_1X_2=S_0 X_1 X_2$$，且機率為$$\mathrm{P}(S_2=S_0u^rd^{2-r})=\binom{2}{r}p^r q^{2-r}, ~r=0,1,2$$。

<mark style="color:red;">以此類推可得股價在時間</mark>$$t$$<mark style="color:red;">價格與機率的通式</mark>：

$$\displaystyle S_t = S_0 \prod_{i=1}^n X_i$$，$$\mathrm{P}(S_t=S_0 u^r d^{t-r})=\binom{t}{r}p^r q^{t-r}, ~r=0,1,2,\dots, t$$。--(1)

#### 將隨機變數$$X_t$$視為連續複利

因為$$S_t=S_{t-1}X_t$$ 且$$S_t, S_{t-1} > 0$$，移項可得$$X_t=\frac{S_t}{S_{t-1}}$$，兩邊取對數得$$\log{X_t}=\log{S_t} - \log{S_{t-1}}$$得$$X_t$$為當期(連續)報酬率。

令$$\epsilon_t \equiv \log X_t=\begin{cases} \log u, \text{ with prob. } p \\ \log d, \text{ with prob. } q \end{cases}$$

則(1)可改寫為$$\displaystyle \log S_t = \log S_0 + \sum_{i=1}^t \epsilon_i$$ 或$$\log S_t = \log S_{t-1} + \epsilon_t$$。--(2)

由$$\epsilon_t$$定義可得：

* $$\mathrm{E}(\epsilon_t)=p \log u + q \log d$$，與時間$$t$$無關。
* $$\mathrm{E}(\epsilon_t^2)=p (\log u)^2 + q (\log d)^2$$
* $$\mathrm{Var}(\epsilon_t)=\mathrm{E}(\epsilon_t^2) - \mathrm{E}^2(\epsilon_t)=pq(\log u - \log d)^2$$，與時間$$t$$無關

為了簡化符號，令$$\mathrm{E}(\epsilon_t)= \mu$$, $$\mathrm{Var}(\epsilon_t)=\sigma^2$$--(3)。

因為假設$$X_t$$為獨立同分佈的二項式變數，因此可得$$\displaystyle \mathrm{E}(\sum_{i=1}^t \epsilon_t)=\mu t$$，$$\displaystyle \mathrm{Var}(\sum_{i=1}^t \epsilon_t)= \sigma^2 t$$--(4)

#### 將連續複利表示為遞迴關係式

令$$h_t = \frac{\epsilon_t - \mu}{\sigma}$$，$$\epsilon_t = \mu + \sigma h_t$$，可得

* $$\mathrm{E}(h_t)=p \cdot \frac{\log u -( p \log u + q \log d) }{\sigma} + q \cdot \frac{\log u - (p \log u + q \log d) }{\sigma} =0$$
* $$\mathrm{Var}(h_t) = 1$$。

<mark style="color:blue;">令</mark>$$W_0=0$$<mark style="color:blue;">，且</mark>$$W_t = W_{t-1} + h_t$$<mark style="color:blue;">為i.i.d.(0,1)的隨機變數</mark>$$h_t$$<mark style="color:blue;">經過</mark>$$t$$<mark style="color:blue;">期的隨機變數(此假設滿足</mark>$$S_t$$<mark style="color:blue;">為平賭過程)</mark>，可得：$$\displaystyle W_t = \sum_{i=1}^t h_t$$。

因此$$\displaystyle \sum_{i=1}^t {\epsilon_i} = \sum_{i=1}^t (\mu + \sigma h_t) = \mu t + \sigma \sum_{i=1}^t h_t=\mu t + \sigma W_t$$--(5)

由(2,5)得$$\log S_t = \log S_0 + \mu t + \sigma W_t$$



####





####
