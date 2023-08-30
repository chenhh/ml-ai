---
description: almost Uniform convergence
---

# 幾乎一致收斂

##



## 幾乎一致收斂(almost uniform convergence)

> 函數序列$$\{f_n\}$$幾乎處處一致收斂至函數$$f$$：
>
> $$\forall \epsilon > 0$$，存在可測集$$E_{\epsilon}$$且滿足$$\mu(E_{\epsilon})<\epsilon$$使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)$$uniformly on $$E_\epsilon^c$$。
>
> 或者說$$\forall \epsilon >0, ~ \mu(E_{\epsilon}) < \infty, ~ \exist n_0 \in \mathbb{N}\ni \forall n \geq n_0$$$$\displaystyle \sup_{x \in X - E_\epsilon^c}\| f_n(x) - f(x)\| < \epsilon$$。

註：<mark style="color:blue;">幾乎一致收斂，只要求一致收斂不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度很小，即</mark> $$\mu(E_\epsilon)< \epsilon$$<mark style="color:blue;">。而幾乎處處有性質</mark>$$P(x)$$<mark style="color:blue;">，則要求</mark>$$P(x)$$<mark style="color:blue;">不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度為0，即</mark>$$\mu(E_\epsilon)=0$$ <mark style="color:blue;">。因此「幾乎一致收斂」絕對不可以說成「幾乎一致收斂」，兩者不是等價定義</mark>。

因此幾乎一致收斂不可寫為$$\exists E_\epsilon \subseteq E, ~ \mu(E_\epsilon)=0 \ni f_n \rightarrow f \text{ uniformly  on } E-E_0$$；

但如果可得$$\displaystyle \sup_{x \in E-E_0}|f_n(x) - f(x)|=0, \forall n \geq n_0$$時，為一致收斂。

#### 範例

