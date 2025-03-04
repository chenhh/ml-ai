---
description: Radon-Nikodym derivative
---

# Lebesgue-Radon-Nikodym定理

## 簡介

Radon-Nikodym 導數定理的證明跟 Lebesgue 分解定理是非常接近的，有些書都是直接稱之為 Lebesgue-Radon-Nikodym-Legesgue 定理，而且是先證了 Lebesgue 分解定理，再推出 Radon-Nikodym 的結論。

由於通常使用正測度的積分定義一般測度(符號測度或複測度)，因此實值函數討論符號測度$$\nu$$相對於正測度$$\mu$$($$\nu \ll \mu$$)的絕對連續即可。(複值函數時才使用複測度)。

## Lebesgue分解

任意一個分佈函數都可以寫成一個離散型隨機變數、一個連續型隨機變數以及一個奇異型隨機變數的和，這就是Lebesgue分解定理，它更深刻地揭示了分佈函數的本質。

機率空間中的分佈函數$$F$$滿足三性質：

1. 單調性：$$F(x)$$單調遞增。
2. 有界性：$$0 \leq F(x) \leq 1$$。
3. 右連續性：$$F(x)$$右連續存在。

$$F$$<mark style="background-color:purple;">存在如下分解：</mark>$$F(x)=g_1(x)+g_2(x)+g_3(x)$$<mark style="background-color:purple;">，其中</mark>$$g_1$$<mark style="background-color:purple;">為絕對連續的單調遞增函數，</mark>$$g_2$$<mark style="background-color:purple;">為奇異函數，</mark> $$g_3$$<mark style="background-color:purple;">為階躍函數</mark>。

這並不是說任意一個隨機變數一定是這三種之一，比如說一個連續隨機變數+一個離散隨機變數所得的結果既不是連續型也不是離散型，只是說<mark style="background-color:purple;">一般的隨機變數可分解成這三類隨機變數的和</mark>。

## Radon-Nikodym 導數應用

$$\forall E \in \Sigma, \nu(E)=\int_E f d\mu$$。

把上式的函數$$f$$ 定義為測度$$\nu$$ 對於測度$$\mu$$ 的 Radon-Nikodym 微分(Radon-Nikodym Derivative of $$\nu$$ with respect to $$\mu$$ )，或者稱為測度$$\nu$$對於測度$$\mu$$的密度 (density of $$\nu$$ with respect to $$\mu$$)。記為$$f =\frac{d\nu}{d\mu}$$或記為$$d\nu=f d\mu$$。

Radon-Nikodym 微分是對 "絕對連續函數可以表示其導數的不定積分" 這一概念的廣義擴展。

唯一性：

若有$$d\nu = f d\mu$$，$$d\nu = g d\nu$$，由定義得$$\int (f-g)d\mu=0$$。因此$$f=g ~ \mu \text{ -a.e.}$$。

* 將在實數上機率理論(如機率密度函數)推廣為在測度空間上的測度論。
* 在金融數學上，將實際機率(actual probability) 轉換成 風險中性的機率(risk neutral probability)。
* 可用來導出在$$L^p, ~1\leq p \leq  \infty$$等空間上的 Riesz 表現定理。
* 物理中質量密度、電荷密度、能量密度等等，他們都是某個測量值和體積之比的極限。所謂密度，就是某個物理量在空間的分佈（從而可以看作測度)。
* Radon-Nikodym導數被叫做導數，是因為它滿足一般導數的鏈式法則。

## 可積分函數定義符號測度

給定可積空間$$(X,\Sigma)$$。

若$$\mu: \Sigma \rightarrow [0, \infty]$$為測度，$$f: X \rightarrow [-\infty,\infty]$$為$$\mu$$可積函數，即$$\displaystyle \int_E fd\mu < \infty$$(如果$$\mu(x)=\infty$$時，只要$$f(x)=0$$得$$\infty \cdot 0=0$$仍然可積)。

定義$$\displaystyle \nu(E)=\int_E f d\mu$$，則可得$$\nu$$為有限符號測度(因為$$\int f <\infty$$)，則$$\nu \ll \mu$$絕對連續。

常將上式寫為微分形式：$$d\nu = f d\mu$$。

<mark style="color:red;">也可推廣測度</mark>$$\mu$$<mark style="color:red;">為符號測度，但一般應用使用測度即可</mark>。

## 引理

> 給定可積空間$$(X,\Sigma)$$與有限測度$$\nu, \mu: \Sigma \rightarrow [0, \infty)$$。
>
> 則可得$$\nu \perp \mu$$或者$$\exists \epsilon > 0, ~ E \in \Sigma \ni \mu(E) >0$$且$$\nu (E) \geq \epsilon \mu(E)$$，即存在集合$$E$$為測度$$\nu-\epsilon \mu$$的正測集)。
>
>

## Lebesgue分解

