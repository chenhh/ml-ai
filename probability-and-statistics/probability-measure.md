# 機率測度\(probability measure\)

## 基本名詞

* **結果\(outcome\)**$$\omega$$為**樣本空間**$$\Omega$$的一個元素，稱為一個點或樣本（point or sample point）。
* 而樣本空間的任一子集稱為**事件\(event\)**，$$E \subseteq \Omega$$，因此事件中包含了許多的結果。
* sigma-field $$\mathcal{F}$$為滿足特定條件的事件集合的集合。
* **隨機變數**$$X: \mathcal{F} \rightarrow \mathbb{R}$$為函數，將sigma-field中的元素\(事件\)，映射到實數值。因此給定實數值$$a$$，可得前像為事件集合的集合，可得$$X^{-1}(a) \in \mathcal{F}$$。
* 機率測度$$P$$量測的是滿足某個實數值$$a$$的前像\(事件集合的集合, $$X^{-1}(a)$$\)發生的機率。

## 機率測度

> 對於樣本空間$$\Omega$$每一個\(子集合\)事件$$E$$而言，實數$$P(E)$$若滿足以下三個條件時，稱$$P(E)$$為事件$$E$$的機率（測度）。
>
> 1. $$ P(E) \geq 0$$
> 2. $$P(\Omega) = 1$$
> 3. $$P(\cup_{i \in \mathbb{N}} E_i )= \sum_{i \in \mathbb{N}} E_i$$,$$E_i \cap E_j = \emptyset, \ \forall i \neq j$$為兩兩互斥的事件集合
>
> 註：機率只有定義事件的條件，可為任意的分佈。

### 性質 

給定機率空間為$$(\Omega, \mathcal{F}, P)$$

* $$\forall E \in \mathcal{F}, 0 \leq P(E) \leq 1$$
* $$\forall E \in \mathcal{F}, P(E^c)=1 - P(E)$$。$$E^c$$為$$E$$的餘事件（complementary event）
* $$P(\emptyset)=0$$。$$\emptyset$$為零事件（null event），又稱空事件，指該事件永不發生。
* $$P(F \cap E^c)=P(F) - P(E \cap F)$$
* $$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$
* If $$E \subseteq F$$ then $$P(F \setminus E) = P(F) - P(E)$$ and $$P(E) \leq P(F)$$
* \[Bonferroni inequality\] $$P(E \cap F) \geq P(E) + P(F) -1$$
* 令事件$$E_1, E_2, \ldots$$為$$\Omega$$的分割\(partition\)，即$$E_i \cap E_j = \emptyset,\ \forall i \neq j$$且 $$\cup_{i \in \mathbb{N}} E_i = \Omega$$，則$$P(F) = \sum_{i \in \mathbb{N}} P(F \cap E_i), \forall F \in \mathcal{F}$$。
* \[Boole inequality\] $$P(\cup_{ i \in \mathbb{N}} E_i) \leq  \sum_{i \in \mathbb{N}} P(E_i)$$

### 多事件聯集的機率

* $$P(E_1 \cup E_2 \cup E_3) =  P(E_1)+P(E_2)+P(E_3) - P(E_1 \cap E_2) - P(E_1 \ cap E_3) - P(E_2 \cap E_3) + P(E_1 \cap E_2 \cap E_3)$$
* $$P(\cup_{i=1}^n E_i) = \sum_{i=1}^n P(E_i) - \sum_{i \leq i < j \leq n} P(A_i \cap A_j)+ \sum_{1 \leq i < j < k \leq n} P(A_i \cap A_j \cap A_k) +\ldots +(-1)^{n+1} P(A_1 \cap A_2 \cap \ldots \cap A_n)$$



### 條件機率（conditional probability）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，給定$$F$$發生後的條件下，$$E$$發生的條件機率為$$P(E|F) = \frac{P(E \cap F)}{P(F)},\ P(F) \neq 0$$。

### 全機率定理（total probability theorem）

$$E, F_1, F_2,\ldots, F_N$$為定義於樣本空間$$\Omega$$的事件（集合），且$$F_1, F_2,\ldots, F_N$$兩兩互斥則$$P(E) = \sum_{i=1}^N P(A|F_i) P(F_i), \ P(F_i) \neq 0 \ \forall i$$

### 機率獨立（independent）

$$E,F$$為樣本空間$$\Omega$$下的二個事件，若且惟若$$P(E \cap F) = P(E)P(F)$$，則稱$$E,F$$為二獨立事件。

* 註：$$P(E\cap F) =  P(E|F)P(F)$$。如果兩事件獨立時，則$$P(E\cap F)=P(E)P(F)$$，因此可知兩事件獨立時，$$P(E) = P(E|F)$$，以資訊理論解釋就是事件$$F$$不包含關於事件$$E$$的資訊，因此兩事件獨立。

$$E_1, E_2, E_3$$為樣本空間$$\Omega$$的三個事件，若且惟若滿足以下條件時，$$E_1, E_2, E_3$$為獨立事件：

* $$P(E_1 \cap E_2)=P(E_1)P(E_2)$$
* $$P(E_1 \cap E_3)=P(E_1)P(E_3)$$
* $$P(E_2 \cap E_3)=P(E_2)P(E_3)$$
* $$P(E_1 \cap E_2 \cap E_3)=P(E_1)P(E_2)P(E_3)$$
* 共$$\begin{pmatrix} 3 \\2 \end{pmatrix} + \begin{pmatrix} 3 \\3 \end{pmatrix} = 3 + 1=4$$個條件。

如果有$$E_1, E_2, \ldots, E_N$$個定義於樣本空間$$\Omega$$的$$N$$個事件，則需要$$\begin{pmatrix} N \\ 2 \end{pmatrix} + \begin{pmatrix} N \\ 3 \end{pmatrix} + \ldots + \begin{pmatrix} N \\ N \end{pmatrix} = 2^N - 1 -N$$個條件。

### 貝式定理（Baye's theorem）

若$$E, F_1, F_2, \ldots, F_N$$為定義於樣本空間$$\Omega$$的事件且$$F_i \cap F_j = \emptyset, \ \forall i \neq j$$為互斥事件，則$$P(F_i|E) = \frac{P(F_i \cap E)}{P(E)} = \frac{P(E|F_i)P(F_i)}{\sum_{i=1}^N P(E|F_i)P(F_i)}$$



