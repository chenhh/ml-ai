---
description: Lebesgue p-th integrable space
---

# Lp空間

簡介

連續(或幾乎處處連續)函數及Riemann積分理論，在很多場合可使用可測函數與Lebesgue理論所取代。

而Lp空間討論的是各種可積函數類的整體結構與性質。其中L2空間由於可定義內積空間且與Fourier級數與其它展開式的表達有重要的應用。

## Lp空間

定義Lp空間時，將$$0<p<\infty$$與$$p=\infty$$分開定義。

> 定義：Lp空間(p為正實數值)
>
> 令$$f$$為定義在$$E \subseteq \mathbb{R}^n$$的可測函數，令範數$$\displaystyle  \|f\|_p = \left( \int_E |f(x)|^p dx\right)^{\frac{1}{p}}, ~ 0 < p < \infty$$，<mark style="color:blue;">此處</mark>$$p$$<mark style="color:blue;">為正實數值而不是自然數</mark>。<mark style="color:blue;">此處積分中的絕對值不可省略，因為</mark>$$f$$<mark style="color:blue;">也可為複數值函數</mark>。
>
> 令$$L^p(E)$$為集合$$E$$上，滿足$$\|f\|_p < \infty$$的函數集合。
>
> 註：$$L^1(E)$$就是Lebesgue積分中的$$L(E)$$函數集合。而$$L(E)$$中的函數$$f$$可積分若且唯若$$|f|$$可積分。
>
> 註：在機率空間中，$$\displaystyle \mathrm{E}(|X|^p)=\int_\Omega |X|^p d\mathrm{P}$$表示隨機變數$$X$$的$$p$$次動差(moment)存在，雖然沒有取$$p^{-1}$$次方，但如果積分內為有限值時，是否取次方不影響計算值是否收斂。

> 定義：Lp空間($$p=\infty$$)
>
> 令$$M\geq 0, |f(x)| \leq M \text{ a.e. } \forall x \in E$$．定義<mark style="color:red;">一致範數(uniform norm)</mark>$$\begin{aligned} \|f\|_\infty &= \inf \{ M\geq 0 ~|~ |f(x)| \leq M \text{ a.e.} ~x \in E\} \\ &= \inf \{ M \geq 0 ~|~ m(\{x \in E ~|~ |f(x)| > M\})=0\} \\ & = \mathrm{ess} \sup |f| \end{aligned}$$
>
> 如果令$$S = \{x \in E ~|~ |f(x)| > M\} = f^{-1}(-\infty, -M) \cup f^{-1}(M, \infty)$$，則：$$\|f\|_\infty =  \begin{cases} \mathrm{ess} \sup |f| & \text{ if } m(S) > 0, \\ 0,  & \text{ if } m(S) = 0 \end{cases}$$
>
> 令$$L\infty$$空間為本性有界函數(幾乎處處有界函數)的集合。

* 可得$$\displaystyle \lim_{p \rightarrow \infty}\|f\|_p =\|f\|_\infty$$。
* 令$$f \in L^{\infty}(E)$$，則存在$$E$$的可測且有界函數$$g$$，且$$f=g \text{ a.e. }$$。
* <mark style="color:red;">在</mark>$$p=2$$<mark style="color:red;">時，可得</mark>$$f, g \in L^2(E) \Rightarrow fg \in L^1(E)$$<mark style="color:red;">，因此可定義內積</mark>$$\displaystyle \langle f,g  \rangle = \int_E f(x)g(x) dx$$<mark style="color:red;">為兩函數間的角度</mark>。<mark style="color:red;">進而得到可積函數(無限維)的內積空間</mark>。

### 一致範數等價於無限p範數

> $$f: E \rightarrow \mathbb{R}$$，$$\displaystyle  \|f\|_p = \left( \int_E |f(x)|^p dx\right)^{\frac{1}{p}}, ~ 0 < p < \infty$$，$$\|f\|_\infty = \mathrm{ess} \sup |f|$$，則：\
> $$\displaystyle \lim_{p \rightarrow \infty}\|f\|_p =\|f\|_\infty$$

<details>

<summary>proof: [todo]</summary>



</details>

### 本性(本質)有界函數(essentially bounded function)

> 令$$f$$為定義在$$E \subseteq \mathbb{R}^n$$的可測函數且$$m(E) > 0$$。
>
> 因為數學分析中的有界函數$$|f(x)|\leq M, \forall x \in  E$$條件太嚴格，因此放寬為在部分測度為0的集合之外都有界，即函數幾乎處處有界，$$\exists E_0 \subseteq E, ~m(E_0)=0$$且$$\exists M \geq  0\ni|f(x)| \leq M , \forall x \in E-E_0$$，此時稱$$f$$在集合$$E$$上本性有界(essential bounded)。而$$M$$稱為函數$$f$$的本性上界(essential upper bound)。
>
> 常簡寫為$$|f(x) \leq M \text{ a.e. }~ \forall x \in E$$或$$\exists M \geq  0 \ni m(\{x \in E~|~ |f(x)|>M\})=0$$。函數在定義域滿足$$f(x)> 0$$的測度為0，因此幾乎處處$$x \in E$$滿足$$f(x) \leq M$$。
>
> 因此$$f$$(值域)幾乎處處有界（a.e. bound）就是本性有界（essential bounded)。

本性有界函數就是定義域內測度不為0的集合$$E-E_0$$之值域$$S=\{|f(x)|~|~\forall x \in E-E_0\}$$為有界集合(或直接考慮值域的絕對值，可保證下界為0，只需處理上界)。此時可再定義$$S$$的上/下確界，稱為本性上/下確界。

