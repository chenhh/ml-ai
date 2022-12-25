---
description: measurable function
---

# 可測函數

## 可測函數定義

> 函數$$f: X \rightarrow \overline{\mathbb{R}}$$，$$(X, \Sigma)$$為可測空間，$$\overline{\mathbb{R}}=\mathbb{R}\cup\{\pm \infty\}$$為擴充實數集合。
>
> 對於實數上的任意開集合$$E\subseteq \mathbb{R}$$，若前像$$f^{-1}(E)=\{x \in X~|~f(x)\in E\} \in \Sigma$$且$$f^{-1}(\{+\infty\}) \in \Sigma$$，$$f^{-1}(\{-\infty\}) \in \Sigma,$$，則稱$$f$$為可測函數，或稱$$f$$在集合$$E$$上可測。

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

<summary>proof: 1-> 2 </summary>

因為$$f$$為可測函數，由定義得給定$$c \in \mathbb{R}$$，$$f^{-1}(c) \in \Sigma$$，同理$$\forall d < c$$，$$f^{-1}(d) \in \Sigma$$。

因為$$\Sigma$$定義集合內任意元素的聯集仍為$$\Sigma$$內的元素，因此$$f^{-1}(c \cup d) \in \Sigma$$ (QED)

</details>



<details>

<summary>proof:  2->3，用開區間逼近閉區間 </summary>

$$(-\infty, c]=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})$$

由$$\Sigma$$的定義得$$f^{-1}((-\infty, c])=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})\in \Sigma$$ (QED)

</details> 



<details>

<summary>proof: 3->4，補集 </summary>

$$f^{-1}((c, \infty))=f^{-1}((\mathbb{R} - (-\infty, c])=\mathbb{R}-f^{-1}((-\infty, c]) \in \Sigma$$ (QED)

</details> 



<details>

<summary>proof: 4->5，用開區間逼近閉區間 </summary>

$$f^{-1}([c, \infty)=f^{-1}(\bigcap_{n=1}^\infty (c - \frac{1}{n}, \infty))=\bigcap_{n=1}^\infty f^{-1}(c-\frac{1}{n}, \infty) \in \Sigma$$ (QED)

</details> 



<details>

<summary>proof: 5->6 </summary>

令$$S = \{A \subseteq \mathbb{R}, ~f^{-1}(A) \in \Sigma \}$$，檢驗Borel set $$\mathbb{B} \subseteq S$$。

由5得$$\forall c \in \mathbb{R}, [c, \infty) \subseteq S$$，且由1得$$\forall d \in \mathbb{R}, ~(-\infty, d) \subseteq S$$，還可得$$\forall e \in \mathbb{R}, (e, \infty) \subseteq S$$。

因此$$(e,d) \subseteq S$$，包含了實數上的任意開區間，因此$$\mathbb{B} \subseteq S$$ (QED)。

</details> 



<details>

<summary>proof: 6->1 </summary>

依可測函數定義可得(QED)

</details> 



## 特徵(指示)函數為可測函數

> 集合$$E$$的特徵(指示)函數為$$\chi_E(x)\equiv \mathbb{I}_E(x)= \left\{ \begin{aligned}  &1 ~ \text{ if } x \in E, \\ &0 ~ \text{ if } x \notin E  \end{aligned} \right.$$
>
> 則$$E$$為可測集合$$\Leftrightarrow \chi_E$$為可測函數。

proof =>:&#x20;

取$$S \in \mathbb{B}(\mathbb{R})$$，可得$$\chi_E^{-1}(S) = \left\{ \begin{aligned} & X,~ \text{ if } 0, 1 \in S, \\ & E,~ \text{ if } 1 \in S, ~ 0 \notin S, \\ & E^c,~ \text{ if } 1 \notin S, ~ 0 \in S, \\ & \empty, ~ \text{ otherwise } \end{aligned} \right.$$

也可用$$\chi_E^{-1}((-\infty, c))= \left\{ \begin{aligned} & \empty,~ \text{ if } c < 0, \\ & E^c,~ \text{ if } 0 \leq c < 1, \\ & E \cup E^c,~ \text{ if } c \geq 1,  \end{aligned} \right.$$

因為$$X, E, E^c, \empty \in \Sigma$$，所以$$\chi_E$$為可測函數 (QED)。

proof <=:

$$\chi_E^{-1}((1/2, \infty))=\{ x\in X ~|~ \chi_{E}(x) > 1/2 \}=E \in \Sigma$$ (QED)

## 集合序列上極限的特徵函數(可穿過limsup符號)

> 令$$\{E_n\}$$為集合序列，且$$\displaystyle E^{*}=\limsup_{n \rightarrow \infty} E_n \equiv \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty E_k$$，則：
>
> $$\displaystyle \chi_E^{*}(x)=\limsup_{n \rightarrow \infty} \chi_{E_n}(x)$$

## 可測函數的正成份與負成份函數也為可測函數

> 給定函數$$f$$，定義正成份(positive part)函數$$f^{+}(x)= \left\{ \begin{aligned} &f(x),&\text{if } f(x) > 0, \\ &0 ,& \text{if } f(x) \leq 0  \end{aligned} \right.$$
>
> 負成份(negative part)函數$$f^{-}(x)= \left\{ \begin{aligned} &0,&\text{if } f(x) > 0, \\ &-f(x) ,& \text{if } f(x) \leq 0  \end{aligned} \right.$$
>
> 則$$f$$為可測函數$$\Leftrightarrow$$ $$f^{+}, f^{-}$$為可測函數。

## 可測函數的絕對值為可測函數

> 若$$f$$為可測函數，則$$|f|$$與$$|f|^2$$為可測函數。

proof: 可測函數的線性計算仍為可測函數

正成分函數 $$f^{+}=\frac{1}{2}(f+|f|)$$，因此$$|f|=2f^{+} -f$$

因為$$f^{+}, f$$均為可測函數，因此$$|f|$$為可測函數(QED)。

proof:

$$|f|^2 = (2f^{+}-f)^2=4f^{+} -2f^{+}\cdot f+f^2$$

因為$$f$$為可測函數，所以$$f^2=f\cdot f$$為可測函數

因為$$f, f^{+}$$為可測函數，所以$$f\cdot f^{+}$$為可測函數

因為$$f^{+}$$為可測函數，所以$$f^{+}$$為可測函數

因為可測函數的線性組合仍為可測函數，因此$$|f|^2$$為可測函數 (QED)
