# 有界變差(bounded variation)

## 簡介

閉區間的單調函數的不連續點為可數(無限)個。

有界變差的幾何意義為函數的弧長。

有界變差函數為有界函數。

有界變差函數只可能有第一類間斷點(jump)，從而可以作連續化處理。

<mark style="color:red;">有界變差函數<=>可分解為兩個單調遞增函數的差值(但不唯一)。</mark>可以定義對它的Lebesgue-Stieltjes積分。

一般函數可由有界變差拆解成連續函數+純跳躍函數之和。

<mark style="color:red;">有界變差函數幾乎處處可微分</mark>。因此可以寫它的導數，而且它的導數可積。

有界變數函數之值為0 <=> 函數為常數值。

布朗運動的一次變差不存在，二次變差為有限值。

#### 對於實線的閉合有界區間上的連續函數，我們有以下包含關係：

<mark style="color:red;">連續可微⊆ Lipschitz 連續⊆絕對連續⊆連續且有界變差 ⊆幾乎處處可微</mark>

## 遞增函數的有限分割的總跳躍量小於值域之差

> 令函數$$f: [a,b] \rightarrow \mathbb{R}$$為遞增函數(不必為連續函數)。
>
> 令$$x_0, x_1, \dots, x_n$$為閉區間$$[a,b]$$的一組有限分割且滿足$$a=x_0 < x_1 < \dots <x_n=b$$
>
> 則可得不等式 $$\sum_{k=1}^{n-1} [f({x_{k+})} - f({x_{k-}})] \leq f(b) - f(a)$$
>
> <mark style="color:blue;">其中</mark>$$f({x_{k+})} - f({x_{k-}})$$<mark style="color:blue;">為函數</mark>$$f$$<mark style="color:blue;">在點</mark>$$x_k$$<mark style="color:blue;">的跳躍量(jump)。</mark>

<details>

<summary>proof: 使用遞增函數的性質</summary>

令$$y_k \in (x_k , x_{k+1})$$

因為$$f$$為遞增函數，可得$$f({x_{k+}}) \leq f_(y_k)$$且 $$f(y_{k-1}) \leq f(x_{k-})$$。

整理可得 $$f(x_{k+}) - f(x_{k-}) \leq f(y_k) - f(y_{k-1})$$。

$$\sum_{k=1}^{n-1} f(x_{k+}) - f(x_{k-})  \leq \sum_{k=1}^{n-1}f(y_k) - f(y_{k-1}) \leq f(b) - f(a)$$ (QED)

</details>

## 定義在閉區間的單調函數的不連續點為可數(無限)個

> $$f: [a,b] \rightarrow \mathbb{R}$$為單調函數，則$$f$$上不連續點的集合為可數個。

<details>

<summary>proof</summary>

不失一般性，令$$f$$為遞增函數。

令$$S_m$$為開區間$$(a,b)$$中，函數$$f$$的跳躍量超過$$\frac{1}{m}, ~ m > 0$$的點所形成的集合。

