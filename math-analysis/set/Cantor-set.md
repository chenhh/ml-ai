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
> Cantor set定義為在$$[0,1]$$當中，在此遞迴刪除過程中沒有被刪除的所有點之集合。即 $$\mathcal {C} \equiv \cap _{n=1}^{\infty }C_{n}$$

![建構Cantor集前六步保留的集合](../../.gitbook/assets/cantor\_set.png)

### Cantor集的性質

* Cantor集合為不可測集。
* Cantor集合的測度為0 (uncountable set)。
* Cantor集合是緊緻集(compact set)。
* Cantor集合是完全集(perfect set)。
* Cantor集合是疏落集。
* Cantor集合是完全不連通集。c
* Cantor集合與正整數冪集合 $$\mathrm{P}(\mathbb{N})$$等價。
* Cantor集合與實數集$$\mathbb{R}$$等價。

## 參考資料

* [Wikipedia: Cantor set](https://en.wikipedia.org/wiki/Cantor\_set)
* [\[知乎\] 搞懂Cantor（康托）集](https://zhuanlan.zhihu.com/p/54711962)
