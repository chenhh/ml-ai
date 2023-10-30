---
description: signed measure
---

# 符號測度

一般討論測度$$u: \Sigma \rightarrow [0, \infty]$$要求其值域為非負值，而符號測度討論的是值域可為負值的情形。

<mark style="color:red;">Hahn分解可得宇集合可分割為正/負測集。</mark>

<mark style="color:red;">Jordan分解可得符號測度的本質表示：有號測度是兩正測度的差</mark>。

## 符號測度

> 給定可測空間$$(X, \Sigma)$$，定義符號測度$$\nu$$可取值$$\pm\infty$$(但不可同時為$$\pm \infty$$)即$$\nu: \Sigma \rightarrow (-\infty, \infty]$$或$$\nu: \Sigma \rightarrow [-\infty, \infty)$$，且滿足：
>
> 1. 定義域$$\Sigma$$為σ域
> 2. $$\nu(\empty)=0$$
> 3. $$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty \nu(E_n)$$，$$E_i \cap E_j = \empty$$且$$\bigcup_{n=1}^\infty E_n \in \Sigma$$。
>
> 此處要求當$$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) < \infty$$時，$$\displaystyle \sum_{n=1}^\infty \nu(E_n)$$ 為絕對收斂。
>
> 則稱$$\nu$$為符號測度。

由定義可知<mark style="color:green;">一般測度為有限測度</mark>的特例。

定義符號測度的應用：

1. 兩個(正)測度的差值時，如$$\nu(E)=\mu_1(E) - \mu_2(E), ~ E \in \Sigma$$，<mark style="color:blue;">其中</mark>$$\mu_1, \mu_2$$<mark style="color:blue;">至少一個為有限(正)測度(因為擴充實數中，兩個無窮大相減無定義)</mark>，且定義在同一個σ域$$\Sigma$$。
2. $$(X, \Sigma, \mu)$$為測度空間，$$f$$為測函數且$$f=f^{+} - f^{-}$$，若至少一個函數$$\int f^+<\infty$$或$$\int f^{-} <\infty$$(因為$$f=f^+-f^{-}$$，而擴充實數中，兩個無窮大相減無定義)，則$$\nu(E) = \int_E f d\mu = \int_E f^{+} d \mu - \int_E f^{-}d\mu$$為在$$(X, \Sigma)$$上的符號測度。

<mark style="color:red;">可證明任何一個符號測度可以分解為兩個有限測度的差值 (Hahn decomposition)或者為可測函數的積分</mark>。

### 測度的連續性

