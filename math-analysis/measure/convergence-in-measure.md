---
description: convergence in measure
---

# 測度收斂

## 簡介

測度收斂強調的$$f_n \rightarrow f$$時，隨著$$n$$變大，不收斂的點對於所有的函數並非在一個固定的集合$$E_0$$中，但是這些不收斂的點形成的集合測度為0。

<mark style="background-color:red;">在有限測度空間中，幾乎處處收斂可得測度收斂</mark>。

<mark style="color:red;">一般測度空間中，幾乎一致收斂可保證測度收斂</mark>。

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

### 範例：幾乎處處不收斂但依測度收斂

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

令$$\{f_n(x)\}, \{g_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列。

### 測度收斂可移項

1. $$f_n \rightarrow f$$ in measure$$\Leftrightarrow  f_n -f \rightarrow 0$$ in measure.
2. $$f_n \rightarrow 0$$ in measure $$\Leftrightarrow f_n^2 \rightarrow 0$$ in measure.
3. $$f_n \rightarrow f$$ in measure $$\Rightarrow f_n^2 \rightarrow f^2$$ in measure.

<details>

<summary>proof 1: 由測度收斂定義移項即為所求</summary>

由定義得$$\displaystyle \lim_{n \rightarrow \infty }\mu(\{x \in E ~|~ |f_n(x)-f(x)| \geq \epsilon\}) =0$$

移項得$$\displaystyle \lim_{n \rightarrow \infty }\mu(\{x \in E ~|~ |(f_n(x)-f(x))-0| \geq \epsilon\}) =0$$

(QED)

</details>

<details>

<summary>proof2: 由測度收斂定義移項即為所求</summary>

由定義得$$\displaystyle \lim_{n \rightarrow \infty }\mu(\{x \in E ~|~ |f_n(x)| \geq \epsilon\}) =0$$

&#x20;可得$$\displaystyle \lim_{n \rightarrow \infty }\mu(\{x \in E ~|~ |f_n^2(x)| \geq \epsilon^2\}) =0$$ (QED)

</details>

<details>

<summary>proof: 移項後整理</summary>

因為$$f_n \rightarrow f$$ in measure，由1得$$f_n - f \rightarrow 0$$ in meaure，由2得$$(f_n-f)^2 \rightarrow 0$$ in measure.

展開得$$f_n^2 +f^2 -2f_nf \rightarrow 0$$ in measure.--(1)



因為$$f_n \rightarrow f$$ in measure，可得$$2f_n \rightarrow 2f$$ in measure，而$$\{f_n\}$$幾乎處處有限且測度收斂至$$f$$，由測度收斂的函數幾乎處處有限得$$f$$幾乎處處有限。

而在有限測度時，測度收斂與幾乎有限函數乘積為測度收斂，因此可得$$2f_nf\rightarrow 2f^2$$ in measure，移項得$$2f_nf-2f^2 \rightarrow 0$$ in measure-(2)

由(1,2)相減得$$f_n^2-f^2 \rightarrow 0$$ in measure.

移項得$$f_n^2 \rightarrow f^2$$ in measure.

(QED)

</details>

### 測度收斂相加減仍為測度收斂(線性性質)

> $$f_n \rightarrow f$$ in measure且$$g_n \rightarrow g$$ in measure.
>
> 則$$\forall a,b \in \mathbb{R}$$, $$af_n + bg_n \rightarrow af + bg$$ in measure.

<details>

<summary>proof：三角不等式</summary>

由三角不等式得：$$|af_n +bg_n - (af+bg)|=|(af_n-af) - (bg_n-bg)|\leq |af_n-af| + |bg_n-bg|$$

因此可得$$\displaystyle  \begin{aligned} \forall \epsilon >0 & ~\{x \in E ~|~ |af_n +bg_n - (af+bg)| \geq \epsilon \} \subseteq \\ 	& \{x \in E ~|~ |af_n - af| \geq \frac{\epsilon}{|a|}\} \cup \\ 	& \{x \in E ~|~ |bg_n - bg| \geq \frac{\epsilon}{|b|}\} \end{aligned}$$

所以當$$n \rightarrow \infty$$，由測度的單調性可得$$\mu(\{x \in E ~|~ |af_n +bg_n - (af+bg)| \geq \epsilon \}) \rightarrow 0$$

(QED)

</details>

### 有限測度時，測度收斂與幾乎有限函數乘積為測度收斂

> 若$$\mu(E) < \infty$$，$$f_n \rightarrow f$$ in measure且$$g$$為可測的處處有限函數，則$$f_ng \rightarrow fg$$ in measure.

### 有限測度時，測度收斂函數乘積為測度收斂

> 若$$\mu(E) < \infty$$，$$f_n \rightarrow f$$ in measure且$$g_n \rightarrow g$$ in measure，則$$f_n g_n \rightarrow fg$$ in measure.

### 有限測度時，測度收斂函數相除為測度收斂

> 若$$\mu(E) < \infty$$，$$f_n \rightarrow f$$ in measure且$$g_n \rightarrow g$$ in measure，若$$g_n, \forall n$$和$$g$$幾乎處處不為0，則$$\frac{f_n}{g_n} \rightarrow \frac{f}{g}$$ in measure.

### 測度收斂的絕對值收斂

> $$f_n \rightarrow f$$ in measure $$\Rightarrow |f_n| \rightarrow |f|$$ in measure.

<details>

<summary>proof: 絕對值的三角不等式</summary>

絕對值的三角不等式，固定$$x \in E$$，可得 $$|f_n(x)-f(x)| \geq ||f_n(x)| - |f(x)||$$

因此$$\forall \epsilon > 0$$，若$$||f_n(x)| - |f(x)|| > \epsilon$$可得$$|f_n(x)-f(x)| >\epsilon$$

可得$$\{x \in E~|~ ||f_n(x)| - |f(x)|| > \epsilon\} \subseteq  \{x \in E~|~|f_n(x)-f(x)| >\epsilon\}$$

因為$$f_n \rightarrow f$$ in measure，所以$$\displaystyle \lim_{n \rightarrow \infty} \mu( \{x \in E~|~|f_n(x)-f(x)| >\epsilon\})=0$$

由測度的單調性可得$$\displaystyle \lim_{n \rightarrow \infty} \mu(\{x \in E~|~ ||f_n(x)| - |f(x)|| > \epsilon\})=0$$

(QED)

</details>

## 有限測度空間中幾乎處處收斂可保證測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列且$$\mu(E) < \infty$$(有限測度空間)。
>
> 若$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) \text{ a.e. on } E$$且$$f$$幾乎處處有限，則$$\{f_n\}$$依測度收斂至$$f$$。

