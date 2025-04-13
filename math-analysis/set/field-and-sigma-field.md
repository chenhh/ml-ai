---
description: σ代數
---

# 域與σ域

## 簡介

<mark style="color:red;">定義σ域（代數）的主要用途，是用於定義實值可測函數（實值隨機變數）的前像，必須為σ域內的元素才符合可測函數的定義。因為實值可測函數的值域為實數，因此實數上任一值依函數定義必定有至少一個以上元素的定義域集合(前像)所映射而來。如果有一實數值的前像不為σ域的元素時，則此對映關係不是函數。</mark>並非定義域中的任意集合(power set)均可定義隨機變數。

因為給定任意的集合時，依公理可以建構出不可測的集合族（set family，元素為集合的集合），為了從冪集合中排除這類性質不佳的集合族，因此才定義sigma域，而日常所使用的集合，幾乎都滿足sigma域的條件，所以可放心使用。

## 環(ring)

> 若集合(族)$$F$$​滿足以下三個條件時稱為環(ring)：
>
> 1. $$\phi \in F$$
> 2. $$A_1 \in F$$​且$$A_2 \in F$$​則$$A_1 - A_2 \in F$$
> 3. 若$$A_1 \in F$$​且$$A_2 \in F$$​則$$A_1 \cup A_2 \in F$$

若集合$$F$$​為環且滿足宇集合$$S \in F$$，則稱$$F$$​為代數(algebra)。

可得出若$$A \in F$$，則$$A^c \in F$$​。

### 任意環的交集仍為環

> $$F_1, F_2$$均為環，則$$F_1 \cap F_2$$也為環

<details>

<summary>proof: 由環的定義證明</summary>

顯然$$\phi \in F_1 \cap F_2$$-- (1)

令$$A_1, A_2 \in F_1 \cap F_2$$，由環的定義得$$A_1 - A_2 \in F_1$$且$$A_1 - A_2 \in F_2$$，則$$A_1 - A_2 \in F_1 \cap F_2$$--(2)

同理可得$$A_1 \cup A_2 \in F_1 \cap F_2$$--(3)

由(1,2,3)得交集為環(QED)

</details>

## σ環(σ-ring)

若集合$$F$$​滿足以下三個條件時，稱為σ-環：

1. $$\phi \in F$$
2. 若$$A_1 \in F$$​且$$A_2 \in F$$​則$$A_1 - A_2 \in F$$
3. 若$$\{A_n\}_{n\in \mathbb{N}} \subseteq \mathbb{R}$$，則$$\bigcup_{n\in \mathbb{N}} A_n \in \mathbb{R}$$

### 任意σ環的交集仍為σ環

> $$F_1, F_2$$均為sigma環，則$$F_1 \cap F_2$$為σ環

## 域（field）或代數（algebra）

令$$S$$為宇集合（universal set or space），令集合$$F \subseteq S$$為包含宇集合的某此子集，若滿足以下三個條件時，稱$$F$$為域（代數）：

1. $$F\neq  \emptyset$$，不為空集合。
2. \[<mark style="color:blue;">F在補集操作下為閉集</mark>]若 $$A \in F$$，則其補集合也為$$F$$內的元素，即$$A^c \in F$$。
3. \[<mark style="color:blue;">F在聯集操作下為閉集</mark>]若$$A_1 \in F$$且$$A_2 \in F$$，則$$A_1 \cup A_2 \in F$$。

**條件3可得有限聯集也是F內的元素**，即$$A_1, A_2, \ldots, A_n \in F$$，則$$\cup_{i=1}^n A_i \in F$$。但不保證無限聯集時成立。

。

### 範例

* $$A_1 = \{ 1, 3\}$$,  $$F=\{A_1, A_2\}=\{(1,3), \{2,4,5,6\}\}$$，則$$F$$為域。
* $$F=\{ \emptyset, S\}$$，則$$F$$為域。
* $$F=\{$$包含所有$$S$$的子集合, 即$$S$$的冪集合$$\}$$, 則$$F$$為域。

