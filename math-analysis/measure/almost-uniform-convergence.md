---
description: almost Uniform convergence
---

# 幾乎一致收斂

## 簡介

幾乎一致收斂是幾乎處處收斂和其它收斂方式中介的性質，常用於證明當中。

## 幾乎一致收斂(almost uniform convergence)

> 函數序列$$\{f_n\}$$幾乎一致收斂至函數$$f$$：
>
> $$\forall \epsilon > 0$$，存在可測集$$E_{\epsilon}$$且滿足$$\mu(E_{\epsilon})<\epsilon$$使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)$$uniformly on $$E_\epsilon^c$$。
>
> 或者說$$\forall \epsilon >0, ~ \mu(E_{\epsilon}) < \infty, ~ \exist n_0 \in \mathbb{N}\ni \forall n \geq n_0$$$$\displaystyle \sup_{x \in X - E_\epsilon^c}\| f_n(x) - f(x)\| < \epsilon$$。
>
> 對於任何給定值 ε，都可以找到一個「可忽略不計」的集合（測度小於ε ），在這個集合上允許不均勻收斂，而在其他定義域，均滿足一致收斂。
>
> 幾乎處處一致收斂(uniform convergence almost everywhere )\[條件更嚴格]
>
> $$\displaystyle \exists E_0，\mu(E_0)=0 \ni  \lim_{n \rightarrow \infty }\sup_{x \in X-E_0} |f_n(x)-f(x)|=0$$。
>
> 此處有一測量0的集合，可允許非均勻收斂，而在其它定義域，均滿足一致收斂。
>
> <mark style="background-color:red;">幾乎處處一致收斂=>幾乎一致收斂</mark>。

註：<mark style="color:blue;">幾乎一致收斂，只要求一致收斂不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度很小，即</mark> $$\mu(E_\epsilon)< \epsilon$$<mark style="color:blue;">。而幾乎處處有性質</mark>$$P(x)$$<mark style="color:blue;">，則要求</mark>$$P(x)$$<mark style="color:blue;">不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度為0，即</mark>$$\mu(E_\epsilon)=0$$ <mark style="color:blue;">。因此「幾乎一致收斂」並非「幾乎處處一致收斂」</mark>。<mark style="color:red;">幾乎處處一致收斂可保證幾乎一致收斂，反之不成立</mark><mark style="color:blue;">。</mark>

<mark style="color:red;">註：不一致收斂發生於收斂函數</mark>$$f$$<mark style="color:red;">出現"突變"處，挖去突變點的附近測度可以任意小的集合(但不是零測度集)，則</mark>$$f_n$$<mark style="color:red;">可以一致收斂</mark>。例如觀察一個非一致致收斂的函數列，比如 $$\ f_n( x )=x^n$$ 在區間$$[ 0 , 1 ]$$上就非一致收斂，但可發現如果把區間挖掉長度$$ϵ>0$$任意小的一部分(不等於0)，那麼$$f_n$$ 在$$[0 , 1 − \epsilon]$$ 上總是一致收斂的。

因此幾乎一致收斂不可寫為$$\exists E_\epsilon \subseteq E, ~ \mu(E_\epsilon)=0 \ni f_n \rightarrow f \text{ uniformly  on } E-E_0$$；

但如果可得$$\displaystyle \sup_{x \in E-E_0}|f_n(x) - f(x)|=0, \forall n \geq n_0$$時，為一致收斂。

#### 範例：幾乎一致收斂但非幾乎處處一致收斂

