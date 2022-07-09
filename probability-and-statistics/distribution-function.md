# 分佈函數(distribution function)

## 累積分佈函數(cumulative distribution function, cdf)

> 對一隨機變數$$X$$​，定義其累積分佈函數(或簡稱為分佈函數)為：$$F_X(x)=\mathrm{P}(X \leq x) \in [0,1], ~ x \in \mathbb{R}$$

完全不同的機率空間，可能得到相同的分佈函數(分佈收斂，如中央極限定理)。

## 分佈函數的定義

> 函數$$F$$​在滿足以下條件時，稱為分佈函數：
>
> 1. $$0 \leq F(x) \leq 1, ~ \forall x \in \mathbb{R}$$​
> 2. $$F$$為非遞減函數 (non-decreasing function)
> 3. $$F$$​為右連續函數(cadlag function)
> 4. $$\displaystyle \lim_{x \rightarrow -\infty }F(x)=0$$且$$\displaystyle \lim_{x \rightarrow \infty }F(x)=1$$。

可得$$\mathrm{P}(a < X \leq b)  = \mathrm{P}(\{ X \leq b\} - \{X \leq a\})=\mathrm{P}(X \leq b) - P(X \leq a) = F(b)-F(a)$$

* $$\mathrm{P}(X=a)=F(x)$$之圖形在$$x=a$$跳躍的高度。
* $$\mathrm{P}(X > a)=1-F(a)$$​
* $$\mathrm{P}(X \geq a ) = 1-F(a) +\mathrm{P}(X=a)$$​
* $$\mathrm{P}(X \leq b) = F(b)$$​
* $$\mathrm{P}(X < b) = F(b)- \mathrm{P}(X=b)$$​
* $$\mathrm{P}(a < X \leq b) = F(b) - F(a)$$​
* $$\mathrm{P}(a < X <b) = F(b) -F(a) -\mathrm{P}(X=b)$$​
* $$\mathrm{P}(a \leq X \leq b) = F(b) -F(a) +\mathrm{P}(X=a)$$
* $$\mathrm{P}(a \leq X <b) = F(b) - F(a) + \mathrm{P}(X=a) - \mathrm{P}(X=b)$$

## 兩分佈函數相同

> 兩隨機變數$$X,Y$$​若滿足 $$\mathrm{P}(X \leq x) = \mathrm{P}(Y \leq x)~, \forall x \in \mathbb{R}$$，或寫成$$F_X(x)=F_Y(x), \forall x \in \mathbb{R}$$
>
> 則稱分佈相同(identically distributed)。



## 機率密度(質量)函數(probability density (mass) function)

> 令$$X$$​為一隨機變數，$$F_X$$為其分佈函數。
>
> 若函數$$f$$滿足以下兩條件，則為隨數變數之機率密度函數：
>
> * $$f(x) \geq 0, ~\forall x \in \mathbb{R}$$
> * $$\sum_{x} f(x)=1$$或$$\int_{-\infty}^{\infty} f(x)dx=1$$

#### 離散隨機變數

若$$X$$為離散型，則其機率密度函數$$f_X(x)=\mathrm{P}(X=x), ~ x \in \mathbb{R}$$。

* 在函數的定義中，可得函數上的跳躍點為可數個，而此集合為$$\mathrm{P}(X=x) >0$$的集合，稱為集合$$C$$​。
* 因此$$\forall x \in C, ~f_X(x) \neq 0$$​。
* 可得$$\mathrm{P}(A)=\mathrm{P}(X \in A) = \sum_{x \in A \cap C} f_X(x)$$且$$F_X(x) = \sum_{t \leq x, ~ t \in C} f_X(t), ~ x \in \mathbb{R}$$

#### 連續隨機變數

給定分佈函數$$F_X$$，則機率密度函數滿足以下條件(不唯一)： $$\displaystyle F_X(x) =\int_{-\infty}^x f_X(t) dt , ~ x \in \mathbb{R}$$。

因為分佈函數定義要求$$\displaystyle \lim_{x \rightarrow \infty} F_X(x)=1$$，因此機率密度函數還要滿足 $$\displaystyle \int_{-\infty}^{\infty} f_X(x)dx=1$$。

