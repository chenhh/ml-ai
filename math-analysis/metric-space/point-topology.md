# 點拓樸集

## 簡介

此為度量空間$$(X,d)$$的點拓樸集，與特定空間的點拓樸集，如$$\mathbb{R}^n$$相比性質較少，但是較為通用。

## 兩集合的距離

> $$A,B \subseteq X$$, $$d(A,B)=\inf \{ d(x,y)| \forall x \in A, ~ \forall y \in B\}$$
>
> • 集合的距離為兩集合間最短的兩點間的距離。>

### 兩集合間的距離不滿足三角不等式

* $$d(A,B) > d(A,C) + d(B,C)$$不滿足三角不等式。
* 但$$d(A,B) \leq d(A,C)+d(B,C)+d(C)$$成立



![](../../.gitbook/assets/set\_distance.png)

## 點到集合的距離

> $$A \subseteq X$$, $$x \in X$$, $$d(x,A)=\inf d(x,y), ~\forall y \in A$$
>
> &#x20;點到集合的距離為點到集合最短兩點間的距離。>

* 若$$A$$為閉集合，且$$x\notin A \Rightarrow d(x,A) >0$$

## 集合的直徑（diameter）

> $$S\subseteq X$$, $$d(S)=\sup\{ d(x,y), ~\forall x, y \in S \}$$
>
> $$S$$可為任意形狀的集合，集合$$S$$的直徑為集合中距離最遠兩點的長度。

* 集合的直徑可能為無窮大。例如$$S=(a,\infty) \text{ or }  (−\infty,b)$$

![集合的直徑為集合中兩點的最長距離](../../.gitbook/assets/set\_diameter-min.png)

## 有界集合（bounded set）

> 稱集合$$S$$為有界集合若滿足
>
> * $$\exists M\geq 0 , ~ y \in S \ni d(x,y) <M, \forall x \in S$$
> * 或 $$\exists M \geq 0 \ni  \sup d(x,y) < M, \forall x, y \in S$$
> * 或 $$\exists x \in S \exists r > 0 \ni S \subseteq N_r(S)$$

* &#x20;有界集合即集合中任意兩點的距離必定小於某個有限實數$$M$$。
* 無界集合即集合中存在兩點的距離為無窮大。因此必須是有界集合才可定義直徑。

## 鄰域、開球（neighborhood, open ball）

> 給定點$$a\in S$$與半徑$$r > 0$$，則點$$a$$以$$r$$為半徑的鄰域（neighborhood of a with radius r）記為 $$N_r(a) \equiv N(a,r)=\{b \in S | d(a,b) < r\}$$

* 注意$$N_r (a)$$包含了以$$a$$為圓心，$$r$$為半徑中，所有屬於集合$$S$$中的點，但不包含圓周上的點。
* **鄰域的定義中使用**$$d(a,b)$$**，因此只要符合距離測度的函數即可**。所以鄰域不一定是以$$a$$為中心的圓形，可能是菱形。$$d(a,b)=|a−b|$$或是其它形狀。
* 鄰域為開集合，因為所有的元素均為內點。

![鄰域或開球](../../.gitbook/assets/neighborhood.jpg)

## 內點（interior point）

> 稱點$$a \in S$$為集合$$S$$的內點若存在以$$a$$為中心的鄰域$$N_r(a)$$為$$S$$的子集合。$$\exists r > 0 \ni N_r(a) \subseteq S$$。
>
> 集合$$S$$中所有內點形成的集合記為$$int(S)$$

* 若點$$a$$恰好位於集合$$S$$的邊界上，則不存在符合上述定義的半徑$$r$$，因此不為內點；
* 反之若點$$a$$在集合$$S$$內，則一定可以找到滿足上述定義的半徑$$r$$

### 歐式空間中，內點一定是極限點

