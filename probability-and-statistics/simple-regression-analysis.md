---
description: simple (linear) regression analysis
---

# 簡單迴歸分析

簡單線性迴歸方程式，指模式中僅包含一個應變數與一個自變數。 此處的「線性」指的是係數與自變數的關係為線性形式，而自變數可為高階次方($$x^n)或函數($$\log(x)\$$。

迴歸分析的目的是期望瞭解自變數的數值或改變量對於應變數產生(影響程度)的數值或改變量。

自關數與應變數的線性關係依Pearson相關係數可$$ho$$分為：負相關($$-1 \leq \rho < 0$$)，不相關($$ho =0$$), 正相關($$0 < \rho \leq 1$$)。

給定資料集$$\{ (Y_1, X_1), (Y_2, X_2), \dots, (Y_t, X_t) \dots (Y_N, X_N)\}$$，假設模型如下：

$$
Y_t = \beta_1 + \beta_2 X_t + \epsilon_t
$$

* $$Y_t$$：應變數(dependent variable)、被解釋變數、內生變數、反應變數、響應變數。為研究的目標變數，其取值可被觀測且隨自變數的變化而變化。
* $$X_t$$：自變數(independent variable），又稱獨立變數、解釋變數（explanatory variable）、外生變數。 可由研究者選擇、控制、研究，且能獨立變化而影響或引起其他變數變化的條件或因素。
* $$\epsilon_t$$：隨機干擾項(stochastic disturbance)、誤差項(error term)。
* $$\beta_1, \beta_2$$ 未知的迴歸係數。

注意:
* 自變數與應變數為相關關係(correlation)，不可推論為因果關係。
* 每組資料假設為獨立同分佈(i.i.d.)。

誤差項需滿足三大假設:

1. 常態性(Normality) : 若母體資料呈現常態分配(Normal Distribution)，則誤差項也會呈現同樣的分配。可採用常態機率圖(normal probability plot) 或Shapiro-Wilk常態性檢定做檢查。
2. 獨立性(Independency) : 誤差項之間應該要相互獨立，否則在估計迴歸係數時會降低統計的檢定力。可以藉由Durbin-Watson test來檢查。
3. 變異數同質性(Constant Variance) : 變異數若不相等會導致自變數無法有效估計依變數。可以藉由殘差圖(Residual Plot)來檢查。

如果樣本資料是依時間先後排項，則稱為<mark style="color:red;">時間序列(time-series)資料</mark>，下標$$t$$代表時間。 如果樣本資料是某個特定時間點，針定特定地區或群體的資料，稱為<mark style="color:red;">橫斷面(cross-section)資料</mark>，下標$$t$$代表觀察對象。 如果資料包含上述兩種性質時，須使用兩個下標$$i, t$$代表觀察對象與時間。 其中變數$$(Y_t, X_t)$$為可收集到的資料，但$$\epsilon_t$$無法觀察到，只能用模型計算得出。

### Libreoffice迴歸分析

{% embed url="https://help.libreoffice.org/6.4/zh-CN/text/scalc/01/statistics_regression.html?DbPAR=CALC" %}

設定回歸類型。有三種類型可用:

「線性回歸」: 找到一條形如「y = a·x + b」的直線, 其中「a」是斜率, b是與資料最匹配的截距。

「對數回歸」: 找到與資料最匹配的形如「y = a·ln(x) + b」的對數曲線, 其中「a」為斜率, b 為截距, ln(x) 為「x」的自然對數。

「冪回歸」: 找到形如「y = a·x^b」的冪曲線, 其中「a」是係數, b 是與資料最匹配的冪。