<details>

<summary>proof: Egoroff定理保證有限測度時，a.e. => a. u. ，而a.u.在一般測度空間保證為測度收斂，因此有限測度時，a.e.=>測度收斂</summary>



</details>

### 範例：一般測度空間幾乎處處收斂或非測度收斂

給定Lebesgue測度空間$$E=(0, \infty)$$，$$\mathcal{L}$$為Lebesgue可測集合，$$m$$為測度。

令函數序列$$\displaystyle  f_n(x)= \begin{cases} 1, & x \in (0, n] \\ 0, & x \in (n, \infty) \end{cases}~ n \in \mathbb{Z}^+$$，則$$\displaystyle \lim_{n \rightarrow \infty }f_n(x)=1 \text{ a.e.}$$

但是對於任意的$$n \in \mathbb{Z}^+$$，取$$0 < \epsilon < 1$$，可得$$m(\{x \in E~|~ |f_n(x)-1| \geq \epsilon\})=m((n, \infty))=\infty$$，因此$$f_n$$在$$E$$上不依測度收斂於1。

## 一般測度空間中幾乎一致收斂可保證測度收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列。
>
> $$f_n \rightarrow f$$ almost unif. $$\Rightarrow f_n \rightarrow f$$ in measure.
>
> 即$$\forall \epsilon > 0$$，存在集合$$E_\epsilon \subseteq E$$且$$\mu(E_\epsilon)< \epsilon$$，使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)$$uniformly on $$E_\epsilon^c$$，則$$f_n \rightarrow f \text{ in measure on } E$$。

<details>

<summary>proof: 依定義直接證明</summary>

幾乎一致收斂依定義得$$\forall \epsilon > 0, \exists n_0 \in \mathbb{N} \ni \forall x \in E-E_\epsilon,~ |f_n(x)-f(x)| < \epsilon, ~  \forall n \geq n_0$$

因此在$$n \geq n_0$$時，只有在$$E_\epsilon$$中的點可能得到$$|f_n(x)-f(x)| \geq \epsilon$$，即$$\{x~|~|f_n(x)-f(x)| \geq \epsilon\} \subseteq E_\epsilon$$。

由測度的單調性得$$\mu(\{x~|~|f_n(x)-f(x)| \geq \epsilon\}) \leq \mu(E_\epsilon)< \epsilon$$

因此$$n \rightarrow \infty$$時，可得$$f_n \rightarrow f$$ in measure (QED)

</details>

## 依測度柯西序列(Cauchy sequence in measure)

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，若$$\forall \epsilon > 0$$，若
>
> $$\displaystyle \lim_{m,n \rightarrow \infty}\mu( x \in E ~|~ |f_m(x) - f_n(x)| \geq \epsilon) = 0$$，則稱$$\{f_n(x)\}$$為$$E$$上的依測度Cauchy序列。
>
> 或者$$\forall \epsilon >0, \forall\delta >0$$, $$\exists n \in \mathbb{N} \ni \mu(\{x\in E ~|~ |f_m(x)-f_n(x)|\geq \epsilon\})<\delta$$。

證明函數序列$$\{f_n\}$$ 依測度收斂時，需要先知道收斂函數$$f$$ 。然而很多時候是沒法求出收斂函數$$f$$ 的，或者我們不關心收斂到哪個函數。因此使用“依測度柯西序列”，無需知道收斂函數$$f$$ ，即可判斷函數序列$$\{f_n\}$$ 是否依測度收斂。

## 測度收斂若且唯若依測度柯西序列

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，
>
> 則$$\{f_n\}$$ Cauchy in measure $$\Leftrightarrow f_n \rightarrow f$$ in measure.

## 測度收斂則存在子序列幾乎一致收斂且幾乎處處收斂

> $$\{f_n(x)\}$$為集合$$E$$上幾乎處處有限的可測函數序列，
>
> $$f_n \rightarrow f$$ in measure $$\Rightarrow \exists {f_{n_k}} \subseteq \{f_n\} \ni f_{n_k} \rightarrow f$$ almost uniformly.
>
> 因此一般測度空間中a.u.可保證a.e.因此可得$$f_{n_k} \rightarrow f$$ a.e.

## 參考資料

* [https://zhuanlan.zhihu.com/p/37034124](https://zhuanlan.zhihu.com/p/37034124)
* [https://www.zhihu.com/question/263466675](https://www.zhihu.com/question/263466675)
