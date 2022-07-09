---
description: closed set
---

# 閉集合

## 閉集合（closed set）

> $$(X,d)$$為度量空間，集合$$S \subseteq X$$，則
>
> * $$S$$為閉集合$$\Leftrightarrow$$$$S^c \equiv X \setminus S$$為開集合。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$等於其閉包$$\overline{S}$$，即$$S = \overline{S} \equiv S \cup d(S)$$。
> * $$S$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點(附著點)。

* 在定義上，閉集合是開集合的補集，但在結構上，閉集合有許多特殊的性質。
* 由於閉集合的餘集是開集，許多性質可用De Morgan定理證明。
* 實數上常見的閉集合為閉區間$$[a,b]$$，在$$n$$維空間則為閉球$$(a_1, b_1) \times (a_2, b_2) \times \cdots \times (a_n, b_n)$$。

### 閉集合包含其所有極限點

> * $$S \subseteq X$$為閉集合$$\Leftrightarrow$$$$S$$包含其所有極限點。
> * $$x \in X$$為$$S$$的極限點 $$\Leftrightarrow$$$$\forall r > 0~ \exists y \in S -\{x\} \ni y \in N_r(x)$$
> * 而$$S$$所有極限點形成為集合為導集合$$d(S)$$

proof >= (閉集合的補集不包含集合的極限點)

* 令$$x \in S^c$$，因為$$S$$為閉集合，所以$$S^c$$為開集合。
* 依開集合定義可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，因此$$\exists r >0 \ni N_r(x) \cap S = \phi$$，即$$x$$不是$$S$$的附著點，因此$$x$$不是$$S$$的極限點 (QED)。

proof <=

* 令$$x \in S^c$$，因為$$x \notin S$$，可得$$\exists r > 0 \ni N_r(x) \cap S = \emptyset$$，因此$$x$$不是$$S$$的附著點。
* 可得 $$\exists r >0 \ni N_r(x) \subseteq S^c$$，即$$S^c$$為開集合，則$$S$$為閉集合(QED)。

### 有限多個閉集合的聯集仍為閉集合

