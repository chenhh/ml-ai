# 中央極限定理(CLT)

一旦隨機樣本的分佈為未知或不是常態分佈時，分析某個統計量或估計式的實際分佈並不是一件容易的事。在此情形下，一種方便的方式是分析統計量的極限行為，並設法推導出其在極限上的分佈。

## 大數法則((law of large numbers)

> $$(\Omega, \mathcal{F}, \mathrm{P})$$為一機率空間，$$X, X_1, X_2, \ldots$$為定義在$$\Omega$$的實值隨機函數，且$$\mathrm{E}(X)=\mu$$存在。
>
> 令$$\overline{X}_n=\frac{1}{n}\sum_{i=1}^n X_i$$，
>
> * &#x20;則$$X_1,X_2, \ldots$$滿足強大數法則 $$\Leftrightarrow$$$$\displaystyle\mathrm{P} (\lim_{n \rightarrow \infty} \overline{X}_n =\mu)=1$$，即樣本均值$$\overline{X}_n$$幾乎確定收斂至母體均值$$\mu$$。樣本均值會收斂至母體均值。
> * &#x20;則$$X_1,X_2, \ldots$$滿足弱大數法則 $$\Leftrightarrow$$$$\displaystyle \forall \epsilon >0 , ~ \lim_{n \rightarrow \infty} \mathrm{P} ( |\overline{X}_n -\mu| > \epsilon)=0$$，即樣本均值$$\overline{X}_n$$機率收斂至母體均值$$\mu$$。樣本均值收斂至母體均值的機率很大，即有時樣本均值會偏離母體均值，但次數（機率）非常小。

* 大數法則是說當（任意分佈）的樣本數夠多，樣本平均會收斂至母體期望值。長期下來，平均的表現， 與真正該有之表現（指期望值）差異便不大。

弱大數定理 proof：弱大數法則中，只要變異數存在，證明便很簡單，因為$$\mathrm{Var}(\overline{X}_n) = \frac{1}{n} \mathrm{Var}(X)  \xrightarrow[n \rightarrow \infty]{} 0$$

## 中央極限定理 (central limit theorem)&#x20;

不論隨機樣本原來的分佈為何，在樣本數$$N$$足夠大時，將**樣本平均數標準化**後所得新統計量的分佈會非常接近於標準常態分佈。(但隨機樣本必須具有有限變異數)。

$$\{X_1,X_2,⋯,X_N \}$$為獨立同分佈（i.i.d.）的隨機變數（可為任意分佈）， 其共同平均數為$$\mu$$,  共同變異數為$$\sigma^2$$，則

$$\forall c > 0$$, $$\displaystyle \lim_{N \rightarrow 0} \mathrm{P}\bigg( \frac{\sqrt{N} (\overline{X}_N-\mu) }{\sigma} \leq c\bigg) = \Phi(c)$$

其中$$\Phi(c)$$為標準常態分佈的累積分佈函數。

也寫成 $$\bigg( \frac{\sqrt{N} (\overline{X}_N-\mu) }{\sigma} \bigg) \xrightarrow {A} N(0,1)$$

**若隨機樣本沒有有限變異數，則不適用中央極限定理**。&#x20;



```python
import numpy as np

def central_limit_theorem(n_sample=1000, n_point=10000):

    for _ in range(10):
        a, b= np.random.randint(1, 10), np.random.randint(1, 10)
        values = np.random.beta(a, b, (n_sample, n_point))
        mu = a / (a+b)
        std = np.sqrt((a*b)/((a+b)* (a+b) *(a+b+1)))

        mu_hat = values.mean(axis=1)

        zs = np.sqrt(n_point)*(mu_hat - mu)/std
        z_mean, z_std = zs.mean(), zs.std()
        print(f"beta({a}, {b}): mu:{z_mean}, std:{z_std}")

if __name__ == '__main__':
    central_limit_theorem()
    
"""
beta(9, 1): mu:0.04, std:0.98
beta(3, 2): mu:-0.01, std:0.98
beta(8, 3): mu:-0.01, std:0.96
beta(8, 6): mu:-0.04, std:1.04
beta(4, 1): mu:-0.00, std:0.96
beta(1, 1): mu:0.02, std:0.98
beta(1, 9): mu:-0.00, std:0.96
beta(7, 2): mu:0.02, std:1.00
beta(2, 2): mu:0.02, std:1.01
beta(7, 6): mu:-0.03, std:0.99
"""
```

