# 特徵函數(characteristic function)

## 簡介

<mark style="color:red;">任何隨機變數的特徵函數(c.f.)必定存在且唯一</mark>。

$$\psi_X(t)=\mathrm{E}(e^{itX}), ~ t \in \mathbb{R}$$

* $$\displaystyle \mathrm{E}(e^{itX})=\int_{-\infty}^\infty e^{itx} dF_X(x)$$，$$F_X(x)$$為(累積)分佈函數。
* 如果機率密度函數(pdf)$$f_X$$存在時，上式可改寫為：$$\displaystyle \mathrm{E}(e^{itX})=\int_{-\infty}^\infty e^{itx} f_X(x)dx$$。
