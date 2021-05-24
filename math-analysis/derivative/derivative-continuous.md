# 導數連續性質

## 連續函數的條件

對於函數$$f: [a,b] \rightarrow \mathbb{R}$$

* 連續可微分$$\subseteq$$Lipschitz連續$$\subseteq$$均勻連續（uniform continuous）
  * $$\subseteq$$點態連續（pointwise continuous）
* Lipschitz連續$$\subseteq$$絕對連續$$\subseteq$$有界變分$$\subseteq$$幾乎處處可微分

![&#x9023;&#x7E8C;&#x53EF;&#x5FAE;&#x5206;&#x51FD;&#x6578;&#x689D;&#x4EF6;&#x6700;&#x56B4;&#x683C;](../../.gitbook/assets/continuous_func-min.png)

## 導數點態連續\(derivative pointwise continuous\)

> * 函數$$f:(a,b) \rightarrow \mathbb{R}$$ 在點$$c  \in (a,b)$$均可以微分，則$$f$$在點$$c$$連續。
> * 此為可微分必連續的充分條件（sufficient condition）。
>
> 可得若$$\forall c \in (a,b)$$, 函數$$f$$均可微分，則函數$$f$$在區間$$(a,b)$$為連續函數。

* $$f(x)=f(c)+ \frac{f(x) - f(c)}{x-c}(x-c)$$
* $$\lim_{x \rightarrow c}f(x)=f(c) + \lim_{ x\rightarrow c}(\frac{f(x)-f(c)}{x-c})\lim_{ x\rightarrow c}{x-c}=f(c)+f^{'}(c)\cdot 0=f(c)$$\(QED\)

### 連續不一定可微分

> $$f(x)=|x|$$在$$x=0$$連續，但微分不存在。

![&#x7D55;&#x5C0D;&#x503C;&#x51FD;&#x6578;](../../.gitbook/assets/abs_func.png)

 $$\lim_{x \rightarrow 0^{-}} |x| = \lim_{x \rightarrow 0^{+}} |x|=0$$，所以在$$x=0$$連續。

$$\lim_{x \rightarrow 0^{-}} \frac{|x| - 0}{x} = -1$$，$$\lim_{x \rightarrow 0^{+}} \frac{|x| - 0}{x} = 1$$，左導數不等於右導數，所以在$$x=0$$不可微分。

## 左右導數點態連續

> 函數$$f:(a,b) \rightarrow \mathbb{R} , c \in (a,b)$$
>
> * 若$$f$$在點$$c$$的左導數和右導數存在（不必相等），則$$f$$在點$$c$$連續。
> * 若$$\forall c \in (a,b)$$, 函數$$f$$的左、右導數均存在，則函數$$f$$在區間$$(a,b)$$為連續函數。

* $$\displaystyle \lim_{x \rightarrow c^− }⁡(f(x)−f(c))= \lim_{x \rightarrow c^− }⁡ \frac{f(x)−f(c)}{(x−c)} (x−c)=\lim_{x \rightarrow c^−}\frac{f(x)−f(c)}{(x−c)} \cdot \lim_{x \rightarrow c^−} ⁡(x−c)=f_−^′ (c)⋅0=0 $$
* $$\displaystyle \lim_{x \rightarrow c^− }⁡(f(x)−f(c))= \lim_{x \rightarrow c^+ }⁡ \frac{f(x)−f(c)}{(x−c)} (x−c)=\lim_{x \rightarrow c^+}\frac{f(x)−f(c)}{(x−c)} \cdot \lim_{x \rightarrow c^+} ⁡(x−c)=f_+^′ (c)⋅0=0 $$
* 則$$\lim_{x \rightarrow c}⁡f(x)=f(c)$$ \(QED\)

## 利普希茨（Lipschitz）條件

> 稱函數$$f$$在點$$c$$滿足$$\alpha$$階的利普希茨條件，若存在常數$$M>0$$\(可能會依賴於$$c$$而不同\)使得 $$|f(x)-f(c)| < M |x-c|^{\alpha}$$, $$x\neq c$$且$$x \in Ball(c)$$
>
> 若對於$$f: S \rightarrow \mathbb{R}$$定義域$$S$$中任意兩點$$a,b$$，若存在常數$$M>0$$滿足$$|f(a)-f(b)|< M|a-b|^{\alpha}~ \forall a,b\in S$$時，稱$$f$$在$$S$$為利普希茨連續。

* 一般應用時是考慮$$α=1$$的條件，即函數$$f$$的斜率為有限值。
* **利普希茨連續，要求函數圖像的曲線上，任意兩點連線的斜率均有界且都小於同一個常數，這個常數就是利普希茨常數**。
* 對於利普希茨連續函數$$f$$，滿足條件的最小常數$$M$$稱為其**利普希茨常數，即函數斜率的最大值（最陡的部份）**。
* 若$$M<1$$時，稱$$f$$為收縮映射。

![Lipschitz&#x689D;&#x4EF6;&#xFF0C;&#x5B58;&#x5728;&#x6709;&#x4E00;&#x500B;&#x767D;&#x8272;&#x6C99;&#x6F0F;&#xFF0C;&#x4F7F;&#x5F97;&#x51FD;&#x6578;&#x4E00;&#x5B9A;&#x80FD;&#x901A;&#x904E;&#x6C99;&#x6F0F;&#x7684;&#x6B63;&#x4E2D;&#x9593;](../../.gitbook/assets/lipschitz_condition.png)





