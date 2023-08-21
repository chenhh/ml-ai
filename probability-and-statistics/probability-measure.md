# 機率測度(probability measure)

## 基本名詞

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

### 性質&#x20;

給定機率空間為$$(\Omega, \mathcal{F}, P)$$

> \[<mark style="color:blue;">事件集合機率的上下限</mark>] $$\forall E \in \mathcal{F}, 0 \leq \mathrm{P}(E) \leq 1$$

* $$\mathrm{P}(\Omega) = \mathrm{P}(E \cup E^c) = \mathrm{P}(E) +\mathrm{P}(E^c) = 1$$
* $$\because \mathrm{P}(E) \geq 0$$ 且 $$\mathrm{P}(E^c) \geq 0$$, $$\therefore  0 \leq \mathrm{P}(E) \leq 1$$(QED)

> \[<mark style="color:blue;">補集事件發生的機率</mark>] $$\forall E \in \mathcal{F}, \mathrm{P}(E^c)=1 - \mathrm{P}(E)$$。$$E^c$$為$$E$$的餘事件（complementary event）

* $$\because \mathrm{P}(\Omega)=\mathrm{P}(E \cup E^c)= \mathrm{P}(E) + \mathrm{P}(E^c)=1$$$$\therefore \mathrm{P}(E^c) = 1 - \mathrm{P}(E)$$ (QED)

> $$\mathrm{P}(\emptyset)=0$$。$$\emptyset$$為<mark style="color:red;">零事件（null event</mark>），又稱空事件，指該事件永不發生。

* $$\because \Omega \cup \emptyset = \Omega$$且$$\mathrm{P}(\Omega ) = \mathrm{P}(\Omega \cup \emptyset) =  \mathrm{P}(\Omega) + \mathrm{P}(\emptyset)=1 + \mathrm{P}(\emptyset) =1$$。

> $$\mathrm{P}(F \cap E^c)=\mathrm{P}(F) - \mathrm{P}(E \cap F)$$

* $$\mathrm{P}(F) = \mathrm{P}((F \cap E^c) \cup (E \cap F)) = \mathrm{P}((F \cap E^c) + \mathrm{P}(E \cap F)$$ (QED)

> $$\mathrm{P}(E \cup F) = \mathrm{P}(E) + \mathrm{P}(F) - \mathrm{P}(E \cap F)$$

* $$\begin{aligned} \mathrm{P}(E \cup F) &= \mathrm{P}((E \cap F^c) \cup (E \cap F) \cup (E^c \cap F)) \\ &= \mathrm{P}(E) - \mathrm{P}(E \cap F) + \mathrm{P}(E \cap F) + \mathrm{P}(F) - \mathrm{P}(E \cap F) \\& = \mathrm{P}(E) + \mathrm{P}(F) - \mathrm{P}(E \cap F)  \end{aligned}$$(QED)

> If $$E \subseteq F$$ then $$\mathrm{P}(F \setminus E) = \mathrm{P}(F) - \mathrm{P}(E)$$ and $$\mathrm{P}(E) \leq \mathrm{P}(F)$$

* $$\because \mathrm{P}(F) = \mathrm{P}(E \cup (F \setminus E)) = \mathrm{P}(E) + \mathrm{P}(F \setminus E)$$且 $$\mathrm{P}(F \setminus E) \geq 0$$, $$\therefore \mathrm{P}(F) \geq \mathrm{P}(E)$$

> \[Bonferroni inequality] $$\mathrm{P}(E \cap F) \geq \mathrm{P}(E) + \mathrm{P}(F) -1$$
>
> * $$\mathrm{P}( (E \cap F)^c) = \mathrm{P}(\Omega \setminus (E \cap F)) = 1- \mathrm{P}(E \cap F)$$--(1)
> * $$\mathrm{P}((E \cap F)^c)=\mathrm{P}(E^c \cup F^c) \leq \mathrm{P}(E^c)+\mathrm{P}(F^c)$$且$$\mathrm{P}(E^c)= 1-\mathrm{P}(E), \mathrm{P}(F^c)=1-\mathrm{P}(F)$$--(2)
> * (1)(2)得 $$1-\mathrm{P}(E \cap F) \leq  2 - \mathrm{P}(E) - \mathrm{P}(F)$$移項得 $$\mathrm{P}(E \cap F) \geq \mathrm{P}(E) + \mathrm{P}(F) -1$$(QED)

> 令事件$$E_1, E_2, \ldots$$為$$\Omega$$的分割(partition)，即$$E_i \cap E_j = \emptyset,\ \forall i \neq j$$且 $$\cup_{i \in \mathbb{N}} E_i = \Omega$$，則$$\mathrm{P}(F) = \sum_{i \in \mathbb{N}} \mathrm{P}(F \cap E_i), \forall F \in \mathcal{F}$$。

### 多事件聯集的機率

* $$\begin{aligned} \mathrm{P}(E_1 \cup E_2 \cup E_3) & =  \mathrm{P}(E_1)+\mathrm{P}(E_2)+\mathrm{P}(E_3) \\& - \mathrm{P}(E_1 \cap E_2) - \mathrm{P}(E_1 \cap E_3) - \mathrm{P}(E_2 \cap E_3) \\ & + \mathrm{P}(E_1 \cap E_2 \cap E_3) \end{aligned}$$
* $$\begin{aligned} \mathrm{P}(\cup_{i=1}^n E_i) & = \sum_{i=1}^n \mathrm{P}(E_i) \\& - \sum_{i \leq i < j \leq n} \mathrm{P}(E_i \cap E_j) \\ &+ \sum_{1 \leq i < j < k \leq n} \mathrm{P}(E_i \cap E_j \cap E_k) +\ldots \\ &+(-1)^{n+1} \mathrm{P}(E_1 \cap E_2 \cap \ldots \cap E_n) \end{aligned}$$



### 條件機率（conditional probability）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，給定$$F$$發生後的條件下，$$E$$發生的條件機率為$$\mathrm{P}(E|F) = \frac{\mathrm{P}(E \cap F)}{\mathrm{P}(F)},\ \mathrm{P}(F) \neq 0$$。

### 全機率定理（total probability theorem）

$$E, F_1, F_2,\ldots, F_N$$為定義於樣本空間$$\Omega$$的事件（集合），且$$F_1, F_2,\ldots, F_N$$兩兩互斥則$$\displaystyle \mathrm{P}(E) = \sum_{i=1}^N \mathrm{P}(A|F_i) \mathrm{P}(F_i), \ \mathrm{P}(F_i) \neq 0 \ \forall i$$

### 機率獨立（statistically independent）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，若且惟若$$\mathrm{P}(E \cap F) = \mathrm{P}(E)\mathrm{P}(F)$$，則稱$$E,F$$為二<mark style="color:red;">獨立事件</mark>。

* 註：$$\mathrm{P}(E\cap F) =  \mathrm{P}(E|F)\mathrm{P}(F)$$。如果兩事件獨立時，則$$\mathrm{P}(E\cap F)=\mathrm{P}(E)\mathrm{P}(F)$$，因此可知兩事件獨立時，$$\mathrm{P}(E) = \mathrm{P}(E|F)$$，以資訊理論解釋就是事件$$F$$不包含關於事件$$E$$的資訊，因此兩事件獨立。

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
