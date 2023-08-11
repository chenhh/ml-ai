# 級數(series)

## 簡介

* 實數中的級數為(有限或無限)數列的總和，可分為**收斂**與**發散級數**二類。
* <mark style="color:red;">只需考慮正項級數（與負項級數，非負項級數等價）與交錯級數的收斂性質即可</mark>。
* 積分是無窮項的總和，其收斂性有時可用級數判斷。

審斂法(tests for convergence)有：篩審斂法(screen test)，Cauchy審斂法，絕對值審斂法，正項級數審斂法，積分審斂法，比較審斂法，極限比較審斂法，交錯級數審斂法，Dirichlet審斂法，比值審斂法，根式審斂法。

### 收斂條件整理

* 絕對收斂（$$\sum_{k=1}^\infty |x_k|$$收斂）$$\subseteq$$條件收斂（$$\sum_{k=1}^\infty |x_k|$$發散、$$\sum_{k=1}^\infty x_k$$收斂）$$\subseteq$$數列收斂至0（$$\displaystyle \lim_{n \rightarrow \infty} x_n = 0$$）。
* \[充要條件]任意級數$$\sum_{k=1}^\infty x_k$$收斂$$\Leftrightarrow$$部份和數列為Cauchy數列。
* \[必要條件]任意級數$$\sum_{k=1}^\infty x_k$$收斂$$\Rightarrow \displaystyle \lim_{n \rightarrow \infty} x_n =0$$。
* 任意級數絕對收斂（$$\sum_{k=1}^\infty |x_k|$$）$$\Rightarrow$$級數$$\sum_{k=1}^\infty x_k$$收斂。
* 若$$\exists n_0 \in \mathbb{N} \ni |x_n| \leq |y_n|, \forall n \geq n_0$$，則$$\sum_{k=1}^\infty |y_k|$$收斂$$\Rightarrow \sum_{k=1}^\infty |x_k|$$收斂。
* 若$$\displaystyle \lim_{n \rightarrow \infty} \left|  \frac{x_n}{y_n}\right| = L \in \mathbb{R}, L \neq0$$，則$$\sum_{k=1}^\infty |y_k|$$收斂$$\Leftrightarrow \sum_{k=1}^\infty |x_k|$$收斂。
* $$f:[1,\infty) \rightarrow \mathbb{R}^{+}$$為遞減函數，$$x_n = f(n)$$，則$$\sum_{k=1}^\infty x_k$$收斂$$\Leftrightarrow$$$$\int_1^\infty f(x)dx$$收斂。
* $$\forall n,~ 0 < x_n \leq y_n$$，若$$\sum_{k=1}^\infty y_k$$收斂$$\Rightarrow \sum_{k=1}^\infty x_k$$收斂。
* $$\forall n,~ 0 < x_n \leq y_n$$, $$\displaystyle \lim_{n \rightarrow \infty}   \frac{x_n}{y_n} = L \in \mathbb{R}, L \neq0$$，則$$\sum_{k=1}^\infty y_k$$收斂$$\Leftrightarrow \sum_{k=1}^\infty x_k$$收斂。
* $$\forall n, x_n \neq 0, ~ \displaystyle \lim_{n \rightarrow \infty } |\frac{x_{n+1}}{x_n}|=p$$，則$$0 \leq p < 1 \Rightarrow \sum_{k=1}^\infty |x_k|$$收斂。

## 級數與部份和

> 令 $$\{ x_n \} \subset \mathbb{R}$$為數列(sequence)，定義級數(series)為 $$\sum_{i=1}^{\infty} x_i = x_1 + x_2 + \ldots$$。定義部份和(partial sum ) $$\displaystyle s_n  = \sum_{i=1}^n x_i = x_1 +x _2 + \ldots + x_n$$。

可定義部份和數列$$\{s_n \} \equiv \{ s_1, s_2, \ldots, s_n \ldots \}$$。則級數可用部份和分析是否收斂，即 $$\displaystyle \lim_{n \rightarrow \infty} s_n =  \lim_{n \rightarrow \infty} \sum_{i=1}^n x_i$$。

* 如果 $$\{ s_n \}$$收斂 (convergence)，則 $$\displaystyle \exists s \in \mathbb{R} \ni \lim_{n \rightarrow \infty} s_n = s$$
* 如果$$\{ s_n\}$$不收斂，則為發散(divergence)。
*   級數的極限值等於部份和的極限值.

    級數收斂等價於部份和序列收斂



