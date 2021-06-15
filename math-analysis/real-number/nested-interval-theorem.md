# 區間套定理\(nested interval theorem\)

## Cantor intersection theorem

> 令$$\{Q_1,Q_2,\ldots\}$$為$$\mathbb{R}^n$$ 上可數的非空集合序列，且
>
> * $$Q_{k+1} \subseteq Q_k, ~ k=1,2,\ldots$$ 為遞減集合，
> * $$Q_1$$ 為有界集合且$$Q_k$$ 為閉集合, $$∀k$$
>
> 則$$\displaystyle\bigcap_{k=1}^\infty Q_k$$  為非空閉集合。
>
> 註: 實數版本即為區間套定理\(nested interval theorem\)。

proof：

* 令$$S=\cap_{k=1}^\infty Q_k$$, [可數個閉集合的交集仍為閉集合](../metric-space/closed-set.md#ke-shu-wu-xian-ge-bi-ji-he-de-jiao-ji-reng-wei-bi-ji-he)的性質得$$S$$為閉集合。
* 要檢驗$$ S \neq \emptyset$$ 即$$\exists x \in S$$。
* 若$$Q_k$$ 集合中為有限多個點時，可簡單證明必定存在$$x \in S$$。
* 假設$$Q_k$$ 集合中有無限多個點，建造集合$$A=\{x_1,x_2, \ldots\}, ~ x_k \in Q_k$$。
* 因為$$A$$有無窮多個元素且$$A \subseteq Q_1$$ 為有界集合，由Bolzano-Weierstrass定理得集合$$A$$有極限點$$x$$。
* 由[極限點的鄰域與集合交集的元素為無窮多個](../metric-space/point-topology.md#ji-xian-dian-de-lin-yu-yu-ji-he-jiao-ji-de-yuan-su-wei-wu-qiong-duo-ge)的性質得$$\forall r>0 N_r (x)$$與$$A$$交集的元素個數為無窮多個。
* 因此$$\cap_{k=1}^\infty Q_k \neq \emptyset$$ \(QED\).





>







