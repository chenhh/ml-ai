---
description: almost Uniform convergence
---

# 幾乎一致收斂

## Littlewood three principles \[[wiki](https://en.wikipedia.org/wiki/Littlewood's\_three\_principles\_of\_real\_analysis)]

> 1. 每個（可測）集合幾乎就是一些區間(interval)的有限聯集(有限和)；&#x20;
> 2. 每個（$$L^k$$可積的）函數幾乎就是連續函數；
> 3. 每個點態收斂的函數列幾乎就是一致收斂的。
>
> 實變函數就是為了說明這些“幾乎(almost)”的意義。

## 函數序列收斂關係

測度$$\mu: E \rightarrow [0, \infty]$$，因此要考慮有限或無限測度的條件。

* <mark style="color:blue;">\[</mark>[<mark style="color:blue;">證明</mark>](measurable-seq-function.md#ji-hu-chu-chu-yi-zhi-shou-lian-bao-zheng-ji-hu-chu-chu-shou-lian)<mark style="color:blue;">]在有限或無限測度空間時，幾乎一致收斂的定義可得幾乎處處收斂</mark><mark style="color:red;">。</mark>
* <mark style="color:red;">\[</mark>[<mark style="color:red;">證明</mark>](almost-uniform-convergence.md#egoroff-ding-li-ji-hu-chu-chu-shou-lian-zai-you-xian-ce-du-tiao-jian-xia-wei-ji-hu-yi-zhi-shou-lian)<mark style="color:red;">]如果為有限測度空間時，Egoroff定理證明了幾乎處處收斂可保證幾乎一致收斂</mark>。
* \[證明]如果為有限測度空間時，幾乎處處收斂可得測度收斂。

<figure><img src="../../.gitbook/assets/convergence-min.png" alt=""><figcaption><p>收斂的性質</p></figcaption></figure>

## 收斂的定義

### (處處)點態收斂(everewhere pointwise convergence)

> $$\forall x \in E, ~\forall \epsilon > 0 ~\exists n_0 \in \mathbb{N} \ni |f_n(x)-f(x)|< \epsilon ~ \forall n > n_0$$

點態收態是根據每一點$$x$$判定收斂，因此每一點收斂的速度都不相同($$f_n$$ 上每一點$$x$$的值域收斂值$$f(x)$$的速度不同)。

此處處處(everywhere)強調對於定義域$$x\in E$$的性質全部成立。

### (處處)一致(均勻)收斂(everywhere uniformly convergence)

> $$\displaystyle \forall \epsilon > 0, \exists n_0 \in \mathbb{N} \ni \lim_{n \rightarrow \infty} \sup_{x \in E}|f_n(x) - f(x)| < \epsilon, ~\forall n \geq n_0$$。
>
> 或者令$$\displaystyle d_n = \sup_{x \in E} |f_n(x) - f(x)|$$，$$\displaystyle \lim_{n \rightarrow \infty} d_n =0$$。

一致收斂考慮的是全部集合內的點($$\forall x \in E$$)，因此每一點的收斂速度都相同(有相同的上限)。

<mark style="color:red;">點態收斂和一致收斂通常用於分析連續函數序列的收斂性，必須為一致收斂才能保證收斂到連續函數</mark>。

### 幾乎處處(點態)收斂(almost everywhere convergence)

> $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~ \text{a.e.}$$，即$$\mu(\{x \in X ~|~ \lim_{n \rightarrow \infty} f_n(x) \neq f(x) \}) = 0$$
>
> $$\exists E_0 \in \Sigma, ~ \mu(E_0)=0 \ni \forall x \in X - E_0, ~ \forall \epsilon > 0 \exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x)|<\epsilon, \forall n \geq n_0$$

函數序列在兩者不相等的集合$$E_0$$的測度為0，其餘的集合點態收斂 。

一般函數而言，單點(可數)集合的測度為0，因此只要$$E_0$$為可數個點的集合均滿足此性質。

<mark style="color:red;">幾乎處處收斂的零測度集合</mark>$$E_0$$<mark style="color:red;">，對於所有函數序列中的函數都是在</mark>$$E_0$$<mark style="color:red;">中測度為0，且在</mark>$$E-E_0$$<mark style="color:red;">外均收斂；而測度收斂中，對於所有序數序列中的函數無法找到共同的</mark>$$E_0$$<mark style="color:red;">，但是可以保證收斂函數與函數序列不相等的點集的測度為0</mark>。

### 幾乎一致(均勻)收斂 (almost uniformly convergence)

> $$\displaystyle \forall \epsilon > 0,\exists E_0 \in \Sigma \ni \mu(E_0) < \epsilon \text{ and } f_n \rightarrow f \text{ uniformly on } E - E_0$$

在測度為0或小於$$\epsilon$$的集合$$E_0$$之外，$$f_n$$一致收斂至$$f$$。

## Egoroff定理 (幾乎處處收斂在有限測度條件下為幾乎一致收斂)

> 令$$\mu(E) <\infty$$為有限測度集合，$$\{f_n\}$$為$$E$$上的幾乎處處有限(幾乎處處實數值)的可測函數序列，則
>
> * $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{a.e.} \Rightarrow \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{almost unif.}$$, $$E_0 \subseteq E$$為閉集合且$$\mu(E_0)=0$$
> * $$\forall \delta > 0 \exists E_{\delta} \subseteq E , ~ m(E_{\delta }) \leq \delta$$，使得$$f_n(x) \rightarrow f(x) \text{ almost uniformly on } E - E_\delta$$
>
> <mark style="color:red;">註：點態收斂無法保證一致收斂，但去掉零測度集合後可為幾乎一致收斂</mark>。

<details>

<summary>proof:</summary>



</details>

### 範例：非一致收斂但為幾乎一致收斂

$$f_n(x)=x^n, ~ x \in [0,1]$$

則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) =  \left\{ \begin{aligned} &0, ~ \text{ if } 0 \leq x < 1 \\ &1, ~ \text{ if } x=1 \end{aligned} \right.$$

得$$\displaystyle \sup_{x \in [0,1]}|f_n(x) - f(x)| = 1 \neq 0$$非一致收斂，但因為不收斂的點$$m(\{1\})=0$$，因此為幾乎一致收斂。

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
