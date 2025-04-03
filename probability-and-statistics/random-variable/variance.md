---
description: 方差，variance
---

# 變異數

## 變異數（variance）

> $$\mathrm{Var}(X)=\mathrm{E}(X- \mathrm{E}(X))^2= \mathrm{E}(X^2) - (\mathrm{E}(X))^2$$

常用$$\mu, \sigma^2$$表示隨機變數$$X$$的期望值與變異數。

<mark style="color:red;">變異數的不偏估計式(樣本估計式)</mark>為 $$\hat{\sigma_X}^2\equiv S_n^2=\frac{1}{n-1}\sum_{i=1}^n (x_i - \overline{x})^2$$。

```python
# -*- coding: UTF-8 -*-
import numpy as np
from typing import Iterable


def variance(values: Iterable):
    xs = np.asarray(values)

    e_x = xs.mean()
    e_x2 = (xs * xs).mean()
    var_x1 = e_x2 - e_x * e_x
    var_x2 = ((xs - e_x) * (xs - e_x)).mean()
    var_np = xs.var(ddof=0)  # default bias estimator
    np.testing.assert_almost_equal(var_x1, var_np, decimal=10)
    np.testing.assert_almost_equal(var_x2, var_np, decimal=10)
    print(f"{var_x1}, {var_x2}, {var_np}")


if __name__ == '__main__':
    values = np.random.rand(1000)
    variance(values)
```

## 變異數的性質

> $$\mathrm{Var}(aX+b) = a^2 \mathrm{Var}(X)$$
>
> 變異數為分佈的(變異)寬度，因此位移不會造成寬度變動，而倍數會放大寬度。

proof:

$$\begin{aligned} \mathrm{Var}(aX+b) & = \mathrm{E}((aX+b - (a\mathrm{E}(X)+b))^2) \\ & = \mathrm{E}((aX - a\mathrm{E}(X))^2) \\ & = a^2 \mathrm{E}((X-\mathrm{E}(X))^2) \\ & = a^2 \mathrm{Var}(X) \end{aligned}$$

## 雙變量隨機變數

> 若$$X,Y$$為離散型隨機變數，則
>
> * 機率質量函數(pmf)定義為$$P_{XY}(x,y)\equiv P(X=x, Y=y)$$
> * 分佈函數$$\displaystyle F_{XY}(x,y) = \sum_{a \leq x} \sum_{b \leq y}P_{XY}(a,b)$$
> * 邊際密度函數(marginal density function)
>   * $$\displaystyle P_X(x) = \sum_y P_{XY}(x,y)$$
>   * $$\displaystyle P_Y(y) = \sum_x P_{XY}(x,y)$$
> * 兩隨機變數獨立記為$$X \perp Y$$滿足 $$P_{XY}(x,y)=P_X(x) P_Y(y)$$
>
> 若$$X,Y$$為連續型隨機變數，則
>
> * 分佈函數 $$\displaystyle F_{XY}(x,y) = \int_{-\infty}^x \int_{-\infty}^y f_{XY}(u,v)dudv$$
> * 機率密度函數$$f_{XY}(x,y) = \frac{\partial^2}{\partial x \partial y} F(x,y)$$
> * 邊際密度函數
>   * $$\displaystyle f_X(x) = \int_{-\infty}^{\infty} f_{XY}(x,y)dy$$
>   * $$\displaystyle f_Y(y) = \int_{-\infty}^{\infty} f_{XY}(x,y)dx$$
> * 兩隨機變數獨立記為$$X \perp Y$$滿足 $$F_{XY}(x,y)=F_X(x) F_Y(y)$$

## 共變異數與相關係數

> 隨機變數$$X,Y$$的
>
> * <mark style="color:red;">共變異數（covariance</mark>） $$\mathrm{Cov}(X,Y) \equiv \mathrm{E}[(X-\mathrm{E}(X))(Y-\mathrm{E}(Y))]$$
> * <mark style="color:red;">相關係數（correlation coefficient）</mark> $$ho_{XY} \equiv \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

* $$\begin{aligned} \mathrm{Cov}(X,Y) &\equiv \mathrm{E}[(X-\mathrm{E}(X))(Y-\mathrm{E}(Y))] \\& = \mathrm{E}[XY - X\mathrm{E}(Y) - Y\mathrm{E}(X)+ \mathrm{E}(X)\mathrm{E}(Y) ] \\ &= \mathrm{E}(XY)-\mathrm{E}(X) \mathrm{E}(Y) - \mathrm{E}(X) \mathrm{E}(Y) + \mathrm{E}(X) \mathrm{E}(Y) \\ &= \mathrm{E}(XY) - \mathrm{E}(X) \mathrm{E}(Y) \end{aligned}$$
* 共變異數的不偏估計式為 $$\displaystyle \hat{\mathrm{Cov}}(X,Y)=\frac{1}{n-1} \sum_{i=1}^n ((x_i - \overline{x}) (y_i - \overline{y}))$$
* $$\mathrm{Var}(X) = \mathrm{Cov}(X,X)=\mathrm{E}(X^2)-(\mathrm{E}(X))^2$$
* $$-1\leq \rho \leq 1$$
  * $$ho = -1$$表$$X,Y$$為完全（線性）負相關。
  * $$ho=1$$表$$X,Y$$為完全（線性）正相關。
  * $$ho=0$$表$$X,Y$$(線性)不相關。
* 相關係數的不偏估計式為 $$\hat{\rho}_{XY}=\frac{\hat{\mathrm{Cov}(X,Y)}}{\hat{\sigma_X} \hat{\sigma_Y}}$$
* $$\mathrm{V} (X \pm Y) = \mathrm{V}(X) + \mathrm{V}(Y)\pm 2\mathrm{Cov}(X,Y)$$
  * 若$$X \perp Y$$，即$$\mathrm{Cov}(X,Y)=0$$，則$$\mathrm{V}(X \pm Y) = \mathrm{X} + \mathrm{Y}$$
* \[Cauchy-Schwarz不等式] $$\mathrm{E}(X^2) \mathrm{E} (Y^2) \geq (\mathrm{E}(XY))^2$$

### 共變異數的性質

> $$\mathrm{Cov}(aX+c, bY+d)=ab \mathrm{Cov}(X,Y)$$
>
> 常數加於隨機變數，不會改變原本的共變異數

> $$\begin{aligned} \mathrm{Cov}(a_1 x_1 + a_2 x_2, b_1y_1+b_2 y_2) = \\ \mathrm{Cov}(a_1 x_1, b_1y_1)+ \mathrm{Cov}(a_1 x_2, b_2 y_2) + \\ \mathrm{Cov}(a_2 x_2, b_1 y_1) + \mathrm{Cov}(a_2 x_2, b_2 y_2) \\=a_1 b_1 \mathrm{Cov}(x_1, y_1) + a_1 b_2 \mathrm{Cov}(x_1, y_2) \\+ a_2 b_1 \mathrm{Cov}(x_2, y_1) + a_2 b_2 \mathrm{Cov}(x_2, y_2) \end{aligned}$$

## 樣本共變異數

給定兩組隨機樣本$$X_1, \dots, X_n$$，$$Y_1, \dots, Y_n$$。

* 樣本共變異數$$S_{XY} = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X})(Y_i - \overline{Y})$$
* 樣本相關係數 $$R_{XY} = \frac{S_{XY}}{S_X S_Y} = \frac{ \sum_{i=1}^n (X_i - \overline{X})(Y_i - \overline{Y})} {(\sum_{i=1}^n (X_i - \overline{X})^2 \sum_{i=1}^n (Y_i - \overline{Y})^2 )^{1/2}}$$
