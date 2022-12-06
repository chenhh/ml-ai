---
description: information matrix
---

# Fisher資訊矩陣

## Fisher Information 的定義

給定獨立同分佈(iid)的隨機變數$$X_1, \dots, X_n$$，機率密度函數為$$f(X; \theta)$$，$$\theta$$為目標參數(假設為純量，且沒有nuissance parameter)，則可得似然函數如下：

$$
\displaystyle L(\mathbf{X}; \theta)= \prod_{i=1}^n f(X_i; \theta)
$$

得對數似然函數$$\displaystyle l(\mathbf{X};\theta) = \sum_{i=1}^n \log f(X_i; \theta)$$，對$$\theta$$微分且令函數為0，可由MLE得$$\hat{\theta}_{MLE}$$。

對數似然函數的一階導數也稱score函數：

$$
\displaystyle S(\mathbf{X}; \theta)=\sum_{i=1}^n \frac{\partial \log f(X_i; \theta)}{ \partial \theta}
$$

而Fisher information定義為$$I(\theta)$$為score函數的二階動差：

$$
I(\theta)=\mathrm{E}(S(X;\theta)^2)
$$

### Fisher infomration為MLE函數的變異數

一般情況下(some regularity conditions)，可得$$\mathrm{E}(S(\mathbf{X};\theta))=0$$。因此可得：

$$
I(\theta)=\mathrm{E}(S(X;\theta)^2)-\mathrm{E}(S(X;\theta))=\mathrm{Var}(S(X;\theta))
$$

可得Fisher information為MLE函數的變異數。隨替收集的資料越來越多(隨機變數數量變多)，MLE函數為隨機變數獨立和的形式，因此代表資訊量變大。

在一般情形下，對score函數在真實值泰勒展開，使用中央極限定理，依機率一致收命與Slutsky定理，可得：

$$
\sqrt{n} (\hat{\theta}_{MLE} - \theta) \sim N(0, I^{*}(\theta)^{-1})
$$

此處 $$I^{*}(\theta)$$為只觀察到單個隨機變數$$X$$的Fisher information，當有$$n$$個獨立同分佈的觀測值時，$$I^{*}(\theta)=\frac{I(\theta)}{n}$$，即反應了對參數估計的精準度。

### Fisher information為對數似然函數參數的負二導數期望值(參數凸函數的曲率)

如果對數似然函數二階可導，在一般情況下，可得：

$$
\mathrm{E}(S(\mathbf{X};\theta)^2) = -E \left(\frac{\partial^2  \log (L(\mathbf{X}; \theta)) }{\partial \theta^2} \right)
$$

對數似然函數在參數的負二階導數，反應了此函數在頂點的彎曲程度，其值越大，整個對數似然函數的形狀就偏向高而窄(參數的變異程度較小)，也就代表掌握的資訊越多。

## 參考資料

* [\[知乎\] 費雪資訊 (Fisher information) 的直觀意義是什麼](https://www.zhihu.com/question/26561604)？
