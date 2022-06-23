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
> $$\sum_{i=0}^kc_{n-i}a_{n-i}=c_na_n+c_{n-1}a_{n-1}+\dots +c_{n-k}a_{n-k}=f(n)$$稱為一$$k$$​階常係數遞迴關係式(linear recurrence relation with constant coefficients of order k)。
>
> 若$$f(n)=0, ~ \forall n \geq 0$$則稱為齊次(homogeneous)遞迴關係式。
>
> 否則稱為非齊次(non-homogeneous)遞迴關係式。

