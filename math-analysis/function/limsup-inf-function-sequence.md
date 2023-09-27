# 函數序列上/下極限

簡介

[集合序列的極限](../set/limit-of-set-sequence.md)。

[實數上(下)確界](../real-number/supremum-Infimum.md)。

[數列的上、下極限](../sequence/limit-sup-inf-of-sequence.md)。

#### 實數序列上極限

$$\displaystyle \limsup_{n \rightarrow \infty} x_n = \inf_{n \geq 0}\{\sup_{k \geq n} x_k\}=b$$ 可寫為$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni x_n < b + \epsilon, ~ \forall n \geq n_0$$。

令$$M_n=\sup\{x_n, x_{n+1}, \dots \}$$，可得$$M_n \geq M_{n+1}$$為遞減數列。

可得$$\displaystyle \limsup_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} M_n \in [-\infty, \infty]$$。如果$$\{x_n\}$$有上界時，則上極限存在，否則上極限為$$\infty$$。

#### 實數序列下極限

$$\displaystyle \liminf_{n \rightarrow \infty} x_n = \sup_{n \geq 0}\{\inf_{k \geq n} x_k\}=a$$可寫為$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni a-\epsilon < x_n, ~\forall n \geq n_0$$。

令$$m_n=\inf\{x_n, x_{n+1}, \dots \}$$，可得$$m_n \leq m_{n+1}$$為遞增數列。

可得$$\displaystyle \liminf_{n \rightarrow \infty} x_n = \lim_{n \rightarrow \infty} m_n \in [-\infty, \infty]$$。如果$$\{x_n\}$$有下界時，則下極限存在，否則下極限為$$-\infty$$。

實數序列$$\{y_n\}$$的上/下極限，等價於函數序列$$\{f_n\}$$中單點的上/下極限。即給定固定的$$x \in E$$後，$$\{y_n \equiv f_n(x)\}$$上/下極限。而函數序列討論的是給定全部的$$x \in E$$，整個函數$$f(x), ~ x \in E$$隨著$$n$$變動時的上/下極限。

#### 函數序列上/下極限

$$\displaystyle \limsup_{n \rightarrow \infty} f_n(x) = \inf_{n \geq 0}\{\sup_{k \geq n} f_k(x)\}$$

$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} \inf_{k \geq n}f_k(x) = \sup_{n \geq 0}\{\inf_{k \geq n} f_k(x)\}$$

## 範例

* $$f_n(x)=x^n, ~ x \in [0,1]$$. ，則$$\displaystyle \liminf_{n \rightarrow \infty}f_n(x)=\chi_{\{1\}}(x)$$。
* $$f_n(x)=\frac{x}{n}$$，則$$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)=0$$。
* $$f_n(x)=(-1)^nx^n$$, $$\displaystyle \liminf_{n \rightarrow \infty} f_n(x)= \begin{cases} \infty,& x < -1, &\text{ whole seq. }\\ -\infty, & x > 1, &\text{ take } n=2k+1, \\ 0, & x \in (-1, 1), &\text{ whole seq. } \\ -1, & x= 1,  &\text{ take } n=2k+1, \\ 1, & x =-1, &\text{ whole seq. } \end{cases}$$

## 參考資料

* [https://www.zhihu.com/question/56591866](https://www.zhihu.com/question/56591866)
* [https://math.stackexchange.com/questions/1130477/liminf-of-a-sequence-of-functions](https://math.stackexchange.com/questions/1130477/liminf-of-a-sequence-of-functions)
