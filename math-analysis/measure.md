# 測度\(measure\)

## 簡介

* 在此討論的是測度應具有的性質，只要符合測度定義的函數均可視為測度。
* 測度是將集合至正實數的函數。

## 測度\(measure\)

> 給定集合$$X$$，$$Σ$$為定義在$$X$$上的[sigma-field](set/field-and-sigma-field.md#sigmafieldsigmaalgebra-yu-ke-ce-kong-jian)。
>
> * 定義函數$$μ: \Sigma \rightarrow [0, \infty]$$（可為無窮大）滿足以下兩個條件：
>
>   *  \[空集合的測度為0\] $$\mu(\emptyset)=0$$
>   *  \[countable additive, 互斥集合聯集的測度等於各別集合測度的加總\] $$\displaystyle \mu(\cup_{n=1}^{\infty}E_n) =\sum_{n=1}^{\infty}\mu (E_n), ~ E_n \in \Sigma $$且$$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$
>
>   測度是測量給定集合內元素個數的方法。

* 測度的定義域是在$$\Sigma$$上，而不是在原始的集合$$X$$，因為如果從$$X$$取出任意的結果$$\omega$$，可依公理建構出不可測的集合$$E$$，但是不可測的集合在實際應用上幾乎不存在，為了理論的嚴謹性，所以要求測度的定義域是在可測的集合，即$$\Sigma$$中的任意集合。
* 同理函數$$f: X\rightarrow \mathbb{R}$$雖然定義域是在一般集合$$X$$中，但是如果任意由值域得到的前像$$f^{-1}$$集合均為$$\Sigma$$中的元素時，則稱為可測函數，否則為不可測函數。
* 註：測度之值在此定義為正實數，但之後可放寬為任意實數\(如負值\)或複數。
* **註: 只要再加上第三個條件**$$\displaystyle \sum_{n=1}^\infty \mu( E_n) =1$$**的條件時，則為機率測度**。

#### 範例

* 在實數$$\mathbb{R}$$上常數的測度有Lebesgue measure 
  * $$\mu([a,b])=\mu([a,b))=\mu((a,b])=\mu((a,b))=|b−a|$$。
  *  $$\mu([a,\infty))=\mu((a,\infty))=\mu((−\infty,b])=\mu((−\infty,b))=\infty$$
* 自然數或整數上的測度有counting measure $$\mu([1,2,3,4,5])=\#([1,2,3,4,5])=5$$。
* 平面空間$$\mathbb{R}^2$$ 上的測度為面積。
* 立體空間$$\mathbb{R}^3$$ 的測度為體積。
* 函數空間的情形較為複雜，因此並非所有函數都存在測度函數可量測其值，因此必須先定義出可測函數後，才可定義測度。
* Dirac measure: 令$$x_0 \in X$$, $$\delta(x_0, E)=\left\{  \begin{align} &1, \text{ if } x_0 \in E \\ &0, \text{ otherwise} \end{align} \right.$$

### 測度的性質

> * \[可加性 ,additive\] $$\forall E,F \in Σ$$, $$E \cap F=\emptyset \Rightarrow \mu( E ∪F)=\mu(E)+\mu(F)$$
> * \[有限可加性 finitely additive\] $$\forall E_1,E_2,\ldots,E_n \in \Sigma$$, $$E_i \cap E_j=\emptyset, ~ \forall i \neq j $$ $$\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i)= \sum_{i=1}^n \mu(E_i)$$

* 由測度的定義可直接得出。

> \[子集合的測度\] $$ \forall E, F \in \Sigma,  E \subseteq F \Rightarrow \mu (E) \leq \mu(F)$$

proof:

* 因為$$E \subseteq F$$，可得 $$F = E \cup (F -E)$$。
* 由測度定義得 $$\mu(F) = \mu (E) + \mu (F-E)$$且$$\mu(F-E) \geq 0$$。
* 因此$$\mu(E) \leq \mu(F)$$ \(QED\)

> * \[次可加性 ,sub-additive\] $$\forall E,F \in \Sigma, ~\mu(E \cup F) \leq \mu(E)+\mu(F)$$
> * \[有限次可加性, finitely sub-additive\] $$\forall E_1,E_2, \ldots,E_n \in \Sigma$$$$\displaystyle \Rightarrow \mu(\bigcup_{i=1}^n E_i ) \leq \sum_{i=1}^n\mu(E_i ) $$
> * \[可數次可加性, countable sub-additive\] $$\forall E_1,E_2, \ldots \in \Sigma$$$$\Rightarrow \mu(\cup_{i=1}^\infty E_i ) \leq \sum_{i=1}^\infty \mu(E_i)$$

proof:

* $$E \cup F = E \cup (F - E)$$
* 由測度定義得 $$\mu(E \cup F) = \mu(E) + \mu(F-E)$$
* 因為$$F-E \subseteq F$$可得$$\mu(F-E) \leq \mu(F)$$
* 因此 $$\mu(E \cup F) \leq \mu (E) +\mu(F)$$ \(QED\)

### 有限測度與sigma有限測度

> 如果對宇集合可得$$\mu(X)<\infty$$，則稱$$\mu$$為有限測度（finite measure）。

* $$\mu(\mathbb{R})=\infty$$，因此實數的長度不是有限測度。
* 所有的機率測度都是有限測度，因為$$\mu(\Omega) =1$$。

> \[sigma-finite measure\] $$\exists \{E_n \}\subseteq \Sigma, ~ X=\bigcup_n E_n  \ni \mu(E_n )< \infty, ~ \forall n$$

* 實數的長度不是有限測度，但實數的長度是sigma有限測度，因為可將實數拆解為多個有限長度的線段的聯集。$$\mathbb{R} = \cdots \cup [-n, -n+1] \cup \cdots \cup[-1,1]\cup [1,2]\cup \cdots \cup [n, n+1] \cup \cdots$$且$$\mu([n, n+1])=1, \forall n$$。





