# 集合

## 集合的元素

<mark style="color:red;">**一個集合(set)就是一些具有相同性質的事物收集起來的結果**</mark>。

集合只討論元素間的關係，如果加上其它的函數，則會形成特定的空間。如考慮距離函數(distance function)則變成度量空間(metric space)。如果考慮角度和額外的性質，則會變成內積空間(inner product space)。如果考慮測量集合內的元素時，會變成測度空間(measure space)。

符合某一條件的數的全體稱為集合(set)，記為$$S$$。

符合此條件的每個數$$a$$均屬於此集合，記為$$a \in S$$。

不符合此條件的每個數$$b$$均不屬於此集合，記為$$b \not \in S$$或$$b \in S^c$$。

任一數$$a$$必定是屬於集合$$S$$或是不屬於集合$$S$$，只能有一成立(true or false，為一命題)。

兩集合$$S,Q$$相等，即$$S = Q \Leftrightarrow S \subseteq Q \land Q \subseteq S$$。

* <mark style="color:blue;">集合中的元素無順序性</mark>，$$\therefore \{ 1, 2, 3,4, 5\} = \{ 2, 1, 4, 5, 3\}$$
* <mark style="color:blue;">集合中的重複元素只算一個(有重複元素的集合稱multiset)</mark>，$$\therefore \{ 1,2, 1, 2, 3, 4,5\} = \{ 1,2,3,4,5\}$$

## 空集合(empty set)

> 空集合$$\emptyset \equiv \{ \}$$不含任何元素，因此 $$\forall x \in U, ~ \ x \notin \emptyset$$。

<mark style="color:red;">空集合唯一</mark>，即若有兩個空集合$$\emptyset, \emptyset^{'} \Rightarrow \emptyset= \emptyset^{'}$$。

<mark style="color:red;">非空集合的集合必含有至少一個元素</mark>，即$$S \neq \empty \Rightarrow ~\exists x \ni x \in S$$。

<mark style="color:red;">空集合為任意集合(包含空集合)的子集合(但不一定是元素)</mark>，即$$\empty \subseteq S$$。

<mark style="color:red;">非空集合必存在至少一個元素(選擇性公理的條件)</mark>。$$S \neq \empty \Rightarrow \exists x \in S$$。

<mark style="color:red;">空集合的基數為零</mark>，$$| \emptyset | = 0$$。

空集合的冪集$$\mathcal{P}(\empty)=\{\empty\}$$。

* $$\empty \cup S = S$$
* $$\empty \cap S = \empty$$
* \[兩集合不相交(disjoint)]$$S \cap Q= \empty$$

### 空集合的最大下界與小上界

> * $$\sup\empty=-\infty$$
> * $$\inf \empty=\infty$$

對於任意實數$$r$$，因為空集合中不存在任何元素大於或小於$$r$$，因此可將$$r$$視為$$\empty$$的下界或下界，又因為此性質對於所有的實數均成立，因此定義空集的上下界如上。

\[陶哲軒] 想像直線的最右端為$$+\infty$$，而在最左端為$$-\infty$$。 若一活塞從$$+\infty$$處向左移動直到遇到集合$$S$$為止，則活塞停下來的地方就是$$S$$的上確界。 同理活塞從$$-\infty$$處向右移動直到遇到集合$$S$$為止，活塞停下來的地方就是$$S$$的下確界。

當集合$$S=\emptyset$$時，活塞從$$+\infty$$移動到$$-\infty$$都沒停下來，因此空集合的上確界為$$-\infty$$； 同理當活塞從$$-\infty$$移動到$$+\infty$$都沒停下來，因此空集合的下確界為$$+\infty$$；

## 單元素集與雙元素集(singleton sets and pair sets)

> * 若$$x$$為一物件，則$$v\{x\}$$包含單一元素的集合。 即 $$\forall y, y \in \{x\} \Leftrightarrow y= x$$，稱$$\{x\}$$為包含元素$$x$$的singleton set。
> * 若$$x,y$$為物件，則$$\{x,y\}$$為包含兩元素的集合。即$$\forall z, z \in \{x,y\} \Leftrightarrow z = x \lor z =y$$。稱$$\{x,y \}$$為包含$$x,y$$的pair set。

由集合相等的定義知$$\{x,y\} = \{y,x\}$$，且$$\{x, x\} = \{x\}$$。

空集合的singleton set 為$$\{ \emptyset\}$$,，因此$$\emptyset \in \{\emptyset\}$$ 。可得 $$\{ \emptyset, \{ \emptyset\} \}$$也是集合。

## 集合族(collection of sets, family of set)

> 集合中的元素為集合時稱為集合族。

常見的集合族，令$$S=\{a,b\}$$：

