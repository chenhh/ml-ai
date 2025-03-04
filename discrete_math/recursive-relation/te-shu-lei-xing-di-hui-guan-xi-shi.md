# 特殊類型遞迴關係式

令$$A(x)=a_0 + a_1 x + \dots + a_n x^n + \dots = \sum_{n=0}^\infty a_n x^n$$為數列$$\{a_n\}_{n=0}^\infty$$的生成函數。

則$$\displaystyle \begin{aligned} A^2(x) & =\left(\sum_{n=0}^\infty a_n x^n \right)\left(\sum_{n=0}^\infty a_n x^n \right) \\     & = (a_0 + a_1 x + \dots + a_n x^n + \dots) (a_0 + a_1 x + \dots + a_n x^n + \dots) \\     & = a_0a_0 + (a_0 a_1 + a_1 a_0)x + (a_0a_2 + a_1a_1 + a_2 a_0)x^2 + \dots  \\     & + (a_0a_n + a_1a_{n-1}+\dots + a_{n-1}a_1 + a_n a_0)x^n + \dots \\     & = \sum_{n=0}^\infty (a_0a_n + a_1a_{n-1}+\dots + a_{n-1}a_1 + a_n a_0)x^n  \end{aligned}$$

得$$A^2(x)$$為數列$$a_0a_0, a_0 a_1 + a_1 a_0, \dots, a_0a_n + a_1a_{n-1}+\dots + a_{n-1}a_1 + a_n a_0$$的生成函數。

將上式展開可得

* $$A^2(x)=\sum_{n=1}^\infty (a_0a_{n-1} + a_1a_{n-2}+\dots + a_{n-2}a_1 + a_{n-1} a_0)x^{n-1}$$
* $$A^2(x)=\sum_{n=2}^\infty (a_0a_{n-2} + a_1a_{n-3}+\dots + a_{n-3}a_1 + a_{n-2} a_0)x^{n-2}$$

## 範例：n個節點的相異二元樹個數?

* 令$$a_n$$為$$n$$個節點的相異二元樹個數，$$a_0=1$$。
* 若左子樹有$$k$$個節點時，則右子樹有$$n-k-1$$個節點，$$k=0,1,\dots,n-1$$。因此：
  * $$k=0$$時，有$$a_0 a_{n-1}$$種二元樹。
  * $$k=1$$時，有$$a_1a_{n-2}$$種二元樹。
  * ...
  * $$k=n-1$$時，有$$a_{n-1}a_0$$種二元樹。
* &#x20;得$$a_n=a_0 a_{n-1}+a_1a_{n-2}+\dots +a_{n-1}a_0, ~ a_1=1$$
* 令生成函數$$A(x)=\sum_{n=0}^\infty a_n x^n$$
* 因為$$a_n=a_0 a_{n-1}+a_1a_{n-2}+\dots +a_{n-1}a_0$$
* 所以$$\sum_{n=1}^\infty a_nx^n = \sum_{n=1}^\infty (a_n=a_0 a_{n-1}+a_1a_{n-2}+\dots +a_{n-1}a_0)x^n$$
* $$A(x)-a_0=x \sum_{n=1}^\infty (a_n=a_0 a_{n-1}+a_1a_{n-2}+\dots +a_{n-1}a_0)x^{n-1}$$
* $$A(x)-1=xA^2(x)$$
* $$A(x)=\frac{1 \pm \sqrt{1-4x}}{2x}$$--(1)

因為

$$\displaystyle \begin{aligned}  (1-4x)^{1/2}  & = \sum_{n=0}^\infty \binom{1/2}{n}(-4x)^n \\     & = \sum_{n=0}^\infty \frac{1/2(1/2-1)\dots(1/2-n+1)}{n!} (-1)^n 4^n x^n \\     & = \sum_{n=0}^\infty \frac{(-1)^{n-1}(1/2)(1/2)(3/2)\dots((2n-3)/2)}{n!} (-1)^n 2^n 2^n x^n \\     & = \sum_{n=0}^\infty \left( \frac{2n-1}{2n-1} \right) \left( \frac{1\cdot3\dots(2n-3)2^n}{n!} \right) \left( \frac{2\cdot4\dots(2n-4)2^n}{n!2^n} \right)x^n \\     & = \sum_{n=0}^\infty \left(  \frac{(2n)!2^n}{n!n!(2n-1)2^n} \right)x^n \\     & = - \sum_{n=0}^\infty\left(  \frac{(2n)!}{n!n!(2n-1)} \right)x^n \\     & = - \sum_{n=0}^\infty \frac{1}{2n-1} \binom{2n}{n} x^n \\ \end{aligned}$$

由於二元樹個數為正數，且由上式知道$$(1-4x)^{1/2}$$為負數。

所以$$\displaystyle \begin{aligned}  (A(x) & = \frac{1 - \sqrt{1-4x}}{2x} \\       & = \frac{1+\sum_{n=0}^\infty \frac{1}{2n-1} \binom{2n}{n} x^n }{2x} \\       & = \frac{1}{2} \sum_{n=1}^\infty \frac{1}{2n-1} \binom{2n}{n} x^{n-1}  \end{aligned}$$

而$$a_n$$為$$A(x)$$中$$x^n$$的係數，因此$$a_n=\frac{1}{n+1}\binom{2n}{n}$$ ，<mark style="color:red;">也稱為Catalan數</mark>(ANS)
