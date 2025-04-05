---
description: moment：動差(tw)，矩(cn)
---

# 動差生成函數(moment generating function)

## 簡介

動差生成函數$$M_X(t)=\mathrm{E}(e^{tX}), ~ t \in \mathbb{R}$$是隨機變數$$X$$動差的一種簿記機制，它將$$X$$的各階動差收集起來並以無窮級數的形式表示。動差生成函數不具備內在含義，它的主要用途在於簡化計算與證明。但是隨機變數的動差生成函數不一定存在，因此某些分佈(如Cauchy分佈)的低階動差不存在，因此有特徵生成函數的存在，但是動差生成函數計算簡單，一般情形下仍使用之。

動差生成函數本身並不是一個從某個定義域映射至某個值域的函數，取名「函數」僅是出於歷史原因。

* 隨機變數的動差生成函數(MGF)具唯一性，<mark style="color:red;">因此若兩個隨機變數的MGF相等時，則這兩個隨機變數具有相同的分佈函數</mark>。
* <mark style="color:red;">但是並非所有隨機變數均存在動差生成函數</mark>(如Cauchy distribution不存在動差生成函數)，此時可改用特徵函數(characteristic function, CHF)證明。
* <mark style="color:red;">隨機變數的特徵函數具唯一性，且必定存在。</mark>CHF可完全取代MGF，但通常MGF計算較為簡單，因此除非MGF不存在時，才會使用CHF證明。
* **隨機變數的動差生成函數可視為隨機變數做Laplace transform (不一定存在)，而特徵函數可視為隨機變數做Fourier transform (一定存在)**。

**核心用途**：

1. 計算各階動差（均值、變異數等）。
2. 推導獨立隨機變數之和的分佈。
3. 證明極限定理。

* **優點**：唯一性、代數運算方便。
* **缺點**：可能不存在，需檢查收斂性。

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

以此類推，高階動差提供了關於分佈更細緻的形狀資訊。直觀上，如果兩個分佈的所有動差都相同，那麼它們在中心位置、散佈程度、對稱性、尾部行為等方面都應該一致。

<mark style="color:red;">在極端情況下，可能存在兩個不同分佈但具有相同動差序列。然而，這種情況通常發生在動差生成函數不存在或動差增長過快時。只要動差生成函數在</mark>$$t=0$$<mark style="color:red;">附近某區間內存在，這種反例就不會出現</mark>。

## 範例：常態分佈的動差

<details>

<summary>python code</summary>

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

</details>

## 動差生成函數(MGF)

> 動差生成函數 $$M(t) \equiv \operatorname{E}(e^{tX}) = \int_{-\infty}^{\infty} e^{tx}dF(x) \text{ or} \sum_{i=1}^n e^{t x_i}\mathrm{P}(x_i)$$，可視為隨機變數的（反）<mark style="color:red;">Laplace轉換</mark>。
>
> 動差生成函式只有在$$t$$的某個鄰域內（通常包括$$t=0$$）收斂時才存在。
>
> 注意此處的$$X$$是隨機變數(可測函數)。因為$$e^{tx}$$在$$x \in \mathbb{R}$$均有定義，而$$\forall \omega \in \Omega, X(\omega) \in \mathbb{R}$$，因此$$e^{tX}$$可視為從單點的$$x$$轉換成函數$$X$$，仍然成立。

$$e^{tX}=1+tX+ \frac{t^2X^2}{2!}+ \dots + \frac{t^nX^n}{n!}+ \dots$$

$$M_X(t)= \mathrm{E}(e^{tX}) = 1+t\mathrm{E}(X) + \frac{t^2\mathrm{E}(X^2)}{2!}+ \dots + \frac{t^n \mathrm{E}(X^n)}{n!} + \dots$$

## 性質

* \[標準化] ：$$M_X(0)=1$$，因為$$e^{0X}=1$$。
* \[線性變換]：若$$Y=aX+b$$，則$$Y$$的動差生成函數為$$M_Y(t)=e^{bt}M_X(at)$$。

