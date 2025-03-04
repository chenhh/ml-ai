---
description: Axiom of Choice
---

# 選擇公理

## 簡介

#### 選擇公理簡述

> 設$$X$$是非空集合的集合族。則我們可以從$$X$$中的每個集合(元素)中選出一個元素。

<mark style="color:blue;">簡單的說，如果你手上有一堆集合，而且可確定每一個集合都包含至少一個元素，那麼一定可以在每一個集合抽一個元素出來(不必考慮選擇的方法)，而不用知道每個集合的其他資訊</mark>。

數學上不存在一個明顯的函數$$f(X)$$，可以在任何一個非空集合$$X$$中準確地抽出一個元素。

\[陶哲軒]此公理被數學家廣為接受，其中一個理論是Kurt Godal證明了一個使用選擇公理的結果，絕對不會與不使用選擇公理證明的結果互相矛盾。可將選擇公理看成分析學的一個方便、安全的工具。

雖然選擇公理很直覺，但可使用選擇公理推出一些很特殊的結果，幾個例子包括：

1. [Banach–Tarski悖論](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox)：存在一個方法，可以將一個三維實心球分成有限個部分，然後通過旋轉和平移，重新組合為兩個半徑和原來相同的完整的球；
2. [Tarski分割圓問題](https://en.wikipedia.org/wiki/Tarski's_circle-squaring_problem)：存在一個方法，可以將平面上的一個圓分割成有限多塊，然後通過平移，重新拼合成面積相同的正方形；
3. 在以下情況中，存在一個策略令只有有限個犯人不被釋放:無窮個犯人面向數軸的正方向依次就座，第$$i$$個犯人坐在數軸上座標為$$i$$的地方，他可以看見所有座標大於$$i$$的囚犯頭頂上的帽子。每個囚犯都戴上了黑色或白色的帽子，然後每個犯人依次猜測自己頭上的帽子顏色，猜對了的予以釋放。犯人們可以事先商量，而且他們都知道自己的座位編號，但犯人們不能聽到其他人的猜測；同時，我們假設每個犯人都是聰明和有無窮記憶力的。

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

### 應用：實數非空有上界集合存在數列收斂至上確界

> $$\emptyset \neq E \subseteq \mathbb{R}$$且滿足$$\sup(E) < \infty$$有上確界，則存在數列$$\{a_n\}_{n =1}^{\infty} \subseteq E$$且$$\displaystyle \lim_{n \rightarrow \infty} a_n = \sup(E)$$

proof:

令集合$$\displaystyle X_n =\left\{  x \in E ~| ~ \sup(E) - \frac{1}{n} \leq x \leq \sup(E)  \right\}$$

由於$$\sup(E)$$為上確界(不一定為$$E$$的元素)，所以$$\sup(E) - \frac{1}{n}$$必定不為上確界，則對於$$\forall n \in \mathbb{N}$$，$$X_n \not = \emptyset$$。

因此可使用選擇公理取$$a_n \in X_n, \forall n \in \mathbb{N}$$得到$$\{a_n\}_{n=1}^\infty \subseteq E$$且$$\sup(E)-\frac{1}{n} \leq a_n \leq \sup(E)$$

根據夾擠定理可得$$\displaystyle  \lim_{n \rightarrow \infty } a_n = \sup(E)$$ (QED)

### 應用：可數個可數集合的並集仍然是可數集

proof:

令集合$$A_1,\dots, A_n,\dots$$都是可數集如下：

* $$A_1=\{a_{11},a_{12},a_{13}, a_{14},\dots, \}$$
* $$A_2=\{a_{21},a_{22},a_{23}, a_{24},\dots, \}$$
* $$A_3=\{a_{31},a_{32},a_{33}, a_{34},\dots, \}$$

稱元素$$a_{pq}$$中索引值$$p+q=h$$為高度，依高度依序將元素排序，高度相同時以$$q$$較小者排前面，以此方法可將$$\bigcup_{n=1}^\infty A_n$$中的元素排序。若$$A_i$$，$$A_j$$中有相同的元素，而上述方法去掉共同的元素後仍為可數集。

這個證明看上去完全是構造性的，並沒有無窮多次的選擇。但是事實上每個可數集以自然數為下標列出元素的方法不是唯一的。

因此，要構造上面那個無窮方陣，就必須在 的各種列出方法中選出一種，在 的各種列出方法中選出一種， 在 的各種列出方法中選出一種，...，也就是必須做出無窮多種選擇，從而使用了選擇公理。 (QED)

## 應用：構造Lebesgue不可測集(Vitali集合)

令$$x,y \in \mathbb{R}$$均為實數，且滿足$$x − y$$ 是有理數，記為 $$x \sim y$$，這是一個等價關係，因為它滿足：

* \[reflexive] $$\forall x \in [0,1]$$ ，可得 $$x \sim x$$ 。
* \[symmetric} 如果 $$x \sim y$$，則 $$y \sim x$$ 。
* \[transitive ]如果 $$x \sim y$$ 且 $$y \sim z$$，則 $$x \sim z$$。

$$\forall x \in \mathbb{R}$$，均存在等價類：$$[x]=\{y\in \mathbb{R}~|~ x-y \in \mathbb{Q}\}$$，這些等價類集合分割了實數$$\mathbb{R}$$。

<mark style="color:red;">現在使用選擇公理從每個非空類</mark>$$[x]$$<mark style="color:red;">取出一點形成集合</mark>$$S$$<mark style="color:red;">，則</mark>$$S$$<mark style="color:red;">為Lebesgue不可測集合(此種方法建構出的集合也稱Vitali集合)</mark>。

<details>

<summary>proof: 反證法(<a href="https://zh.wikipedia.org/zh-tw/%E7%BB%B4%E5%A1%94%E5%88%A9%E9%9B%86%E5%90%88">from wiki</a>)</summary>

若$$S$$為可測集，可分為$$m(S) > 0$$與$$m(S)=0$$兩種情形討論。

令$$\{r_k \in \mathbb{Q}\}_{k=1}^\infty \subseteq [-1,1]$$為區間內所有的有理數(有理數為可數集)。

定義集合$$S_k\equiv \{s+r_k ~|~ s \in S \}~k=1,2,\dots$$為互斥的集合

而且可得$$[0,1] \subseteq \bigcup_{k} S_k \subseteq [-1,2]$$

從Lebesgue可測集合的定義中，可以證明所有這類的集合都滿足以下兩個性質：

1. 測度具可數可加性，即$$S_k$$為互斥集合時，$$m(\bigcup_{k=1}^\infty S_k)=\sum_{k=1}^\infty m(S_k)$$
2. 測度具平移不變性，即$$\forall x \in \mathbb{R}$$可得$$m(S+x)=m(S)$$

因此可得$$m([0,1]) \leq m(\bigcup_{k}S_k) \leq m([-1,2])$$，即$$1 \leq \sum_{k=1}^\infty m(S_k) \leq 3$$

由於平移不變性，可得$$m(S_k)=m(S)$$

因此可得$$1 \leq \sum_{k=1}^\infty m(S) \leq 3$$

* 如果$$m(S)=0$$，得$$1 \leq 0 \leq 3$$矛盾。
* 如果$$m(S) > 0$$，則$$\sum_{k=1}^\infty m(S)=\infty$$，得$$1 \leq \infty \leq 3$$矛盾。

因此$$S$$為不可測集合(QED)

</details>