### 收斂(發散)級數即使去除掉有限項仍為收斂(發散)級數

> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 收斂 $$\Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$收斂
> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 發散 $$\Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$發散
>
> 級數是否收斂(發散)不是依據前面有限項的部份和，而是無窮多項的元素和有關。
>
>

proof:=>

* 令部份和  $$\displaystyle s_n = \sum_{i=1}^n x_i$$
* 因為$$\displaystyle \sum_{i=1}^{\infty} x_i$$收斂，令$$\displaystyle \lim_{ n \rightarrow \infty} s_n  = \lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i=s$$收斂。
* 因為$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i = \lim_{ n \rightarrow \infty}  \left(\sum_{i=1}^{k-1} x_i + \sum_{i=k}^n x_i \right) = \sum_{i=1}^{k-1} x_i +  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s$$
* 因此$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i =  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s -  \sum_{i=1}^{k-1} x_i$$收斂
* (QED)

proof: <= 使用相同的方法可得證。(QED)

### 級數為線性算子

> 若 $$\displaystyle \sum_{k=1}^\infty x_k =a$$ 且 $$\displaystyle \sum_{k=1}^\infty y_k =b,  \forall s,t \in \mathbb{R}$$, 則> ：$$\displaystyle \sum_{k=1}^\infty (s\cdot x_k + t \cdot y_k) =s\cdot a + t \cdot b$$

proof:

* 因為$$\displaystyle \sum_{k=1}^n (sx_k + ty_k) =  s\cdot\sum_{k=1}^n x_k + t\cdot  \sum_{k=1}^n y_k$$
* 所以$$\begin{align} \displaystyle \lim_{ n \rightarrow \infty}  \sum_{k=1}^n (sx_k + ty_k) &= s\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n x_k + t\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n y_k \\&=  s a + tb \end{align}$$(QED)

外顯級數和內隱級數(apparent series and concealed series)


> 令收斂級數 $$\displaystyle \sum_{k=1}^\infty x_k =x$$
>
> * 若有方法可得到$$x$$之值，則稱級數$$\displaystyle \sum_{k=1}^\infty x_k$$為一外顯級數>   。
> * 若無法得到$$x$$之值，則稱級數$$\displaystyle \sum_{k=1}^\infty x_k$$為內隱級數>   。

### 望遠鏡級數(telescoping series)為外顯級數

> $$\displaystyle \sum_{k=1}^\infty \frac{1}{k(k+1)} =1$$

* 令$$s_n = \frac{1}{1\cdot 2} + \frac{1}{2\cdot 3}+ \ldots + \frac{1}{n\cdot (n+1)} = (1 - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3})+ \ldots + (\frac{1}{n} - \frac{1}{n+1}) = 1 - \frac{1}{n+1}$$
* 可得 $$\displaystyle  \lim_{n \rightarrow \infty} s_n =  \lim_{n \rightarrow \infty}(1 - \frac{1}{n+1})=1$$

## 幾何級數、等比級數(geometric, common ratio series)

>> $$a \neq 0$$, 則形式為$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k=a+ax+ax^2+\ldots+ax^n+ \ldots$$稱為幾何級數。

### &#x20;幾何級數必為外顯級數

> $$\displaystyle  \sum_{k=0}^\infty a\cdot x^k=a+ax+ax^2+\ldots+ax^n+ \ldots, ~ a \neq 0$$
>
> * 若$$|x|<1$$，則$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k = \frac{a}{1-x}$$
> * 若$$|x| \geq 1$$ ，則$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k$$ 發散

proof:

* 部份和 $$s_n = \displaystyle  \sum_{k=0}^n a\cdot x^k = a+ ax + ax^2 +\cdots + ax^n = \frac{a(1-x)^n}{1-x}$$
* 若$$|x| <1$$，則$$\displaystyle \lim_{n \rightarrow \infty} s_n = \frac{a}{1-x}$$。
* 若$$|x| \geq 1$$，則$$|a| \leq |ax| \leq |ax^2| \leq \cdots$$
* 因此若 $$\displaystyle \lim_{n \rightarrow \infty} |ax^k|$$存在，則可得$$\displaystyle \lim_{n \rightarrow \infty} |ax^k|  \geq \lim_{n \rightarrow \infty}|a| = |a| \neq0$$
* 而由[篩審斂法](series-convergence-test.md)得$$\displaystyle \lim_{n \rightarrow \infty} |ax^k| \neq 0$$，則級數$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k$$發散 (QED)

