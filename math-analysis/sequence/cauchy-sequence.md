# 柯西數列(Cauchy sequence)

## 簡介

數列極限是否存在，依定義$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$必須要先知道收斂值$$a$$才可判定，而Cauchy數列只需知道數列中相鄰兩個元素間的距離是否足夠接近，即可判定數列是否收斂，而不需要知道收斂值。

## Cauchy數列

> $$(X,d)$$為度量空間，且$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列。> 若$$\forall \epsilon >0 ~ \exists n_0 \in \mathbb{N} \ni   d(a_n,a_m )<\epsilon ~ \forall n,m \geq n_0$$，則稱$$\{a_n\}$$為Cauchy序列。

* Cauchy序列的功能在於不須知道收斂值，只須檢定數列中元素的接近程度即可判別數列是否收斂。
* 任意度量空間中，由定或可得出收斂數列必為Cauchy數列。
* 實數空間中，因為實數的完備性，因此Cauchy數列必為收斂數列。反之一般的度量空間，必須是完備空間，才能夠保證Cauchy數列是收斂數列。

### 收斂數列必為Cauchy數列

> $$(X,d)$$為度量空間，且$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列。若$$\displaystyle \lim_{n \rightarrow \infty} a_n = a$$，則$$\{a_n\}$$為Cauchy數列。

* 任意度量空間中，由定義可得出收斂數列必為Cauchy數列。
* 實數空間中，因為實數的完備性，因此Cauchy數列必為收斂數列。反之一般的度量空間，必須是完備空間，才能夠保證Cauchy數列是收斂數列。

Proof:

* 令$$\{a_n\}_{n \in \mathbb{N}} \subseteq X$$為一數列且$$\displaystyle \lim_{n \rightarrow \infty} a_n =a$$
* 由收斂定義得$$\forall \epsilon>0  ~ \exists n_1 \in \mathbb{N} \ni d(a_n,a)<\epsilon/2  ~ \forall n \geq n_0$$
* 由三角不等式得$$d(a_n,a_m )<d(a_m,a)+d(a_n,a)<\epsilon ~\forall n,m≥n_0$$  (QED)

### Cauchy數列的子數列若收斂，則原數列收斂至同一點

> $$\{a_n\}$$為度量空間$$(X,d)$$中的Cauchy數列，若子數列$$\{a_{n_r} \}$$收斂，$$\displaystyle \lim_{r \rightarrow \infty} a_{n_r}  =a$$，則$$\displaystyle \lim_{n \rightarrow \infty} a_n =a$$。

