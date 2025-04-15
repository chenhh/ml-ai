# Jarque-Bera檢定

## 簡介

根據資料的「偏態（Skewness）」與「峰度（Kurtosis）」檢定，於大樣本下適用。常見於經濟與金融分析。

## Jarque-Bera檢定

令$$n$$個樣本的$$k$$階中央動差為$$\displaystyle m_k = \frac{1}{n} \sum_{i=1}^n (x_i - \overline{x})^k, ~k=2,3,4$$

樣本偏度$$g_1 = \frac{m_3}{m_2^{3/2}}$$，常態分佈的$$\gamma_1=0$$

樣本(超)峰度$$g_2 = \frac{m_4}{m_2^2}$$ (有些定義為$$\gamma_2= \frac{m_4}{m_2^2}-3$$，以常態分佈的$$g_2=3$$做為基準值)

JB檢定：令$$X$$則常態分佈, 則三階與四階樣本動差為：

* $$\mathrm{E}(\gamma_1)\equiv g_1=0$$
* $$\mathrm{Var}(\gamma_1)=\frac{6(n-2)}{(n+1)(n+3)} \approx \frac{6}{n}$$
* $$\mathrm{E}(\gamma_2)\equiv g_2=\frac{3(n-1)}{(n+1)} \approx 3$$
* $$\mathrm{Var}(\gamma_2) = \frac{24n(n-2)(n-3)}{(n+1)^2 (n+3)(n+5)} \approx \frac{24}{n}$$

虛無假設$$H_0$$將$$g_1, g_2$$標準化後平方的統計量$$JB$$為：$$\displaystyle JB =  \left( \frac{\gamma_1}{\sqrt{6}{n}} \right)^2  +  \left( \frac{\gamma_2 - 3}{\sqrt{24}{n}} \right)^2  = \frac{n\gamma_1^2}{6} + \frac{n(\gamma_2 - 3)^2}{24} \sim \chi^2(2)$$

若$$H_0$$正確，在樣本數$$n$$夠大時，可得$$\gamma_1 \approx 0$$且$$\gamma_2 \approx 3$$。

JB統計量的定義表明，任何對此（偏度為0，峰度為3）的偏離都會使得JB統計量增加。

對於$$\gamma_1 \neq 0$$且$$\gamma_2 \neq 3$$的非常態分佈檢定力很高，但對於$$\gamma_1=0$$而$$\gamma_2 \neq 3$$的非常態分佈檢定力較弱。

小樣本時的修正統計量$$CJB$$如下：

$$\displaystyle  \begin{aligned} CJB & = \left(  \frac{\gamma_1}{\sqrt{\frac{6(n-2)}{(n+1)(n+3)}}}   \right)^2 + \left(  \frac{\gamma_2 - \frac{3(n-1)}{n+1}}{\sqrt{\frac{24n(n-2)(n-3)}{(n+1)^2(n+3)(n+5)}}}  \frac{}{} \right)^2 \\ & = \frac{\gamma_1^2 (n+1)(n+3)}{6(n-2)} + \frac{(n+1)^2(n+3)(n+5)(\gamma_2 - \frac{3(n-1)}{n+1})^2}{24n(n-2)(n-3)} \sim \chi^2(2)  \end{aligned}$$



### 參考資料

* [\[wikipedia\] Jarque-Bera test](https://en.wikipedia.org/wiki/Jarque%E2%80%93Bera_test)
* [曾郁婷。”小樣本的常態性檢定之探討”，碩士論文，數理科學研究所，真理大學，2008](https://hdl.handle.net/11296/wqssvk)。
* [_Jarque, Carlos M._](https://en.wikipedia.org/wiki/Carlos_Jarque)_; Bera, Anil K. (1987). "A test for normality of observations and regression residuals". International Statistical Review. 55 (2): 163–172._ [_doi_](https://en.wikipedia.org/wiki/Doi_\(identifier\))_:_[_10.2307/1403192_](https://doi.org/10.2307%2F1403192)_._ [_JSTOR_](https://en.wikipedia.org/wiki/JSTOR_\(identifier\)) [_1403192_](https://www.jstor.org/stable/1403192)_._
