# 集合序列的極限

## 簡介

* 集合$$A, B$$的最小上界可視為$$A \cup B$$（因為$$A,B \subseteq A \cup B$$且任何同時包含$$A,B$$的集合均比$$A\cup B$$大），而最大下界可視為$$A\cap B$$。
* 函數數列上下極限的定義，其關鍵之處在於尋找到函數數列上下確界的類似物，這與找出集合論中與大小關係類似的運算，即集合的包含關係。
* 按照集合的包含關係，所謂集合數列的「最小上界\(sup\)」是包含所有$$A_n$$的集合中最小的那個集合，顯而易見，這個集合就是所有$$A_n$$的聯集$$\bigcup_n A_n$$。	 類似的概念可找出找出集合數列的「最大下界\(inf\)」，為所有$$A_n$$ 的交集$$\bigcap_n A_n$$。

##  單調\(monotone\)集合數列

> * $$\{E_n \}_{n \in \mathbb{N}}$$ 為單調遞增\(monotone increasing\)若 $$E_n \subseteq E_{n+1}, ~ \forall n \in \mathbb{N} $$。
> * $$\{E_n\}_{n \in \mathbb{N}}$$ 為單調遞減\(monotone decreasing\)若$$ E_n \supseteq E_{n+1}, ~ \forall n \in \mathbb{N}$$。

## 集合數列的上極限\(superior limit of  sequence of set\)

> $$\{E_n\}_{n \in \mathbb{N}}$$ 為集合數列，則$$\displaystyle \limsup_{n \rightarrow \infty}⁡ E_n  =\{x \in X |\forall n \in \mathbb{N} ~\exists k>n∋x∈E_k \}$$，$$x$$存在於無窮多個$$E_n$$。

$$\displaystyle \limsup_{n \rightarrow \infty}⁡ E_n  =\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k =(E_1 \cup E_2\cup \ldots) \cap (E_2 \cup E_3 \cup \ldots )\cap \ldots$$

* 令$$\forall n \in \mathbb{N}, ~M_n = E_n \cup E_{n+1} \cup \ldots $$為從第$$n$$個集合元素的聯集（上界）。
  * $$M_1 = (E_1 \cup E_2 \cup E_3 \cup \ldots)$$
  * $$M_2 = (E_2 \cup E_3 \cup \ldots)$$
  * 可得 $$M_1 \supseteq M_2 \supseteq\ldots$$為遞減集合數列。
  * 可得$$\displaystyle \limsup_{n \rightarrow \infty}⁡ E_n  =\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k  = \bigcap_{n=1}^\infty M_n$$，為遞減集合數列的交集。
  * 若$$x\in \bigcap_{n=1}^\infty M_n$$，依交集的性質可得$$x$$存在於全部的$$M_n$$ 中，但因為$$\{M_n\}$$ 為遞減集合數列，因此較前面的$$M_1,M_2, \ldots$$可能不包含$$x$$，因此$$x$$不必存在於全部的集合中，只需存在於可數個集合中即可。
* 與數列的上極限一樣，集合數列的上極限也是從第$$n$$個元素開始的最小上界形成集合的最大下界。