$$f_n(x)=x^n$$ on $$[0,1]$$，可得點態收斂$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)= \left\{ \begin{aligned} 0&, \text{ if } 0 \leq x < 1, \\ 1&, \text{ if } x = 1  \end{aligned} \right.$$為非連續函數，但即使去除掉$$x=1$$，考慮$$f_n(x)=x^n ~ \text{ on } [0,1)$$也非一致收斂(由sup的定義可得$$\displaystyle \sup_{x \in [0,1)}x^n = \sup_{x \in (0,1)}x^n = \sup_{x \in (0,1)}x^n =1$$)；更進一步可得不存在集合$$S$$使得$$f_n \rightarrow f$$ uniformly on $$[0,1]-S$$。

令$$0 < \epsilon <1$$，取$$x = \frac{1+\epsilon}{2}$$，可得$$\epsilon < x < 1$$。

$$x^n = \frac{1+\epsilon}{2}^n=\frac{1}{2^n}(1+\epsilon)^n=\frac{1}{2^n} \sum_{k=0}^n \binom{n}{k}\epsilon^k > \frac{1}{2^n} \epsilon \sum_{k=0}^n \binom{n}{k} = \frac{1}{2^n} 2^n \epsilon = \epsilon$$

此時不存在$$n_0 \in \mathbb{N}$$使得$$x^{n_0} < \epsilon~\forall 0 < \epsilon < 1$$，因此不為一致收斂。

#### 幾乎一致收斂定義的討論

* [https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition](https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition)
* [https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence](https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence)
* [https://math.stackexchange.com/questions/2714634/equivalent-definition-of-almost-uniform-convergence?rq=1](https://math.stackexchange.com/questions/2714634/equivalent-definition-of-almost-uniform-convergence?rq=1)
* [https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence?rq=1](https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence?rq=1)
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

令$$\displaystyle F=\bigcup_{m=1}^\infty E_m^c$$，因為在所有集合中均為一致收，且一致收斂為點態收斂，因此$$f_n \rightarrow f \text{ pointwise on } F$$。

而$$\displaystyle \mu(F^c)= \mu(\bigcap_{m=1}^\infty E_m)\leq \mu(E_m) < \frac{1}{m}, ~\forall m \in \mathbb{N}$$，因此$$\mu(F^c)=0$$，所以$$f_n \rightarrow f \text{ a.e. on } F$$

(QED)

</details>

## Egoroff定理 (幾乎處處收斂在有限測度空間中幾乎一致收斂)

> 令$$\mu(E) <\infty$$為有限測度集合，$$\{f_n\}$$為$$E$$上的幾乎處處有限(幾乎處處實數值)的可測函數序列，則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{a.e.} \Rightarrow \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{almost unif.}$$。
>
> 若$$f_n \rightarrow f \text{ a.e. on } E$$，則$$\forall \epsilon > 0$$，存在可測集合$$E_\epsilon$$且$$\mu(E_\epsilon)<\epsilon \ni f_n \rightarrow f \text{ unif. on } E-E_\epsilon$$。
>
> <mark style="color:red;">註：一般可測空間中，幾乎一致收斂可得幾乎處處收斂；而Egoroff定理證明了有限測度空間中(如機率空間)，幾乎處處收斂等價於幾乎一致收斂</mark>。

<details>

<summary>proof:將不一致收斂的集合，以可數集合列表示，再利用測度的可數可加性證明為任意小</summary>

proof: 不收斂的集合測度小於epsilon

因為$$f_n \rightarrow f \text{ a.e. on }E$$，即存在可測集合$$E_0 \subseteq E , \mu(E_0)=0$$使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{pointwise   on} E-E_0$$。

即給定$$x \in E-E_0$$, 取$$\epsilon=1/k, ~k \in \mathbb{N}$$，則存在$$n_k \in \mathbb{N} \ni |f_n(x) - f(x)|<1/k, ~\forall n \geq n_k$$。

若固定$$k$$的值，上式可得在$$n \geq n_k$$之後，所有$$x \in E-E_0$$的元素都可以保證$$|f_n(x) - f(x)| < 1/k$$。

令集合$$A_{n,k}=\{ x \in E- E_0 ~|~|f_n(x) - f(x)| \geq 1/k \}$$

則給定$$k$$後，集合$$E-E_0$$中的點$$x$$只會在$$n < n_k$$時，可能為$$A_{n,k}$$中的元素。而所有的點$$x$$在$$n \geq n_k$$時，必定不是$$A_{n,k}$$中的元素。

由集合序列上極限定義$$\displaystyle \limsup_{n \rightarrow \infty} A_{n,k}=\bigcap_{n=1}^\infty \bigcup_{n=n_k}^\infty A_{n,k}=\emptyset$$

由測度定義得$$\displaystyle \mu(\limsup_{n \rightarrow \infty} A_{n,k})=\mu(\bigcap_{n=1}^\infty \bigcup_{n=n_k}^\infty A_{n,k})=\mu(\emptyset)=0$$--(1)

令$$B_{n,k}=\bigcup_{i=n}^\infty A_{i,k}$$。

可得$$B_{n,k} \supseteq B_{n+1,k}\supseteq \dots$$為單調遞減集合序列，因此$$\displaystyle \lim_{n \rightarrow \infty}B_{n,k}=\bigcap_{n=1}^\infty B_{n,k}$$。

整理可得$$\displaystyle \bigcap_{n=1}^\infty \bigcup_{n=n_k}^\infty A_{n,k} = \bigcap_{n=1}^\infty B_{n,k} = \lim_{n \rightarrow \infty} B_{n,k}$$--(2)

由遞減集合極限的測度且$$\mu(E)<\infty$$，(2)可得$$\displaystyle \mu( \lim_{n \rightarrow \infty} B_{n,k}) = \lim_{n \rightarrow \infty} \mu(B_{n,k})$$--(3)

由(1,2,3)可得$$\displaystyle \lim_{n \rightarrow \infty} \mu(B_{n,k})=0$$。--(4)

因此對於任意$$k \in \mathbb{N}$$，由(4)的極限定義得存在$$n_k \in \mathbb{N} \ni \mu(B_{n_k, k}) < \frac{\epsilon}{2^k}$$

再將所有滿足條件的$$k$$的集合聯集，可得測度$$\displaystyle \mu(\bigcup_{k=1}^\infty B_{n_k, k} ) \leq \sum_{k=1}^\infty \mu(B_{n_k, k}) < \sum_{k=1}^\infty \frac{\epsilon}{2^k}=\epsilon$$--(5)

即$$\displaystyle E_\epsilon = \bigcup_{k=1}^\infty B_{n_k, k} = \bigcup_{k=1}^\infty \bigcup_{n=n_k}^\infty A_{n,k} = \{x \in E- E_0 ~|~ |f_n(x) - f(x)| \geq 1/k \}$$的測度$$\mu(E_\epsilon)=\epsilon$$。

(QED)

proof: $$f_n$$在$$E-E_\epsilon$$上一致連續。

因為給定$$k \in \mathbb{N}$$，可得$$x \in E-E_0$$且$$X \notin E_\epsilon$$時，可得$$x \notin B_{n_k, k}$$，由集合定義可得$$|f_n(x)-f(x)| < 1/k, \forall n \geq n_k$$。

因此可得$$f_n \rightarrow f \text{ uniform. on } (E-E_0) - E_\epsilon$$

因為$$(E-E_0) -E_\epsilon = E -(E_0 \cup E_\epsilon)$$，由(5)與測度定義得$$\mu(E_0 \cup E_\epsilon) \leq \mu(E_0) + \mu(E_\epsilon) = \mu(E_\epsilon) < \epsilon$$

(QED)

</details>

### 範例：非一致收斂但為幾乎一致收斂

$$f_n(x)=x^n, ~ x \in [0,1]$$

則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) =  \left\{ \begin{aligned} &0, ~ \text{ if } 0 \leq x < 1 \\ &1, ~ \text{ if } x=1 \end{aligned} \right.$$

得$$\displaystyle \sup_{x \in [0,1]}|f_n(x) - f(x)| = 1 \neq 0$$非一致收斂。

$$\forall \epsilon > 0, ~ E_\epsilon=[1-\epsilon, 1]$$，可得$$m(E_\epsilon)=\epsilon$$

且對於所有的$$x \in [0,1]-E_\epsilon$$，可得$$\displaystyle \sup_{[0,1]-E_\epsilon}|f_n(x)-f(x)|=\sup_{x \in [0,1-\epsilon]}|x^n -0|=(1-\epsilon)^n \rightarrow 0 \text {as } n \rightarrow \infty$$，因此為一致收斂。

### 範例：非有限測度時，Egroff定理不一定成立

令$$(X, \Sigma)$$為實數上的Lebesgue可測空間，$$f_n(x) =\chi_{(0, n)}(x), ~n=1,2,\dots ~ x \in (0,\infty)$$。

則$$\displaystyle \lim_{n \rightarrow \infty } f_n(x) = 1 ~\text{a.e. on } (0, \infty)$$但是在$$(0, \infty)$$中任一個有限測度集外均非一致收斂於$$f(x)=1$$。

## 幾乎處處收斂保證測度收斂

* [https://math.stackexchange.com/questions/3332265/almost-uniform-convergence-implies-convergence-in-measure?rq=1](https://math.stackexchange.com/questions/3332265/almost-uniform-convergence-implies-convergence-in-measure?rq=1)



參考資料

* [\[知乎\] Egoroff定理：重溫與昇華](https://zhuanlan.zhihu.com/p/503514372)。
* [\[知乎\] Egoroff定理和Lusin定理](https://zhuanlan.zhihu.com/p/36952467)。
* [https://wuli.wiki/online/EgrfTh.html](https://wuli.wiki/online/EgrfTh.html)
