---
description: measurable function
---

# 可測函數

## 可測函數定義

> 函數$$f: X \rightarrow \overline{\mathbb{R}}$$或$$f: X \rightarrow [-\infty, \infty]$$，$$(X, \Sigma)$$為可測空間，$$\overline{\mathbb{R}}=\mathbb{R}\cup\{\pm \infty\}$$為擴充實數集合。
>
> 對於實數上的任意開集合$$E\subseteq \mathbb{R}$$，若前像$$f^{-1}(E)=\{x \in X~|~f(x)\in E\} \in \Sigma$$且$$f^{-1}(\{+\infty\}) \in \Sigma$$，$$f^{-1}(\{-\infty\}) \in \Sigma,$$，則稱$$f$$為可測函數，或稱$$f$$在集合$$E$$上可測。
>
> 或者說 $$\forall t \in \mathbb{R}$$, 集合$$\{x \in X~|~ f(x) \leq t\} \in \Sigma$$，則$$f$$為可測函數。

<mark style="color:blue;">可測函數的值域為擴充實數，且值域任意值的前像集合必須為可測集合，以避免出現有函數值，但沒有定義域元素對應的情形</mark>。

可測函數包含了連續與非連續函數(連續與離散隨機變數)，因此更一般化。

可測函數$$f$$在機率空間$$(X,\mathbb{F}, P)$$中為隨機變數。

<mark style="color:red;">可測函數在極限運算下是封閉的，比連續函數在極限連算時非封閉的性質好</mark>。

### 擴充實數集的計算

* $$x + (\pm \infty )= (\pm \infty) + x = \pm \infty$$。
* $$x - (\pm \infty)=(\mp \infty) -x =\mp \infty$$。
* $$(+\infty) +(+ \infty)=(+\infty) -(- \infty) = + \infty$$。
* $$(-\infty) - (-\infty)=(- \infty) - (+ \infty) = -\infty$$。
* 但是$$(+\infty)+(-\infty)$$、$$(+\infty) - (+\infty)$$與$$(-\infty) - (-\infty)$$未定義。
* $$(\pm \infty)(\pm \infty) = +\infty$$、$$(\pm \infty)(\mp \infty)=-\infty$$。
* $$\forall x \in \mathbb{R}$$，$$\displaystyle x(\pm \infty) =(\pm \infty) x =  \left\{ \begin{aligned} \pm \infty&, \text{ for } x > 0 \\ 0&, \text{ for } x = 0 \\ \mp \infty&, \text{ for } x < 0 \end{aligned} \right.$$，<mark style="color:red;">此處特別約定</mark>$$0 \cdot \pm \infty = 0$$<mark style="color:red;">。</mark>

## 可測函數的等價條件

> $$f: X \rightarrow [-\infty, \infty]$$，則以下條件均等價：
>
> 1. $$f$$為可測函數
> 2. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c))=\{x \in X~|~ f(x)<c \} \in \Sigma$$
> 3. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c])=\{x \in X~|~ f(x)\leq c \} \in \Sigma$$
> 4. $$\forall c \in \mathbb{R}$$，$$f^{-1}((c, \infty))=\{x \in X~|~ f(x)>c \} \in \Sigma$$
> 5. $$\forall \in \mathbb{R}$$，$$f^{-1}([c, \infty))=\{x \in X~|~ f(x) \geq c \} \in \Sigma$$
> 6. $$f^{-1}(B) \in \mathbb{B}$$為Borel set(由實數上所有開(閉)區間形成的最小的σ域)。

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
>
> * 遞增函數：$$a \leq x_1 \leq x_2 \leq b \Rightarrow f(x_1 ) \leq f(x_2)$$。
> * 遞減函數：$$a \leq x_1 \leq x_2 \leq b \Rightarrow f(x_1 ) \geq f(x_2)$$

<details>

<summary>proof:</summary>

$$\forall t \in \mathbb{R}$$, 集合 $$E= \{ x \in [a,b] ~|~ f(x)<t \}$$必為以下三種集合之一： (半開或閉)區間、單點集合或空集合。

因此$$E$$為可測集 (QED)

</details>

## \[證明常用] 將開(閉)區間表示為可數個集合的聯集與交集

