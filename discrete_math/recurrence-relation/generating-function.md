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

