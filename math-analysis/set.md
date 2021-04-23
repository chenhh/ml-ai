# 集合

## 集合的元素

一個集合\(set\)就是一些事物收集起來的結果。集合只討論元素間的關係，如果加上其它的函數，則會形成特定的空間。如考慮距離函數\(distance function\)則變成度量空間\(metric space\)。如果考慮角度和額外的性質，則會變成內積空間\(inner product space\)。

* 符合某一條件的數的全體稱為集合\(set\)，記為$$S$$。
* 符合此條件的每個數$$a$$均屬於此集合，記為$$a \in S$$。
* 不符合此條件的每個數$$b$$均不屬於此集合，記為$$b \not \in S$$。
* 任一數$$a$$必定是屬於集合$$S$$或是不屬於集合$$S$$，只能有一成立\(true or false，為一命題\)。

## 卡式積\(Cartesian product\)

the Cartesian product $$A\times B=\{ (a,b) \ \vert \ \forall a \in A, b\forall b \in B\}$$

* 若 $$|A| =M < \infty, |B|=N < \infty \Rightarrow |A \times B| =MN$$
* 集合$$A$$或$$B$$的元素可為無窮多個，如$$A=\mathbb{R}，B=\mathbb{R} \Rightarrow A \times B = \mathbb{R}^2$$

## 聯集與交集運算\(intersection and union\)

令$$X,Y$$為相異的兩個集合，$$I$$為一指標集合\(index set\)\(有限或無窮多個\)。

* 聯集\(union\): 屬於任一個集合的元素。 $$X \cup Y= \{z\ \vert \ z \in X \lor z \in Y\}$$
* 交集\(intersection\): 同時屬於所有集合的元素。$$X \cup Y= \{z \vert  z \in X \land z \in Y\}$$
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





## 