> 函數$$f: E \rightarrow [-\infty, \infty]$$為在集合$$E$$上的可測函數，則：
>
> * $$\displaystyle \{x \in E~|~ f(x)=\infty\} = \bigcap_{k=1}^\infty \left\{x\in E ~|~ f(x) > k\right\} = E- \displaystyle \{x \in E~|~ f(x)<\infty\}$$。
> * $$\displaystyle \{x \in E~|~ f(x) < \infty\} = \bigcup_{k=1}^\infty \left\{x\in E ~|~ f(x) <k \right\}$$。
> * $$\displaystyle \{x \in E~|~ f(x) > - \infty\} = \bigcup_{k=1}^\infty \left\{x\in E ~|~ f(x) >-k \right\}$$。
> * $$\displaystyle \{x \in E~|~ f(x)=-\infty\}  = E - \displaystyle \{x \in E~|~ f(x) > -\infty\}$$
> * $$\displaystyle \{x \in E~|~ f(x)\geq t\} = \bigcap_{k=1}^\infty \left\{x\in E ~|~ f(x) > t-\frac{1}{k}\right\}$$。
> * $$\displaystyle \{x \in E~|~ f(x) >  t\} =\bigcup_{k=1}^\infty \{x\in E ~|~ f(x) \geq t+\frac{1}{k} \}= E - \{x \in E~|~ f(x) \leq t\}$$。
> * $$\displaystyle \{x \in E~|~ f(x)\leq t\} = \bigcap_{k=1}^\infty \left\{x\in E ~|~ f(x) < t+\frac{1}{k}\right\} = E - \displaystyle \{x \in E~|~ f(x)> t\}$$。
> * $$\displaystyle \{x \in E~|~ f(x) < t \} =\bigcup_{k=1}^\infty \{x\in E ~|~ f(x) \leq t-\frac{1}{k}\}= E - \{x \in E~|~ f(x) \geq t \}$$。
> * $$\displaystyle \{x \in E~|~ f(x) = t \} = \displaystyle \{x \in E~|~ f(x) \geq t \} \cap \displaystyle \{x \in E~|~ f(x) \leq t \}$$

* 令$$S_m=\{x \in E ~|~ |f(x) - g(x)| \geq 1/m\}, ~m\in \mathbb{N}$$, $$S=\{x\in E ~|~ f(x) \neq g(x)\}$$，可得$$\displaystyle S= \bigcup_{m=1}^\infty S_m$$
* $$\displaystyle [a,b]=\bigcap_{k=1}^\infty (a-\frac{1}{k}, b+\frac{1}{k})$$ \[由外部交集夾擠，開區間改成閉區間也成立]

<details>

<summary>proof</summary>

\=>

因為$$[a,b] \subseteq (a-1/k, b+1/k), \forall k \in \mathbb{N}$$，因此$$[a,b] \subseteq \bigcap_{k=1}^\infty (a-1/k, b+1/k)$$--(1)

\[QED]

<=

要證明$$[a,b] \supseteq \bigcap_{k=1}^\infty (a-1/k, b+1/k)$$--(2)

令$$x \notin [a,b]$$，即$$x<a$$或$$x >b$$。如果可得$$x \notin \bigcap_{k=1}^\infty (a-1/k, b+1/k)$$時，則可證明(2)。

\[反證法]假設$$x \notin [a,b]$$且$$x \in \bigcap_{k=1}^\infty (a-1/k, b+1/k)$$--(3)。

* 由(3)可得$$a-\frac{1}{k} < x  < a, ~ \forall k \in \mathbb{N}$$，但實數中不存在滿足此條件的$$x$$，因此(3)矛盾，即$$\exists k_0 \in \mathbb{N} \ni a-\frac{1}{k_0} \le x < a$$，因此存在$$x \notin (a-1/k_0, b+1/k_0)$$--(4)
* 同理可得$$b < x < b+\frac{1}{k}, \forall k \in \mathbb{N}$$，但實數中不存在滿足此條件的$$x$$，因此(3)矛盾，即$$\exists k_0 \in \mathbb{N} \ni b < x \leq b+ \frac{1}{k_0}$$--(5)

由(4,5)得假設$$x \notin [a,b]$$=>$$x \notin \bigcap_{k=1}^\infty (a-1/k, b+1/k)$$(QED)

註：開區間$$(a-\frac{1}{k}, b+\frac{1}{k})$$改為$$[a-\frac{1}{k}, b+\frac{1}{k}]$$時也成立。

因為(1)仍然成立。而(3)可得 $$a-\frac{1}{k} \leq x < a, ~\forall k \in \mathbb{N}$$但實數中不存在滿足此條件的$$x$$，因此(3)矛盾，即$$\exists k_0 \in \mathbb{N} \ni a-\frac{1}{k_0} \le x < a$$--(6)

