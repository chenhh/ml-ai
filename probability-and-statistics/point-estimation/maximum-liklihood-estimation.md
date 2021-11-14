# 最大似然估計(MLE)

## 簡介

假設資料的機率密度函數$$f(X|\theta)$$的解析型式已知，但是參數$$\theta$$未知。而從資料中獲得$$N$$個觀測值$$X_1, X_2, \ldots, X_N$$（**不必獨立，只要是同分佈即可**）。

通常假設這些資料為獨立同分佈（i.i.d.），獨立的目的是要讓似然函數（ikelihood function）為觀測值函數值的乘積。但即使資料不為獨立，估計參數值乃會正比於獨立時的機率，而我們只是要求出有最大機率的參數即可。

* 令似然函數 $$\displaystyle L(\theta|X) = \prod_{i=1}^N f(X_i | \theta)$$，求$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X)$$
* 通常會將似然函數取對數簡化求極值的步驟，稱為log-likelihood function $$l(\theta|X) = \log L(\theta |X) = \sum_{i=1}^N \log{f(X_i|\theta})$$。
* 因為對數函數是單調函數，極值的參數不變，即$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X) = \mathop{\arg\min}_{\theta} l(\theta |X)$$。
* 因為$$l(\theta | X)$$為凸函數，解析方法是取偏微分為0處的參數，而數值方法可以用梯度法快速求值。

### 例：丟銅板

* 假如我們觀察拋擲銅板的現象，得到觀察序列 $$X = \{0, 1, 0, 0, 1, 1, 0, 0, 0, 1 \}$$ 這個現象，其中的 1 代表正面 (人頭)，0 代表反面 (字)，因此正面共出現 4 次，反面共出現 6 次。  $$\mathrm{P}(X=1)=0.4,  \mathrm{P}(X=0)=0.6$$  。
* 丟銅板的機率已知為二項分佈$$X \sim Ber(N,p)$$，其中$$\mathrm{P}(X=1)=p$$。
  * $$\begin{aligned} f(X|\theta) & = \binom{N}{k}\mathrm{P}(X=1)^{k}\mathrm{P}(X=0)^{n-k} \\&= \binom{N}{k}p^k(1-p)^{n-k} \end{aligned}$$
* 根據最大似然法則，我們應該去找 $$p^{*} = \mathrm{argmax}_{p} \sum_{i=1}^N \log{f(x_i|p)}$$

### 例：Poisson分佈

* $$X_1, X_2,\ldots, X_N \sim P(\lambda),\ \lambda > 0$$。
* pdf $$f(X=x|\lambda) =  \frac{e^{-\lambda} \lambda^x}{x!}$$
* $$\displaystyle L(\lambda|X)= \prod_{i=1}^N \frac{1}{x_i !} e^{n \lambda } \lambda^{\sum_{i=1}^N x_i}$$
* $$\displaystyle l(\lambda|X) = -\log(\prod_{i=1}^N x_i !) - N \lambda + \sum_{i=1}^N x_i \log \lambda$$
* $$\frac{\partial l(\lambda |X)}{\partial \lambda} = -N + N \frac{\overline{x}_N}{\lambda} =0 \Rightarrow \hat{\lambda}_{MLE} = \overline{x}_N$$
* $$\frac{\partial^2 l(\lambda |X)}{\partial \lambda ^2} = -N \frac{\overline{X}_N}{\lambda^2} < 0 , \ \forall \lambda >0$$
* 所以$$\hat{\lambda}_{MLE} = \overline{x}_N$$為極大值。

本例中，使用動差法一樣會得到$$\lambda = \overline{x}_N$$ 的結果，即動差法與MLE得到的估計式可能相同。

### 例：常態分佈

* $$X_1, X_2, \ldots, X_N \sim N(\mu, \sigma^2),  \ \theta=(\mu, \sigma^2)$$
* pdf $$\displaystyle f(X|\theta)= \frac{1}{\sqrt{2\pi} \sigma} \exp \bigg( - \frac{(X-\mu)^2}{2 \sigma^2} \bigg)$$
* $$\displaystyle L(\theta|X)= \big( \frac{1}{\sqrt{2\pi}  \sigma}\big)^N \exp \bigg( - \frac{1}{2 \sigma^2} \sum_{i=1}^N (x_i - \mu)^2\bigg)$$
* $$\displaystyle l(\theta|X) =-\frac{N}{2}\log 2\pi - \frac{N}{2} \log \sigma^2 - \frac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2$$
* $$\frac{\partial l}{\partial \mu} = \frac{N}{\sigma^2}(\overline{x}_N - \mu) = 0 \Rightarrow \hat{mu}_{MLE} = \overline{x}_N$$
* $$\frac{\partial l}{\partial \sigma^2}= - \frac{N}{ 2 \sigma^2} + \frac{1}{2 \sigma^4} \sum_{i=1}^N (x_i - \mu)^2 =0 \Rightarrow \hat{\sigma}^2_{MLE}=\sum_{i=1}^N \frac{(x_i - \mu)^2}{N}$$

### 例：均勻分佈

