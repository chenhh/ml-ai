---
description: signed measure
---

# 符號測度

一般討論測度$$u: \Sigma \rightarrow [0, \infty]$$要求其值域為非負值，而符號測度討論的是值域可為負值的情形。

<mark style="color:red;">Hahn分解可得符號測度的本質表示：有號測度是兩正測度的差</mark>。

## 符號測度

> 給定可測空間$$(X, \Sigma)$$，定義函數$$\mu: \Sigma \rightarrow [-\infty, \infty]$$可取值$$\pm\infty$$且滿足：
>
> 1. 定義域$$\Sigma$$為σ域
> 2. $$\mu(\empty)=0$$
> 3. $$\displaystyle \mu(\bigcup_{n=1}^\infty E_n) = \sum_{n=1}^\infty \mu(E_n)$$，$$E_i \cap E_j = \empty$$且$$\bigcup_{n=1}^\infty E_n \in \Sigma$$。此處要求當$$\displaystyle \mu(\bigcup_{n=1}^\infty E_n) < \infty$$時，$$\displaystyle \sum_{n=1}^\infty \mu(E_n)$$ 為絕對收斂。
>
> 則稱$$\mu$$為符號測度。

由定義可知<mark style="color:green;">一般測度為有限測度</mark>的特例。

定義符號測度的應用：

1. 兩個(正)測度的差值時，如$$\mu(E)=\mu_1(E) - \mu_2(E), ~ E \in \Sigma$$，<mark style="color:blue;">其中</mark>$$\mu_1, \mu_2$$<mark style="color:blue;">至少一個為有限測度(因為擴充實數中，兩個無窮大相減無定義)</mark>，且定義在同一個σ域$$\Sigma$$。
2. $$(X, \Sigma, \mu)$$為測度空間，$$f$$為測函數且$$f=f^{+} - f^{-}$$，若至少一個函數$$\int f^+<\infty$$或$$\int f^{-} <\infty$$(因為$$f=f^+-f^{-}$$，而擴充實數中，兩個無窮大相減無定義)，則$$\lambda(E) = \int_E f d\mu = \int_E f^{+} d \mu - \int_E f^{-}d\mu$$為在$$(X, \Sigma)$$上的符號測度。

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

> 令$$\mu$$為有號測度，則
>
> * 稱$$A$$在測度$$\mu$$下為正集合，若$$E \subseteq A$$為可測集合且$$\mu(E) \geq 0$$。
> * 稱$$B$$在測度$$\mu$$下為負集合，若$$E \subseteq B$$為可測集合且$$\mu(E) \leq 0$$。
> * 稱$$C$$在測度$$\mu$$下零測集(null set)，若$$E \subseteq C$$為可測集合且$$\mu(E)=0$$。
>
> [https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets](https://en.wikipedia.org/wiki/Positive\_and\_negative\_sets)

## Hahn分解定理(The Hahn decomposition theorem)

> 在可測空間$$(X, \Sigma)$$中，令$$\mu$$為符號測度，則存在正集合$$A$$與負集合$$B$$(均在測度$$\mu$$下)滿足：
>
> $$X = A \cup B$$且$$A\cap B = \emptyset$$。
>
> 註：Hahn分解可得有號測度的本質表示：符號測度是兩正測度的差。
>
> [https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem](https://en.wikipedia.org/wiki/Hahn\_decomposition\_theorem)

## 參考資料

[https://zhuanlan.zhihu.com/p/274555361](https://zhuanlan.zhihu.com/p/274555361)
