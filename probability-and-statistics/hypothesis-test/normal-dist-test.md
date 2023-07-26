# 常態分佈檢定

## 簡介

常見的方法有：Jarque-Bera test , Kolmogorov-Smirnov test , Anderson-Darling test、Shapiro-Wilk test，Cramér-von-Mises test、相關係數檢定法(The probability plot correlation coefficient test)。

\[Das 16] 在進行任何正式的統計分析之前，評估資料的正態性是至關重要的。否則我們可能會得出錯誤的推斷和錯誤的結論。正態性可以通過視覺和正態性檢驗來評估。大多數統計軟體包都會自動生成PP圖和QQ圖。由於圖形檢驗非常主觀，所以強烈建議使用分析檢驗。然而。<mark style="color:red;">但是，當我們在回歸和/或實驗設計中測試殘差的正常性時，Shapiro-Wilk和Jarque-Bera檢驗都不合適。在這方面，我們建議使用重標動差檢驗</mark>。

\[Hernandez21] 判斷一個資料樣本是否來自常態分配的群體是統計學和資料分析中的一個常見做法。到目前為止，科學文獻中已經提出了幾十種檢驗正態性的方法。因此，出現的一個共同問題是。什麼是檢驗樣本正態性的最佳方法？本報告的第一部分簡要回顧了用於檢驗正態性的最重要的方法類型。然後，通過對過去30年中發表的幾種正態性測試的力量對比的調查，對55種最常見的方法進行了排名。這項分析的總冠軍是基於回歸的Shapiro-Wilk（SW）正態性檢驗。(排名見Table 2)。

### 相關文獻

* Keya Rani Das and A. H. M. R. Imon. "A brief review of tests for normality," pp. 5-12, Vol. 5.1, American Journal of Theoretical and Applied Statistics, 2016.
* <mark style="color:red;">Hugo Hernandez, "Testing for normality: what is the best method," Vol. 6, 2021-05, ForsChem Research Reports, 2021</mark>.

## Jarque and Bera檢定

令$$n$$個樣本的$$k$$階中央動差為$$\displaystyle m_k = \frac{1}{n} \sum_{i=1}^n (x_i - \overline{x})^k, ~k=2,3,4$$

樣本偏度$$g_1 = \frac{m_3}{m_2^{3/2}}$$，常態分佈的$$\gamma_1=0$$

樣本(超)峰度$$g_2 = \frac{m_4}{m_2^2}$$ (有些定義為$$\gamma_2= \frac{m_4}{m_2^2}-3$$，以常態分佈的$$g_2=3$$做為基準值)

JB檢定：令$$X$$則常態分佈, 則三階與四階樣本動差為：

* $$\mathrm{E}(\gamma_1)\equiv g_1=0$$
* $$\mathrm{Var}(\gamma_1)=\frac{6(n-2)}{(n+1)(n+3)} \approx \frac{6}{n}$$
* $$\mathrm{E}(\gamma_2)\equiv g_2=\frac{3(n-1)}{(n+1)} \approx 3$$
* $$\mathrm{E}(\gamma_2) = \frac{24n(n-2)(n-3)}{(n+1)^2 (n+3)(n+5)} \approx \frac{24}{n}$$

虛無假設$$H_0$$將$$g_1, g_2$$標準化後平方的統計量$$JB$$為：$$\displaystyle JB =  \left( \frac{\gamma_1}{\sqrt{6}{n}} \right)^2  +  \left( \frac{\gamma_2 - 3}{\sqrt{24}{n}} \right)^2  = \frac{n\gamma_1^2}{6} + \frac{n(\gamma_2 - 3)^2}{24} \sim \chi^2(2)$$

若$$H_0$$正確，在樣本數$$n$$夠大時，可得$$\gamma_1 \approx 0$$且$$\gamma_2 \approx 3$$。

JB統計量的定義表明，任何對此（偏度為0，峰度為3）的偏離都會使得JB統計量增加。

對於$$\gamma_1 \neq 0$$且$$\gamma_2 \neq 3$$的非常態分佈檢定力很高，但對於$$\gamma_1=0$$而$$\gamma_2 \neq 3$$的非常態分佈檢定力較弱。

小樣本時的修正統計量$$CJB$$如下：

$$\displaystyle  \begin{aligned} CJB & = \left(  \frac{\gamma_1}{\sqrt{\frac{6(n-2)}{(n+1)(n+3)}}}   \right)^2 + \left(  \frac{\gamma_2 - \frac{3(n-1)}{n+1}}{\sqrt{\frac{24n(n-2)(n-3)}{(n+1)^2(n+3)(n+5)}}}  \frac{}{} \right)^2 \\ & = \frac{\gamma_1^2 (n+1)(n+3)}{6(n-2)} + \frac{(n+1)^2(n+3)(n+5)(\gamma_2 - \frac{3(n-1)}{n+1})^2}{24n(n-2)(n-3)} \sim \chi^2(2)  \end{aligned}$$



### 參考資料

* [\[wikipedia\] Jarque-Bera test](https://en.wikipedia.org/wiki/Jarque%E2%80%93Bera\_test)
* [曾郁婷。”小樣本的常態性檢定之探討”，碩士論文，數理科學研究所，真理大學，2008](https://hdl.handle.net/11296/wqssvk)。
* [_Jarque, Carlos M._](https://en.wikipedia.org/wiki/Carlos\_Jarque)_; Bera, Anil K. (1987). "A test for normality of observations and regression residuals". International Statistical Review. 55 (2): 163–172._ [_doi_](https://en.wikipedia.org/wiki/Doi\_\(identifier\))_:_[_10.2307/1403192_](https://doi.org/10.2307%2F1403192)_._ [_JSTOR_](https://en.wikipedia.org/wiki/JSTOR\_\(identifier\)) [_1403192_](https://www.jstor.org/stable/1403192)_._

## Geary檢定

Ｇeary檢定對$$\gamma_1=0$$且$$\gamma_2 \neq 3$$而的非常態分佈檢定力較JB強。

### 參考資料

* Robert Charles. Geary,  "Testing for normality,"pp. 209-242, Vol. 34, No. 3/4, Biometrika, 1947 .
* Ralph B.D'Agostino and Bernard Rosman. "The power of Geary's test of normality," pp. 181-184, Vol. 61.1, Biometrika,1974.

## D'Agostino D檢定