## 正項與交錯級數(positive terms and alternative series)

> 令$$\{x_n\}_{n \in \mathbb{N}}$$為一數列，
>
> * 若$$\forall n \in \mathbb{N}, ~ x_n>0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k$$為正項級數(positive terms series)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n\geq 0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k$$為非負項項級數(non-negative terms series)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n<0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k$$為負項級數(negative terms series)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n>0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty (-1)^{k+1} x_k$$為交錯級數(alternative series)。
> * 若$$\forall n \in \mathbb{N},  ~x_n \neq 0$$ 且滿足$$\forall n_0 \in \mathbb{N}, \exists m,l \neq n_0 \ni x_m>0, x_l<0$$ 則稱$$x_1+x_2+ \cdots+x_n+ \cdots$$為廣義交錯級數(generalized alternative series)。

### 正項級數收斂的充要條件

> 令級數 $$\displaystyle  \sum_{k=1}^\infty x_k$$  為非負項級數，若去除數列$$\{x_n\}$$中$$x_n=0$$的元素，得到數列$$\{y_n\}$$，則級數$$\displaystyle  \sum_{k=1}^\infty x_k$$   收斂若且唯若$$\displaystyle  \sum_{k=1}^\infty y_k$$   收斂，而且$$\displaystyle  \sum_{k=1}^\infty x_k  = \displaystyle  \sum_{k=1}^\infty y_k$$。

> * 此定理說明了級數收斂不必考慮非負項級數，只需考慮正項級數即可。
> * 可將序列內所有元素取負號得正項級數$$\displaystyle  \sum_{k=1}^\infty x_k$$  收斂的充要條件為負項級數 $$\displaystyle  \sum_{k=1}^\infty (-x_k )$$  收斂，因此也不用考慮負項級數，只須考慮正項級數即可。

proof:

* 令部份和$$\displaystyle  X_n=\sum_{k=1}^n x_n ,~ Y_n=\sum_{k=1}^n y_n$$ ，則依條件得$$\{Y_n\}$$為$$\{X_n\}$$的子數列。
  * 例如 $$\sum_{k=1}^\infty x_k =1+0+2+0+3+0+4+0+5+\ldots$$
  * $$\{X_n\}=\{1,1,3,3,6,6,10,10,15,\ldots\}$$
  * $$\{Y_n\}=\{1,3,6,10,15,\ldots\}$$
* proof =>
* 令$$\displaystyle \lim_{ n \rightarrow \infty} X_n=X$$，因為$$\{Y_n\}$$為$$\{X_n\}$$的子數列，可得 $$\displaystyle \lim_{ n \rightarrow \infty} Y_n=X$$ (QED)
* proof <=
* 反之令$$\displaystyle \lim_{ n \rightarrow \infty} Y_n=Y$$，依極限定義得$$\forall \epsilon > 0, ~ \exists n_0 \in \mathbb{N}   \ni  |Y_n−Y|<\epsilon, ~ \forall n \geq n_0$$
* 由於數列$$\{X_n\}$$包含了許多$$\{Y_n\}$$的重複項，因此 $$\exists m_0 \in \mathbb{N} \ni X_{m_0}=Y_{n_0}$$  且$$\forall n \geq m_0 ~ |X_n−Y|<\epsilon$$
* 因此$$\displaystyle \lim_{ n \rightarrow \infty} X_n=Y$$ (QED)

### 正項級數審斂法

> 正項級數$$\displaystyle  \sum_{k=1}^\infty x_k$$收斂的充要條件是其部份和數列$$\{S_n\}$$有上界。
>
> 註：由實數的完備性若非空集合有上界時有最小上界。

Proof:

