---
description: moment：動差(tw)，矩(cn)
---

# 動差生成函數(moment generating function)

## 簡介

動差生成函數$$M_X(t)$$是隨機變數$$X$$動差的一種簿記機制，它將$$X$$的各階動差收集起來並以無窮級數的形式表示。動差生成函數不具備內在含義，它的主要用途在於簡化計算與證明。

動差生成函數本身並不是一個從某個定義域映射至某個值域的函數，取名「函數」僅是出於歷史原因。

* 隨機變數的動差生成函數(MGF)具唯一性，<mark style="color:red;">因此若兩個隨機變數的MGF相等時，則這兩個隨機變數具有相同的分佈函數</mark>。
* <mark style="color:red;">但是並非所有隨機變數均存在動差生成函數</mark>(如Cauchy distribution不存在動差生成函數)，此時可改用特徵函數(characteristic function, CHF)證明。
* <mark style="color:red;">隨機變數的特徵函數具唯一性，且必定存在。</mark>CHF可完全取代MGF，但通常MGF計算較為簡單，因此除非MGF不存在時，才會使用CHF證明。
* **隨機變數的動差生成函數可視為隨機變數做Laplace transform (不一定存在)，而特徵函數可視為隨機變數做Fourier transform (一定存在)**。

## 隨機變數的k次動差(k-th moment)



> 令隨機變數$$X$$的機率密度函數為$$f$$，則（以0為中心）$$k$$次動差為：
>
> * $$X$$為離散隨機變數，$$\displaystyle \operatorname{E}(X^k) = \sum_{i=1}^{\infty} x_i^k f(x_i)$$, $$x_i$$為可能的實現值。
> * $$X$$為連續隨機變數，$$\displaystyle \operatorname{E}(X^k) = \int_{-\infty}^{\infty} x^k f(x)dx = \int_{-\infty}^{\infty} x^k dF(x)$$
> * 如果$$X$$的觀察值(樣本)為$$x_1, x_2,\ldots, x_N$$，則$$k$$次動差為$$\displaystyle \operatorname{E}(X^k) = \frac{1}{N} \sum_{i=1}^N x_i^k$$。
>
> 以期望值為中心的$$k$$次動差為 $$\displaystyle   \operatorname{E}((X-\mu)^k)=\int_{-\infty}^{\infty}x^k dF(x)$$

* &#x20;一階動差為平均值(mean)，描述分佈的集中程度。
* 二階中央動差為變異數(variance)，描述分佈的分散程度。
* 三階中央動差為偏度(skewness)，描述分佈左、右偏移的程度。
* 四階中央動差為峰度(kurtosis)，述述分佈尖聳的程度。

```python
import numpy as np
from typing import Iterable

def kth_moment(values: Iterable):
      ys = np.asarray(values)
    mu = ys.mean()
    for k in range(1, 4+1):
        e_xs = (ys**k).mean()
        e_center_xs = ((ys - mu)**k).mean()
        print(f"{k}th moment: {e_xs:.4f}")
        print(f"{k}th center moment: {e_center_xs:.4f}")
        
if __name__ == '__main__':
    values = np.random.randn(100000)
    kth_moment(values)
    
""" 標準常態分佈均值為0, 二階中央動差為1, 三階中央動差為0, 四階中央動差為3
1th moment: 0.0034
1th center moment: 0.0000
2th moment: 1.0031
2th center moment: 1.0031
3th moment: 0.0014
3th center moment: -0.0089
4th moment: 3.0038
4th center moment: 3.0039
"""
```

*

## 動差生成函數(MGF)

> 動差生成函數 $$M(t) \equiv \operatorname{E}(e^{tX}) = \int_{-\infty}^{\infty} e^{tx}dF(x) \text{ or} \sum_{i=1}^n e^{t x_i}\mathrm{P}(x_i)$$，可視為隨機變數的（反）<mark style="color:red;">Laplace轉換</mark>。

* $$e^{tX}=1+tX+ \frac{t^2X^2}{2!}+ \dots + \frac{t^nX^n}{n!}+ \dots$$
* $$M_X(t)= \mathrm{E}(e^{tX}) = 1+t\mathrm{E}(X) + \frac{t^2\mathrm{E}(X^2)}{2!}+ \dots + \frac{t^n \mathrm{E}(X^n)}{n!} + \dots$$

> 隨機變數的MGF$$M(t)$$不一定存在，<mark style="color:red;">但存在時與分佈函數</mark>$$F(x)$$<mark style="color:red;">有一對一的關係</mark>。若$$M_X(t), M_Y(t)$$存在，則$$F_X=F_Y \Leftrightarrow M_X(t)=M_Y(t)$$。

> 特徵生成函數 $$\phi(t) \equiv \operatorname{E}(e^{itX}) = \int_{-\infty}^{\infty} e^{itx}dF(x) \text{ or} \sum_{i=1}^n e^{i t x_i} \mathrm{P}(x_i)$$，可視為隨機變數的（反）<mark style="color:red;">Fourier轉換</mark>。
>
> 隨機變數的CHF 一定存在，且與機率分佈$$F(x)$$有一對一的關係。即$$F_X = F_Y \Leftrightarrow\phi_X(t)=\phi_Y(t)$$。

**MGF與CHF主要用途，是證明兩個相異隨機變數有相同的機率分佈**。

由泰勒展開式可知：

* $$\operatorname{E}(X^k) = \frac{d^k}{dt^k}M_X(t)|_{t=0}$$
* $$\operatorname{E}(X^k) = i^{-k} \frac{d^k}{dt^k}\phi_X(t)|_{t=0}$$

### 特徵函數的應用：反傅立葉變換求機率分佈

> 如果隨機變數$$X$$的機率分佈無法直接求出，可先求出其特徵函數$$\phi_X(t)$$後，再以Fourier轉換求出其機率分佈。
>
> $$\displaystyle f(x) = \frac{1}{2} \pi \int_{-\infty}^{\infty} e^{-itx} \phi_X(t)dt$$

有時無法根據上式求出$$f(x)$$的公式解，而必須依賴數值方法求$$f(x)$$，如亞洲式選擇權中，標的物的平均值機率分佈無法直接得到，必須先算平均股價的特徵函數後，再以上式反推平均價的機率分佈。

