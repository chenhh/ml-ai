# 隨機變數（random variable）

## 隨機變數（r.v.）

> 隨機變數是一個由樣本空間$$\Omega$$映射至實數集$$\mathbb{R}$$的實函數（real-valued function）。
>
> * 以函數的定義，隨機變數$$X$$的值$$x \in \mathbb{R}$$的前像$$X^{-1}(x) = \{ \omega \in \Omega | X(\omega) = x\}$$為一個在樣本空間$$\Omega$$的事件$$E$$。
> * 而在測度論中，要求事件$$E$$必須為sigma-field $$\mathcal{F}$$的元素，此時$$X$$稱為可測函數（measurable function）。

隨機變數依值域可分為：

* 連續隨機變數：若隨機變數之值為實區間上之任意部份集合，則稱之。
* 離散隨機變數：若隨機變數之發生值為有限或無限可數，則稱之。

## 單變數隨機變數

> 隨機變數$$X$$在區間$$(a,b]$$發生的機率為$$P(a< X \leq b) = P(\omega \in \Omega | X(\omega) \in (a,b] )$$，則分佈函數（distribution function）為 $$F(x) = P(X \leq x)$$。