> 給定集合$$S\subseteq \mathbb{R}^n$$，內點$$a \in S$$（$$\exists r > 0 \ni N_r(a) \subseteq S$$），則$$a$$為$$S$$的極限點（$$\forall r > 0  N_r(a) \cap S \setminus \{a\} \neq \emptyset$$）。
>
> 註：一般拓墣空間不一定成立。

* 當$$a \in S$$為內點時，則\exists r > 0 \ni $$N_r(a) \subseteq S$$包含了$$S$$的無窮多個元素，即使扣除掉點$$a$$，$$N_r(a)$$與$$S$$的交集也不是空集合，因此$$a$$為極限點。(QED)

### 內點的性質

> 給定度量空間$$(X,d)$$與子集合$$A,B \subseteq X$$，則
>
> 1. $$A\subset B \Rightarrow int(A) \subset int(B)$$
>    * 反之不成立，考慮孤立點不為內點的情形。$$A=\{0\} \cup [1,2]$$, $$B=[0.5, 2.5]$$, $$int(A)=(1,2),~ int(B)=(0.5, 2.5)$$可得 $$int(A) \subset int(B)$$但$$A \nsubseteq B$$。
> 2. $$int(A\cap B)=int(A) \cap int(B)$$
> 3. $$int(A) \cup int(B) \subset int(A \cup B)$$
> 4. $$int(A)=X-\overline{X-A}$$，$$\overline{X-A}$$為$$X-A$$的閉包（closure）。
> 5. $$int(X-A)=X-\overline{A}$$
> 6. $$int(int(A))=int(A)$$
> 7. $$int(\cap_{i=1}^nA_i)=\cap_{i=1}^n(int(A_i)), ~ A_i \subseteq X$$
> 8. $$int(\cap_{i=1}^{\infty} A_i) \subseteq \cap_{i=1}^{\infty}(int(A_i)), ~ A_i \subseteq X$$
> 9. $$\cup_{i=1}^{\infty} (int(A_i)) \subseteq int(\cup_{i=1}^{\infty} A_i), ~ A_i \subseteq X$$
> 10. 若$$A$$在$$X$$中為開集合或閉集合，令$$\partial(A)$$為$$A$$的邊界點，則$$int(\partial A)=\emptyset$$，
> 11. 若$$int(A)=int(B)=\emptyset$$，則$$A$$在$$X$$為閉集合，則$$int(A \cup B)=\emptyset$$

proof 1:

* 令$$a \in int(A)$$，則$$\exists r > 0 \ni N_a(r) \subset A$$
* 因為$$A\subset B$$，可得$$N_a(r) \subset B$$，所以$$int(A) \subset int(B)$$(QED)

## 邊界點（boundary point）

> 令$$(X,d)$$為度量空間，給定子集合$$S \subset X$$
>
> 稱點$$p \in X$$為集合$$S$$的邊界點若$$\forall r >0 . N_r(a) \cap S \neq \emptyset$$且$$N_r(a) \cap S^c \neq \emptyset$$
>
> * $$x$$的每個鄰域中至少有一個點在 $$S$$ 中，且至少有一個點不在$$S$$ 中。

![x為內點，y為邊界點](../../.gitbook/assets/510px-Interior\_illustration-min.png)

## 邊界集合（boundary set）

> $$S \subseteq X$$，點$$p$$為集合$$S$$的邊界點，邊界集合記為$$\partial (S) = \{ p \in X | \forall r > 0 , N_r(p) \cap S \neq \emptyset \land N_r(p) \cap S^c \neq \emptyset \}$$

### 邊界集合的性質

> 1. $$A \subset B$$不一定可得$$\partial(A) \subset \partial(B)$$。
> 2. $$\partial(A) \cup \partial(B)$$不一定可得 $$\partial(A \cup B)$$。
> 3. $$\partial(A) \cap \partial(B)$$不一定可得 $$\partial(A \cap B)$$。
> 4. $$\partial(\emptyset)=\emptyset$$
> 5. $$\partial(\mathbb{Q})=\mathbb{R}$$

例如：

