# 集合的特徵函數

## 集合的特徵函數

## 集合的特徵函數(指示函數)(characteristic function, indicator function)

> 給定集合$$E \subseteq X$$。定義特徵函數 $$\chi_E:X \rightarrow \mathbb{R}$$(對應域為實數可便於定義可測函數，但值域只有$$\{0,1\}$$）$$\chi_E (x)=\left \{ \begin{align} &1, \text { if } x \in E, \\ &0, \text{ if } x \notin E \end{align} \right.$$
>
> * 因為$$\chi_E$$為函數，因此也可以考慮函數的極限。在分析中也常用$$I_E$$的符號表示。
> * <mark style="color:red;">特徵函數最重要的功能是可以用函數的方式自訂集合的範圍</mark>。

* 特徵函數是可測函數（隨機變數）。特徵函數在討論機率的條件期望值時經常使用，因為可將隨機變數以函數的方式定義在特定的集合中。例如$$\mathrm{E}(I_A(\omega))=\mathrm{P}(A)$$。
* 特徵函數另一個常用的用途是定義Riemann積分: $$\displaystyle f = \sum_{k=1}^n \alpha_k\chi_{R_k}$$(step function)，其中每一個$$R_k$$都是矩形。定義Lebesgue積分$$\displaystyle f = \sum_{k=1}^n \alpha_k\chi_{E_k}$$(simple function), $$E_k$$為$$\alpha_k$$的前像集合。

#### 性質

> 當$$E=X$$時，$$\chi_E(x)\equiv 1$$
>
> 當$$E=\emptyset$$時，$$\chi_E(x)\equiv 0$$
>
> $$E_1 \subseteq E_2 \Leftrightarrow \chi_{E_1}(x) \subseteq \chi_{E_2}(x)$$
>
> $$E_1 = E_2 \Leftrightarrow \chi_{E_1}(x) =\chi_{E_2}(x)$$

#### 聯集與交集的特徵函數

> $$A,B \subseteq X$$，則
>
* $$\chi_{A \cap B}= \min\{ \chi_A, \chi_B\}=\chi_A\chi_B$$
* $$\chi_{A\cup B}=\max\{ \chi_A, \chi_B\}=\chi_A +\chi_B-\chi_A \chi_B$$
* $$\displaystyle \chi_{\bigcup_{i \in I} A_i}(x) = \max_{i \in I}\chi_{A_i} (x)$$
* $$\displaystyle \chi_{\bigcap_{i \in I} A_i}(x) = \min_{i \in I}\chi_{A_i} (x)$$

* $$\chi_{A\cap B}= \left\{\begin{aligned}1, &\text{ if } x \in A \cap B\\ 0, &\text{ if } x \notin A \cap B \end{aligned} \right.$$
  * if $$x \in A \land x \in B$$, $$\min\{ \chi_A, \chi_B\}=1, \chi_A, \chi_B=1$$
  * if $$x \in A \land x \notin B$$, $$\min\{ \chi_A, \chi_B\}=0, \chi_A, \chi_B=0$$
  * if $$x \notin A \land x \in B$$, $$\min\{ \chi_A, \chi_B\}=0, \chi_A, \chi_B=0$$
  * if $$x \notin A \land x \notin B$$, $$\min\{ \chi_A, \chi_B\}=0, \chi_A, \chi_B=0$$

#### 特徵函數在集合序列的極限(點態收斂)

> * $$\displaystyle \limsup_{n \rightarrow \infty}\chi_{E_n} =\chi_{\limsup_{n \rightarrow \infty} E_n}$$(特徵函數可穿過$$\limsup$$，函數序列極限等於集合序列極限)
> *   $$\displaystyle \liminf_{n \rightarrow \infty}\chi_{E_n} =\chi_{\liminf_{n \rightarrow \infty} E_n}$$(特徵函數可穿過$$\liminf$$，函數序列極限等於集合序列極限)
>
>     註：$$\displaystyle \limsup_{n \rightarrow \infty}\chi_{E_n }$$ 為函數序列的上極限而$$\displaystyle \chi_{\limsup_{n \rightarrow \infty} E_n}$$ 為集合序列的上極限。

<details>

<summary> proof:  </summary>

令上極限集$$\displaystyle \limsup_{n \rightarrow \infty} E_n =\bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k=E$$

可得 $$\displaystyle \chi_{\limsup_{n \rightarrow \infty} E_n}(x)=\chi_E(x)$$ ，即點$$x$$為上極限集合的元素時為1，否則為0。

而$$\displaystyle \limsup_{n \rightarrow \infty} \chi_{E_n}$$ 為函數序列$$\{\chi_{E_1}, \chi_{E_2}, \chi_{E_3}, \ldots\}$$的上極限 。

給定集合$$E_n$$，因為$$\chi_{E_n} (x) = \left\{ \begin{align} 1,& \text{ if } x \in E_n,\\ 0,& \text{ if } x \notin E_n \end{align} \right.$$

因此$$\displaystyle \limsup_{n \rightarrow \infty} \chi_{E_n} (x) = \left\{ \begin{align} 1,& \text{ if } x \in \bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k=E,\\ 0,& \text{ if } x \notin\bigcup_{n=1}^\infty \bigcap_{k=n}^\infty E_k=E \end{align} \right. =\chi_E(x)$$

所以$$\displaystyle \limsup_{n \rightarrow \infty} \chi_{E_n} = \chi_E(x)=\chi_{\limsup_{n \rightarrow \infty} E_n}$$(QED)

</details>



#### 集合序列極限存在的充要條件

> $$\{E_n\} \subseteq X$$，則$$\displaystyle \lim_{n \rightarrow \infty} E_n$$ 存在若且唯若$$\displaystyle \lim_{n \rightarrow \infty} \chi_{E_n}$$ 存在

<details>

<summary> proof </summary>

proof=>

若$$\displaystyle \lim_{n \rightarrow \infty} E_n = E$$存在，則$$\displaystyle \limsup_{n \rightarrow \infty} E_n = \displaystyle \liminf_{n \rightarrow \infty} E_n =E$$

因為$$\displaystyle \chi_{\limsup_{n \rightarrow \infty} E_n} = \limsup_{n \rightarrow \infty} \chi_{E_n} =\chi_{E}$$且$$\displaystyle \chi_{\liminf_{n \rightarrow \infty} E_n } =\displaystyle \liminf_{n \rightarrow \infty} \chi_{E_n} = \chi_{E}$$

所以$$\limsup_{n \rightarrow \infty} \chi_{E_n} =\chi_{E} = \liminf_{n \rightarrow \infty} \chi_{E_n}$$

因此可得 $$\displaystyle \lim_{n \rightarrow \infty} \chi_{E_n}$$存在(QED)

proof <=

使用相同的方法可得證(QED)

</details>

