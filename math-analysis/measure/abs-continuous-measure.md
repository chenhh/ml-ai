---
description: absolutely continuous
---

# 絕對連續測度

## 簡介

絕對連續測度的概念，主要用於Raydon-Nikodym導數，可保證RK導數不會出現分母為0而分子不為0的情況，只會出現分母為0且分子同時為0之值。

而RK導數主要應用在一般化的條件期望值的存在性，即$$Z=\mathrm{E}(X|\mathcal{F})$$隨機變數的存在性。

* 符號測度$$\nu$$相對於測度$$\mu$$絕對連續若$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$，記為$$\nu \ll \mu$$。
* 符號測度$$\nu$$相對於符號測度$$\mu$$絕對連續若$$\forall E \in \Sigma, ~ |\mu|(E)=0 \implies \nu(E)=0$$，記為$$|\nu| \ll |\mu| \iff \nu \ll |\mu|$$。
* <mark style="color:red;">絕對連續測度</mark>$$\nu \ll |\mu|$$<mark style="color:red;">可保證</mark>$$\mu$$<mark style="color:red;">零測集仍為</mark>$$\nu$$<mark style="color:red;">零測集</mark>。因為正測度$$\mu=|\mu|$$，因此如果$$\nu \ll |\mu|$$可寫為$$\nu \ll \mu$$。
* <mark style="color:red;">有限符號測度</mark>的絕對連續可定義為：$$\nu \ll \mu \iff E \in \Sigma,  \forall \epsilon > 0, ~ \exists \delta >0 \ni |\nu(E)|< \epsilon ,~ \nu(E) < \delta$$。

## 絕對連續測度

給定可測空間$$(X, \Sigma)$$：

### 正測度絕對連續於正測度

正測度$$\nu: \Sigma \rightarrow [0, \infty]$$相對於正測度$$\mu: \Sigma \rightarrow [0,\infty]$$絕對連續，記為$$\nu \ll \mu$$若$$\forall E \in \Sigma, \mu(E)=0 \implies \nu(E)=0$$。

<mark style="color:blue;">因為正測度有單調性，因此</mark>$$\forall F \in \Sigma, F \subseteq E$$<mark style="color:blue;">，若</mark>$$0 \leq \mu(F) \leq \mu(E) \implies \mu(F)=0$$<mark style="color:blue;">。可保證</mark>$$E$$<mark style="color:blue;">為</mark>$$\mu$$<mark style="color:blue;">零測集。同理可得</mark>$$\nu(E)$$<mark style="color:blue;">為</mark>$$\nu$$<mark style="color:blue;">零測集</mark>。

### 符號測度絕對連續於符號測度

符號測度$$\nu: \Sigma \rightarrow [-\infty, \infty)$$相對於符號測度$$\mu: \Sigma \rightarrow [-\infty, \infty)$$絕對連續，記為$$\nu \ll |\mu|$$若$$\forall E \in \Sigma, |\mu|(E)=0 \implies \nu(E)=0$$。

其中$$|\mu|=\mu^{+}+\mu^{-}$$為全變差測度。

<mark style="color:blue;">符號測度不滿足單調性，因此符號測度在絕對連續時必須使用全變差測度是因為\[零測度集合若且唯若全變差測度為0]，如此才能保證</mark>$$E$$<mark style="color:blue;">為</mark>$$|\mu|$$<mark style="color:blue;">零測集。</mark>

如果$$\mu$$為正測度時，因為可保證$$E$$為零測集，仍然考慮$$\nu \ll \mu$$即可。

注意$$\nu \ll |\mu| \iff |\nu| \ll |\mu|$$。

<details>

<summary>proof: 符號測度的零測度集合若且唯若全變差測度為0</summary>

給定$$\forall E \in \Sigma, |\mu|(E)=0 \implies \nu(E)=0$$。

因為$$|\mu|$$為正測度，由單調性得$$E$$為$$|\mu|$$零測集。

因為$$\forall F \in \Sigma, F \subseteq E$$，在$$\mu(F)=0$$，均可得$$\nu(F)=0$$，因此$$E$$也為$$\nu$$的零測集。

因為$$\nu(E)=0$$且$$E$$由\[零測度集合若且唯若全變差測度為0]得$$|\nu|(E)=0$$。

所以$$|\mu|(E)=0 \implies |\nu|(E)=0$$

(QED)

</details>

### 任意測度絕對連續於正測度

