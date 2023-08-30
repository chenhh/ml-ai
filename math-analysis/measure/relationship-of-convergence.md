# 收斂的定義與關係

## Littlewood three principles \[[wiki](https://en.wikipedia.org/wiki/Littlewood's\_three\_principles\_of\_real\_analysis)]

> 1. 每個（可測）集合幾乎就是一些區間(interval)的有限聯集(有限和)；&#x20;
> 2. 每個（$$L^k$$可積的）函數幾乎就是連續函數；
> 3. 每個點態收斂的函數列幾乎就是一致收斂的。
>
> 實變函數就是為了說明這些“幾乎(almost)”的意義。

## 函數序列收斂關係

測度$$\mu: E \rightarrow [0, \infty]$$，因此要考慮有限或無限測度的條件。

* <mark style="color:blue;">\[</mark>[<mark style="color:blue;">證明</mark>](convergence-ae.md#ji-hu-chu-chu-yi-zhi-shou-lian-bao-zheng-ji-hu-chu-chu-shou-lian)<mark style="color:blue;">]在有限或無限測度空間時，幾乎一致收斂的定義可得幾乎處處收斂</mark><mark style="color:red;">。</mark>
* <mark style="color:red;">\[</mark>[<mark style="color:red;">證明</mark>](relationship-of-convergence.md#egoroff-ding-li-ji-hu-chu-chu-shou-lian-zai-you-xian-ce-du-tiao-jian-xia-wei-ji-hu-yi-zhi-shou-lian)<mark style="color:red;">]如果為有限測度空間時，Egoroff定理證明了幾乎處處收斂可保證幾乎一致收斂</mark>。
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

> $$\displaystyle \forall \epsilon > 0,\exists E_\epsilon \in \Sigma \ni \mu(E_\epsilon) < \epsilon \text{ and } f_n \rightarrow f \text{ uniformly on } E - E_\epsilon$$

在測度小於$$\epsilon$$的集合$$E_\epsilon$$之外，$$f_n$$一致收斂至$$f$$。
