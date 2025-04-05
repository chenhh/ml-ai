---
description: cumulant generating function
---

# 累積量生成函數(cumulant generating function)

## 簡介

累積量生成函數與動差生成函數（Moment-Generating Function, MGF）密切相關，但提供了一種不同的視角，特別是在分析隨機變數的獨立性和加和性質時非常有用。

<mark style="color:red;">累積量實際上是動差的某種「重新組織」，特別適合描述獨立隨機變數的加和性質，而動差則更直接反映分佈的原始統計特性</mark>。

* **獨立性分析：**&#x7D2F;積量的加性質使其在研究獨立隨機變數的和（如中心極限定理）時非常有用。
* **分佈識別：**&#x901A;過檢查累積量的模式，可以推斷隨機變數的分佈。例如，若 $$\kappa_3 = \kappa_4 = \cdots = 0$$則分佈可能是正態的。
* **高階統計：**&#x7D2F;積量提供了比動差更直接的方式來描述分佈的非正態性（如偏度和峰度）。

## 累積量生成函數

> 隨機變數$$X$$的累積量生成函數$$K_X(t)$$定義為動差生成函數$$M_X(t)$$的自然對數：
>
> $$K_X(t) = \log M_X(t) = \log \mathrm{E}(e^{tX})$$。
>
> 因此$$M_X(t)$$必須存在才可定義$$K_X(t)$$。
>
> $$t \in \mathbb{R}$$且且假設$$M_X(t)$$在$$t=0$$附近某個開區間內存在且有限。

$$M_X(t)=\mathrm{E}(e^{tX})=1+t\mathrm{E}(X) + \frac{t^2}{2!}\mathrm{E}(X^2) + \dots + \frac{t^n}{n!}\mathrm{E}(X^n) + \dots$$

## 累積量（Cumulants）

> 累積量是從$$K_X(t)$$ 的 Taylor 展開式中提取的係數。具體來說，若$$K_X(t)$$ 在$$t=0$$附近展開：$$K_X(t)=\log \mathrm{E}(e^{tX}) = k_1t + \frac{k_2}{2!}t^2 + \dots + \frac{k_n}{n!}t^n + \dots$$
>
> 其中$$k_n$$是第$$n$$階累積量。

#### 方法1：將動差生成函數展開再取對數

令$$u(t) = t\mathrm{E}(X) + \frac{t^2}{2!}\mathrm{E}(X^2) + \dots + \frac{t^n}{n!}\mathrm{E}(X^n) + \dots$$

$$\log \mathrm{E}(e^{tX}) = \log [1+t\mathrm{E}(X) + \frac{t^2}{2!}\mathrm{E}(X^2) + \dots + \frac{t^n}{n!}\mathrm{E}(X^n) + \dots] = \log (1+u(t))$$

而Taylor展開式：$$\log(1+x)=x - \frac{x^2}{2} + \frac{x^3}{3} -  \frac{x^4}{4} + \dots$$，當$$|x|<1$$。

但$$u(t)$$為$$t$$的函數且$$u(0)=0$$，因此要計算$$u(t)$$的展開式並代入上式(不好算)。

#### 方法2：通過微分來建立關係

$$K_X(t) = \log M_X(t)$$

對$$t$$ 一次微分得：  $$K^{'}_X(t) = \frac{M^{'}_X(t)}{M_X(t)}$$。

其中：$$M_X^{'}(t) =\frac{d}{dt}\mathrm{E}(e^{tX})= \mathrm{E}(Xe^{tX})$$。

在$$t=0$$時，$$M_X^{'}(0)=\mathrm{E}(X), ~M_X(0)=1$$，所以$$K_X^{'}(0)=\frac{M_X^{'}(0)}{M_X(0)}=\mathrm{E}(X)=\kappa_1$$。

對$$t$$二次微分得$$K^{(2)}_X(t) = \frac{dt}{dt} \left( \frac{M^{'}_X(t)}{M_X(t)}\right) = \frac{M_X^{(2)}(t)M_X(t) - (M_X^{'}(t))^2}{(M_X(t))^2}$$

在$$t=0$$時，$$M_X^{(2)}(t)=\mathrm{E}(X^2 e^{tX})$$，可得$$M_X^{(2)}(0)= \mathrm{E}(X^2)$$。且$$M_X^{'}(0)=1$$。

所以$$K_X^{(2)}(0)=\frac{\mathrm{E}(X^2)  - (\mathrm{E}(X))^2}{1}=\mathrm{Var}(X)=\kappa_2$$。

<mark style="color:red;">這些公式表明，累積量是動差的非線性組合，反之亦然</mark>。

其中$$n$$階累積量可以通過對​$$K_X(t)$$做$$n$$次微分後，取$$t=0$$得出：

$$k_1 = K^{(1)}_X(0)$$

$$k_2 = K_X^{(2)}(0)$$

$$k_n = \frac{d^n}{dt^n}K_X(t)|_{t=0}$$

## 累積量與動差的關係

累積量和動差（Moments）之間存在聯繫，但它們描述的性質不同：

* 一階累積量：$$k_1 = \mathrm{E}(X)$$，等於均值。
* 二階累積量：$$k_2 = \mathrm{Var}(X) = \mathrm{E}(X^2) - (\mathrm{E}(X))^2$$，等於變異數。
* 三階累積量：$$k_3 = \mathrm{E}((X-\mathrm{E}(X))^3)$$ ，與偏度相關。
* 四階累積量：$$k_4 = \mathrm{E}((X-\mathrm{E}(X))^4)$$，與峰度相關。

與動差不同，累積量在處理獨立隨機變數的和時具有簡單的加性質，這是它的一大優勢。

反過來，動差也可以用累積量，即$$M_X(t) = \exp (K_X(t))$$。

* $$\mathrm{E}(X) = \kappa_1$$。
* $$\mathrm{E}(X^2) = \kappa_2 + \kappa_1^2$$。
* $$\mathrm{E}(X^3) = \kappa_3 + 3\kappa_1 \kappa_2 + \kappa_1^3$$。
* $$\mathrm{E}(X^4) = \kappa_4 + 4 \kappa_1 \kappa_3 + 3 \kappa_2^2 + 6 \kappa_1^2 \kappa_2 + \kappa_1^4$$。

## 獨立隨機變數的累積量生成函數

> 如果$$X,Y$$是獨立的隨機變數，則它們的和$$X+Y$$的累積量生成函數：$$K_{X+Y}(t)=K_X(t) + K_Y(t)$$。

因為$$X,Y$$是獨立的隨機變數時，動差生成函數$$M_{X+Y}(t) = M_X(t)M_Y(t)$$，取對數得$$\log M_{X+Y}(t) = \log M_X(t) + \log M_Y(t)$$。

## 標準化

> 如果隨機變數$$X$$標準化為$$Z=\frac{X-\mu}{\sigma}, ~ \mu=\mathrm{E}(X), \sigma^2 = \mathrm{Var}(X)$$，則$$k_1 =0, k_2 = 1$$。
>
> 高階累積量則成為無量綱的量，用於描述分佈的形狀。

例如常數分佈$$X \sim N(\mu, \sigma^2)$$, $$K_X(t) = \mu t + \frac{\sigma^2 t^2}{2}$$，因此$$k_1 =\mu, k_2 = \sigma^2$$，所有高階累積量均為0，這是正態分佈的一個獨特特徵。