同樣可得$$\exists k_0 \in \mathbb{N} \ni b < x \leq b+ \frac{1}{k_0}$$--(7)

由(4,5)得假設$$x \notin [a,b]$$=>$$x \notin \bigcap_{k=1}^\infty [a-1/k, b+1/k]$$(QED)

</details>

* $$\displaystyle (a,b)=\bigcup_{k=1}^\infty [a+\frac{1}{k}, b-\frac{1}{k}]$$ \[由內部聯集擴充，閉區間改為開區間也成立].&#x20;

<details>

<summary>proof</summary>

因為$$\exists k \ni \mathbb{N}\ni[a+1/k, b-1/k] \subseteq (a,b)$$，所以$$\displaystyle (a,b)\supseteq \bigcup_{k=1}^\infty [a+\frac{1}{k}, b-\frac{1}{k}]$$--(1)

要證明$$\displaystyle (a,b) \subseteq \bigcup_{k=1}^\infty [a+\frac{1}{k}, b-\frac{1}{k}]$$--(2)

令$$x \in (a,b)$$，即$$a < x < b$$。

由Archmedian property得$$\exists k_a \in \mathbb{N}\ni  a < a+1/k_a <x$$。

同理可得$$\exists K_b \in \mathbb{N} \ni x < b-1/k_b < b$$。

取$$k_0 = \max(k_a, k_b)$$，可得$$x \in (a+1/k_0, b-1-k_0) \subseteq [a+1/k_0, b-1-k_0]$$，因此(2)成立

(QED)

</details>

* $$\displaystyle (-\infty, \infty)=\bigcup_{n=\infty}^\infty (n, n+1)$$
* 單點集 $$\displaystyle \{a\}=\bigcap_{k=1}^\infty(a-\frac{1}{k}, a+\frac{1}{k})$$。可想成$$B_a(\frac{1}{k})=\{ x\in \mathbb{R}~|~ |x-a|<\frac{1}{k}\}$$

[https://math.stackexchange.com/questions/323327/open-interval-written-as-countable-union-of-closed-intervals](https://math.stackexchange.com/questions/323327/open-interval-written-as-countable-union-of-closed-intervals)

[https://math.stackexchange.com/questions/2869734/show-that-a-b-bigcap-n-1-infty-a-1-n-b1-n](https://math.stackexchange.com/questions/2869734/show-that-a-b-bigcap-n-1-infty-a-1-n-b1-n)

### 個別可測集合的函數的聯集仍為可測函數

> 給定函數$$f: X_1 \cup X_2 \rightarrow \mathbb{\overline{R}}$$，若$$f$$在 $$X_1$$可測，且在$$X_2$$也可測， 則在$$X_1 \cup X_2$$也可測。

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
> 2. $$f(x) \pm g(x)$$ 為可測函數。
> 3. $$f(x)g(x)$$為可測函數。
> 4. $$h(x)=\max\{f(x), g(x)\}$$為可測函數。
> 5. $$h(x)=\min\{f(x), g(x)\}$$為可測函數。
>
> 註：<mark style="color:blue;">上述計算性質對於取值為擴充實數的可測函數也成立</mark>，只要考慮$$\{x~|~ f(x)=\infty\}$$，$$\{x~|~ g(x)=\infty\}$$，$$\{x~|~ f(x)=-\infty\}$$，$$\{x~|~ g(x)=-\infty\}$$均為可測集合即可。

<details>

<summary>proof: 1</summary>

令$$\Sigma$$為$$X$$的σ域。

因為$$f$$為可測函數，所以 $$\forall d \in \mathbb{R}, f^{-1}((-\infty, d)) \in \Sigma$$

若$$c >0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}((-\infty, cd)) \in \Sigma$$--(1)

若$$c <0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}((cd, \infty)) \in \Sigma$$--(2)

若$$c =0$$，可得$$f^{-1}(c(-\infty, d))=f^{-1}(\{0\}) \in \Sigma$$--(3)

由(1,2,3)得$$cf(x)$$為可測函數 (QED)

</details>

<details>

<summary>proof: 2</summary>

