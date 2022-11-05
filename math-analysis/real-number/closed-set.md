---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> 集合$$S \subseteq \mathbb{R}^n$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S^c \equiv \mathbb{R}^n - S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup S^d$$。
> * $$S$$為閉集合$$\Leftrightarrow$$ $$S$$包含其所有極限點(附著點)。

在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。

由於閉集合的餘集是開集，許多性質可用De-Morgan定理證明。

實數上常見的閉集合為閉區間$$[a,b]$$，在$$n$$維空間則為閉球$$[a_1, b_1] \times [a_2, b_2] \times \cdots \times [a_n, b_n]$$。


### 閉集合包含其所有極限點
> $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$ $$\forall r > 0~ \exists y \in S -\{x\} \ni y \in B_r(x)$$
> 
> 令$$S$$所有極限點形成為集合為導集合$$S^d$$ (derived set)
> 
> 在一般度量空間中均成立

<details>

<summary> proof: 閉集合的補集不包含原集合的極限點 </summary>

proof >= 

令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。

依開集合定義可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，

因此$$\exists r >0 \ni B_r(x) \cap S = \empty$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 (QED)。

proof <=

令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni B_r(x) \cap S = \empty$$，因此$$x$$不是$$S$$的附著點。

可得 $$\exists r >0 \ni B_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合(QED)。

</details>


### 有限多個閉集合的聯集仍為閉集合

> $$E_i \subseteq \mathbb{R}^n，~ i =1,2,\dots, N$$為閉集合，則$$\displaystyle \bigcup_{i=1}^N E_i$$為閉集合。
>
> 註：(可數或不可數)無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。
> 
> 在一般度量空間中均成立

<details>

<summary> proof: DeMorgan定理 </summary>

 $$E_i$$為閉集合，則依定義$$E_i^c$$為開集合。

 由DeMorgan定理知 $$(E_1 \cup E_2)^c = E_1^c \cap E_2^c$$，因此$$E_1 \cup E_2 = (E_1^c \cap E_2^c )^c$$

 同理可得 $$\cup_{i=1}^n E_i=E_1 \cup E_2 \cup \dots \cup E_n = (E_1^c \cap E_2^c \cap \dots \cap E_n^c)^c$$

 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，
 且開集合的補集為閉集合，可得$$\cup_{i=1}^N E_i$$為閉集合。(QED)

</details>

### 無限個閉集合的交集仍為閉集合

> $$E_i \subseteq \mathbb{R}^n, ~ \ i \in I$$為閉集合，則 $$\displaystyle \cap_{i \in I} E_i$$為閉集合。
> 
> 指標集合$$I$$可能為可數集合或是不可數集合。
> 
> 在一般度量空間中均成立

<details>

<summary> proof: DeMorgan定理 </summary>

因為$$E_i$$為閉集合，依定義$$E_i^c$$為開集合。

由DeMorgan定理知 $$\cap_{i \in I} E_i=(\cup_{i \in I} E_i^c)^c$$

