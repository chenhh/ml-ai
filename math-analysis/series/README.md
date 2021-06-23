# 級數\(series\)

## 簡介

實數中的級數為\(有限或無限\)數列的總和，可分為**收斂**與**發散級數**二類。

審斂法\(tests for convergence\)有：篩審斂法\(screen test\)，Cauchy審斂法，絕對值審斂法，正項級數審斂法，積分審斂法，比較審斂法，極限比較審斂法，交錯級數審斂法，Dirichlet審斂法，比值審斂法，根式審斂法。

## 級數與部份和

> 令 $$\{ x_n \} \subset \mathbb{R}$$為數列\(sequence\)，定義級數\(series\)為 $$\sum_{i=1}^{\infty} x_i = x_1 + x_2 + \ldots$$。定義部份和\(partial sum \) $$\displaystyle s_n  = \sum_{i=1}^n x_i = x_1 +x _2 + \ldots + x_n $$。

可定義部份和數列$$\{s_n \} \equiv \{ s_1, s_2, \ldots, s_n \ldots \}$$。則級數可用部份和分析是否收斂，即 $$\displaystyle \lim_{n \rightarrow \infty} s_n =  \lim_{n \rightarrow \infty} \sum_{i=1}^n x_i$$。

* 如果 $$\{ s_n \} $$收斂 \(convergence\)，則 $$\displaystyle \exists s \in \mathbb{R} \ni \lim_{n \rightarrow \infty} s_n = s$$
* 如果$$\{ s_n\}$$不收斂，則為發散\(divergence\)。
* 級數的極限值等於部份和的極限值.

  級數收斂等價於部份和序列收斂

### 收斂\(發散\)級數即使去除掉有限項仍為收斂\(發散\)級數

> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 收斂 $$ \Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$收斂
> * $$\displaystyle \sum_{i=1}^{\infty} x_i$$ 發散 $$ \Leftrightarrow$$$$\displaystyle \sum_{i=k}^\infty x_i$$發散
>
> 級數是否收斂\(發散\)不是依據前面有限項的部份和，而是無窮多項的元素和有關。

proof:=&gt;

* 令部份和  $$\displaystyle s_n = \sum_{i=1}^n x_i$$
* 因為$$\displaystyle \sum_{i=1}^{\infty} x_i$$收斂，令$$\displaystyle \lim_{ n \rightarrow \infty} s_n  = \lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i=s$$收斂。
* 因為$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i = \lim_{ n \rightarrow \infty}  \left(\sum_{i=1}^{k-1} x_i + \sum_{i=k}^n x_i \right) = \sum_{i=1}^{k-1} x_i +  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s$$
* 因此$$\displaystyle\lim_{ n \rightarrow \infty} \sum_{i=1}^n x_i =  \lim_{ n \rightarrow \infty}  \left(\sum_{i=k}^n x_i \right)  = s -  \sum_{i=1}^{k-1} x_i$$收斂
* \(QED\)

proof: &lt;= 使用相同的方法可得證。\(QED\)

### 級數為線性算子

> 若 $$\displaystyle \sum_{k=1}^\infty x_k =a$$ 且 $$\displaystyle \sum_{k=1}^\infty y_k =b,  \forall s,t \in \mathbb{R}$$, 則：$$\displaystyle \sum_{k=1}^\infty (s\cdot x_k + t \cdot y_k) =s\cdot a + t \cdot b$$

proof:

* 因為$$\displaystyle \sum_{k=1}^n (sx_k + ty_k) =  s\cdot\sum_{k=1}^n x_k + t\cdot  \sum_{k=1}^n y_k$$
* 所以$$\begin{align} \displaystyle \lim_{ n \rightarrow \infty}  \sum_{k=1}^n (sx_k + ty_k) &= s\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n x_k + t\cdot \lim_{ n \rightarrow \infty}  \sum_{k=1}^n y_k \\&=  s a + tb \end{align}$$\(QED\)

## 外顯級數和內隱級數\(apparent series and concealed series\)

> 令收斂級數 $$\displaystyle \sum_{k=1}^\infty x_k =x $$
>
> * 若有方法可得到$$x$$之值，則稱級數$$\displaystyle \sum_{k=1}^\infty x_k$$為一外顯級數  。
> * 若無法得到$$x$$之值，則稱級數$$\displaystyle \sum_{k=1}^\infty x_k$$為內隱級數  。

### 望遠鏡級數\(telescoping series\)為外顯級數

> $$\displaystyle \sum_{k=1}^\infty \frac{1}{k(k+1)} =1$$

* 令$$s_n = \frac{1}{1\cdot 2} + \frac{1}{2\cdot 3}+ \ldots + \frac{1}{n\cdot (n+1)} = (1 - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3})+ \ldots + (\frac{1}{n} - \frac{1}{n+1}) = 1 - \frac{1}{n+1}$$
* 可得 $$\displaystyle  \lim_{n \rightarrow \infty} s_n =  \lim_{n \rightarrow \infty}(1 - \frac{1}{n+1})=1$$

## 幾何級數、等比級數\(geometric, common ratio series\)

