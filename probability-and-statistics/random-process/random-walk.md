# 隨機漫步(random walk)

## 單一變數對稱隨機漫步

> $$X_0=0$$，$$X_t=\epsilon_1+\dots+\epsilon_t$$或者$$X_t=X_{t-1}+\epsilon_t$$
>
> 其中$$\mathrm{P}(\epsilon_t=1)=\mathrm{P}(\epsilon_t=-1)=\frac{1}{2}$$
>
> 且$$\epsilon_1, \dots, \epsilon_t$$獨立。
>
> 滿足此條件的隨機過程$$X_t$$稱為單一變數對稱隨機漫步。

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
> 且$$\epsilon_1, \dots, \epsilon_t$$獨立。
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
> $$\mathrm{P}(\epsilon_t=1)=, ~\mathrm{P}(\epsilon_t=-1)=1/2$$且$$\epsilon_1, \dots, \epsilon_t$$獨立。
>
> 則$$\displaystyle \mathrm{E}(X_{t+1} ~|~ \sigma(X_1, X_2, \dots, X_t)) = \mathrm{E}(X_{t+1} ~|~ X_1, X_2, \dots, X_t) = X_t$$

<details>

<summary>proof: 使用一般化的條件期望值定義</summary>

$$\displaystyle  \begin{aligned} \mathrm{E}(X_{t+1} ~|~ X_1, X_2, \dots, X_t)  &=  \mathrm{E}(X_t+ \epsilon_{t+1} ~|~ X_1, X_2, \dots, X_t) \\ & = \mathrm{E}(X_t~|~ X_1, X_2, \dots, X_t) + \mathrm{E}(\epsilon_{t+1} ~|~ X_1, X_2, \dots, X_t) \\ & = X_t + \mathrm{E}(\epsilon_{t+1}) \\ & = X_t + 0 \\ & = X_t   \end{aligned}$$

(QED)

</details>