$$f_n(x)=x^n$$ on $$[0,1]$$，可得點態收斂$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)= \left\{ \begin{aligned} 0&, \text{ if } 0 \leq x < 1, \\ 1&, \text{ if } x = 1  \end{aligned} \right.$$為非連續函數，但即使去除掉$$x=1$$，考慮$$f_n(x)=x^n ~ \text{ on } [0,1)$$也非一致收斂(由sup的定義可得$$\displaystyle \sup_{x \in [0,1)}x^n = \sup_{x \in (0,1)}x^n = \sup_{x \in (0,1)}x^n =1$$)；更進一步可得不存在集合$$S$$使得$$f_n \rightarrow f$$ uniformly on $$[0,1]-S$$。

令$$0 < \epsilon <1$$，取$$x = \frac{1+\epsilon}{2}$$，可得$$\epsilon < x < 1$$。

$$x^n = \frac{1+\epsilon}{2}^n=\frac{1}{2^n}(1+\epsilon)^n=\frac{1}{2^n} \sum_{k=0}^n \binom{n}{k}\epsilon^k > \frac{1}{2^n} \epsilon \sum_{k=0}^n \binom{n}{k} = \frac{1}{2^n} 2^n \epsilon = \epsilon$$

此時不存在$$n_0 \in \mathbb{N}$$使得$$x^{n_0} < \epsilon~\forall 0 < \epsilon < 1$$，因此不為一致收斂。

#### 幾乎一致收斂定義的討論

* [https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition](https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition)
* [https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence](https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence)
* [https://math.stackexchange.com/questions/3198020/does-xn-converges-uniformly-on-0-1](https://math.stackexchange.com/questions/3198020/does-xn-converges-uniformly-on-0-1)
* [https://math.stackexchange.com/questions/1254285/why-is-f-nx-xn-not-uniformly-convergent-on-0-1](https://math.stackexchange.com/questions/1254285/why-is-f-nx-xn-not-uniformly-convergent-on-0-1)

#### 範例

考慮閉區間$$[0,1]$$的Borel set。$$f_n(x)=x^n$$為連續函數，則：

1. $$f_n \rightarrow f$$點態收斂。
2. $$f_n \rightarrow f$$ 幾乎處處一致收斂。

$$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=f(x)=\left\{ \begin{aligned} 0 &, ~ x \in [0, 1) \\ 1 &, ~ x= 1 \end{aligned} \right.$$為點態收斂。

$$\displaystyle$$$$\displaystyle \sup_{x \in [0,1]} | f_n(x) - f(x) | = 1 \neq 0$$所以非一致收斂。

取$$\epsilon \in (0,1)$$，$$E_{\epsilon}=(1-\frac{\epsilon}{2}, 1]$$，$$\mu(E_\epsilon)= \frac{\epsilon}{2}$$，

且對於$$\forall x \in [0,1] - E_\epsilon$$，可得$$\displaystyle \sup_{x \in [0,1] - E_{\epsilon}}\|f_n(x) - f(x)\|=\sup_{x \in [0, 1-\epsilon]}\|x^n  - 0\|=\| 1- \frac{\epsilon}{2}\|^n \rightarrow 0$$ as $$n \rightarrow \infty$$。

### 幾乎一致收斂保證幾乎處處收斂

> 定義在集合$$E$$的幾乎處處實值(有限)的可測函數序列$$\{f_n\}$$幾乎一致收斂於可測函數$$f$$ ，則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~\text{a.e. on } E$$ 。
>
> <mark style="color:blue;">註：此處的</mark>$$\mu(E)$$<mark style="color:blue;">可為無窮大，即不限定在有限測度空間</mark>。

<details>

<summary>proof：由定義直接證明</summary>

因為$$\{f_n\}$$幾乎一致收斂於$$f$$，由定義得存在集合$$E_\epsilon \subseteq E$$滿足$$\forall \epsilon > 0$$，$$\mu(E_\epsilon) < \epsilon$$ $$\displaystyle \exists n_0 \in \mathbb{N} \ni \forall n \geq n_0, \sup_{x \in E-E_\epsilon}|f_n(x) - f(x)|=0$$。

取$$\epsilon=\frac{1}{m}, m \in \mathbb{N}$$，由一致收斂定義可得$$\forall m >1 ~\exists \mu(E_m)< \frac{1}{m} \ni f_n \rightarrow f \text{ unif. on } E_m^c$$。

令$$\displaystyle F=\bigcup_{m=1}^\infty E_m^c$$，因為一致收斂為點態收斂，因此$$f_n \rightarrow f \text{ pointwise on } F$$。

而$$\displaystyle \mu(F^c)= \mu(\bigcap_{m=1}^\infty E_m)\leq \mu(E_m) < \frac{1}{m}, ~\forall m \in \mathbb{N}$$，因此$$\mu(F^c)=0$$，所以$$f_n \rightarrow f \text{ a.e. on } F$$

(QED)

</details>

## Egoroff定理 (幾乎處處收斂在有限測度空間中幾乎一致收斂)

> 令$$\mu(E) <\infty$$為有限測度集合，$$\{f_n\}$$為$$E$$上的幾乎處處有限(幾乎處處實數值)的可測函數序列，則
>
> * $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{a.e.} \Rightarrow \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{almost unif.}$$
>
> <mark style="color:red;">註：點態收斂無法保證一致收斂，但在有限測度時，去掉很小的測度集合</mark>$$E_\epsilon$$<mark style="color:red;">後為幾乎一致收斂</mark>。

<details>

<summary>proof:</summary>



</details>

### 範例：非一致收斂但為幾乎一致收斂

$$f_n(x)=x^n, ~ x \in [0,1]$$

則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) =  \left\{ \begin{aligned} &0, ~ \text{ if } 0 \leq x < 1 \\ &1, ~ \text{ if } x=1 \end{aligned} \right.$$

得$$\displaystyle \sup_{x \in [0,1]}|f_n(x) - f(x)| = 1 \neq 0$$非一致收斂。

$$\forall \epsilon > 0, ~ E_0=[1-\epsilon, 1]$$，可得$$m(E_0)=\epsilon$$

### 範例：非有限測度時，Egroff定理不一定成立

令$$(X, \Sigma)$$為實數上的Lebesgue可測空間，$$f_n(x) =\chi_{(n, \infty)}(x)$$。

則$$\displaystyle \lim_{n \rightarrow \infty } f_n(x) = 0 ~\text{a.e.}$$但不是almost uniformly。

## Lusin定理

> $$f: E \rightarrow \mathbb{R}$$為可測函數。則存在連續函數$$g: \mathbb{R} \rightarrow \mathbb{R}$$與閉集合$$F \subseteq E$$滿足$$f(x)=g(x), ~ \forall x \in F$$且$$\mu(E-F)=0$$。
>
> <mark style="color:red;">註：可測函數去除掉測度為0的定義域集合後為連續函數</mark>。



參考資料

* [\[知乎\] Egoroff定理：重溫與昇華](https://zhuanlan.zhihu.com/p/503514372)。
* [\[知乎\] Egoroff定理和Lusin定理](https://zhuanlan.zhihu.com/p/36952467)。
* [https://wuli.wiki/online/EgrfTh.html](https://wuli.wiki/online/EgrfTh.html)
