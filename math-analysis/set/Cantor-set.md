# Cantor集

## 簡介

Cantor 集合為測度論中，<mark style="color:red;">在實數上為不可數(uncountable)且測度為0集合(因為收斂到單點形成的集合)的範例(註：實數上一般常見的不可數集為區間，測度不為0)</mark>。

Cantor集具有許多奇特的性質，實分析中的很多反例就是用Cantor集構造的。

* 實數上所有可數(countable)集合的(Lebesgue)測度均為0，即單點的測度(長度)為0。
* Borel集合為實數上所有開(閉)區間(interval)形成的最小sigma-algebra，而所有的長度非0的區間都是不可數集合。
* Cantor集合中存在子集合為可測集合，但不是Borel集合。

Cantor集合可得知以下兩問題答案均為否。

* 若集合的測度為0，則此集合是否為可數集合? 否。
* 若集合為可測(measurable)，則此集合是否為Borel measurable? 否。

### Cantor集合

<mark style="color:red;">Cantor集是由不斷去掉線段中間的三分之一開區間而得出。一般使用閉區間</mark>$$[0,1]$$<mark style="color:red;">建構得出</mark>。<mark style="color:red;">Cantor集就是由所有遞迴刪除過程中沒有被去掉的區間 \[0,1] 中的點組成，需要注意的是，每次去掉的都是開區間</mark>。

> 給定實數閉區間$$C_0=[0,1]$$，將此區間分三等份，每次刪除閉區間中的中間的開區間，遞迴(無限次)刪除下去。
>
> 第一層：中間的開區間記為$$I_1^1=(\frac{1}{3}, \frac{2}{3})$$，兩側的閉區間記為$$F_1=F_1^1 \cup F_1^2=[0,\frac{1}{3}] \cup [\frac{2}{3}, 1]$$。
>
>
>
> * 其中$$I_{n}^{i}$$為第$$n$$層第$$i$$個開區間；同理$$F_n^i$$為第$$n$$層第$$i$$個閉區間。
> * 第$$n$$層(步)會有$$2^{n-1}$$個開區間，每個開區間長度為$$\frac{1}{3^n}$$。
>
> 第二層：$$F_1$$的兩個閉區間以同樣方式分割後得到的開區間為$$I_2^1 \cup I_2^2 = (\frac{1}{9}, \frac{2}{9}) \cup (\frac{7}{9}, \frac{8}{9})$$，剩下的閉區間為$$F_2 = [0, \frac{1}{9}] \cup [\frac{2}{9}, \frac{3}{9}] \cup [\frac{4}{9}, \frac{7}{9}] \cup [\frac{8}{9}, 1]$$。
>
> 可得$$F_2=F_2^1 \cup F_2^2 \cup F_2^3 \cup F_2^4 =\frac{F_1}{3}\cup (\frac{2}{3}+\frac{F_1}{3})$$, $$I_2 = \frac{I_1}{3}\cup (\frac{2}{3} +\frac{I_1}{3})$$
>
> 遞迴關係式為
>
> * $$F_n =\frac{F_{n-1}}{3} \cup (\frac{2}{3}+\frac{F_{n-1}}{3}), \forall n \in \mathbb{N}, \ F_0 = [0,1]$$
> * $$I_n = \frac{I_{n-1}}{3}\cup(\frac{2}{3} + \frac{I_{n-1}}{3})$$
>
> Cantor set定義為在$$[0,1]$$當中，在此遞迴刪除過程中沒有被刪除的所有點之集合。即 $$\mathcal {C} \equiv \cap _{n=1}^{\infty }F_{n}$$
>
> $$\displaystyle C=[0,1]-\bigcup_{n=1}^\infty \bigcup_{k=0}^{3^{n-1}-1} \left(  \frac{3k+1}{3^n}, \frac{3k+2}{3^n}  \right)$$

![建構Cantor集前六步保留的集合](../../.gitbook/assets/cantor\_set.png)

因為$$F_n, ~n \in \mathbb{N}$$均為非空有界閉集，且$$F_{n+1} \subset F_n$$，根據區間套定理可得$$C$$不是空集合，且每個閉區間的端點都沒有被移去，所以$$C$$為閉集合。

###

### Cantor集的性質

