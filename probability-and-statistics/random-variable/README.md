# 隨機變數（random variable）

## 機率空間(probability space)

<mark style="color:red;">機率空間</mark> $$(\Omega, \mathcal{F}, \mathrm{P})$$ 包含三個元素：

<mark style="color:red;">樣本空間</mark> $$\Omega =\{\omega_a, ~ a \in A\}$$為所有可能發生的結果(outcome) $$\omega_a$$形成的集合，$$A$$為結果的指標集合(可數或不可數)。

<mark style="color:red;">σ域</mark> $$\mathcal{F}$$為樣本空間$$\Omega$$特定子集合形成的集合族(family of set)，其內部的元素 (集合)必須滿足以下三個性質：

* \[宇集合為σ域的元素] $$\Omega \in \mathcal{F}$$。
* \[補集為σ域的元素]$$E \in \mathcal{F} \Rightarrow E^c \in \mathcal{F}$$。
* \[可數集合聯集為σ域的元素] $$\displaystyle E_i \in \mathcal{F} ~ i \in \mathbb{N} \Rightarrow \bigcup_{i=1}^\infty E_i \in \mathcal{F}$$。

<mark style="color:red;">機率測度</mark> $$\mathrm{P}: \mathcal{F} \rightarrow [0,1]$$必須滿足以下三個性質：

* $$\mathrm{P}(E) \geq 0, ~ \forall E \in \mathcal{F}$$
* \[**有限測度**] $$\mathrm{P}(\Omega)= 1$$
* \[可數可加性] $$E_i \in \mathcal{F}, i \in \mathbb{N}$$且$$E_i \cap E_j = \emptyset, ~ \forall i \neq j$$，則$$\displaystyle \mathrm{P}(\bigcup_{i=1}^\infty E_i) = \sum_{i=1}^\infty \mathrm{P}(E_i)$$

## 隨機變數（random variable）

> 隨機變數是一個由樣本空間$$\Omega$$(但不是$$\Omega$$的任意集合，而是σ-field)映射至實數集$$\mathbb{R}$$的實函數（real-valued function）。
>
> * 以函數的定義，隨機變數$$X$$的值$$x \in \mathbb{R}$$的前像$$X^{-1}(x) = \{ \omega \in \Omega | X(\omega) = x\}$$為一個在樣本空間$$\Omega$$的事件$$E$$。
> * 而在測度論中，要求事件$$E$$必須為σ-field $$\mathcal{F}$$的元素，此時$$X$$稱為$$\mathcal{F}$$-可測函數（measurable function）。
> * $$X$$ 必須是可測函數，是為了避免在實數上任一點(或區間)的前像不存在於$$\mathcal{F}$$ 中沒有定義；反之如果$$X$$ 為可測函數，因為在$$\mathbb{R} >$$​中所有點的前像均存在於$$\mathcal{F}$$​，因此在求積分值的時候切割$$\mathbb{R}$$找對應的前像$$X^{-1}([a,b])$$​必為$$\mathcal{F}$$​的元素，因此可求值。
> * 把$$X$$在$$\Omega$$上的Lebesgue積分 $$\displaystyle \mathrm{E}(X)= \int_\Omega X d\mathrm{P}$$稱為$$X$$的期望值。

可測隨機變數$$X$$ 必須滿足任意實現值$$x$$的前像$$E \equiv X^{-1}(x)(\omega)$$必須是σ域的元素，是由值域反向要求定義域的特性。 而宇集合$$\Omega$$中任意元素的組合均可以得到事件集合$$E$$，而此集合對於$$X$$不一定可測。

不可測隨機變數通常須使用選擇性公理建構，而在一般的應用中的均為(可測)隨機函數。

隨機變數依值域可分為：

* 連續(continuous)隨機變數：若隨機變數之值為實區間上之任意部份集合，則稱之。
* 離散(discrete)隨機變數：若隨機變數之發生值為有限或無限可數，則稱之。

### 隨機變數的值可將前像的宇集合切割

> 定義隨機變數$$X$$的值$$x \in \mathbb{R}$$的前像$$E_x=X^{-1}(\{x\}) = \{ \omega \in \Omega | X(\omega) = x\}$$在樣本空間$$\Omega$$。
>
> * 互不相交性 ：若$$x \neq y$$，則$$E_x \cap E_y = \emptyset$$。
>   * 因為若存在$$\omega \in E_x \cap E_y$$，則$$X(\omega)=x$$且$$X(\omega)=y$$不符合函數的定義。
> * 全覆蓋性：所有$$E_x$$的聯集為$$\Omega$$，即$$\bigcup_{x \in \mathbb{R}}E_x =\Omega$$。
>   * 因為對於任意的$$\omega \in \Omega$$，$$X(\omega)$$必為某個$$x_0 \in \mathbb{R}$$，即$$\omega \in E_{x_0}$$。

