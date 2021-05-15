# 最大似然估計\(MLE\)

## 簡介

假設資料的機率密度函數$$f(X|\theta)$$的解析型式已知，但是參數$$\theta$$未知。而從資料中獲得$$N$$個觀測值$$X_1, X_2, \ldots, X_N$$（不必獨立，只要是同分佈即可）。

通常假設這些資料為獨立同分佈（i.i.d.），獨立的目的是要讓似然函數（ikelihood function）為觀測值函數值的乘積。但即使資料不為獨立，估計參數值乃會正比於獨立時的機率，而我們只是要求出有最大機率的參數即可。

* 令似然函數 $$\displaystyle L(\theta|X) = \prod_{i=1}^N f(X_i | \theta)$$，求$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X)$$
* 通常會將似然函數取對數簡化求極值的步驟，稱為log-likelihood function $$l(\theta|X) = \log L(\theta |X) = \sum_{i=1}^N \log{f(X_i|\theta})$$。
* 因為對數函數是單調函數，極值的參數不變，即$$\displaystyle \theta^{*} = \mathop{\arg\min}_{\theta} L(\theta |X) = \mathop{\arg\min}_{\theta} l(\theta |X)$$。