若分割點$$x_1 < x_2 < \dots, x_{n-1}$$均在集合$$S_m$$中時，由[遞增函數的有限分割總跳躍量小於值域之差](bounded-variation.md#di-zeng-han-shu-de-you-xian-fen-ge-de-zong-tiao-yue-liang-xiao-wu-zhi-yu-zhi-cha)的性質可得 $$\frac{n-1}{m} \leq f(b) - f(a)$$。

即$$S_m$$內集合點的總變動量的上限為$$f(b) - f(a)$$，所以$$n<\infty$$，因此$$S_m$$為有限個元素的集合  。

而函數$$f$$在開區間$$(a,b)$$的不連續點形成的集合為$$\displaystyle \bigcup_{m=1}^\infty S_m$$的子集合，因此$$f$$上不連續點為可數個。(QED)

</details>

## 有界變差函數 (functions of bounded variation)

> 定義: 分割(partition)
>
> $$[a,b]$$為緊緻區間，令集合$$P=\{x_0, x_1, \dots ,x_n\}$$滿足不等式：
>
> $$a=x_0 < x_1 < \dots < x_n=b$$為$$[a,b]$$的一組分割。
>
> 令$$\Delta x_k = x_{k} - x_{k-1}$$為其中的第$$k$$組分割，可得$$\sum_{k=1}^n \Delta x_k = b-a$$。
>
> <mark style="color:blue;">令區間</mark>$$[a,b]$$<mark style="color:blue;">上所有分割形成的集合為</mark>$$\mathcal{P}[a,b]$$。

> <mark style="color:red;">定義：有界變差函數</mark>
>
> 給定函數$$f: [a,b] \rightarrow \mathbb{R}$$與分割$$P \in \mathcal{P}[a,b]$$。
>
> 令$$\Delta f_k = f(x_k) - f(x_{k-1}), ~ k =1,2,\dots, n$$。
>
> 若存在正實數$$M > 0 \ni \sum_{k=1}^n | \Delta f(x_k)| \leq M$$，$$\forall \text{ paritition } P \in \mathcal{P}[a,b]$$，則稱$$f$$在區間$$[a,b]$$為有界變差函數。
>
> 也可用全變差定義：$$V_f(a,b)=\sup\left\{  \sum_{k=1}^n |\Delta f(x_k)| ~|~ \forall P \in  \mathcal{P}[a,b] \right\}<\infty$$。
>
> 記$$[a,b]$$上有界變差函數的集合為$$\mathrm{BV}([a,b])$$。

### 單調函數為有界變差函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為單調函數，則$$f$$在$$[a,b]$$為有界變差函數。
>
> 反之若$$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，若$$V_f(a,b)=f(b)-f(a)$$，則$$f$$為遞增函數。

<details>

<summary>proof: 單調函數的變動上(下)限為|f(b)-f(a)|</summary>

proof 1

不失一般性令$$f$$為遞增函數。

對於所有分割$$P \in \mathcal{P}[a,b]$$，遞增函數可得$$\Delta f_k=f(x_k) - f(x_{k-1}) \geq 0$$。

因此$$\sum_{k=1}^n | \Delta f_k | = \sum_{k=1}^n \Delta f_k = \sum_{k=1}^n [f(x_k) - f(x_{k-1})]=f(b) -f(a)$$ (QED)

</details>

### 可微分且微分值有限的函數為有界變差函數

> $$f: [a,b] \rightarrow \mathbb{R}$$數且$$f'(x)$$在$$(a,b)$$可微分。
>
> 若$$f'(x)$$在$$(a,b)$$有界，即$$\exists M > 0 \ni |f^{'}(x)| \leq M ~\forall x \in (a,b)$$，
>
> 則$$f$$在$$[a,b]$$為有界變差函數。

<details>

<summary>proof: 因為函數變動斜率M為有限值，因此函數變動量有限</summary>

