# 平穩性、定態(stationary)

## 平穩性(定態)(stationary)

平穩時間序列是其統計量不依賴於觀察該序列的時間$$t$$的序列。

因此，具有趨勢或季節性的時間序列不是平穩的，因為趨勢和季節性將影響不同時間的時間序列的值。另一方面，白噪聲序列是平穩的，無論何時觀察它，它在任何時間點看起來都應該大致相同。

有些情況可能會令人困惑，<mark style="color:blue;">具有循環行為（但沒有趨勢或季節性）的時間序列是平穩的。這是因為週期不是固定長度的，所以在我們觀察序列之前，我們無法確定週期的峰值和谷值在哪裡</mark>。

一般來說，一個平穩的時間序列在長期內沒有可預測的模式。時間圖將顯示該系列大致水平（儘管一些循環行為是可能的），具有恆定的變異數。

平穩與不平穩是針對隨機過程（如時間序列）。<mark style="color:blue;">計量經濟學中假設時間序列平穩是為了保證收集到的資料服從同分佈（嚴格平穩）的。然後再依據近似獨立（即漸進獨立）等假設，才能使用回歸估計</mark>。嚴格平穩的假設太強，因此用弱平穩假設來近似滿足同分佈的假設，即一階動差（期望），二階中央動態（變異數與共變異數）不隨時間而改變。

如何能推出弱平穩的這些假設呢？就需要建立自回歸模型。單位根的概念就這樣出現了。

用滯後運算元理論可以使模型書寫上簡化，<mark style="color:blue;">可以把滯後運算元理解為自回歸模型中解釋變數（即滯後被解釋變數）的係數的倒數</mark>。單位根就是上述系數出現等於1的情況。此時，自回歸模型得到的被解釋變數不會隨時間收斂，其期望與變異數也就不滿足恆定（不隨時間變化）的假設，即時間序列不平穩（不滿足弱平穩的條件）。此時，不應該建立自回歸模型。

而解釋變數（即滯後被解釋變數）的係數應該有三種情況：<mark style="color:red;">小於1，等於1和大於1</mark>。小於1就是不存在單位根，此時被解釋變數隨時間會趨於收斂，期望，方差也會存在且與時間無關，即序列平穩。如果等於1或者大於1，時間序列均不平穩。如上段所說明。等於1的情況就是存在單位根，大於1的情況被預設忽略了，因為現實中不可能出現大於1的情況。

主要有兩大類情況導致非平穩時間序列：

1. 存在單位根；
2. 2.存在趨勢。而趨勢又分為確定性趨勢和隨機性趨勢。

如果你想檢驗時間序列是否平穩，可以用ADF分三步走，分別對確定性趨勢、隨機性趨勢和單位根進行檢驗，當檢驗拒絕零假設，即不存在單位根，則可以停止檢驗。

<mark style="color:blue;">平穩序列實際上最核心的就是有非時變的均值</mark>，即其均值是恆定， 不受時間t影響，<mark style="color:red;">換種說法就是這個序列無論怎麼走都會收斂至均值</mark>。所以可以簡單看出來，所謂AR模型不過是一個均值回歸模型，而p的數則會影響該模型預測收斂至均值的速度。

### 弱定態時間序列(weak stationary)

> 給定序列$$\{y_t\}_{t=-\infty}^{\infty}$$，若對於任意的時間跨度$$k$$，序列的統計量滿足：
>
> 1. \[平均值為固定值(非時變)] $$\mathrm{E}(y_t)=\mu$$
> 2. \[變異數為有限值(可時變)] $$\mathrm{Var}(y_t) < \infty$$
> 3. \[共變異數只與時間跨度有關，與特定時間點$$t$$無關] $$\mathrm{Cov}(y_t, y_{t-k})=\mathrm{E}(y_t - \mu)(y_{t-k} - \mu)=\gamma(k)$$
>
> 則稱為弱定態(weak stationary)或共變異定態(covariance stationary)，或簡稱為定態時間序列。

由定義可知定態就是時間序列的結構，不會隨時間變化，而有穩定的結構，才是可預測的序列。

穩定序列有以下的性質：

