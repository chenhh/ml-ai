# 隨機變數（random variable）

## 隨機變數（r.v.）

> 隨機變數是一個由樣本空間$$\Omega$$映射至實數集$$\mathbb{R}$$的實函數（real-valued function）。
>
> * 以函數的定義，隨機變數$$X$$的值$$x \in \mathbb{R}$$的前像$$X^{-1}(x) = \{ \omega \in \Omega | X(\omega) = x\}$$為一個在樣本空間$$\Omega$$的事件$$E$$。
> * 而在測度論中，要求事件$$E$$必須為sigma-field $$\mathcal{F}$$的元素，此時$$X$$稱為可測函數（measurable function）。

隨機變數依值域可分為：

* 連續隨機變數：若隨機變數之值為實區間上之任意部份集合，則稱之。
* 離散隨機變數：若隨機變數之發生值為有限或無限可數，則稱之。

## 單變數隨機變數

> 隨機變數$$X$$在區間$$(a,b]$$發生的機率為$$P(a< X \leq b) = P(\omega \in \Omega | X(\omega) \in (a,b] )$$，則分佈函數（distribution function）為 $$F(x) = P(X \leq x)$$。

## 分佈函數（distribution function）

$$F(x)$$為隨機變數$$X$$的分佈函數，則

* $$ 0 \leq F(x) \leq 1$$
* $$F(x)$$為非遞減（non-decreasing）函數。
* $$\lim_{h \rightarrow 0} F(x+h) = F(x)$$, 則稱$$F(x)$$為右連續（right continuous）函數。
* $$\lim_{x \rightarrow \infty} F(x)=1$$且 $$\lim_{x \rightarrow 0} F(x) = 0 $$
* $$P(a < X \leq b) = F_X(b) - F_X(a)$$ 

## 機率密度（質量）函數（probability density \(mass\) function）

如果離散隨機變數$$X$$，定義機率質量函數\(pmf\)$$P(x_i)\equiv P(X=x_i) \equiv P(\{ \omega \in \Omega | X(\omega \in x_i\})$$且滿足

* $$P(x_i ) \geq 0$$
* $$\sum_{x_i}P(x_i) =1$$

連續隨機變數的機率密度函數\(pdf\)$$f(x) = \frac{dF(x)}{dx}$$且滿足

* $$f(x) \geq 0$$, $$x \in \mathbb{R}$$
* $$\int_{-\infty}^{\infty} f(x)dx=1$$

## 期望值

* 離散隨機變數$$X$$的pmf為 $$P(X=x_i) =p_i, \ i \in \mathbb{N}$$。若$$\sum_{i=1}^{\infty} |x_i| p_i < \infty$$\(有限值時\)，則$$X$$的期望值為$$\operatorname{E}(X) \equiv \sum_{i=1}^{\infty} x_i p_i$$
* 連續隨機變數的pdf為$$f(x), \forall x \in \mathbb{R}$$，若$$ \int_{-\infty}^{\infty}|x|f(x) < \infty$$，則期望值為$$\operatorname{E}(X) \equiv  \int_{-\infty}^{\infty} x f(x)dx$$
* 而pdf期望值的Stieltjes積分形式為 $$\operatorname{E}(X) \equiv\int_{-\infty}^{\infty} xdF(x)$$

## Theorem

> 若$$\int_{-\infty}^{\infty} |g(x)|dF(x) < \infty$$，則$$\operatorname{E}(g(X))$$存在且$$\operatorname{E}(g(X))= \int_{-\infty}^{\infty}g(x)dF(x)$$

## Theorem：加法算子與期望值算子的交換性

> * $$X_1, X_2,\ldots$$為非負值的隨機變數，則 $$\operatorname{E}( \sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty} \operatorname{E}(X_i)$$
> * 對任意的$$X_1, X_2, \ldots$$，若$$\sum_{i=1}^{\infty} \operatorname{E}(|X_i|) < \infty$$，則$$\operatorname{E}(\sum_{i=1}^{\infty} X_i)= \sum_{i=1}^{\infty}\operatorname{E}(X_i)$$

## 變異數（variance）

> $$\operatorname{V}(X)=\operatorname{E}(X- \operatorname{E}(X))^2= E(X^2) - (E(X))^2$$

常用$$\mu, \sigma^2$$表示隨機變數$$X$$的期望值與變異數。

