# 函數的極限

## 平均變化與割線\(average rate of change and secant\)

> 函數$$y=f(x)$$在區間$$[x_1, x_2]$$的平均變化率為 $$\frac{\Delta y}{\Delta x}=\frac{f(x_2) - f(x_1)}{x_2 - x_1}=\frac{f(x_1+h) -f(x_1)}{h}, ~ h \neq 0$$

![&#x5E73;&#x5747;&#x8B8A;&#x5316;&#x7387;](../../.gitbook/assets/average-change-of-rate-min.png)

![&#x7531;&#x5272;&#x7DDA;&#x6F38;&#x8FD1;&#x5230;&#x5207;&#x7DDA;&#x7684;&#x904E;&#x7A0B;](../../.gitbook/assets/secant-to-tangent-min.png)

![&#x5272;&#x7DDA;&#x903C;&#x8FD1;&#x5230;&#x5207;&#x7DDA;&#x7684;&#x7BC4;&#x4F8B;](../../.gitbook/assets/example-of-secant-min.png)

## 函數的極限

> 函數$$f: \mathbb{R} \rightarrow \mathbb{R}$$：$$\displaystyle \lim_{x \rightarrow c}⁡f(x)=L $$，	• 若從定義域左側、右側逼近得到的函數值與函數在該點的函數均相同時，稱函數在該點連續。
>
> 給定度量空間$$(X,d)$$，函數$$f: X \rightarrow \mathbb{R}$$為實值函數，點$$c \in X$$,$$L \in \mathbb{R}$$，則$$\displaystyle \lim_{x \rightarrow c} f(x)=L$$定義為：
>
> * $$\forall \epsilon > 0 ~ \exists \delta > 0 \ni |f(x) -L| < \epsilon, ~ \forall d(x, c) < \epsilon$$
> * 極限存在時，則$$x$$從任意方向逼近$$c$$時，其函數值也都會趨近於$$L$$。
> * 極限存在不代表連續，只有在$$f(c)=L$$時才為連續。
>
> • 更一般化的函數定義為給定度量空間$$(S, d_s ), (T,d_T )$$，函數$$f:S \rightarrow T$$，$$A \subseteq S$$，$$c \in A$$為極限點，$$L \in T$$，則$$\lim_{ x \rightarrow c} f(x) = L$$ 若且唯若 $$\forall \epsilon > 0 ~ \exists \delta > 0 \ni d_T(f(x), L) < \epsilon $$ whenever $$pc\neq x, x\in A, d_S(x,c) <\delta$$。
>
> 也可以用球來定義，$$f(x)\in B_{T}(L, \epsilon)$$ whenever $$x \in B_S(c, \delta) \cap A, ~ x \neq p$$

![&#x51FD;&#x6578;&#x6975;&#x9650;&#x7684;epsilon-delta&#x5B9A;&#x7FA9;](../../.gitbook/assets/epsilon-delta_definition-min.png)

![&#x5169;&#x500B;&#x5EA6;&#x91CF;&#x7A7A;&#x9593;&#x51FD;&#x6578;&#x6975;&#x9650;&#x7684;epsilon-delta&#x5B9A;&#x7FA9;](../../.gitbook/assets/metric-limit-epsilon-delta-min.png)