* $$\gamma(0)\equiv \mathrm{Var}(y_t)=\mathrm{Var}(y_{t-k})$$
* $$\gamma(k)=\gamma(-k)$$，即$$\mathrm{Cov}(y_t, y_{t-k})=\mathrm{Cov}(y_t, y_{t+k})$$
* $$\rho(k)=\frac{\mathrm{Cov}(y_t,y_{t-k})}{\sigma_t \sigma_{t-k}}=\frac{\gamma(k)}{\gamma(0)}$$

$$\gamma(k)$$的樣本估計式$$\hat{\gamma}(k)=\hat{\mathrm{Cov}}(y_t, y_{t-k})=\frac{1}{T}\sum_{t=k+1}^T(y_t-\overline{y})(y_{t-k}-\overline{y})$$。

可得$$\hat{\mathrm{Var}}(y_t)=\frac{1}{T}\sum_{t=1}^T(y_t-\overline{y})^2$$

$$\hat{\rho}(k)=\frac{\hat{\mathrm{Cov}}(y_t, y_{t-k})}{\hat{\mathrm{Var}(y_t)}}$$

### 範例弱定態時間序列

> $$y_t=A\sin(\omega t+\theta)$$

### 強定態時間序列（strict stationary)

> 給定序列$$\{ y_t\}_{t=-\infty}^\infty$$，若對於任意的時間跨度$$k$$，其聯合機率分佈$$F(\cdot)$$均與時間$$t$$無關，，則稱為嚴格定態序列。
>
> $$F(y_t, y_{t-1}, \dots, y_{t-k})=F(y_{\tau}, y_{\tau-1}, \dots, y_{\tau-k}), ~ \forall t, \tau, k$$

若序列為嚴格定態，則其聯合機率陽佈不會因為時間點而改變(invariant under time shift)。

例：

* i.i.d.的抽樣樣本若依抽樣的時間排序後，為嚴格定態的時間序列。

### 白噪音為嚴格定態時間序列

> 定義白噪音$$e_t \sim \mathrm{WN}(0, \sigma^2)$$滿足以下條件：
>
> * \[均值為０] $$\mathrm{E}(e_t)=0, ~\forall t$$
> * \[變異數為常數] $$\mathrm{E}(e_t^2)=\sigma^2, ~\forall t$$
> * \[序列間元素不相關] $$\mathrm{E}(e_te_{t-k})=0,~\forall t,k$$
>
> 註：有些論文定義白噪音為i.i.d.的樣本序列，比不相關條件更強。

![白噪音的ACF](../../.gitbook/assets/white\_noise-min.png)

```python
def white_noise(n_point=10000):
    from statsmodels.tsa.stattools import (acovf, acf)
    import matplotlib.pyplot as plt
    from statsmodels.graphics.tsaplots import plot_acf
    values = np.random.rand(n_point)  
    gammas = acovf(values)
    rhos = acf(values)
    print(f"gamma:{gammas}, rho:{rhos}")
    plot_acf(values)
    plt.show()

if __name__ == '__main__':
    white_noise()
```

### 強定態時間序列為弱定態時間序列

> 若時間序列$$\{y_t\}$$為強定態，且$$\mathrm{E}(y_t^2)<\infty$$，則$${y_t}$$為弱定態時間序列。



## 差分(difference)

差分即通過消除時間序列水平的變化來幫助穩定時間序列的平均值，從而消除（或減少）趨勢和季節性。有時差分數據看起來不是平穩的，可能需要第二次差分數據以獲得平穩序列。

除了檢視數據的時間圖外，ACF 圖對於識別非平穩時間序列也很有用。<mark style="color:blue;">對於平穩的時間序列，ACF 會相對較快地下降到零，而非平穩數據的 ACF 下降緩慢</mark>。

## 單根檢驗(unit root test)

更客觀地確定是否需要差分的一種方法是使用單位根檢驗。這些是平穩性的統計假設檢驗，旨在確定是否需要差分。

有許多單位根檢驗可用，它們基於不同的假設，可能會導致相互矛盾的答案。

<mark style="color:red;">Granger and Newbold發現發定態變數之間，可能會出現所謂「假性迴歸」(spurious regression)的問題，因此使用時間序列態，都必須使用單根檢定確定隨機變數是否為定態</mark>。