### <mark style="color:red;">任意域的的交集仍為域</mark>

#### 範例：域的聯集不一定為域

## σ域（σ代數）與可測空間

> $$F$$為σ域若$$F$$為域且滿足$$\cup_{i=1}^\infty A_i \in F$$ ，即<mark style="color:blue;">無限可數的集合也是屬於</mark>$$F$$。
>
> 稱集合對$$(S, F)$$為<mark style="color:red;">可測空間（measurable space）</mark>。
>
> 由定義可知 σ域 <mark style="color:red;">必為域</mark>。

* \[<mark style="color:blue;">F在可數交集下為閉集</mark>]如果$$F$$為σ域，則$$\forall A_i \in F, i \in \mathbb{N}, \ \cap_{i=1}^\infty A_i \in F$$。
* 空集合$$\emptyset$$與宇集合$$S$$也都是$$F$$的元素。
* 若$$A_1, A_2,\dots \in F$$，由定義知$$\displaystyle \limsup_{n \rightarrow \infty} A_n \equiv \bigcap_{n=1}^\infty \bigcap_{k=n}^\infty A_k \in F$$，同理$$\displaystyle \liminf_{n \rightarrow \infty} A_n \equiv \bigcup_{n=1}^\infty \bigcap_{k=n}^\infty A_k \in F$$。

### σ域的原子集合(atomic set)

