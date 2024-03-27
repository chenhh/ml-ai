---
description: student distribution
---

# t分佈

## 簡介

常用的三大抽樣分佈之一，t分佈，卡方分佈，F分佈。

令隨機變數$$X \sim N(0,1)$$，$$Y \sim \chi_n^2$$為自由度$$n$$的卡方分佈，則$$T=\frac{X}{\sqrt{Y/n}} \sim t(n)$$為自由度$$n$$的t分佈。

t 分佈說明當母體標準差$$\sigma$$不明，且觀察結果來自常態分佈母體時，樣本平均數與母體平均數之間的標準距離。

* 和常態分佈相同，t 分佈的形狀很平滑。&#x20;
* 和常態分佈相同，t 分佈對稱呈現。
* 如果從平均數將分佈圖形對折，兩邊會是同等大小。&#x20;
* 和標準常態分佈 (或 z 分佈) 相同，t 分佈的平均數為 0。
* <mark style="color:red;">常態分佈假設母體標準差已知。t 分佈則不做此假設</mark>。&#x20;
* t 分佈由自由度定義。自由度與樣本量相關。
* <mark style="color:red;">t 分佈在樣本量較小、標準差未知，或兩者條件兼具時最有用</mark>。&#x20;
* 隨著樣本量增加，t 分佈會越來越近似於常態分佈。
* 大原則為在樣本量至少為 30 時，可以用常態分佈取代 t 分佈。

<figure><img src="../../.gitbook/assets/image (19).png" alt="" width="375"><figcaption><p>t 分佈與標準常態分佈。</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (20).png" alt="" width="375"><figcaption><p>常態分佈與自由度為 30 時的 t 分佈</p></figcaption></figure>

## 機率密度函數

$$X \sim t(n)$$，

$$\displaystyle  \begin{aligned} f(t) &= \frac{\Gamma((n+1)/2)}{\sqrt{n \pi} \Gamma(n/2)} (1+t^2/n)^{-(n+1)/2}, ~ t \in \mathbb{R} \\ \Gamma(n) &= \int_0^\infty t^{n-1} e^{-t} dt, ~ n > 0  \end{aligned}$$

在 t 分佈裡, 若自由度$$n=1$$，得到柯西分佈$$\mathcal{C}(0,1)$$。

期望值：$$\mathrm{E}(X) =0, n \geq 2$$。

變異數：$$\mathrm{Var}(X) = \frac{n}{n-2}, n \geq 3$$。
