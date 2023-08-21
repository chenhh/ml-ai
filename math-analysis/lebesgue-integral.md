# Lebesgue積分

## 簡介

建構Lebesgue積分分為三個階段：

1. 定義非負可測簡單函數的積分。
2. 考慮可測簡單函數和非負可測函數的關系。
3. 通過$$f(x)=f^{+}(x)-f^{-}(x)$$定八一般可測函數的積分。

## 零測度集合(measure zero set)

> 定義集合$$S \subseteq \mathbb{R}$$ 的測度為0( measure zero)若
>
> * 對任意$$\epsilon >0$$，存在集合$$S$$可數的開區間覆蓋，且這些可數開區間覆蓋的總長度小於$$\epsilon$$。(註：Haine-Borel定理：實數上的有界閉區間(緊緻集)必可被有限開區間覆蓋)。
> *>   令$$F_k=(a_k, b_k ), ~ k \in \mathbb{N}$$  為集合$$S$$的可數開區間覆蓋，則$$\forall \epsilon >0 , ~ S \subseteq \cup_{k \in \mathbb{N}} (a_k, b_k)$$ 且 $$\displaystyle \sum_{k \in \mathbb{N}} (b_k - a_k) < \epsilon$$。
> * 即$$S$$為零測度的集合若$$S$$為測度(長度)任意小的開區間聯集之子集合（即不論多小的開區集之聯集，S均為此聯集的子集合）>

* 註：因為在基礎分析沒有定義測度與其性質，因此使用此Lebesgue測度任意小時，使用夾擠收斂來描述集合測度為0時應該有的性質。

## Riemann積分

### Darbounx upper and lower sum

> 函數$$f: [a,b] \rightarrow \mathbb{R}$$，給定區間$$[a,b]$$的分割$$P=\{x_0, x_1, \dots,x_n\}$$滿足$$a=x_0 < x_1<\dots<x_n=b$$。
>
> 定義Darboux對於函數$$f$$與分割$$P$$的上和(upper sum)與下和(lower sum)如下：
>
> * $$\displaystyle L(f,P)=\sum_{i=1}^n m_i \cdot (x_i - x_{i-1})$$
> * $$\displaystyle U(f,P)=\sum_{i=1}^n M_i \cdot (x_i - x_{i-1})$$
> * $$\displaystyle m_i = \inf\{f(x) ~|~ x_{i-1} < x < x_i \}$$，$$\displaystyle M_i = \sup\{f(x) ~|~ x_{i-1} < x < x_i \}$$分別為函數$$f$$在區間開區間$$(x_{i-1}, x_i)$$的下、上界，如果使用閉區間$$[x_{i-1}, x_i]$$也可得到相同的$$m_i, M_i$$值。

### Riemann integrable

> 下積分 $$(R)\underline{\int_a^b }f = \sup \{ L(f,P)~|~ P \text{ is partition of } [a,b]\}$$
>
> 上積分 $$(R)\overline{\int_a^b }f = \inf \{ U(f,P)~|~ P \text{ is partition of } [a,b]\}$$
>
> 因為$$f$$之值為有限值，且$$[a,b]$$長度有限，因此上、下積分均為有限值。
>
> 函數$$f$$稱為Riemann integrable $$(R){\int_a^b }f$$ $$\Leftrightarrow$$$$(R)\underline{\int_a^b }f = (R)\overline{\int_a^b }f$$，

## 階梯函式是Riemann integrable

> 函數$$\psi: [a,b] \rightarrow \mathbb{R}$$稱為階梯函數若給定分割$$P=\{x_0, x_1, \dots, x_n\}$$，函數$$\psi$$在每一個開區間$$(x_{i-1}, x_i)$$都只有一個實數值$$c_i < \infty$$即：
>
> $$L(\psi, P) = \sum_{i=1}^n c_i (x_i - x_{i-1}) = U(\psi, P)\psi(x) = c_i, ~ x \in (x_{i-1}, x_i)$$

因為$$L(\psi, P) = \sum_{i=1}^n c_i (x_i - x_{i-1}) = U(\psi, P)$$

所以階梯函數是Reimann integrable $$\displaystyle (R) \int_a^b \psi = \sum_{i=1}^n c_i (x_i - x_{i-1})$$
