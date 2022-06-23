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

> $$c_na_n=c_{n-1}a_{n-1}+f(n)$$&#x20;

最簡單的遞迴關係，它的一般項可以逐項代入求得一般通式。

### 齊次一階線性遞迴關係

> 齊次遞迴關係：$$c_na_n=c_{n-1}a_{n-1}$$
>
> * $$a_n= \frac{c_{n-1}}{c_n} a_{n-1}=g_{n-1} a_{n-1}, ~n\geq 1$$
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

## 二階線性遞迴關係(second-order linear recurrence relation)

> 當$$c_na_n+=c_{n-1}a_{n-1}+c_{n-2}a_{n-2}+f(n)$$&#x20;

### 齊次二階線性遞迴關係

> $$c_na_n=c_{n-1}a_{n-1}+c_{n-2}a_{n-2}=0$$ 可令$$c_n=1$$

* 直接展開時，因此每次都會分成二支，展開到$$n=1$$時有$$2^n$$個系數，難以歸納。

改寫線性方程式矩陣形式如下：

$$\begin{aligned} a_n &= c_{n-1}a_{n-1} + c_{n-2} a_{n-2} \\ a_{n-1} &= a_{n-1} \end{aligned}$$

所以

$$\begin{bmatrix} a_n \\ a_{n-1} \end{bmatrix}=\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}  \begin{bmatrix} a_{n-1} \\ a_{n-2} \end{bmatrix}, ~ n \geq 2$$

令$$u_{n-1}=\begin{bmatrix} a_n \\ a_{n-1} \end{bmatrix}$$, $$A=\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$$，則可改寫為矩陣$$\begin{aligned}  \begin{bmatrix} a_{n+1} \\ a_n \end{bmatrix} & = u_{n} \\     & = A^nu_{0}, ~ n \geq 0 \\     & = PD^nP^{-1}u_0 \\     & = \begin{bmatrix} \lambda_1 & \lambda_2 \\ 1 & 1 \end{bmatrix}         \begin{bmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{bmatrix}         \begin{bmatrix} h_1 \\ h_2 \end{bmatrix}         =\begin{bmatrix} h_1\lambda_1^{n+1} + h_2 \lambda_2^{n+1} \\                          h_1 \lambda_1^n + h_2 \lambda_2^n \end{bmatrix}  \endn{aligned}$$

初始條件為$$u_0=\begin{bmatrix} a_1 \\ a_{0} \end{bmatrix} =\begin{bmatrix} 1 \\ 0\end{bmatrix}$$

可得$$u_n=A^nu_0$$因此解差分方程式等於計算冪矩陣$$A^n$$。

而$$A^n$$可先將$$A$$正交對角化為$$A=PDP^{-1}$$後，得$$A^n=PD^nP^{-1}$$, 其中$$D=\mathrm{diag}(\lambda_1, \lambda_2)$$為矩陣$$A$$的特徵根。

令$$\begin{bmatrix} h_1 \\ h_2 \end{bmatrix} = P^-1u_0$$, 整理後得$$\begin{aligned} \begin{bmatrix} a_{n+1} \\ a_n \end{bmatrix} & = u_{n} \\     & = A^n u_{0}, ~ n \geq 0 \\     & = P D^n P^{-1}u_0 \\     & = \begin{bmatrix} \lambda_1 & \lambda_2 \\ 1 & 1 \end{bmatrix}         \begin{bmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{bmatrix}         \begin{bmatrix} h_1 \\ h_2 \end{bmatrix} \\     & = \begin{bmatrix} h_1 \lambda_1^{n+1} + h_2 \lambda_2^{n+1} \\                          h_1 \lambda_1^n + h_2 \lambda_2^n \end{bmatrix} \end{aligned}$$

整理以上步驗，可得$$k$$階常係數齊次遞迴關係式的求解分為兩個步驟：

1. 求解特徵方程式$$t^k=d_1t^{k-1}+d_2t^{k-2}+\dots + d_k$$，並得到特徵根$$\lambda_1, \lambda_2,\dots, \lambda_k$$。
2. 由特徵根求通解。

* 如果$$k$$個根完全相異時，則齊次解為$$a_n=c_1\lambda_1^n+c_2\lambda_2^n+\dots + c_k \lambda_k^n, ~ n \geq 0$$ ，其中參參數$$c_1, c_2, \dots, c_k$$可由給定的初始條件求得。
* 有$$t<k$$個相異根，令$$\lambda_i$$有重根數$$m_i$$個，$$i=1,2,\dots, t$$，則相對於第$$i$$個特徵根的解為$$u_i(n)=(c_{i0}+c_{i1}n+\dots +c_{i m_i-1}n^{m_i-1})\lambda_i^n$$。\
  而$$a_n=u_1(n)+u_2(n)+\dots +u_t(n)$$
* 如果有一組共軛複根(相異根的特例)$$\lambda_1=\delta+ i\omega$$, $$\lambda_2= \delta - i\omega, \omega \neq 0$$\
  令$$\rho=\sqrt{\delta^2+ \omega^2}$$, $$\theta=\tan^{-1}\frac{\omega}{\delta}$$\
  則該組的解為$$c_1 \lambda_1^n + c_2 \lambda_2^n6$$



$$\begin{aligned} \begin{bmatrix} a_{n+1} \\ a_n \end{bmatrix} & = u_{n} \\     & = A^n u_{0}, ~ n \geq 0 \\     & = P D^n P^{-1}u_0  \endn{aligned}$$