* $$A=[1,2]$$的閉區間，$$\partial(A)=\{1,2\}$$
* $$B=[0,3]$$的閉區間，$$\partial(B)=\{0,3\}$$
* $$A \subseteq B$$但$$\partial(A) \not \subset \partial(B)$$
* $$\partial(A \cup B) = \{0,3\}$$, $$\partial(A) \cup \partial(B)=\{0,1,2,3\}$$
* $$\partial (A \cap B) = \{1,2\}$$, $$\partial(A) \cap \partial(B) = \emptyset$$
* 實數$$\mathbb{R}$$​中，有理數$$\mathbb{Q}$$​與無理數$$\mathbb{R - Q}$$​的內部都是空集合，邊界都是$$\mathbb{R}$$​。

## 外點（exterior point）

> 點$$p \in S^c$$，若滿足$$\exists r > 0 \ni N_r(p) \subset S^c$$，則稱$$p$$為集合$$S$$的外點（或$$p$$為集合$$S^c$$的內點 ）
>
> 所有外點形成的集合記為$$ext(S)$$

## 集合的三一律

> $$\forall S \subset X$$，有以下的性質
>
> * $$int(S) \subset S$$
> * $$ext(S) = int(X\setminus S)$$
> * $$ext(S) \subset X \setminus S$$
> * $$int(S) \cap ext(S) = \emptyset$$
> * $$int(S) \cap \partial(S) = \emptyset$$
> * $$ext(S) \cap \partial (S) = \emptyset$$
> * $$int(S) \cup ext(S) \cup \partial(S) = X$$
>
> 因此點$$x \in int(S),~ x \in ext(S), ~ x \in \partial(S)$$只能有一個成立。

## 凝集點（condensation point）

> 集合$$S\subseteq X$$，若$$x\in X$$滿足 $$\forall r > 0, N_r(x)\cap S$$均為不可數集合時，稱$$x$$為$$S$$的凝集點。

### 不可數集合必存在凝聚點

> 若$$S$$為不可數集合，則存在$$x \in S$$為凝聚點。
>
> 反之，不存在凝聚點的集合必為可數集合。

* 假設$$\forall x \in S$$均不為凝聚點，則對於每一個點$$x$$, $$\exists r > 0 \ni N_{r(x)}(x) \cap S$$為可數集合。因此可得 $$S \subseteq \cup_{x \in S} (N_{r(x)}(x) \cap S)$$。
* 由於可數集合的（有限或無限）聯集仍為可數集合，且可數集合的任意子集仍為可數集合，因此得$$S$$為可數集合（QED）。

### 凝集點的性質

> 令集合$$S \subseteq X$$為不可數集合，且$$T$$為$$S$$的凝集點集合，則
>
> 1. $$S \setminus T$$為可數集合。
> 2. $$S \cap T$$為不可數集合。
> 3. $$T$$為閉集合。
> 4. $$T$$不包含孤立點。

* proof(1): $$S \setminus T$$中不包含凝集點，因此為可數集合。(QED)。
* proof(2): 因為$$S$$為不可數集合，因此$$S$$中必包含凝集點，可得$$S\cap T \neq \emptyset$$為部份凝集點的集合，因此為不可數集合。(QED)
* proof(3): 令$$x\in T$$為凝集點，由定義得$$\forall r > 0~ \exists N_r(x) \cap S$$為不可數集合，因此 $$\forall r > 0, N_r(x) \cap S \setminus \{ x\} \neq \emptyset$$，即$$x$$為$$S$$的極限點，可得$$T$$為所有$$S$$極限點的集合，因此$$T$$為閉集合(QED)。
* proof(4): 令$$x\in T$$為凝集點，由定義得$$\forall r > 0~ \exists N_r(x) \cap S$$為不可數集合，因此$$N_r(x) \cap S \neq \{x\}$$不包含孤立點。(QED)。

## 附著點（adherent point）

