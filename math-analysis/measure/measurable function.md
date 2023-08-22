---
description: measurable function
---

# 可測函數

## 可測函數定義

> 函數$$f: X \rightarrow \overline{\mathbb{R}}$$，$$(X, \Sigma)$$為可測空間，$$\overline{\mathbb{R}}=\mathbb{R}\cup\{\pm \infty\}$$為擴充實數集合。
>
> 對於實數上的任意開集合$$E\subseteq \mathbb{R}$$，若前像$$f^{-1}(E)=\{x \in X~|~f(x)\in E\} \in \Sigma$$且$$f^{-1}(\{+\infty\}) \in \Sigma$$，$$f^{-1}(\{-\infty\}) \in \Sigma,$$，則稱$$f$$為可測函數，或稱$$f$$在集合$$E$$上可測。
>
> 或者說 $$\forall t \in \mathbb{R}$$, 集合$$\{x \in X~|~ f(x) \leq t\} \in \Sigma$$，則$$f$$為可測函數。

<mark style="color:blue;">可測函數的值域為擴充實數，且值域任意值的前像集合必須為可測集合，以避免出現有函數值，但沒有定義域元素對應的情形</mark>。

可測函數$$f$$在機率空間$$(X,\mathbb{F}, P)$$中為隨機變數。

可測函數在極限運算下是封閉的，比連續函數在極限連算時非封閉的性質好。

## 可測函數的等價條件

> $$f: X \rightarrow \overline{\mathbb{R}}$$，則以下條件均等價：
>
> 1. $$f$$為可測函數
> 2. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c))=\{x \in X~|~ f(x)<c \} \in \Sigma$$
> 3. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c])=\{x \in X~|~ f(x)\leq c \} \in \Sigma$$
> 4. $$\forall c \in \mathbb{R}$$，$$f^{-1}((c, \infty))=\{x \in X~|~ f(x)>c \} \in \Sigma$$
> 5. $$\forall \in \mathbb{R}$$，$$f^{-1}([c, \infty))=\{x \in X~|~ f(x) \geq c \} \in \Sigma$$
> 6. $$f^{-1}(B) \in \mathbb{B}$$為Borel set(由實數上所有開(閉)區間形成的最小的sigma域)。

<details>

<summary>proof: 1-> 2：σ域中任意元素的聯集仍為σ域的元素。</summary>

因為$$f$$為可測函數，由定義得給定$$c \in \mathbb{R}$$，$$f^{-1}(c) \in \Sigma$$，同理$$\forall d < c$$，$$f^{-1}(d) \in \Sigma$$。

因為$$\Sigma$$定義集合內任意元素的聯集仍為$$\Sigma$$內的元素，因此$$f^{-1}(c \cup d) \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 2->3，用開區間逼近閉區間</summary>

$$(-\infty, c]=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})$$

由$$\Sigma$$的定義得$$f^{-1}((-\infty, c])=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})\in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 3->4，補集</summary>

