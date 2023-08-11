# 隨機漫步(random walk)

## 單一變數對稱隨機漫步

> $$X_0=0$$，$$X_t=Y_1+\dots+Y_t$$
>
> 其中$$\mathrm{P}(Y_t=1)=\mathrm{P}(Y_t=-1)=\frac{1}{2}$$
>
> 且$$Y_1, \dots, Y_t$$獨立。
>
> 滿足此條件的隨機過程$$X_t$$墜為單一變數對稱隨機漫步。

### 單一變數對稱隨機漫步的性質

1. $$\mathrm{E}(X_t)=0$$
2. $$\mathrm{Var}(X_t)=t$$
3. 若$$s <t$$，則$$X_s$$與$$X_t-X_s$$獨立。
4. $$\displaystyle \mathrm{P}(X_t=k) = \left\{ \begin{aligned} &\binom{t}{\frac{t+k}{2}} \left(\frac{1}{2}\right)^t ~&~ t+k \text{ is even and } -t \leq k \leq t \\ & 0   ~&~ t+k \text{ is odd or } |k| > t     \end{aligned} \right.$$



<details>

<summary>proof 期望值</summary>

$$\displaystyle  \begin{aligned} \mathrm{E}(X_t) & =\mathrm{E}(Y_1 + \dots + Y_t) \\     & = \mathrm{E}(Y_1) + \dots + \mathrm{E}(Y_t) \\     & = 0 + \dots 0 = 0   \end{aligned}$$

(QED)

</details>

<details>

<summary>proof: 變異數</summary>

$$\displaystyle  \begin{aligned} \mathrm{Var}(X_t) & =\mathrm{Var}(Y_1 + \dots + Y_t) \\     & = \mathrm{Var}(Y_1) + \dots + \mathrm{Var}(Y_t) ~ \because Y_t \text{ independent }\\     & = 1 + \dots + 1 \\     & = t \end{aligned}$$

(QED)

</details>

<details>

<summary>proof: 增量獨立</summary>

$$X_s = Y_1 + \dots +Y_s$$

$$X_t - X_s = Y_{s+1} + \dots +Y_t$$

因為$$Y_i, Y_j, i \neq j$$獨立，所以$$X_s, ~X_t - X_s$$獨立。(QED)

</details>