<mark style="color:blue;">本性有界函數類，是在一個測度為零的集合之外有界的函數的全體</mark>。

由定義可得<mark style="color:red;">有界函數=>本性有界函數</mark>。

#### 範例：本性有界但無界的函數

$$f(x) = \begin{cases} x, \text{ if } x \in \mathbb{Q}, \\ 0, \text{ otherwise } \end{cases}$$

則$$f(x)$$無界，但因為有理數集的測度為0，即$$m(\mathbb{Q})=0$$，因此$$f$$本性有界，且$$\mathrm{ess} \sup f = \mathrm{ess} \inf f =0$$。

#### 範例：有界但不等於一致範數的函數

$$f(x) = \begin{cases} 1, \text{ if } x \in \mathbb{Q}, \\ 0, \text{ otherwise } \end{cases}$$

則$$|f(x)| \leq 1$$有界，且本性上/下界為$$0$$，因此$$0=\|f\|_\infty \neq  \sup f=1$$。

### 本性上/下確界

$$\mathrm{ess} \sup f = \inf\{ a \in \mathbb{R}~|~ m(\{x ~|~ f(x) > a\})=0\} = \inf\{ a \in \mathbb{R}~|~ m(f^{-1}(a, \infty))=0\}$$，也就是說，對於定義域內的幾乎所有$$x$$，都有$$f(x) \leq a$$，再取滿足條件$$a$$的最大下界。若為空集時則$$\mathrm{ess} \sup f = \infty$$。

$$\mathrm{ess}\inf f = \sup\{ b \in \mathbb{R}~|~ m(\{x ~|~ f(x) <b \})=0\} =  \sup\{ b \in \mathbb{R}~|~ m(f^{-1}(-\infty, b))=0\}$$，也就是說，對於定義域內的幾乎所有$$x$$，都有$$f(x) \geq b$$，再取滿足條件$$b$$的最小上界。若為空集時，則$$\mathrm{ess} \inf f = -\infty$$。

$$\sup f= \sup\{ a \in \mathbb{R} ~|~ f(x) \leq a\}$$滿足$$\forall x \in E,~ \forall \epsilon >0, f(x) < a + \epsilon$$。此時$$\{x \in E~|~ f(x) > a\} = \emptyset$$為空集合，因此測度為0。

$$\inf f = \inf \{b \in \mathbb{R} ~|~ f(x) \geq b\}$$，即$$\forall x \in E,~ \forall \epsilon > 0, f(x) > b - \epsilon$$。此時$$\{x \in E~|~ f(x) < b\} = \emptyset$$為空集合，因此測度為0

### 本性下/下確界與上/下確界的不等式關係

> 令$$f: E \rightarrow \mathbb{R}$$，則可得：
>
> $$-\infty \leq \inf f \leq \mathrm{ess} \inf f\leq f  \leq \mathrm{ess} \sup f \leq \sup f  \leq \infty$$。
>
> 註：令$$E_0 \subseteq E$$且$$E_0=\emptyset$$時，則$$\inf(f)=\mathrm{ess} \inf (f)$$且$$\sup(f)=\mathrm{ess} \sup (f)$$且有可能等於$$\pm \infty$$。如果只有$$m(E_0)=0$$時，無法得到此等式，見下例。

註：空集合的上/下確界為$$\sup(\emptyset)=-\infty$$，$$\inf(\emptyset)=\infty$$。且$$m(\emptyset)=0$$。因此當函數的定義域$$m(E)=0$$時，得$$\infty = \mathrm{ess} \inf f \geq \mathrm{ess} \sup f = -\infty$$。

#### 範例

$$\displaystyle f(x) = \begin{cases} 5 & \text{ if } x = 1,\\ -4 & \text{ if } x = -1,\\ 2 & \text{ otherwise } \end{cases}$$

則$$\sup(f)=5, ~\inf(f)=-4$$，但由於$$m(\{x~|~f(x)=5\})=0$$且$$m(\{x~|~f(x)=-4\})=0$$，所以$$\mathrm{ess} \sup (f) = \mathrm{ess} \inf (f)=2$$。

#### 範例：無上/下界但有本性上/下界的函數

$$\displaystyle f(x) = \begin{cases} x^3 & \text{ if } x  \in \mathbb{Q},\\ \arctan(x) & \text{ if } x  \in \mathbb{R-Q} \end{cases}$$

則$$\sup(f)=\infty, ~\inf(f)=-\infty$$

由於有理數的測度為0，即$$m(\mathbb{Q})=0$$，則本性上/下確界由定義在無理數的值域決定。可得$$\mathrm{ess} \sup (f) =\pi/2$$，$$\mathrm{ess} \inf (f) =-\pi/2$$。

## 參考資料

* [https://math.stackexchange.com/questions/858494/definition-of-l-infty-norm](https://math.stackexchange.com/questions/858494/definition-of-l-infty-norm)
* [https://en.wikipedia.org/wiki/Lp\_space](https://en.wikipedia.org/wiki/Lp\_space)
* [https://en.wikipedia.org/wiki/Essential\_infimum\_and\_essential\_supremum](https://en.wikipedia.org/wiki/Essential\_infimum\_and\_essential\_supremum)
* [https://en.wikipedia.org/wiki/Uniform\_norm](https://en.wikipedia.org/wiki/Uniform\_norm)
