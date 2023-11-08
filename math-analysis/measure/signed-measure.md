---
description: signed measure
---

# 符號測度

## 簡介

在討論(正)測度的線性組合時，自然會考慮到測度為負值的情形。即在可測空間$$(X, \Sigma)$$中定義兩測度$$\mu_1, \mu_2$$，在相加時測度仍為正值沒問題，但若兩測度相減如$$\nu(E)=\mu_1(E)-\mu_2(E)$$時的定義，就必須避開$$\mu_1, \mu_2$$同時為無窮大的情形。

一般討論測度$$u: \Sigma \rightarrow [0, \infty]$$要求其值域為非負值，而符號測度討論的是值域可為負值的情形，但正/負無窮大只能取一，即$$\nu: \Sigma \rightarrow [-\infty, \infty) \text{ or } \nu: \Sigma \rightarrow (-\infty, \infty]$$。

<mark style="color:red;">Hahn分解可得宇集合可分割為正/負測集。</mark>Hahn分解定理的一個重要的推論是Jordan分解定理，任何一個符號測度都可以像實值函數那樣分解成正部與負部的差。

<mark style="color:red;">Jordan分解可得符號測度的本質表示：(有限)符號測度是兩(有限)正測度的差(而且是(正)測度值最小的分解)</mark>。

由Jordan分解的結果可定義符號測度的積分：$$\displaystyle \int_X f d\mu = \int_X f d\mu^{+} - \int_X f d\mu^{-}$$。等號在兩側積分存在時成立。

若全變差測度$$|\nu|$$為有限(σ-有限)測度，則符號測度$$\nu$$為有限(σ-有限)測度。

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>來源: <a href="https://zhuanlan.zhihu.com/p/36652587">https://zhuanlan.zhihu.com/p/36652587</a></p></figcaption></figure>

## 符號測度

> 給定可測空間$$(X, \Sigma)$$，定義符號測度$$\nu$$可取值$$\pm\infty$$(但不可同時為$$\pm \infty$$)即$$\nu: \Sigma \rightarrow (-\infty, \infty]$$或$$\nu: \Sigma \rightarrow [-\infty, \infty)$$避免出現無窮大符號之間沒有定義的行為出現，且滿足：
>
> 1. 定義域$$\Sigma$$為σ域，且值域一般是使用$$[-\infty, \infty)$$。
> 2. $$\nu(\empty)=0$$
> 3. $$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty \nu(E_n)$$，$$E_i \cap E_j = \empty$$且$$\bigcup_{n=1}^\infty E_n \in \Sigma$$。
>
> 此處要求當$$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) < \infty$$時，$$\displaystyle \sum_{n=1}^\infty \nu(E_n)$$ 為絕對收斂(converges absoulutely)。
>
> 則稱$$\nu$$為符號測度。

由定義可知<mark style="color:red;">一般測度為有限測度的特例</mark>。

如果$$\nu: \Sigma \rightarrow (-\infty, \infty)$$時，稱為<mark style="color:red;">有限符號測度</mark>。

定義符號測度的應用：

1. 兩個(正)測度的差值時，如$$\nu(E)=\mu_1(E) - \mu_2(E), ~ E \in \Sigma$$，<mark style="color:blue;">其中</mark>$$\mu_1, \mu_2$$<mark style="color:blue;">至少一個為有限(正)測度(因為擴充實數中，兩個無窮大相減無定義)</mark>，且定義在同一個σ域$$\Sigma$$。
2. $$(X, \Sigma, \mu)$$為測度空間，$$f$$為測函數且$$f=f^{+} - f^{-}$$，若至少一個函數$$\int f^+<\infty$$或$$\int f^{-} <\infty$$(因為$$f=f^+-f^{-}$$，而擴充實數中，兩個無窮大相減無定義)，則$$\nu(E) = \int_E f d\mu = \int_E f^{+} d \mu - \int_E f^{-}d\mu$$為在$$(X, \Sigma)$$上的符號測度。

<mark style="color:red;">可證明任何一個符號測度可以分解為兩個有限測度的差值 (Hahn decomposition)或者為可測函數的積分</mark>。

### 測度的連續性

