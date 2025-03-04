# 函數序列上/下極限

## 簡介

[集合序列的極限](../set/limit-of-set-sequence.md)。

[實數上(下)確界](../real-number/supremum-infimum.md)。

[數列的上、下極限](../sequence/limit-sup-inf-of-sequence.md)。

討論序列極限時，極限不存在可能是發散至$$\pm \infty$$，或是上/下極限不相等。

而序列上/下極限必為實數或是$$\pm \infty$$，因此必定存在。

### 實數序列上極限

$$\displaystyle \limsup_{n \rightarrow \infty} x_n = \inf_{n \geq 0}\{\sup_{k \geq n} x_k\}=b$$ 可寫為$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni x_n < b + \epsilon, ~ \forall n \geq n_0$$。

令$$M_n=\sup\{x_n, x_{n+1}, \dots \}$$，可得$$M_n \geq M_{n+1}$$為遞減數列。

可得$$\displaystyle \limsup_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} M_n \in [-\infty, \infty]$$。如果$$\{x_n\}$$有上界時，則上極限存在，否則上極限為$$\infty$$。

### 實數序列下極限

$$\displaystyle \liminf_{n \rightarrow \infty} x_n = \sup_{n \geq 0}\{\inf_{k \geq n} x_k\}=a$$可寫為$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni a-\epsilon < x_n, ~\forall n \geq n_0$$。

令$$m_n=\inf\{x_n, x_{n+1}, \dots \}$$，可得$$m_n \leq m_{n+1}$$為遞增數列。

可得$$\displaystyle \liminf_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} m_n \in [-\infty, \infty]$$。如果$$\{x_n\}$$有下界時，則下極限存在，否則下極限為$$-\infty$$。

當$$n \rightarrow \infty$$時，序列$$\{x_n\}$$ 的波動被「限制」在$$\displaystyle \limsup_{n \rightarrow \infty} x_n$$ ​和$$\displaystyle \liminf_{n \rightarrow \infty} x_n$$ 之間。

實數序列$$\{y_n\}$$的上/下極限，等價於函數序列$$\{f_n\}$$中給定單點的上/下極限。即給定固定的$$x \in E$$後，$$\{y_n \equiv f_n(x)\}$$上/下極限。而函數序列討論的是給定全部的$$x \in E$$，整個函數$$f(x), ~ x \in E$$隨著$$n$$變動時的上/下極限。

### 函數序列上/下極限

函式序列的上下極限不僅是逐點的極限，還可能具有全域性性質。

$$\displaystyle \limsup_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} \sup_{k \geq n}f_k(x)  = \inf_{n \geq 0}\{\sup_{k \geq n} f_k(x)\}$$

它表示在每個位置$$x$$，隨著$$n$$增大，序列$$\{f_n ​ (x)\}$$ 的「上包絡線」的極限。

$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} \inf_{k \geq n}f_k(x) = \sup_{n \geq 0}\{\inf_{k \geq n} f_k(x)\}$$

它表示在每個位置$$x$$x，隨著$$n$$增大，序列$$\{f_n ​ (x)\}$$ 的「下包絡線」的極限。

在實數序列中，上下極限可視為「最終」的上下界：

* **上極限** ：當$$n$$足夠大時，序列$$\{x_n\}$$ 的值不會超過$$\limsup x_n​+\epsilon$$。
* **下極限** ：當$$n$$足夠大時，序列$$\{x_n \}$$ 的值不會低於$$\liminf x_n​- \epsilon$$。
* **意義** ：當$$n \rightarrow \infty$$時，序列$$\{x_n\}$$ 的波動被「限制」在$$\displaystyle \limsup_{n \rightarrow \infty} x_n$$ ​和$$\displaystyle \liminf_{n \rightarrow \infty} x_n$$ 之間。

類似地，函式序列的上下極限可解釋為：

* **上極限函數**：對每個$$x$$，當$$n$$足夠大時，$$f_n​ (x)$$的值最終被限制在$$\displaystyle \limsup_{n \rightarrow \infty}​ f_n(x)+\epsilon$$ 以下。
* **下極限函數**：對每個$$x$$，當$$n$$足夠大時，$$f_n​ (x)$$的值最終被限制在$$\displaystyle \liminf_{n \rightarrow \infty}​ f_n(x)-\epsilon$$ 以上。
* **意義** ：當$$n \rightarrow \infty$$，函數值的振幅被限制在和$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)$$之間。

## 範例

* $$f_n(x)=x^n, ~ x \in [0,1]$$. ，則$$\displaystyle \liminf_{n \rightarrow \infty}f_n(x)=\begin{cases} 0, & x \in [0,1) \\ 1, & x = 1 \end{cases}$$。
* $$f_n(x)=\frac{x}{n}$$，則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)=0$$。
* $$f_n(x)=(-1)^nx^n$$, $$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)= \begin{cases} \infty,& x < -1, &\text{ whole seq. }\\ -\infty, & x > 1, &\text{ take } n=2k+1, \\ 0, & x \in (-1, 1), &\text{ whole seq. } \\ -1, & x= 1,  &\text{ take } n=2k+1, \\ 1, & x =-1, &\text{ whole seq. } \end{cases}$$

