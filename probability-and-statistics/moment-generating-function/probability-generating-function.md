---
description: probability generating function
---

# 機率生成函數(probability generating function)

## 簡介

機率生成函式是機率論中用來描述離散隨機變數（特別是**非負整數值隨機變數**）分佈的一個重要工具。它通過將隨機變數的機率質量函數編碼成生成函式的形式，提供了一種方便的方法來分析分佈的性質、計算動差以及研究隨機變數的和。

與動差生成函式和累積量生成函式相比，PGF 更專注於離散分佈的特性，在機率論和應用數學中有廣泛用途。

## 機率生成函數定義

> 對於一個取非負整數值（$$X=0,1,2,\dots$$）的離散隨機變數$$X$$，其機率生成函數\
> $$G_X(s)$$定義為：
>
> $$G_X(s)=\mathrm{E}(s^X)=\sum_{k=0}^\infty \mathrm{P}(X=k)s^k$$。
>
> 其中$$s \in \mathbb{R}$$或$$s \in \mathbb{C}$$，通常考慮$$|s| \leq 1$$以保證級數收斂。

當$$s=1$$，$$G_X(1)= \sum_{k=1}^\infty \mathrm{P}(X=k)=1$$符合機率測度的定義。

$$\mathrm{P}(X=k)$$可通過對$$G_X(s)$$的$$k$$次微分且取$$s=0$$時得出，即$$\mathrm{P}(X=k)= \frac{1}{k!} \frac{d^k}{ds^k} G_X(s)|_{s=0}$$ 。

* $$\mathrm{P}(X=0)=G_X(0)$$。
* $$\mathrm{P}(X=1)=G_X^{(1)}(0)$$。
* $$\mathrm{P}(X=2)=\frac{1}{2!}G_X^{(2)}(0)$$。

### 動差計算

* 均值：$$\mathrm{E}(X) = G_X^{'}(1)$$。
* 二階動差：$$\mathrm{E}(X(X-1))=G_X^{(2)}(1)$$。
* 變異數：$$\mathrm{Var}(X)=G_X^{(2)}(1) + G_X^{(1)}(1) - (G_X^{(1)}(1))^2$$。

## 獨立隨機變數的和

> 若$$X,Y$$是獨立的非負整數值隨機變數，則它們的和的機率生成函數滿足$$G_{X+Y}(s)=G_X(s) G_Y(s)$$。

因為在獨立時，$$\mathrm{E}(s^{X+Y}) = \mathrm{E}(s^X) \mathrm{E}(s^{Y})$$

## 與其它生成函數的關係

與動差生成函式的關係：$$M_X(t)=\mathrm{E}(e^{tX})=G_X(e^t)$$，即$$s=e^t$$代入PGF可得MGF。因此，PGF 是 MGF 在離散整數情況下的一種特殊形式。

與累積量生成函式的關係：$$K_X(t) = \log M_X(t) = \log G_x(e^t)$$。
