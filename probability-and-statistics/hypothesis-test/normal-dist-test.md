# 常態分佈檢定

## Jarque and Bera檢定

令$$n$$個樣本的$$k$$階中央動差為$$\displaystyle m_k = \frac{1}{n} \sum_{i=1}^n (x_i - \overline{})^k, ~k=2,3,4$$

偏度$$\gamma_1 = \frac{m_3}{m_2^{3/2}}$$，常態分佈的$$\gamma_1=0$$

峰度$$\gamma_2 = \frac{m_4}{m_2^2}$$ (有些定義為$$\gamma_2= \frac{m_4}{m_2^2}-3$$，因為常態分佈的$$g_2=3$$做為基準值)

JB檢定：令$$X$$則常態分佈：

* $$\mathrm{E}(\gamma_1)=0$$
* $$\mathrm{Var}(\gamma_1)=\frac{6(n-2)}{(n+1)(n+3)} \approx \frac{6}{n}$$
* $$\mathrm{E}(\gamma_2)=\frac{3(n-1)}{(n+1)} \approx 3$$
* $$\mathrm{E}(\gamma_2) = \frac{24n(n-2)(n-3)}{(n+1)^2 (n+3)(n+5)} \approx \frac{24}{n}$$

虛無假設$$H_0$$將$$\gamma_1, \gamma_2$$標準化後平方的統計量$$JB$$為：$$\displaystyle JB =  \left( \frac{\gamma_1}{\sqrt{6}{n}} \right)^2  +  \left( \frac{\gamma_2 - 3}{\sqrt{24}{n}} \right)^2  = \frac{n\gamma_1}{6} + \frac{n(\gamma_2 - 3)^2}{24} \sim \chi^2(2)$$

若$$H_0$$正確，則$$\gamma_1 \approx 0$$且$$\gamma_2 \approx 3$$。

對於$$\gamma_1 \neq 0$$且$$\gamma_2 \neq 3$$的非常態分佈檢定力很高，但對於$$\gamma_1=0$$而$$\gamma_2 \neq 3$$的非常態分佈檢定力較弱。

## Geary檢定

## D'Agostino D檢定
