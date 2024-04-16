# 機率測度(probability measure)

基本名詞

* 一個<mark style="color:red;">**隨機實驗（random experiment）**</mark>是一個機會機制（chance mechanism）且滿足以下三個條件：
  1. 實驗的所有可能結果（outcome）已事先知道。
  2. 但每一次實驗的結果無法事先預知，而這些結果的發生有某種規律。
  3. 每一次實驗都可以在同樣的條件下進行。
* <mark style="color:red;">**結果(outcome)**</mark>$$\omega$$為**樣本空間**$$\Omega$$的一個元素，稱為一個**點或樣本（point or sample point）**。
  * 投一個銅板的樣本空間為$$\Omega = \{ H, T\}$$。
  * 丟一顆骰子的樣本空間為 $$\Omega=\{1,2,3,4,5,6\}$$。
  * 每天股價的樣本空間為 $$\Omega = \{x_t | 0 < x_t < \infty\}$$。
* 而樣本空間的任一子集稱為<mark style="color:red;">**事件(event)**</mark>，$$E \subseteq \Omega$$，因此事件中包含了許多(有限或無限多個)結果。
* <mark style="color:red;">sigma-field(sigma-algebra)</mark> $$\mathcal{F}$$為滿足特定條件的事件集合的集合。
* <mark style="color:red;">**隨機變數**</mark>$$X: \mathcal{F} \rightarrow \mathbb{R}$$為函式，將sigma-field中的元素(事件)，對映到實數值。因此給定實數值$$a \in \mathbb{R}$$，可得前像為事件集合的集合，可得$$X^{-1}(a) \in \mathcal{F}$$。
* <mark style="color:red;">**機率測度**</mark>$$\mathrm{P}$$量測的是滿足某個實數值$$a$$的前像(事件集合的集合, $$X^{-1}(a)$$)發生的機率。(機率測度測量滿足特定條件的集合後，給出一個實數值)。

## 機率測度（probability measure）

機率測度是用來衡量或計算某一個隨機實驗結果發生的可能性(事件集合)，加以量化。