> 給定度量空間$$(X,d)$$，子集合$$S \subseteq X$$，點$$x\in X$$。若$$\forall r >0, N_r(x) \cap S \neq \emptyset$$ 則稱點$$x$$為集合$$S$$的附著點。
>
> 若$$x$$為$$S$$的附著點，可得$$\forall \epsilon > 0 \ \exists y \in S \ni d(x,y) < \epsilon$$。
>
> 註：有些書不區分附著點與極限點，因此要定義清楚。

* $$x$$為附著點，但$$x$$不必為集合$$S$$的元素。
* 附著點直觀的解釋是$$x$$的任意鄰域必定包含至少一個$$S$$集合中的元素。
* &#x20;附著點(鄰域)與極限點(去心鄰域)的定義，唯一差異是極限點與$$S$$的交集不可為點$$x$$自身。
* 因為$$x$$的任意鄰域$$N_r (x)$$均包含集合$$S$$至少一個元素，因此$$x$$為$$S$$中的元素或在$$S$$的邊界點上。
* 若$$x$$在集合$$S$$的邊界點外（外點），則$$\exists r>0 \ni N_r (x) \cap S=\emptyset$$。

#### 範例

* 在實數區間$$(a,b), [a,b], (a,b], [a,b)$$中的所有點都是附著點。

## 孤立點（isolated point）

> 集合$$S \subset X$$，如果點$$x\in S$$滿足 $$\exists r > 0 \ni N_r(x) \cap S = \{x\}$$，則稱$$x$$為孤立點。
>
> 若不是孤立點，則$$N_r(x) \cap S$$為不可數集合。

* 存在$$x$$的某一個鄰域即可，不需要保證$$x$$ 的每個鄰域都成立。
* $$x$$ 是$$S$$ 的孤立點，意味著 $$x$$ 必在 $$S$$ 中，但是它相當於在一個球隊中被孤立、靠邊站了，但還沒有離隊。
* 由定義知孤立點不是極限點。
* 由定義知孤立點不是內點, 因為若$$\exists r>0 \ni N_r (x) \subset S$$，可得$$N_r (x)\cap S=N_r (x) \neq \{x\}$$。
* 因為$$N_r (x) \cap S$$集合中元素應為無窮多個，若只有一個點時，表示$$x$$附近沒有任何元素，即為孤立點。
* 例如 $$S=\{1/n, \forall n \in \mathbb{N}\}$$，則$$S$$內的每一點都是孤立點。
* 例如$$S=\{0\} \cup [1,2]$$，則0為孤立點。
* 但$$S=\{0\} \cup \{ ,1, 1/2, 1/3,\ldots\}$$中，0不是孤立點，因為可以找到任意接近0的元素，但每一個1/k都是孤立點。

### 孤立點集合為可數集合

> • $$S \subseteq X$$, 令$$F$$為$$S$$中孤立點形成的集合，則$$F$$為可數(有限或無限)集合。

* 若$$S$$中的孤立點為有限個，則$$F$$為可數有限集合。
* 令$$S$$中孤立點個數為無限多個，考慮$$x \in S$$為孤立點，即 $$\exists r  > 0 \ni N_r(x) \cap S =\{ x\}$$。
* 因為$$F$$為孤立點的集合, 令$$r_1=\min⁡\{r >0~|~ \forall x \in F, N_r (x) \cap  S=\{x\}\}$$, 且令滿足此最小半徑的點為$$x_1$$， 則此點必定唯一，否則違反孤立點的定義。
* 從$$F\setminus \{x_1\}$$的集合中，可得$$r_2=\min \{  r>0  | \forall x \in F \setminus \{x_1\}, N_r (x) \cap S=\{x\}  \}$$ 且令滿足此最小半徑的點為$$x_2$$。
* 以此類推，可得$$F$$中的點與自然數集合$$\mathbb{N}$$有一對一的關係，因此$$F$$為可數集合。 (QED)

### 歐式空間中，孤立點就是邊界點

