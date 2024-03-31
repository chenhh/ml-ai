# Lebesgue積分

## 簡介

建構Lebesgue積分的方法各本書方法不完全一致。雖然都是切割一般可測函數$$f$$的值域$$[-\infty, \infty]$$後，確認前像在σ域內，相乘後再加總得積分。但建構過程各異。

由於測度$$m: \Sigma \rightarrow [0,\infty]$$和可測函數$$f: E\rightarrow [-\infty, \infty]$$之值均可能為$$\infty$$，因此討論可積分函數$$\int_E f<\infty$$要特別討論測度為0且函數值為$$\infty$$與測度為$$\infty$$且函數值為0兩種條件(因為$$0\cdot \infty=0$$)。

Tom M. Apostol在數學分析中使用了切割定義域的上積分差值定義Lebesgue積分，因為在數學分析中沒有定義測度，所以此定義方法在實變分析不常見。

## 常見建構Lebesgue積分

### 使用非負簡單函數，周民強/陶哲軒/Walter Rudin

1. 定義非負可測簡單函數的積分。
2. 可測簡單函數積分上界定義非負可測函數的積分。
3. 通過$$f(x)=f^{+}(x)-f^{-}(x)$$定義一般可測函數的積分。

### 使用一般簡單函數，Halsey Royden/Gerald B. Folland/Elias M. Stein

1. 定義一般簡單函數在有限測度集相對於有界函數的積分。
2. 用一般簡單函數在有限測度集的上/下積分夾擠得有界函數的積分。
3. 用有界非負函數在有限支撐集的積分上界定義一般非負可測函數在一般測度的積分。
4. 一般可測函數的積分。

### 使用Cauchy in mean建構積分, Avner Friedman

1. 定義一般簡單函數的積分。
2. 定義Cauchy sequence in mean的函數序列$$(\displaystyle \lim_{n,m \rightarrow \infty}\int_E |f_n-f_m|=0$$)，且函數序列幾乎處處(或測度)收斂$$(\displaystyle \lim_{n \rightarrow \infty} f_n(x)=f(x)$$)。則積分定義為$$\displaystyle \int_E f(x)dx = \lim_{n \rightarrow \infty}\int_E f_n(x)dx$$。

### 使用函數的undergraph定義積分Charles Pugh

1. 定義非負實值可測函數$$f: \mathbb{R} \rightarrow [0, \infty)$$在值域以下相對於實數面積$$uf=\{(x,y) \in \mathbb{R} \times [0, \infty) ~|~ 0 \leq y <f(x)\}$$的測度$$m(uf)$$為積分。
2. 定義非負可測函數$$f: \mathbb{R} \rightarrow [0, \infty)$$在值域(含)相對於實數面積$$\hat{u}f=\{(x,y) \in \mathbb{R} \times [0, \infty) ~|~ 0 \leq y \leq f(x)\}$$與可積分時的性質。



* 若$$m(E)<\infty$$，則定義在$$E$$上的所有有界可測函數$$f$$相對於$$E$$均可積(即$$\int_E f < \infty$$)。
* 在集合$$E$$的可測函數$$f$$不可積分，即$$\displaystyle \int_E f = \pm \infty$$。
* $$f$$在$$E$$可積$$\Leftrightarrow$$$$|f|$$在$$E$$可積分，且$$|\int_E f| \leq \int_E |f|$$。因此絕對可積分等價於可積分。
* $$m(E) <\infty$$且$$f$$在$$E$$為上有界函數，若將$$E$$可分割為$$E=\bigcup_{i=1}^m E_i$$，則$$\int_E f = \sum_{i=1}^m \int_{E_i} f$$。
* $$f,g$$在$$E$$均可積分，且$$f \leq g \text{ a.e. on } E$$，則$$\int_E f \leq \int_E g$$。
* 積分有線性性質 $$\int_E (af+g) = a\int_E f  + \int_E g$$。
* $$f \in L(E)$$，則存在簡單函數$$g$$可逼近$$f$$，即$$\forall \epsilon > 0, ~\int_E |f - g|  < \epsilon$$。
* $$E$$上的Riemann可積函數$$f$$必為Lebesgue可積函數，且積分值相等。
* \[Domain control theorem, DCT]
* \[Monotone converge theorem, MCT]
*   \[Fatou lemma]



##

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
> <mark style="color:red;">函數</mark>$$f$$<mark style="color:red;">稱為Riemann integrable(可積分)</mark> $$(R){\int_a^b }f$$ $$\Leftrightarrow$$$$(R)\underline{\int_a^b }f = (R)\overline{\int_a^b }f$$，

## 階梯函式是Riemann可積分

> 函數$$\psi: [a,b] \rightarrow \mathbb{R}$$稱為階梯函數若給定分割$$P=\{x_0, x_1, \dots, x_n\}$$，函數$$\psi$$在每一個開區間$$(x_{i-1}, x_i)$$都只有一個實數值$$c_i < \infty$$即：
>
> $$L(\psi, P) = \sum_{i=1}^n c_i (x_i - x_{i-1}) = U(\psi, P)\psi(x) = c_i, ~ x \in (x_{i-1}, x_i)$$

因為$$L(\psi, P) = \sum_{i=1}^n c_i (x_i - x_{i-1}) = U(\psi, P)$$

所以階梯函數是Reimann integrable $$\displaystyle (R) \int_a^b \psi = \sum_{i=1}^n c_i (x_i - x_{i-1})$$
