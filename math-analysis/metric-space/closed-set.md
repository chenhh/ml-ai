---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> $$(X,d)$$為度量空間，集合$$S \subseteq X$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$$$S^c \equiv X \setminus S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup d(S)$$。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。

* 在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。
* 由於閉集合的餘集是開集，許多性質可用De Morgan定理證明。

### 閉集合包含其所有極限點

> * $$S \subseteq X$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。
> * $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$$$\forall r > 0~ \exists y \in S \setminus \{x\} \ni y \in N_r(x)$$
> * 而$$S$$所有極限點形成為集合為導集合$$d(S)$$

proof &gt;= \(閉集合的補集不包含集合的極限點\)

* 令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。
* 依開集合定義可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，因此$$ \exists r >0 \ni N_r(x) \cap S = \phi$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 \(QED\)。

proof &lt;=

* 令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni N_r(x) \cap S = \emptyset$$，因此$$x$$不是$$S$$的附著點。
* 可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合\(QED\)。

### 有限多個閉集合的聯集仍為閉集合

> $$A_n \subseteq X，~ n =1,2,\ldots, N$$為閉集合，則$$\cup_{n=1}^N A_n$$為閉集合。
>
> 註：無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$(A_1 \cup A_2)^c = A_1^c \cap A_2^c$$，因此$$A_1 \cup A_2 = (A_1^c \cap A_2^c )^c$$
* 同理可得 $$\cup_{n=1}^N A_n=A_1 \cup A_2 \cup \ldots \cup A_N = (A_1^c \cap A_2^c \cap \ldots \cap A_N^c)^c$$
* 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，可得$$\cup_{n=1}^N A_n$$為閉集合。\(QED\)

### 可數無限個閉集合的交集仍為閉集合

