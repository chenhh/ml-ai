# 測度\(measure\)

## 簡介

* 在此討論的是測度應具有的性質，只要符合測度定義的函數均可視為測度。
* 測度是將集合至正實數的函數。

## 測度\(measure\)

> 給定集合$$X$$，$$Σ$$為定義在$$X$$上的sigma-field。
>
> * 定義函數$$μ: \Sigma \rightarrow [0, \infty]$$ \(可為無窮大\)滿足以下兩個條件：
>   *  \[空集合的測度為0\] $$\mu(\emptyset)=0$$
>   *  \[countable additive, 互斥集合聯集的測度等於各別集合測度的加總\] $$\displaystyle \mu(\cup_{n=1}^{\infty}E_n) =\sum_{n=1}^{\infty}\mu (E_n), ~ E_n \in \Sigma $$且$$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$

* 註：測度之值在此定義為正實數，但之後可放寬為任意實數\(如負值\)或複數。
* **註: 只要再加上第三個條件**$$\displaystyle \sum_{n=1}^\infty \mu( E_n) =1$$**的條件時，則為機率測度**。

>