因為[開集點的聯集仍是開集合](open-set.md#ren-yi-ke-shu-wu-xian-ge-kai-ji-he-de-lian-ji-reng-shi-kai-ji-he)，
而開集合的補集為閉集合，因此$$\cap_{i \in I} E_i$$ 為閉集合。(QED)

</details>

### 開集合與閉集合的差集的性質

> $$A,B \subseteq \mathbb{R}^n$$，若$$A$$為開集合，$$B$$為閉集合，則$$A - B$$為開集合，$$B - A$$為閉集合。
> 
> 在一般度量空間中均成立

<details>

<summary> proof: 以閉集合聯集與交集的性質可得證 </summary>

proof 1: $$A - B = A \cap B^c$$， 且$$A$$為開集合，$$B^c$$為開集合，而開集合的有限交集仍為開集合 (QED)。

proof 2: $$B - A = B \cap A^c$$， 且$$A^c$$為閉集合，$$B$$為閉集合，而閉集合的任意交集仍為閉集合 (QED)

</details>

### 歐式空間中空集合與宇集合同時為開集合與閉集合

> $$\empty$$與$$\mathbb{R}^n$$同時為開集合與閉集合。
> 
> 註：$$\mathbb{R}^n$$為無界閉集合。

可得$$\forall x \in \mathbb{R}^n, \exists r>0 \ni B_r (x) \subseteq \mathbb{R}^n$$, 因此$$\mathbb{R}^n$$為開集合。

因為$$\empty = (\mathbb{R}^n)^c$$, 所以$$\empty$$為閉集合。

同理因為空集合$$\empty$$不存在任何元素，因此其為開集合。

而$$\mathbb{R}^n=\empty^c$$, 所以$$\mathbb{R}^n$$為閉集合。

### 實數中整數集合與自然數集合為（無界）閉集合

> $$\mathbb{N},~ \mathbb{Z}$$均為無界閉集合。

<details>

<summary> proof: 可由補集為開集合或是導集合為空證明 </summary>

$$\mathbb{Z}, \mathbb{N}$$為閉集合。因為$$\mathbb{R} - \mathbb{Z}$$與$$\mathbb{R} - \mathbb{N}$$為開集合。

proof: 開集合

$$\mathbb{R} - \mathbb{Z} = \bigcup_{a \in \mathbb{Z}}(a,a+1)$$，$$(a,a+1)$$為開區間（開集合），
而[可數個開集合的聯集仍為開集合](open-set.md#ren-yi-wu-xian-ge-kai-ji-he-de-jiao-ji-bu-yi-ding-shi-kai-ji-he)，
因此$$\mathbb{R} - \mathbb{Z}$$為開集合。 (QED)

proof: 導集合為空集合

由極限點的定義可知$$\mathbb{Z}$$不存在極限點，因此導集合$$\mathbb{Z}^d=\empty$$為空集合。

因為空集合為任意集合的子集合，所以$$\mathbb{Z}^d \subseteq \mathbb{Z}$$，即整數集合包含了所有的極限點。 (QED)

</details>

### 歐式空間中的有限集都是閉集

> $$S \subset \mathbb{R}^n$$，且集合為有限集$$|S| < \infty$$，則$$S$$為閉集合。

<details>

<summary> proof: 補集為開集合得證  </summary>

令$$S \subset \mathbb{R}^n$$為有限集，

則$$\forall x \in \mathbb{R}^n - S$$，

取$$r > 0 \ni \forall y \in S, d(x,y) > r$$，則$$B_r(x) \subset R^n -S$$為開集合，因此$$S$$為閉集合(QED)。

</details>

## 閉包（closure）
> 
> 定義1：閉包為集合與其導集合的聯集
> 
> $$S\subseteq \mathbb{R}^n$$，$$S^d$$為集合$$S$$的導集合（所有極限點的集合），定義閉包$$\overline{S} = S \cup S^d$$。
>
> * $$S^d \equiv \{ x \in \mathbb{R}^n ~ |~ \forall r > 0, \ B_r(x) \cap S - \{ x \} = \empty \}$$
> * 極限點$$x \in \mathbb{R}^n$$不必為$$S$$的元素。
>
> 定義2：閉包為包含該集合的最小閉集合
> 
> $$\overline{S}=\cap\{ F \subseteq \mathbb{R}^n ~|~ S \subseteq F \text{ and } F \text{ is closed set}  \}$$

例如在度量空間$$(\mathbb{R}, d(x,y)=|x-y|)$$，$$E=(1,3) \cup \{6\}$$，
則$$\overline{E}=[1,3] \cup \{6\}$$，
導集合為$$E^d=\{ 1,3\}$$，孤立點為$$\{6\}$$，內點為$$(1,3)$$，邊界點$$E^b=\{1,3,6\}$$。


### 閉集合等於其閉包

> $$S \subseteq \mathbb{R}^n$$為閉集合 且$$S= \overline{S}=S \cup S^d$$
>
> 因此閉包$$\overline{S}$$包含了$$S$$的所有極限點（所有附著點）。
> 
> 一般度量空間也成立

<details>

<summary> proof:  </summary>

=>

因為閉集合包含其所有極限點，可得$$S^d \subseteq S$$，所以$$\overline(S) = S \cup S^d = S$$ (QED)

<=

令$$x \in \overline{S}$$為極限點，則$$x \in S$$或$$x \in S^d$$。

若$$x \in S$$，因為$$S^d$$為所有$$S$$極限點的集合，因此$$x \in S^d$$，所以$$x \in \overline{S}$$。

若$$x \in S^d$$，因為$$S^d$$為閉集合，所以$$S^d \subseteq \overline{S}$$，可得$$x \in \overline{S}$$

所以$$S=\overline{S}$$包含所有極限點，因此$$S$$為閉集合。(QED)

</details>

### 導集合的性質

> $$S^d$$為$$S$$的導集合，$$T^d$$為$$T$$的導集合，閉包$$\overline{S}=S \cup S^d$$，則
>
> 1. $$S^d$$為閉集合，且$$(S^d)^d \subseteq S^d$$
> 2. $$S \subseteq T \Rightarrow S^d \subseteq T^d$$
> 3. $$(S \cup T)^d= S^d \cup T^d$$
> 4. $$\overline{S}^d=S^d$$
> 5. $$\overline{S}$$為包含$$S$$的最小閉集合。

<details>

<summary> proof: 1 </summary>

$$S^d=\{x \in \mathbb{R}^n ~|~ \forall r>0, B_r (x) \cap S - \{x\}\neq \emptyset\}$$

$$(S^d)^d= \{ x \in S | \forall r>0, B_r (x)\cap S^d \setminus\{x\} \neq \emptyset\}$$

令$$x \in (S^d)^d$$ 則 $$ x \in S$$ 且滿足$$ \forall r>0, B_r (x) \cap S \setminus^d \{x\} \neq \emptyset$$

因此 $$\forall r>0, B_r (x)\cap S \setminus \{x\} \neq \emptyset$$

可得 $$\therefore x \in (S^d)^d \Rightarrow x \in S^d$$  (QED)

</details>

<details>

<summary> proof: 2 </summary>

給定$$x \in S^d$$ 可得 $$x \in \mathbb{R}^n, ~ \forall r>0, B_r (x)\cap S - \{x\} \neq \emptyset$$

因為 $$S \subseteq T$$，，因此上式可得$$x \in \mathbb{R}^n, ~ \forall r>0, B_r (x)\cap T \setminus \{x\} \neq \emptyset$$

可得$$\therefore x S^d \Rightarrow x \in T^d$$ (QED)

</details>

<details>

<summary> proof: 3 </summary>

令 $$x \in (S \cup T)^d$$，則$$ x \in \mathbb{R}^n,~ \forall r>0, B_r (x) \cap (S \cup T) - \{x\} \neq \emptyset$$

由De Morgan定理得 $$B_r (x)\cap (S \cup T)=(B_r (x)\cap S) \cup (B_r (x)\cap T)$$

而$$(B_r (x)\cap S)\cup (B_r (x) \cap T)- \{x\}=(B_r (x)\cap S-  \{x\})\cup (B_r (x)\cap T - \{x\})$$

因此$$x \in \mathbb{R}^n,~ \forall r>0, (B_r (x)\cap S - \{x\})\cup (B_r (x)\cap T \- \{x\}) \neq \emptyset$$

即$$x \in S^d \cup T^d$$

同理可得$$x \in S^d \cup T^d \Rightarrow x \in (S\cup T)^d$$

所以$$(S \cup T)^d=S^d \cup T^d$$  (QED)

</details>

<details>

<summary> proof: 4 </summary>

$$\overline{S}=S \cup S^d$$

因此$$\(S \cup S)^d=S^d \cup (S^d)^d $$

因為 $$(S^d)^d \subseteq S^d$$

所以$$S^d \cup (S^d)^d= S^d$$

因此$$(S \cup S^d)^d=S^d$$  (QED).


</details>