> 對於樣本空間$$\Omega$$每一個(子集合)可測的事件$$E$$而言\[（或者對於$$\Omega$$的sigma-field $$\mathcal{F}$$中的元素$$E$$）機率測度$$\mathrm{P}: \mathcal{F} \rightarrow \mathbb{R}$$\[直接考慮可測集合]，實數$$\mathrm{P}(E)$$若滿足以下三個條件時，稱$$\mathrm{P}(E)$$為事件$$E$$的機率（測度）。
>
> 1. \[<mark style="color:blue;">機率為正實數</mark>]$$\mathrm{P}(E) \geq 0, ~ E \in \mathcal{F}$$。。
> 2. \[<mark style="color:blue;">宇集合的機率為1</mark>] $$\mathrm{P}(\Omega) = 1$$。。
> 3. \[<mark style="color:blue;">sigma-additive</mark>]$$\mathrm{P}(\cup_{i \in \mathbb{N}} E_i )= \sum_{i \in \mathbb{N}} \mathrm{P}(E_i)$$,$$E_i \cap E_j = \emptyset, \ \forall i \neq j$$為兩兩互斥的事件集合。不相交的事件，其聯集機率為個別事件機率之和。
>
> 註：機率測度只有定義事件的條件，可為任意的分佈。

### 機率空間（probability space）

計算機率有三個元素，宇集合$$\Omega$$，宇集合中的子集合（事件）形成的simga-field $$\mathcal{F}$$，與機率測度$$\mathrm{P}$$，三者$$(\Omega, \mathcal{F}, \mathrm{P})$$合稱<mark style="color:red;">機率空間</mark>。

整體金融市場以機率空間表示時，$$\Omega$$為金融市場，$$\mathcal{F}$$為金融市場的訊息及相關資料，$$\mathrm{P}$$為對金融事件發生的機率測度。

### 性質

給定機率空間為$$(\Omega, \mathcal{F}, P)$$

> \[<mark style="color:blue;">事件集合機率的上下限</mark>] $$\forall E \in \mathcal{F}, 0 \leq \mathrm{P}(E) \leq 1$$

* $$\mathrm{P}(\Omega) = \mathrm{P}(E \cup E^c) = \mathrm{P}(E) +\mathrm{P}(E^c) = 1$$
* $$\because \mathrm{P}(E) \geq 0$$ 且 $$\mathrm{P}(E^c) \geq 0$$, $$\therefore 0 \leq \mathrm{P}(E) \leq 1$$(QED)

> \[<mark style="color:blue;">補集事件發生的機率</mark>] $$\forall E \in \mathcal{F}, \mathrm{P}(E^c)=1 - \mathrm{P}(E)$$。$$E^c$$為$$E$$的餘事件（complementary event）

* $$\because \mathrm{P}(\Omega)=\mathrm{P}(E \cup E^c)= \mathrm{P}(E) + \mathrm{P}(E^c)=1$$$$\therefore \mathrm{P}(E^c) = 1 - \mathrm{P}(E)$$ (QED)

> $$\mathrm{P}(\emptyset)=0$$。$$\emptyset$$為<mark style="color:red;">零事件（null event</mark>），又稱空事件，指該事件永不發生。

* $$\because \Omega \cup \emptyset = \Omega$$且$$\mathrm{P}(\Omega ) = \mathrm{P}(\Omega \cup \emptyset) = \mathrm{P}(\Omega) + \mathrm{P}(\emptyset)=1 + \mathrm{P}(\emptyset) =1$$。

> $$\mathrm{P}(F \cap E^c)=\mathrm{P}(F) - \mathrm{P}(E \cap F)$$

* $$\mathrm{P}(F) = \mathrm{P}((F \cap E^c) \cup (E \cap F)) = \mathrm{P}((F \cap E^c) + \mathrm{P}(E \cap F)$$ (QED)

> $$\mathrm{P}(E \cup F) = \mathrm{P}(E) + \mathrm{P}(F) - \mathrm{P}(E \cap F)$$

* $$\begin{aligned} \mathrm{P}(E \cup F) &= \mathrm{P}((E \cap F^c) \cup (E \cap F) \cup (E^c \cap F)) \\ &= \mathrm{P}(E) - \mathrm{P}(E \cap F) + \mathrm{P}(E \cap F) + \mathrm{P}(F) - \mathrm{P}(E \cap F) \\& = \mathrm{P}(E) + \mathrm{P}(F) - \mathrm{P}(E \cap F) \end{aligned}$$(QED)

> If $$E \subseteq F$$ then $$\mathrm{P}(F \setminus E) = \mathrm{P}(F) - \mathrm{P}(E)$$ and $$\mathrm{P}(E) \leq \mathrm{P}(F)$$

* $$\because \mathrm{P}(F) = \mathrm{P}(E \cup (F \setminus E)) = \mathrm{P}(E) + \mathrm{P}(F \setminus E)$$且 $$\mathrm{P}(F \setminus E) \geq 0$$, $$\therefore \mathrm{P}(F) \geq \mathrm{P}(E)$$

> \[Bonferroni inequality] $$\mathrm{P}(E \cap F) \geq \mathrm{P}(E) + \mathrm{P}(F) -1$$
>
> * $$\mathrm{P}( (E \cap F)^c) = \mathrm{P}(\Omega \setminus (E \cap F)) = 1- \mathrm{P}(E \cap F)$$--(1)
> * $$\mathrm{P}((E \cap F)^c)=\mathrm{P}(E^c \cup F^c) \leq \mathrm{P}(E^c)+\mathrm{P}(F^c)$$且$$\mathrm{P}(E^c)= 1-\mathrm{P}(E), \mathrm{P}(F^c)=1-\mathrm{P}(F)$$--(2)
> * (1)(2)得 $$1-\mathrm{P}(E \cap F) \leq 2 - \mathrm{P}(E) - \mathrm{P}(F)$$移項得 $$\mathrm{P}(E \cap F) \geq \mathrm{P}(E) + \mathrm{P}(F) -1$$(QED)

> 令事件$$E_1, E_2, \ldots$$為$$\Omega$$的分割(partition)，即$$E_i \cap E_j = \emptyset,\ \forall i \neq j$$且 $$\cup_{i \in \mathbb{N}} E_i = \Omega$$，則$$\mathrm{P}(F) = \sum_{i \in \mathbb{N}} \mathrm{P}(F \cap E_i), \forall F \in \mathcal{F}$$。

### 多事件聯集的機率

* $$\begin{aligned} \mathrm{P}(E_1 \cup E_2 \cup E_3) & = \mathrm{P}(E_1)+\mathrm{P}(E_2)+\mathrm{P}(E_3) \\& - \mathrm{P}(E_1 \cap E_2) - \mathrm{P}(E_1 \cap E_3) - \mathrm{P}(E_2 \cap E_3) \\ & + \mathrm{P}(E_1 \cap E_2 \cap E_3) \end{aligned}$$
* $$\begin{aligned} \mathrm{P}(\cup_{i=1}^n E_i) & = \sum_{i=1}^n \mathrm{P}(E_i) \\& - \sum_{i \leq i < j \leq n} \mathrm{P}(E_i \cap E_j) \\ &+ \sum_{1 \leq i < j < k \leq n} \mathrm{P}(E_i \cap E_j \cap E_k) +\ldots \\ &+(-1)^{n+1} \mathrm{P}(E_1 \cap E_2 \cap \ldots \cap E_n) \end{aligned}$$

### 條件機率（conditional probability）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，給定$$F$$發生後的條件下，$$E$$發生的條件機率為$$\mathrm{P}(E|F) = \frac{\mathrm{P}(E \cap F)}{\mathrm{P}(F)},\ \mathrm{P}(F) \neq 0$$。

### 全機率定理（total probability theorem）

$$E, F_1, F_2,\ldots, F_N$$為定義於樣本空間$$\Omega$$的事件（集合），且$$F_1, F_2,\ldots, F_N$$兩兩互斥則$$\displaystyle \mathrm{P}(E) = \sum_{i=1}^N \mathrm{P}(A|F_i) \mathrm{P}(F_i), \ \mathrm{P}(F_i) \neq 0 \ \forall i$$

### 機率獨立（statistically independent）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，若且惟若$$\mathrm{P}(E \cap F) = \mathrm{P}(E)\mathrm{P}(F)$$，則稱$$E,F$$為二<mark style="color:red;">獨立事件</mark>。

* 註：$$\mathrm{P}(E\cap F) = \mathrm{P}(E|F)\mathrm{P}(F)$$。如果兩事件獨立時，則$$\mathrm{P}(E\cap F)=\mathrm{P}(E)\mathrm{P}(F)$$，因此可知兩事件獨立時，$$\mathrm{P}(E) = \mathrm{P}(E|F)$$，以資訊理論解釋就是事件$$F$$不包含關於事件$$E$$的資訊，因此兩事件獨立。

$$E_1, E_2, E_3$$為樣本空間$$\Omega$$的三個事件，若且惟若滿足以下條件時，$$E_1, E_2, E_3$$為獨立事件：

* $$\mathrm{P}(E_1 \cap E_2)=\mathrm{P}(E_1)\mathrm{P}(E_2)$$
* $$\mathrm{P}(E_1 \cap E_3)=\mathrm{P}(E_1)\mathrm{P}(E_3)$$
* $$\mathrm{P}(E_2 \cap E_3)=\mathrm{P}(E_2)\mathrm{P}(E_3)$$
* $$\mathrm{P}(E_1 \cap E_2 \cap E_3)=\mathrm{P}(E_1)\mathrm{P}(E_2)\mathrm{P}(E_3)$$
* 共$$\begin{pmatrix} 3 \\2 \end{pmatrix} + \begin{pmatrix} 3 \\3 \end{pmatrix} = 3 + 1=4$$個條件。

如果有$$E_1, E_2, \ldots, E_N$$個定義於樣本空間$$\Omega$$的$$N$$個事件，則需要$$\begin{pmatrix} N \\ 2 \end{pmatrix} + \begin{pmatrix} N \\ 3 \end{pmatrix} + \ldots + \begin{pmatrix} N \\ N \end{pmatrix} = 2^N - 1 -N$$個條件。

### 貝式定理（Baye's theorem）

若$$E, F_1, F_2, \ldots, F_N$$為定義於樣本空間$$\Omega$$的事件且$$F_i \cap F_j = \emptyset, \ \forall i \neq j$$為互斥事件，則$$\mathrm{P}(F_i|E) = \frac{P(F_i \cap E)}{\mathrm{P}(E)} = \frac{\mathrm{P}(E|F_i)\mathrm{P}(F_i)}{\sum_{i=1}^N \mathrm{P}(E|F_i)\mathrm{P}(F_i)}$$。

註：如果事件集合$$F_i \cap F_j \neq \empty$$，在證明中常用方法是建立新的集合序列$$E_1=F_1$$, $$E_2=F_2 - E_1, \dots, E_n=F_n-\cup_{k=1}^{n-1} E_n$$，如此一來為兩兩互斥的集合序列。

## 機率測度的連續性(單調集合極限的測度)

> 給定集合序列$$\{E_n\}_{n \in \mathbb{N}}$$，如果：
>
> * [遞增集合序列](../math-analysis/set/limit-of-set-sequence.md#di-zeng-ji-he-xu-lie-de-ji-xian-wei-suo-you-ji-he-de-lian-ji)，即$$E_1 \subseteq E_2 \subseteq  \cdots$$，可得$$\displaystyle \lim_{n \rightarrow \infty} E_n = \bigcup_{n \in \mathbb{N}} E_n$$，因此$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{P}(E_n) =\mathrm{P}(\lim_{n \rightarrow \infty} E_n ) = \mathrm{P}(\bigcup_{n \in \mathbb{N}} E_n)$$。
> * [遞減集合序列](../math-analysis/set/limit-of-set-sequence.md#di-jian-ji-he-xu-lie-de-ji-xian-wei-suo-you-ji-he-de-jiao-ji)，即$$E_1 \supseteq E_2 \supseteq \dots$$，可得$$\displaystyle \lim_{n \rightarrow \infty} E_n = \bigcap_{n \in \mathbb{N}} E_n$$，因此$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{P}(E_n) =\mathrm{P}(\lim_{n \rightarrow \infty} E_n ) = \mathrm{P}(\bigcap_{n \in \mathbb{N}} E_n)$$。
>
> 同[一般測度的性質](../math-analysis/measure/#di-zeng-ji-he-ji-xian-de-ce-du-ce-du-de-lian-xu-xing-continuity-of-measure)，注意機率測度為有限測度。

### 機率在無窮大事件的矛盾範例

給定一無窮大的袋子，且有無限多個編號為1、2、…的球。

#### 實驗1&#x20;

* 在中午12點前差1分時，將1\~10號球放入袋中，同時取出10號球(假設取出時不花時間)。
* 在中午12點前差1/2分時，將11\~20號球放入袋中，同時取出20號球。
* 在中午12點前差1/4分時，將21\~30號球放入袋中，同時取出30號球。
* 以此類推。

<mark style="color:blue;">則在12點整時候，袋子中有無限多個球</mark>。

在12點前差$$(1/2)^{n-1}$$分，都是取編號$$10n$$的球。因為任一球的號數，只要不是10的倍數都在袋子中，且在12點前並沒有取出。

#### 實驗2

* 在中午12點前差1分時，將1\~10號球放入袋中，同時取出1號球(假設取出時不花時間)。
* 在中午12點前差1/2分時，將11\~20號球放入袋中，同時取出2號球。
* 在中午12點前差1/4分時，將21\~30號球放入袋中，同時取出3號球。
* 以此類推。

<mark style="color:blue;">則在12點整時候，袋子中沒有任何球</mark>。

考慮編號$$n$$的球，在12點前差$$(1/2)^{n-1}$$分，該球會從袋中被取出。因此對於第$$n$$號球，在12點之前都會被取出。

#### 實驗3

設定同上，在12點前差$$(1/2)^{n-1}$$分，隨機取出一球，<mark style="color:blue;">則12點整時，袋中沒有任何球</mark>。

考慮編號1的球，定義事件$$E_n$$為$$n$$次取球後，1號球仍在袋裡的事件。因此$$\mathrm{P}(E_n)=\frac{9 \times 18 \times 27 \times 9n}{10 \times 19 \times 28 \times \dots (9n+1)}$$。因為第1次取球時，不取到1號球的機率為9/10；第二次取球時，不取到1號球的機率為18/19，以此類推。

在12點時，1號球留在袋中的事件為$$\bigcap_{n=1}^\infty E_n$$，且$$E_1 \supseteq E_2 \supseteq \dots$$為遞減集合序列，因此$$\displaystyle \mathrm{P}( \lim_{n \rightarrow \infty} E_n) =\mathrm{P}(\bigcap_{n=1}^\infty E_n) =\prod_{n=1}^\infty \left(  \frac{9n}{9n+1}\right)=0$$。

令$$F_i$$為在12點時，第$$i$$號球仍在袋中的事件。已知$$\mathrm{P}(F_1)=0$$，同理可得$$\mathrm{P}(F_i)=0, \forall i \in \mathbb{N}$$。

因此在12點，袋裡有球的機率為$$\mathrm{P}(\bigcup_{i=1}^\infty F_i) \leq \sum_{i=1}^\infty \mathrm{P}(F_i)=0$$。

## 事件序列上/下極限

> 給定集合序列$$\{E_n\}_{n \in \mathbb{N}}$$，定義：
>
> * 上極限$$\displaystyle \limsup_{n \rightarrow \infty} E_n =\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k$$。in infinitely many of the sets.
> * 下極限$$\displaystyle \liminf_{n \rightarrow \infty} E_n =\bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k$$。in all but finitely many the sets.

<mark style="background-color:red;">上極限由「不會永遠離開」的元素組成（在</mark>$$n$$<mark style="background-color:red;">之後的部份集合中，因此有無限多個集合包含這些元素）</mark>。

<mark style="background-color:red;">下極限由「最終永遠存在」的元素組成（在某個指標</mark>$$n$$<mark style="background-color:red;">之後的所有集合中，因此下極限的元素只不存在於有限個集合中</mark>）。

令$$M_n = \bigcup_{k=n}^\infty E_k$$，可得$$M_1 \supseteq M_2 \supseteq \dots$$為遞減集合序列

假設樣本點$$x$$屬於上極限。當$$n=1$$時，$$x \in M_1 \cap M_2 \cap\dots$$為所有集合的交集，當$$n=2$$時，$$x \in M_2 \cap M_3 \cap \dots$$為排除掉$$E_1$$後的所有集合交集，因此樣本點不屬於$$E_1$$。依此類推$$x$$不屬$$E_1, E_2, \dots, E_n, \dots$$等有限個集合，只有在$$n \rightarrow \infty$$時的集合才能得到樣本點。而滿足此條件的集合有無限多個。

## Borel-Cantelli lemma

> $$E_1, E_2, \dots$$為可測事件序列，若$$\sum_{n=1}^\infty \mathrm{P}(E_n) < \infty$$，則$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) = 0$$或$$\displaystyle \mathrm{P}(\liminf_{n \rightarrow \infty} E_n) = 1$$。
>
> $$\displaystyle \begin{aligned} \mathrm{P}(\limsup_{n \rightarrow \infty} E_n)      & = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k \\ & = \{\omega \in \Omega ~|~ \omega \in \text{ infinitely many (often) } E_n \} \\  & = \{\omega \in \Omega ~|~ \forall n \in \mathbb{N} ~ \exists n_0 > n \ni \omega \in E_{n_0} \} \end{aligned}$$
>
> 註：此處不要求$$E_i, E_j$$間為獨立事件。\
> <mark style="color:red;">無窮多個(Infinite)事件發生的機率，其總和若為有限(Finite)，則此無窮多個事件同時發生(交集)的機率為0</mark>。
>
> 如果無限多個集合的測度和為有限值，那麼包含於在無限多個集合中的子集的測度必為0，否則這無限多個集合每個測度都不小於$$\epsilon$$ ，加在一起就無窮大了。
>
>

[測度版本的證明](../math-analysis/measure/#the-borel-cantelli-lemma)。

上極限可解釋為就是無窮個集合中都存在的元素的集合。

假設歌手舉辦第$$k$$場演唱會，令參加該場演唱會的人數集合為$$E_k$$，而$$\mathrm{P}(E_k)$$為該場演唱會中，成為粉絲的機率。若$$\sum_{n=1}^\infty \mathrm{P}(E_n) < \infty$$，表示歌手舉辦了無限多次演唱會，且圈粉的機率總和為有限值。$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n)$$表示舉辦無限次演唱會時，圈粉的機率上極限。如果$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) > 0$$, 表示每次舉辦演唱會總是可以圈粉，此時可得$$\sum_{n=1}^\infty \mathrm{P}(E_n) \rightarrow \infty$$與假設矛盾。因此$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) \leq 0$$。而機率測度公理要求$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) \geq 0$$，因此可得$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) = 0$$。

