# Lebesgue外測度

## 簡介

測度的定義中，只有要求測度的性質，但沒有建構測度的方法。

考慮$$\mathbb{R}^n$$​的測度，集合的面積可以從內部小集合往外擴張，或是從外部開集合(覆蓋)夾擠的方式求出(一般書使用外部夾擠)，只要找出所有能夠覆蓋此集合的所有外部集合面積的下確界，即為此集合的面積。

但是在建構外測度時，必須要排除有些集合是不可測集合，<mark style="color:red;">而排除掉這些不可測集合，只在可測集合上定義的外測度即為測度</mark>。

## Lebesgue測度

> 函數$$m: B \rightarrow \mathbb{R}$$，$$B\subseteq \mathbb{R}$$為所有實數上開集合與閉集合形成的sigma域。
>
> 若函數$$m$$滿足以下三個性質時，稱為Lebesgue測度：
>
> 1. \[區間的測度為其長度] $$I \neq \empty$$且$$I \subseteq \mathbb{R}$$為Lebesgue可測集，則$$m(I)=\text{length of } I$$。
> 2. \[平移不變性]$$E$$為Lebesgue可測集，$$y\in \mathbb{R}$$為任意實數，定義集合$$E+y=\{x+y~|~ x\in E\}$$，則$$m(E+y)=m(E)$$。
> 3. \[可數可加性] $$\{E_n\}_{n=1}^\infty$$，$$E_i \cap E_j =\empty, ~\forall i \neq j$$為Lebesgue可測集合序列，則$$\displaystyle m(\bigcup_{n=1}^\infty E_n)=\sum_{n=1}^\infty m(E_n)$$。

實數上並非所有任意集合均可定義滿足以上三個條件的函數$$m$$，必須是可測集合才可建構出滿足以上三個條件的函數$$m$$。

<mark style="color:red;">不可測的集合必須使用選擇性公理才能建構出</mark>，一般應用中所遇到的集合均為可測集合，可放心使用。

## L覆蓋(L-covering)

> 令集合$$E \subset \mathbb{R}^n$$​，若$$\{I_k\} \subset \mathbb{R}^n$$為可數（countable)開矩體（開集合），且$$I_k \neq \empty$$，且有$$\displaystyle E \subseteq \bigcup_{k = 1}^\infty I_k$$，則稱$$\{I_k\}$$​為集合$$E$$​的一組L-覆蓋。

由定義知$$E$$​的L-覆蓋不唯一，可以有任意組，且每一組L-覆蓋可得$$\sum_{k \geq 1} |I_k|$$，其中$$|I_k|$$​為其長度(體積)，可以是$$+\infty$$​。

## Lebesgue外測度(Lebesgue outer measure)

> 定義$$\displaystyle m^{*}(E)=\inf \{ \sum_{k \geq 1}|I_k| ~\big|~ E\subseteq \bigcup_{k=1}^\infty I_k, ~\{I_k\} \text{ i.e. is L-covering of set } E  \}$$
>
> 為集合$$E$$​的外測度。
>
> $$m^{*}$$在$$\mathbb{R}$$為長度，在$$\mathbb{R}^n, n \geq 2$$為體積，因為性質均相同，<mark style="color:blue;">為了便於證明與說明，一般使用實數中的長度定義</mark>。

* 若集合$$E$$​的任意個L-覆蓋$$\{I_k\}$$​均滿足$$\displaystyle \sum_{k \geq 1}|I_k|＝\infty$$，則$$m^{*}(E)=\infty$$，否則$$m^{*}(E)<\infty$$為有限測度。
* 由定義知$$m^{*}(\empty)=0$$，因為$$\empty$$為任意集合的子集合，而包含$$\empty$$的最小集合為$$\empty$$。

### 外測度的性質

1. \[非負性] $$m^{*}(E) \geq 0, ~ m^{*}(\empty)=0$$
2. \[單調性] $$A \subseteq B \Rightarrow m^{*}(A) \leq m^{*}(B)$$
3. \[次可加性] $$m^{*}(\bigcup_{k=1}^\infty E_k) \leq \sum_{k=1}^\infty m^{*}(E_k)$$

## 外測度的單調性

> 若$$A \subseteq B$$，則$$m^{*}(A) \leq m^{*}(B)$$。

因為$$B \subseteq \bigcup_{k=1}^\infty I_k$$可得$$A \subseteq \bigcup_{k=1}^\infty I_k$$

## 可數集合的外測度為0

> 取開集合$$I$$​且$$x_0 \in I$$​，因為$$|I|$$​任意小時(=0)仍可包含$$x_0$$​，因此外測度為0。

proof:&#x20;

令$$C=\{c_k\}_{k=1}^\infty$$為可數集合。

令$$\epsilon >0$$，$$\forall k \in \mathbb{N}$$，定義$$I_k=(c_k - \frac{\epsilon}{2^{k+1}},  c_k + \frac{\epsilon}{2^{k+1}})$$，因此$$C \subseteq \bigcup_{k=1}^\infty I_k$$。

而$$0 \leq m^{*} \sum_{k=1}^\infty |I_k| = \sum_{k=1}^\infty \frac{\epsilon}{2^k} = \epsilon$$

