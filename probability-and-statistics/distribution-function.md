# 分佈函數(distribution function)

## 累積分佈函數(cumulative distribution function, cdf)

> 對一隨機變數$$X$$​，定義其累積分佈函數(或簡稱為分佈函數)為：$$F_X(x)=\mathrm{P}(X \leq x) \in [0,1], ~ x \in \mathbb{R}$$

完全不同的機率空間，可能得到相同的分佈函數(分佈收斂，如中央極限定理)。

## 分佈函數

> 函數$$F: \mathbb{R} \rightarrow [0,1]$$​在滿足以下條件時，稱為分佈函數：
>
> 1. $$0 \leq F(x) \leq 1, ~ \forall x \in \mathbb{R}$$​
> 2. $$F$$為非遞減函數 (non-decreasing function)
> 3. $$F$$​為<mark style="color:red;">右連續函數(cadlag function) (此性質可由CDF原始定義推出)</mark>
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

### 分佈函數為右連續函數

<mark style="color:red;">cadlag指定義在實數集或其子集上的處處右連續且有左極限的函數</mark>。這類函數在研究有跳躍甚至是需要跳躍的隨機過程時很重要，這類隨機過程不像布朗運動具有連續的樣本軌道。

> 令$$(M,d)$$​為度量空間，集合$$E \subseteq \mathbb{R}$$。
>
> 函數$$f: E \rightarrow M$$若滿足以下條件時，稱為右連左極函數：$$\forall a \in E$$
>
> * 左極限存在 $$\displaystyle f(a-)=\lim_{x \rightarrow a-}f(x)$$ ( 通常和$$f(a)$$有跳躍，只有連續時才會等於$$f(a)$$)
> * 右極限存在且等於$$f(a)$$，$$f(a+)=\lim_{x \rightarrow a+} f(x) = f(a)$$



#### 參考資料

* [\[wikipedia\] cadlag function](https://zh.wikipedia.org/wiki/%E5%8F%B3%E8%BF%9E%E5%B7%A6%E6%9E%81%E5%87%BD%E6%95%B0).
* [\[math exchange\] Proving a CDF is cadlag](https://math.stackexchange.com/questions/3801342/proving-a-cdf-is-cadlag)
* [https://christophborgers.com/cadlag-property-of-distribution-functions](https://christophborgers.com/cadlag-property-of-distribution-functions)

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