> $$A_n \subseteq X，~ n =1,2,\ldots, N$$為閉集合，則$$\cup_{n=1}^N A_n$$為閉集合。
>
> 註：無限多個閉集合的聯集可能會變成無上、下限的集合而變成開集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$(A_1 \cup A_2)^c = A_1^c \cap A_2^c$$，因此$$A_1 \cup A_2 = (A_1^c \cap A_2^c )^c$$
* 同理可得 $$\cup_{n=1}^N A_n=A_1 \cup A_2 \cup \ldots \cup A_N = (A_1^c \cap A_2^c \cap \ldots \cap A_N^c)^c$$
* 因為[有限多個開集合的交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，可得$$\cup_{n=1}^N A_n$$為閉集合。(QED)

### 可數無限個閉集合的交集仍為閉集合

> $$A_n \subseteq X, ~ \ n \in \mathbb{N}$$為閉集合，則 $$\cap_{n =1}^\infty A_n$$為閉集合。

* $$A_n$$為閉集合，則依定義$$A_n^c$$為開集合。
* 由DeMorgan定理知 $$\cap_{n=1}^\infty A_n=(A_1 \cap A_2 \cap \ldots )=(A_1^c \cup A_2^c \cup \ldots )^c$$
* 因為[可數無限個開集點的聯集仍是開集合](open-set.md#ren-yi-ke-shu-wu-xian-ge-kai-ji-he-de-lian-ji-reng-shi-kai-ji-he)，而開集合的補集為閉集合，因此$$\cap_{n=1}^\infty A_n$$ 為閉集合。(QED)

### 開集合與閉集合的差集的性質

> $$A,B \subseteq X$$，若$$A$$為開集合，$$B$$為閉集合，則$$A\setminus B$$為開集合，$$B \setminus A$$為閉集合。

* $$A\setminus B = A \cap B^c$$，因為[有限個開集合的任意交集仍為開集合](open-set.md#you-xian-ge-kai-ji-he-de-jiao-ji-reng-shi-kai-ji-he)，因此為開集合。
* $$B\setminus A = B \cap A^c$$，因為可數無限個閉集合的交集仍為閉集合，因此為閉集合。

### 實數中空集合與實數同時為開集合與閉集合

* 可得$$\forall x \in \mathbb{R}, \exists r>0 \ni N_r (x) \subseteq \mathbb{R}$$, 因此$$\mathbb{R}$$為開集合。
* 因為$$\emptyset = \mathbb{R}^c$$, 所以$$\emptyset$$為閉集合。
* 因為空集合$$\emptyset$$不存在任何元素，因此其為開集合。
* 而$$\mathbb{R}=\emptyset^c$$, 所以$$\mathbb{R}$$為閉集合。
* **此範例說明了閉集合不一定有界**。

### 實數中整數集合與自然數集合為（無界）閉集合

* $$\mathbb{Z}, \mathbb{N}$$為閉集合。因為$$\mathbb{R} - \mathbb{Z},～\mathbb{R} - \mathbb{N}$$為開集合。
* $$\mathbb{R} - \mathbb{Z} = \bigcup_{a \in \mathbb{Z}}(a,a+1)$$，$$(a,a+1)$$為開區間（開集合），而[可數個開集合的聯集仍為開集合](open-set.md#ren-yi-wu-xian-ge-kai-ji-he-de-jiao-ji-bu-yi-ding-shi-kai-ji-he)，因此$$\mathbb{R} - \mathbb{Z}$$為開集合。
* 由極限點的定義可知$$\mathbb{Z}$$不存在極限點，因此導集合$$d(\mathbb{Z})=\emptyset$$為空集合。
* 因為空集合為任意集合的子集合，所以$$d(\mathbb{Z}) \subseteq \mathbb{Z}$$，即整數集合包含了所有的極限點。

## 閉包（closure）

> $$S\subseteq X$$，$$d(S)$$為集合$$S$$的導集合（所有極限點的集合），定義閉包$$\overline{S} = S \cup d(S)$$。
>
> * $$d(S) = \{ x \in X | \forall r > 0, \ N_r(x) \cap S \setminus \{ x \} = \emptyset \}$$
> * 極限點$$x \in X$$不一定是$$S$$的元素。
>
> 定義2：$$\overline{S}=\cap\{ F \subseteq X | S \subset F \text{ and } F \text{ is closed set}  \}$$，即閉包為包含$$S$$的最小閉集合。

例如在度量空間$$(\mathbb{R}, d(x,y)=|x-y|)$$，$$E=(1,3) \cup \{6\}$$，則$$\overline{E}=[1,3] \cup \{6\}$$，極限點為$$d(E)=\{ 1,3\}$$，孤立點為$$\{6\}$$，內點為$$(1,3)$$，邊界點$$\partial (E)=\{1,3,6\}$$。

### 閉集合等於其閉包

> $$S \subseteq X$$為閉集合 $$\Leftrightarrow$$$$S= \overline{S}=S \cup d(S)$$
>
> 因此閉包$$\overline{S}$$包含了$$S$$的所有極限點（所有附著點）。

proof =>&#x20;

* 因為 [閉集合包含其所有極限點](closed-set.md#bi-ji-he-bao-han-qi-suo-you-ji-xian-dian)，可得$$d(S) \subseteq S$$，所以$$\overline(S) = S \cup d(S) = S$$ (QED)

proof <=

* 令$$x \in \overline{S}$$為極限點，則$$x$$為$$S$$或$$d(S)$$的極限點。
* 若$$x \in S$$，因為$$d(S)$$為所有$$S$$極限點的集合，因此$$x \in d(S)$$，所以$$x \in \overline{S}$$。
* 若$$x \in d(S)$$，因為$$d(S)$$為閉集合，所以$$d(S) \subseteq \overline{S}$$，可得$$x \in \overline{S}$$
* 所以$$S=\overline{S}$$包含所有極限點，因此$$S$$為閉集合。(QED)

### 導集合的性質

> $$d(S)$$為$$S$$的導集合，$$d(T)$$為$$T$$的導集合，閉包$$\overline{S}=S \cup d(S)$$，則
>
> 1. $$d(S)$$為閉集合，且$$d(d(S)) \subseteq d(S)$$
> 2. $$S \subseteq T \Rightarrow d(S) \subseteq d(T)$$
> 3. $$d(S \cup T)= d(S) \cup d(T)$$
> 4. $$d(\overline{S})=d(S)$$
> 5. $$\overline{S}$$為包含$$S$$的最小閉集合。

Proof (1):

* $$d(S)=\{x \in X| \forall r>0, N_r (x) \cap S \setminus \{x\}\neq \emptyset\}$$
* $$d(d(S))= \{ x \in S | \forall r>0, N_r (x)\cap d(S) \setminus\{x\} \neq \emptyset\}$$
* 令$$x \in d(d(S))$$$$\Rightarrow x \in S,  \forall r>0, N_r (x)∩d(S) \setminus \{x\} \neq \emptyset$$
* $$\therefore \forall r>0, N_r (x)\cap S \setminus \{x\} \neq \emptyset$$
* $$\therefore x \in d(d(S) ) \Rightarrow x \in d(S)$$  (QED)

Proof (2):

* 給定$$x \in d(S) \Rightarrow x \in X, \forall r>0, N_r (x)\cap S \setminus \{x\} \neq \emptyset$$
* &#x20;$$\because S \subseteq T \Rightarrow x \in X, \forall r>0, N_r (x)\cap T \setminus \{x\} \neq \emptyset$$
* $$\therefore x \in d(T)$$
* $$\therefore x \in d(S) \Rightarrow x \in d(T)$$ (QED)

Proof (3)

* $$x \in d(S \cup T) \Rightarrow x \in X, \forall r>0, N_r (x) \cap (S \cup T) \setminus \{x\} \neq \emptyset$$
* 由De Morgan定理得 $$N_r (x)\cap (S \cup T)=(N_r (x)\cap S) \cup (N_r (x)\cap T)$$
* 而$$(N_r (x)\cap S)\cup (N_r (x) \cap T)\setminus \{x\}=(N_r (x)\cap S\setminus \{x\})\cup (N_r (x)\cap T\setminus \{x\})$$
* $$\therefore x \in X, \forall r>0, (N_r (x)\cap S \setminus \{x\})\cup (N_r (x)\cap T \setminus \{x\})\neq \emptyset$$
* 即$$x \in d(S) \cup d(T)$$
* 同理可得$$x \in d(S) \cup d(T) \Rightarrow x \in d(S\cup T)$$
* 所以$$d(S \cup T)=d(S) \cup d(T)$$  (QED)

Proof (4)

* $$\overline{S}=S \cup d(S)$$
* $$\therefore d(S \cup d(S) )=d(S) \cup d(d(S))$$
* $$\because d(d(S) \subseteq d(S)$$
* $$\therefore  d(S) \cup d(d(S))= d(S)$$
* $$\therefore d(S \cup d(S))=d(S)$$  (QED).

### 開集合為其閉包的真子集

> $$S \subseteq X$$為開集合，則$$S \subset \overline{S}$$。

* &#x20;因為$$S$$為開集合，所以$$S^c$$為閉集合，所以存在極限點$$x \in S^c$$, 且$$x \notin S$$。
* 而閉包$$\overline{S} = S \cup d(S)$$，依定義$$x \in d(S)$$且$$x \notin S$$，則$$S \subset \overline{S}$$。(QED)

### 閉包交集的性質

> $$S,T \subseteq X$$，且$$\overline{S}, \overline{T}$$為對應的閉包，則：
>
> 1. $$\overline{S \cap T} \subseteq \overline{S} \cap \overline{T}$$
> 2. 若$$S$$為開集合，則$$S \cap \overline{T} \subseteq \overline{S \cap T}$$

proof (1):

* $$\overline{(S\cap T)}=(S \cap T)\cup d(S\cap T)$$ &#x20;
* $$\overline{S} \cap \overline{T}=(S \cup d(S) )\cap (T \cup d(T) )=(S\cap T) \cup (d(S) \cap T) \cup (S\cap d(T) ) \cup (d(S) \cap d(T) )$$
* 檢驗$$d(S\cap T)  \subseteq (d(S) \cap T) \cup (S \cap d(T) ) \cup (d(S) \cap d(T) )$$
* $$x \in d(S \cap T)$$，即$$x$$為$$S \cap T$$的極限點，因此$$x$$為$$S$$的極限點且$$x$$為$$T$$的極限點，可得$$x \in d(S) \cap d(T)$$  (QED)

proof (2):

* 若$$S$$為開集合，則$$S \cap \overline{T}=S \cap (T \cup d(T) )=(S \cap T) \cup (S \cap d(T) )$$
* $$\overline{(S \cap T)}=(S \cap T)\cup d(S \cap T)$$
* 檢驗 $$(S\cap d(T) ) \subseteq d(S\cap T)$$
* $$x \in d(S\cap T)$$，即$$x$$為$$S\cap T$$的極限點，可得$$x$$為$$S$$的極限點且$$x$$為$$T$$的極限點  。
* 因為$$S$$為開集合，因此$$S$$不包含所有$$S$$的極限點，即$$\exists x \in S$$, $$x$$不是$$S$$的極限點。
* 因為$$x \in S \cap d(T)$$，表示$$x \in S$$且$$x$$為$$T$$的極限點。
* 因此$$S\cap \overline{T} \subseteq \overline{(S\cap T)}$$  (QED)

## 緊緻集合（compact set）

> $$S\subseteq X$$ 稱為緊致集合若且唯若集合$$S$$的任意開覆蓋均存在有限個數的子開覆蓋。>

> 即$$S\subseteq X$$為緊緻集合 $$\Leftrightarrow \exists \{I_1, I_2,\ldots, I_m\}$$為開集合族且 $$S\subseteq \bigcup_{k=1}^m I_k$$。

### 緊緻度量空間的閉集合為緊緻集合

> $$(X,d)$$為緊緻度量空間，$$S \subseteq X$$為閉集合，則$$S$$為緊緻集合。

proof:

* 令開集合族$$F$$為$$S$$的開覆蓋，即$$S \subseteq \bigcup_{A \in F} A$$。
* 因為$$S$$為閉集合，所以$$X−S$$為開集合，所以$$F \cup \{X−S\}$$為$$X$$的開覆蓋。
* 因為$$X$$為緊緻集合，所以$$F\cup\{X−S\}$$為有限個元素的開集合族。
* $$S \subseteq X \subseteq \{A_1 \cup A_2 \cup \cdots \cup A_p \cup \{X−S\}\}$$
* 因為 $$\forall x \in S, x \notin X−S \Rightarrow S \subseteq \{A_1 \cup A_2 \cup \cdots \cup A_p\}$$
* 因此$$S$$為緊緻集合 (QED)

### 緊緻集合與閉集合的交集為緊緻集合

> $$(X,d)$$為度量空間，$$S,T \subseteq X$$。若$$S$$為閉集合且$$T$$為緊緻集合, 則$$S \cap T$$為緊緻集合> 。

Proof:

* $$S$$為閉集合 $$\Leftrightarrow  X−S$$為開集合。
* $$T$$在$$(X,d)$$為緊緻集合，由定義得即存在$$\{I_1,I_2,\ldots,I_n \}$$為開集合族， $$I_i \subseteq X$$且$$T \subseteq \bigcup_{i=1}^n I_i$$。
* 可得$$T \subseteq \{I_1 \cup I_2 \cup \ldots \cup I_n \cup \{X−S\} \}$$
* $$S\cap T \subseteq T \subseteq \{I_1 \cup I_2 \cup \ldots \cup I_n \cup \{X−S\}\}$$
* 因為$$\forall x \in S \cap T$$，可得 $$x \notin X−S$$。
* 因此$$S \cap T \subseteq \{I_1 \cup I_2 \cup \ldots \cup I_n\}$$  (QED)

### 緊致集合的遞移性

> $$(X,d)$$為度量空間，且$$S,T \subseteq X$$。
>
> 若$$S \subseteq T$$，則$$S$$在$$(X,d)$$中為緊緻集合若且唯若$$S$$在$$(T,d)$$中為緊緻集合。

Proof =>

* $$S$$在$$(X,d)$$為緊緻集合，即存在$$\{I_1,I_2, \ldots ,I_n \}$$為開集合族， $$I_i \subseteq X$$且$$S \subseteq \bigcup_{i=1}^n I_i$$。
* 不失一般性，假設$$S \cap I_i \neq \emptyset, ~ i=1,2,\ldots,n$$。&#x20;
* 因為$$S \subseteq T \Rightarrow T \cap I_i \neq \emptyset, i=1,2, \ldots ,n$$。
* 令$$J_i=T \cap I_i$$, 可得 $$S \subseteq \bigcup_{i=1}^n J_i,  ~\forall J_i \subseteq T$$
* 所以$$S$$在$$(T,d)$$為緊緻集合 (QED)

• Proof <=:&#x20;使用相同的方式可得證 (QED)

### 有限個緊緻集合的聯集仍為緊緻集合

> $$(X,d)$$為度量空間，$$S_1,S_2, \ldots ,S_n \subseteq X$$為緊緻集合，則$$\bigcup_{i=1}^n S_n$$ 為緊緻集合。

由緊緻集合的定義可證明。

### 任意數量的緊緻集合的交集仍為緊緻集合

> $$(X,d)$$為度量空間，$$S_1,S_2, \ldots \subseteq X$$為緊緻集合，則$$\bigcap_{i=1}^\infty S_n$$ 為緊緻集合。

由緊緻集合的定義可證明。

## 稠密集合（dense set）

> 令$$A \subseteq X$$，且存在$$S \subseteq X$$使得$$A \subseteq S \subseteq \overline{A}$$，則稱集合$$A$$在集合$$S$$中稠密。(A dense in S)。
>
> * $$A$$的閉包$$\overline{A}$$是包含$$A$$的最小閉集合，其包含了$$A$$的所有極限點。因此$$S$$包含了$$A$$的所有元素，以及集合$$A$$外的部分或全部極限點。

* 例$$A=(0,1) \subseteq \mathbb{R}$$，$$S=[0,1)$$或$$(0,1)$$或$$(0,1]$$或$$[0,1]$$，則$$A$$在$$S$$稠密。
* 有理數在實數稠密，因為$$\mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{\overline{Q}} = \mathbb{R}$$。

### 稠密集合滿足遞移性

> •$$A$$在集合$$S$$中稠密，且$$S$$在集合$$T$$中稠密，則$$A$$在集合$$T$$中稠密> 。

* $$A$$在集合$$S$$中稠密 ，即$$A \subseteq S \subseteq \overline{A}=A\cup d(A)$$
* $$S$$在集合$$T$$中稠密，即$$S\subseteq T\subseteq \overline{S}=S \cup d(S)$$
* 可得$$A⊆S⊆T$$
*   檢驗$$T\subseteq \overline{A}$$

    * 若$$S=A \cup d(A)$$，則$$S$$為閉集合，即$$S=\overline{S}=T$$, 可得$$T=\overline{A}$$。
    * 若$$S \subset A \cup d(A)$$，即$$S$$包含了$$A$$中所有元素與$$A$$的部分極限點。
    * $$\overline{S}=S \cup d(S) \subset (A\cup d(A) ) \cup d(A \cup d(A))=(A \cup d(A) ) \cup (d(A) \cup d(d(A)) )=A \cup d(A) \cup d(d(A) ))$$
    * 因為$$d(d(A)) \subseteq d(A)$$
    * 所以$$A \cup d(A) \cup d(d(A)) = A \cup d(A)$$
    * 因此$$\overline{S} \subset (A∪d(A))=\overline{A} \Rightarrow T \subset \overline{A}$$
    * 由$$A\subseteq T \subseteq \overline{A}$$ 得證 (QED)



### 稠密集合的性質

> 1. • 若$$A$$在集合$$S$$中稠密（$$A \subseteq S \subseteq \overline{A}$$），且$$B$$為$$S$$中的開集合，則$$B \subseteq \overline(A \cap B)$$。
> 2. 若$$A, B$$在集合$$S$$中稠密，且$$B$$為$$S$$中的開集合，則$$A \cap B$$在$$S$$中稠密。

proof (1):

* $$A$$在集合$$S$$中稠密，則$$S \subseteq A \subseteq \overline{S}$$
* $$B$$為$$S$$中的開集合，由[閉包交集的性質](closed-set.md#bi-bao-jiao-ji-de-xing-zhi)得 $$B \cap \overline{A} \subseteq \overline{(A \cap B) }$$
* 因為 $$B \subseteq S,\ S\subseteq A \Rightarrow B\subseteq A$$，所以
* 所以 $$B=B \cap \overline{A} \subseteq \overline{(A\cap B)}$$  (QED)

proof (2):

*   • $$A,B$$在集合$$S$$中稠密，則$$S \subseteq A \subseteq \overline{S}$$,  $$S \subseteq B \subseteq \overline{S}$$,  可得$$A \cap B \subseteq \overline{S}$$。

    • 檢驗 $$S \subseteq A \cap B$$

    &#x9;• 若$$A=S, B=S$$， 可得$$A \cap B=S$$

    &#x9;• 若$$A \supset S, B=S$$，則 $$A \cap B=S$$

    &#x9;• 若$$A=S, B \supset S$$，則 $$A \cap B=S$$

    &#x9;• 若$$A \supset S, B \supset S$$，則 $$A \cap B \supseteq S$$

    • 因此$$S \subseteq A \cap B \subseteq  \overline{S}$$  (QED)

可分離集合（separable set）
---------------

> 給定度量空間$$(X,d)$$，$$X$$稱為可分離集合若存在可數子集合$$A \subseteq X$$, 且$$A$$在$$X$$中稠密\[（$$A \subseteq X \subseteq \overline{A}$$）。>

* 例如實數$$\mathbb{R}$$為可分離集合，因為存在有理數$$\mathbb{Q}$$在$$\mathbb{R}$$上稠密，且$$\mathbb{Q}$$為可數集合。
* 歐式空間$$\mathbb{R}^n$$均為可分離集合。
* **Lindelof覆蓋定理在可分離度量空間均成立**。

連通集合與分離集合（connected and separated set）
----------------------------------

> * 給定度量空間$$(X,d)$$，$$A,B \subseteq X$$稱為分離集合若$$A \cap B^c=A^c \cap B=\emptyset$$。
> * $$S \subseteq X$$稱為連通集合，若$$S$$不為兩個非空的分離集合的聯集， 即$$A \neq \emptyset$$, $$B \neq \emptyset$$,$$A \cap B \neq \emptyset$$。

![連通與分離集合](../../.gitbook/assets/220px-Union\_et\_intersection\_d'ensembles-min.png)