* 令$$\displaystyle  \sum_{k=1}^\infty x_k$$  為正項級數，則其部份和序列 $$S_n=x_1+x_2+\ldots+x_n=S_{n−1}+x_n$$。
* proof =>，若$$\displaystyle  \sum_{k=1}^\infty x_k =x$$收斂，則$$\displaystyle \lim_{ n \rightarrow \infty} S_n=x$$，因此$$\{S_n\}$$有最小上界。
* proof <=，由於$$x_n > 0$$，可得$$\{S_n\}$$為嚴格遞增序列，而[嚴格遞增數列收斂的充分條件](../sequence/monotonic-sequence.md#shi-shu-zhong-de-you-jie-chan-diao-shu-lie-bi-shou-lian)是序列$$\{S_n\}$$有上界。
* 因此正項級數$$\displaystyle  \sum_{k=1}^\infty x_k$$  收斂的充要條件是其部份和序列$$\{S_n \}$$有上界。 (QED)

## p-級數

> 令$$p>0$$，則形式如$$\displaystyle \sum_{k=1}^\infty \frac{1}{k^p}$$  的級數稱為$$p$$級數。

### &#x20;p級數收斂的充要條件

> $$p>0$$，則級數 $$\displaystyle \sum_{k=1}^\infty \frac{1}{k^p}$$收斂若且唯若 $$p>1$$。

Proof (積分審斂法)

* 給定函數$$f:[1, \infty) \rightarrow \mathbb{R}$$，且$$\forall x \in [1, \infty), f(x)=\frac{1}{x^p}$$, 則$$\forall x \in [1,\infty), f(x)>0$$ 且$$f(x)$$為嚴格遞減函數。
* $$\displaystyle \int_1^n \frac{1}{x^p}dx=\left\{    \begin{align}  &\frac{n^{1-p}-1}{1-p} &\text{ if } p \neq 1 \\ & \ln n &\text{ if } p=1  \end{align}  \right.$$
* 因此當
  * $$p>1, \displaystyle \lim_{n \rightarrow \infty}\int_1^n\frac{1}{x^p}  dx=\frac{1}{p−1}$$
  * $$p=1, \displaystyle \lim_{n \rightarrow \infty}\int_1^n\frac{1}{x^p}  dx=\infty$$
  * $$0<p<1, \displaystyle \lim_{n \rightarrow \infty}\int_1^n\frac{1}{x^p}  dx= \infty$$(QED)

## α-級數

> 令$$\alpha>0$$，則形式如$$\displaystyle \sum_{k=3}^\infty \frac{1}{k (\ln k)^\alpha}$$  的級數稱為$$\alpha$$級數。

### &#x20;α-級數收斂的充要條件

> 令$$\alpha>0$$，則級數$$\displaystyle \sum_{k=3}^\infty \frac{1}{k (\ln k)^\alpha}$$  收斂若且唯若$$\alpha > 1$$。

Proof (積分審斂法)

* 給定函數$$f:[1, \infty) \rightarrow \mathbb{R}$$，且$$\forall x \in [3, \infty), f(x)=\frac{1}{x (\ln ⁡x)^\alpha}$$, 則  $$\forall x \in [3, \infty), f(x)>0$$ 且$$f(x)$$為嚴格遞減函數。
* $$n > 3, \displaystyle \int_3^n \frac{1}{x(\ln x)^\alpha} dx = \int_3^n \frac{1}{(\ln x)^\alpha} d(\ln x)$$

$$=\left \{  \begin{align} &\frac{ (\ln n)^{1-\alpha} - (\ln 3)^{1-\alpha}}{1-\alpha} &\text{ if } \alpha \neq 1, \\ &\ln (\ln x)|_3^n = \ln (\ln n) - \ln(\ln 3)& \text{ if } \alpha \neq 1 \end{align} \right.$$&#x20;

* 若$$\alpha>1, \displaystyle \lim_{n \rightarrow \infty} \int_3^n  \frac{1}{(x(\ln ⁡x )^\alpha} dx= \frac{(\ln ⁡3 )^{1−α}}{α−1}$$
* 若$$\alpha=1, \displaystyle \lim_{n \rightarrow \infty} \int_3^n  \frac{1}{(x(\ln ⁡x )^\alpha} dx=\infty$$
* 若$$0<\alpha<1,  \displaystyle \lim_{n \rightarrow \infty} \int_3^n  \frac{1}{(x(\ln ⁡x )^\alpha} dx=\infty$$ (QED)

### 範例&#xD;

* 級數 $$\displaystyle  \sum_{k=1}^\infty \frac{1}{k^2}$$   與級數 $$\displaystyle  \sum_{k=3}^\infty \frac{1}{ k (\ln k)^{1.5}}$$  收斂
* 級數$$\displaystyle  \sum_{k=1}^\infty \frac{1}{k}$$ 與級數 $$\displaystyle  \sum_{k=3}^\infty \frac{1}{ k (\ln k)}$$   發散
* 級數$$\displaystyle  \sum_{k=1}^\infty \frac{1}{k^{0.1}}$$   與級數$$\displaystyle  \sum_{k=3}^\infty \frac{1}{ k (\ln k)^{0.99}}$$  發散。



