# field與sigma-field

## 簡介

定域sigma域（代數）的主要用途，是在定義實值可測函數（實值隨機變數）的前像，必須為sigma域內的元素才符合定義，而不是定義域中的任意集合均可定義。因為可測函數（隨機變數）的定義域，依公理可以建構出不可測的集合族（set family，元素為集合的集合），為了排除這類性質不佳的集合族，因此才定義sigma域，而日常所使用的集合，幾乎都滿足sigma域的條件，所以可放心使用。

## 域（field）或代數（algebra）

令$$G$$為宇集合（universal set or space），令集合$$F \subseteq G$$為包含宇集合的某此子集，若滿足以下三個條件時，稱$$F$$為域（代數）：

1. $$F\neq  \emptyset$$，不為空集合。
2. \[F is closed under complementation\] 若 $$A \in F$$，則其補集合也為$$F$$內的元素，即$$A^c \in F$$。
3. \[F is closed under union\]若$$A_1 \in F$$且$$A_2 \in F$$，則$$A_1 \cup A_2 \in F$$。

**條件3可得有限聯集也是F內的元素**，即$$A_1, A_2, \ldots, A_n \in F$$，則$$ \cup_{i=1}^n A_i \in F$$。但不保證無限聯集時成立。

### 範例

* $$A_1 = \{ 1, 3\}$$, $$A_2 = \{ 2,4,5,6\}$$. $$F=\{A_1, A_2\}=\{(1,3), \{2,4,5,6\}\}$$，則$$F$$為field。
* $$F=\{ \emptyset, G\}$$，則$$F$$為field。
* $$F=\{$$包含所有$$G$$的子集合, 即$$G$$的冪集合$$\}$$, 則$$F$$為field。

## sigma-field（sigma-algebra）與可測空間

> $$F$$為sigma-field若$$F$$為field且滿足 $$A_i \in F, i \in \mathbb{N} \Rightarrow \cup_{i=1}^\infty A_i \in F$$，即無限可數的集合也是屬於$$F$$。
>
> 稱集合對$$(G, F)$$為可測空間（measurable space）。
>
> 由定義可知 sigma-field 必為 field。

* \[closed under countable intersection \]如果$$F$$為sigma-field，則$$\forall A_i \in F, i \in \mathbb{N}, \ \cap_{i=1}^\infty A_i \in F$$。
* 空集合$$\emptyset$$與宇集合$$G$$也都是$$F$$的元素。

### 範例

* $$F=\{ \emptyset, G\}$$，則$$F$$為sigma-field。
* $$F=\{$$包含所有$$G$$的子集合, 即$$G$$的冪集合$$\}$$, 則$$F$$為sigma-field。
* $$F=\{A, A^C, G, \emptyset\}$$為sigma-field。

## Borel sigma-field

> 令宇集合$$G=\mathbb{R}$$為實數集（直線）。定義Borel sigma-field \(Borel set\) $$\mathcal{B} $$為直線上的所有開（閉）區間，即$$\mathcal{B}=\{ (x,y)| x < y \text{ and } x,y \in \mathbb{R}\}$$。

此處$$\mathcal{B}$$集合定義中的區間可為開區間，閉區間，或是半開區間都可以，因為根據sigma-field的定義，開區間的補集是閉區間，仍為sigma-field的元素，反之亦然。而半開區間可寫為開區間與閉區間的聯集，依定義也是sigma-field內的元素。

### 範例

* $$\mathcal{B}=\{(x,y), [x,y], (x,y], [x,y), (-\infty, x], (-\infty, x), [x, \infty), (x, \infty) \}$$為Borel sigma-field。
* $$\mathcal{B} =\{ (x,y] | x<y \text{ and } x, y \in \mathbb{R} \}$$包含所有實數上的半開區間為Borel sigma-field。
* $$\mathcal{B} =\{ [x,y] | x<y \text{ and } x, y \in \mathbb{R} \}$$包含所有實數上的閉區間為Borel sigma-field。

## filtration

> 令 $$\Omega$$為一個樣本空間，$$\mathcal{F}$$為事件 \(可測集\) 組成的 sigma-代數，$$\mathrm{P}: \mathcal{F} \rightarrow [0,1]$$為一個測度且$$\mathrm{P}(\Omega)=1$$ 。把$$(\Omega, \mathcal{F}, \mathrm{P})$$稱為機率空間。
>
> 將滿足以下性質的一族sigma-代數$$\{ \mathcal{F}_t\}$$稱為filitration：
>
> * 若$$s<t$$，則$$\mathcal{F}_s \subseteq \mathcal{F}_t$$
> * 對於 $$\displaystyle \sigma(\cup_t \mathcal{F}_t)\equiv \mathcal{F}_\infty \subseteq \mathcal{F}$$
>
> 稱$$(\Omega, \mathcal{F}, \{\mathcal{F}\}, \mathrm{P})$$為filtrated 機率空間。

* Filtration $$\mathcal{F}_t$$為隨機過程中，隨時間擴大的資訊集合；
* 機率的核心在於可測性。**簡單來說，我們是想通過現在能夠觀測到的資訊來對未來可能發生的事件做出預測**。其中$$\mathcal{F}$$是所有能夠觀察到的事件，而filtration則體現了隨時間變化的可測性：隨著時間過去，能觀測到的事件越多。



### 參考資料

* [\[知乎\]以測度為基礎的概率基本概念與結論](https://zhuanlan.zhihu.com/p/32334499)





