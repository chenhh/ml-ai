---
description: conditional expectation
---

# 條件期望值

## 簡介

* 隨機變數$$X$$的期望值$$\mathrm{E}(X)$$為常數值。
* 隨機變數$$X$$相對於隨機變數$$Y$$的特定實現值$$Y=y$$的期望值$$\mathrm{E}(X|Y=y)$$為常數值。
* 隨機變數$$X$$相對於隨機變數$$Y$$的期望值$$\mathrm{E}(X|Y)$$$$=f(Y)$$為隨機變數。
* 隨機變數$$X$$相對於事件集合$$E$$的期望值$$\mathrm{E}(X|E)$$為隨機變數。
* 隨機變數$$X$$相對於σ域$$\sigma(E)$$的期望值$$\mathrm{E}(X|\sigma(E))$$為隨機變數。

<mark style="color:red;">在最一般化的情況下，條件期望值是相對特定的σ域(且</mark>$$X$$<mark style="color:red;">不需為</mark>$$\mathcal{F}$$<mark style="color:red;">可測)的隨機變數</mark>。

* 隨機變數$$X$$的期望值，可視為隨機變數相對於宇集合$$\Omega$$生成的σ域$$\sigma(\Omega)=\{\emptyset, \Omega\}$$的隨機變數。
* 相對於對事件集合$$E$$的條件期望值，可視為相對於生成該事件的σ域$$\sigma(E)=\{\emptyset, E, E^c, \Omega\}$$的隨機變數。
* 而相對於隨機變數$$Y$$的條件期望值，可視為相對於生成該隨機變數的σ域$$\sigma(Y)$$的隨機變數。
* 而相對於隨機變數$$Y$$的特定實現值$$y$$的條件期望值，為退化的$$\sigma(Y)$$的隨機變數，為常數值。

離散隨機變數的條件期望值$$\mathrm{E}(X~|~Y)$$實際上就是把先把$$Y$$限制在某些值（比如2,1,7）上，求得對應的事件件（比如{a, b},{c, d}或{e, f}）（也就是可測函數的前像），然後找到$$X$$中對應的事件求均值，各個集合

## 條件期望值

條件期望值有三種形式：

1. $$\mathrm{E}(c|Y)$$​為一實數值。
2. $$\mathrm{E}(X|Y=y)$$​為一實數值。
3. $$\mathrm{E}(X|Y)$$為一依賴於$$Y$$​的隨機變數。

> * $$\displaystyle \mathrm{E}(Y|X=k)=\sum_{h} h \cdot\mathrm{P}(Y=h|X=k)$$，在事件$$X=k$$下，$$Y$$的條件期望值。
> * $$\displaystyle \mathrm{E}(Y|X=k)=\int_{-\infty}^{\infty}y\cdot f_{Y|X}(y|k)dy$$
> * $$\mathrm{P}(Y=h|X=k) = \frac{\mathrm{P}(Y=h \cap X=k)}{\mathrm{P}(X=k)}$$

* 條件期望值$$\mathrm{E}(Y|X=k)$$在$$X=k$$給定後，其值已經決定了，因此為$$k$$的函數，即$$\mathrm{E}(Y|X=k) = f(k)$$。如果$$X$$之值未定時，則$$\mathrm{E}(Y|X) = g(X)$$。

### 條件期望值為最佳預測值

> $$\displaystyle \mathrm{E}(Y|X) = \arg \min_{g(X)} \mathrm{E}(Y-g(X))^2$$，即$$\mathrm{E}(Y|X)$$為對於$$Y$$的最佳預測值。
>
> 註：也可用內積空間的[最小平方解](../../linear-algebra/inner-product-space/least-square-solution.md)得出。[https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/01\_law\_of\_iterated\_expectations.svg/1024px-01\_law\_of\_iterated\_expectations.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/01\_law\_of\_iterated\_expectations.svg/1024px-01\_law\_of\_iterated\_expectations.svg.png)

<details>

<summary>proof: 離散隨機變數</summary>

