# 覆蓋\(covering\)

## 簡介

* Lindelof 覆蓋定理證明了$$\mathbb{R}^n$$ 中集合$$S$$的任意（\(可數或不可數）開覆蓋，必定存在可數的子開覆蓋。
* Heine-Borel 覆蓋定理證明了$$\mathbb{R}^n$$ 中**有界閉集合必定存在有限個的覆蓋**。
* Bolzano-Weierstrass定理，Cantor交集定理，Lindelof，Heine-Borel均使用了$$\mathbb{R}^n$$上的性質，因此在一般化的度量空間$$(M,d)$$不一定會成立。

## 覆蓋\(covering\)

> * 集合族\(a collection of set\) $$F$$稱為集合$$S$$的覆蓋若 $$S\subseteq \bigcup_{A \in F} A$$。  即$$\forall x \in S, ~ \exists A \in F \ni x \in A$$。  也稱集合族$$F$$覆蓋集合$$S$$。
> * 若$$F$$是開集合的集合族，則稱$$F$$開覆蓋集合$$S$$ \($$F$$ is an open covering of set$$S$$\)。

#### 範例

*  \[可數覆蓋\(countable covering\)\] 所有以下形式的區間 $$\frac{1}{n}<x<\frac{2}{n}, ~ n=2,3,4, \ldots$$可覆蓋開區間$$(0,1)$$。即$$(0,1) \subseteq \bigcup_{n=2}^\infty (\frac{1}{n}, \frac{2}{n})$$。
* \[不可數覆蓋 \(uncountable covering\)\] 實數$$\mathbb{R}$$ 可被所有的開區間$$(a,b)$$覆蓋。  但實數存在可數覆蓋 $$(n,n+2), ~\forall n \in \mathbb{N}$$。

## 開集合S中的任一點為有理數球A集合內的點且A為S的子集

> 給定可數集合族$$G=\{A_1,A_2, \ldots\}$$，$$A_k$$ 為有理數$$x_k \in \mathbb{Q}^n$$ 為中心，且半徑$$r_k \in \mathbb{Q}^{+}$$ 也為正有理數形成的球$$N_{r_k} (x_k)$$。因為有理數集合$$\mathbb{Q}^n$$為可數集合，所以$$G$$為可數集合。
>
> 假設點$$x \in S\ \subseteq \mathbb{R}^n$$，$$S$$為開集合，則集合族$$G$$中存在至少一個有理數球為$$S$$的子集合，即$$ x \in A_k \subseteq S。$$

Proof:

* 因為$$A_k$$ 是由有理數中心與正有理數半徑所構成的鄰域，因此$$G$$為可數集合族。
* 因為$$S$$為開集合且$$x∈S$$，由開集合的定義得$$\exists r>0 \ni N_r (x) \subseteq S$$。
* 檢驗：存在有理數點$$y∈S$$，且存在有理數半徑$$q \in \mathbb{Q}^{+} \ni x \in N_q (y) \subseteq S$$。
* 因為$$N_r (x) \subseteq S$$，由[實數的稠密性](./#shi-shu-ji-de-chou-mi-xing)得在$$x$$為中心，半徑為$$r$$的圓內必定存在有理數點$$y$$。
* 令$$x=(x_1,x_2, \ldots ,x_n )$$取$$y_k \in \mathbb{Q} \ni |y_k−x_k |<\frac{r}{4n}, ~ k=1,2,\ldots,n$$
* $$x,y$$兩點的距離由三角不等式可得 $$\|y−x\| \leq |y_1−x_1 |+\cdots+|y_n−x_n |<\frac{r}{4}$$
* 取$$q \in \mathbb{Q}^{+} \ni \frac{r}{4}<q<\frac{r}{2}$$
* 則$$x \in N_q (y)$$ 且 $$N_q (y) \subseteq N_r (x) \subseteq S$$
* 因為$$N_q (y) \in G$$， 得證 \(QED\)





