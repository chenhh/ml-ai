---
description: Radon-Nikodym derivative
---

# Lebesgue-Radon-Nikodym定理

## Radon-Nikodym 導數應用

* 將在實數上機率理論(如機率密度函數)推廣為在測度空間上的測度論。
* 在金融數學上，將實際機率(actual probability) 轉換成 風險中性的機率(risk neutral probability)。
* 可用來導出在$$L^p, ~1\leq p \leq  \infty$$等空間上的 Riesz 表現定理。
* 物理中質量密度、電荷密度、能量密度等等，他們都是某個測量值和體積之比的極限。所謂密度，就是某個物理量在空間的分佈（從而可以看作測度)。
* Radon-Nikodym導數被叫做導數，是因為它滿足一般導數的鏈式法則。

## Lebesgue分解

任意一個分佈函數都可以寫成一個離散型隨機變數、一個連續型隨機變數以及一個奇異型隨機變數的和，這就是Lebesgue分解定理，它更深刻地揭示了分佈函數的本質。

機率空間中的分佈函數$$F$$滿足三性質：

1. 單調性：$$F(x)$$單調遞增。
2. 有界性：$$0 \leq F(x) \leq 1$$。
3. 右連續性：$$F(x)$$右連續存在。

$$F$$存在如下分解：$$F(x)=g_1(x)+g_2(x)+g_3(x)$$ ,其中$$g_1$$為絕對連續的單調遞增函數，$$g_2$$為奇異函數， $$g_3$$為階躍函數。

這並不是說任意一個隨機變數一定是這三種之一，比如說一個連續隨機變數+一個離散隨機變數所得的結果既不是連續型也不是離散型，只是說一般的隨機變數分解成這三類隨機變數的和。

## 可積分函數定義符號測度

給定可積空間$$(X,\Sigma)$$。

若$$\mu: \Sigma \rightarrow [0, \infty]$$為測度，$$f: X \rightarrow [-\infty,\infty]$$為$$\mu$$可積函數，即$$\displaystyle \int_E fd\mu < \infty$$。

定義$$\displaystyle \nu(E)=\int_E f d\mu$$，則可得$$\nu$$為符號測度，則$$\nu \ll \mu$$絕對連續。

常將上式寫為微分形式：$$d\nu = f d\mu$$。

<mark style="color:red;">也可推廣測度</mark>$$\mu$$<mark style="color:red;">為符號測度，但一般應用使用測度即可</mark>。

## 引理

> 給定可積空間$$(X,\Sigma)$$與有限測度$$\nu, \mu: \Sigma \rightarrow [0, \infty)$$。
>
> 則可得$$\nu \perp \mu$$或者$$\exists \epsilon > 0, ~ E \in \Sigma \ni \mu(E) >0$$且$$\nu (E) \geq \epsilon \mu(E)$$，即存在集合$$E$$為測度$$\nu-\epsilon \mu$$的正測集)。
>
>

## Lebesgue-Radon-Nikodym定理

> 令$$\mu, \nu$$為可測空間$$(X, \Sigma)$$上的σ-finite測度。
>
> 則存在唯一的σ-finite測度$$\nu_0, \nu_1$$滿足：
>
> 1. $$\nu=\nu_0 + \nu_1$$。(<mark style="color:red;">Lebesgue分解(decomposition</mark>)
> 2. $$\nu_0 \ll \mu$$ (絕對連續，即$$\forall E \in \Sigma, ~\mu(E)=0 \implies \nu_0(E)=0$$)
> 3. $$\nu_1 \perp \mu$$ (相互奇異(正交)，即$$\exists E, F \in \Sigma, E \cup F =X, E\cap F=\emptyset, \nu_1(E)=0, \mu(F)=0$$且$$E$$為$$\nu_1$$的零測集，$$F$$為$$\mu$$的零測集)。
>
> Radon–Nikodym–Lebesgue 定理把測度沿著 σ-有限測度分解為絕對連續部分與奇異部分，並給出絕對連續部分的分類。

## 參考資料

* [https://en.wikipedia.org/wiki/Lebesgue%27s\_decomposition\_theorem](https://en.wikipedia.org/wiki/Lebesgue's\_decomposition\_theorem)
* [http://www.scu.edu.tw/math/Chieping/n.5-dimension/calculus-on-measure.html](http://www.scu.edu.tw/math/Chieping/n.5-dimension/calculus-on-measure.html)
* [https://www.colorado.edu/amath/sites/default/files/attached-files/lebesgue\_decomp.pdf](https://www.colorado.edu/amath/sites/default/files/attached-files/lebesgue\_decomp.pdf)
* [https://zhuanlan.zhihu.com/p/80783917](https://zhuanlan.zhihu.com/p/80783917)
* [https://zhuanlan.zhihu.com/p/388395062](https://zhuanlan.zhihu.com/p/388395062)
* [https://zhuanlan.zhihu.com/p/526492250](https://zhuanlan.zhihu.com/p/526492250)
* [https://zhuanlan.zhihu.com/p/37493234](https://zhuanlan.zhihu.com/p/37493234)
* [https://zhuanlan.zhihu.com/p/74308890](https://zhuanlan.zhihu.com/p/74308890)
