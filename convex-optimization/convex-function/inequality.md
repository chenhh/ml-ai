# 不等式

## Jensen不等式

> 基本型：若$$f$$為凸函數，則$$\forall 0 \leq c \leq 1$$，$$f(cx + (1-c)y) \leq c f(x) + (1-c)f(y)$$。
>
> 多點：若$$f$$為凸函數，$$x_1, x_2 , \dots ,x_k \in \mathrm{dom} f$$, $$c_1, c_2, \dots, c_k \geq 0, ~ \sum_{i=1}^k c_i = 1$$，則$$f(c_1x_1 + \dots + c_k x_k ) \leq c_1 f(x_1 ) + \dots + c_k f(x_k)$$。
>
> 積分：令集合$$S \subseteq \mathrm{dom}f$$且$$\forall x \in S, ~ p(x) \geq 0, ~ \int_S p(x) dx = 1$$，若積分存在時，可得$$f\left( \int_S p(x)x dx \right) \leq \int_S f(x) dx$$
>
> 機率測度：$$x$$為隨機變數，且$$x\in \mathrm{dom}f$$的機率為1，若$$f$$為凸函數，且對應的期望值存在時，可得 $$f(\mathrm{E}(x)) \leq \mathrm{E}(f(x))$$。

### 應用：隨機擾動從平均效果上不會減少凸函數的值

$$f$$為凸函數，若$$x \in \mathrm{dom}f \subseteq \mathbb{R}^n$$，$$z\in \mathbb{R}^n$$為隨機變數，且其均值為$$\mathrm{E}(z)=0$$，則可得：

* $$\begin{aligned} \mathrm{E}(f(x+z)) & \geq f(\mathrm{E}(x+z)) \\     & = f(\mathrm{E}(x)+ \mathrm{E}(z)) \\     & =f(\mathrm{E}(x)) \end{aligned}$$

## 算術-幾何平均不等式(arithmetric-geometric mean inequality)

> $$\forall a,b \geq 0, ~ \sqrt{ab} \leq \frac{a+b}{2}$$

proof:

* $$-\log x$$為凸函數，令$$c = 1/2$$，則由Jensen不等式得$$-\log (\frac{a+b}{2}) \leq \frac{-\log a - \log b}{2}$$。
* 得$$\log (\frac{a+b}{2}) \geq \frac{\log a + \log b}{2} = \log (ab)^{1/2}$$
* 兩邊取指數得$$\frac{a+b}{2} \geq (ab)^{1/2}$$ (QED)

## Holder不等式

> $$p>1, ~ \frac{1}{p}+\frac{1}{q} = 1, ~ x, y \in \mathbb{R}^n$$可得
>
> $$\displaystyle \sum_{i=1}^n x_i y_i \leq \left(\sum_{i=1}^n |x_i|^p\right)^{1/p} \left(\sum_{i=1}^n |u_i|^q \right)^{1/q}$$