> 令$$\nu: \Sigma \rightarrow [-\infty, \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$\{E_n\}$$為$$\Sigma$$上的遞增集合，則$$\displaystyle \nu(\bigcup_{n=1}^\infty E_n)=\lim_{n \rightarrow \infty} \nu(E_n)$$。
>
> 若$$\{E_n\}$$為$$\Sigma$$上的遞減集合且$$\nu(E_1)\neq \pm \infty$$，則$$\displaystyle \nu(\bigcap_{n=1}^\infty E_n)=\lim_{n \rightarrow \infty} \nu(E_n)$$。
>
> 註：此性質和[正測度的連續性](../measure.md#di-zeng-ji-he-ji-xian-de-ce-du-ce-du-de-lian-xu-xing-continuity-of-measure)相同。

### 有限測集的子集仍為有限測集

> 令$$\nu: \Sigma \rightarrow [-\infty, \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> $$F \subseteq E$$為可測集，若$$|\nu(E)|<\infty$$，則$$|\nu(F)|<\infty$$。

<details>

<summary> proof: 反證法</summary>

$$F \subseteq E \Rightarrow E=F \cup(E-F)$$。--(1)

不失一般性令$$|\nu(F)|=\infty$$，即$$\nu(F)=-\infty$$--(2)

由(1,2)得$$\nu(E)=-\infty$$ ，即$$|\nu(E)|=\infty$$ (QED)

</details>

## 正測集與負測集(positive set and negative set)

> 令$$\nu: \Sigma \rightarrow [-\infty, \infty)$$為符號測度，則
>
> * 稱$$A$$在測度$$\mu$$下為<mark style="color:red;">正測集(positive set)</mark>，若任意可測子集測度均大於等於0$$\forall E \subseteq A, ~ E \in \Sigma, ~\mu(E) \geq 0$$。記為$$A \geq 0$$。
> * 稱$$B$$在測度$$\mu$$下為<mark style="color:red;">負測集(negative set)</mark>，若任意可測子集測度均小於等於0。若$$\forall E \subseteq B, ~ E \in \Sigma, ~\mu(E) \leq 0$$。記為$$B \leq 0$$。
> * 稱$$C$$在測度$$\mu$$下<mark style="color:red;">零測集(null set)</mark>，若若任意可測子集測度均等於0。$$\forall E \subseteq C, ~ E \in \Sigma, ~\mu(E) = 0$$。記為$$C=0$$。
>
> 註：零測集同時為正測集與負測集。
>
> [https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets](https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets)

令$$P$$為$$X$$中的最大正測集，則$$N=X-P$$為負測集且不含零測集，即$$\forall E \subseteq N, E \in \Sigma, \nu(E)<0$$。同理令$$N$$為$$X$$中的最大負測集，則$$P=X-N$$為負測集且不含零測集，即$$\forall E \in P, E \in \Sigma,  \mu(E)>0$$。

以$$\nu(E)=\int_E f d\mu$$為例，正測集即$$\int_E f \geq 0 \text{ a.e. on }  E$$，負測集則$$\int_E f \leq 0 \text{ a.e. on }  E$$，零測集則$$\int_E f = 0 \text{ a.e. on } E$$。<mark style="color:blue;">注意此處的測度值是</mark>$$f$$<mark style="color:blue;">在集合</mark>$$E$$<mark style="color:blue;">的積分值，而非函數值</mark>。

### 正(負)測集的性質

> 令$$\nu: \Sigma \rightarrow [-\infty , \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> * <mark style="color:red;">\[正測集的可測子集為正測集]</mark>若$$E$$為正測集，則$$\forall F \subseteq E$$且$$F$$為可測集，則$$F$$為正測集。
> * <mark style="color:red;">\[正測集的可數聯集為正測集]</mark>$$\{E_n\}$$為正測集序列，則$$\bigcup_{n=1}^\infty E_n$$為正測集。
> * <mark style="color:red;">\[正測集的測度單調性]</mark>若$$E$$為正測集，$$F \subseteq E$$為可測集，則$$\nu(F) \leq \nu(E)$$。
> * <mark style="color:red;">\[零測集同時為正負測集]</mark>$$P$$為正測集，$$N$$為負測集，則$$P \cap N$$為零測集。

<details>

<summary>proof: 將集合拆解為互斥集合</summary>

因為$$E$$為正測集且$$F \subseteq E$$，由定義得$$\nu(F) \geq 0$$。--(1)

令可測集$$G \subseteq F$$，可得$$G \subseteq E$$，由正測集定義得$$\nu(G) \geq 0$$。--(2)

由(1,2)得$$F$$為正測集。

(QED)

令$$F_n = E_n - \bigcup_{n=1}^{n-1} E_n$$，可得$$F_n \subseteq E_n$$，由正測集定義得$$\nu(F_n)\geq 0$$。

因此若$$S \subseteq \bigcup_{n=1}^\infty E_n$$，則$$\nu(S)=\sum_{n=1}^\infty \nu(S \cap F_n) \geq 0$$&#x20;

(QED)

$$F \subseteq E$$可得$$E=F \cup (E-F)$$。

由測度定義得$$\nu(E)=\nu(F) + \nu(E-F)$$。

因為$$E-F \subseteq E$$且可測，由正測集定義得$$\nu(E-F) \geq 0$$。

因此$$\nu(E) \geq \nu(F)$$&#x20;

(QED)

令$$F \subseteq P \cap N$$為可測集，則$$F \subseteq P$$且$$F \subseteq N$$。

由正/負測集定義得$$\nu(F) \geq 0$$且$$\nu(F) \leq 0$$，因此$$\nu(F)=0$$ (QED)

</details>

### 有限正值測度集合包含正測集且測度為正值(Hahn's lemma)

> 令$$\nu: \Sigma \rightarrow [-\infty, \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$E$$為有限可測集合且測度為正值($$E \in \Sigma, ~ 0 < \nu(E) <\infty$$)，則存在可測子集$$F \subseteq E$$，$$F$$為正測集且$$\nu(F) > 0$$。。
>
> 註：$$E$$只是測度大於0，不一定為正測集。如果$$E$$是正測集時，依定義必滿足條件。

<details>

<summary>proof: 遞迴排除E中的負測度值集合後，排除後(可能有無窮多個)剩下的集合為正測集且不含零測集。</summary>

如果$$E$$為正測集，由\[正(負)測集的性質/正測集的可測子集為正測集]得其任意可測子集為正測集, 排除掉零測集之後即為所求。

若$$E$$非正測集，則存在可測子集$$E_1 \subseteq E$$且$$\nu(E_1) < 0$$。則存在最小的自然數$$n_1$$滿足以下條件：$$\exists n_1 \in \mathbb{N} \ni \nu(E_1) < -1/n, \forall n \geq n_1$$。

如果$$E-E_1$$為正測集，則證明完成。否則遞迴從$$E-E_1$$中存在可測子集$$E_2 \subseteq E-E_1$$且$$\nu(E_2) < 0$$。則存在最小的自然數$$n_2$$滿足以下條件$$\exists n_2 \in \mathbb{N} \ni \nu(E_2) < -1/n, \forall n \geq n_2$$。

做到第$$k$$步，如果$$E-\bigcup_{i=1}^k E_i$$不是正測集，則$$E-\bigcup_{i=1}^k E_i$$存在可測子集$$E_k \subseteq E-\bigcup_{i=1}^k E_i$$且$$\nu(E_k) < 0$$。則存在最小的自然數$$n_k$$滿足以下條件$$\exists n_k \in \mathbb{N} \ni \nu(E_k) < -1/n, \forall n \geq n_k$$

如果在有限步內無法完成，令$$S=E-\bigcup_{i=1}^\infty E_i$$。即$$E= S \bigcup (\bigcup_{i=1}^\infty E_i)$$。因為在建構過程中$$S$$與$$E_i$$兩兩互斥， 由測度定義得$$\nu(E)=\nu(S)+\sum_{i=1}^{\infty} \nu(E_i)$$--(1)。

因為假設$$\nu(E) <\infty$$，由定義得$$\sum_{i=1}^{\infty} \nu(E_i)$$必須[絕對收斂](../series/series-convergence-test.md#jue-dui-shou-lian-yu-tiao-jian-shou-lian)即$$\displaystyle \sum_{i=1}^\infty |\nu(E_i)|<\infty$$。

因此得$$\displaystyle \lim_{i \rightarrow \infty} |\nu(E_i)|=0$$。因為$$\nu(E_i) <- 1/n_i$$，因此$$\displaystyle \lim_{i \rightarrow \infty} n_i = \infty$$。--(2)

接下來證明$$S$$為正測集。

取可測子集$$F \subseteq S$$，因為$$S=E-\bigcup_{i=1}^\infty E_i$$，所以$$F \subseteq E-\bigcup_{i=1}^\infty E_i$$--(3)。

由(3)假設$$\nu(F) < - 1/(n_i-1), i \in \mathbb{N}$$。

可得$$\nu(F)<-1/(n_i-1) < -1/n_i$$，因此$$F \in  E_i$$ 但這與(3)矛盾。因此$$\nu(F) \geq -1/(n_i-1), \forall i \in \mathbb{N}$$--(4)

由(2,4)得$$\nu(F) \geq 0$$，因此$$S$$為正測集。

因為$$\nu(E)=\nu(S)+\sum_{i=1}^{\infty} \nu(E_i) > 0$$且$$\nu(\sum_{i=1}^{\infty} \nu(E_i)) <0$$因此$$\nu(S) > 0$$ (QED)

</details>

### 有限符號測度中的集合中存在正測集的測度大於集合測度

> 令$$\nu: X\rightarrow [-\infty, \infty)$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$E \in \Sigma$$，$$\nu(E)\neq -\infty$$(有限測度)，則存在正測集$$P \subseteq E \ni \nu(P) \geq  \nu(E)$$。

## Hahn分解定理(The Hahn decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，令$$\nu : \Sigma \rightarrow [-\infty, \infty)$$為符號測度，則存在正測集$$A$$與負測集$$B$$(均在測度$$\nu$$下)滿足：
>
> $$X = A \cup B$$且$$A\cap B = \emptyset$$。
>
> 若$$E, F$$為另一組滿足上述條件的集合，則$$A \cap E=B \cap F$$在測度$$\nu$$下為零測集或者說$$A \oplus E = (A \cap E^c) \cup (A^c \cap E)$$在測度$$\nu$$下為零測集。
>
> <mark style="color:red;">註：Hahn分解可得宇集合(在任意符號測度下)可分割為正/負測集</mark>。
>
> Hahn分解不唯一(因為有零測集存在)。
>
> 如果$$X$$不存在零測集時，則Hahn分解唯一。
>
> [https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem](https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem)
>
> [https://zhuanlan.zhihu.com/p/36652587](https://zhuanlan.zhihu.com/p/36652587)

<details>

<summary>proof: 找到一個“最大”的正測集，再來證明它的補集一定是負測集。</summary>

假設$$\nu: \Sigma \rightarrow [-\infty, \infty)$$。\[若值域為$$(-\infty, \infty]$$時，討論$$-\nu$$即可]

對於$$X$$上的所有正測集集合族$$\mathbb{A}_0 =\{A \in \Sigma ~|~ A \geq 0\}$$，取$$\displaystyle M=\sup_{A \in \mathbb{A}_0} \nu(A)<\infty$$為正測集的測度值最小上界。可得$$M \geq 0$$--(1)。

因為$$M$$為正測集的上確界且有界($$M < \infty$$)，由\[[實數單調有界定理](../sequence/monotonic-sequence.md#shi-shu-chan-diao-you-jie-ding-li-bounded-convergence-theorem)]存在測度遞增正測集合序列$$\displaystyle  \{A_j \geq 0\} \ni \lim_{j \rightarrow \infty} \nu(A_j) =M$$。(注意是$$\nu(A_j) \leq \nu(A_{j+1})$$，而不是$$A_j \subseteq A_{j+1}$$)

令$$A = \bigcup_{j=1}^\infty A_j$$，由\[正測集的可數聯集為正測集]得$$A$$為正測集。由(1)得$$\nu(A) \leq M$$。--(2)

因為$$A = \bigcup_{j=1}^\infty A_j \supseteq A_j~,\forall j \in \mathbb{N}$$，由\[正測集的測度單調性]得$$\nu(A) \geq \nu(A_j)$$，因此$$\displaystyle \nu(A) \geq \lim_{j \rightarrow \infty} \nu(A_j)\implies \nu(A) \geq M$$--(3)

由(2,3)得$$\nu(A)=M$$，即$$A$$的測度等於正測集的最小上界--(4)

\[反證法]令$$B=X-A$$且假設$$B$$不是負測集。

則存在可測且測度為有限正值的子集合(但不一定是正測集)$$E \subseteq B \ni 0< \nu(E) <\infty$$。

由\[Hahn's lemma]得存在正測子集$$F \subseteq E \ni \nu(F) > 0$$。

可得$$F \cap A = \emptyset$$，且$$F \cup A$$為正測集。

由(1)得$$M \geq \nu(F \cup A) = \nu(F) + \nu(A) = \nu(F) + M$$，因此得到$$\nu(F) =0$$。

但這又與$$\nu(F) > 0$$的假設矛盾，因此$$B$$為負測集&#x20;

(QED)

</details>

## 相互奇異(正交)測度(mutually singular measures)

> 在可測空間$$(X, \Sigma)$$中，令$$\mu,\nu: \Sigma \rightarrow [-\infty, \infty)$$為符號測度。
>
> 稱$$\mu, \nu$$兩測度相互奇異(mutually singularity)或$$\nu$$相對於$$\mu$$奇異($$\nu$$ is singularity w.r.t. $$\mu$$)若：
>
> ($$E,F$$為$$X$$的可測分割且$$E$$為$$\mu$$的零測集，$$F$$為$$\nu$$的零測集)。
>
> $$\exists E,F \in \Sigma$$，$$E \cap F=\emptyset$$，$$E \cup F = X$$ $$\mu(E)=0, \nu(F)=0$$且$$\forall E_s \in \Sigma, E_s \subseteq E,~ \mu(E_s) =0$$，$$\forall F_s \in \Sigma, F_s \subseteq F,~ \nu(F_s) =0$$。
>
> <mark style="color:red;">常將此兩測度用正交符號記為：</mark>$$\mu \perp \nu$$<mark style="color:red;">。</mark>

註：可測函數$$f=f^{+}-f^{-}$$，其中集合$$({f^{+}})^{-1}$$與$$({f^{-}})^{-1}$$在各自的符號測度下相互奇異(正交)。

## Jordan分解定理(the Jordan decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，$$\mu: \Sigma \rightarrow [-\infty, \infty)$$為符號測度。
>
> 存在唯一的(正)測度$$\nu^{+}$$與$$\nu^{-}$$使得$$\nu=\nu^{+}-\nu^{-}$$($$\forall E \in \Sigma, ~\nu(E)=\nu^{+}(E)-\nu^{-}(E)$$)且$$\nu^{+} \perp \nu^{-}$$。
>
> 其中$$\nu^{+}, \nu^{-}: \Sigma \rightarrow [0, \infty]$$至少有一個測度為實數值(不可同時為無窮大)。

註：唯一性是指相異測度對同一集合的測度值相等，即$$\nu(E)=\mu(E)$$。

如果$$\nu^{+}<\infty$$且$$\nu^{-}<\infty$$，則稱$$\nu$$為<mark style="color:red;">有限符號測度(finite signed measure)</mark>。

$$X=P \cup N$$為測度$$\nu$$的Hahn分解。$$\nu^{+}(S)=\nu(S \cap P), ~\nu^{-}(S)=\nu(S \cap N)$$

$$\nu^{+}, \nu^{-}$$也稱為符號測度$$\nu$$的<mark style="color:red;">正/負變差(positive/negative variation)</mark>。$$\nu=\nu^{+}-\nu^{-}$$稱為<mark style="color:red;">Jordan(測度)分解</mark>。類似於遞增函數的分解。

<mark style="color:red;">符號測度</mark>$$\nu$$<mark style="color:red;">的全變差(total variation)</mark>定義為$$|\nu|=\nu^{+} + \nu^{-}$$。注意全變差測度為(正)測度。

<details>

<summary>proof: 任意集合依Hann分解定理可分割為正/負測集。再定義正/負測集的正測度即為所求。</summary>

令$$X=P \cup N$$為測度$$\nu$$的Hahn分解。

存在性：

$$\forall S \in \Sigma$$，定義$$\nu^{+}(S)=\nu(S \cap P)$$，$$\nu^{-}(S)=-\nu(S \cap N)$$。

因此可得$$\nu(S)=\nu^{+}(S) - \nu^{-}(S)$$且$$\nu^{+}(S) \perp \nu^{-}(S)$$。&#x20;

唯一性：

令$$\nu=\mu^{+} - \mu^{-}$$且$$\mu^{+} \perp \mu^{-}$$。

令$$E, F \in \Sigma, ~ E \cap F = \emptyset, ~ E \cup F= X$$且$$\mu^{+}(F)=\mu^{-}(E)=0$$。

則$$X=E \cup F$$為測度$$\nu$$的另一組Hahn分解。

由Hahn 分解可得$$P \oplus E = (P \cap E^c) \cup (P^c \cap E)$$為$$\nu$$的零測集。

可得$$\forall A \in \Sigma, ~ \mu^{+}(A)=\mu^{+}(A \cap E) =\nu(A \cap E)=\nu(A \cap E)=\nu^{+}(A)$$。

同理可得$$\mu^{-}(A)=\nu^{-}(A)$$。

(QED)

</details>

### 範例：可積函數的Jordan分解

$$f: \mathbb{R} \rightarrow \mathbb{R}$$為實數上的可積分函數，給定可測集合$$E \in \mathcal{B}$$，定義符號測度$$\displaystyle \nu(E)=\int_E f dm < \infty$$。

定義$$A =\{ x \in \mathbb{R} ~|~ f(x) \geq 0\}$$，$$B =\{ x \in \mathbb{R} | f(x) <0\}$$。

定義(正)測度：

* $$\displaystyle \nu^{+}(E)=\int_{A \cap E}f dm$$
* $$\displaystyle \nu^{-}(E)=-\int_{B \cap E}f dm$$

則$$\{A, B\}$$為實數上相對於符號測度$$\nu$$的Hahn分解。$$\nu^{+}, \nu^{-}$$是符號測度$$\nu$$的Jordan分解。

### 正負變差與全變差測度的不等式

> 在可測空間$$(X, \Sigma)$$中，$$\nu$$為符號測度，則$$\forall E \in \Sigma$$：
>
> * $$\nu^{-}(E) \leq \nu(E) \leq \nu^{+}(E)$$。
> * $$|\nu(E)| \leq |\nu|(E)$$。

###

### 有限符號測度的Jordan分解是測度的最小上界/最大下界

> 在可測空間$$(X, \Sigma)$$中，$$\nu$$為有限符號測度，則：
>
> $$\nu = \nu^{+} - \nu^{-}$$且$$\forall E \in \Sigma$$：
>
> * $$\displaystyle \nu^{+}(E)=\sup_{B \in \Sigma, B \subseteq E}\nu(B)$$。
> * $$\displaystyle \nu^{-}(E)=-\inf_{B \in \Sigma, B \subseteq E}\nu(B)=\sup_{B \in \Sigma, B \subseteq E}-\nu(B)$$。
> * $$|\nu|(E)=\sup \sum_{i=1}^n |\nu(E_i)|$$，$$\{E_i\}_{i=1}^n \subseteq X$$為互斥的可測集合。

<details>

<summary>proof: <span class="math"> E \cap P \subseteq E, ~ E \cap N \subseteq E</span>。</summary>

令$$X=P \cup N$$為測度$$\nu$$的Hahn分解。

給定$$E \in \Sigma, ~ B \subseteq E, ~ B \in \Sigma$$，可得$$\displaystyle  \begin{aligned} \nu(B) & =\nu^{+}(B) - \nu^{-}(B) \\  & \leq \nu^{+}(B) ~ [\because \nu^{+}, ~\nu^{-} \text{ both positive measures  }] \\  & \leq \nu^{+}(E)~ [\because B \subseteq E, ~\text{ monotonicity} ] \\     & = \nu(E \cap P)     \end{aligned}$$因為$$E \cap P \subseteq E$$，因此$$\sup \nu(B)=\nu^{+}(E)$$。

同理得：

$$\displaystyle  \begin{aligned} \nu(B) & =\nu^{+}(B) - \nu^{-}(B) \\  & \geq -\nu^{-}(B) ~ [\because \nu^{+}, ~\nu^{-} \text{ both positive measures  }] \\  & \geq -\nu^{+}(E)~ [\because B \subseteq E, ~\text{ monotonicity} ] \\     & = -\nu(E \cap N)     \end{aligned}$$因為$$E \cap N \subseteq E$$，因此$$\sup -\nu(B)=\nu^{-}(E)$$

(QED)

</details>

### 符號測度的Jordan分解的最小性質(minimal property)

> 在可測空間$$(X, \Sigma)$$中，$$\nu$$為符號測度，$$\lambda, \mu: \Sigma \rightarrow [0, \infty)$$為有限正測度且滿足$$\nu=\lambda - \mu$$。
>
> 若$$\nu=\nu^{+}-\nu^{-}$$為Jordan分解，則$$\lambda \geq \nu^{+}$$且$$\mu \geq \nu^{-}$$。
>
> 註：$$X=P \cup N$$為測度$$\nu$$的Hahn分解。$$\nu^{+}(S)=\nu(S \cap P), ~\nu^{-}(S)=-\nu(S \cap N)$$。

<details>

<summary>proof: 反證法</summary>

令$$E \in \Sigma$$且$$\lambda(E) < \nu^{+}(E)$$--(1)。

因為$$E=(E \cap P) \cup (E \cap N)$$為分割，由(1)可得不等式：$$\lambda(E \cap P) + \lambda(E \cap N) < \nu^{+}( E \cap P) + \nu^{+}( E \cap N)$$

由Jordan分解得$$\nu^{+}(E \cap N)=0$$且$$\lambda (E \cap N) \geq 0$$，因此$$\lambda (E \cap P) < \nu^{+}(E \cap P)$$--(2)

因為$$\lambda (E \cap P) - \mu(E \cap P) = \nu^{+}(E \cap P) - \nu^{-}( E \cap P)$$--(3)

由(2,3)得$$\mu^(E \cap P ) < \nu^{-}(E \cap P)=0$$，但$$\mu$$為正測度不可為負值，因此假設(1)矛盾&#x20;

(QED)

</details>

### 有限符號測度的三角不等式

> 在可測空間$$(X, \Sigma)$$中，$$\nu_1, \nu_2: \Sigma \rightarrow \mathbb{R}$$為有限符號測度，則：
>
> * $$|\nu_1 + \nu_2| \leq |\nu_1| + |\nu_2|$$。
> * $$a,b \in \mathbb{R}, ~a \nu_1 + b \nu_2$$為有限符號測度。
> * $$|a \nu|=|a||\nu|$$。

<details>

<summary>proof: 三角不等式由Hahn分解證明</summary>

$$|\nu_1+\nu_2| = (\nu_1+\nu_2)^{+} + (\nu_1+\nu_2)^{-}$$

$$X=P \cup N$$為測度$$\nu$$的Hahn分解。$$\nu^{+}(S)=\nu(S \cap P), ~\nu^{-}(S)=-\nu(S \cap N)$$。

$$\forall E \in \Sigma$$,&#x20;

$$\displaystyle  \begin{aligned} (\nu_1 + \nu_2)^{+}(E) &= (\nu_1 + \nu_2)(E \cap P) \\ 	&= (\nu_1^{+}+ \nu_2^{+} - \nu_1^{-} - \nu_2^{-})(E \cap P) \\ 	& \leq (\nu_1^{+}+ \nu_2^{+})(E \cap P) ~[\because \nu_1^{-},\nu_2^{-} \geq 0] \\ 	& \leq \nu_1^{+}(E) + \nu_2^{+}(E)~ [\because E \cap P \subseteq E] \end{aligned}$$

同理可得

$$\displaystyle  \begin{aligned} (\nu_1 + \nu_2)^{-}(E) &= -(\nu_1 + \nu_2)(E \cap N) \\ 	& \leq \nu_1^{-}(E) + \nu_2^{-}(E)~  \end{aligned}$$

因此$$\displaystyle  \begin{aligned} |\nu_1 + \nu_2|(E) &= (\nu_1 + \nu_2)^{+}(E) + (\nu_1 + \nu_2)^{-}(E) \\ 	& \leq \nu_1^{+}(E) + \nu_1^{-}(E) + \nu_2^{+}(E) + \nu_2^{-}(E) \\ 	& = |\nu_1(E)| + |\nu_2(E)| \end{aligned}$$

(QED)

</details>



### 零測度集合若且唯若全變差測度為0

> 在可測空間$$(X, \Sigma)$$中，$$\nu$$為符號測度。
>
> $$E \in \Sigma, \nu(E)=0, ~ \forall F \subseteq E, ~ F \in \Sigma, ~ \nu(F) = 0 \iff |\nu|(E)=0$$。

<details>

<summary>proof: 零測集同時為正/負測集</summary>

\=>(反證法)

全變差測度$$|\nu|: \Sigma \rightarrow \infty [0, \infty]$$，$$|\nu|=\nu^{+} + \nu^{-}$$。

如果$$|\nu|(E)=\infty$$，則$$\nu^{+} (E)=\infty$$或$$\nu^{-}(E)=\infty$$。因此$$\nu(E) \neq 0$$。

令$$0<|\nu|(E) <\infty$$。

因為$$|\nu|(E)=\nu^{+}(E) + \nu^{-}(E) > 0$$且$$\nu^{+}(E) \geq 0,~\nu^{-}(E) \geq 0$$

因此$$\nu^{+}(E),~\nu^{-}(E)$$不會同時為0。

* 如果$$\nu^{+}(E),~\nu^{-}(E)$$有一者為0 ，可得$$\nu(E) = \nu^{+}(E) - \nu^{-}(E) \neq 0$$.&#x20;
* 如果$$\nu^{+}(E),~\nu^{-}(E)$$均不為0，且兩者不相等時，可得$$\nu(E) = \nu^{+}(E) - \nu^{-}(E) \neq 0$$。
* 如果$$\nu^{+}(E),~\nu^{-}(E)$$均不為0，且兩者相等時，由\[有限非負測度集合包含正測集]得$$E$$不是零測集。

因此$$E$$不是零測集(QED)

<=

因為$$|\nu|(E)=\nu^{+}(E) + \nu^{-}(E) = 0$$，且$$\nu^{+}, \nu^{-}$$均為正測度，因此得$$\nu^{+}(E) =  \nu^{-}(E)=0$$。--(1)

同理對$$E$$的任意可測子集$$F \subseteq E$$，因為$$|\nu|$$為正測度且由有號測度的單調性得$$0\leq |\nu|(F) \leq |\nu|(E)=0$$。--(2)

由(1,2)得$$E$$為零測集(QED)

</details>

<details>

<summary>proof2</summary>

\=>

若$$E$$為零測集，則$$|\nu|(E)=\nu^{+}(E)+\nu^{-}(E)=\nu(E \cap P) - \nu(E \cap N)=0 - 0 = 0$$

(QED)

<=

若$$|\nu|(E)=0$$，則$$\nu^{+}(E)+\nu^{-}(E)=0$$且$$\nu^{+}(E) \geq 0, \nu^{-}(E) \geq 0$$。

因此$$\nu^{+}(E)=0, \nu^{-}(E)=0$$。

且對於任何可測子集$$F \subseteq E$$，均可得$$\nu(F)=\nu^{+}(F)-\nu^{-}(F)=0$$ (QED)

</details>

### 相互奇異測度與全變差、正/負變差均相互奇異

> 在可測空間$$(X, \Sigma)$$中，令$$\mu,\nu$$為符號測度。
>
> $$\nu \perp \mu \iff |\nu| \perp \mu \iff \nu^{+} \perp \mu \iff \nu^{-} \perp \mu$$。
>
> $$\nu=\nu^{+} - \nu^{-}, ~|\nu|=\nu^{+} + \nu^{-}$$

<details>

<summary>proof</summary>

因為$$\nu \perp \mu$$，由定義得$$\exists E,F \in \Sigma$$，$$E \cap F=\emptyset$$，$$E \cup F = X$$ 且$$\mu(E)=0, \nu(F)=0$$且$$\forall E_s \in \Sigma, E_s \subseteq E,~ \mu(E_s) =0$$，$$\forall F_s \in \Sigma, F_s \subseteq F,~ \nu(F_s) =0$$。。

因為$$F$$為$$\nu$$的零測集，由\[零測度集合若且唯若全變差測度為0]得$$|\nu|(F)=0$$因此可得$$|\nu| \perp \mu$$ (QED)。

因為$$\nu(F)=\nu^{+}(F)-\nu^{-}(F)=0$$且$$|\nu|(F)=\nu^{+}(F)+\nu^{-}(F)=0$$，求解後可得$$\nu^{+}(F)=\nu^{-}(F)=0$$且對其任意可測子集均成立，因此$$\nu^{+} \perp \mu$$且$$\nu^{-} \perp \mu$$。 (QED)

</details>

## 參考資料

* [https://zhuanlan.zhihu.com/p/274555361](https://zhuanlan.zhihu.com/p/274555361)
* [https://www.ams.org/proc/1980-080-02/S0002-9939-1980-0577778-7/S0002-9939-1980-0577778-7.pdf](https://www.ams.org/proc/1980-080-02/S0002-9939-1980-0577778-7/S0002-9939-1980-0577778-7.pdf)
* [https://zhuanlan.zhihu.com/p/159129138](https://zhuanlan.zhihu.com/p/159129138)
* [https://zhuanlan.zhihu.com/p/68660066](https://zhuanlan.zhihu.com/p/68660066)