若$$X$$ 是離散的（取值為可數集合 $$\{x_1, x_2, \dots\}$$ )，則 $$\Omega$$ 被分割為可數個互不相交的事件$$E_{x_1}, E_{x_2}, \dots,$$且：$$\mathrm{P}(X=x_i)=\mathrm{P}(E_{x_i})$$。$$\Omega = \bigcup_{i \in \mathbb{N}} X^{-1}(\{x_i\})$$。

若$$X$$是連續的（如常態分佈），則對所有單點$$x$$，$$\mathrm{P}(E_x ​ )=0$$。此時分割依然存在，但需通過更複雜的結構（如密度函式）描述機率分佈。通常可用區間切割$$X^{-1}([a,b))=\{\omega \in \Omega~|~ a \leq X(\omega) < b\}$$再聯集得到宇集合的畫分。

### 非隨機變數範例

$$\Omega=\{1,2,3,4\}$$，$$\mathcal{F}=\sigma(\{1,2\}, \{3\}, \{4\})$$

令$$X(1)=2, X(2)=3, X(3)=4, X(4)=5$$。

因為$$\{X \leq 2\}=\{1\} \notin \mathcal{F}$$，因此$$X$$不是$$\mathcal{F}$$可測的隨機變數。

令$$Y(1)=Y(2)=2, Y(3)=10, Y(4)=-500$$

因為：

* $$r< -500, ~\{Y \leq r\} = \emptyset \in \mathcal{F}$$
* $$-500 \leq r < 2, ~\{Y \leq r\} = \{4\} \in \mathcal{F}$$
* $$2 \leq r < 10, ~ \{Y \leq r\} = \{1,2,4\} \in \mathcal{F}$$
* $$r \geq 10\}, \{Y \leq r\} = \Omega \in \mathcal{F}$$

因此$$Y$$為$$\mathcal{F}$$可測的隨機變數。

## 單變數隨機變數

> 隨機變數$$X$$在區間$$(a,b]$$發生的機率為$$P(a< X \leq b) = P(\omega \in \Omega | X(\omega) \in (a,b] )$$，則<mark style="color:red;">分佈函數（distribution function）</mark>為 $$F(x) = P(X \leq x)$$。

連續隨機變數恰好等於某數值$$c$$的機率為0，即$$P(X=c)=0$$，因此$$P(a < x \leq b) = P(a < X < b)=(a \leq X<b)=P(a \leq X \leq b)$$

但離散隨機變數無此性質。

## 分佈函數（distribution function）

$$F(x)$$為隨機變數$$X$$的分佈函數，須滿足以下條件：

* $$0 \leq F(x) \leq 1$$
* $$F(x)$$為非遞減（non-decreasing）函數。
* $$\displaystyle \lim_{h \rightarrow 0} F(x+h) = F(x)$$, 則稱$$F(x)$$為右連續（right continuous）函數。
* $$\displaystyle \lim_{x \rightarrow \infty} F(x)=1$$且 $$\displaystyle \lim_{x \rightarrow 0} F(x) = 0$$
* $$P(a < X \leq b) = F_X(b) - F_X(a)$$

也可定義為$$F(x) = \mathrm{P}(X \leq x)$$

### 經驗分佈函數(empirical distribution)

> 令$$X_1, X_2, \ldots$$為一組隨機樣本, 以$$F$$為共同分佈函數。令 $$F_n(x)=\frac{X_i \leq x}{n}, ~ \forall x \in \mathbb{R}$$，則$$F_n$$稱為此組樣本之經驗分佈函數，為一階梯函數。

![經驗分佈函數](../../.gitbook/assets/empirical_dist-min.png)

```python
import numpy as np
from typing import Iterable
import matplotlib.pyplot as plt

def empirical_distribution(values: Iterable):
    ys = np.asarray(values)
    fig, ax = plt.subplots()
    n_bin = ys.size//10
    n, bins, patches = ax.hist(ys, bins=n_bin, density=True, 
        cumulative=True, label='empirical distribution')
    ax.set_ylabel('Frequency')
    ax.set_title('Probability')
    ax.legend()
    fig.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    values = np.random.randn(1000)
    empirical_distribution(values)
```

## 機率密度（質量）函數（probability density (mass) function）

