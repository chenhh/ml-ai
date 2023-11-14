---
description: complex measure
---

# 複測度

## 簡介



## 複測度(complex measure)

> 給定可測空間$$(X, \Sigma)$$，複測度$$\mu: \Sigma \rightarrow \mathbb{C}$$滿足：
>
> * $$\mu(\emptyset)=0$$。
> * $$E \in \Sigma, ~ E=\bigcup_{n=1}^\infty E_n, E_i \cap E_j =\emptyset, \forall i \neq j$$則，$$\displaystyle \mu(E)=\sum_{n=1}^\infty \mu(E_n) \in \mathbb{C}$$。(因為不為無窮大，且對於$$E_n$$的任意排列均收斂，因此級數為絕對收斂)。

由定義可知$$\mu$$的值域為複數，因此不包含$$\infty$$<mark style="color:red;">。即</mark>$$\mu$$<mark style="color:red;">的值域必然是包含在複平面上某個半徑有限的圓盤內 (disc of finite radius) - 這一性質也被稱為有界變差 ( bounded variation)</mark>。許多定理可以直接從符號測度推廣到複測度上，且定理的條件自動滿足。

複數的等號必需是實部與虛部均相等，而複測度$$\mu$$可寫成實數與虛部兩個符號測度，$$\mu=\mu_r+i\mu_i$$，其中$$\mu_r, \mu_i$$為符號測度。

可定義複測度的積分：$$\displaystyle \int_E f d\mu = \int_E f d\mu_r i \int_E f d\mu_i$$。





## 參考資料

* [https://en.wikipedia.org/wiki/Complex\_measure](https://en.wikipedia.org/wiki/Complex\_measure)
* [https://zhuanlan.zhihu.com/p/71775089](https://zhuanlan.zhihu.com/p/71775089)