> $$a \neq 0$$, 則形式為$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k=a+ax+ax^2+\ldots+ax^n+ \ldots$$稱為幾何級數。

###  幾何級數必為外顯級數

> $$\displaystyle  \sum_{k=0}^\infty a\cdot x^k=a+ax+ax^2+\ldots+ax^n+ \ldots, ~ a \neq 0$$
>
> * 若$$|x|<1$$，則$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k = \frac{a}{1-x}$$
> * 若$$|x| \geq 1$$ ，則$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k$$ 發散

proof:

* 部份和 $$s_n = \displaystyle  \sum_{k=0}^n a\cdot x^k = a+ ax + ax^2 +\cdots + ax^n = \frac{a(1-x)^n}{1-x}$$
* 若$$|x| <1$$，則$$\displaystyle \lim_{n \rightarrow \infty} s_n = \frac{a}{1-x}$$。
* 若$$|x| \geq 1$$，則$$|a| \leq |ax| \leq |ax^2| \leq \cdots$$
* 因此若 $$\displaystyle \lim_{n \rightarrow \infty} |ax^k|$$存在，則可得$$\displaystyle \lim_{n \rightarrow \infty} |ax^k|  \geq \lim_{n \rightarrow \infty}|a| = |a| \neq0$$
* 而由[篩審斂法](series-convergence-test.md)得$$\displaystyle \lim_{n \rightarrow \infty} |ax^k| \neq 0$$，則級數$$\displaystyle  \sum_{k=0}^\infty a\cdot x^k$$發散 \(QED\)

## 交錯級數\(alternative series\)

> 令$$\{x_n\}_{n \in \mathbb{N}}$$為一數列，
>
> * 若$$\forall n \in \mathbb{N}, ~ x_n>0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k $$為正項級數\(positive terms series\)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n\geq 0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k $$為非負項項級數\(non-negative terms series\)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n<0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty x_k $$為負項級數\(negative terms series\)。
> * 若$$\forall n \in \mathbb{N}, ~ x_n>0$$ 則稱級數$$\displaystyle  \sum_{k=1}^\infty (-1)^{k+1} x_k $$為交錯級數\(alternative series\)。
> * 若$$\forall n \in \mathbb{N},  ~x_n \neq 0$$ 且滿足$$\forall n_0 \in \mathbb{N}, \exists m,l \neq n_0 \ni x_m>0, x_l<0$$ 則稱$$x_1+x_2+ \cdots+x_n+ \cdots$$為廣義交錯級數\(generalized alternative series\)。

### 正項級數收斂的充要條件

> 令級數 $$\displaystyle  \sum_{k=1}^\infty x_k $$  為非負項級數，若去除數列$$\{x_n\}$$中$$x_n=0$$的元素，得到數列$$\{y_n\}$$，則級數$$\displaystyle  \sum_{k=1}^\infty x_k $$   收斂若且唯若$$\displaystyle  \sum_{k=1}^\infty y_k $$   收斂，而且$$\displaystyle  \sum_{k=1}^\infty x_k  = \displaystyle  \sum_{k=1}^\infty y_k$$。

> * 此定理說明了級數收斂不必考慮非負項級數，只需考慮正項級數即可。
> * 可將序列內所有元素取負號得正項級數$$\displaystyle  \sum_{k=1}^\infty x_k $$  收斂的充要條件為負項級數 $$\displaystyle  \sum_{k=1}^\infty (-x_k )$$  收斂，因此也不用考慮負項級數，只須考慮正項級數即可。

proof:

* 令部份和$$\displaystyle  X_n=\sum_{k=1}^n x_n ,~ Y_n=\sum_{k=1}^n y_n$$ ，則依條件得$$\{Y_n\}$$為$$\{X_n\}$$的子數列。
  * 例如 $$\sum_{k=1}^\infty x_k =1+0+2+0+3+0+4+0+5+\ldots$$
  * $$\{X_n\}=\{1,1,3,3,6,6,10,10,15,\ldots\}$$
  * $$\{Y_n\}=\{1,3,6,10,15,\ldots\}$$
* proof =&gt;
* 令$$\displaystyle \lim_{ n \rightarrow \infty} X_n=X$$，因為$$\{Y_n\}$$為$$\{X_n\}$$的子數列，可得 $$\displaystyle \lim_{ n \rightarrow \infty} Y_n=X$$ \(QED\)
* proof &lt;=
* 反之令$$\displaystyle \lim_{ n \rightarrow \infty} Y_n=Y$$，依極限定義得$$\forall \epsilon > 0, ~ \exists n_0 \in \mathbb{N}   \ni  |Y_n−Y|<\epsilon, ~ \forall n \geq n_0$$
* 由於數列$$\{X_n\}$$包含了許多$$\{Y_n\}$$的重複項，因此 $$\exists m_0 \in \mathbb{N} \ni X_{m_0}=Y_{n_0}$$  且$$\forall n \geq m_0 ~ |X_n−Y|<\epsilon$$
* 因此$$\displaystyle \lim_{ n \rightarrow \infty} X_n=Y$$ \(QED\)



### 



