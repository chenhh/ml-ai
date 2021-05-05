---
description: moment：動差(tw)，矩(cn)
---

# 動差生成函數\(moment generating function\)

## 簡介

* 隨機變數的動差生成函數\(MGF\)具唯一性，因此若兩個隨機變數的MGF相等時，則這兩個隨機變數具有相同的機率分佈。
* 但是並非所有隨機變數均存在動差生成函數\(如Cauchy distribution不存在動差生成函數\)，此時可改用特徵函數\(characteristic function, CHF\)證明。
* 隨機變數的特徵函數具唯一性，且必定存在。CHF可完全取代MGF，但通常MGF計算較為簡單，因此除非MGF不存在時，才會使用CHF證明。
* **隨機變數的動差生成函數可視為隨機變數做Laplace transform \(不一定存在\)，而特徵函數可視為隨機變數做Fourier transform \(一定存在\)**。

## 隨機變數的k次動差\(k-th moment\)



> 令隨機變數$$X$$的機率密度函數為$$f$$，則$$k$$次動差為：
>
> * $$X$$為離散隨機變數，$$\operatorname{E}(X^k) = \sum_{i=1}^{\infty} x_i^k f(x_i)$$, $$x_i$$為可能的實現值。
> * $$X$$為連續隨機變數，$$\operatorname{E}(X^k) = \int_{-\infty}^{\infty} x^k f(x)dx$$
> * 如果$$X$$的觀察值\(樣本\)為$$x_1, x_2,\ldots, x_N$$，則$$k$$次動差為$$\operatorname{E}(X^k) = \frac{1}{N} \sum_{i=1}^N x_i^k$$。

*  一階動差為平均值\(mean\)，描述分佈的集中程度。
* 二階中央動差為變異數\(variance\)，描述分佈的分散程度。
* 三階中央動差為偏度\(skewness\)，描述分佈左、右偏移的程度。
* 四階中央動差為峰度\(kurtosis\)，述述分佈尖聳的程度。









