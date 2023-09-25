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
> 令$$f$$為定義在$$E \subseteq \mathbb{R}^n$$的可測函數，令範數$$\displaystyle  \|f\|_p = \left( \int_E |f(x)|^p dx\right)^{\frac{1}{p}}, ~ 0 < p < \infty$$，<mark style="color:blue;">此處</mark>$$p$$<mark style="color:blue;">為正實數值而不是自然數</mark>。
>
> 令$$L^p(E)$$為集合$$E$$上，滿足$$\|f\|_p < \infty$$的函數集合。
>
> 註：$$L^1(E)$$就是Lebesgue積分中的$$L(E)$$函數集合。而$$L(E)$$中的函數$$f$$可積分若且唯若$$|f|$$可積分。

### 本性(本質)有界函數(essentially bounded function)

> 令$$f$$為定義在$$E \subseteq \mathbb{R}^n$$的可測函數且$$m(E) > 0$$。
>
> 因為數學分析中的有界函數$$|f(x)|\leq M, \forall x \in  E$$條件太嚴格，因此放寬為在部分測度為0的集合之外都有界，即函數幾乎處處有界，$$\exists E_0 \subseteq E, ~m(E_0)=0$$且$$\exists M > 0\ni|f(x)| \leq M , \forall x \in E-E_0$$，此時稱$$f$$在集合$$E$$上本性有界(essential bounded)。而$$M$$稱為函數$$f$$的本性上界(essential upper bound)。
>
> 可簡寫為$$\exists M > 0 \ni m(\{x \in E~|~ |f(x)|>M\})=0$$。函數在定義域滿足$$f(x)> 0$$的測度為0，因此幾乎處處$$x \in E$$滿足$$f(x) \leq M$$。
>
> 因此$$f$$幾乎處處有界（a.e. bound）就是本性有界（essential bounded)。

本性有界函數就是定義域內測度不為0的集合$$E-E_0$$之值域$$S=\{f(x)~|~\forall x \in E-E_0\}$$為有界集合。此時可再定義$$S$$的上/下確界，稱為本性上/下確界。

<mark style="color:blue;">本性有界函數類，是在一個測度為零的集合之外有界的函數的全體</mark>。

由定義可得<mark style="color:red;">有界函數=>本性有界函數</mark>。

### 本性上/下確界

$$\mathrm{ess} \sup f = \inf\{ a \in \mathbb{R}~|~ m(\{x ~|~ f(x) > a\})=0\}$$，也就是說，對於定義域內的幾乎所有$$x$$，都有$$f(x) \leq a$$，再取滿足條件$$a$$的最大下界。若為空集時則$$\mathrm{ess} \sup f = \infty$$。

$$\mathrm{ess}\inf f = \sup\{ b \in \mathbb{R}~|~ m(\{x ~|~ f(x) <b \})=0\}$$，也就是說，對於定義域內的幾乎所有$$x$$，都有$$f(x) \geq b$$，再取滿足條件$$b$$的最小上界。若為空集時，則$$\mathrm{ess} \inf f = -\infty$$。

$$\sup f= \sup\{ a \in \mathbb{R} ~|~ f(x) \leq a\}$$滿足$$\forall x \in E,~ \forall \epsilon >0, f(x) < a + \epsilon$$。此時$$\{x \in E~|~ f(x) > a\} = \emptyset$$為空集合，因此測度為0。

$$\inf f = \inf \{b \in \mathbb{R} ~|~ f(x) \geq b\}$$，即$$\forall x \in E,~ \forall \epsilon > 0, f(x) > b - \epsilon$$。此時$$\{x \in E~|~ f(x) < b\} = \emptyset$$為空集合，因此測度為0

### 本性下/下確界與上/下確界的不等式關係

> 令$$f: E \rightarrow \mathbb{R}$$，則可得：$$\inf f \leq \mathrm{ess} \inf f \leq \mathrm{ess} \sup f \leq \sup f$$
>
> 註：令$$E_0 \subseteq E$$且$$m(E_0)=0$$。如果$$E_0=\emptyset$$時，$$\inf(f)=\mathrm{ess} \inf (f)$$且$$\sup(f)=\mathrm{ess} \sup (f)$$。

#### 範例

$$\displaystyle f(x) = \begin{cases} 5 & \text{ if } x = 1,\\ -4 & \text{ if } x = -1,\\ 2 & \text{ otherwise } \end{cases}$$

則$$\sup(f)=5, ~\inf(f)=-4$$，但由於$$m(\{x~|~f(x)=5\})=0$$且$$m(\{x~|~f(x)=-4\})=0$$，所以$$\mathrm{ess} \sup (f) = \mathrm{ess} \inf (f)=2$$。

#### 範例

$$\displaystyle f(x) = \begin{cases} x^3 & \text{ if } x  \in \mathbb{Q},\\ \arctan(x) & \text{ if } x  \in \mathbb{R-Q} \end{cases}$$

則$$\sup(f)=\infty, ~\inf(f)=-\infty$$

由於有理數的測度為0，即$$m(\mathbb{Q})=0$$，則本性上/下確界由定義在無理數的值域決定。可得$$\mathrm{ess} \sup (f) =\pi/2$$，$$\mathrm{ess} \inf (f) =-\pi/2$$。

## Holder不等式

> 共軛指標
>
> 若$$p,q \geq 1$$且滿足$$\frac{1}{p}+\frac{1}{q} = 1$$，則稱$$p,q$$為共軛指標。
>
> 可定義$$p=1$$時，$$q=\infty$$。

> Holder不等式
>
> $$p,q$$為共軛指標，$$1 \leq p \leq \infty$$且$$f \in L^p(E), g \in L^q(E)$$，可得
>
> $$\|fg\|_1 \leq \|f\|_p \|g\|_q$$。

$$p=q=2$$<mark style="color:red;">稱，Holder不等式為Schawarz不等式</mark>。

$$\displaystyle  \int_E |f(x) g(x) | \leq  \left( \int_E |f(x)|^2 dx \right)^{\frac{1}{2}} \left( \int_E |g(x)|^2 dx \right)^{\frac{1}{2}}$$

## Minkowski不等式

若$$f,g \in L^p(E), ~ 1 \leq p \leq \infty$$，則$$\|f+g\|_p \leq \|f\|_p + \|g\|_p$$。