1. 冪集合$$\mathcal{P}(S) = \{\phi, \{a\}, \{b\}, \{a,b\}\}$$
2. 可測集sigma代數 $$\sigma_S=\{\emptyset, \{a\}, \{b\}, \{a,b\}, S\}$$

## 卡式積(Cartesian product)

卡式積 $$X \times Y=\{ (x,y) \ \vert \ \forall x \in X, \forall y \in Y\}$$

若 $$|X| =M < \infty, |Y|=N < \infty \Rightarrow |X \times Y| =MN$$

集合$$X$$或$$Y$$的元素可為無窮多個，如$$X=\mathbb{R}，Y=\mathbb{R} \Rightarrow X \times Y = \mathbb{R}^2$$或$$\mathbb{C}$$

## 聯集與交集運算(intersection and union)

令$$X,Y$$為相異的兩個集合，$$I$$為一指標集合(index set)(有限或無窮多個元素，可數或不可數集合)，$$U$$為包含$$X,Y$$的宇集合。

### 聯集(union)

屬於任一個集合的元素或至少一集合存在該元素。 $$X \cup Y= \{z\ \vert \ z \in X \lor z \in Y\}$$

* $$X\cup X = X \cup \emptyset = \emptyset \cup X = X$$
* $$X \cup U = U$$

### 多集合的聯集: 元素只須存在於某些集合

$$\displaystyle \bigcup_{i\in I} S_i =\{ x \ \vert \ \exists j\in I, x \in S_j\}$$

### 交集(intersection)

同時屬於所有集合的元素，或者為所有集合都存在的素。$$X \cap Y= \{z \vert z \in X \land z \in Y\}$$

* $$X \cap \emptyset = \emptyset$$
* $$X\cap X = X \cap U= X$$

### 多集合的交集: 元素必須存在於所有的集合

$$\displaystyle \bigcap_{i \in I} S_i = \{ x \ \vert \ \forall j \in I, x \in S_j\}$$

### 交換律 (commutative law)

* $$X \cup Y = Y \cup X$$
* $$X\cap Y = Y \cap X$$

### 結合律 (associative law)

* $$(X \cup Y) \cup Z = X \cup (Y \cup Z)$$
* $$(X \cap Y) \cap Z = X \cap (Y \cap Z)$$

### 分配律 (distributive law)

* $$X \cap (\cup_{i \in I} Y_i) = \cup_{i \in I} (X \cap Y_i)$$
* $$X \cup (\cap_{i \in I} Y_i) = \cap_{i \in I} (X \cup Y_i)$$

### 吸收律(absorb law)

* $$X\cup(X\cap Y) = X$$
* $$X \cap (X \cup Y) = X$$

### 兩集合的關係必為不相交、部份相交或者子集合三種其中之一

![兩集合的關係為三種之一](../../.gitbook/assets/set\_algebra-min.png)

### additive function

> 函數$$f: U \rightarrow \mathbb{R}$$稱為additive function 若滿足 $$f(X \cup Y)=f(X)+f(Y), \ X,Y \subseteq U, \ X \cap Y = \emptyset$$。且具有以下性質：
>
> * $$f(X \cup Y) = f(X) + f(Y \setminus X)$$
> * $$f(X \cap Y) = f(X) + f(Y) - f(X \cap Y)$$

由定義可得知additive function在集合經函數變換後，其性質和變換前近似。

## 差集與補集運算(difference and complement)

令$$U$$為宇集合(universal set)，即為全部元素的集合。

### 補集(complement)

$$X^c = \{ z \ \vert \ z \in U \land z \notin X\}$$

* $$X^c = U \setminus X \equiv U-X$$
* $$X \cup X^c = U$$
* $$X \cap X^c = \emptyset$$

可得$$X, X^c$$為宇集合$$U$$的分割。

### 差集(difference)

元素只屬於第一個集合，但不屬於第二個集合，不符合交換律。

* $$X\setminus Y \equiv X-Y = \{ z \ \vert \ z \in X \land z \notin Y\} =X \cap Y^c$$

若$$X \subseteq Y$$，則$$Y - (Y -X)=Y$$

若$$X \cap Y = \emptyset$$，則$$X - Y= X, ~ Y - X=Y$$

### DeMorgan law

> * $$(X \cup Y)^c = X^c \cap Y^c$$
> * $$(X \cap Y)^c = X^c \cup Y^c$$
>
> 在指標集$$I$$為(有限或無限)可數集甚至為不可數集時也成立：
>
> * $$\displaystyle \left(\bigcup_{i \in I} X_i \right)^c = \bigcap_{i \in I} \left(X_i \right)^c$$
> * $$\displaystyle \left(\bigcap_{i \in I} X_i \right)^c = \bigcup_{i \in I} \left(X_i \right)^c$$

