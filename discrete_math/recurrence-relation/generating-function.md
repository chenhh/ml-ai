# 生成函數法

## 數列的生成函數

> 給定數列$$\{a_n\}_{n=0}^\infty$$，則其生成函數$$A(x)=a_0+a_1x+\dots+a_nx^n+\dots = \sum_{n=0}^\infty a_n x^n$$

### 起始點不同的生成函數

#### $$a_n$$型

* $$\displaystyle \sum_{n=1}^\infty a_nx^n= a_1x+\dots + a_nx^n+\dots = A(x)-a_0$$
* $$\displaystyle \sum_{n=2}^\infty a_nx^n= a_2x^2+\dots + a_nx^n+\dots = A(x)-a_0-a_1x$$
* 以此類推

#### $$a_{n-1}$$型

* $$\displaystyle \sum_{n=1}^\infty a_{n-1}x^n= a_0x+a_1x^2 +\dots + a_nx^{n+1}+\dots = xA(x)$$
* $$\displaystyle \sum_{n=2}^\infty a_{n-1}x^n= a_1x^2 +\dots + a_nx^{n+1}+\dots = xA((x)-a_0)$$
* 以此類推

#### $$a_{n-2}$$型

* $$\displaystyle \sum_{n=2}^\infty a_{n-2}x^n= a_0x^2+a_1x^3 +\dots + a_nx^{n+2}+\dots = x^2A(x)$$
* $$\displaystyle \sum_{n=3}^\infty a_{n-2}x^n= a_1x^3+a_2x^4 +\dots + a_nx^{n+2}+\dots = x^2(A(x)-a_0)$$
* 以此類推

這些是常見的生成函數關係式，如果有用到其它型式者，類推即可。

## 範例：Fibonacci數列

$$\left\{ \begin{aligned} & f_{n}= f_{n-1}+f_{n-2}, ~ n\geq 2 \\ & f_0=0, ~f_1=1 \end{aligned} \right.$$

令$$A(x)=\sum_{n=0}^\infty f_nx^n$$

因為$$f_n=f_{n-1}+f_{n-2}$$

所以$$\sum_{n=2}^\infty f_nx^n = \sum_{n=2}^\infty f_{n-1} x^n + \sum_{n=2}^\infty f_{n-2} x^n$$

$$A(x)-f_0-f_1x=x(A(x)-f_0)+x^2A(x)$$

整理得$$A(x)=\frac{x}{1-x-x^2} = \frac{x}{(1-c_1x)(1-c_2x)}, ~ c_1 = \frac{1+\sqrt{5}}{2}, ~ c_2 = c_1 = \frac{1-\sqrt{5}}{2}$$

移項得$$\begin{aligned} A(x)=\frac{x}{1-x-x^2} &= \frac{1}{\sqrt{5}} \left( \frac{1}{1-c_1x} - \frac{1}{1-c_2 x}\right) \\  & =\frac{1}{\sqrt{5}}\left(   \sum_{n=0}^\infty (c_1 x)^n - \sum_{n=0}^\infty (c_2 x)^n \right) \\  & = \frac{1}{\sqrt{5}}\left( \sum_{n=0}^\infty (c_1^n - c_2^n) x^n\right)  \end{aligned}$$

可得$$a_n =a_n = \frac{1}{\sqrt{5}}\left(   \left(\frac{1+\sqrt{5}}{2} \right)^n -  \left(\frac{1-\sqrt{5}}{2} \right)^n  \right), ~ n \geq 0$$



## 範例：長度為n的二進位數列，不含連續0有幾種

令$$a_n$$為所求的序列個數，可分為第n位數字為0，則第n-1位數字必為1，因此前n-2個數字不含連續0即可；與第n位數字為1兩種情形，則前n-1個數子必不含連續0。

可得遞迴關係式&#x20;

* $$a_n=a_{n-1}+a_{n-2}, n\geq 3$$
* 邊界條件$$a_1=2$$, $$a_2=3$$
