# 實數

## 簡介

分析數學中的主要概念，如收斂性、微分與積分等，對其討論時，必定都將追溯到實數系的基本性質。	• 我們需證明實數集合$$\mathbb{R}$$ 為一個具有完備性的有序體\(complete ordered field\)。

### 實數的組成

$$\mathbb{N}$$為自然數集合，$$\mathbb{Z}$$為整數集合，$$\mathbb{Q}$$為有理數集合，$$\mathbb{\Gamma}$$為無理數集合，$$\mathbb{A}_R$$為代數數中的實數集合，$$\mathbb{T}_R$$為超越數\(transcendental number\)的實數集合，$$\mathbb{R}$$為實數集合，$$\mathbb{C}$$為複數集合。

* $$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{A}_R \subset \mathbb{R} \subset \mathbb{C}$$
* $$\mathbb{Q} \cup \mathbb{\Gamma} = \mathbb{R}$$ and $$\mathbb{Q} \cap \mathbb{\Gamma} = \emptyset$$
* $$\mathbb{A}_R \cup \mathbb{T}_R = \mathbb{R}$$and $$\mathbb{A}_R \cap \mathbb{T}_R= \emptyset$$
* $$\mathbb{Q} \subset \mathbb{A}_R$$
* $$\mathbb{T}_R \subset \mathbb{\Gamma}$$

![&#x5BE6;&#x6578;&#x4E2D;&#x7684;&#x96C6;&#x5408;](../.gitbook/assets/real_number_sets-min.png)





## 整數\(integer\)

* 整數集合 $$\mathbb{Z} = \{ \cdots, -2, -1, 0, 1, 2, \cdots \}  = - \mathbb{N} \cup \{0\} \cup \mathbb{N}$$
* 可以處理$$ a−b,  a<b  \text{ and } a, b \in \mathbb{N}$$ 擴展定義
* 由定義可得自然數為整數的子集合，$$\mathbb{N} \subset \mathbb{Z}$$。
* 雖然自然數為整數的子集合，但因為兩者均為無限集合，且兩者可找出一對一且映成的函數，所以兩集合元素個數相等，$$| \mathbb{N} | = | \mathbb{Z} |$$。

## 有理數\(rational number\)

* 有理數定義為 $$r = \frac{n}{m}, \forall n, m \in \mathbb{Z}$$，$$gcd(n,m)=1$$，是為了處理$$ \frac{n}{m}$$ 不為整數的擴展定義。
* 有理數集合記為$$\mathbb{Q}$$
* 兩個有理數之間，必定存在一個相異有理數，所以**有理數處處稠密\(dense\)**。
  * $$\forall a,b \in \mathbb{Q} ,\text {let } c = \frac{a+b}{2} \Rightarrow c \in \mathbb{Q}$$
* 因為有理數+無理數\(如$$1 + \sqrt{2}$$\)仍為無理數，同理**無理數處處稠密**。

有理數的有限個數十進位表示法$$ r = a_0 + \frac{a_1}{10}+\frac{a_2}{10^2}+\cdots + \frac{a_n}{10^n}=a_0.a_1a_2\cdots a_n, a_0 \in \mathbb{Z}, a_1,\cdots, a_n \in \{0,1,2,\cdots, 9\}$$

## 無理數 \(irrational number\)

* 無理數即實數中，無法表示為有理數之數，定義為集合$$\mathbb{\Gamma}$$。
* 
  任一無理數均可表示為不循環的小數。

* 實數為有理數與無理數的聯集，$$\mathbb{R} = \mathbb{Q} \cup \mathbb{\Gamma}$$ 且$$ \mathbb{Q} \cap \mathbb{\Gamma} = \emptyset$$。

無理數主要有以下三種定義方法：

* \[最常見且直覺\] Dedekind以分劃\(cut\)定義無理數。
* Cantor以收斂有理數數列定義無理數 \(converge sequence of rational numbers\)。
* Weierstrass以nested interval定義無理數。

## 代數數\(algebraic number\)

* 代數數是任何整係數多項式的複數根，因此代數數可為實數或複數。
  * $$z \in \mathbb{C}$$若存在$$ n \in \mathbb{N}$$以及 $$q_0, q_1, \cdots, q_n \in \mathbb{Q}, q_n \neq 0 \$$
  * $$ \ni q_n z^n + q_{n-1} z^{n-1} + \cdots + q_1z + q_0 = 0$$
  * 則稱$$z$$為代數數。
* 因為$$q_i$$為有理數，只要乘以$$M_i \in \mathbb{N}$$可變為整數，因此所以「存在有理係數多項式使得$$z$$是其複數根」可以推出「存在整係數多項式使得$$z$$是其複數根」。
* 同理， ，由於整數集合是有理數集合的子集，所以「存在整係數多項式使得$$z$$是其複根」也可以推出「存在有理係數多項式使得$$z$$是其複根」。這說明兩個定義是等價的。



* 因為整係數多項式的未知元素為可數個，所以**代數數為可數集合\(可數無限多的可數集的聯集是可數\)**。
* 兩個代數數的和、差、積與商（約定除數不為零）也是代數數。

## 超越數\(transcendental number\)

超越數是指任何一個不是代數數的無理數。只要它不是任何一個有理係數代數方程的根，它即是超越數。如$$\pi, e$$。

* 超越數是代數數的相反，也即是說若$$x$$是一個超越數，那麼對於任何$$a_{n}, a_{n-1},\ldots ,a_{0}\in \mathbb{Z}, a_n \neq 0$$都符合 $$a_n x^n  + a_{n-1} x^{n-1} + \ldots +  a_1 x + a_0 \neq 0$$



幾乎所有的實數和複數都是超越數，這是因為代數數的集合是可數集，而實數和複數的集合是不可數集之故。