<details>

<summary>proof:遞減事件序列集合測度</summary>

令$$M_n = \cup_{k=n}^\infty E_k$$

可得$$M_1 \supseteq M_2 \supseteq \dots$$為遞減集合序列。因此$$\displaystyle \lim_{n  \rightarrow \infty}  M_n = \bigcap_{n=1}^\infty M_n$$。

可得$$\displaystyle \mathrm{P}(\lim_{n  \rightarrow \infty}  M_n) = \lim_{n \rightarrow \infty} \mathrm{P}( M_n)$$

可得：

$$\displaystyle \begin{aligned} \mathrm{P}(\limsup_{n \rightarrow \infty} E_n)      & = \mathrm{P}(\bigcap_{n=1^\infty} \bigcup_{k=n}^\infty E_k) \\     & = \mathrm{P}(\lim_{n \rightarrow \infty } \bigcup_{k=n}^\infty E_k ) \\     & = \lim_{n \rightarrow \infty } \mathrm{P}(\bigcup_{k=n}^\infty E_k )) \\     & \leq \lim_{n \rightarrow \infty} \sum_{k=n}^\infty \mathrm{P}(E_k) \\     & = 0   \end{aligned}$$(QED)



</details>

### 逆Borel-Cantelli 引理

> $$E_1, E_2, \dots$$為獨立可測集合序列，即$$E_i, E_j, i \neq j$$獨立，若$$\sum_{n=1}^\infty \mathrm{P}(E_n)=\infty$$，則$$\displaystyle \mathrm{P}(\limsup_{n \rightarrow \infty} E_n) = 1$$或$$\displaystyle \mathrm{P}(\liminf_{n \rightarrow \infty} E_n) = 0$$。
>
> <mark style="color:red;">獨立的無窮多個事件機率總和若為無窮大，則此無窮多個事件同時發生的機率為1</mark>。