* $$X_1,  X_2, \ldots, X_N \sim U(-\theta, \theta), \ \theta > 0$$
* $$L(\theta|X) = \big(\frac{1}{2 \theta} \big)^N \mathrm{I}(|x_i| \leq \theta) = \big(\frac{1}{2 \theta} \big)^N \mathrm{I}(\theta \geq \max|x|)$$
* 由於$$\theta>0$$，因此$$\big(\frac{1}{2 \theta} \big)^N$$ 為$$\theta$$之遞減函數，因此$$\theta$$越小其值越大，但不可小於$$\max⁡|x|$$。
* $$\hat{\theta}_{MLE} = \max|X| = X_{(N)}$$。

### 例：Cauchy分佈的MLE不唯一

* $$X_1,  X_2, \ldots, X_N \sim C(\theta, 1), \ \theta  \in \mathbb{R}$$
* $$\displaystyle L(\theta|X) = \prod_{i=1}^N \frac{1}{\pi(1+(x_i - \theta)^2)}$$
* $$\displaystyle\frac{\partial l}{\partial \theta} \sum_{i=1}^N \frac{x_i- \theta}{1+(x_i - \theta)^2} = 0$$
* 可得$$\theta$$的$$2N-1$$個方程式，有$$2N-1$$個解。

### 例：MLE不存在

* $$X_1, X_2, \ldots, X_N \sim f(X| \theta) = e^{-(x-\theta)}, \ x > \theta,  \ \theta  \in \mathbb{R}$$
* $$L(\theta|X)=e^{N (\theta - \overline{x}_N)} \mathrm{I}(x_{(1)} > \theta)$$
* 當$$\theta$$越大，$$N(\theta - \overline{x}_N)$$之值越大，$$L(\theta|x)$$也越大。而$$\hat{\theta }_{MLE} = X_{(1)}$$，但$$\theta$$依定義必須小於$$X_{(1)}$$，因此$$\hat{\theta }_{MLE}$$ 不存在。

### 例：MLE無解析解(Gamma distribution)

* $$X_1, X_2, \ldots, X_N \sim \Gamma(a,b), ~a,b >0, ~ \theta=(a,b)$$
* $$\displaystyle l(\theta|X)=  -N \log \Gamma(a)  -Na \log b +(a-1) \sum_{i=1}^N \log x_i - \frac{1}{b} \sum_{i=1}^N x_i$$
* $$\frac{\partial l}{\partial a} = -N \frac{(\Gamma(a))^{'}}{\Gamma(a)}-N \log b+\sum_{i=1}^N \log x_i = 0$$
* $$\frac{\partial l }{\partial b} = - \frac{Na}{b} + \frac{1}{b^2} \sum_{i=1}^N x_i = 0$$

&#x20;由於上兩式中存在$$(\Gamma(a))^{′}$$，無解析解，但可由數值方法求解。

### 例：MLE無解析解(Weibull distribution)

* $$X_1, X_2, \ldots, X_N \sim W(a,b), ~a,b >0, ~ \theta=(a,b)$$
* $$\displaystyle l(\theta|X)=N \log(ab)+(b-1)\sum_{i=1}^N \log x_i -a \sum_{i=1}^N x_i^b$$
* $$\displaystyle \frac{\partial l}{\partial a} = \frac{N}{a} - \sum_{i=1}^N x_i^b = 0$$
* $$\displaystyle \frac{\partial l}{\partial b} = \frac{N}{b} + \sum_{i=1}^N \log x_i - a\sum_{i=1}^N x_i^b  \log x_i= 0$$

上兩式顯示無解析解，但可由數值方法求解。

## MLE的不變性（invariance principle）

> 對機率密度函數的參數$$\theta$$的任一函數$$f(\theta)$$，如果$$\theta^{*}$$ 為$$\theta$$之MLE，則$$f(\theta^{*})$$為$$f(\theta)$$之MLE> 。
>
> 註：$$f$$不必為一對一函數，只須滿足普通函數定義即可。
>
> * 一般的想法是將似然函數 $$L(\theta|X)$$中的$$\theta$$換成$$f(\theta)$$得$$L(f(\theta)|X)$$後再求MLE得$$f(\theta^{*} )$$，但可能轉換後的函數相當複雜，因此不變性提供了一個相當好的性質。
> * 動差法也有不變性，但不保證轉換後的參數有極大似然率值。
> *

MLE與充分統計量的關係


* 動差估計量不一定是充分統計量的函數。
*   而**MLE估計量必須存在且唯一，才會是充分統計量的函數**    。

    * &#x20;若$$T$$為$$\theta$$一充分統計量，且存在唯一的$$\theta$$之MLE $$\theta^{*}$$，則$$\theta^{*}$$必為T的函數。
    * 若$$\theta$$之MLE不唯一，則必有為$$T$$函數之MLE $$\theta^{*}$$  ，但仍然不唯一。



### 例：MLE為充分統計量的函數但非充分統計量

* $$X_1,X_2, \ldots ,X_N \sim U(\theta ,2\theta), ~ \theta >0$$
* 順序統計量 $$(X_{(1)}, X_{(n)} )$$  為$$\theta$$之最小充分統計量  。
* 但$$\theta$$之MLE為$$X_{(n)}/2$$為最小充分統計量的函數，但非充分統計量。







