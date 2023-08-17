# 變差(bounded variation)

## 簡介

一般函數可由變差拆解成連續函數+純跳躍函數之和。

布朗運動的一次變差不存在，二次變差為有限值。

## 遞增函數的有限分割的總跳躍量小於值域之差

> 令函數$$f: [a,b] \rightarrow \mathbb{R}$$為遞增函數。
>
> 令$$x_0, x_1, \dots, x_n$$為閉區間$$[a,b]$$的一組有限分割且滿足$$a=x_0 < x_1 < \dots <x_n=b$$
>
> 則可得不等式 $$\sum_{k=1}^{n-1} [f({x_{k+})} - f({x_{k-}})] \leq f(b) - f(a)$$
>
> <mark style="color:blue;">其中</mark>$$f({x_{k+})} - f({x_{k-}})$$<mark style="color:blue;">為函數</mark>$$f$$<mark style="color:blue;">在點</mark>$$x_k$$<mark style="color:blue;">的跳躍量(jump)。</mark>

<details>

<summary>proof</summary>

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

即$$S_m$$內集合點的總變動量的上限為$$f(b) - f(a)$$，所以$$n<\infty$$，因此$$S_m$$為有限集合。

而函數$$f$$在開區間$$(a,b)$$的不連續點為$$\displaystyle \bigcup_{m=1}^\infty S_m$$的子集合，因此$$f$$上不連續點為可數個。(QED)

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

> 定義：有界變差函數
>
> 給定函數$$f: [a,b] \rightarrow \mathbb{R}$$與分割$$P \in \mathcal{P}[a,b]$$。
>
> 令$$\Delta f_k = f(x_k) - f(x_{k-1}), ~ k =1,2,\dots, n$$。
>
> 若存在正實數$$M > 0 \ni \sum_{k=1}^n | \Delta f(x_k)| \leq M$$，$$\forall \text{ paritition } P \in \mathcal{P}[a,b]$$，則稱$$f$$在區間$$[a,b]$$為有界變差函數。

### 單調函數為有界變差函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為單調函數，則$$f$$在$$[a,b]$$為有界變差函數。

<details>

<summary>proof</summary>

不失一般性令$$f$$為遞增函數。

對於所有分割$$P \in \mathcal{P}[a,b]$$，遞增函數可得$$\Delta f_k=f(x_k) - f(x_{k-1}) \geq 0$$。

因此$$\sum_{k=1}^n | \Delta f_k | = \sum_{k=1}^n \Delta f_k = \sum_{k=1}^n [f(x_k) - f(x_{k=1})]=f(b) -f(a)$$ (QED)

</details>

### 連續可微分且微分值有限的函數為有界變差函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為連續函數且$$f'(x)$$在$$(a,b)$$可微分。
>
> 若$$f'(x)$$在$$(a,b)$$有界，即$$\exists M > 0 \ni |f^{'}(x)| \leq M ~\forall x \in (a,b)$$，
>
> 則$$f$$在$$[a,b]$$為有界變差函數。

<details>

<summary>proof</summary>

由微分均值定理可得$$\Delta f_k= f(x_k) - f(x_{k-1} )= f^{'}(t_k)(x_k - x_{k-1}), ~ t_k \in (x_{k-1}, x_k)$$

因此可得$$\sum_{k=1}^n |\Delta f_k| = \sum_{k=1}^n |f^{'}(t_k)| \Delta x_k \leq M \sum_{k=1}^n \Delta x_k = A(b-a)$$ (QED)

</details>

### 範例：連續函數但非有界變差函數

$$f(x)=x \cos[\frac{\pi}{2x}]$$，$$if x \neq 0, f(0)=0$$。則$$f$$在$$[0,1]$$連續。

若考慮分割$$P=\{0, \frac{1}{2n}, \frac{1}{2n-1}, \dots, \frac{1}{3}, \frac{1}{2}, 1\}$$

可得變差$$\sum_{k=1}^2n |\Delta f_k| = \frac{1}{2n}+\frac{1}{2n} + \frac{1}{2n-2}+\frac{1}{2n-2}+\dots +\frac{1}{2} + \frac{1}{2} = 1+ \frac{1}{2} +\dots + \frac{1}{n}$$

但並非對所有$$n$$收斂，如$$\sum_{n=1}^\infty \frac{1}{n}$$發散。

此例中$$f{'}$$在$$(0,1)$$存在，但並非有界。

### 範例：微分值有限函數不一定為有界變差函數

$$f(x)=x^{1/3}$$在任意有限區間為單調函數，因此為有界變差函數。

但在$$x \rightarrow \infty$$時，$$f'(x) \rightarrow \infty$$。

## 有界變差函數為有界函數

> $$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，即$$\exists M > 0 \ni \sum |\Delta f_k| \leq M$$，$$\forall P \in \mathcal{P}[a,b]$$，則$$f$$為有界函數，即$$\exists N > 0 \ni f(x) \leq N, \forall x \in [a,b]$$。

<details>

<summary>proof</summary>

令$$x \in (a,b)$$

考慮分割$$P=\{a,x,b\}$$可得 $$|f(x) - f(a)| + |f(b) - f(x) | \leq M$$

即$$|f(x) - f(a)| \leq M$$，$$|f(x)| \leq |f(a)| + M$$

在$$x=a$$或$$x=b$$時也可得到相同不等式(QED)

</details>

## 全變差(total variation)

> 給定$$f: [a,b] \rightarrow \mathbb{R}$$為有界變差函數，令$$\sum(P)=\sum_{k=1}^n | \Delta f_k|$$為區間$$[a,b]$$使用分割$$P=\{x_0, x_1, \dots ,x_n\}$$的變差之和。
>
> 定義$$V_f(a,b) = \sup \{ \sum(P) ~|~ P \in \mathcal{P}[a,b]\}$$為區間$$[a,b]$$的全變差。
>
> 通常簡寫為$$V_f$$

* 由定義可得因為$$f$$為有界變差函數，所以$$V_f < \infty$$。
* 因為$$\sum(P) \geq 0$$，可得$$V_f \geq 0$$。
* $$V_f =0 \Leftrightarrow f(x) =c, \forall x \in [a,b]$$為常數。