> 給定集合$$S \subseteq \mathbb{R}^n$$，點$$x \in S$$為孤立點（$$\exists r >0 \ni N_r(x) \cap S = \{x\}$$），則$$x$$為邊界點（$$\forall r>0 , N_r(x) \cap S \neq \emptyset ~\land~ \ N_r(x) \cap S^c \neq \emptyset$$）

* 例如$$S=\{0\} \cup [1,2]$$。$$x=0$$為孤立點，因存在$$r=0.5$$使得$$N_r(x)=(-0.5, 0.5) , N_r(x) \cap (S\setminus \{x\}) = \emptyset$$。
  * 由於$$x=0$$與$$[1,2]$$間存在空隙，因此$$x$$的任意鄰域均包含了不屬於$$S$$的元素，即$$\forall h > 0, N_h(x) \cap S^c \neq \emptyset$$。
  * 因此$$x$$為邊界點。

#### 反之邊界點不一定是孤立點

* $$S=[1,2]$$，邊界點為1,2，但都不是孤立點。

### 一般拓撲空間中，孤立點就不一定是邊界點

## 極限點（limit point）&#x20;

或稱accumulation point, cluster point

> * 給定集合$$S \subset X$$，點$$x \in X$$，若$$\forall r>0  \exists\ y \in S, y \neq x \ni y \in N_r (x)$$ 或 $$\forall r >0 (N_r (x)\cap S)\setminus \{x\} \neq \emptyset$$，則稱$$x$$為$$S$$的極限點。
> * $$x \in X$$為$$S$$的極限點，則$$\forall \epsilon >0, ~ \exists y \in S \setminus \{x\}  \ni d(x,y)<\epsilon$$。

* **由定義知極限點必為附著點**。
* &#x20;極限點就是由序列收斂點的觀點來定義極限的性質。
* 極限點直觀的解釋是$$x$$的**去心鄰域**必定包含至少一個S集合中的元素。

#### 範例

* 可得實數中閉區間$$[a,b]$$中所有元素都是極限點，而開區間$$(a,b)$$除了端點外均為極限點。
* $$\{\frac{1}{n}, n=1,2,\ldots\}$$的極限點只有0($$\lim_{n \rightarrow \infty} \frac{1}{n} = 0$$)。
* 有理數集合$$\mathbb{Q}$$的極限點為實數集合$$\mathbb{R}$$。

![極限點](../../.gitbook/assets/topological\_space\_accum-min.png)

### 沒有極限點的集合

* 自然數集合$$\mathbb{N}$$不存在極限點。

### &#x20;極限點的鄰域與集合交集的元素為無窮多個

> 若點$$x$$為集合$$S$$的極限點，則$$\forall r>0, N_r(x) \cap S \setminus \{x\}$$集合內的元素個數為無窮多個。

* 此定理可得出具有極限點的集合$$S$$內的元素必定為無窮多個。
* 但有無窮多個元素的集合不一定有極限點，如$$\mathbb{N}$$。

proof:

* 假設集合 $$(N_r (x)\cap S)\setminus \{x\}$$  只有有限個元素，記為$$p_1, p_2, \ldots, p_n$$。
* 令$$r_0=\min⁡(d(x,p_1 ), d(x,p_2 ),\ldots ,d(x,p_n ))$$
* 則$$N_{r_0} (x) \cap S\setminus \{x\}=\emptyset$$ 與極限點的定義矛盾  。
* 因此$$(N_r (x) \cap S) \setminus \{x\}$$  有無窮多個元素 (QED)

### 有限個數的集合不存在極限點

> 由上述的性質可得出。

### 集合內若存在極限點若且唯若存在相異無窮數列其收斂至此點

> $$x \in S$$為極限點 $$\Leftrightarrow$$$$\displaystyle \exists \{ x_n\} \subseteq S, x_i \neq x_j ~ \forall i \neq j, ~ \lim_{ n \rightarrow \infty} x_n =x$$
>
> 註： $$\{x_n\}$$內的點必須為相異點才有此性質，如$$\{0,1,1,\ldots,1,\ldots\}$$, $$x_1=0$$, $$x_n=1$$,$$\displaystyle \lim_{n \rightarrow \infty}⁡ x_n =1$$, 但1不是集合$$\{0,1\}$$的極限點。

