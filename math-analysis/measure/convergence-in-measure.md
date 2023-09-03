---
description: convergence in measure
---

# 測度收斂

## 簡介

測度收斂強調的$$f_n \rightarrow f$$時，隨著$$n$$變大，不收斂的點對於所有的函數並非在一個固定的集合$$E_0$$中，但是這些不收斂的點形成的集合測度為0。

<mark style="background-color:red;">在有限測度空間中，幾乎處處收斂可得測度收斂</mark>。

## 測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若
>
> $$\forall \epsilon > 0$$，可得$$\displaystyle \lim_{n \rightarrow \infty}\mu( \{x \in E ~|~ |f_n(x) - f(x)| > \epsilon\}) = 0$$。
>
> 或 $$\forall \epsilon >0, ~ \exists n_0 \in \mathbb{N} \ni \mu(\{ x \in E ~|~ |f_n(x) - f(x)| > \epsilon\}) =0, ~ \forall n \geq n_0$$.&#x20;
>
> 則稱$$\{f_n\}$$依測度收斂至函數$$f$$。$$f$$可測且幾乎處處有限。
>
> <mark style="color:blue;">注意此處的limit符號是在測度外，表示不限特定集合。如果等號在測度內為a.e.收斂</mark>。

<mark style="color:red;">註：測度收斂強調的是不收斂的點形成的集合測度為0，而不要求所有函數序列有在相同的集合中不收斂</mark>。

### 範例：無限測度時幾乎處處不收斂但依測度收斂

在Lebesgue測度空間$$(\mathbb{R}, L, m)$$ 上，取半開區間$$E=(0,1]$$ 。建構函數序列如下：

第一步將$$(0,1]$$二等分，定義兩個函數：$$\displaystyle f_1^{(1)}= \begin{cases} 1, & x \in (0,1/2], \\ 0, & x \in (1/2, 1] \end{cases}$$$$\displaystyle f_2^{(1)}= \begin{cases} 0, & x \in (0,1/2], \\ 1, & x \in (1/2, 1] \end{cases}$$

第2步將$$(0,1]$$四等分、第3步八等分、。。。依次作下去，到第$$n$$步時，將$$(0,1]$$平均分成$$2^n$$份，並定義$$2^n$$個函數，每個函數$$\displaystyle f_j^{(n)}= \begin{cases} 1, & x \in (\frac{j-1}{2^n},\frac{j}{2^n}], \\ 0, & x \notin (\frac{j-1}{2^n},\frac{j}{2^n}] \end{cases}$$

將$$\{f_j^{(n)}\}, ~j=1,2,\dots, 2^n$$先按$$n$$後按$$j$$的順序排成一列得$$f_1^{(1)}, f_2^{(1)}, f_1^{(2)}, f_2^{(2)}, f_3^{(2)}, f_4^{(2)}, \dots, f_1^{(n)}, f_2^{(n)}, \dots, f_{2^n}^{(n)}, \dots$$。其中$$f_j^{(n)}$$在這個序列裡是第$$2^n-2+j$$ 個函數。

可得$$\{f_j^{(n)}\}$$在$$E$$上處處不收斂，但依Lebesgue測度$$m$$收斂至0。

任取一點$$x_0 \in (0,1]$$，對於任意的$$2^n$$切分，必定存在一個$$j$$使得$$x_0 \in (\frac{j-1}{2^n}, \frac{j}{2^n}]$$，即$$f_j^{(n)}(x_0)=1$$。但是$$f_{j-1}^{(n)}(x_0)=f_{j+1}^{(n)}(x_0)=0$$，<mark style="color:blue;">也就是說對任意一點</mark>$$x_0$$<mark style="color:blue;">，</mark>$$\{f_j^{(n)}\}$$<mark style="color:blue;">中有無窮多個函數值取1，無窮多個函數值取0，因此在</mark>$$(0,1]$$<mark style="color:blue;">任意一點都是發散的</mark>。

考慮測度收斂至0，計算第$$N=2^n-2+j$$個函數與$$f$$的差值大於$$\epsilon$$的點。

即$$\forall \epsilon > 0$$，$$E=\{x \in (0,1] ~|~ |f_j^{(n)}(x) - f(x)| \geq \epsilon\} = (\frac{j-1}{2^n}, \frac{j}{2^n}]$$，即切$$2^n$$段中，只有一段滿足條件，因此$$m(E)=m((\frac{j-1}{2^n}, \frac{j}{2^n}])=\frac{1}{2^n}$$。

當$$N \rightarrow \infty$$時，$$n \rightarrow \infty$$，可得$$\displaystyle \lim_{n \rightarrow \infty }m(E)=0$$。

## 測度收斂的函數幾乎處處有限

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若在$$E$$上依測度收斂至$$f(x)$$，則$$f(x)$$為幾乎處處有限的函數。
>
> $$f_n \rightarrow f \text{ in measure } \Rightarrow f \text{  finite a.e. }$$