由微分均值定理可得$$\Delta f_k= f(x_k) - f(x_{k-1} )= f^{'}(t_k)(x_k - x_{k-1}), ~ t_k \in (x_{k-1}, x_k)$$

因此可得$$\sum_{k=1}^n |\Delta f_k| = \sum_{k=1}^n |f^{'}(t_k)| \Delta x_k \leq M \sum_{k=1}^n \Delta x_k = A(b-a)$$ (QED)

</details>

### 範例：連續函數但非有界變差函數

$$f(x)=x \cos[\frac{\pi}{2x}]$$，$$if x \neq 0, f(0)=0$$。則$$f$$在$$[0,1]$$連續。

若考慮分割$$P=\{0, \frac{1}{2n}, \frac{1}{2n-1}, \dots, \frac{1}{3}, \frac{1}{2}, 1\}$$

可得變差$$\sum_{k=1}^2n |\Delta f_k| = \frac{1}{2n}+\frac{1}{2n} + \frac{1}{2n-2}+\frac{1}{2n-2}+\dots +\frac{1}{2} + \frac{1}{2} = 1+ \frac{1}{2} +\dots + \frac{1}{n}$$

但並非對所有$$n$$收斂，如$$\sum_{n=1}^\infty \frac{1}{n}$$發散。

此例中$$f{'}$$在$$(0,1)$$存在，但並非有界。

### 範例：函數微分值有限但不是定義在閉區間時不一定為有界變差函數

$$f(x)=x^{1/3}$$在任意有限區間為單調函數，因此為有界變差函數。

但在$$x \rightarrow \infty$$時，$$f'(x) \rightarrow \infty$$。

## 有界變差函數為有界函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，即$$\exists M > 0 \ni \sum |\Delta f_k| \leq M$$，$$\forall P \in \mathcal{P}[a,b]$$，則$$f$$為有界函數，即$$\exists N > 0 \ni f(x) \leq N, \forall x \in [a,b]$$。
>
> 反之可得$$f$$不是有界函數=> $$f$$不是有界變差函數。

<details>

<summary>proof: 有界變差函數的變動量為函數的弧長，若有限時，表示函數有上下限。</summary>

令$$x \in (a,b)$$

考慮分割$$P=\{a,x,b\}$$可得 $$|f(x) - f(a)| + |f(b) - f(x) | \leq M$$

即$$|f(x) - f(a)| \leq M$$，$$|f(x)| \leq |f(a)| + M$$

在$$x=a$$或$$x=b$$時也可得到相同不等式(QED)

</details>

## 有界變差函數取最大值為有界變差函數

> $$f,g: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，則$$m(x)=\max\{f(x), g(x)\}$$為有界變差函數。

## 有界變差函數取絕對值為有界函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，則$$|f|$$為有界變差函數。反之不成立。

## 有界變差函數集合為線性空間

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，記為$$f \in \mathrm{BV}([a,b])$$。則$$\mathrm{BV}([a,b])$$為線性空間。
>
> 即$$\forall f,g \in \mathrm{BV}([a,b]), a,b \in \mathbb{R}$$，可得：$$af+bg \in \mathrm{BV}([a,b])$$。

## 全變差(total variation)

> 給定$$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，令$$\sum(P)=\sum_{k=1}^n | \Delta f_k|$$為區間$$[a,b]$$使用分割$$P=\{x_0, x_1, \dots ,x_n\}$$的變差之和。
>
> 定義$$V_f(a,b) = \sup \{ \sum(P) ~|~ P \in \mathcal{P}[a,b]\}$$為區間$$[a,b]$$的全變差。
>
> 通常簡寫為$$V_f$$
>
> 也可寫成$$\displaystyle V_f(a,b)=\lim_{\Delta x_n \rightarrow 0}\sum_{k=1}^n |\Delta f_k|$$其中$$\displaystyle \Delta x_n = \max_{1\leq k \leq n}(x_k - x_{k-1})$$。

* 由定義可得若$$f$$為有界變差函數，則$$V_f < \infty$$。
* 因為$$\sum(P) \geq 0$$，可得$$V_f \geq 0$$。
* $$V_f =0 \Leftrightarrow f(x) =c, \forall x \in [a,b]$$為常數。
* <mark style="color:red;">全變差就是函數的數值變化的差的總和</mark>。

### 連續可微分函數的全變差等於其微分函數的絕對積分值

> 可微分連續函數$$f: [a,b] \rightarrow \mathbb{R}$$的全變差為其弧長。
>
> $$\displaystyle  V_f(a,b)=\int_a^b |f^{'}(x)|dx$$

## 相異函數全變差的次可加性

> $$f,g$$為定義在區間$$[a,b]$$的有界變差函數。
>
> 令$$A=\sup\{ |g(x)~|~ x \in [a,b]\}$$，$$B=\sup\{ |f(x)~|~ x \in [a,b]\}$$ ，可得
>
> * $$V_{f \pm g} \leq V_f + V_g$$
> * $$V_{fg} \leq AV_f + BV_g$$

<details>

<summary>proof</summary>

令$$h(x)=f(x)g(x)$$

$$\forall P \in \mathcal{P}[a,b]$$可得

$$\begin{aligned} |\Delta h_k| & = |f(x_k)g(x_k) - f(x_{k-1})g(x_{k-1})| \\ & = |f(x_k)g(x_k) - f(x_{k-1})g(x_{k})| \\ & + |f(x_{k-1})g(x_k) - f(x_{k-1})g(x_{k-1})| \\ & \leq A|\Delta f_k| + B |\Delta g_k|  \end{aligned}$$

因此$$h$$為有界變差，可得$$V_h \leq AV_f + BV_g$$ (QED)

</details>

## 有界變差且函數值不為0的函數的倒數函數也是有界變差函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，且函數值均不為0，即$$\exists m > 0 \ni 0 < m < |f(x)| ~ \forall x \in [a,b]$$。
>
> 則$$g(x) = \frac{1}{f(x)}$$在區間$$[a,b]$$也為有界變差函數且$$V_g \leq \frac{V_f}{m^2}$$

<details>

<summary>proof</summary>

$$|\Delta g_k|=\left| \frac{1}{f(x_k)} - \frac{1}{f(x_{k-1})} \right|=\left|  \frac{\Delta f_k}{f(x_k)f(x_{k-1})} \right| \leq \frac{|\Delta f_k|}{m^2}$$(QED)

</details>

## 全變差函數定義域區間的可加性

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數。
>
> 假設$$c \in (a,b)$$，則$$f$$在區間$$[a,c]$$與$$[c,b]$$也為有界全變差函數且滿足 $$V_f(a,b) = V_f(a,c)+V_f(c,b)$$

<details>

<summary>proof</summary>

首先證明$$f$$在區間$$[a,c]$$與$$[c,b]$$也為有界變差函數。

令$$P_1, P_2$$分別為區間$$[a,c]$$與$$[c,b]$$的分割，令$$P_0 = P_1 \cup P_2$$為$$[a,b]$$的分割。

令$$\sum(P)=\sum_{k=1}^n | \Delta f_k|$$為區間$$[a,b]$$使用分割$$P$$後，函數$$f$$的變差之和。

可得$$\sum({P_1}) + \sum(P_2) = \sum(P_0) \leq V_f(a,b)$$

因此$$\sum({P_1}) , \sum(P_2)$$之值均為有界。

因為有界變差函數為有界函數，所以$$f$$在區間$$[a,c]$$與$$[c,b]$$為有界變差函數 (QED 1)

可得$$V_f(a,c) + V_f(c,b) \leq V_f(a,b)$$--(1)

令$$P=\{x_0, x_1, \dots, x_n\} \in \mathcal{P}[a,b]$$且令$$P_0 = P \cup c, ~ c \in [x_{k-1},x_k]$$為一組新的分割。

可得不等式 $$|f(x_k ) - f(x_{k-1})| \leq |f(x_k) - f(c)|+|f(c) - f(x_{k-1})|$$

即$$\sum(P) \leq \sum(P_0)$$。

令$$P_1 = \{a=x_0, \dots, c\}$$且$$P_2=\{c, \dots, x_n=b]$$，則上式可改寫為：

$$\sum(P) \leq \sum(P_0) = \sum(P_1) + \sum(P_2) \leq v_f(a,c) + V_f (c,b)$$

即$$V_f(a,c)+V_f(c,b)$$為$$\sum(P)$$的上界，$$\forall P \in \mathcal{P}[a,b]$$。

而$$\sum(P)$$的最小上界為$$V_f(a,b)$$， 因此可得$$V_f(a,b) \leq V_f(a,c) + V_f(c,b)$$  --(2) (QED 2)

由(1,2)可得$$V_f(a,b)  = V_f(a,c) + V_f(c,b)$$ (QED)

</details>

## 全變差函數之值為0若且唯若為常數函數

> 給定$$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數。則 $$V_f(a,b)=0 \Leftrightarrow f(x)=c$$。

## 全變差函數值為函數兩端點差值時為遞增函數

> 給定$$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，若$$V_f(a,b)=f(b)-f(a)$$，則$$f$$為遞增函數。

## 全變差函數以終點為函數的性質

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數。
>
> 定義函數$$V(x)=V_f(a,x), ~ a < x \leq b, ~V(a)=0$$ ，則可得：
>
> 1. $$V$$在區間$$[a,b]$$為遞增函數。\[總變動量遞增]
> 2. $$V-f$$在區間$$[a,b]$$為遞增函數。&#x20;
> 3. <mark style="color:red;">有界變差函數</mark>$$f = V - (V-f)$$<mark style="color:red;">為遞增函數與遞增函數之差值，但此分解法不唯一</mark>。

<details>

<summary>proof</summary>

proof 1

若$$a < x < y \leq b$$，由全變差函數定義域區間的可加性得$$V_f(a,y)=V_f(a,x)+V_f(x,y)$$。

整理可得$$V(y)-V(x)=V_f(x,y) \geq 0$$

所以$$V(x) \leq V(y)$$ (QED)

proof 2

令$$D(x)=V(x) - f(x), ~ x \in [a,b]$$

若$$a \leq x < y \leq b$$可得 $$D(y) - D(x) = V(y) - V(x) -[f(y) - f(x)]=V_f(x,y) - [f(y) - f(x)]$$

由全變差的定義可得$$f(y) - f(x) \leq V_f(x,y)$$

因此$$D(y) - D(x) \geq 0$$，即$$D(y) \geq D(x)$$ (QED)

</details>

## Jordan分解定理(有界變差函數若且唯若可分解為二個遞增函數的差值)

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數 $$\Leftrightarrow$$ $$f$$可分解為兩個遞增函數的差值
>
> 遞增函數的分解法不唯一。
>
> 可分解為：$$f=V-(V-f)$$。

<details>

<summary>proof </summary>

\=> 由 全變差函數以終點為函數的性質3，可得$$f = V - (V-f)$$ (QED)

<=&#x20;

令$$f = f_1 - f_2$$，$$f_1, f_2$$在區間$$[a,b]$$均為遞增函數。

由「單調函數為有界變差函數」可得 $$f_1, f_2$$為有界變差函數，即$$\exists M_1 >0 \ni V_{f_1} <\infty$$且$$\exists M_2 >0 \ni V_{f_2} <\infty$$。

由「相異函數全變差的次可加性」可得 $$V_{f_1 - f_2} \leq V_{f_1} + V_{f_2} < M_1 +M_2$$ (QED)

</details>

## 有界變差連續函數若且唯若全變差函數為連續函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數。
>
> 令$$V_f(x)=V_f(a,x), ~x \in [a,b]$$且$$V(a)=0$$。
>
> 若$$f$$在點$$c\in [a,b]$$連續 $$\Leftrightarrow$$ $$V_f$$在點$$c$$連續。

## 有界變數函數幾乎處處可微分

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，令$$V_f(x)=V_f(a,x), x \in [a,b]$$，
>
> 則$$\frac{dV_f(x)}{dx}=|f^{'}(x)|, ~ \text{a.e. } x \in [a,b]$$。

## 有界變差函數序列若收斂也為有界變差函數

> $$f_k: [a,b] \rightarrow \mathbb{R}, ~ k \in \mathbb{N}$$為有界變差函數且有$$V_{f_k}(a,b) \leq M, \forall k$$。
>
> 若$$\displaystyle \lim_{k \rightarrow \infty} f_k(x) = f(x), ~ x \in [a,b]$$，則$$f$$在$$[a,b]$$為有界變差函數且$$V_f(a,b) \leq M$$。