[https://math.stackexchange.com/questions/541118/proving-that-sum-of-two-measurable-functions-is-measurable](https://math.stackexchange.com/questions/541118/proving-that-sum-of-two-measurable-functions-is-measurable)

$$f(x)+g(x) <t \Leftrightarrow f(x) < t- g(x) \Leftrightarrow  \exists r \in \mathbb{Q} \ni f(x) < r <t-g(x)$$。

因為$$\mathbb{Q}$$dense in $$\mathbb{R}$$，且取有理數是因為有理數集合內的元素為可數個。

令$$\Sigma$$為$$X$$的σ域。

$$\forall t \in \mathbb{R}$$，因為$$f(x) + g(x) <t$$就是$$f(x) < t-g(x)$$

因此 $$\displaystyle \{x \in X~|~ f(x)+g(x)<t \} = \bigcup_{i=1}^\infty (\{x \in X | f(x) < r_i\} \cap \{ x \in X | g(x) < t - r_i \})$$

其中$$\{r_i\}$$是所有有理數形成的集合，因此可得$$\{x \in X~|~ f(x)+g(x)<t \} \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 3</summary>

$$fg=\frac{1}{2}[(f+g)^2 -f^2 - g^2]$$

因為已經證明可測函數相加減仍為可測函數，因此只要證明$$f^2$$為可測函數即可。

$$\forall t \geq 0$$，可得$$\{x\in X ~|~ f^2(x) >t\} = \{x\in X ~|~ f(x) > \sqrt{t} \} \cup \{x\in X ~|~ f(x) < - \sqrt{t}\}$$

而當$$t <0$$時，可得$$\{x\in X ~|~ f^2(x) >t\} = X$$

因此$$f^2$$為可測函數(QED)

</details>

<details>

<summary>proof 4</summary>

$$\forall c \in \mathbb{R}$$，可得$$\{x \in X ~|~ \max\{f(x), g(x)\}<c\}=\{x \in X ~|~ f(x) < c\} \cup \{x \in X ~|~ g(x) < c\}$$

因為$$f,g$$為可測函數，因此$$\{x \in X | f(x) < c\} \in \Sigma$$且$$\{x \in X | (x) < c\} \in \Sigma$$

由σ域的定義得$$\{x \in X | \max\{f(x), g(x)\}<c\} \in \Sigma$$ (QED)

</details>

<details>

<summary>proof 5</summary>

$$\forall c \in \mathbb{R}$$，可得$$\{x \in X ~|~ \min\{f(x), g(x)\}<c\}=\{x \in X ~|~ f(x) < c\} \cap \{x \in X ~|~ g(x) < c\}$$

因為$$f,g$$為可測函數，因此$$\{x \in X | f(x) < c\} \in \Sigma$$且$$\{x \in X | (x) < c\} \in \Sigma$$

由σ域的定義得$$\{x \in X | \min\{f(x), g(x)\}<c\} \in \Sigma$$ (QED)

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

已知$$\{x \in X ~|~ \sup\{f(x), g(x)\}<c\}=\{x \in X ~|~ f(x) < c\} \cup \{x \in X ~|~ g(x) < c\}$$

由數學歸納法得 $$\displaystyle \{x \in X ~|~ \sup_{k \geq 1} \{ f_k(x)\} > t \} = \bigcup_{k=1}^\infty \{x \in X ~|~  f_k(x) > t \} \in \Sigma$$

(QED)

</details>

<details>

<summary>proof: 2</summary>

$$\displaystyle \inf_{k \geq 1} \{ f_k(x)\} = - \sup_{k \geq 1} \{ -f_k(x)\} \in \Sigma$$ (QED)

</details>

<details>

<summary>proof: 3</summary>

$$\displaystyle \limsup_{k \rightarrow \infty} f_k(x) = \inf_{i \geq 1}\{ \sup_{k \geq i} f_k(x)\}$$

由1,2的性質得證

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

<summary>proof: 函數等於正成分減去負成份，可參考符號測度</summary>

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

### 可測函數若且唯若任意開集合的前像為可測集合

> $$f$$為定義在可測集合$$E$$，則：
>
> $$f$$在$$E$$上可測 $$\Leftrightarrow$$ $$O$$為值域的任意開集合，其前像$$f^{-1}(O)=\{x \in E~|~ f(x) \in O\}$$為可測集合。

<details>

<summary>proof</summary>

<= 若任意開集合的前像均為可測集合，因此可知開區間$$(c, \infty)$$為可測集，得$$f^{-1}(c, \infty) \in \Sigma$$，因此$$f$$為可測函數(QED)。

\=>



</details>

### 可測函數的σ域為全局σ域的子集

> $$(X, \mathcal{F})$$為可測空間，$$f: \mathcal{F} \rightarrow \mathbb{R}$$為可測函數，則$$\sigma(f) \subseteq \mathcal{F}$$。
>
> 若$$(\Omega, \Sigma)$$為可測機率空間，$$X: \Sigma\rightarrow \mathbb{R}$$為隨機變數，則$$\sigma(X) \subseteq \Sigma$$。
>
> 即可測函數的資訊量小於等於全局的資訊量。
>
> <mark style="color:red;">此性質常用於隨機過程中的filitration</mark> $$\mathcal{F}_t$$<mark style="color:red;">，當</mark>$$X$$<mark style="color:red;">為</mark>$$\mathcal{F}_t$$<mark style="color:red;">可測時，則</mark>$$\sigma(X) \subseteq \mathcal{F}_t$$。



### 可測函數的複合函數為原函數σ域的子集

> $$(X, \mathcal{F})$$為可測空間，$$f: \mathcal{F} \rightarrow \mathbb{R}$$為可測函數, $$g: \mathbb{R} \rightarrow \mathbb{R}$$為可測函數，則$$\sigma(g\circ f) \subseteq \sigma(f)$$。
>
> 若$$(\Omega, \Sigma)$$為可測機率空間，$$X: \Sigma\rightarrow \mathbb{R}$$為隨機變數，$$g: \mathbb{R} \rightarrow \mathbb{R}$$為可測函數，則$$\sigma(g(X)) \subseteq \sigma(X)$$。
>
> 即函數$$g$$無法提供比$$X$$的結構更多的資訊。

### 連續函數與可測函數的合成函數為可測函數

> $$f: \mathbb{R} \rightarrow \mathbb{R}$$為連續函數且$$g: E \rightarrow [-\infty, \infty]$$為可測函數，則合成函數$$g \circ f(x) \equiv f(g(x))$$為可測函數。

## 幾乎處處性質(almost everywhere)

> 假設有一集合$$X \subseteq \mathbb{R}^n$$中的點$$x$$相關的命題$$P(x)$$， 若除了$$X$$中的某一個零測度集之外，$$P(x)$$均為真，則稱$$P(x)$$在$$X$$上幾乎處處為真， 並記為$$P(x) ~\text{a.e.} ~x \in X$$。

### 幾乎處處相等

> $$f,g: X \rightarrow [-\infty, \infty]$$為可測函數，若滿足： $$\displaystyle m(\{x \in X~|~ f(x) \neq g(x) \}) = 0$$， 則稱$$f,g$$在$$X$$幾乎處處相等，記為$$f(x)=g(x)~\text{a.e.} ~x \in X$$。

### 幾乎處處有限

> $$f: X \rightarrow [-\infty, \infty]$$為可測函數，若有 $$\displaystyle m(\{ x \in X~|~ |f(x)| = \infty \})=0$$， 則稱$$f$$在$$X$$上幾乎處處有限，記為$$|f(x)|<\infty ~ \text{a.e.} ~ x \in X$$。

<mark style="color:red;">註：幾乎處處有限不保證有界</mark>，例如$$f(x)=x, ~ x \in \mathbb{R}$$，可得$$m(\{x \in \mathbb{R}~|~ f(x)=\infty\})=0$$，但非有界函數。

### 可測函數的幾乎處處相等函數仍可測

> $$f,g: X \rightarrow [-\infty, \infty]$$為廣義實值函數，且$$f$$在集合$$X$$可測。
>
> 若$$f(x)=g(x) \text{a.e.} ~ x\in X$$，則$$g$$在$$X$$可測。
>
> 註：<mark style="color:red;">對一可測函數來說，改變其在零測度集合的函數值不會改變函數的可測性</mark>。

<details>

<summary>proof:</summary>

令$$S =\{ x \in X ~|~ f(x) \neq g(x)\}$$，則$$m(S) =0$$，且$$X- S$$為可測集。

$$\forall t \in \mathbb{R}$$，可得 $$\{x \in X| g(x) < t\} = \{x \in X-S| g(x) < t\} \cup \{x \in S| g(x) < t\} =\{x \in X-S| f(x) < t\} \cup \{x \in S| g(x) < t\}$$

因為$$f$$在$$X$$可測，所以$$\{x \in X-S| f(x) < t\} \in \Sigma$$。

而$$m({x \in S| g(x) < t}) = 0$$，因此可得$$\{x \in X| g(x) < t\} \in \Sigma$$ (QED)

</details>

##