因為$$\forall \epsilon >0$$，上述不等式均成立，所以$$m^{*}(E)=0$$。 (QED)

### 範例：有理數集合的外測度為0

因為有理數集合$$\mathbb{Q}$$為可數集合，因此$$m^{*}(\mathbb{Q})=0$$。

### 範例：外測度為0的集合不一定是可數集

如在閉區間$$[0,1]$$的Cantor集合$$C$$的外測度為0，但$$C$$不是可數集合。

因為$$C=\bigcap_{n=1}^\infty F_n$$，其中$$F_n$$是$$2^n$$個長度為$$3^{-n}$$的閉區間之聯合，因此可得：$$m^{*}(C) \leq m^{*} (F_n) \leq 2^n \cdot 3^{-n}$$

所以$$m^{*}(C)=0$$，但Cantor集C不是可數集。

## 區間的外測度等於其長度

> $$I \subset \mathbb{R}$$​為開區間，$$\overline{I}$$​為閉包(閉集合)，則$$m^{*}(\overline{I})=|I|$$

proof:

$$\forall \epsilon >0$$​，取一開區間$$J \ni \overline{I} \subset J$$且$$|J| < |I|+\epsilon$$​

因此可得$$\forall \epsilon >0 ~ m^{*}(|\overline{I}|) \leq |J|< |I| + \epsilon$$--(1)

設$$\{I_k\}$$​為$$\overline{I}$$​的一組L-覆蓋。因為$$\overline{I}$$​為有界閉集，根據[Heine-Borel定理](../real-number/covering.md#heineborel-fu-gai-ding-li)，可知存在$$\{I_k\}$$​的有限子覆蓋使得$$\{I_{i1}, I_{i2},\dots, I_{il}\} \ni \overline{I} \subset \bigcup_{j=1}^l I_{ij}$$

而$$|I| \leq \sum_{j=1}^l |I_{ij}| \leq \sum_{k=1}^\infty |I_k|$$

因此$$|I| \leq m^{*}(|\overline{I}|)$$--(2)

由(1)(2)得$$m^{*}(\overline{I})=|I|$$ (QED)

## 外測度的平移不變性

> 對於任意的集合$$E\subseteq \mathbb{R}$$與實數$$y$$，可得$$m^{*}(E+y)=m^{*}(E)$$

proof:

令$$\{I_k\}_{k=1}^\infty$$為可數開集合序列且$$E \subseteq \bigcup_{k=1}^\infty I_k$$。

則$$\{I_k+y\}_{k=1}^\infty$$也為開集合序列且$$E+y \subseteq \bigcup_{k=1}^\infty (I_k+y)$$

若$$I_k$$為(有限或無限)開區間時，其長度與$$(I_k+y)$$一樣長，因此$$\displaystyle \sum_{k=1}^\infty |I_k| = \sum_{k=1}^\infty |I_k+y|$$--(1)

(1)取inf後，由定義可得$$m^{*}(E+y)=m^{*}(E)$$(QED)

## 外測度的可數次可加性

> 給定可數集合序列$$\{E_k\}_{k=1}^\infty$$(不必為互斥集合)，則：$$\displaystyle m^{*} (\bigcup_{k=1}^\infty E_k) \leq \sum_{k=1}^\infty m^{*}(E_k)$$。

proof:

如果集合序列中任一集合的外測度為無窮大時($$\exists k \in \mathbb{N} \ni m^{*}(E_k)=\infty$$)，則不等式必成立。

考慮所有集合的外測度均為有限值時$$\forall k \in \mathbb{N}, ~ m^{*}(E_k) < \infty$$。

令$$\epsilon > 0$$，$$\forall k \in \mathbb{N}$$，令可數有界開集合序列$$\{I_{k,i}\}_{i=1}^\infty$$為$$E_k$$的L-覆蓋，滿足 $$E_k \subseteq \bigcup_{i=1}^\infty I_{k,i}$$且 $$\sum_{i=1}^\infty |I_{k,i}| < m^{*}(E_k) + \epsilon/2^k$$。

因此可得$$\displaystyle \bigcup_{k=1}^\infty E_k \subseteq \bigcup_{k=1,i=1}^\infty I_{k,i}$$，且$$\displaystyle \sum_{k=1, i=1}^\infty |I_{k,i}| < \sum_{k=1}^\infty m^{*}(E_k) + \epsilon$$。

所以$$\{I_{k,l}, k.l=1,2,\dots\}$$為$$\bigcup_{k=1}^\infty E_k$$的L-覆蓋，可得：

$$\displaystyle  \begin{aligned} m^{*}(\bigcup_{k=1}^{\infty} E_k) & \leq \sum_{k,l=1}^\infty |I_{k,l}| \\ & = \sum_{k=1}^{\infty} \sum_{l=1}^{\infty} |I_{k,l}|  \\ & < \sum_{k=1}^{\infty} m^{*}(E_k) + \epsilon/2 \\ & = \sum_{k=1}^{\infty}m^{*}(E_k) + \epsilon  \end{aligned}$$--(1)

$$\forall \epsilon >0$$時，(1)均成立，因此得可數次可加性(QED)。

## 距離外測度性質

> 給整集定
