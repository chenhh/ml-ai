# 組合\(combination\)

## 組合公式

> $$ n$$件相異物，不允許重覆取$$r$$件組合的方法數有$$C(n,r) \equiv \begin{pmatrix} n \\ r \end{pmatrix} =\frac{n!}{r!(n-r)!}, \ 0\leq r \leq n$$

* $$n$$件相異物，不允許重覆取$$r$$件排列的方法數有$$\frac{n!}{(n−r)!}$$。
* 而組合相對於排列則**不考慮次序**，因此有$$\frac{n!}{(n−r)!r!}$$ 種 \(QED\)

例：1,2,3三個數字中取2個相異數字，取到1,2或2,1兩類視為相同的組合，因此有C\(3,2\)=3種組合。

例：$$1,2,\ldots ,300$$中取3個數使其和為3的倍數之選法?

* 將$$1,2,\ldots,300$$分為除以3餘數為$$0,1,2$$三個集合。
* $$A_1=\{3k \vert 1 \leq k \leq100\}$$為除以3餘數為0的集合。
* $$A_2= \{3k+1 \vert 1 \leq k \leq 99\}$$為除以3餘數為1的集合。
* $$A_3=\{3k+2 \vert 1 \leq k \leq 99 \}$$為除以3餘數為2的集合。
* 可得 $$|A_1 |=|A_2 |=|A_3 |=100$$。
* 取3個數和為3的倍數有以下情形
* 3個數均從$$A_1$$ 選出，有$$C(100, 3)$$種組合。
* 3個數均從$$A_2$$ 選出，有$$C(100,3)$$種組合。
* 3個數均從$$A_3$$ 選出，有$$C(100,3)$$種組合。
* 3個數分別由$$A_1,A_2,A_3$$ 選出，有$$C(100,1)^3$$ 組合。
* 因此總共有$$3 \times C(100,3) + C(100,1)^3 $$ 種組合。

## 組合公式的遞迴關係式

> $$\begin{pmatrix} n \\ r \end{pmatrix} = \begin{pmatrix} n-1 \\ r-1 \end{pmatrix} + \begin{pmatrix} n-1 \\ r \end{pmatrix},  0 \leq r \leq n$$

### 

#### 排列組合的意義

* $$\begin{pmatrix} n \\ r \end{pmatrix}$$表示從$$n$$件相異物不允許重複取$$r$$件的組合方法數。
* 考慮其中某一物件$$x$$，組合方法中，可分為取中該物件與沒有取中該物件兩種情形。

  * 取中該物件時，相當於從剩餘的$$(n-1)$$件相異物取$$(r-1)$$件，有$$\begin{pmatrix} n -1 \\ r-1 \end{pmatrix}$$種組合。
  * 沒有取中該物件時，表示取中其它物件，相當於從剩餘的$$(n-1)$$件相異物取$$r$$件，有$$\begin{pmatrix} n -1 \\ r \end{pmatrix}$$種組合。

#### 代數證明

$$\begin{pmatrix} n -1 \\ r-1 \end{pmatrix} + \begin{pmatrix} n -1 \\ r \end{pmatrix} = \frac{(n-1)!}{(r-1)!(n-r)!}+\frac{(n-1)!}{r!(n-r-1)!} = \frac{r(n-1)!}{r!(n-r)!} + \frac{((n-r)(n-1)!}{r!(n-r)!} = \frac{n!}{r!(n-r)!} = \begin{pmatrix} n \\ r \end{pmatrix}$$

## 二項式定理\(binomial theorem\)

> $$x,y$$為變數，$$n \in \mathbb{N}$$，則 $$(x+y)^n = \sum_{k=0}^n \begin{pmatrix} n \\ k \end{pmatrix} x^k y^{n-k}$$
>
> * $$x=1, y=1$$代入後可得 $$2^n= \begin{pmatrix} n \\ 0 \end{pmatrix}  \begin{pmatrix} n \\ 1 \end{pmatrix} + \ldots + \begin{pmatrix} n \\  n \end{pmatrix}$$
> * $$x=1, y=-1$$代入後可得 $$0 = \begin{pmatrix} n \\ 0 \end{pmatrix} - \begin{pmatrix} n \\ 1 \end{pmatrix} + \begin{pmatrix} n \\ 2 \end{pmatrix} + \ldots + (-1)^n \begin{pmatrix} n \\  n \end{pmatrix}$$

* $$(x+y)^n = (x+y)(x+y) \ldots (x+y)$$
* 而$$x^k y^{n-k}$$的係數為上式$$n$$個乘項中選$$k$$個$$x$$，$$n-k$$個$$y$$，因此為 $$\frac{n!}{k!(n-k)!} = \begin{pmatrix} n \\ k \end{pmatrix} , k=0,1,2\ldots, n$$\(QED\)。

## 多項方程式

> $$(x_1 +x_2+ \ldots +x_k)^n = \sum_{0 \leq n_i \leq n, n_1+n_2+\ldots + n_k=n} \begin{pmatrix} n \\ n_1, n_2,\ldots, n_k \end{pmatrix}x_1^{n_1} x_2^{n_2}\ldots x_k^{n_k}$$

* $$x_1^{n_1} x_2^{n_2}\ldots x_k^{n_k}$$的係數，等同於$$n$$個不全相異物，共有$$k$$類的排列方法。
* 因為$$n$$項乘積中先選$$n_1$$ 個$$x_1$$，再由剩下的$$n−n_1$$ 個乘積中選$$n_2$$ 個$$x_2$$，以此類推到$$n−n_1−\ldots−n_{k−1}$$個乘積中選$$n_k$$ 個$$x_k$$。
* 有 $$\begin{pmatrix} n \\ n_1 \end{pmatrix} \begin{pmatrix} n  - n_1\\ n_2 \end{pmatrix} \begin{pmatrix} n -n_1 - n_2 \\ n_3 \end{pmatrix} \ldots \begin{pmatrix} n - n_1 \ldots - n_{k-1} \\ n_k \end{pmatrix} = \frac{n!}{n_1! n_2! \ldots n_k!}$$

