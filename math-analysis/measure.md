# 測度\(measure\)

## 簡介

* 在此討論的是測度應具有的性質，只要符合測度定義的函數均可視為測度。
* 測度是將集合至正實數的函數。

## 測度\(measure\)

> 給定集合$$X$$，$$Σ$$為定義在$$X$$上的[sigma-field](set/field-and-sigma-field.md#sigmafieldsigmaalgebra-yu-ke-ce-kong-jian)。
>
> * 定義函數$$μ: \Sigma \rightarrow [0, \infty]$$ \(可為無窮大\)滿足以下兩個條件：
>   *  \[空集合的測度為0\] $$\mu(\emptyset)=0$$
>   *  \[countable additive, 互斥集合聯集的測度等於各別集合測度的加總\] $$\displaystyle \mu(\cup_{n=1}^{\infty}E_n) =\sum_{n=1}^{\infty}\mu (E_n), ~ E_n \in \Sigma $$且$$E_i \cap E_j=\emptyset, ~ \forall i \neq j$$

* 註：測度之值在此定義為正實數，但之後可放寬為任意實數\(如負值\)或複數。
* **註: 只要再加上第三個條件**$$\displaystyle \sum_{n=1}^\infty \mu( E_n) =1$$**的條件時，則為機率測度**。

#### 範例

* 在實數$$\mathbb{R}$$上常數的測度有Lebesgue measure 
  * $$\mu([a,b])=\mu([a,b))=\mu((a,b])=\mu((a,b))=|b−a|$$。
  *  $$\mu([a,\infty))=\mu((a,\infty))=\mu((−\infty,b])=\mu((−\infty,b))=\infty$$。
* 自然數或整數上的測度有counting measure $$\mu([1,2,3,4,5])=\#([1,2,3,4,5])=5$$。
* 平面空間$$\mathbb{R}^2$$ 上的測度為面積。
* 立體空間$$\mathbb{R}^3$$ 的測度為體積。
* 函數空間的情形較為複雜，因此並非所有函數都存在測度函數可量測其值，因此必須先定義出可測函數後，才可定義測度。
* Dirac measure: 令$$x_0 \in X$$, $$\delta(x_0, E)=\left\{  \begin{align} &1, \text{ if } x_0 \in E \\ &0, \text{ otherwise} \end{align} \right.$$

### 測度的性質

> * \[additive\] $$\forall E,F \in Σ$$, $$E \cap F=\emptyset \Rightarrow \mu( \cup ∪F)=\mu(E)+\mu(F)$$
> * \[finitely additive\] $$\forall E_1,E_2,\ldots,E_n \in \Sigma$$, $$E_i \cap E_j=\emptyset, ~ \forall i \neq j $$ $$\Rightarrow \mu(\cup_{i=1}^n E_i)= \sum_{i=1}^n \mu(E_i)$$
> * \[sub-additive\] $$\forall E,F \in \Sigma, \mu(E \cup F) \leq \mu(E)+\mu(F)$$
> * \[finitely sub-additive\] $$\forall E_1,E_2, \ldots,E_n \in \Sigma$$$$\Rightarrow \mu(\cup_{i=1}^n E_i ) \leq \sum_{i=1}^n\mu(E_i ) $$
> * \[countable sub-additive\] $$\forall E_1,E_2, \ldots \in \Sigma$$$$\Rightarrow \mu(\cup_{i=1}^\infty E_i ) \leq \sum_{i=1}^\infty \mu(E_i)$$
>
>
>
> * \[finite measure\] $$\mu(X)<\infty$$
> * \[sigma-finite measure\] $$\exists \{E_n \}\subseteq \Sigma, ~ X=\cup_n E_n  \ni \mu(E_n )< \infty, ~ \forall n$$

* $$\mu(\mathbb{R})=\infty$$, 因此實數的長度不是finite measure。
* 但實數的長度是sigma−finite measure，因為可將實數拆解為多個有限長度的線段的聯集 $$\mathbb{R} = \cdots \cup [-n, -n+1] \cup \cdots \cup[-1,1]\cup [1,2]\cup \cdots \cup [n, n+1] \cup \cdots$$且$$\mu([n, n+1])=1, \forall n$$。





