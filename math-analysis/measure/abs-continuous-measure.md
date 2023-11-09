---
description: absolutely continuous
---

# 絕對連續測度

## 簡介

絕對連續測度的概念，主要用於Raydon-Nikodym導數，可保證RK導數不會出現分母為0而分子不為0的情況，只會出現分母為0且分子同時為0之值。

而RK導數主要應用在一般化的條件期望值的存在性，即$$Z=\mathrm{E}(X|\mathcal{F})$$隨機變數的存在性。

* 符號測度$$\nu$$相對於測度$$\mu$$絕對連續若$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$，記為$$\nu \ll \mu$$。
* 有限符號測度的絕對連續可定義為：$$\nu \ll \mu \iff E \in \Sigma,  \forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ,~ \nu(E) < \delta$$。

## 絕對連續測度

給定可測空間$$(X, \Sigma)$$

#### 正測度絕對連續於正測度

測度$$\nu: \Sigma \rightarrow [0, \infty)$$相對於測度$$\mu: \Sigma \rightarrow [0,\infty]$$絕對連續，記為$$\nu \ll \mu$$若$$\forall E \in \Sigma, \mu(E)=0 \implies \nu(E)=0$$。

#### 符號測度絕對連續於符號測度

符號測度$$\nu: \Sigma \rightarrow [-\infty, \infty)$$相對於符號測度$$\mu: \Sigma \rightarrow [-\infty, \infty)$$絕對連續，記為$$\nu \ll \mu$$若$$\forall E \in \Sigma, |\mu|(E)=0 \implies \nu(E)=0$$。

#### 任意測度絕對連續於正測度

任意測度$$\nu$$(正測度、符號測度、複測度)與測度$$\mu: \Sigma \rightarrow [0,\infty]$$絕對連續，記為$$\nu \ll \mu$$若$$\forall E \in \Sigma, \mu(E)=0 \implies \nu(E)=0$$。

註：符號$$\ll$$可解釋為遠小於。

註：因為(正)測度為符號測度的特例，因為若$$\nu$$為正測度時，$$\nu \ll \mu$$條件不變。

## 測度在集合集中