如果離散隨機變數$$X$$，定義機率質量函數(pmf)$$P(x_i)\equiv P(X=x_i) \equiv P(\{ \omega \in \Omega | X(\omega \in x_i\})$$且滿足

* $$P(x_i ) \geq 0$$
* $$\displaystyle \sum_{x_i}P(x_i) =1$$

連續隨機變數的機率密度函數(pdf)$$f(x) = \frac{dF(x)}{dx}$$且滿足

* $$f(x) \geq 0$$, $$x \in \mathbb{R}$$
* $$\displaystyle \int_{-\infty}^{\infty} f(x)dx=1$$

![機率密度(質量)函數](../../.gitbook/assets/pmf-min.png)

```python
import numpy as np
from typing import Iterable
import matplotlib.pyplot as plt

def probability_mass_function(values: Iterable):
    ys = np.asarray(values)
    fig, ax = plt.subplots()
    n_bin = ys.size // 10
    n, bins, patches = ax.hist(ys, bins=n_bin, density=True, 
        cumulative=False, edgecolor='black', label='pmf')
    ax.set_ylabel('Frequency')
    ax.set_title('Probability')
    ax.legend(fontsize=24)
    fig.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    values = np.random.randn(1000)
    probability_mass_function(values)
```

## 期望值

* 離散隨機變數$$X$$的pmf為 $$P(X=x_i) =p_i, \ i \in \mathbb{N}$$。若$$\displaystyle \sum_{i=1}^{\infty} |x_i| p_i < \infty$$(有限值時)，則$$X$$的期望值為$$\displaystyle \mathrm{E}(X) \equiv \sum_{i=1}^{\infty} x_i p_i$$
* 連續隨機變數的pdf為$$f(x), \forall x \in \mathbb{R}$$，若$$\displaystyle \int_{-\infty}^{\infty}|x|f(x) < \infty$$，則期望值為$$\displaystyle \mathrm{E}(X) \equiv \int_{-\infty}^{\infty} x f(x)dx$$
* 而pdf期望值的Stieltjes積分形式為 $$\displaystyle \mathrm{E}(X) \equiv\int_{-\infty}^{\infty} xdF(x)$$
* 期望值的不偏估計式為 $$\displaystyle \hat{\mu_X} = \frac{1}{n} \sum_{i=1}^n x_i$$

### 隨機變數函數的期望值

> * $$\displaystyle \mathrm{E}(u(X))=\sum_{i=1}^\infty u(x_i) p_i$$
> * $$\displaystyle \mathrm{E}(u(X))=\int_{-\infty}^{\infty} u(x)f(x)dx$$

### 期望值為線性算子

> * $$\mathrm{E}(a_1X_1 + a_2 X_2 )=a_1 \mathrm{E}(X_1) + a_2 \mathrm{E}(X_2)$$
> * $$\displaystyle \mathrm{E}(\sum_{i=1}^n a_i X_i) = \sum_{i=1}^n a_i \mathrm{E}(X_i)$$
> * $$g_1, g$$為兩函數，若$$\mathrm{E}(g_1(X)), \mathrm{E}(g_2(X))$$存在，則$$\mathrm{E}( ag_1(X)+ bg_2(X)+c) = a\mathrm{E}(g_1(x)) + b \mathrm{E}(g_2(x))+c$$

### 期望值與單調函數的性質

$$g_1, g_2$$為兩函數，使得期望值$$\mathrm{E}(g_1(X)), \mathrm{E}(g_2(X))$$存在，則：

* $$\forall x \in \mathbb{R}, g_1(x) \geq 0 \Rightarrow \mathrm{E}(g_1(x)) \geq 0$$
* $$\forall x \in \mathbb{R}, g_1(x) \geq g_2(x) \Rightarrow \mathrm{E}(g_1(x)) \geq \mathrm{E}(g_2(x))$$
* $$\forall x \in \mathbb{R}, a \leq g_1(x) \leq b \Rightarrow a \leq \mathrm{E}(g_1(x)) \leq b$$

### 有界的隨機變數必存在期望值

> 隨機變數$$X$$稱為有界(bounded)若$$\exists M > 0 \ni \mathrm{P}(|X| \leq M ) = 1$$。

## Theorem

> 若$$\displaystyle \int_{-\infty}^{\infty} |g(x)|dF(x) < \infty$$，則$$\mathrm{E}(g(X))$$存在且$$\displaystyle\mathrm{E}(g(X))= \int_{-\infty}^{\infty}g(x)dF(x)$$

## Theorem：加法算子與期望值算子的交換性

> * $$X_1, X_2,\ldots$$為非負值的隨機變數，則 $$\displaystyle \operatorname{E}( \sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty} \operatorname{E}(X_i)$$
> * 對任意的$$X_1, X_2, \ldots$$，若$$\displaystyle \sum_{i=1}^{\infty} \operatorname{E}(|X_i|) < \infty$$，則$$\displaystyle\operatorname{E}(\sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty}\operatorname{E}(X_i)$$

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
