# 數列的上、下極限

## 簡介

* 數列$$\{a_n\}$$的上極限和下極限為數列在索引值$$n$$無窮大時的值，為單點且可視為**數列在極限的上下界**。
* 數列的極限不一定存在，因為數列極限可能發散或是在區間內震盪（如正弦、餘弦函數）。
* **但數列的上、下極限必定存在**，因為序列的上極限或下極限為單點，沒有收斂的問題，且擴展實數中非空集合必有最小上（下）界。（考慮擴展實數是因為上、下極限可能為正負無窮大）。
* 下兩圖中，紅色的線是由$$n$$開始的序列最小上界（最大下界）所連成的線，即$$\sup\{x_n, x_{n+1},x_{n+2}, \ldots\}  $$與$$\inf\{x_n, x_{n+1},x_{n+2}, \ldots\}$$，而紅色的線在$$n \rightarrow \infty$$時才是$$\limsup⁡ x_n$$與$$\liminf x_n$$ 之值。

![&#x6578;&#x5217;&#x7684;&#x4E0A;&#x3001;&#x4E0B;&#x6975;&#x9650;&#x5FC5;&#x5B58;&#x5728;](../../.gitbook/assets/limsup_inf-min.png)

![&#x6578;&#x5217;&#x4E0A;&#x3001;&#x4E0B;&#x6975;&#x9650;&#x7684;&#x5B9A;&#x7FA9;](../../.gitbook/assets/lim_sup_inf_detail-min.png)

## 實數序列上極限\(limit superior of a sequence\)

> 令$$\{x_n\}_{n \in \mathbb{N}} \subseteq \mathbb{R}$$為一數列，
>
> * $$\displaystyle \overline{\lim_{n \rightarrow \infty}}x_n\equiv \limsup_{n \rightarrow \infty} x_n=\inf_{n \geq 0}\sup_{ k \geq n} x_k = \inf_{n \geq 0}\{\sup_{k \geq n} x_k\}$$或
> * $$\displaystyle \limsup_{n \rightarrow \infty} x_n =\lim_{ n \rightarrow \infty} (\sup_{k \geq n} x_k)$$
> * 上極限是所有收斂子序列的最大值。
> * 上極限是由第$$n$$個元素開始的最小上界形成集合的最大下界。

* 令$$\{x_n\}$$有上界，則$$\exists M \in \mathbb{R} \ni x_n \leq M,~ \forall n \in \mathbb{N}$$。
* 令$$\forall n \in \mathbb{N}, M_n=\sup\{x_n,x_{n+1}, x_{n+2},\ldots\}  $$
  * $$M_1$$ 為$$\{x_k\}_{k=1}^\infty$$ （第一個元素開始）的最小上界。
  * $$M_2$$ 為$$\{x_k\}_{k=2}^\infty$$ （從第二個元素開始）的最小上界。
  * 以此類推得$$ M_n$$ 為$$\{x_k\}_{k=n}^\infty$$ （從第$$n$$個元素開始）的最小上界。
  * 可得$$\displaystyle \limsup_{n \rightarrow \infty}⁡x_n =\lim_{n \rightarrow \infty}M_n  \in [-\infty, \infty]$$，即數列的上極限等於數列第$$n$$個至無窮多個元素的最小上界    。