proof:

$$x \in \bigcup_{i\in I} X_i$$，可得元素$$x$$至少為其中一個集合的元素，即$$\exists j \in I \ni x \in X_j$$。

而$$x \in \left(\bigcup_{i\in I} X_i \right)^c$$，可得元素$$x$$不存在所有的$$X_i, ~ \forall i \in I$$中。

可得$$x \in X_i^c$$，且對於所有$$i \in I$$均成立，因此$$x \in \bigcap_{i \in I} (X_i)^c$$ (QED)。

proof:

$$x \in \bigcup_{i \in I} X_i^c \Leftrightarrow \exists j \in I \ni x \in X_j^c \Leftrightarrow x \notin \bigcap_{i \in I} X_i \Leftrightarrow x \in (\bigcap_{i \in I} X_i)^c$$ (QED)

## 對稱差運算(symmetric difference)

> $$X \Delta Y \equiv (X \cup Y) - (X \cap Y)$$

如果$$X \cap Y=\empty$$，則$$X \Delta Y = (X \cup Y)$$

## 子集合(subset)

> $$X$$為$$Y$$子集合，$$X\subseteq Y \Leftrightarrow \forall x \in X, x\in Y$$
>
> $$X$$為$$Y$$的真子集(proper subset) $$X \subset Y \Leftrightarrow X \subseteq Y \land X \neq Y$$

* 元素屬於集合，但不是子集合。如$$2 \in \{1,2,3\}$$but $$2 \subsetneq \{1,2,3\}$$。須改為 $$\{2\} \subseteq \{1,2,3\}$$。因為2為元素，而$$\{2\}$$是集合。
* <mark style="color:red;">對於任意的集合</mark>$$S$$，$$S$$<mark style="color:red;">為自身集合的子集合</mark>，即$$S \subseteq S$$($$\empty \subseteq \empty$$)。
* 空集合為任意集合的子集合(但不一定是元素)，$$\empty \subseteq S$$。

### 子集合滿足遞移律

> $$X \subseteq Y$$且 $$Y \subseteq Z$$則 $$X\subseteq Z$$
>
> $$X \not \subseteq Y, ~ Y \not \subseteq Z \Rightarrow X \not \subseteq Z$$

proof:

令$$\forall x \in X$$，因為$$X \subseteq Y$$，可得$$\forall x \in Y$$

因為$$Y \subseteq Z$$，可得$$\forall x \in Z$$，因此$$X \subseteq Z$$(QED)

### 集合相等的充要條件為兩集合互為子集合

> $$X \subseteq Y$$ 且 $$X \supseteq Y$$則$$X=Y$$

## 布林代數與sigma field(algebra)

給定一群基底集合，則由此基底集合所構成的空間中的任意集合，必須可以用此基底集合的(有限或無限)聯集(union)、交集(intersection)、補集(complement)操作所得出。

## Russell誖論 (Russell paradox)

前述在討論集合時，是定義集合內的元素均符合相同的性質(條件)。

> 令對於元素$$x$$, $$P(x) \in \{ true, false\}$$為做用在$$x$$的某種性質。因此可得集合$$\{x \vert P(x) \text{ is true} \}$$。
>
> 推論可得 $$\forall y, \ y \in \{x \vert P(x) \text{ is true}\} \Leftrightarrow P(y) \text{ is true}$$

但此此推論在集合論中有矛盾 (by Russell)，令 $$P(x)$$為 $$x$$is a set and $$x \notin x$$。即當$$x$$為一集合且不包含自已時，$$P(x)$$才為真。

* 如$$P({1,2,3})$$為true，因為$$\{1,2,3\} \notin \{1,2,3\}$$.
* 令$$S$$為包含所有集合的集合，因此$$S$$為集合，而且$$S \in S$$，所以$$P(S)$$為false。
* 考慮 $$\Omega = \{ x \vert P(x) \text{ is true}\} =\{ x \vert x \text{ is a set and } x \notin x\}$$，即$$\Omega$$為所有不包含自已集合的集合。
  * 考慮$$\Omega \in \Omega$$時，由定義知$$P(\Omega)$$為true，即$$\Omega$$為集合，且$$\Omega \notin \Omega$$。
  * 考慮 $$\Omega \notin \Omega$$時，由定義知$$P(\Omega)$$為true，此時$$\Omega$$在集合，因此$$\Omega \in \Omega$$。
  * 兩種推論都得到矛盾的結論。

得到上述矛盾結果的原因是因為討論的集合包含了"全部"的集合(包含了全部集合的集合)。如果要避開Russell誖論，可建構出不會產生Russell誖論的集合來討論即可。一般分析中的集合不會產生Russell誖論。