$$f^{-1}((c, \infty))=f^{-1}((\mathbb{R} - (-\infty, c])=\mathbb{R}-f^{-1}((-\infty, c]) \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 4->5，用開區間逼近閉區間</summary>

$$f^{-1}([c, \infty)=f^{-1}(\bigcap_{n=1}^\infty (c - \frac{1}{n}, \infty))=\bigcap_{n=1}^\infty f^{-1}(c-\frac{1}{n}, \infty) \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 5->6</summary>

令$$S = \{A \subseteq \mathbb{R}, ~f^{-1}(A) \in \Sigma \}$$，檢驗Borel set $$\mathbb{B} \subseteq S$$。

由5得$$\forall c \in \mathbb{R}, [c, \infty) \subseteq S$$，且由1得$$\forall d \in \mathbb{R}, ~(-\infty, d) \subseteq S$$，還可得$$\forall e \in \mathbb{R}, (e, \infty) \subseteq S$$。

因此$$(e,d) \subseteq S$$，包含了實數上的任意開區間，因此$$\mathbb{B} \subseteq S$$ (QED)。

</details>

<details>

<summary>proof: 6->1</summary>

依可測函數定義可得(QED)

</details>

### 單調函數為可測函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為單調函數，則$$f(x)$$在閉區間$$[a,b]$$可測。

<details>

<summary>proof:</summary>

$$\forall t \in \mathbb{R}$$, 集合 $$E= \{ x \in [a,b] ~|~ f(x)<t \}$$必為以下三種集合之一： (半開或閉)區間、單點集合或空集合。

因此$$E$$為可測集 (QED)

</details>

### 個別可測集合的函數的聯集仍為可測函數

> 給定函數$$f: X_1 \cup X_2 \rightarrow \overline{R}$$，若$$f$$在 $$X_1$$可測，且在$$X_2$$也可測， 則在$$X_1 \cup X_2$$也可測。

<details>

<summary>proof: 以定義直接證明</summary>

因為$$f$$在$$X_1$$可測，可得$$\forall c \in \mathbb{R}$$, 可得$$f^{-1}((\infty, c)) \subseteq X_1$$。

同理因為$$f$$在$$X_2$$可測，可得$$\forall c \in \mathbb{R}$$, 可得$$f^{-1}((\infty, c)) \subseteq X_2$$

因此 $$\forall c \in \mathbb{R}$$，可得 $$f^{-1}((\infty, c)) \subseteq X_1 \cup X_2$$ (QED)

</details>

## 可測函數的計算性質

> $$f,g$$為集合$$X$$實值可測函數，則：
>
> 1. $$c \in \mathbb{R}~ cf(x)$$為可測函數。
> 2. $$f(x) + g(x)$$ 為可測函數。
> 3. $$f(x)g(x)$$為可測函數。

<details>

<summary>proof: 1</summary>

令$$\Sigma$$為$$X$$的sigma域。

因為$$f$$為可測函數，所以 $$\forall d \in \mathbb{R}, f^{-1}((-\infty, d)) \in \Sigma$$

若$$c >0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}((-\infty, cd)) \in \Sigma$$--(1)

若$$c <0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}((cd, \infty)) \in \Sigma$$--(2)

若$$c =0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}(\{0\}) \in \Sigma$$--(3)

由(1,2,3)得$$cf(x)$$為可測函數 (QED)

</details>

<details>

<summary>proof: 2</summary>

令$$\Sigma$$為$$X$$的sigma域。

$$\forall t \in \mathbb{R}$$，因為$$f(x) + g(x) <t$$就是$$f(x) < t-g(x)$$

因此 $$\displaystyle \{x \in X~|~ f(x)+g(x)<t \} = \bipcup_{i=1}^\infty (\{x \in X | f(x) < r_i\} \cap \{ x \in X | g(x) < t - r_i \})$$

其中$$\{r_i\}$$是所有有理數形成的集合，因此可得$$\{x \in X~|~ f(x)+g(x)<t \} \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 3</summary>



</details>

### 可測函數序列的性質

> 令$$\{f_k(x)\}$$為集合$$X$$上的可測函數序列，σ，則：
>
> 1. $$\displaystyle \sup_{k \geq 1} \{ f_k(x)\}=\sup\{f_1(x), f_2(x), \dots\}$$為可測函數。
> 2. $$\displaystyle \inf_{k \geq 1} \{ f_k(x)\}=\inf\{f_1(x), f_2(x), \dots\}$$為可測函數。
> 3. $$\displaystyle \limsup_{k \rightarrow \infty} f_k(x) = \inf_{i \geq 1}\{ \sup_{k \geq i} f_k(x)\}$$為可測函數。
> 4. $$\displaystyle \liminf_{k \rightarrow \infty} f_k(x) = \sup_{i \geq 1}\{ \inf_{k \geq i} f_k(x)\}$$為可測函數。

