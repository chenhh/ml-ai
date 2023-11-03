# 絕對連續測度

## 簡介

絕對連續測度的概念，主要用於Raydon-Nikodym導數，可保證RK導數不會出現分母為0而分子不為0的情況，只會出現分母為0且分子同時為0之值。

而RK導數主要應用在一般化的條件期望值的存在性，即$$Z=\mathrm{E}(X|\mathcal{F})$$隨機變數的存在性。

* 符號測度$$\nu$$相對於測度$$\mu$$絕對連續若$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$，記為$$\nu \ll \mu$$。
* 有限符號測度的絕對連續可定義為：$$\nu \ll \mu \iff E \in \Sigma,  \forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ,~ \nu(E) < \delta$$。

## 絕對連續測度

> 給定可測空間$$(X, \Sigma)$$與符號測度$$\nu: \Sigma \rightarrow [-\infty, \infty)$$與正測度$$\mu: \Sigma \rightarrow [0,\infty]$$。
>
> 稱符號測度$$\nu$$相對於測度$$\mu$$絕對連續若$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$，記為$$\nu \ll \mu$$。
>
> 註：符號$$\ll$$可解釋為遠小於。

### 絕對連續測度與全變差測度和Jordan分解測度等價

> $$\nu \ll \mu \iff |\nu| \ll \mu \iff \nu^{+} \ll \mu \iff \nu^{-} \ll \mu$$。
>
> * 符號測度的Jordan分解：$$\nu=\nu^{+} - \nu^{-}$$。其中$$\nu^{+}, \nu^{-}$$為正測度且不會同時為無窮大。
> * 全變差測度$$|\nu|=\nu^{+} + \nu^{-}$$。

<details>

<summary>proof: 零測度集合若且唯若全變差測度為0</summary>

給定可測空間$$(X, \Sigma)$$

給定$$\nu \ll \mu$$，則$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$。

因為$$E$$的任意可測子集在測度$$\nu$$中均為0，因此$$E$$為零測集。

由\[零測度集合若且唯若全變差測度為0]得$$\nu(E)=0 \iff |\nu(E)|=0$$。

因此$$|\nu| \ll \mu$$ (QED)

符號測度的Jordan分解：$$\nu=\nu^{+} - \nu^{-}$$與全變差測度$$|\nu|=\nu^{+} + \nu^{-}$$。

因為$$\nu(E)=|\nu|(E)=0$$，所以$$\nu^{+}(E)=\nu^{-}(E)=0$$

因此$$\nu^{+} \ll \mu$$且$$\nu^{-} \ll \mu$$。

(QED)

</details>

## 有限符號測度絕對連續的充要條件

> 給定可測空間$$(X, \Sigma)$$與有限符號測度$$\nu: \Sigma \rightarrow (-\infty, \infty)$$與正測度$$\mu: \Sigma \rightarrow [0,\infty]$$。
>
> 則$$\nu \ll \mu \iff E \in \Sigma,  \forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ,~ \nu(E) < \delta$$。

## 參考資料

* [https://zhuanlan.zhihu.com/p/37493234](https://zhuanlan.zhihu.com/p/37493234)
* [https://en.wikipedia.org/wiki/Absolute\_continuity](https://en.wikipedia.org/wiki/Absolute\_continuity)
