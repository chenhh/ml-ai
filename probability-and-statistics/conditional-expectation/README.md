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

在最一般的情況下，條件期望值是相對特定的σ域的隨機變數。

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
> * $$\displaystyle \mathrm{E}(Y|X=k)=\int_{-\infty}^{\infty}y\cdot f_{Y|X}(y|x)dy$$
> * $$\mathrm{P}(Y=h|X=k) = \frac{\mathrm{P}(Y=h \cap X=k)}{\mathrm{P}(X=k)}$$

* 條件期望值$$\mathrm{E}(Y|X=k)$$在$$X=k$$給定後，其值已經決定了，因此為$$k$$的函數，即$$\mathrm{E}(Y|X=k) = f(k)$$。如果$$X$$之值未定時，則$$\mathrm{E}(Y|X) = g(X)$$。

## 參考資料

* [https://stats.stackexchange.com/questions/230545/intuition-for-conditional-expectation-of-sigma-algebra](https://stats.stackexchange.com/questions/230545/intuition-for-conditional-expectation-of-sigma-algebra)
* [https://stats.stackexchange.com/questions/495562/how-to-understand-conditional-expectation-w-r-t-sigma-algebra-is-the-conditiona](https://stats.stackexchange.com/questions/495562/how-to-understand-conditional-expectation-w-r-t-sigma-algebra-is-the-conditiona)