<details>

<summary>proof</summary>

$$\displaystyle \begin{aligned} \mathrm{P}(\limsup_{n \rightarrow \infty} E_n)      & = \mathrm{P}(\bigcap_{n=1^\infty} \bigcup_{k=n}^\infty E_k) \\     & = \mathrm{P}(\lim_{n \rightarrow \infty } \bigcup_{k=n}^\infty E_k ) \\     & = \lim_{n \rightarrow \infty } \mathrm{P}(\bigcup_{k=n}^\infty E_k )) \\     &  \lim_{n \rightarrow \infty }[1- \mathrm{P}(\bigcap_{k=n}^\infty E_k^c)]    \end{aligned}$$

因為$$E_n$$獨立，所以

$$\displaystyle \begin{aligned}  \mathrm{P}(\bigcap_{k=n}^\infty E_k^c)     & = \prod_{k=n}^\infty \mathrm{P}(E_k^c) \\      & = \prod_{k=n}^\infty (1- \mathrm{P})(E_k))~ [\because 1-x \leq e^{-x}]\\      & \leq \prod_{k=n}^\infty e^{-\mathrm{P}(E_k)} \\     & = \exp(- \sum_{k=n}^\infty \mathrm{P}(E_k)) \\     & = 0 \end{aligned}$$(QED)

