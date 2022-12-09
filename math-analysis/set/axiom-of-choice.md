---
description: Axiom of Choice
---

# 選擇公理

## 簡介

分析中基礎的大部分可不使用選擇公式建立，但在進階部份使用選擇公理非常方便，且可推論出許多不直觀的結果如Banach-Tarski悖論等。

\[陶哲軒]此公理被數學家廣為接受，其中一個理論是Kurt Godal證明了一個使用選擇公理的結果，絕對不會與不使用選擇公理證明的結果互相矛盾。可將選擇公理看成分析學的一個方便、安全的工具。

## 無限Cartesian乘積

> 給定指標集合$$I$$(可為無限集)，且對於$$\forall  i \in I$$，$$X_i$$為集合。
>
> 定義Cartesian乘積$$\displaystyle \prod_{i \in I}X_i$$為集合如下：
>
> $$\displaystyle \prod_{i \in I}X_i \equiv  \left \{ (x_i)_{i \in I} \in (\bigcup_{j \in I} X_j)^I ~|~ \forall i \in I, ~x_i \in X_i  \right\}$$

## 選擇公理

> 令$$I$$為指標集合，且對於$$\forall i \in I$$，$$X_i$$為非空集合，則$$\displaystyle \prod_{i \in I}X_i$$也為非空集合。
>
> 即存在一函數$$(x_i)_{i \in I}$$將$$i \in I$$對應給元素$$x_i \in X_i$$

給定一個非空的集合$$X_i$$的集合族$$\{X_i~|~i\in I \}$$，一定可以從每個集合$$X_i$$選出單個元素$$x_i$$，然後將所有的選擇建構成無限的組$$(x_i)_{i \in I}$$。

在使用選擇公理時，沒有明確的法則(非構造性)說明如何進行選擇，只是保證一定選的到元素。

<mark style="color:red;">通常使用選擇公理時，不必使用全部的功能，常用</mark><mark style="color:red;">**可數選擇公理**</mark>。

### 實數非空有上界集合存在數列收斂至上確界

> $$\emptyset \neq E \subseteq \mathbb{R}$$且滿足$$\sup(E) < \infty$$有上確界，則存在數列$$\{a_n\}_{n =1}^{\infty} \subseteq E$$且$$\displaystyle \lim_{n \rightarrow \infty} a_n = \sup(E)$$

proof:

令集合$$\displaystyle X_n =\left\{  x \in E ~| ~ \sup(E) - \frac{1}{n} \leq x \leq \sup(E)  \right\}$$

由於$$\sup(E)$$為上確界(不一定為$$E$$的元素)，所以$$\sup(E) - \frac{1}{n}$$必定不為上確界，則對於$$\forall n \in \mathbb{N}$$，$$X_n \not = \emptyset$$。

因此可使用選擇公理取$$a_n \in X_n, \forall n \in \mathbb{N}$$得到$$\{a_n\}_{n=1}^\infty \subseteq E$$且$$\sup(E)-\frac{1}{n} \leq a_n \leq \sup(E)$$

根據夾擠定理可得$$\displaystyle  \lim_{n \rightarrow \infty } a_n = \sup(E)$$ (QED)