## 函數序列上下極限的性質

### 序列下極限小於上極限

> $$\forall x \in S$$，上下極限函式滿足：$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x) \leq  \limsup_{n \rightarrow \infty} f_n(x)$$。
>
> 或者寫成$$\displaystyle \forall \epsilon >0, \exists n_0 \in \mathbb{N} \ni   \liminf_{n \rightarrow \infty} f_n(x)   -\epsilon \leq f(x) \leq \limsup_{n \rightarrow \infty} f_n(x) + \epsilon$$
>
> 這表明上下極限函數為序列在無窮遠處的漸近上下界。
>
> 這是因為下極限是序列可能的最小極限值，而上極限是序列可能的最大極限值。

### 序列收斂時下極限等於上極限

> 若$$\{f_n\}$$一致收斂至函數$$f(x)$$時，則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x) =  \limsup_{n \rightarrow \infty} f_n(x) = f(x)$$。
>
> 但反之不一定成立：若僅在每個 $$x$$處點態收斂，序列不一定一致收斂。
>
> 且存在$$n_0 \in \mathbb{N} \ni \forall x \in S, |f_n(x) -f(x)| < \epsilon, ~\forall n \geq n_0$$。
>
> 此時，上下極限函數不僅逐點相等，且整體控制所有後續項的函數值。

### 函數序列有界時，上下極限均存在且有限

> 如果函式序列$$\{f_n\}$$在某點$$x$$處有界（即存在$$M$$使得 $$|f_n(x)| \leq M$$ 對所有$$n$$成立），則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)$$ 與$$\displaystyle \limsup_{n \rightarrow \infty}f_n(x)$$均存在且有限。
>
> 若序列在$$x$$處無界，則可能出現：
>
> * $$\displaystyle \limsup_{n \rightarrow \infty}f_n(x) = + \infty$$(若序列無上界）。
> * $$\displaystyle \liminf_{n \rightarrow \infty}f_n(x) = - \infty$$(若序列無下界）。

### 算術運算不等式

> 給定函式序列$$\{f_n\}, \{g_n\}$$，可得：
>
> * $$\displaystyle \limsup_{n \rightarrow \infty} (f_n(x)  + g_n(x)) \leq  \limsup_{n \rightarrow \infty} f_n(x) +  \limsup_{n \rightarrow \infty} g_n(x)$$
> * $$\displaystyle \liminf_{n \rightarrow \infty} (f_n(x)  + g_n(x)) \geq  \liminf_{n \rightarrow \infty} f_n(x) +  \liminf_{n \rightarrow \infty} g_n(x)$$
>
> 對於乘法或除法，也有類似性質，但通常需要額外條件（如正性或有界性）以確保結果成立。

### 連續函式序列上/下極限不一定是連續函數

> 給定連續函數序列$$\{f_n\}$$，則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)$$ 與$$\displaystyle \limsup_{n \rightarrow \infty}f_n(x)$$不一定是連續函數。

範例：$$ $f_n(x)=x^n, x \in [0,1] $$$$f_n(x)=x^n, ~ x \in [0,1]$$為連續函數序列，但$$n \rightarrow \infty$$時，$$0\leq x <1, x^n =0$$，但$$x=1$$時，$$x^n=1$$，所以連續函數序列收斂(上/下極限相等)，但不是連續函數。

範例：$$f_n(x)=(-1)^n x, ~x \in [0,1]$$為連續函數序列。

* 在$$x=0$$時函數序列收斂，$$\displaystyle  f_n(0) =  \liminf_{n \rightarrow \infty} f_n(x) = \limsup_{n \rightarrow \infty} f_n(x)  = 0$$。
* 在$$x \in (0,1]$$，$$f_n(x)=(-1)^n x$$會在$$n$$為奇、偶數之間交替：
  * $$n$$為偶數時$$f_n=x$$；$$n$$為奇數時$$f_n=-x$$。
  * 上極限$$\displaystyle \limsup_{n \rightarrow \infty} f_n(x) = x$$。
  * 下極限$$\displaystyle   \liminf_{n \rightarrow \infty} f_n(x)  = -x$$。

### 可測函式序列上/下極限仍為可測函數

> 給定可測函數序列$$\{f_n\}$$，則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)$$ 與$$\displaystyle \limsup_{n \rightarrow \infty}f_n(x)$$為可測函數。

## 參考資料

* [https://www.zhihu.com/question/56591866](https://www.zhihu.com/question/56591866)
* [https://math.stackexchange.com/questions/1130477/liminf-of-a-sequence-of-functions](https://math.stackexchange.com/questions/1130477/liminf-of-a-sequence-of-functions)
* [https://math.stackexchange.com/questions/2546082/explanation-of-lim-inf-of-sequence-of-functions-f-n-for-fatous-lemma](https://math.stackexchange.com/questions/2546082/explanation-of-lim-inf-of-sequence-of-functions-f-n-for-fatous-lemma)