[https://math.stackexchange.com/questions/3565953/what-does-it-mean-to-be-a-e-finite-real-function-to-converge-in-measure](https://math.stackexchange.com/questions/3565953/what-does-it-mean-to-be-a-e-finite-real-function-to-converge-in-measure)

<details>

<summary>proo:f把函數<span class="math">f</span>之值為<span class="math">\pm \infty</span>的點分兩類：一種是<span class="math">f_n</span>在這點取值均為<span class="math">\pm \infty</span> ，於是<span class="math">f</span>自然在這點取值為<span class="math">\pm \infty</span> ；另一種是<span class="math">f_n</span>雖然在這點取有限值，但隨著<span class="math">n \rightarrow \infty</span> ， <span class="math">f_n</span>之值趨於無窮大。</summary>

case 1:$$f_n$$在同一點取值均為$$\pm \infty$$。

令$$S_n=\{x \in E~|~ f_n(x)=\pm \infty\}$$，$$\displaystyle S=\bigcup_{n=1}^\infty  S_n$$

依不相交集合的測度次可加性得$$\displaystyle \mu(S) \leq \sum_{n=1}^\infty \mu(S_n)$$。

因為$$f_n$$幾乎處處有限，因此$$\mu(S_n)=0, \forall n$$，可得$$0 \leq \mu(S) \leq 0$$，因此$$\mu(S)=0$$ (QED)

case 2:$$f_n$$在該點均為有限值，但隨$$n$$發散。

已知$$f_n \rightarrow f \text{ measure }$$，且$$f_n$$ finite a.e.

令$$F=\{x \in E ~|~ f(x)=\pm \infty\}$$，由假設得$$\forall x \in F, |f_n(x)| < \infty, ~\forall n$$。

因為擴充實數中$$|c-\infty|=\infty$$因此集合$$F$$中的點$$x$$滿足$$\forall \epsilon > 0, |f_n(x)-f(x)|\geq \epsilon$$。

因此可得$$\displaystyle \forall \epsilon >0,~ F \subseteq \{x \in E~|~ |f_n(x) - f(x)| \geq \epsilon\}$$

不相交集合的測度次可加性得$$\displaystyle \mu(F) \leq \mu(\{x \in E~|~ |f_n(x) - f(x)| \geq \epsilon\})=0$$

因此$$\mu(F)=0$$ (QED)

</details>

## 測度收斂的唯一性

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若在$$E$$上依測度收斂至$$f(x)$$與$$g(x)$$，則$$f(x) = g(x)$$ a.e. $$\forall x \in E$$。

<details>

<summary>proof: 三角不等式</summary>

令$$S_m=\{x \in E ~|~ |f(x) - g(x)| \geq 1/m\}, ~m\in \mathbb{N}$$, $$S=\{x\in E ~|~ f(x) \neq g(x)\}$$，可得$$\displaystyle S= \bigcup_{m=1}^\infty S_m$$。

若$$|f(x) - g(x)| \geq 1/m$$，可得$$|f(x) - f_n(x)| \geq 1/(2m)$$或者 $$|f_n(x) - g(x)| \geq 1/(2m)$$。

因為若$$|f(x)-f_n(x)|, |f_n(x)-g(x)| < 1/(2m)$$同時成立時，由三角不等式得$$|f(x)-g(x)| \leq |f(x)-f_n(x)|+|f_n(x) - g(x)| < 1/m$$

與假設不符。

因此對於$$n \in \mathbb{N}$$，可得$$\displaystyle S_m \subseteq \{x \in E ~|~ |f(x) -f_n(x) \geq \frac{1}{2m} \} \cup \{ x \in E ~|~ |f_n(x) -g(x)| \geq \frac{1}{2m}\}$$

由測度的次可加性得$$\displaystyle \mu(S_m) \leq \mu(\{x \in E ~|~ |f(x) -f_n(x) \geq \frac{1}{2m} \}) + \mu( \{ x \in E ~|~ |f_n(x) -g(x)| \geq \frac{1}{2m}\})$$

當$$n \rightarrow \infty$$由$$f_n \rightarrow f \text{ measure }$$與$$f_n \rightarrow g \text { measure }$$的條件知右側值為0，因此$$\mu(S_m)=0$$

而$$S=\bigcup_{m=1}^\infty S_m$$，由測度次可加性得$$\mu(S) \leq \sum_{m=1}^\infty \mu(S_m) =0$$

因此$$\mu(S)=0$$

(QED)

</details>

## 測度收斂的線性性質

$$\{f_n(x)\}, \{g_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列。

### 測度收斂相加減仍為測度收斂

> $$f_n \rightarrow f$$ in measure且$$g_n \rightarrow g$$ in measure.
>
> 則$$\forall a,b \in \mathbb{R}$$, $$af_n + bg_n \rightarrow af + bg$$ in measure.

### 有限測度時，測度收斂與幾乎有限函數乘積為測度收斂

> 若$$\mu(E) < \infty$$，$$f_n \rightarrow f$$ in measure且$$g$$為可測的處處有限函數，則$$f_ng \rightarrow fg$$ in measure.

### 有限測度時，測度收斂函數乘積為測度收斂

> 若$$\mu(E) < \infty$$，$$f_n \rightarrow f$$ in measure且$$g_n \rightarrow g$$ in measure，則$$f_n g_n \rightarrow fg$$ in measure.

### 測度收斂的絕對值收斂

> $$f_n \rightarrow f$$ in measure $$\Rightarrow |f_n| \rightarrow |f|$$ in meausre.





## 有限測度空間中幾乎處處收斂可保證測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列且$$\mu(E) < \infty$$(有限測度空間)。
>
> 若$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) \text{ a.e. on } E$$且$$f$$幾乎處處有限，則$$\{f_n\}$$依測度收斂至$$f$$。







## 依測度Cauchy序列(Cauchy sequence in measure)

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若$$\forall \epsilon > 0$$，若
>
> $$\displaystyle \lim_{m,n \rightarrow \infty}\mu( x \in E ~|~ |f_m(x) - f_n(x)| > \epsilon) = 0$$，則稱$$\{f_n(x)\}$$為$$E$$上的依測度Cauchy序列。

## 參考資料

* [https://zhuanlan.zhihu.com/p/37034124](https://zhuanlan.zhihu.com/p/37034124)
