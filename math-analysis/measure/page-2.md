---
description: signed measure
---

# 有號測度

一般討論測度$$u: \Sigma \rightarrow [0, \infty]$$要求其值域為非負值，而有號測度討論的是值域可為負值的情形。

## 有號測度定義

> $$\mu: \Sigma \rightarrow [-\infty, \infty]$$可取值$$\pm\infty$$且滿足：
>
> 1. 定義域$$\Sigma$$為sigma域
> 2. $$\mu(\empty)=0$$
> 3. $$\displaystyle \mu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty E_n$$，$$E_i \cap E_j = \empty$$且$$\bigcup_{n=1}^\infty E_n \in \Sigma$$
>
> 時，稱$$\mu$$為有號測度。

定義有號測度的目的是考慮兩個測度的差值時，如$$\mu(E)=\mu_1(E) - \mu_2(E), ~ E \in \Sigma$$，其中$$\mu_1, \mu_2$$至少一個為有限測度，且定義在同一個sigma域$$\Sigma$$。
