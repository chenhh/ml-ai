# 遞迴關係式

## 簡介

遞迴關係（recurrence relation），也稱為差分方程式（difference equation），是一種遞推地定義一個序列的方程式式：序列的每一項目是定義為前若干項的函數。

某些簡單定義的遞迴關係式可能會表現出非常複雜的（混沌的）性質，他們屬於數學中的非線性分析領域。所謂解一個遞迴關係式，也就是求其解析解，即關於$$n$$的非遞迴函數。

## 遞迴關係式

> definition: recurrence relation
>
> 給定數列$$a_0, a_1,\dots, a_n, \dots$$，遞迴關係式為一個相對於$$a_n$$的方程式，此方程式除了$$a_n$$外，只包含該mgp 列中$$a_n$$部份的項目。

例如 $$\left \{ \begin{aligned} a_n &= 3a_n-1, ~n \geq 0,\\a_0& =  5\end{aligned}\right.$$​

* $$a_0=5$$稱為<mark style="color:red;">邊界條件(boundary condition)或是初始條件(initial condition)</mark>。

直接展開序列可得 $$a_0=5$$​， $$a_1=3a_0=3(5)$$，$$a_2=3^2(5)$$，以此類推可得$$a_n=3^n(5)$$為<mark style="color:red;">通解(general solution)</mark>。

一般遞迴關係式的解法有三類：

1. <mark style="color:red;">代入法(substiution method)：常用於簡單的問題。</mark>
2. <mark style="color:red;">數學歸納法(induction method)：用於大概可猜出答案時，直接驗證。</mark>
3. <mark style="color:red;">特徵多項式法(characteristic polynomial method)：求複雜的遞迴關係式</mark>。

## 常係數線性遞迴關係式

> definition: 常係數線性遞回關係式
>
> 假設$$k \in \mathbb{N},$$ $$c_n, c_{n-1}, \dots, c_{n-k} \in \mathbb{R}$$ 且$$c_n, c_{n-k} \neq 0$$
>
> 令$$a_n, n=0,1,2,\dots$$為一數列，則
>
> $$\sum_{i=0}^kc_{n-i}a_{n-i}=c_na_n+c_{n-1}a_{n-1}+\dots +c_{n-k}a_{n-k}=f(n)$$稱為一$$k$$​階<mark style="color:red;">常係數遞迴關係式</mark>(linear recurrence relation with constant coefficients of order k)。
>
> 若$$f(n)=0, ~ \forall n \geq 0$$則稱為<mark style="color:red;">齊次(homogeneous)遞迴關係式</mark>。
>
> 否則稱為<mark style="color:red;">非齊次(non-homogeneous)遞迴關係式</mark>。

### 範例：等比數列

> 公比為$$r$$的等比數列$$\{a_n=a_0 r^n\}$$滿足遞迴關係 $$a_n=r a_{n}, ~ n \geq 1$$ 。
>
> 是一個常係數齊次一階線性遞迴關係式。

### 範例：等差數列

> 公差為$$d$$的等差數列$$\{a_n=a_0 + nd\}$$滿足遞迴關係$$a_n=a_{n-1}+d, ~ n \geq 1$$​。
>
> 是一個常係數非齊次一階線性遞迴關係式。

### 範例：部分和數列

> 數列$$\{a_n\}$$的部份和數列 $$\{s_n = \sum_{k=0}^n a_k \}$$滿足遞迴關係$$s_n = s_{n-1}+a_n, ~ n\geq 1$$
>
> 是一個常係數非齊次一階線性遞迴關係式。

### 範例：Fibonacci數列

> * $$f_{n+2}= f_{n+1}+f_n, ~ n\geq 0$$
> * $$f_0=f_1=1$$
>
> 是一個常係數非齊次二階線性遞迴關係式。

### 範例：Catalan數列

> $$c_n = \frac{1}{n+1}\binom{2n}{n}$$滿足遞迴關係式$$c_n-c_0c_{n-1}-c_1c_{n-2}-\dots - c_{n-1}c_0=0, ~n \geq 1$$

### 一階線性遞迴關係(first-order linear recurrence relation)

> $$c_na_n+c_{n-1}a_{n-1}=f(n)$$&#x20;

最簡單的遞迴關係，它的一般項可以逐項代入求得一般通式。

### 齊次一階線性遞迴關係

> 齊次遞迴關係：$$c_na_n=c_{n-1}a_{n-1}$$
>
> * $$a_n= \frac{c_{n-1}}{c_n} a_{n-1}=g_n a_{n-1}, ~n\geq 1$$
> * 可得 $$a_n =\left( \prod_{k=0}^{n-1}g_k \right) a_0$$

* 一般情形$$g_k=\frac{c_{k-1}}{c_k}$$, 則$$a_n=\frac{c_0}{c_n}a_0$$
* 常數係數 $$g_k=c$$, 則$$\frac{a_n}{a_{n-1}}=c$$, 因此$$a_n=c^na_0$$。

### 非齊次一階線性遞迴關係

> $$c_na_n = c_{n-1}a_{n-1} + f(n-1), ~ n \geq 0$$\
> 可得$$\displaystyle a_n =\left( \prod_{k=0}^{n-1}g_k \right) a_0 + \sum_{k=0}^{n-1}(\prod_{m=k+1}^{n-1}g_m)f(k)$$(通解+特解)\
> 其中$$\displaystyle \prod_{m=n}^{n-1}g_m=1$$

$$\begin{aligned}   a_n & = g_{n-1}a_{n-1} + f(n-1), ~ n \geq 0  \\         & = (g_{n-1}g_{n-2})a_{n-2}  + g_{n-1}f(n-2) + f(n-1) \\         & = (g_{n-1}g_{n-2}g_{n-3})a_{n-3} + (g_{n-1}g_{n-2})f(n-3) + g_{n-1}f(n-2) + f(n-1) \\         & = \cdots \\         & = (\prod_{k=0}^{n-1}  g_k) a_0 + \sum_{k=0}^{n-1} (\prod_{m=k+1}^{n-1}g_m)f(k)  \end{aligned}$$(QED)

#### 範例

$$a_n=2 a_{n-1} + 3, ~ n \geq 2,  ~a_1 =3$$

* $$\begin{aligned}  a_n & = 2 a_{n-1} + 3 \\     & = 2^2 a_{n-2} + (2+1) 3 \\     & = 2^3 a_{n-3} + (2^2 + 2 + 1)3 \\     & = \dots \\     & = 2^{n-1}a_1 + (2^{n-2}+2^{n-3}+\dots +1)3 \\     & =2^{n-1}3+(2^{n-1}-1)3 \\     & = 3(2^n-1), ~n \geq `1. \end{aligned}$$

### 齊次解

> 當$$\sum_{i=0}^kc_{n-i}a_{n-i}=0$$ 解的型式為$$a_n=A\alpha^n, ~ A, \alpha \in \mathbb{R}$$

* $$k=1$$時，$$c_na_n+c_{n-1}a_{n-1}=0$$
* $$\therefore a_n= - \frac{c_{n-1}}{c_n} a_{n-1}$$
* $$k=2$$時，$$c_na_n+c_{n-1}a_{n-1}+c_{n-2}a_{n-2}=0$$
* $$\therefore a_n = -\frac{c_{n-1}}{c_n}a_{n-1} - \frac{c6_{n-2}}{c_n}a_{n-2}$$
