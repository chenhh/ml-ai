# 關聯結構\(copula\)

## 簡介

我們希望能夠建構適合描述多維度隨機變數的聯合分佈。多元常態分佈是文獻最常出現的多維度機率模式，然而許多現象卻非常態分佈所能描述。

以存活變數的邊際分佈的特性而論，存活變數通常具偏斜\(skewed\)分佈，不具有對稱性。期望值與變異數是常態分佈最重要的參數，然而動差容易受少部份的極端值影響，並不太適合用來描述偏斜的存活函數。

Copula的概念是Sklar，在1959年研究多維分佈函數與低維邊際函數之間的關係的問題時首次引入。優點：

* Copula是一種研究相依性測度的方法  。
* Copula是作為研究無標度（scale-free）依賴度量的一種方法  。
* Copula作為構造二維分佈族的起點，可用於多元模型分佈與隨機模擬。 

### 分佈函數\(distribution function\)

> 邊際分佈函數（marginal distribution function）
>
> * $$F(x)=\mathrm{P}(X \leq x) \in [0,1]$$
> * $$G(y) = \mathrm{P}(Y \leq y) \in [0,1]$$
>
> 聯合分佈函數（joint distribution function）
>
> * $$H(x,y)=\mathrm{P}(X \leq x, Y \leq y) \in [0,1]$$
> * $$F(x)=\int_{y \in \mathbb{Y}} H(x,y)dy$$
> * $$G(y) = \int_{x \in \mathbb{X}}H(x,y) dx$$





