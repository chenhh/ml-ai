# Littlewood, Egoroff, Lusin theorem

## Littlewood three principles \[[wiki](https://en.wikipedia.org/wiki/Littlewood's\_three\_principles\_of\_real\_analysis)]

> 1. 每個（可測）集合幾乎就是一些區間(interval)的有限聯集(有限和)；&#x20;
> 2. 每個（$$L^k$$可積的）函數幾乎就是連續函數；
> 3. 每個點態收斂的函數列幾乎就是一致收斂的。
>
> 實變函數就是為了說明這些“幾乎(almost)”的意義。

<figure><img src="../../.gitbook/assets/convergence-min.png" alt=""><figcaption><p>收斂的性質</p></figcaption></figure>

## 收斂的定義

### (處處)點態收斂(everewhere pointwise convergence)

> $$\forall x \in X, ~\forall \epsilon > 0 ~\exists n_0 \in \mathbb{N} \ni |f_n(x)-f(x)|< \epsilon ~ \forall n > n_0$$

* 點態收態是根據每一點$$x$$判定收斂，因此每一點收斂的速度都不相同($$f_n$$ 上每一點$$x$$的值域收斂值$$f(x)$$的速度不同)。
* 此處everywhere強調對於定義域$$x\in X$$的性質全部成立。

### (處處)一致(均勻)收斂(everywhere uniformly convergence)

> $$\displaystyle \forall \epsilon > 0, \exists n_0 \in \mathbb{N} \ni \sup_{x \in X}|f_n(x) - f(x)| < \epsilon$$

均勻收斂考慮的是全部集合內的點($$\forall x \in X$$)，因此每一點的收斂速度都相同。

### 幾乎處處(點態)收斂(almost everywhere convergence)

> $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~ \text{a.e.}$$，即$$\mu(\{x \in X ~|~ \lim_{n \rightarrow \infty} f_n(x) \neq f(x) \}) = 0$$
>
> $$\exists E_0 \in \Sigma, ~ \mu(E_0)=0 \ni \forall x \in X - E_0, ~ \forall \epsilon > 0 \exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x)|<\epsilon, \forall n \geq n_0$$

* 函數序列在兩者不相等的集合$$E_0$$的測度為0，其餘的集合點態收斂&#x20;
* 一般函數而言，單點(可數)集合的測度為0，因此只要$$E_0$$為可數個點的集合均滿足此性質。

### 幾乎一致(均勻)收斂 (almost uniformly convergence)

> $$\displaystyle \forall \epsilon > 0,\exists E_0 \in \Sigma \ni \mu(E_0) < \epsilon \text{ and } f_n \rightarrow \text{ uniformly on } X - E_0$$

在測度為0的集合$$E_0$$之外，$$f_n$$一致收斂至$$f$$。



## Egoroff定理 (幾乎處處收斂在有限測度條件下為幾乎均勻收斂)

> 令$$\mu(X) <\infty$$為有限測度，則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{a.e.} \Rightarrow \lim_{n \rightarrow \infty} f_n(x) = f(x)~ \text{almost unif.}$$
>
> 註：(處處)的點態收斂無法得到一致收斂。

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