> $$A_n \subseteq X, ~ \ n \in \mathbb{N}$$為閉集合，則 $$\cap_{n =1}^\infty A_n$$為閉集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$\cap_{n=1}^\infty A_n=(A_1 \cap A_2 \cap \ldots )=(A_1^c \cup A_2^c \cup \ldots )^c$$
* 因為[可數無限個開集點的聯集仍是開集合](open-set.md#ren-yi-ke-shu-wu-xian-ge-kai-ji-he-de-lian-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，因此$$\cap_{n=1}^\infty A_n$$ 為閉集合。\(QED\)

### 開集合與閉集合的差集的性質

> $$A,B \subseteq X$$，若$$A$$為開集合，$$B$$為閉集合，則$$A\setminus B$$為開集合，$$B \setminus A$$為閉集合。

* $$A\setminus B = A \cap B^c $$，因為[有限個開集合的任意交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，因此為開集合。
* $$B\setminus A = B \cap A^c$$，因為可數無限個閉集合的交集仍為閉集合，因此為閉集合。

### 實數中空集合與實數同時為開集合與閉集合

* 可得$$ \forall x \in \mathbb{R}, \exists r>0 \ni N_r (x) \subseteq \mathbb{R}$$, 因此$$\mathbb{R}$$為開集合。
* 因為$$\emptyset = \mathbb{R}^c$$, 所以$$\emptyset$$為閉集合。
* 因為空集合$$\emptyset$$不存在任何元素，因此其為開集合。
* 而$$\mathbb{R}=\emptyset^c$$, 所以$$\mathbb{R}$$為閉集合。
* **此範例說明了閉集合不一定有界**。

## 閉包（closure）

> $$S\subseteq X$$，$$d(S)$$為集合$$S$$的導集合（所有極限點的集合），定義閉包$$\overline{S} = S \cup d(S)$$。
>
> * $$d(S) = \{ x \in X | \forall r > 0, \ N_r(x) \cap S \setminus \{ x \} = \emptyset \}$$
> * 極限點$$x \in X$$不一定是$$S$$的元素。
>
> 定義2：$$\overline{S}=\cap\{ F \subseteq X | S \subset F \text{ and } F \text{ is closed set}  \}$$，即閉包為包含$$S$$的最小閉集合。

### 閉集合等於其閉包

> $$S \subseteq X$$為閉集合 $$\Leftrightarrow$$$$S= \overline{S}=S \cup d(S)$$

proof =&gt; 

* 因為 [閉集合包含其所有極限點](closed-set.md#bi-ji-he-bao-han-qi-suo-you-ji-xian-dian)，可得$$d(S) \subseteq S$$，所以$$\overline(S) = S \cup d(S) = S$$ \(QED\)

proof &lt;=

* 令$$x \in \overline{S}$$為極限點，則$$x$$為$$S$$或$$d(S)$$的極限點。
* 若$$x \in S$$，因為$$d(S)$$為所有$$S$$極限點的集合，因此$$x \in d(S)$$，所以$$x \in \overline{S}$$。
* 若$$x \in d(S)$$，因為$$d(S)$$為閉集合，所以$$d(S) \subseteq \overline{S}$$，可得$$x \in \overline{S}$$
* 所以$$S=\overline{S}$$包含所有極限點，因此$$S$$為閉集合。\(QED\)

### 導集合的性質

> $$d(S)$$為$$S$$的導集合，$$d(T)$$為$$T$$的導集合，閉包$$\overline{S}=S \cup d(S)$$，則
>
> 1. $$d(S)$$為閉集合，且$$d(d(S)) \subseteq d(S)$$
> 2. $$S \subseteq T \Rightarrow d(S) \subseteq d(T)$$
> 3. $$d(S \cup T)= d(S) \cup d(T)$$
> 4. $$d(\overline{S})=d(S)$$
> 5. $$\overline{S}$$為包含$$S$$的最小閉集合。

Proof \(1\):

* $$d(S)=\{x \in X| \forall r>0, N_r (x) \cap S \setminus \{x\}\neq \emptyset\}$$
* $$d(d(S))= \{ x \in S | \forall r>0, N_r (x)\cap d(S) \setminus\{x\} \neq \emptyset\} $$
* 令$$x \in d(d(S))$$$$ \Rightarrow x \in S,  \forall r>0, N_r (x)∩d(S) \setminus \{x\} \neq \emptyset $$
* $$\therefore \forall r>0, N_r (x)\cap S \setminus \{x\} \neq \emptyset $$
* $$\therefore x \in d(d(S) ) \Rightarrow x \in d(S)$$  \(QED\)

Proof \(2\):

* 給定$$x \in d(S) \Rightarrow x \in X, \forall r>0, N_r (x)\cap S \setminus \{x\} \neq \emptyset$$
*  $$\because S \subseteq T \Rightarrow x \in X, \forall r>0, N_r (x)\cap T \setminus \{x\} \neq \emptyset  $$
* $$ \therefore x \in d(T)$$
* $$\therefore x \in d(S) \Rightarrow x \in d(T) $$ \(QED\)

Proof \(3\)

* $$x \in d(S \cup T) \Rightarrow x \in X, \forall r>0, N_r (x) \cap (S \cup T) \setminus \{x\} \neq \emptyset $$
* 由De Morgan定理得 $$N_r (x)\cap (S \cup T)=(N_r (x)\cap S) \cup (N_r (x)\cap T) $$
* 而$$(N_r (x)\cap S)\cup (N_r (x) \cap T)\setminus \{x\}=(N_r (x)\cap S\setminus \{x\})\cup (N_r (x)\cap T\setminus \{x\}) $$
* $$\therefore x \in X, \forall r>0, (N_r (x)\cap S \setminus \{x\})\cup (N_r (x)\cap T \setminus \{x\})\neq \emptyset $$
* 即$$x \in d(S) \cup d(T) $$
* 同理可得$$x \in d(S) \cup d(T) \Rightarrow x \in d(S\cup T) $$
* 所以$$d(S \cup T)=d(S) \cup d(T)$$  \(QED\)

Proof \(4\)

* $$ \overline{S}=S \cup d(S) $$
* $$\therefore d(S \cup d(S) )=d(S) \cup d(d(S)) $$
* $$\because d(d(S) \subseteq d(S) $$
* $$\therefore  d(S) \cup d(d(S))= d(S)$$
* $$\therefore d(S \cup d(S))=d(S)$$  \(QED\).

### 開集合為其閉包的真子集

> $$ S \subseteq X$$為開集合，則$$S \subset \overline{S}$$。

*  因為$$S$$為開集合，所以$$S^c$$為閉集合，所以存在極限點$$x \in S^c$$, 且$$x \notin S$$。
* 而閉包$$\overline{S} = S \cup d(S)$$，依定義$$x \in d(S)$$且$$x \notin S$$，則$$ S \subset \overline{S}$$。\(QED\)

### 閉包交集的性質

> $$S,T \subseteq X$$，且$$\overline{S}, \overline{T}$$為對應的閉包，則：
>
> 1. $$\overline{S \cap T} \subseteq \overline{S} \cap \overline{T}$$
> 2. 若$$S$$為開集合，則$$S \cap \overline{T} \subseteq \overline{S \cap T}$$

proof \(1\):

* $$\overline{(S\cap T)}=(S \cap T)\cup d(S\cap T)$$  
* $$\overline{S} \cap \overline{T}=(S \cup d(S) )\cap (T \cup d(T) )=(S\cap T) \cup (d(S) \cap T) \cup (S\cap d(T) ) \cup (d(S) \cap d(T) ) $$
* 檢驗$$d(S\cap T)  \subseteq (d(S) \cap T) \cup (S \cap d(T) ) \cup (d(S) \cap d(T) ) $$
* $$x \in d(S \cap T)$$，即$$x$$為$$S \cap T$$的極限點，因此$$x$$為$$S$$的極限點且$$x$$為$$T$$的極限點，可得$$x \in d(S) \cap d(T)$$  \(QED\)

proof \(2\):

* 若$$S$$為開集合，則$$S \cap \overline{T}=S \cap (T \cup d(T) )=(S \cap T) \cup (S \cap d(T) ) $$
* $$ \overline{(S \cap T)}=(S \cap T)\cup d(S \cap T) $$
* 檢驗 $$(S\cap d(T) ) \subseteq d(S\cap T) $$
* $$x \in d(S\cap T)$$，即$$x$$為$$S\cap T$$的極限點，可得$$x$$為$$S$$的極限點且$$x$$為$$T$$的極限點  。
* 因為$$S$$為開集合，因此$$S$$不包含所有$$S$$的極限點，即$$\exists x \in S$$, $$x$$不是$$S$$的極限點。
* 因為$$x \in S \cap d(T)$$，表示$$x \in S$$且$$x$$為$$T$$的極限點。
* 因此$$S\cap \overline{T} \subseteq \overline{(S\cap T)}$$  \(QED\)

## 稠密集合（dense set）

> 令$$A \subseteq X$$，且存在$$S \subseteq X$$使得$$A \subseteq S \subseteq \overline{A}$$，則稱集合$$A$$在集合$$S$$中稠密。\(A dense in S\)。
>
> * $$A$$的閉包$$\overline{A}$$是包含$$A$$的最小閉集合，其包含了$$A$$的所有極限點。因此$$S$$包含了$$A$$的所有元素，以及集合$$A$$外的部分或全部極限點。

* 例$$A=(0,1) \subseteq \mathbb{R}$$，$$S=[0,1)$$或$$(0,1)$$或$$(0,1]$$或$$[0,1]$$，則$$A$$在$$S$$稠密。
* 有理數在實數稠密，因為$$\mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{\overline{Q}} = \mathbb{R}$$。

### 稠密集合滿足遞移性

> •$$A$$在集合$$S$$中稠密，且$$S$$在集合$$T$$中稠密，則$$A$$在集合$$T$$中稠密。

* $$A$$在集合$$S$$中稠密 ，即$$A \subseteq S \subseteq \overline{A}=A\cup d(A) $$
* $$S$$在集合$$T$$中稠密，即$$S\subseteq T\subseteq \overline{S}=S \cup d(S) $$
* 可得$$A⊆S⊆T  $$
* 檢驗$$T\subseteq \overline{A}$$

  * 若$$S=A \cup d(A)$$，則$$S$$為閉集合，即$$S=\overline{S}=T$$, 可得$$T=\overline{A} $$。
  * 若$$S \subset A \cup d(A)$$，即$$S$$包含了$$A$$中所有元素與$$A$$的部分極限點。
  * $$ \overline{S}=S \cup d(S) \subset (A\cup d(A) ) \cup d(A \cup d(A))=(A \cup d(A) ) \cup (d(A) \cup d(d(A)) )=A \cup d(A) \cup d(d(A) )) $$
  * 因為$$d(d(A)) \subseteq d(A)$$
  * 所以$$A \cup d(A) \cup d(d(A)) = A \cup d(A)$$
  * 因此$$\overline{S} \subset (A∪d(A))=\overline{A} \Rightarrow T \subset \overline{A} $$
  * 由$$A\subseteq T \subseteq \overline{A} $$ 得證 \(QED\)

### 稠密集合的性質

> 1. • 若$$A$$在集合$$S$$中稠密（$$A \subseteq S \subseteq \overline{A}$$），且$$B$$為$$S$$中的開集合，則$$B \subseteq \overline(A \cap B) $$。
> 2. 若$$A, B$$在集合$$S$$中稠密，且$$B$$為$$S$$中的開集合，則$$A \cap B$$在$$S$$中稠密。

proof \(1\):

* $$A$$在集合$$S$$中稠密，則$$S \subseteq A \subseteq \overline{S}$$
* $$B$$為$$S$$中的開集合，由[閉包交集的性質](closed-set.md#bi-bao-jiao-ji-de-xing-zhi)得 $$B \cap \overline{A} \subseteq \overline{(A \cap B) }$$
* 因為 $$B \subseteq S,\ S\subseteq A \Rightarrow B\subseteq A$$，所以
* 所以 $$B=B \cap \overline{A} \subseteq \overline{(A\cap B)}$$  \(QED\)

proof \(2\):

* • $$A,B$$在集合$$S$$中稠密，則$$S \subseteq A \subseteq \overline{S}$$,  $$S \subseteq B \subseteq \overline{S}$$,  可得$$A \cap B \subseteq \overline{S}$$。

  • 檢驗 $$S \subseteq A \cap B $$

  	• 若$$A=S, B=S$$， 可得$$A \cap B=S$$

  	• 若$$A \supset S, B=S$$，則 $$A \cap B=S$$

  	• 若$$A=S, B \supset S$$，則 $$A \cap B=S$$

  	• 若$$A \supset S, B \supset S$$，則 $$A \cap B \supseteq S $$

  • 因此$$S \subseteq A \cap B \subseteq  \overline{S}$$  \(QED\).





