# Taylor級數

## 泰勒定理\(Taylor theorem\)

> 若$$f:\mathbb{R} \rightarrow \mathbb{R}$$為多項式函數（無窮階可微分）時，可得$$ f(x)=f(c)+f^{′}(c)(x−c)+\frac{(f^{(2)} (c)}{2! }(x−c)^2+\cdots + \frac{(f^{(n) } (c)}{n!} (x−c)^n$$

若$$f$$推廣至$$C^{(n+1)}$$ 函數\(即函數$$f$$為$$n+1$$階可微分的連續函數\)，可得以下三類推廣：

* Taylor定理積分餘式\(Taylor's theorem with integral remainder\)推廣微積分基本定理。
* Taylor定理Cauchy餘式推廣均值定理  。
* Taylor定理Lagrange餘式推廣均值定理。

## Taylor級數

> 函數$$f:(a,b) \rightarrow \mathbb{R}$$ 為$$(n+1)$$階可微分的連續函數，給定$$c \in (a,b)$$，若Taylor定理中的餘式$$\displaystyle \lim_{ n \rightarrow \infty} R_n(x)=0$$時，得Taylor級數：
>
> $$\displaystyle f(x)=\sum_{k=0}^\infty \frac{f^{(k)}(c)}{k!}(x-c)^k=f(c)+f^{'}(c)(x-c)+\frac{f^{(2)}(c)}{2!}(x-c)^2 + \dots + \frac{f^{(n)}(c)}{n!}(x-c)^n+\dots$$

## Maclaurin級數

> 當Taylor級數c=0時，稱為Maclaurin級數 。$$\displaystyle f(x)=\sum_{k=0}^\infty \frac{f^{(k)}(0)}{k!}x^k=f(0)+f^{'}(0)x+\frac{f^{(2)}(0)}{2!}x^2 + \dots + \frac{f^{(n)}(0)}{n!}x^n+\dots$$



## Taylor定理積分餘式\(Taylor's theorem with integral remainder\)

> 函數$$f:(a,b) \rightarrow \mathbb{R}$$ 為$$(n+1)$$階可微分的連續函數，記為$$f \in C^{n+1} (a,b) $$。給定 $$c \in (a,b)$$ 可得Taylor定理積分餘式：
>
> $$\displaystyle f(x)=f(c)+f^{′}(c)(x−c)+ \frac{f^{(2)}(c)}{2!} (x−c)^2+\dots+\frac{f^{(n)} (c)}{n!} (x−c)^n+\int_c^x \frac{(x−t)^n}{n!} f^{(n+1)} (t)dt $$

## Taylor定理Cauchy餘式

> 函數$$f:(a,b) \rightarrow \mathbb{R}$$ 為$$(n+1)$$階可微分的連續函數，記為$$f \in C^{n+1} (a,b) $$。給定 $$c \in (a,b)$$ ，則對於$$ x\in (a,b)$$，存在$$\xi \in (c,x)$$得Cauchy餘式：
>
> $$\displaystyle  f(x)=f(c)+f^{′}(c)(x−c)+\frac{f^{(2)}  (c)}{2!} (x−c)^2+\dots+ \frac{f^{(n)} (c)}{n!} (x−c)^n+\frac{f^{(n+1)} (\xi)}{n!} (x−\xi)^n (x−c)$$

## Taylor定理Lagrange餘式

> 函數$$f:(a,b) \rightarrow \mathbb{R}$$ 為$$(n+1)$$階可微分的連續函數，記為$$f \in C^{n+1} (a,b) $$。給定 $$c \in (a,b)$$ ，則對於$$ x\in (a,b)$$，存在$$\xi \in (c,x)$$得

> $$\displaystyle  f(x)=f(c)+f^{′}(c)(x−c)+\frac{f^{(2)}  (c)}{2!} (x−c)^2+\dots+ \frac{f^{(n)} (c)}{n!} (x−c)^n+\frac{f^{(n+1)} (\xi)}{(n+1)!}  (x−c)$$



