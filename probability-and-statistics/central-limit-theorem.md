# 中央極限定理\(CLT\)

一旦隨機樣本的分佈為未知或不是常態分佈時，分析某個統計量或估計式的實際分佈並不是一件容易的事。在此情形下，一種方便的方式是分析統計量的極限行為，並設法推導出其在極限上的分佈。

## 大數法則\(\(law of large numbers\)

> $$(\Omega, \mathcal{F}, \mathrm{P})$$為一機率空間，$$X, X_1, X_2, \ldots$$為定義在$$\Omega$$的實值隨機函數。
>
> 令$$S_n=\sum_{i=1}^n X_i, ~~A_n = \frac{S_n}{n}$$
>
> *  則$$X_1,X_2, \ldots$$滿足強大數法則 $$\Leftrightarrow$$$$\displaystyle\mathrm{P} (\lim_{n \rightarrow \infty} X_n =X)=1$$，即$$X_n$$幾乎確定收斂至$$X$$。
> *  則$$X_1,X_2, \ldots$$滿足弱大數法則 $$\Leftrightarrow$$$$\displaystyle \forall \epsilon >0 , ~ \lim_{n \rightarrow \infty} \mathrm{P} ( |X_n -X| > \epsilon)=0$$，即$$X_n$$機率收斂至$$X$$。

## 中央極限定理 \(central limit theorem\) 

不論隨機樣本原來的分佈為何，在樣本數$$N$$足夠大時，將**樣本平均數標準化**後所得新統計量的分佈會非常接近於標準常態分佈。\(但隨機樣本必須具有有限變異數\)。

$$\{X_1,X_2,⋯,X_N \}$$為獨立同分佈（i.i.d.）的隨機變數（可為任意分佈）， 其共同平均數為$$\mu$$,  共同變異數為$$ \sigma^2$$，則

$$\forall c > 0$$, $$\displaystyle \lim_{N \rightarrow 0} \mathrm{P}\bigg( \frac{\sqrt{N} (\overline{X}_N-\mu) }{\sigma} \leq c\bigg) = \Phi(c)$$

其中$$\Phi(c)$$為標準常態分佈的累積分佈函數。

也寫成 $$\bigg( \frac{\sqrt{N} (\overline{X}_N-\mu) }{\sigma} \bigg) \xrightarrow {A} N(0,1)$$

**若隨機樣本沒有有限變異數，則不適用中央極限定理**。 



