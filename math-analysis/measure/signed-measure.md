---
description: signed measure
---

# 符號測度

一般討論測度$$u: \Sigma \rightarrow [0, \infty]$$要求其值域為非負值，而符號測度討論的是值域可為負值的情形。

<mark style="color:red;">Hahn分解可得符號測度的本質表示：有號測度是兩正測度的差</mark>。

## 符號測度

> 給定可測空間$$(X, \Sigma)$$，定義函數$$\nu: \Sigma \rightarrow [-\infty, \infty]$$可取值$$\pm\infty$$且滿足：
>
> 1. 定義域$$\Sigma$$為σ域
> 2. $$\nu(\empty)=0$$
> 3. $$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty \nu(E_n)$$，$$E_i \cap E_j = \empty$$且$$\bigcup_{n=1}^\infty E_n \in \Sigma$$。此處要求當$$\displaystyle \nu(\bigcup_{n=1}^\infty E_n) < \infty$$時，$$\displaystyle \sum_{n=1}^\infty \nu(E_n)$$ 為絕對收斂。
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
> 若$$\{E_n\}$$為$$\Sigma$$上的遞減集合且$$\nu(E_1)<\infty$$，則$$\displaystyle \nu(\bigcap_{n=1}^\infty E_n)=\lim_{n \rightarrow \infty} \nu(E_n)$$。
>
> 註：此性質和[正測度的連續性](../measure.md#di-zeng-ji-he-ji-xian-de-ce-du-ce-du-de-lian-xu-xing-continuity-of-measure)相同。



## 正集合與負集合(positive set and negative set)

> 令$$\nu$$為符號測度，則
>
> * 稱$$A$$在測度$$\mu$$下為<mark style="color:red;">正集合(positive set)</mark>，若$$E \subseteq A$$為可測集合且$$\nu(E) \geq 0$$。
> * 稱$$B$$在測度$$\mu$$下為<mark style="color:red;">負集合(negative set)</mark>，若$$E \subseteq B$$為可測集合且$$\nu(E) \leq 0$$。
> * 稱$$C$$在測度$$\mu$$下<mark style="color:red;">零測集(null set)</mark>，若$$E \subseteq C$$為可測集合且$$\nu(E)=0$$。
>
> [https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets](https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets)

以$$\nu(E)=\int_E f d\mu$$為例，正集合即$$f \geq 0 \text{ a.e. on }  E$$，負集合則$$f \leq 0 \text{ a.e. on } E$$，零測集則$$f = 0 \text{ a.e. on } E$$。

### 正集合的子集仍為正集合且正集合的可數連集仍為正集合

> 令$$\nu$$為$$(X, \Sigma)$$上的符號測度。
>
> 若$$E$$為可測集且$$\nu(E) \geq 0$$，則$$\forall F \subseteq E$$，$$\nu(F) \geq 0$$。
>
> 若$$\{E_n\}$$為可測集且$$\nu(E_n) \geq 0, \forall n$$，則$$\displaystyle \forall S \in \bigcup_{n=1}^\infty E_n,~  \nu(S) \geq 0$$。

<details>

<summary>proof: 將集合拆解為互斥集合</summary>

1. 因為$$F \subseteq E$$，且$$\nu(E) \geq 0$$，由正集合定義得$$\nu(F) \geq 0$$。(QED)
2. 令$$F_n = E_n - \bigcup_{n=1}^{n-1} E_n$$，可得$$F_n \subseteq E_n$$，由正集合定義得$$\nu(F_n)\geq 0$$。

因此若$$S \subseteq \bigcup_{n=1}^\infty E_n$$，則$$\nu(S)=\sum_{n=1}^\infty \nu(S \cap Q_n) \geq 0$$ (QED)

</details>

## Hahn分解定理(The Hahn decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，令$$\nu$$為符號測度，則存在正集合$$A$$與負集合$$B$$(均在測度$$\nu$$下)滿足：
>
> $$X = A \cup B$$且$$A\cap B = \emptyset$$。
>
> 若$$E, F$$為另一組滿足上述條件的集合，則$$A \cap E=B \cap F$$在測度$$\nu$$下為零測集。
>
> <mark style="color:red;">註：Hahn分解可得符號測度是兩正測度的差</mark>。
>
> Hahn分解不唯一(因為有零測集存在)。
>
> [https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem](https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem)
>
> [https://zhuanlan.zhihu.com/p/36652587](https://zhuanlan.zhihu.com/p/36652587)

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

[https://zhuanlan.zhihu.com/p/274555361](https://zhuanlan.zhihu.com/p/274555361)