任意測度$$\nu$$(正測度、符號測度、複測度)與測度$$\mu: \Sigma \rightarrow [0,\infty]$$絕對連續，記為$$\nu \ll |\mu|$$若$$\forall E \in \Sigma, |\mu|(E)=0 \implies \nu(E)=0$$。

註：符號$$\ll$$可解釋為遠小於。

## 測度在集合集中(或測度在集合支撐(support on the set))

> 令$$\nu$$為可測空間$$(X, \Sigma)$$的任意測度(正測度、符號測度、複測度)。
>
> 稱測度$$\nu$$在可測集合$$E \in \Sigma$$是集中的(concentrated)若 $$\forall S \in \Sigma, ~ \nu(S) = \nu(S \cap E)$$。
>
> 等價定義: 測度$$\nu$$在可測集合$$E \in \Sigma$$是集中的(concentrated)若$$\forall S \in \Sigma, ~ S \cap E= \emptyset \implies \nu(S)=0$$。
>
> <mark style="color:red;">註：測度</mark>$$\nu$$<mark style="color:red;">在</mark>$$E^c$$<mark style="color:red;">中的任意可測子集的測度均為0。可說</mark>$$E$$<mark style="color:red;">為測度</mark>$$\nu$$<mark style="color:red;">的支撐集(support set)</mark>。
>
> [https://math.stackexchange.com/questions/956634/equivalence-of-definition-of-measure-concentrated-on-a-set-a](https://math.stackexchange.com/questions/956634/equivalence-of-definition-of-measure-concentrated-on-a-set-a)

任意可測集$$S = (S \cap E) \cup (S \cap E^c)$$，由$$\nu(S)=\nu(S \cap E)$$可得$$\nu(S \cap E^c)=0$$，<mark style="color:blue;">即</mark>$$S$$<mark style="color:blue;">的測度可用與集合</mark>$$E$$<mark style="color:blue;">的交集得出。而在集合</mark>$$E$$<mark style="color:blue;">之外的部份的量測值必為0</mark>。

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
> \[測度集中]如果能找到兩可測集合$$A, B \in \Sigma, ~ A \cap B=\emptyset$$使得$$\nu$$在$$A$$集中($$\forall E \in \Sigma, (E \cap A) =\emptyset \implies \mu(E)=0$$)，$$\mu$$在$$B$$集中($$\forall E \in \Sigma, (E \cap B) =\emptyset \implies \nu(E)=0$$)，則稱$$\nu, \mu$$相互奇異，記為$$\nu \perp \mu$$。
>
> \[零測集]$$X=A \cup B, ~ A \cap B=\emptyset$$且$$B$$為$$\nu$$的零測集($$\forall E \in \Sigma, E \subseteq B, \nu(E)=0)$$，$$A$$為$$\mu$$的零測集($$\forall E \in \Sigma, E \subseteq A, \mu(E)=0$$)，則$$\nu \perp \mu$$。

<details>

<summary>proof: 兩定義的等價性</summary>

集中=> 零測集

因為$$\nu$$在$$A$$集中，則$$\forall E \in \Sigma, E \cap A=\emptyset \implies \nu(E)=0$$。

因為$$A \cup B=X, ~ A \cap B=\emptyset$$，因此$$E \cap A=\emptyset \implies E \subseteq B$$，則$$\nu(E)=0$$，即$$B$$為$$\nu$$Ｄ的零測集。

同理可得$$A$$為$$\mu$$的零測集

(QED)

零測集=>集中

因為$$B$$為$$\nu$$的零測集，得$$\forall E \in \Sigma, E \subseteq B, \nu(E)=0$$。

因為$$A \cup B=X, ~ A \cap B=\emptyset$$，因此$$E \subseteq B \implies E \cap A=\emptyset$$，因此$$\nu(E \cap A)=0=\nu(E)$$，所以$$\nu$$在$$A$$集中。

同理可得$$\mu$$在$$B$$集中。

(QED)

</details>

### 絕對連續與相互奇異測度的性質

> 給定可測空間$$(X, \Sigma)$$，$$\nu, \nu_1, \nu_2$$為任意測度(正測度、符號測度、複測度)，$$\mu: \Sigma \rightarrow [0, \infty]$$為正測度，則：
>
> 1. 若$$\nu$$在$$E$$集中，則$$|\nu|$$在$$E$$集中。(因為在$$E$$之外的任意可測集均為$$\nu$$零測集)
> 2. 若$$\nu_1 \perp \nu_2$$，則$$|\nu_1| \perp |\nu_2|$$。
> 3. 若$$\nu_1 \perp \mu, ~ \nu_2 \perp \mu$$，則$$\nu_1 + \nu_2 \perp \mu$$。
> 4. 若$$\nu_1 \ll \mu, ~ \nu_2 \ll \mu$$，則$$\nu_1 + \nu_2 \ll \mu$$。
> 5. 若$$\nu \ll \mu$$，則$$|\nu| \ll \mu$$。\[已證明]
> 6. 若$$\nu_1 \ll \mu, ~ \nu_2 \perp \mu$$，則$$\nu_1 \perp \nu_2$$。
> 7. 若$$\nu \ll \mu, ~ \nu \perp \mu$$，則$$\nu=0$$。

<details>

<summary>proof 1: 由|v|為任意分割測度總和的最小上界=0得出</summary>

因為$$\nu$$在$$E$$集中，所以$$\forall S \in \Sigma, ~ S\cap E =\emptyset \implies \nu(S)=0$$。

且$$\forall Q \subseteq S, ~ Q \cap E=\emptyset \implies \nu(Q)=0$$。

因此$$S \subseteq E^c$$為$$\nu$$零測集。

令$$\displaystyle \mathbf{S}=\left\{\{S_n\}_{n=1}^\infty | \bigcup_{n=1}^\infty S_n =S, ~ S_i \cap S_j=\emptyset, \forall i \neq j\right\}$$為$$S$$的一組可數分割集合，則$$\nu(S_n)=0, \forall n$$。

可得$$\displaystyle |\nu|(S)=\sup_{\{S_n\} \in \mathbf{S}} \sum_{n=1}^\infty |\nu(S_n)| = 0$$

(QED)

</details>

<details>

<summary>proof2: 由1與相互奇異測度(以測度集中定義)得出。</summary>

令$$X =P \cup N$$為Hahn分解，且$$\nu_1$$在$$P$$集中，$$\nu_2$$在$$N$$集中。

由1得$$|\nu_1|$$在$$P$$集中且$$|\nu_2|$$在$$N$$集中。

由\[相互奇異測度(以測度集中定義)]定義得$$|\nu_1| \perp |\nu_2|$$。

(QED)

</details>

<details>

<summary>proof 3: Hahn的任意分解只會相差零測度集</summary>

$$(\nu_1+\nu_2)(E)\equiv \nu_1(E)+\nu_2(E)$$

令$$X =P_1 \cup N_1$$為Hahn分解，且$$\nu_1$$在$$P_1$$集中，$$\mu$$在$$N_1$$集中。

令$$X =P_2 \cup N_2$$為Hahn分解，且$$\nu_2$$在$$P_2$$集中，$$\mu$$在$$N_2$$集中。

因為Hahn的任意分解只會相差零測度集，即$$P_1 \oplus P_2 = (P_1 \cap P_2^c) \cup (P_1^c \cap P_2)$$為$$\mu$$零測集。而$$N_1 \oplus N_2 = (N_1 \cap N_2^c) \cup (N_1^c \cap N_2)$$為$$\nu_1$$或$$\nu_2$$零測集。

因此已知$$\mu$$在$$N_1 \oplus N_2$$集中， 只要證明$$\nu_1 + \nu_2$$在$$P_1 \oplus P_2$$集中。--(1)

$$\nu_1$$在$$P_1$$集中得$$\forall E \in \Sigma, E \subseteq P_1, \nu_1 (E)=\nu_1(E \cap P_1)$$。

$$\nu_2$$在$$P_2$$集中得$$\forall E \in \Sigma, E \subseteq P_2, \nu_2(E)=\nu_2(E \cap P_2)$$。

則$$\forall E \in \Sigma, E \subseteq (P_1 \oplus P_2)$$可折解得$$E \cap [(P_1 \cap P_2^c) \cup (P_1^c \cap P_2)]= (E\cap P_1 \cap P_2^c) \cup (E \cap P_1^c \cap P_2)$$，且$$(E\cap P_1 \cap P_2^c) \cap (E \cap P_1^c \cap P_2) =\emptyset$$

因此$$\nu_1(E)=\nu_1(E\cap P_1 \cap P_2^c) + \nu_1(E \cap P_1^c \cap P_2)= \nu_1(E\cap P_1)$$

同理得$$\nu_2(E)=\nu_2(E\cap P_1 \cap P_2^c) + \nu_2(E \cap P_1^c \cap P_2)= \nu_2(E\cap P_2)$$

因此$$\nu_1(E)+\nu_2(E)=\nu_1(E \cap P_1 \oplus P_2) + \nu_2(E \cap P_1 \oplus P_2)$$--(2)

由(1,2)得$$\nu_1 + \nu_2 \perp \mu$$

(QED)

</details>

<details>

<summary>proof 4: <span class="math">\mu</span>零測集可得<span class="math">\nu_1, \nu_2</span>零測集，因此<span class="math">\mu</span>的零測集仍為<span class="math">\nu_1+\nu_2</span>的零測集。</summary>

因為$$\nu_1 \ll \mu$$且$$\nu_2 \ll \mu$$，即$$\mu$$的零測集為$$\nu_1$$的零測集，同時也是$$\nu_2$$的零測集。

因此可得$$\mu$$的零測集為$$\nu_1 +\nu_2$$的零測集。

(QED)

</details>

<details>

<summary>proof 6:<span class="math">P,N</span>為<span class="math">X</span>的Hahn分解 ，<span class="math">N</span>為<span class="math">\nu_2</span>的零測集，<span class="math">P</span>為<span class="math">\mu</span>的零測集且的<span class="math">\mu</span>零測集為<span class="math">\nu_1</span>的零測集。</summary>

$$\nu_1 \ll \mu$$，所以$$\mu$$的零測集為$$\nu_1$$的零測集。--(1)

$$\nu_2 \perp \mu$$，則存在$$X=P \cup N, P \cap N =\emptyset$$ ，$$\nu_2$$在$$P$$集中，$$\mu$$在$$N$$集中。或者說$$N$$為$$\nu_2$$的零測集，$$P$$為$$\mu$$的零測集。--(2)

由(1)得$$P$$為$$\nu_1$$的零測集。--(3)

由(2,3)得$$N$$為$$\nu_2$$的零測集且$$P$$為$$\nu_1$$的零測集，因此$$\nu_1 \perp \nu_2$$。

(QED)

</details>

<details>

<summary>proof 7: 由6得<span class="math">\nu \perp \nu</span>，因此得<span class="math">\nu=0</span></summary>

由6得$$\nu \ll \mu$$且$$\nu \perp \mu$$，因此$$\nu \perp \nu$$。

令$$P, N$$為$$X$$的Hahn分解，且$$P,N$$為$$\nu$$的零測集。

即$$\forall E \in \Sigma, E \subseteq P \cup N=X, ~ \nu(E)=0$$&#x20;

(QED)

</details>

### 絕對連續測度與全變差測度和Jordan分解測度等價

> 給定可測空間$$(X, \Sigma)$$與符號測度$$\nu, \mu: \Sigma \rightarrow [-\infty, \infty)$$。
>
> $$\nu \ll |\mu| \iff |\nu| \ll |\mu| \iff \nu^{+} \ll |\mu| \iff \nu^{-} \ll |\mu|$$。
>
> 如果$$\mu$$為正測度，$$\nu$$為符號測度時：
>
> $$\nu \ll \mu \iff |\nu| \ll \mu \iff \nu^{+} \ll \mu \iff \nu^{-} \ll \mu$$
>
> * 符號測度的Jordan分解：$$\nu=\nu^{+} - \nu^{-}$$。其中$$\nu^{+}, \nu^{-}$$為正測度且不會同時為無窮大。
> * 全變差測度$$|\nu|=\nu^{+} + \nu^{-}$$。

<details>

<summary>proof: 零測度集合若且唯若全變差測度為0</summary>

給定可測空間$$(X, \Sigma)$$

給定$$\nu \ll \mu$$，則$$\forall E \in \Sigma, ~ \mu(E)=0 \implies \nu(E)=0$$。

因為$$E$$的任意可測子集在測度$$\nu$$中均為0，因此$$E$$為$$\nu$$零測集。

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
> * [https://math.stackexchange.com/questions/3053527/absolute-continuity-of-measure-and-epsilon-delta-condtion](https://math.stackexchange.com/questions/3053527/absolute-continuity-of-measure-and-epsilon-delta-condtion)
> * [https://math.stackexchange.com/questions/780824/equivalent-ideas-of-absolute-continuity-of-measures](https://math.stackexchange.com/questions/780824/equivalent-ideas-of-absolute-continuity-of-measures)

<details>

<summary>proof</summary>

<=

令$$E \in \Sigma, ~\mu(E)=0$$為$$\mu$$零測集。

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