proof =>:

* 若$$x$$為集合$$S$$的極限點，則
* $$r_1=1$$，取$$x_1 \in N_{r_1} (x)\cap S, x_1\neq x$$
* $$r_2=\frac{1}{2} \|x_1−x|<\frac{1}{2}$$，取$$x_2 \in N_{r_2} (x)\cap S,\ x_2 \neq x, x_2 \neq x_1$$
* &#x20;$$r_3=\frac{1}{2} \|x_2−x\|<\frac{1}{2^2}$$ ，取$$x_3 \in N_{r_3} (x)\cap S, x_3\neq x,x_1,x_2$$
* 以此類推可建構出無窮序列$$\{x_1,x_2,x_3, \ldots \} \subseteq S$$
* 且可得$$\lim_{n \rightarrow \infty}⁡ x_n=x$$(QED)

Proof <=

*   $$\displaystyle \{x_n\} \subseteq S,\ x_i \neq x_j, \ \forall i \neq j,\ \ lim_{n \rightarrow \infty}⁡x_n =x$$

    • 即$$\forall \epsilon >0 ~ \exists n_0 \in \mathbb{N} \ni   \forall n \geq n_0 \Rightarrow \|x−x_n \|< \epsilon$$

    • 因此$$\forall r>0, N_r (x) \cap S \setminus \{x\} \neq \emptyset$$, 得$$x$$為極限點 (QED)

## 導集合（derived set）

> 導集合$$d(S)$$為集合$$S$$所有極限點形成的集合。
>
> $$d(S)=\{x \in X | \forall r >0, N_r(x) \cap S \setminus \{ x\}\neq \emptyset \}$$

* 導集合$$d(S)$$和[閉包](closed-set.md#bi-bao-closure)$$\overline{S} = S \cup d(S)$$有重要的關聯性，參考[導集合的性質](closed-set.md#dao-ji-he-de-xing-zhi)。
* 導集合為閉集合。
* $$S=\{ \frac{1}{n}, \ n \in \mathbb{N}\}$$，則$$0$$為$$S$$的極限點。
* $$x_n=(-1)^n \frac{n}{n+1}$$極限不存在，但有兩個極限點-1與1。

![極限點為序列聚集之處](../../.gitbook/assets/800px-Rational\_sequence\_with\_2\_accumulation\_points\_svg.png)

###

## 完美集合（perfect set）

> $$S \subseteq X$$稱為完全集合，若此集合等於其導集合，即$$S=d(S)$$。>

由下面的性質可知**完全集合為不含孤立點的閉集合**。

### 完美集合若且唯若集合不含孤立點且為閉集合

* 由 $$S=d(S)$$  得$$S$$包含其所有極限點，因此完美集合$$S$$為閉集合。
* 若$$x \in S$$為孤立點，則 $$\exists r >0 \ni N_r(x) \cap S \setminus \{ x\} =\emptyset$$
* 但因為$$S=d(S)$$，因此$$\forall x \in S, N_r(x) \cap S \setminus \{x\} \neq \emptyset$$
* 所以$$S$$中不含孤立點。(QED)

### Cantor-Bendixon定理

> $$F \subseteq X$$ 為不可數閉集合，則可將$$F$$分解為$$F=A \cup B$$，$$A$$完美集合，$$B$$為可數集合。
>
> Note: 此定理說明**任意閉集合可分解為不含孤立點的閉集合與可數集合的聯集**。

* 因為$$F$$為不可數集合, 因此存在$$x \in F$$為其凝聚點。令$$T$$為$$F$$所有凝聚點形成的集合。
* 由凝聚點的性質，得$$T$$為閉集合且$$T$$不含孤立點，且$$F \setminus T$$為可數集合。
* 令$$A=T$$, $$B=F \setminus T$$ 得證 (QED)

