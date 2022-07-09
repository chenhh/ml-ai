---
description: likelihood ratio test, Wilks 檢定
---

# 似然比檢定

## 簡介

似然比檢定根據兩個相互競爭（一個是所有參數都是自由參數的無約束模型，另一個是由原假設約束的含較少參數的相應約束模型，nested model）的統計模型的似然比，來評估它們對資料的的擬合程度。

Neyman-Pearson 引理告訴我們，在簡單原假設對簡單備擇假設的檢定問題中，最優勢檢定由似然比檢定給出，即似然比檢定有最佳的檢定力。事實上，似然比檢定方法也可用在復合假設檢定問題中構造檢定。這是構造檢定的常用方法。

## 簡單對立假設的檢定問題

> 令$$X=(X_1,X_2,\dots, X_n)$$的分佈密度函數為$$\mathrm{P}(X;\theta), ~ \theta \in \Theta$$)未知參數可能為向量。
>
> * 簡單虛無假設為$$H_0:\theta = \theta_0$$。
> * 簡單對立假設為$$H_1: \theta=\theta_1 ~(\theta_1 \neq \theta_0)$$​。
>
> 此檢定問題的似然比為$$\lambda(x)=\frac{\mathrm{P}(x;\theta_1)}{\mathrm{P}(x;\theta_0)}$$，

### 範例：常態分佈與雙參數指數分佈族的似然比

虛無假設$$H_0$$為資料來自常態分佈$$X \sim N(\mu, \sigma^2)$$。

* pdf為$$\mathrm{P}_0(x; \mu, \sigma^2) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left( - \frac{(x-\mu)^2}{2 \sigma^2} \right)$$
* MLE為$$\hat{\mu}_0=\overline{X}$$，$$\hat{\sigma}_0=\sqrt{\frac{1}{n} \sum_{i=1}^n (X_i - \overline{X})^2}$$

對立假設$$H_1$$​為資料來自雙指數分佈族$$X \sim \exp(\mu, \sigma^2)$$。

* pdf為$$\mathrm{P}_1(x; \mu, \sigma^2) = \left\{ \begin{aligned} & \frac{1}{\sigma} \exp \left( -\frac{x- \mu}{ \sigma} \right), & x - \mu \geq 0 \\ & 0 & x - \mu < 0 \end{aligned} \right.$$
* MLE為$$\hat{\mu}_1=X_{(1)}=\min\{X_1,\dots, X_n \}$$, $$\hat{\sigma}_1=\overline{X} - X_{(1)}$$

所以似然比為$$\displaystyle \lambda(x)=\frac{\prod_{i=1}^n \mathrm{P}_1(x_i; \hat{\mu}_1, \hat{\sigma}_1)}{\prod_{i=1}^n \mathrm{P}_0(x_i; \hat{\mu}_0, \hat{\sigma}_0)} = \left( \sqrt{2\pi e^{-1}} \right)^n D^n$$，$$\displaystyle D= \frac{ n \sum_{i=1}^n (x_i - \overline{x})^2 }{\sum_{i=1}^n (x_i - x_{(1)})}$$。

由於$$\lambda(x)$$對$$D$$​嚴格遞增，所以拒絕域可選$$\{ x: D \geq c\}$$，而不論虛無假設或是對立假設為真，$$D$$的分佈均與$$\mu, \sigma$$無關，因此：

* 虛無假設為真時，type-I錯誤：$$\mathrm{P}\{ D \geq c ~| \text{ sample from N(0, 1}\}$$
* 對立假設為真的，type-II錯誤為$$\mathrm{P}=\{ D < c | \text{ sample from exp(0, 1)}\}$$。

## 複合對立假設的檢定問題

> 令$$X=(X_1,X_2,\dots, X_n)$$的分佈密度函數為$$\mathrm{P}(X;\theta)$$。
>
> * 虛無假設為$$H_0: \theta \in \Theta_0$$
> * 對立假設為$$H_1: \theta \in \Theta_1$$
>
> 似然比$$\displaystyle \lambda(x)=\frac{\sup_{\theta \in \Theta_1} \mathrm{P}(x;\theta)}{\sup_{\theta \in \Theta_0}\mathrm{P}(x;\theta)} = \frac{\mathrm{P}(x;\hat{\theta}_1)}{\mathrm{P}(x;\hat{\theta}_0)}$$
>
> 其中$$\hat{\theta_0}$$​與$$\hat{\theta_1}$$​分別是$$H_0$$和$$H_1$$​成立時，$$\theta$$的MLE。
>
> <mark style="color:red;">這個檢定方法常用於區分樣本來自這類分佈，還是另一類分佈的檢驗問題</mark>。

在$$\lambda(x)$$​之值較大時，觀察到資料從對立假設出現的機率較大，因此應拒絕虛無假設。故檢定的拒絕域為$$\{ x: \lambda(x) \geq c\}$$。

## 參考資料

[\[知乎\]數理統計學習筆記：似然比檢驗](https://zhuanlan.zhihu.com/p/104583619)
