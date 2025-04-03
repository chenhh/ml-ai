# 分佈函數(distribution function)

## 累積分佈函數(cumulative distribution function, cdf)

> 對一隨機變數$$X$$​，定義其累積分佈函數(或簡稱為分佈函數)為：$$F_X(x)=\mathrm{P}(X \leq x) \in [0,1], ~ x \in \mathbb{R}$$
>
> 可表示為$$\displaystyle F(x) = \begin{cases} & \sum_{x_i \leq x} f(x_i), ~ \text{ 離散r.v. } \\ & \int_{-\infty}^x f(x) dx , ~ \text{ 連續r.v. } \end{cases}$$

當$$X$$為連續隨機變數時，cdf$$F(X)$$與機率密度函數(pdf)$$f(x)$$之間的關係為$$dF(x)/dx=f(x)$$。

當$$X$$為離散隨機變數時，cdf$$F(X)$$與機率質量函數(pmf)$$f(x)$$之間的關係：令$$x_1 < x_2 < \dots <x_k$$為$$X$$的有限個相異取值，可得$$F(x_1) = f(x_1)$$，且$$\Delta F(x_i) = F(x_i) - F(x_{i-1})=f(x_i), ~ i=2,\dots, k$$。

<mark style="color:red;">完全不同的機率空間，可能得到相同的分佈函數(分佈收斂，如中央極限定理)</mark>。

簡單的說，因為$$\mathrm{P}(X \leq x)$$中包含了$$\mathrm{P}(X=x)$$的機率，因此分佈函數必為右連續。

## 分佈函數

> 函數$$F: \mathbb{R} \rightarrow [0,1]$$​在滿足以下條件時，稱為分佈函數：
>
> 1. $$0 \leq F(x) \leq 1, ~ \forall x \in \mathbb{R}$$​
> 2. $$F$$為非遞減函數 (non-decreasing function)
> 3. $$F$$<mark style="color:red;">​為右連續函數(cadlag function)，即</mark>$$\displaystyle \lim_{\delta \to 0}F(x-\delta) \neq F(x) = \lim_{\delta \to 0}F(x+\delta)$$<mark style="color:red;">或</mark>$$\displaystyle F(x-) \neq F(x) = F(x+)$$<mark style="color:red;">(當</mark>$$X$$<mark style="color:red;">為連續隨機變數時，</mark>$$F$$<mark style="color:red;">為連續函數(左/右均連續)，而</mark>$$X$$<mark style="color:red;">為離散隨機變數時，</mark>$$F$$<mark style="color:red;">只需滿足右連續函數即可)。</mark>
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

### 分佈函數為右連續函數(cadlag)

> 令$$(M,d)$$​為度量空間，集合$$E \subseteq \mathbb{R}$$。
>
> 函數$$f: E \rightarrow M$$若滿足以下條件時，稱為右連左極函數：$$\forall a \in E$$
>
> * 左極限存在 $$\displaystyle f(a-)=\lim_{x \rightarrow a-}f(x)$$ ( 通常和$$f(a)$$有跳躍，只有連續時才會等於$$f(a)$$)
> * 右極限存在且等於$$f(a)$$，$$f(a+)=\lim_{x \rightarrow a+} f(x) = f(a)$$

<mark style="color:red;">cadlag指定義在實數集或其子集上的處處右連續且有左極限的函數</mark>。這類函數在研究有跳躍甚至是需要跳躍的隨機過程時很重要，這類隨機過程不像布朗運動具有連續的樣本軌道。

CDF 定義為$$F(x)=\mathrm{P}(X \leq x)$$，這意味著我們考慮的是隨機變數$$X$$小於或等於某個值$$x$$的機率。根據這個定義，當我們考慮$$x$$從右側趨近於某一點時（即$$x \to c+$$），事件$$X \leq x$$ 的機率應該逐漸收斂到$$\mathrm{P}(X \leq c)$$。這正好對應了右連續性的要求。即$$\displaystyle \lim_{x \to c+} F(x) = F(c)$$。

<mark style="color:red;">如果分佈函數不滿足右連續性，就會導致邏輯上的矛盾</mark>。例如，如果$$F​(x)$$ 在某點$$c$$處不右連續，則可能會出現當$$x$$從右側接近$$c$$時，$$F​(x)$$的值不等$$F​(c)$$，這會使得$$\mathrm{P}(X \leq c)$$的計算結果不一致，違反定義。

對於離散型隨機變數，分佈函數是階梯函式（step function）。在每一個可能的取值點$$x_k$$，分佈函數會發生跳躍，且跳躍的高度等於該點的機率質量$$\mathrm{P}(X=x_k)=F(x_k) - F(x_k^-)$$，因此分佈函數在每個跳躍點是右連續。

而連續型隨機變數，因為分佈函數為積分形式，積分的定義本身保證了當$$x$$從右側接近某一點時，積分值會收斂到該點的函式值，因此為右連續。

### 為什麼不是左連續？

原因在於分佈函數的定義中使用了「小於或等於」（≤）的符號。這個符號自然地導致了右連續性。如果們改用「小於」（<）來定義分佈函數，即 $$F(x)=\mathrm{P}(X<x)$$，那麼 CDF 將會是左連續的。

然而，這樣的定義會導致一些不便：

* 它不符合傳統的分佈函數定義。
* 在處理離散型隨機變數時，分佈函數的跳躍點會變得難以解釋。

因此，右連續性成為了標準選擇。

### 參考資料

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

## 分位函數(quantile function)

> 分佈函數的分位函數為$$F^{-1}(x)=\inf\{t \in \mathbb{R} ~| ~ F(t) \geq x \}, ~ x \in (0,1)$$。

* 即使分佈函數$$F$$​不一定連續，也不一定嚴格遞增，但$$F^{-1}$$​必定存在。
* 如若分佈函數$$F$$​連續且嚴格遞增，則$$F^{-1}(x)$$​滿足$$F(t)=x$$​唯一的$$t$$​，此時與一般反函數定義相同。

### 基本性質

> 令$$F^{-1}$$​為分佈函數之分位函數。
>
> * $$\forall x, t \in \mathbb{R}$$, $$F^{-1}(x) \leq t \Leftrightarrow x \leq F(t)$$
> * $$F^{-1}$$​為非遞減且左連續的函數
> * 若$$F$$​為連續函數，則$$F(F^{-1}(x))=x, \forall \in (0,1)$$

### 分位函數抽樣定理

> 令$$F$$​為分佈函數，且隨機變數$$U \sim U(0,1)$$，則$$X=F^{-1}(U)$$以$$F$$​為分佈函數。

proof:

$$\mathrm{P}(X \leq t) = \mathrm{P}(F^{-1}(U) \leq t) = \mathrm{P}(U \leq F(t)) = F(t)$$(QED)

