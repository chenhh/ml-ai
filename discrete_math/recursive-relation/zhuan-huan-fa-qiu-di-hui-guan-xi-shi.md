# 轉換法求遞迴關係式

## 簡介

特徵多項式法只適用於常係數遞迴關係式，有些關係式可先將參數轉換後，變成常係數式再求解。

## Divide-and-conquer演算法常見時間複雜度遞迴關係式

> $$a,b,c \in \mathbb{Z}^+$$, $$b \geq 2$$, 令$$f: \mathbb{Z}^+ \rightarrow \mathbb{R}$$，若
>
> * $$f(1)=c$$ 且
> * $$f(n)=af(\frac{n}{b})+c, ~ n=b^k~ k\geq 1$$&#x20;
>
> 則對於所有$$n=1,b,b^2,b^3,\cdots$$
>
> * 當$$a=1$$時，$$f(n)=c(\log_bn +1)$$.&#x20;
> * 當$$a \geq 2$$時，$$f(n)=\frac{c(an^{\log_b a}-1)}{a-1}$$