<details>

<summary>proof: 1</summary>





(QED)

</details>

<details>

<summary>proof: 2</summary>

$$\displaystyle \inf_{k \geq 1} \{ f_k(x)\} = - \sup_{k \geq 1} \{ -f_k(x)\} \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 3</summary>



(QED)

</details>

<details>

<summary>proof: 4</summary>

$$\displaystyle \liminf_{k \rightarrow \infty} f_k(x) = - \limsup_{k \rightarrow \infty} -f_k(x) \in \Sigma$$

(QED)

</details>

### 可測函數序列的極限仍為可測函數

> 給定$$\{f_k(x)\}$$為$$X$$上的可測函數，且有 $$\displaystyle \lim_{k \rightarrow \infty} f_k(x)=f(x), ~x \in X$$ 則$$f(x)$$為$$X$$的可測函數。

<details>

<summary>proof: 由可測函數序列的性質得出</summary>

因為$$\{f_k(x)\}$$為$$X$$上的可測函數，所以$$\displaystyle \limsup_{k \rightarrow \infty} f_k(x)$$與 $$\displaystyle \liminf_{k \rightarrow \infty} f_k(x)$$均為可測函數。

因為$$\displaystyle \lim_{k \rightarrow \infty} f_k(x)=f(x)$$，因此可得 $$\displaystyle f(x)=\liminf_{k \rightarrow \infty} f_k(x)=\limsup_{k \rightarrow \infty} f_k(x)$$

因此$$f(x)$$為$$X$$的可測函數 (QED)

</details>

### 可測函數的正成份與負成份函數也為可測函數