* 度量空間中，[收斂數列的子數列必為收斂數列且收斂至同一點](./#shou-lian-shu-lie-de-zi-shu-lie-bi-wei-shou-lian-shu-lie-qie-shou-lian-zhi-tong-yi-dian)。反之必須要所有的子數列均收斂到同一點，才能保證原始數列收斂。**而Cauchy子數列簡化了此性質，只要Cauchy數列的子數列收斂，則可保證原數列收斂至同一點**。

Proof:

* $$\{a_n\}$$為Cauchy數列，且子數列$$\displaystyle \lim_{r \rightarrow \infty} a_{n_r} =a$$
* 由收斂定義得$$\forall \epsilon>0 ~ \exists n_1 \in \mathbb{N} \ni d(a_{n_r},a)<\epsilon, ~ \forall n \geq n_1$$
* 因為$$\{a_n\}$$為Cauchy數列，所以$$\forall \epsilon>0 ~\exists n_2 \in \mathbb{N}   \ni d(a_n,a_m)<\epsilon, ~\forall n,m \geq n_2$$
* 取$$n_0=n_1+n_2$$
* 由三角不等式可得 $$d(a_n,a) \leq d(a_n,a_{n_0})+d(a_{n_0},a)<\epsilon$$ (QED)

### 實數中的所有Cauchy數列都是有界數列

> $$\{a_n\} \subseteq \mathbb{R}$$為Cauchy數列，則$$\exists r > 0 \ni  |a_n| \leq r ~ ,\forall n$$
>
> * 有界數列不一定是Cauchy數列。如$$\{a_n = \sin n\} \subseteq  [-1,1]$$但不是Cauchy數列，也不是收斂數列。

proof:

* 依Cauchy數列定義，給定$$\epsilon=1 ~\exists n_0 \in \mathbb{N} \ni |a_n−a_m |<1 ~\forall n,m \geq n_0$$
* 因此當$$n \geq n_0$$ 時，$$|a_n−a_{n_0} |<1 \Rightarrow |a_n |<|a_{n_0} |+1$$
* 令$$r=\max \{|a_1 |, |a_2 |,\ldots,|a_{n_0−1} |, |a_{n_0} |+1\}$$
* 可得$$\forall n \in \mathbb{N}, ~ |a_n | \leq r$$
* 因此$$\{a_n\}$$為有界數列 (QED).

### 實數中的任意Cauchy數列都會收斂

> 因為實數為完備空間，所以定理成立> 。一般度量空間必須為完備空間才有此性質。
>
> 非完備空間之Cauchy數列的收斂點可能不在該空間中。例如有理數中的Cauchy數列可能收斂至無理數。>

Proof：存在性

* 令$$\{a_n \}_{n \in \mathbb{N}} \subseteq \mathbb{R}$$為Cauchy數列，因為[實數中的所有Cauchy數列都是有界數列](cauchy-sequence.md#shi-shu-zhong-de-suo-you-cauchy-shu-lie-du-shi-you-jie-shu-lie)，所以$$\{a_n\}$$為有界集合。
* $$\forall n \in \mathbb{N}$$, 令$$S_n=\{a_m |m \in \mathbb{N},  m \geq n\}$$是由數列$$\{a_n,a_{n+1},a_{n+2}, \ldots\}$$所形成的集合。
* 則得遞減集合序列 $$S_1 \supseteq S_2\supseteq \ldots  \supseteq S_n \supseteq \ldots$$，且$$\forall n, ~S_n$$ 均為有界集合。
* 依實數的非空有界子集合必有上確界性質，令$$b_n=\sup⁡(S_n), c_n=\inf⁡(S_n ) \Rightarrow c_n \leq a_n \leq b_n$$
* 因為$$S_{n+1} \subseteq S_n \Rightarrow b_n \geq b_{n+1} \geq c_{n+1}  \geq c_n$$
* 根據數學歸納法，$$\forall m,n \in \mathbb{N}, b_n \geq b_{n+m} \geq c_{n+m} \geq c_n$$
* 因此集合$$\{b_n\}_{n \in \mathbb{N}}$$的元素均大於等於$$\{c_n\}_{n \in \mathbb{N}}$$ 的元素。
* 所以集合$$\{b_n\}$$ 有下界且$$\{c_n\}$$ 有上界。
* 令$$b=\inf⁡(\{b_n\}), c=\sup⁡{\{c_n\} } \Rightarrow b \geq c$$−−(1)

proof： 證明收斂於一點

* $$\{a_n \}\subseteq \mathbb{R}$$為Cauchy數列，由定義得$$\forall \epsilon>0 ~\exists n_0 \in \mathbb{N} \ni |a_n−a_m |<\epsilon ~\forall n,m \geq n_0$$
* 移項後可得$$\forall ϵ>0,  ~\exists n_0 \in \mathbb{N} \ni a_n−\epsilon<a_m<a_n+\epsilon ~ \forall n,m \geq n_0$$
* 令集合$$S_n=\{a_m |m \in \mathbb{N}, ~ m \geq n_0 \}$$，則$$S_n$$的所有元素均小於集合$$\{a_n+ \epsilon |n \in \mathbb{N},~ n \geq n_0 \}$$的所有元素  。
* 因此集合$$S_n$$內的最小上界小於或等於後一個集合內的最大下界。
* 即$$b_{n_0} \leq c_{n_0}+\epsilon \Rightarrow 0 \leq b−c \leq b_{n_0}−c_{n_0} \leq \epsilon$$
* 因此 $$\forall \epsilon>0, ~0 \leq b−c \leq \epsilon⇒b=c$$−−(2)

proof：證明數列收斂於同一點

* $$\forall \epsilon>0, b+\epsilon$$不是$$\{b_n\}$$的下界，因此$$\exists n_1 \in \mathbb{N}  \ni b_{n_1}<b+ \epsilon$$。
* 同理$$\forall \epsilon>0, b−\epsilon =c−\epsilon$$不是$$\{c_n\}$$的上界，因此$$\exists n_2 \in \mathbb{N}  \ni c_{n_2} >b−\epsilon$$。
* 取$$n_0=\max\{n_1,n_2\}$$，則當$$n \geq n_0$$ 時，可得$$b_{n_1} \leq b_{n_0} <b+\epsilon, ~ c_{n_0} \geq c_{n_2} >b−\epsilon$$
* $$b-\epsilon<c_n \leq a_n \leq b_n<b+\epsilon  \Rightarrow |a_n−b|<\epsilon,  \forall n \geq n_0$$
* 所以 $$\displaystyle \lim_{n \rightarrow \infty} a_n =b$$−−(3)

由(1,2,3)可得Cauchy數列$$\{a_n \} \subseteq \mathbb{R}$$收斂至一實數  (QED)

完備度量空間(complete metric space)


> 度量空間$$(X,d)$$  稱為完備度量空間若集合$$X$$中的任意Cauchy數列均收斂至$$X$$中的某一點。

### 範例：有理數不是完備空間&#xD;

* $$x_0=1$$, $$x_{n+1}=\frac{x_n+\frac{2}{x_n}}{2}  \in \mathbb{Q}$$, $$\displaystyle \lim_{n \rightarrow \infty} x_n =\sqrt{2} \notin \mathbb{Q}$$

### 完備空間中的任意緊緻子集合仍為完備空間

> * $$(X,d)$$為完備度量空間，$$S \subseteq X$$為緊緻集合(compact  set)（即$$S$$的任意開覆蓋均存在有限個數的子開覆蓋），則$$(S,d)$$為完備度量空間。

例如：實數上的閉區間$$[a,b]$$為完備度量空間。

Proof :

* $$\{x_n\}\subseteq S$$為Cauchy數列，且$$A=\{x_1,x_2,\ldots\}$$為數列的值域。
* 若$$A$$為有限集合，則$$\{x_n\}$$必定收斂至$$S$$中的某一點，因此$$\{x_n\}$$收斂在$$S$$中。
* 若$$A$$為無限集合，因為$$(X,d)$$為完備度量空間，因此可得 $$p \in A$$為極限點，$$S$$為緊緻集合，由度量空間[緊緻集合的充要條件](../real-number/compact-set.md#ou-shi-kong-jian-zhong-jin-zhi-ji-he-de-chong-yao-tiao-jian)（緊致集合$$S$$的任意無窮子集合均存在極限點$$x$$，且$$x \in S$$）可得$$p \in S$$。
* $$\forall \epsilon>0, \text{ take }N \in \mathbb{N} \ni d(x_n,x_m )<\frac{\epsilon}{2}, ~\forall n,m \geq N$$
* 則$$N_{\frac{\epsilon}{2}} (p)$$至少包含了點$$x_m, ~ \forall m \geq N$$
* 若$$n \geq N$$，由三角不等式得 $$d(x_n,p) \leq d(x_n,p)+d(x_m,p)<\epsilon/2+\epsilon/2=\epsilon$$
* 所以$$\displaystyle \lim_{n \rightarrow \infty} x_n = p$$且$$p \in S$$，所以$$S$$為完備度量空間 (QED)

### 完備度量空間為閉集合

> 若$$(X,d)$$為度量空間（不必完備），$$S \subseteq X$$為完備度量空間，則$$S$$為閉集合（$$X-S$$為開集合）。&#x20;>

* 例如：實數上的閉區間$$[a,b]$$為完備度量空間，且為閉集合。
* 例如：實數$$\mathbb{R}$$為完備度量空間，包含了所有極限點，為閉集合（但同時也為開集合）。

proof :

* 令$$\{ x_n \} \subseteq  S$$為Cauchy數列，且令$$\lim_{n \rightarrow \infty} x_n = p$$，因為$$(S,d)$$為完備度量空間，可得$$p \in S$$。
* 因為所有Cacuhy數列的極限點均為$$S$$的元素，由[閉集合](../metric-space/closed-set.md#bi-ji-he-closed-set)的定義得$$S$$為閉集合(QED)。