> 令$$\mu, \nu$$為可測空間$$(X, \Sigma)$$上的σ-finite(符號)測度。
>
> 則存在唯一的σ-finite(符號)測度$$\nu_0, \nu_1$$滿足：
>
> 1. $$\nu=\nu_0 + \nu_1$$。(<mark style="color:red;">Lebesgue分解(decomposition</mark>)
> 2. $$\nu_0 \ll \mu$$ (絕對連續，即$$\forall E \in \Sigma, ~\mu(E)=0 \implies \nu_0(E)=0$$)
> 3. $$\nu_1 \perp \mu$$ (相互奇異(正交)，即$$\exists E, F \in \Sigma, E \cup F =X, E\cap F=\emptyset, \nu_1(E)=0, \mu(F)=0$$且$$E$$為$$\nu_1$$的零測集，$$F$$為$$\mu$$的零測集)。
>
> σ-finite $$\nu$$測度指的是對於任意可測分割$$\bigcup_{n=1}^\infty E_n = X$$，$$\nu(E_n) < \infty, ~\forall n$$，但$$\nu(X)$$可能為$$\infty$$。因此可得有限測度為σ有限測度的子集合。
>
> Radon–Nikodym–Lebesgue 定理把測度沿著 σ-有限測度分解為絕對連續部分與奇異部分，並給出絕對連續部分的分類。
>
> 有界變差函數可以在精確到加減常數的意義下唯一分解為一個絕對連續函數、一個奇異函數和一個跳躍函數的和。

step:

* 從$$\mu, \nu$$建構$$\nu_0$$使得$$\nu_0 \ll \mu$$。
* 驗證$$\nu - \nu_0 \perp \mu$$。

## 正測度非負函數積分為絕對連續的正測度

> $$(X, \Sigma)$$為可積空間，$$\mu: \Sigma \rightarrow [0, \infty]$$為正測度。
>
> 給定$$\mu$$可積的非負函數$$h: X \rightarrow [0,\infty]$$，定義集合函數$$\nu(E)=\int_E h d\mu, \forall E \in \Sigma$$，則：
>
> 1. $$\nu$$為正測度且$$\nu \ll \mu$$。
> 2. 任意$$\mu$$可測非負函數$$f:X \rightarrow [0,\infty]$$，可得$$\forall E \in \Sigma, ~ \int_E f d\nu = \int_E f\cdot h d\mu$$。
>
> 註： Radon-Nikodym 定理，則是此定義的逆命題。

## Radon-Nikodym定理

> $$(X, \Sigma)$$為可積空間，$$\mu: \Sigma \rightarrow [0, \infty]$$為 σ-有限正測度，$$\nu$$為任意測度(正測度/符號測度/複測度)，且$$\nu \ll \mu$$，則：
>
> 1. 存在$$\mu$$可測的函數$$f$$滿足$$\forall E \in \Sigma, ~ \nu(E)=\int_E f d \mu$$。
> 2. 若$$\forall E \in \Sigma, \nu(E)=\int_E g d\mu$$，則$$f=g \text { a. e. on } (\mu)$$。
>
> 幾乎所有的拓展都是圍繞測度$$\nu$$來進行的，而測度 $$\mu$$的條件則一直都是  σ-有限正測度。這個條件很重要，如果不滿足的話，Radon-Nikodym 定理是不成立的。
>
> 如果我們要求 Radon-Nikodym 定理中的函數$$f$$的值域有限，那麼測度$$\nu$$的σ-有限性也是必須的.。



### 範例：非σ-有限正測度不滿足Radon-Nikodym定理

考慮實數$$\mathbb{R}$$上的Borel集合$$\mathbb{B}$$ , 令$$\mu$$是($$\mathbb{R}, \mathbb{B})$$ 上的計數測度。可得$$\mu$$不是  σ-有限測度，因為有很多 Borel 集都不能寫成可數個有限集的聯集。

令$$\nu$$為Lebesgue測度($$\nu$$是  σ-有限測度)，可得$$\nu \ll \mu$$。因為$$\nu(E)=0 \implies E=\emptyset \implies \nu(E)=0$$。

如果Radon-Nikodym定理成立，則存在$$\mu$$可測函數$$f \ni \forall E \in \mathbb{B}, ~ \nu(E)=\int_E f d\mu$$。

令$$S=\{a\}, a \in \mathbb{R}$$為單點集。則$$\nu(S)=0$$。而$$\int_S f d\mu=f(a)$$。因此$$\forall a \in \mathbb{R}, f(a)=0$$，即Lebesgue測度$$\nu$$永遠等於0，與定義矛盾。

### 範例：非σ-有限正測度且函數的值域有限時不滿足Radon-Nikodym定理

$$\mu$$為有限正測度，$$\nu$$為正測度但不是  σ-有限測度。

令$$X=\{0\}$$，$$\mu(X)=1$$，$$\nu(X)=\infty$$。

則$$\mu(E) \implies E=\emptyset \implies \nu(E)=0 \implies \nu \ll \mu$$。

但是不存在函數的值域$$f(X) \in (-\infty, \infty)$$滿足 Radon-Nikodym 定理；但是如果允許$$f(x)=\infty$$ 則可以。

## 參考資料

* [https://en.wikipedia.org/wiki/Lebesgue%27s\_decomposition\_theorem](https://en.wikipedia.org/wiki/Lebesgue's_decomposition_theorem)
* [http://www.scu.edu.tw/math/Chieping/n.5-dimension/calculus-on-measure.html](http://www.scu.edu.tw/math/Chieping/n.5-dimension/calculus-on-measure.html)
* [https://www.colorado.edu/amath/sites/default/files/attached-files/lebesgue\_decomp.pdf](https://www.colorado.edu/amath/sites/default/files/attached-files/lebesgue_decomp.pdf)
* [https://zhuanlan.zhihu.com/p/80783917](https://zhuanlan.zhihu.com/p/80783917)
* [https://zhuanlan.zhihu.com/p/388395062](https://zhuanlan.zhihu.com/p/388395062)
* [https://zhuanlan.zhihu.com/p/526492250](https://zhuanlan.zhihu.com/p/526492250)
* [https://zhuanlan.zhihu.com/p/37493234](https://zhuanlan.zhihu.com/p/37493234)
* [https://zhuanlan.zhihu.com/p/74308890](https://zhuanlan.zhihu.com/p/74308890)