> 令$$\nu$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$\{E_n\}$$為$$\Sigma$$上的遞增集合，則$$\displaystyle \nu(\bigcup_{n=1}^\infty E_n)=\lim_{n \rightarrow \infty} \nu(E_n)$$。
>
> 若$$\{E_n\}$$為$$\Sigma$$上的遞減集合且$$\nu(E_1)\neq \pm \infty$$，則$$\displaystyle \nu(\bigcap_{n=1}^\infty E_n)=\lim_{n \rightarrow \infty} \nu(E_n)$$。
>
> 註：此性質和[正測度的連續性](../measure.md#di-zeng-ji-he-ji-xian-de-ce-du-ce-du-de-lian-xu-xing-continuity-of-measure)相同。

### 有限測集的子集仍為有限測集

> 令$$\nu$$為$$(X, \Sigma)$$上的符號測度。
>
> $$F \subseteq E$$為可測集，若$$|\nu(E)|<\infty$$，則$$|\nu(F)|<\infty$$。

<details>

<summary> proof: 反證法</summary>

$$F \subseteq E \Rightarrow E=F \cup(E-F)$$。--(1)

不失一般性令$$\nu(F)=\infty$$。則$$\nu: \Sigma \rightarrow (-\infty, \infty]$$。--(2)

由(1,2)得$$\nu(E)=\infty$$ (QED)

</details>

## 正測集與負測集(positive set and negative set)

> 令$$\nu$$為符號測度，則
>
> * 稱$$A$$在測度$$\mu$$下為<mark style="color:red;">正測集(positive set)</mark>，若$$\forall E \subseteq A$$為可測集合且$$\nu(E) \geq 0$$。記為$$A \geq 0$$。
> * 稱$$B$$在測度$$\mu$$下為<mark style="color:red;">負測集(negative set)</mark>，若$$\forall E \subseteq B$$為可測集合且$$\nu(E) \leq 0$$。記為$$B \leq 0$$。
> * 稱$$C$$在測度$$\mu$$下<mark style="color:red;">零測集(null set)</mark>，若$$\forall E \subseteq C$$為可測集合且$$\nu(E)=0$$。記為$$C=0$$。
>
> 註：零測集同時為正測集與負測集。
>
> 正測集就是其所有可測子集的符號測度都是大於等於0。負測集就是其所有可測子集的符
>
> 號測度都是小於等於0
>
> [https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets](https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets)

以$$\nu(E)=\int_E f d\mu$$為例，正測集即$$f \geq 0 \text{ a.e. on }  E$$，負測集則$$f \leq 0 \text{ a.e. on } E$$，零測集則$$f = 0 \text{ a.e. on } E$$。

### 正(負)測集的性質

> 令$$\nu$$為$$(X, \Sigma)$$上的符號測度。
>
> * \[正測集的可測子集為正測集]若$$E$$為正測集，則$$\forall F \subseteq E$$且$$F$$為可測集，則$$F$$為正測集。
> * \[正測集的可數聯集為正測集]$$\{E_n\}$$為正測集序列，則$$\bigcup_{n=1}^\infty E_n$$為正測集。
> * \[正測集的測度單調性]若$$E$$為正測集，$$F \subseteq E$$為可測集，則$$\nu(F) \leq \nu(E)$$。
> * \[零測集同時為正負測集]$$P$$為正測集，$$N$$為負測集，則$$P \cap N$$為零測集。

<details>

<summary>proof: 將集合拆解為互斥集合</summary>

因為$$E$$為正測集且$$F \subseteq E$$，由定義得$$\nu(E) \geq 0$$。--(1)

令可測集$$G \subseteq F$$，可得$$G \subseteq E$$，由正測集定義得$$\nu(G) \geq 0$$。--(2)

由(1,2)得$$F$$為正測集。

(QED)

令$$F_n = E_n - \bigcup_{n=1}^{n-1} E_n$$，可得$$F_n \subseteq E_n$$，由正測集定義得$$\nu(F_n)\geq 0$$。

因此若$$S \subseteq \bigcup_{n=1}^\infty E_n$$，則$$\nu(S)=\sum_{n=1}^\infty \nu(S \cap F_n) \geq 0$$ (QED)

$$F \subseteq E$$可得$$E=F \cup (E-F)$$。

由測度定義得$$\nu(E)=\nu(F) + \nu(E-F)$$。

因為$$E-F \subseteq E$$且可測，由正測集定義得$$\nu(E-F) \geq 0$$。

因此$$\nu(E) \geq \nu(F)$$ (QED)

令$$F \subseteq P \cap N$$為可測集，則$$F \subseteq P$$且$$F \subseteq N$$。

由正/負測集定義得$$\nu(F) \geq 0$$且$$\nu(F) \leq 0$$，因此$$\nu(F)=0$$ (QED)

</details>

### 有限非負測度集合包含正測集

> 令$$\nu$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$E \in \Sigma, ~ 0 \leq \nu(E) <\infty$$，則存在可測子集$$F \subseteq E$$且$$F$$為正測集。
>
> 註：$$E$$只是測度大於等於0，不一定為正測集。如果$$E$$是正測集時，依定義必滿足條件。

<details>

<summary>proof: 遞迴排除E中的負測度集，排除後(可能有無窮多個)剩下的集合為正測集。</summary>

如果$$E$$為正測集，由\[正(負)測集的性質/正測集的可測子集為正測集]得其任意可測子集為正測集。

若$$E$$非正測集，則存在可測子集$$E_1 \subseteq E$$且$$\nu(E_1) < 0$$。則存在最小的自然數$$n_1$$滿足以下條件：$$\exists n_1 \in \mathbb{N} \ni \nu(E_1) < -1/n, \forall n \geq n_1$$。

如果$$E-E_1$$為正測集，則證明完成。否則遞迴從$$E-E_1$$中存在可測子集$$E_2 \subseteq E-E_1$$且$$\nu(E_2) < 0$$。則存在最小的自然數$$n_2$$滿足以下條件$$\exists n_2 \in \mathbb{N} \ni \nu(E_2) < -1/n, \forall n \geq n_2$$。

做到第$$k$$步，如果$$E-\bigcup_{i=1}^k E_i$$不是正測集，則$$E-\bigcup_{i=1}^k E_i$$存在可測子集$$E_k \subseteq E-\bigcup_{i=1}^k E_i$$且$$\nu(E_k) < 0$$。則存在最小的自然數$$n_k$$滿足以下條件$$\exists n_k \in \mathbb{N} \ni \nu(E_k) < -1/n, \forall n \geq n_k$$

如果在有限步內無法完成，令$$S=E-\bigcup_{i=1}^\infty E_i$$。即$$E= S \bigcup (\bigcup_{i=1}^\infty E_i)$$。因為在建構過程中$$S$$與$$E_i$$兩兩互斥， 由測度定義得$$\nu(E)=\nu(S)+\sum_{i=1}^{\infty} \nu(E_i)$$--(1)。

因為假設$$\nu(E) <\infty$$，因此$$\sum_{i=1}^{\infty} \nu(E_i)$$必須[絕對收斂](../series/series-convergence-test.md#jue-dui-shou-lian-yu-tiao-jian-shou-lian)。因此當$$\displaystyle \lim_{i \rightarrow \infty} |\nu(E_i)|=0$$。因為$$\nu(E_i) > 1/n_i$$，因此$$\displaystyle \lim_{i \rightarrow \infty} n_i = \infty$$。--(2)

取可測子集$$F \subseteq S$$，因為$$S=E-\bigcup_{i=1}^\infty E_i$$，所以$$F \subseteq E-\bigcup_{i=1}^\infty E_i$$--(3)。

由(3)假設$$\nu(F) < - 1/(n_i-1), i \in \mathbb{N}$$。

可得$$\nu(F)<-1/(n_i-1) < -1/n_i$$，因此$$F \in  E_i$$ 但這與(3)矛盾。因此$$\nu(F) \geq -1/(n_i-1), \forall i \in \mathbb{N}$$--(4)

由(2,4)得$$\nu(F) \geq 0$$，因此$$S$$為正測集(QED)

</details>

### 有限符號測度中集合的測度存在正測集的測度大於集合測度

> 令$$\nu: X\rightarrow [-\infty, \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$E \in \Sigma$$，$$\nu(E)\neq \infty$$，則存在可測子集$$P \subseteq E \ni \nu(P) > \nu(E)$$。

## Hahn分解定理(The Hahn decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，令$$\nu$$為符號測度，則存在正集合$$A$$與負集合$$B$$(均在測度$$\nu$$下)滿足：
>
> $$X = A \cup B$$且$$A\cap B = \emptyset$$。
>
> 若$$E, F$$為另一組滿足上述條件的集合，則$$A \cap E=B \cap F$$在測度$$\nu$$下為零測集。
>
> <mark style="color:red;">註：Hahn分解可得宇集合可分割為正/負測集</mark>。
>
> Hahn分解不唯一(因為有零測集存在)。
>
> 如果$$X$$不存在零測集時，則Hahn分解唯一。
>
> [https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem](https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem)
>
> [https://zhuanlan.zhihu.com/p/36652587](https://zhuanlan.zhihu.com/p/36652587)

<details>

<summary>proof</summary>

假設$$\nu: \Sigma \rightarrow [-\infty, \infty)$$。\[若值域為$$(-\infty, \infty]$$時，討論$$-\nu$$即可]

對於$$X$$上的所有正測集集合族$$A_0$$，取$$\displaystyle M=\sup_{A_0 \geq 0} \nu(A_0)$$--(1)。

因為$$M$$為正測集的上確界且有界($$M < \infty$$)，由\[[實數單調有界定理](../sequence/monotonic-sequence.md#shi-shu-chan-diao-you-jie-ding-li-bounded-convergence-theorem)]存在測度遞增正測集合序列$$\displaystyle  \{A_j \geq 0\} \ni \lim_{j \rightarrow \infty} \nu(A_j) =M$$。(注意是$$\nu(A_j) \leq \nu(A_{j+1})$$，而不是$$A_j \subseteq A_{j+1}$$)

令$$A = \bigcup_{j=1}^\infty A_j$$，由\[正測集的可數聯集為正測集]得$$A$$為正測集。i由(1)得$$\nu(A) \leq M$$。--(2)

因為$$A = \bigcup_{j=1}^\infty A_j \supseteq A_j$$，由\[正測集的測度單調性]得$$\nu(A) \geq \nu(A_j)$$，因此$$\displaystyle \lim_{j \rightarrow \infty} \nu(A) \geq \lim_{j \rightarrow \infty} \nu(A_j)\implies \nu(A) \geq M$$--(3)

由(2,3)得$$\nu(A)=M$$--(4)

\[反證法]令$$B=X-A$$且假設$$B$$不是負測集。

因此存在可測子集$$E \subseteq B \ni \nu(E) > 0$$。

由\[有限非負測度集合包含正測集]得存在$$F \subseteq E \ni \nu(F) \geq 0$$，且$$F \cap A = \emptyset$$，且$$F \cup A$$為正測集。

因此$$M \geq \nu(F \cup A) = \nu(F) + \nu(A) = \nu(F) + M$$

因此若$$\nu(F) > 0$$時，會得到$$M > M$$的矛盾，因此只能得到$$\nu(F) =0$$。但這又與$$\nu(E) > 0$$的假設矛盾，因此$$B$$為負測集&#x20;

(QED)

</details>

## 相互奇異(正交)測度(mutually signular measures)

> 在可測空間$$(X, \Sigma)$$中，令$$\mu,\nu$$為符號測度。
>
> 稱$$\mu, \nu$$兩測度相互奇異(mutually signularity)或$$\nu$$相對於$$\mu$$奇異($$\nu$$ si singularity w.r.t. $$\mu$$)若：
>
> ($$E,F$$為$$X$$的可測分割且$$E$$為$$\mu$$的零測集，$$F$$為$$\nu$$的零測集)，$$\exists E,F \in \Sigma$$，$$E \cap F=\emptyset$$，$$E \cup F = X$$ 且$$\mu(E)=0, \nu(F)=0$$。
>
> <mark style="color:red;">常將此兩測度用正交符號記為：</mark>$$\mu \perp \nu$$<mark style="color:red;">。</mark>

註：可測函數$$f=f^{+}-f^{-}$$，其中集合$$({f^{+}})^{-1}$$與$$({f^{-}})^{-1}$$在各自的符號測度下相互奇異(正交)。

## Jordan分解定理(the Jordan decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，$$\nu$$為符號測度。
>
> 存在唯一的(正)測度$$\nu^{+}$$與$$\nu^{-}$$使得$$\nu=\nu^{+}-\nu^{-}$$且$$\nu^{+} \perp \nu^{-}$$。

## 參考資料

* [https://zhuanlan.zhihu.com/p/274555361](https://zhuanlan.zhihu.com/p/274555361)
* [https://www.ams.org/proc/1980-080-02/S0002-9939-1980-0577778-7/S0002-9939-1980-0577778-7.pdf](https://www.ams.org/proc/1980-080-02/S0002-9939-1980-0577778-7/S0002-9939-1980-0577778-7.pdf)
