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

> 令集合$$E \subset \mathbb{R}^n$$​，若$$\{I_k\} \subset \mathbb{R}^n$$為可數（countable)開矩體（開集合），且有$$\displaystyle E \subseteq \bigcup_{k\geq 1} I_k$$，則稱$$\{I_k\}$$​為集合$$E$$​的一組L-覆蓋。

由定義知$$E$$​的L-覆蓋不唯一，可以有任意組，且每一組L-覆蓋可得$$\sum_{k \geq 1} |I_k|$$，其中$$|I_k|$$​為其體積，可以是$$+\infty$$​。

## Lebesgue外測度(Lebesgue outer measure)

> 定義$$\displaystyle m^{*}(E)=\inf \{ \sum_{k \geq 1}|I_k| ~\big|~ \{I_k\} \text{ is L-covering of set } E  \}$$
>
> 為集合$$E$$​的外測度。

若集合$$E$$​的任意個L-覆蓋$$\{I_k\}$$​均滿足$$\sum_{k \geq 1}|I_k|＝\infty$$，則$$m^{*}(E)=\infty$$，否則$$m^{*}(E)<\infty$$。

#### 歐式空間中單點集合的外測度為0

$$\forall x_0 \in \mathbb{R}^n, m^{*}(\{x\})=0$$

取開集合$$I$$​且$$x_0 \in I$$​，因為$$|I|$$​任意小時(=0)仍可包含$$x_0$$​，因此外測度為０。

#### 歐式空間中的閉矩體外測度等於其體積

$$I \subset \mathbb{R}^n$$​為開矩陣，$$\overline{I}$$​為閉矩體，則$$m^{*}(\overline{I})=|I|$$

$$\forall \epsilon >0$$​，取一開矩陣$$J \ni \overline{I} \subset J$$且$$|J| < |I|+\epsilon$$​

因此可得$$\forall \epsilon >0 ~ m^{*}(|\overline{I}|) \leq |J|< |I| + \epsilon$$--(1)

設$$\{I_k\}$$​為$$\overline{I}$$​的一組L-覆蓋。因為$$\overline{I}$$​為有界閉集，根據[Heine-Borel定理](../real-number/covering.md#heineborel-fu-gai-ding-li)，可知存在$$\{I_k\}$$​的有限子覆蓋使得$$\{I_{i1}, I_{i2},\dots, I_{il}\} \ni \overline{I} \subset \bigcup_{j=1}^l I_{ij}$$

而$$|I| \leq \sum_{j=1}^l |I_{ij}| \leq \sum_{k=1}^\infty |I_k|$$

因此$$|I| \leq m^{*}(|\overline{I}|)$$--(2)

由(1)(2)得$$m^{*}(\overline{I})=|I|$$ (QED)