> 令$$\nu$$為可測空間$$(X, \Sigma)$$的任意測度(正測度、符號測度、複測度)。
>
> 稱測度$$\nu$$在可測集合$$E \in \Sigma$$是集中的(concentrated)若 $$\forall S \in \Sigma, ~ \nu(S) = \nu(S \cap E)$$。
>
> 等價定義: 測度$$\nu$$在可測集合$$E \in \Sigma$$是集中的(concentrated)若$$\forall S \in \Sigma, ~ S \cap E= \emptyset \implies \nu(S)=0$$。
>
> [https://math.stackexchange.com/questions/956634/equivalence-of-definition-of-measure-concentrated-on-a-set-a](https://math.stackexchange.com/questions/956634/equivalence-of-definition-of-measure-concentrated-on-a-set-a)

<details>

<summary>proof: 等價定義證明</summary>

\=>

如果$$\nu$$在$$E$$集中時，得$$\nu(S)=\nu(S \cap E)$$。

若$$S \cap E=\emptyset$$，則$$\nu(S \cap E)=\nu(S)=0$$ 。

(QED)

<=

如果$$\nu$$在$$E$$集中時，得$$\forall S \in \Sigma, S \cap E=\emptyset$$且$$\nu(S)=0$$。

因為$$S = (S \cap E) \cup (S \cap E^c)$$且$$(S \cap E^c) \cap E=\emptyset$$，所以$$\nu(S \cap E^c)=0$$

因此$$\nu(S)=\nu(S \cap E)$$ (QED)

</details>

## 相互奇異測度(以測度集中定義)

> 令$$\nu, \mu$$為可測空間$$(X, \Sigma)$$的任意測度(正測度、符號測度、複測度)。
>
> 如果能找到兩可測集合$$A, B \in \Sigma, ~ A \cap B=\emptyset$$使得$$\nu$$在$$A$$集中，$$\mu$$在$$B$$集中，則稱$$\nu, \mu$$相互奇異，記為$$\nu \perp \mu$$。

### 絕對連續與相互奇異測度的性質

> 給定可測空間$$(X, \Sigma)$$，$$\nu, \nu_1, \nu_2$$為任意測度(正測度、符號測度、複測度)，$$\mu: \Sigma \rightarrow [0, \infty]$$為正測度，則：
>
> 1. 若$$\nu$$在$$E$$集中，則$$|\nu|$$在$$E$$集中。
> 2. 若$$\nu_1 \perp \nu_2$$，則$$|\nu_1| \perp |\nu_2|$$。
> 3. 若$$\nu_1 \perp \mu, ~ \nu_2 \perp \mu$$，則$$\nu_1 + \nu_2 \perp \mu$$。
> 4. 若$$\nu_1 \ll \mu, ~ \nu_2 \ll \mu$$，則$$\nu_1 + \nu_2 \ll \mu$$。
> 5. 若$$\nu \ll \mu$$，則$$|\nu| \ll \mu$$。
> 6. 若$$\nu_1 \ll \mu, ~ \nu_2 \perp \mu$$，則$$\nu_1 \perp \nu_2$$。
> 7. 若$$\nu \ll \mu, ~ \nu \perp \mu$$，則$$\nu=0$$。





### 絕對連續測度與全變差測度和Jordan分解測度等價

> 給定可測空間$$(X, \Sigma)$$與符號測度$$\nu, \mu: \Sigma \rightarrow [-\infty, \infty)$$。
>
> $$\nu \ll \mu \iff |\nu| \ll |\mu| \iff \nu^{+} \ll \mu \iff \nu^{-} \ll \mu$$。
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
> 則$$\nu \ll \mu \iff E \in \Sigma,  \forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ~\text{ whenever } \mu(E) < \delta$$。
>
> 註：因為$$\nu \ll \mu \iff |\nu| \ll \mu$$且$$|\nu(E)| \leq |\nu|(E)$$，因此只要考慮$$\nu=|\nu|$$非負值部份即可。
>
> [https://math.stackexchange.com/questions/3053527/absolute-continuity-of-measure-and-epsilon-delta-condtion](https://math.stackexchange.com/questions/3053527/absolute-continuity-of-measure-and-epsilon-delta-condtion)

<details>

<summary>proof</summary>

<=

令$$E \in \Sigma, ~\mu(E)=0$$

若$$\forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ,\text{ whenever } \mu(E) < \delta$$

因為$$\mu(E)=0 \implies  \forall \epsilon >0, ~ |\nu(E)|<\epsilon$$，因此$$\nu(E)=0$$ (QED)

\=> (反證法)

假設$$\exists \epsilon > 0 \ni \forall n \in \mathbb{N}$$，存在$$E_n \in \Sigma$$且$$\mu(E_n) < 1/2^n$$且$$\nu(E_n) \geq \epsilon$$。

令$$F_k =\bigcup_{n=k}^\infty E_n$$ 且 $$F =\bigcap_{k=1}^\infty F_k$$

則$$\nu(F_k)< \sum_{n=k}^\infty 1/2^n = 2^{1-k}$$，因此$$\mu(F)=0$$，但$$\nu(F_k) \geq \epsilon, \forall k$$。

因為$$\nu$$為有限測度，$$\nu(F)=\lim_{k \rightarrow \infty} F_k \geq \epsilon$$，因此不是絕對連續。(QED)

</details>

## 參考資料

* [https://zhuanlan.zhihu.com/p/37493234](https://zhuanlan.zhihu.com/p/37493234)
* [https://en.wikipedia.org/wiki/Absolute\_continuity](https://en.wikipedia.org/wiki/Absolute\_continuity)
* [https://zhuanlan.zhihu.com/p/75414600](https://zhuanlan.zhihu.com/p/75414600)
