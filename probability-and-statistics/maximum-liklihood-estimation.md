# 最大似然估計\(MLE\)

## 簡介

假設資料的機率密度函數$$f(X|\theta)$$的解析型式已知，但是參數$$\theta$$未知。而從資料中獲得$$N$$個觀測值$$X_1, X_2, \ldots, X_N$$（不必獨立，只要是同分佈即可）。

通常假設這些資料為獨立同分佈（i.i.d.），獨立的目的是要讓似然函數（ikelihood function）為觀測值函數值的乘積。但即使資料不為獨立，估計參數值乃會正比於獨立時的機率，而我們只是要求出有最大機率的參數即可。

* 令似然函數 $$\displaystyle L(\theta|X) = \prod_{i=1}^N f(X_i | \theta)$$，求$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X)$$
* 通常會將似然函數取對數簡化求極值的步驟，稱為log-likelihood function $$l(\theta|X) = \log L(\theta |X) = \sum_{i=1}^N \log{f(X_i|\theta})$$。
* 因為對數函數是單調函數，極值的參數不變，即$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X) = \mathop{\arg\min}_{\theta} l(\theta |X)$$。
* 因為$$l(\theta | X)$$為凸函數，最大值唯一，解析方法是取偏微分為0處的參數，而數值方法可以用梯度法快速求值。

### MLE的不變性（invariance principle）

> 對機率密度函數的參數$$\theta$$的任一函數$$f(\theta)$$，如果$$\theta^{*}$$ 為$$\theta$$之MLE，則$$f(\theta^{*})$$為$$f(\theta)$$之MLE。
>
> 註：$$f$$不必為一對一函數，只須滿足普通函數定義即可。
>
> * 一般的想法是將似然函數 $$L(\theta|X)$$中的$$\theta$$換成$$f(\theta)$$得$$L(f(\theta)|X)$$後再求MLE得$$f(\theta^{*} )$$，但可能轉換後的函數相當複雜，因此不變性提供了一個相當好的性質。
> * 動差法也有不變性，但不保證轉換後的參數有極大似然率值。

## MLE與充分統計量的關係

* 動差估計量不一定是充分統計量的函數。
* 而MLE估計量必須存在且唯一，才會是充分統計量的函數  。
  *  若$$T$$為$$\theta$$一充分統計量，且存在唯一的$$\theta$$之MLE $$\theta^{*}$$，則$$\theta^{*}$$必為T的函數。
  * 若$$\theta$$之MLE不唯一，則必有為$$T$$函數之MLE $$\theta^{*}$$  ，但仍然不唯一。