$$\because \mathrm{E}(e^{tY})=\mathrm{E}(e^{t(aX+b)})=e^{tb}\mathrm{E}(e^{taX})=e^{tb}M_X(at)$$。



### 動差生成函數的唯一性

> 若兩個隨機變數的動差生成函數存在且相同，若且唯若它們具有相同的機率分佈。
>
> 隨機變數的MGF$$M(t)$$不一定存在，<mark style="color:red;">但存在時與分佈函數</mark>$$F(x)$$<mark style="color:red;">有一對一的關係</mark>。若$$M_X(t), M_Y(t)$$存在，則$$F_X=F_Y \Leftrightarrow M_X(t)=M_Y(t)$$。
>
> **此性質的主要用途是證明兩個相異隨機變數有相同的機率分佈**。
>
> 註：有些分佈動差存在但可能MGF不存在(或者$$t$$只在某些實數集成立)，如[log-normal分佈](https://en.wikipedia.org/wiki/Log-normal_distribution)。

> 特徵生成函數 $$\phi(t) \equiv \operatorname{E}(e^{itX}) = \int_{-\infty}^{\infty} e^{itx}dF(x) \text{ or} \sum_{i=1}^n e^{i t x_i} \mathrm{P}(x_i)$$，可視為隨機變數的傅立葉轉換。
>
> 隨機變數的CHF 一定存在，且與機率分佈$$F(x)$$有一對一的關係。即$$F_X = F_Y \Leftrightarrow\phi_X(t)=\phi_Y(t)$$。

<details>

<summary>proof: ⇒ 當兩隨機變數的機率分佈相同時，可得全部動差均相同，因此MGF相同。<br>&#x3C;= MGF相同可得兩變數全部動差相同，得機率分佈相同。</summary>

⇒ 給定兩隨機變數$$X,Y$$有相同的(累積)機率分佈$$F_X(x)= F_Y(x), \forall x$$。

因為$$M_X(t)=\int_{-\infty}^\infty e^{tx}f_X(x)dx$$，$$M_Y(t)=\int_{-\infty}^\infty e^{tx}f_Y(x)dx$$，因為$$f_X(x)=f_Y(x)$$可得$$M_X(t)=M_Y(t)$$。

也可以說因為$$F_X(x)= F_Y(x), \forall x$$，所以$$\mathrm{E}(X^k)=\mathrm{E}(Y^k), \forall k \in \mathbb{N}$$，因此$$M_X(t)=M_Y(t)$$。

因此，若$$𝑋, Y$$的分佈相同，則它們的動差生成函數必然相等。



(QED)

<=給定$$M_X(t)=M_Y(t)$$在某個$$t=0$$的開區間成立

動差生成函數的 Taylor 展開式（在$$t=0$$ 附近）給出了隨機變數的所有動差$$M_X(t)=\mathrm{E}(e^{tX})=1+t\mathrm{E}(X)+\frac{t^2}{2!}\mathrm{E}(X^2)+\frac{t^3}{3!}\mathrm{E}(X^3)+\dots$$。

$$M_Y(t)=\mathrm{E}(e^{tY})=1+t\mathrm{E}(Y)+\frac{t^2}{2!}\mathrm{E}(Y^2)+\frac{t^3}{3!}\mathrm{E}(Y^3)+\dots$$

因為$$M_X(t)=M_Y(t)$$在$$t \in (-h,h)$$成立，因此兩函數的Taylot級數相同，因此所有動差相同$$\mathrm{E}(X^k)=\mathrm{E}(Y^k), \forall k \in \mathbb{N}$$。

如果一個隨機變數的所有動差存在且唯一決定其分佈（即動差問題的解是唯一的），則$$X,Y$$的分佈必須相同。(QED)

</details>

## 由動差生成函數求動差值

由j指數的泰勒展開式可知：

$$M_X(t)= \mathrm{E}(e^{tX}) = 1+t\mathrm{E}(X) + \frac{t^2\mathrm{E}(X^2)}{2!} + + \frac{t^3\mathrm{E}(X^3)}{3!}+ \dots + \frac{t^n \mathrm{E}(X^n)}{n!} + \dots$$

對$$t$$一次微分得$$\frac{dM_X(t)}{dt}=\mathrm{E}(X) + t\mathrm{E}(X^2) + \frac{t^2}{2!}\mathrm{E}(X^3)  +\dots + \frac{t^{n-1}}{(n-1)!}\mathrm{E}(X^n) + \dots$$

對$$t$$二次微分得$$\frac{d^2M_X(t)}{dt^2}=\mathrm{E}(X^2)+ t \mathrm{E}(X^3) +\dots + \frac{t^{n-2}}{(n-2)!}\mathrm{E}(X^n) + \dots$$

因此取$$k$$階動差只要先將MGF微分$$k$$次後，再將$$t=0$$代入即可求值。

$$\operatorname{E}(X^k) = \frac{d^k}{dt^k}M_X(t)|_{t=0}$$

$$\operatorname{E}(X^k) = i^{-k} \frac{d^k}{dt^k}\phi_X(t)|_{t=0}$$



## 獨立隨機變數之和的動差生成函數

> 若隨機變數$$X, Y$$獨立，且動差生成函數$$M_X(t), M_Y(t)$$存在，則$$M_{X+Y}(t)=M_X(t) M_Y(t)$$。
>
> 這一性質在推導多個獨立隨機變數之和的分佈時非常有用。
>
> 推廣到$$n$$個獨立變數$$X_1, \dots, X_n$$時，則和$$S=\sum_{i=1}^n X_i$$的動差生成函數為$$M_S(t)=\prod_{i=1}^n M_{X_i}(t)$$。

### 特徵函數的應用：傅立葉變換求機率分佈

> 如果隨機變數$$X$$的機率分佈無法直接求出，可先求出其特徵函數$$\phi_X(t)$$後，再以Fourier轉換求出其機率分佈。
>
> $$\displaystyle f(x) = \frac{1}{2} \pi \int_{-\infty}^{\infty} e^{-itx} \phi_X(t)dt$$

有時無法根據上式求出$$f(x)$$的公式解，而必須依賴數值方法求$$f(x)$$，如亞洲式選擇權中，標的物的平均值機率分佈無法直接得到，必須先算平均股價的特徵函數後，再以上式反推平均價的機率分佈。

## 樣本平均值的動差生成函數

> 令$$X_1,\dots, X_n$$為獨立同分佈的$$n$$​個樣本，令樣本均值為$$\overline{X}_n=\frac{1}{n}\sum{i=1}^n X_i$$。
>
> 可得均值的動差生成函數$$\begin{aligned} M_{\overline{X}_n}(t) & =\mathrm{E}(e^{t\overline{X}_n}) \\ 	& = \mathrm{E}(e^{t \frac{1}{n}(X_1 + X_2+ \dots + X_n)}) \\ 	& = (\mathrm{E}(e^{\frac{t}{n}X}))^n \\ 	& = (M_X(\frac{t}{n}))^n  \end{aligned}$$

### 範例：常態分佈樣本均值的動差生成函數

若$$X_1,\dots, X_n \sim N(\mu, \sigma^2)$$獨立同分佈，可得

* $$M_{\overline{X}_n}(t) = e^{\mu t + \frac{\frac{\sigma^2}{n}t^2}{2}}$$，即$$\overline{X}_n \sim N(\mu, \frac{\sigma^2}{n})$$。

即樣本平均仍為常態分佈，期望值不變，而變異數隨樣本數$$n$$​增多而變小。

### 範例：gamma分佈樣本均值的動差生成函數

若$$X_1,\dots, X_n \sim \Gamma(\alpha, \beta)$$獨立同分佈，則：

* $$M_{\overline{X}_n}(t) = \left(\frac{1}{(1-\frac{\beta t}{n})^\alpha} \right)^n  = \frac{1}{(1-\frac{\beta}{n}t)^{n\alpha}}$$，即$$\overline{X}_n \sim  \Gamma(n\alpha, \frac{\beta}{n})$$