> 給定函數$$f$$，定義正成份(positive part)函數$$f^{+}(x)= \left\{ \begin{aligned} &f(x),&\text{if } f(x) > 0, \\ &0 ,& \text{if } f(x) \leq 0 \end{aligned} \right.$$
>
> 負成份(negative part)函數$$f^{-}(x)= \left\{ \begin{aligned} &0,&\text{if } f(x) > 0, \\ &-f(x) ,& \text{if } f(x) \leq 0 \end{aligned} \right.$$
>
> 則$$f$$為可測函數$$\Leftrightarrow$$ $$f^{+}, f^{-}$$為可測函數。

<details>

<summary>proof: 函數等於正成分減去負成份</summary>

$$f(x) = f^{+}(x) - f^{-}(x)$$

若$$f(x)$$在$$X$$為可測函數，可得$$f^{+}(x), f^{-}(x)$$在$$X$$也為可測函數，反之亦然(QED)

</details>

### 可測函數的絕對值為可測函數

> 若$$f$$為可測函數，則$$|f|$$與$$|f|^2$$為可測函數。 註：反之不一定成立

<details>

<summary>proof: 可測函數的線性計算仍為可測函數</summary>

proof $$|f|$$

正成分函數 $$f^{+}=\frac{1}{2}(f+|f|)$$，因此$$|f|=2f^{+} -f$$

因為$$f^{+}, f$$均為可測函數，因此$$|f|$$為可測函數(QED)。

proof $$|f|^2$$

$$|f|^2 = (2f^{+}-f)^2=4f^{+} -2f^{+}\cdot f+f^2$$

因為$$f$$為可測函數，所以$$f^2=f\cdot f$$為可測函數

因為$$f, f^{+}$$為可測函數，所以$$f\cdot f^{+}$$為可測函數

因為$$f^{+}$$為可測函數，所以$$f^{+}$$為可測函數

因為可測函數的線性組合仍為可測函數，因此$$|f|^2$$為可測函數 (QED)

</details>

## 幾乎處處性質(almost everywhere)

> 假設有一集合$$X \subseteq \mathbb{R}^n$$中的點$$x$$相關的命題$$P(x)$$， 若除了$$X$$中的某一個零測度集之外，$$P(x)$$均為真，則稱$$P(x)$$在$$X$$上幾乎處處為真， 並記為$$P(x) ~\text{a.e.} ~x \in X$$。

### 幾乎處處相等

> $$f,g: X \rightarrow \mathbb{R}$$為可測函數，若滿足： $$\displaystyle m(\{x \in X~|~ f(x) \neq g(x) \}) = 0$$， 則稱$$f,g$$在$$X$$幾乎處處相等，記為$$f(x)=g(x)~\text{a.e.} ~x \in X$$。

### 幾乎處處有限

> $$f: X \rightarrow \mathbb{R}$$為可測函數，若有 $$\displaystyle m(\{ x \in X~|~ |f(x)| = \infty \})=0$$， 則稱$$f$$在$$X$$上幾乎處處有限，記為$$|f(x)|<\infty ~ \text{a.e.} ~ x \in X$$。

### 可測函數的幾乎處處相等函數仍可測

> $$f,g: X \rightarrow \overline{R}$$為廣義實值函數，且$$f$$在集合$$X$$可測。
>
> 若$$f(x)=g(x) \text{a.e.} ~ x\ in X$$，則$$g$$在$$X$$可測。
>
> 註：對一可測函數來說，改變其在零測度集合的函數值不會改變函數的可測性。

<details>

<summary>proof:</summary>

令$$S =\{ x \in X ~|~ f(x) \neq g(x)\}$$，則$$m(S) =0$$，且$$X- S$$為可測集。

$$\forall t \in \mathbb{R}$$，可得 $$\{x \in X| g(x) < t\} = \{x \in X-S| g(x) < t\} \cup \{x \in S| g(x) < t\} =\{x \in X-S| f(x) < t\} \cup \{x \in S| g(x) < t\}$$

因為$$f$$在$$X$$可測，所以$$\{x \in X-S| f(x) < t\} \in \Sigma$$。

而m({x \in S| g(x) < t}) = 0，因此可得$$\{x \in X| g(x) < t\} \in \Sigma$$ (QED)

</details>

## 特徵(指示)函數為可測函數

> 集合$$E$$的特徵(指示)函數為$$\chi_E(x)\equiv \mathbb{I}_E(x)= \left\{ \begin{aligned} &1 ~ \text{ if } x \in E, \\ &0 ~ \text{ if } x \notin E \end{aligned} \right.$$
>
> 則$$E$$為可測集合$$\Leftrightarrow \chi_E$$為可測函數。

<details>

<summary>proof: 以定義直接證明</summary>

proof =>:

取$$S \in \mathbb{B}(\mathbb{R})$$，可得$$\chi_E^{-1}(S) = \left\{ \begin{aligned} & X,~ \text{ if } 0, 1 \in S, \\ & E,~ \text{ if } 1 \in S, ~ 0 \notin S, \\ & E^c,~ \text{ if } 1 \notin S, ~ 0 \in S, \\ & \empty, ~ \text{ otherwise } \end{aligned} \right.$$

也可用$$\chi_E^{-1}((-\infty, c))= \left\{ \begin{aligned} & \empty,~ \text{ if } c < 0, \\ & E^c,~ \text{ if } 0 \leq c < 1, \\ & E \cup E^c,~ \text{ if } c \geq 1, \end{aligned} \right.$$

因為$$X, E, E^c, \empty \in \Sigma$$，所以$$\chi_E$$為可測函數 (QED)。

proof <=:

$$\chi_E^{-1}((1/2, \infty))=\{ x\in X ~|~ \chi_{E}(x) > 1/2 \}=E \in \Sigma$$ (QED)

</details>

### 集合序列上極限的特徵函數(可穿過limsup符號)

> 令$$\{E_n\}$$為集合序列，且$$\displaystyle E^{*}=\limsup_{n \rightarrow \infty} E_n \equiv \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k$$，則：
>
> $$\displaystyle \chi_E^{*}(x)=\limsup_{n \rightarrow \infty} \chi_{E_n}(x)$$
