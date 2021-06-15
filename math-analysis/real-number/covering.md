# 覆蓋\(covering\)

## 簡介

* Lindelof 覆蓋定理證明了$$\mathbb{R}^n$$ 中**（開或閉）集合的任意開覆蓋，必定存在可數的子開覆蓋**。
* Heine-Borel 覆蓋定理證明了$$\mathbb{R}^n$$ 中**有界閉集合必定存在有限個的開覆蓋**。
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

## Lindelof 覆蓋定理

> 令（開或閉）集合$$A \subseteq \mathbb{R}^n$$， 且集合族$$F$$為$$A$$的開覆蓋，則存在$$F$$的可數子集合族為$$A$$的開覆蓋。
>
> * 註：集合$$A$$若可被集合族$$F$$開覆蓋，則可從$$F$$中取出有理數球（可數）集合族開覆蓋$$A$$。
> * 註：閉覆蓋集合族無此性質，因只要$$A$$中有任一維度之值為正負無窮大時無法覆蓋，所以必須為開覆蓋。
>   * 例如：實數存在可數開覆蓋$$ (n,n+2), ~\forall n \in \mathbb{N}$$

Proof:

* 令可數有理數集合族$$G=\{A_1,A_2,\ldots\}$$，$$A_i$$ 為有理數為中心且半徑為正有理數的球（鄰域）。
* Idea: 由$$G$$中取出集合形成子集合族$$F$$, 且$$A\subseteq \bigcup_{I∈F} I$$。
* 令$$x∈A$$，由條件知存在開集合$$S \in F \ni x \in S$$。
* 由[開集合中的任一點為有理數球集合內的點且有理數球為開集合的子集](covering.md#kai-ji-heszhong-de-ren-yi-dian-wei-you-li-shu-qiuaji-he-nei-de-dian-qieaweisde-zi-ji)得 $$\exists A_k∈G \ni x \in A_k \subseteq S$$
* 由有數數的稠密性可知滿足上述條件的$$A_k$$ 有無窮多個，取$$G$$中具有最小索引值的$$A_k$$, 且令索引值為$$m(x)$$, 因此可得$$x \in A_{m(x)}  \subseteq S$$。
* $$\forall x∈A$$，均可得到對應的$$A_{m(x)}$$，且$$m(x)$$的個數為可數，因此$$\{A_(m(x)) \}$$形成$$A$$的可數開覆蓋集合族 \(QED\)

## Heine-Borel 覆蓋定理



> 有界閉集合$$A \subseteq \mathbb{R}^n$$，且集合族$$F$$為$$A$$的開覆蓋，則存在$$F$$的有限子集合族為$$A$$的開覆蓋。
>
> * 註：必定存在開集合$$\mathbb{R}^n \ni A \in \mathbb{R}^n$$。
> * 註：由Lindelof 覆蓋定理得$$F$$為$$A$$的可數子覆蓋，因此將$$F$$中的所有集合聯集成單一集合S（可數個開集合的聯集仍然開集合），仍然可得$$A \subseteq S$$。

Proof:

* 由Lindelof定理得存在$$F$$的可數子集合族$$\{I_1,I_2,\ldots\}$$開覆蓋$$A$$，即$$ A\subseteq \bigcup_{i \in \mathbb{N}} I_i$$, $$I_i$$ 為開集合。
* 令$$S_m=\bigcup_{k=1}^m I_k$$，因為有限個開集合的聯集仍是開集合，因此$$S_m$$ 為開集合。
* 檢驗: $$\exists m \in \mathbb{N} \ni A \subseteq S_m$$
* 因為$$S_m$$ 為開集合，由定義得$$\mathbb{R}^n−S_m$$  為閉集合。
* 令$$Q_1=A$$, $$Q_2=A \cap (\mathbb{R}^n−S_1 )$$,$$\ldots ~Q_m=A \cap (\mathbb{R}^n−S_m )$$。
* 所以$$x \in Q_m \Rightarrow x \in A $$且$$ x \notin S_m$$, 即$$A$$中有些點不在$$S_m$$ 之中。
* 因此檢驗$$A\subseteq S_m$$ 等價於$$\exists m \in \mathbb{N} \ni Q_m=\emptyset$$。
* 由$$Q_1\supseteq Q_2 \supseteq \ldots \supseteq Q_m \ldots$$得集合序列$$\{Q_1,Q_2,\ldots,Q_m \}$$為遞減序列。
* 因為$$Q_1$$ 為有界集合且$$Q_m ,~ \forall m$$為閉集合，由[Cantor intersection theorem](bolzano-weierstrass-theorem.md#ying-yong-cantor-intersection-theorem) 得 $$\bigcap_{m=1}^\infty Q_m$$  為非空閉集合。
* 由$$\bigcap_{m=1}^\infty Q_m $$ 為非空閉集合可得存在$$x \in A$$ 且$$x \in Q_m, \forall m \in \mathbb{N}$$，即$$A$$中存在點$$x$$落在所有的集合$$S_m$$之外，$$\forall m \in \mathbb{N}$$
* 但此結論與假設$$A \subseteq \bigcup_{m=1}^\infty S_m=\bigcup_{m=1}^\infty I_m$$ 不符, 因此必定存在$$Q_m=\emptyset$$ \(\(QED\).









