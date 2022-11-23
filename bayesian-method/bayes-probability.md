# 貝葉斯機率

## 貝葉斯主義者認為機率是長期的平均數嗎？

貝葉斯對機率的思考方式允許理論和假設的檢驗。

## 先驗、似然、後驗機率(prior, likelihood, posterior probability)

在貝式統計中，一個隨機事件或者一個不確定事件的後驗機率是在考慮和給出相關證據或數據後所得到的條件機率。同樣，後驗機率分布是一個未知量（視為隨機變量）基於試驗和調查後得到的機率分佈。

**「後驗」在此中代表考慮了被測試事件的相關證據**。

* 後驗機率(posterior probability)是機率分佈的參數$$\theta$$，在給定證據(evidence) $$X$$後的機率：$$\mathrm{P}(\theta \vert X)$$。
* 與似然函數(likelihood function)相反，其為證據$$X$$給定了參數$$\theta$$後的機率：$$\mathrm{P}(X \vert \theta)$$。
* 首先定義參數$$\theta$$的先驗機率(prior probability)為某個帶參數的機率分佈函數$$\mathrm{P}(\theta)$$，則樣本在此參數的可能性為$$\mathrm{P}(X|\theta)$$，因此使用貝式定理得後驗機率為：

$$
\mathrm{P}(\theta | X)=\frac{\mathrm{P}(\theta, X)}{\mathrm{P}(X)}=\frac{\mathrm{P}(X|\theta)\mathrm{P}(\theta)}{\mathrm{P}(X)}=\frac{(X|\theta)\mathrm{P}(\theta)}{\int_{\theta^{'}}\mathrm{P}(X| \theta^{'})\mathrm{P}(\theta^{'})d\theta^{'}}
$$

* 後驗機率可以寫成更易記憶的形式，為後驗機率(posterior probability) ∝可能性(likelihood)×先驗機率(prior probability)。
* Posterior = ( Likelihood \* Prior ) /  Evidence。
