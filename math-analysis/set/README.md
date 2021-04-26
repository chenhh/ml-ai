# 集合

## 集合的元素

一個集合\(set\)就是一些事物收集起來的結果。集合只討論元素間的關係，如果加上其它的函數，則會形成特定的空間。如考慮距離函數\(distance function\)則變成度量空間\(metric space\)。如果考慮角度和額外的性質，則會變成內積空間\(inner product space\)。

* 符合某一條件的數的全體稱為集合\(set\)，記為$$S$$。
* 符合此條件的每個數$$a$$均屬於此集合，記為$$a \in S$$。
* 不符合此條件的每個數$$b$$均不屬於此集合，記為$$b \not \in S$$。
* 任一數$$a$$必定是屬於集合$$S$$或是不屬於集合$$S$$，只能有一成立\(true or false，為一命題\)。
* 兩集合$$S,Q$$相等，即$$S = Q \Leftrightarrow S \subseteq Q \land Q \subseteq S$$。

  * note: 集合中的元素無順序性，$$\therefore \{ 1, 2, 3,4, 5\} = \{ 2, 1, 4, 5, 3\}$$
  * 集合中的重複元素只算一個，$$\therefore \{ 1,2, 1, 2, 3, 4,5\} = \{ 1,2,3,4,5\}$$

## 空集合\(empty set\)

> 空集合$$\emptyset \equiv \{ \}$$不含任何元素, $$\forall x, \ x \notin \emptyset$$。

* 空集合唯一，即若有兩個空集合$$\emptyset, \emptyset^{'} \Rightarrow \emptyset= \emptyset^{'}$$。
* 非空集合的集合必含有至少一個元素，即$$\exists x \ni x \in S$$。
* 空集合的基數為零，$$| \emptyset | = 0$$。

## singleton sets and pair sets

> * 若$$x$$為一物件，則$$\{x\}$$包含單一元素的集合。 即 $$\forall y, y \in \{x\} \Leftrightarrow y= x$$，稱$$\{x\}$$為包含元素$$x$$的singleton set。
> * 若$$x,y$$為物件，則$$\{x,y\}$$為包含兩元素的集合。即$$\forall z, z \in \{x,y\} \Leftrightarrow z = x \lor z =y$$。稱$$\{x,y \}$$為包含$$x,y$$的pair set。

* 由集合相等的定義知$$\{x,y\} = \{y,x\}$$，且$$\{x, x\} = \{x\}$$。
* 空集合的singleton set 為$$\{ \emptyset\}$$,，因此$$\emptyset \in \{\emptyset\}$$ 。可得 $$\{ \emptyset, \{ \emptyset\} \}$$也是集合。



## 卡式積\(Cartesian product\)

the Cartesian product $$X \times Y=\{ (x,y) \ \vert \ \forall x \in X, \forall y \in Y\}$$

* 若 $$|X| =M < \infty, |Y|=N < \infty \Rightarrow |X \times Y| =MN$$
* 集合$$X$$或$$Y$$的元素可為無窮多個，如$$X=\mathbb{R}，Y=\mathbb{R} \Rightarrow X \times Y = \mathbb{R}^2$$

## 聯集與交集運算\(intersection and union\)

令$$X,Y$$為相異的兩個集合，$$I$$為一指標集合\(index set\)\(有限或無窮多個\)。

* 聯集\(union\): 屬於任一個集合的元素。 $$X \cup Y= \{z\ \vert \ z \in X \lor z \in Y\}$$
  * $$X\cup X = X \cup \emptyset = \emptyset \cup X = X$$
* 交集\(intersection\): 同時屬於所有集合的元素。$$X \cap Y= \{z \vert  z \in X \land z \in Y\}$$
* 多集合的聯集: 元素只須存在於某一個集合。$$\cup_{i\in I} S_i =\{ x \ \vert \  \exists j\in I, x \in S_j\}$$



* 多集合的交集: 元素必須存在於所有的集合。 $$\cap_{i \in I} S_i = \{ x \ \vert \ \forall j \in I, x \in S_j\}$$
* 
  交換律 \(commutative law\)。 $$X \cup Y = Y \cup X$$， $$X\cap Y = Y \cap X$$

* 結合律 \(associative law\)。$$(X \cup Y) \cup Z = X \cup (Y \cup Z)$$，$$ (X \cap Y) \cap Z = X \cap (Y \cap Z)$$
* 


  分配律 \(distributive law\)。$$ X \cap (\cup_{i \in I} Y_i) = \cup_{i \in I} (X \cap Y_i)$$，$$ X \cup (\cap_{i \in I} Y_i) = \cap_{i \in I} (X \cup Y_i)$$

* 吸收律\(absorb law\)。 $$X\cup(X\cap Y) = X$$， $$ X \cap (X \cup Y) = X$$

## 差集與補集運算\(difference and complement\)

令$$U$$為宇集合\(universal set\)，即為全部元素的集合。

* 補集\(complement\)。$$X^c  = \{ z \ \vert \ z \in U \land z \notin X\}$$
* 差集\(difference\)：元素只屬於第一個集合，但不屬於第二個集合，不符合交換律。
  * $$ X\setminus Y = \{ z \ \vert \ z \in X \land z \notin Y\} =X \cap Y^c$$

## 子集合\(subset\)

> $$X$$為$$Y$$子集合，$$X\subseteq Y \Leftrightarrow \forall x \in X, x\in Y$$
>
> $$X$$為$$Y$$的真子集\(proper subset\)  $$X \subset Y \Leftrightarrow X \subseteq Y \land X \neq Y$$

* $$X \subseteq Y$$and $$Y \subseteq Z$$then $$ X\subseteq Z$$。
* $$ X \subseteq Y$$ and $$Y \subseteq X$$$$\Leftrightarrow$$ $$Ｘ=Y$$。
* 元素屬於集合，但不是子集合。如$$2 \in \{1,2,3\}$$but $$ 2 \subsetneq \{1,2,3\}$$。須改為 $$\{2\} \subseteq \{1,2,3\}$$。因為2為元素，而$$\{2\}$$是集合。



## 布林代數與sigma field\(algebra\)

給定一群基底集合，則由此基底集合所構成的空間中的任意集合，必須可以用此基底集合的\(有限或無限\)聯集\(union\)、交集\(intersection\)、補集\(complement\)操作所得出。