</details>

### 應用：Infinite monkey problem

此為The Second Borel-Cantelli Lemma的一個重要思想上的應用，它敘述了一隻猴子的打字次數達到「無窮」以後，必然能夠打出一篇完整的文章。

此定理當中，「必然」是數學上的定義(機率為1)，然而「猴子」卻不是真的猴子，牠也可代換成「打字員」，它主要想說明的論點是不要把非常大但是有限的數視同無限 。

就英文字而言，隨機打出一個與指定文字相同者的機率是(1/26)，隨機打出兩個相同字的機率則是(1/26\*26)=(1/676)=0.148%。光是要打出20個完全與指定文字相同的機率，就已經小於10^(-29)了。

在現實中，要讓一隻猴子用隨機打字的方式打出一篇完整的莎士比亞劇本，機率是微乎其微(趨近於0)，因為現實是一種非常大的有限(而不是嚴格意義上的無限)。現實是在猴子的生命週期中，不太可能打得出一篇完整的文章。

現實生活中非常多件事情雖然還是有可能同時發生，但機率不會是1(也就是不必然)。同理，有可能某些事情非常不可能會發生，但機率不會是0。

The Second Borel-Cantelli告訴我們，眼光放至「無窮」，才能說什麼事情不是「一定會」發生，就是「一定不會」發生。現實生活因為並非無限，任何事情都應該要考慮到「可能性」才是。
