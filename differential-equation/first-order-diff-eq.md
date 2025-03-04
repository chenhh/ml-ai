---
description: Separation of variables
---

# 一階微分方程式

## 分離變數法(separation of variables)

> 若可將一階微分方程式$$F(x,y,y^{'})=0$$寫成 $$\frac{dy}{dx}=f(x)g(y), ~ g(y) \neq 0$$或$$P(x)dx+Q(y)dy=0$$，則稱為可分離微分方程式（separable differential equation）。
>
> 此種微分方程式的通解為
>
> * $$\int \frac{dy}{g(y)}=\int f(x)dx+c$$或
> * $$\int P(x)dx + \int Q(y)dy=c$$, $$c \in \mathbb{R}$$為任意係數。

如果為初值問題：

* $$\left\{  \begin{aligned} & P(x)dx+Q(y)dy=0, \\ &y(x_0)=y_0 \end{aligned} \right.$$
* 則特解為 $$\int_{x_0}^x P(x)dx+\int_{y_0}^y Q(y)dy=0$$

### 範例

> $$\frac{dy}{dx}+y^2e^{-x}=0$$

* $$\frac{dy}{dx}=-y^2 e^{-x}$$移項可得$$-\frac{dy}{y^2}=e^{-x}dx$$
* 若$$y\neq 0$$，則$$\int - \frac{1}{y^2} dy = \int e^{-x}dx$$，所以通解為$$\frac{1}{y}=-e^{-x}+c$$。

> $$x \frac{dy}{dx} -y - y^3=0$$

* 可整理為 $$xdy - y(1+y^2)dx=0$$
* 同除$$(1+y^2)xy$$得 $$\frac{1}{y(1+y^2)}dy - \frac{1}{x}dx=0$$，積分式 $$\int  \frac{1}{y(1+y^2)}dy - \int \frac{1}{x}dx=c$$
* $$\therefore \int \left( \frac{1}{y} - \frac{y}{1+y^2}\right) dy - \int \frac{1}{x} dx = c$$
* $$\ln |y| - \frac{1}2{} \ln (1+y^2) - \ln |x| = c$$
* 通解為 $$y = e^c x \sqrt{1+y^2}$$