> 令$$\mathcal{F}$$為σ域，定義集合族中最小的元素集合族為：
>
> $$A(\mathcal{F})=\{S \in \mathcal{F} ~|~ S \neq \emptyset, \text{ and  if } H \in \mathcal{F} \text{ and} H \subseteq S, \text{ then } H = S\}$$為$$\mathcal{F}$$中無法被其它元素可數聯集的集合所組成的集合族。
>
> 由定義得$$A(\mathcal{F}) \subseteq \mathcal{F}$$，且$$\forall \emptyset \neq S \in \mathcal{F}$$，$$S$$可由$$A(\mathcal{F})$$聯集得出。
>
> 當$$| \mathcal{F}| < \infty$$時，$$A(\mathcal{F})$$形成$$\Omega$$的一組有限分割，可得$$\mathcal{F}=\sigma(A(\mathcal{F}))$$。
>
> $$\Omega \notin A(\mathcal{F})$$，假設$$\emptyset \neq H \in \mathcal{F}$$，必可得$$H \subset \Omega$$且$$H \neq \Omega$$。
>
> [https://math.stackexchange.com/questions/3065633/prove-or-disprove-that-every-finite-sigma-algebra-on-omega-is-generated-by](https://math.stackexchange.com/questions/3065633/prove-or-disprove-that-every-finite-sigma-algebra-on-omega-is-generated-by) (有限元素的σ域可由宇集合的有限分割所生成)
>
> [https://stats.stackexchange.com/questions/372534/atoms-of-a-sigma-algebra](https://stats.stackexchange.com/questions/372534/atoms-of-a-sigma-algebra) (宇集合的可數分割可形成σ域，且分割為原子集合)
>
> [https://math.stackexchange.com/questions/1414129/is-every-sigma-algebra-generated-by-a-partition?rq=1](https://math.stackexchange.com/questions/1414129/is-every-sigma-algebra-generated-by-a-partition?rq=1)
>
> 註：可數的σ域必為有限元素，而有無限個元素的σ域必為不可數的。
>
> <mark style="color:red;">存在無限個元素的σ域不是由宇集合的分割生成</mark>，例如閉區間\[0,1]上的Borel集$$\mathcal{B}$$無法由\[0,1]的任意分割生成。(反證法)令$$\{E_i\}_{i \in I}$$為\[0,1]的分割，因為單點集$$\{x\} \in \mathcal{B}$$，因此可得$$E_i, ~\forall i \in I$$都必須為單點集。但是單點集的可數聯集無法生成區間$$[0,1]$$，因為\[0,1]為不可數集合，無法表示為可數集合的聯集。因此Borel集不是由\[0,1]的分割生成。
>
> 註：雖然Borel集不是由分割生成，但是Borel集包含了將\[0,1]切成分割的資訊。

### 範例

<mark style="background-color:orange;">\[trivial σ域]</mark> $$F=\{ \emptyset, S\}$$，則$$F$$為σ域 <mark style="color:red;">(最小的σ域)</mark>。而$$A(\mathcal{F})=\emptyset$$。

<mark style="background-color:orange;">\[power set]</mark> $$F=\{$$包含所有$$S$$的子集合, 即$$S$$的冪集合$$\}\equiv 2^S$$, 則$$F$$為σ域<mark style="color:red;">(最大的σ域)</mark>。而$$A(\mathcal{F})=S$$中每一個元素形成的signleton集合族。

<mark style="background-color:orange;">\[包含集合A的最小σ域]</mark> $$F=\{A, A^C, \emptyset\ , \Omega\}$$為σ域。

$$S=\{1,2,3\}$$，則：

* $$F_1=\{\phi, \{1\}, \{2,3\}, S\}$$為σ域。$$A(\mathcal{F}_1)=\{\{1\}, \{2,3\}\}$$。
* $$F_2=\{\phi, \{1\}, \{2\},\{3\}, S\}$$不是σ域，因為$$\{2,3\} \notin F_2$$。
* $$F_3=\{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{2,3\}, \{1,3\}, \{1,2,3\}\}$$為冪集合是σ域。$$A(\mathcal{F})=\{\{1\}, \{2\}, \{3\}\}$$。

$$S=\mathbb{N}$$則：

* $$F=\{\phi, \{1,3,5,7,\dots\}, \{2,4,6,8,\}, \mathbb{N}\}$$為σ域。
* $$F_2=\{A \subseteq \mathbb{N}, ~ A \text{ is finite or } A^c \text{ is finite} \}$$不是σ域。例如$$A_n=\{n\} \in F_2$$，但$$\bigcup_{n=1}^\infty A_n = \mathbb{N} \notin F_2$$。
* $$F_3=\{A \subseteq \mathbb{N}, ~ A \text{ is countable or } A^c \text{ is countable} \}$$為σ域。
* <mark style="color:red;">同一集合中可生成相異的σ域</mark>。

### <mark style="color:red;">任意σ域的的交集仍為σ域</mark>

#### 範例：σ域的聯集不一定為σ域

### 包含集合族的最小的σ域

> 給定集合族$$G$$，則包含集合$$G$$的最小σ域記為$$\sigma(G)$$。
>
> $$\sigma(G)$$稱為由集合$$G$$生成的最小σ域(sigma-field generated by S)。
>
> 也可定義為所有包含$$G$$的σ域的交集：$$\displaystyle  \bigcap_{F \text{ is } \sigma\text{-field of } G} F$$，因為任意個σ域的交集仍為σ域。

由定義得$$\sigma(G)$$唯一。

#### 範例

$$S=\{1,2,3,4\}$$，$$G=\{\{1,2\},\{4\}\}$$，則$$\sigma(G)=\{\phi, \{1,2,\}  \{3\}, \{4\}, \{1,2,3\}, \{1,2,4\}, \{3,4\}, S \}$$。$$A(\sigma(G))=G$$。

## Borel σ域

> 令宇集合$$S=\mathbb{R}$$為實數集（直線）。定義<mark style="color:red;">Borel</mark> σ<mark style="color:red;">域 (Borel set)</mark> $$\mathcal{B}$$<mark style="color:red;">為直線上的所有開（閉）區間的集合族</mark>，即$$\mathcal{B}=\{ (x,y)| x < y \text{ and } x,y \in \mathbb{R}\}$$。
>
> 可得$$\mathcal{B}=\sigma(\mathbb{R})$$

此處$$\mathcal{B}$$集合定義中的區間可為開區間，閉區間，或是半開區間都可以，因為根據σ域的定義，開區間的補集是閉區間，仍為σ域元素，反之亦然。而半開區間可寫為開區間與閉區間的聯集，依定義也是σ域內的元素。

### 範例

* $$\mathcal{B}=\{(x,y), [x,y], (x,y], [x,y), (-\infty, x], (-\infty, x), [x, \infty), (x, \infty) \}$$為Borel σ域。
* $$\mathcal{B} =\{ (x,y] | x<y \text{ and } x, y \in \mathbb{R} \}$$包含所有實數上的半開區間為Borel σ域。
* $$\mathcal{B} =\{ [x,y] | x<y \text{ and } x, y \in \mathbb{R} \}$$包含所有實數上的閉區間為Borel σ域。

## 濾流(filtration)

> 令 $$\Omega$$為一個樣本空間，$$\mathcal{F}$$為事件 (可測集) 組成的σ域，$$\mathrm{P}: \mathcal{F} \rightarrow [0,1]$$為一個測度且$$\mathrm{P}(\Omega)=1$$ 。把$$(\Omega, \mathcal{F}, \mathrm{P})$$稱為機率空間。
>
> 將滿足以下性質的一族σ域$$\{ \mathcal{F}_t\}$$稱為濾流：
>
> * \[遞增集合]若$$s<t$$，則$$\mathcal{F}_s \subseteq \mathcal{F}_t$$
> * 對於 $$\displaystyle \sigma(\cup_t \mathcal{F}_t)\equiv \mathcal{F}_\infty \subseteq \mathcal{F}$$
>
> 稱$$(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathrm{P})$$為filtrated 機率空間。通常用於隨機過程中。

* Filtration $$\mathcal{F}_t$$為隨機過程中$$X(t,\omega)$$，隨時間擴大的<mark style="color:red;">資訊集合</mark>，而在$$t \rightarrow \infty$$時，才可得到$$\mathcal{F}_\infty \equiv \mathcal{F}$$； 因為隨機過程的一條樣本路徑$$X(\omega)$$，必須要經過所有的時間$$t \in \mathcal{T}$$才可得出；反之在特定時間點$$t$$得到的樣本$$X(t)$$只是部分未走完樣本的實現值，因此只包含部份的資訊。
* 機率的核心在於可測性。**簡單來說，我們是想通過現在能夠觀測到的資訊來對未來可能發生的事件做出預測**。其中$$\mathcal{F}$$是所有能夠觀察到的事件，<mark style="color:blue;">而filtration則體現了隨時間變化的可測性：隨著時間過去，能觀測到的事件越多</mark>。
* 濾流並非單個資訊本身(如同硬碟並不是資訊本身), 而是對$$t$$時間所有可觀察事件資訊的彙集，之後再使用條件期望對未來時刻隨機變數不斷細化加工。正因為此，稱加工為"濾"，細化為"流"。濾流是資訊的載體，不同的濾流編碼了不同資訊。

什麼是$$X_t$$適應$$\mathcal{F}_t$$呢？那就是在同一時刻下，可計算的機率不會超出已知的知識範圍。隨著「能形成看待的事物的知識範圍」不斷增大，這樣就組成了一個濾流。在任意時間$$t$$，$$X_t$$都可以通過觀測$$\mathcal{F}_t$$中包含的事件資訊後成為predetermined/known value，而不再具有隨機性且不會出現無法求$$X_t$$之值的情形。即以$$\mathcal{F}_t$$ 對$$\Omega$$ 的分類方式， $$t$$時刻之前的所有可行軌道必須全部能被逐個區分。

對於隨機過程的一條路徑，從時間0到某個時間$$t$$ ，有一些事件是可以被確定的，有一些則不能，濾流把可以被確定的那些事件選出來。

###



### 參考資料

* [\[知乎\]以測度為基礎的概率基本概念與結論](https://zhuanlan.zhihu.com/p/32334499)
* [https://zhuanlan.zhihu.com/p/345656686](https://zhuanlan.zhihu.com/p/345656686)