$$\displaystyle  \begin{aligned}  \mathrm{E}[(g(X)-Y)^2] & = \mathrm{E}[(g(X)- \mathrm{E}(Y|X) + \mathrm{E}(Y|X) - Y)^2] \\         & = E[(g(X) - \mathrm{E}(Y|X)^2)] \\         & + 2 \mathrm{E}[(g(X) - \mathrm{E}(Y|X))(\mathrm{E}(Y|X)- Y)] \\         & + \mathrm{E}[(\mathrm{E}(Y|X)-Y)^2] \end{aligned}$$

其中第二項展開後得：$$\displaystyle  \begin{aligned} \mathrm{E}[(g(X) - \mathrm{E}(Y|X))(\mathrm{E}(Y|X)- Y)] &= \mathrm{E}[g(X) \mathrm{E}(Y|X) ] \\     & -\mathrm{E}[\mathrm{E}(Y|X) \mathrm{E}(Y|X)] \\     & - \mathrm{E}[g(X)Y] \\     & + \mathrm{E}[Y \mathrm{E}(Y|X)] \\     & = \mathrm{E}[g(X)Y] - \mathrm{E}[Y\mathrm{E}(Y|X)] - \mathrm{E}[g(X)Y] + \mathrm{E}[Y\mathrm{E}(Y|X)] \\     & = 0 \end{aligned}$$而第三項與$$g(X)$$無關。

因此第一項為0時，可得$$\mathrm{E}[(Y-g(X))^2]$$有最小值，即$$g(X) = \mathrm{E}(Y|X)$$ (QED)

</details>

### 重複期望值定理(law of iterated expectation, Law of total expectation)

> &#x20;$$\mathrm{E}(\mathrm{E}(X|Y))=\mathrm{E}(X)$$
>
> 簡單地說，$$X$$的平均值等於條件平均值的加權平均值。

<details>

<summary>proof: 離散隨機變數</summary>

$$\displaystyle {\begin{aligned} \mathrm {E}\left(\mathrm {E}(X|Y)\right)&{}=\sum \limits _{y}\mathrm {E}(X|Y=y)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\left(\sum \limits _{x}x\cdot \mathrm {P}(X=x|Y=y)\right)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\sum \limits _{x}x\cdot \mathrm {P}(X=x|Y=y)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\sum \limits _{x}x\cdot \mathrm {P}(Y=y|X=x)\cdot \mathrm {P}(X=x)\\&{}=\sum \limits _{x}\sum \limits _{y}x\cdot \mathrm {P}(Y=y|X=x)\cdot \mathrm {P}(X=x)\\&{}=\sum \limits _{x}x\cdot \mathrm {P}(X=x)\cdot \left(\sum \limits _{y}\mathrm {P}(Y=y|X=x)\right)\\&{}=\sum \limits _{x}x\cdot \mathrm {P}(X=x)\\&{}=\mathrm {E}(X).\end{aligned}}$$

</details>

<details>

<summary>proof: 連續隨機變數</summary>

$${\displaystyle {\begin{aligned}\mathrm {E} (X)&=\int x\Pr[X=x]~dx\\\mathrm {E} (X\mid Y=y)&=\int x\Pr[X=x\mid Y=y]~dx\\\mathrm {E} (\mathrm {E} (X\mid Y))&=\int \left(\int x\Pr[X=x\mid Y=y]~dx\right)\Pr[Y=y]~dy\\&=\int \int x\Pr[X=x,Y=y]~dx~dy\\&=\int x\left(\int \Pr[X=x,Y=y]~dy\right)~dx\\&=\int x\Pr[X=x]~dx\\&=\mathrm {E} (X)\,.\end{aligned}}}$$

</details>



## 參考資料

* [https://stats.stackexchange.com/questions/230545/intuition-for-conditional-expectation-of-sigma-algebra](https://stats.stackexchange.com/questions/230545/intuition-for-conditional-expectation-of-sigma-algebra)
* [https://stats.stackexchange.com/questions/495562/how-to-understand-conditional-expectation-w-r-t-sigma-algebra-is-the-conditiona](https://stats.stackexchange.com/questions/495562/how-to-understand-conditional-expectation-w-r-t-sigma-algebra-is-the-conditiona)