* Cantor集合為不可數集。
* Cantor集合的Lebesgue測度為0。
* Cantor集合是緊緻集(compact set)。
* Cantor集合是完全集(perfect set)。
* Cantor集合是疏落集。
* Cantor集合是完全不連通集。
* Cantor集合與正整數冪集合 $$\mathrm{P}(\mathbb{N})$$等價。
* Cantor集合與實數集$$\mathbb{R}$$等價。

## Cantor集是不可數集

<mark style="color:red;">註：Cantor集可寫成3進位小數中，完全不含位元1的任意實數點集</mark>。

這裡需要用到實數的三進位表示，在三進位系統中，數字僅僅允許為0，1，2。

> 令$$x=0.a_1a_2\dots a_n\dots \in [0,1], a_j \in \{0,1,2\}$$為區間$$[0,1]$$中以三進位表示的實數。
>
> 則$$x \in C \Leftrightarrow a_j \{0,2\}, \forall n \in \mathbb{N}$$

構造Cantor集時，

* 第一步去掉的開區間用三進位表示為$$I_1^1=(\frac{1}{3}, \frac{2}{3})_{10}=(0.1, 0.2)_3$$
* 第二步去掉的開區間用三進位表示為：$$I_2^1 \cup I_2^2 = (\frac{1}{9}, \frac{2}{9})_{10} \cup (\frac{7}{9}, \frac{8}{9})_{10} = (0.01, 0.02)_3 \cup (0.21, 0.22)_3$$
* 第$$n$$步去掉的第$$k$$個開區間為$$I_n^k, ~k=1,2,\dots, 2^{n-1}$$用三進位表示為$$(0.a_1a_2\dots a_{n-1}1, 0.a_1a_2\dots a_{n-1}2)_3$$

而位於區開間$$I_n^k$$中的元素必可表示為以下三進位：$$(0.a_1a_2\dots a_{n-1} 1 a_{n+1}a_{n+2}\dots)_3$$

可發現去除的規律為在第$$n$$步時，去掉的區間中前$$n-1$$位元$$a_1, a_2, \dots , a_{n-1}$$只能是0或2，第$$n$$位的$$a_n$$必為1，第$$n$$位後的位元$$a_{n+1}, a_{n+2},\dots$$可為0,1,2任一值。

因此把$$[0,1]-C$$補集中的任意值以三進位表示後，至少有一位元之值為1。

所以Cantor集可寫成3進位小數中，完全不含位元1的實數點集：$$\displaystyle C=\left\{   x\in [0,1]~|~ x=(0.a_1a_2\dots a_n\dots)=\sum_{k=1}^\infty a_k3^{-k}, ~ a_k \in \{0,2 \} \right\}$$

令函數$$f$$將$$x=(0.a_1a_2\dots a_n\dots), ~ a_k \in \{0,2 \}$$中所有的2替換成1的函數，即$$\displaystyle f(\sum_{k=1}^\infty a_k3^{-k}) =  \sum_{k=1}^\infty \frac{a_k}{2} 2^{-k}$$。

則轉換後的$$f(x) \in [0,1]$$為二進位實數。

因此$$\forall y \in [0,1], ~\exists x \in C \ni f(x)=y$$，即$$f: C \rightarrow [0,1]$$為onto函數，所以基數$$|[0,1]| \leq |C|$$。

由於$$|[0,1]|=|\mathbb{R}|=\aleph_1$$，因此$$C$$為不可數集。

## Cantor集的Lebesque測度為0

在閉區間$$[0,1]$$建構Cantor集時，在第$$n$$步總共會去掉$$2^{n-1}$$個開區間，且每個開區間的長度均為$$\frac{1}{3^n}$$。

因此去掉的總區間長度為$$\displaystyle \sum_{n=1}^\infty 2^{n-1}\frac{1}{3^n}  = \frac{1}{3} \sum_{n=0}^\infty \left(\frac{2}{3}\right)^n  = \frac{1}{3} \left( \frac{1}{1-2/3} \right) = 1$$

所以Cantor集$$C$$的長度為$$|[0,1]|-1=0$$&#x20;

## 參考資料

* [Wikipedia: Cantor set](https://en.wikipedia.org/wiki/Cantor\_set)
* [\[知乎\] 搞懂Cantor（康托）集](https://zhuanlan.zhihu.com/p/54711962)
