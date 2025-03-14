---
description: sequences of functions
---

# 函數序列

## 簡介

函數序列是在同一定義域的多個函數之集合，分析收斂性質時，要考慮定義域每一點的收斂速度，可分為點態收斂與一致收斂，其區別在於對於定義域所有點是否有收斂速度的上限。

* 點態收斂、逐點收斂(pointwise convergence)
  * 點態收斂：只要求每個點單獨收斂，速度和方式可以因點而異。
  * 函式曲線在每個$$x$$ 上逐漸靠近極限，但某些區域可能收斂很慢。
  * 點態收斂是「逐點檢查」的收斂。對於每個$$x$$，你單獨看序列$$\{f_n ​ (x)\}$$ 是否趨向於$$f(x)$$。
  * $$N_0$$可以隨著$$x$$的不同而改變(每個點收斂速度不同)，也就是說，不同的$$𝑥$$可能需要不同的$$𝑛$$才能使 $$f_n ​ (x)$$ 足夠接近 $$f(x)$$。
  * <mark style="color:red;">點態收斂無法保證連續函數收斂為連續函數</mark>，但能保證收斂為處處連續函數。
  * <mark style="color:red;">點態收斂無法保證可微分函數收斂為可微分函數</mark>。
  * <mark style="color:red;">點態收斂無法保證函數序列(Riemann)積分收斂到函數極限的積分</mark>。
  * <mark style="color:blue;">因此連續函數在極限運算下不滿足封閉性</mark>。
* 一致收斂、均勻收斂(uniform convergence)
  * 一致收斂要求函式序列在定義域$$D$$ 上「整體一致地」接近極限函式$$f(x)$$。
  * 函式曲線在整個定義域上「整齊地」貼近極限，像一張毯子均勻覆蓋。
  * $$N_0$$ 是統一的，對所有的$$𝑥$$都有效，這意味著序列$${f_n ​ (x)}$$在整個定義域上的誤差同時變小，而不是某些點快、某些點慢。
  * 均勻收斂保連續函數收斂為連續函數
  * <mark style="color:red;">均勻收斂可保證函數序列Riemann積分收斂至函數序列極限的積分</mark>。
* 逐點有界：逐點有界的概念僅保證對於每個固定點，函式序列的值都不會無限制增大，但這個界限可能隨點而變。
* 一致有界(uniformly bounded)：一致有界是對所有點以及對所有函有共同的全域上下界。
* 有界收斂

在Lebesgue積分中，只要可測函數序列幾乎點態收斂再加上部分限制條件，即可保證Lebesuge積分收斂。

<mark style="color:red;">一個序列可以點態收斂但不一致收斂（如</mark>$$x^n$$<mark style="color:red;">在</mark>$$[0,1]$$ <mark style="color:red;">上），但如果一致收斂，則一定點態收斂</mark>。

## 函數序列

令$$S \subseteq \mathbb{R}^n$$為歐式空間非空集合，$$\forall n \in \mathbb{N}$$，給定函數$$f_n: S \rightarrow \mathbb{R}$$，則$$\{f_n\}_{n \in \mathbb{N}}$$為定義在集合$$S$$的函數序列。

#### 範例

* $$S=[0,1]$$, $$f_n(x)=x^n$$
* $$S=[0,1], f_n(x)=nx(1-x^2)^n$$
* $$S=[-\pi, \pi], a_n, b_n \in \mathbb{R}$$, $$f_n(x)=a_n \cos(nx) + b_n \sin(nx)$$

## 函數數列的點態(逐點)收斂

> 給定同一定義域的實數(複數)函數數列$$\{f_n\}$$，若函數$$f$$滿足 $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x), ~ x \in S$$，則稱函數$$f$$為函數數列的<mark style="color:red;">極限函數(limit function)</mark>，且稱<mark style="color:red;">函數數列</mark>$$\{f_n\}$$<mark style="color:red;">逐點收斂至集合</mark>$$S$$。
>
> $$\forall x \in S$$, $$\forall \epsilon > 0 \exists n_0 \in \mathbb{N} \ni d(f_n(x) - f(x)) < \epsilon ~\forall n \geq n_0$$
>
> 點態收斂中，$$n_0$$依賴於$$\epsilon$$與$$x$$兩者。(一致收斂只依賴於$$\epsilon$$，而與$$x$$的實際取值無關)。

點態收斂中，每一點$$x$$只考慮$$B_{\epsilon}(x)$$的收斂性，而非集合$$S$$內所有點的收斂性，因此給定$$\epsilon>0$$，當$$x_1 \neq x_2$$時，兩者收斂時所需要的項次$$n_1, n_2$$可能沒有上限。

<mark style="color:red;">點態收斂無法保證連續函數收斂為連續函數，但可保證連續函數收斂為處處連續函數(不收斂的集合測度為0)</mark>。

### 點態收斂的每一點收斂速度相異

$$f_n(x)= \frac{1}{nx^2+1}, ~ x \in \mathbb{R}, ~ n \in \mathbb{N}$$。

* 若 $$x \neq 0$$，則 $$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=0$$。
* 若 $$x=0$$，可得 $$\displaystyle \lim_{n \rightarrow \infty}f_n(x) = 1$$

給定$$\epsilon = 0.5$$，

* 在$$x=0$$時，只要$$n \geq 1$$即可滿足。
* $$x=1$$時，須$$n > 1$$。
* $$x=\frac{1}{100}$$時，需要$$n > \frac{1}{10000}$$。

因此給定$$\epsilon$$值，對相異的$$x$$，收斂所需要$$n$$值大小程度不同(沒有上限)。

#### 範例：點態收斂無法保證連續函數收斂為連續函數

令$$f_n(x)=\frac{x^{2n}}{1+x^{2n}}, ~ x \in \mathbb{R}, ~ n \in \mathbb{N}$$,則$$\displaystyle \lim_{n \rightarrow \infty} f(x) = \left\{ \begin{aligned} 0 & \text{ if } |x| \leq 1, \\ \frac{1}{2} & \text{ if } |x| = 1 \\ 1 & \text{ if } |x| > 1 \end{aligned} \right.$$，由連續函數收斂至非連續函數(但為幾乎處處連續函數)。

![逐點收斂無法保證函數連續性](../../.gitbook/assets/Figure_1-min.png)

<details>

<summary>code，逐點收斂無法保證函數連續性</summary>

```python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def PointwiseConvergeOfsequenceContinuousFunction():
    # 點態收斂無法保證連續函數收斂為連續函數
    xs = np.arange(-1, 1, 0.001)
    ns = range(1, 100)

    for n in ns:
        xs2n = xs**(2*n)
        ys = xs2n/(1+xs2n)
        plt.plot(xs, ys)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    PointwiseConvergeOfsequenceContinuousFunction()
```

</details>

### 範例：點態收斂無法保證函數可微

$$S=[0,1]$$，$$\displaystyle f_n(x)=\sqrt{\frac{nx^2+1}{n}}$$

可得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} \sqrt{\frac{nx^2+1}{n}} = \lim_{n \rightarrow \infty}\sqrt{x^2+\frac{1}{n}}=\sqrt{x^2}=|x|$$

因此$$f(x)=|x|$$在$$[0,1]$$連續，但是在$$x=0$$不可微分。

### 範例：點態收斂無法保證函數積分收斂到極限函數的積分

函數序列$$\displaystyle \lim_{n \rightarrow \infty} \int_0^1 f_n(x) dx \neq \int_0^1 \lim_{n \rightarrow \infty} f_n(x)dx$$

令$$f_n(x)=n^2x(1-x)^n, ~ \forall x \in \mathbb{R}$$

若$$0 \leq x \leq 1$$，則$$\displaystyle f(x) = \lim_{n \rightarrow \infty} f(x) = 0$$存在，所以$$\displaystyle \int_0^1 f(x) dx = 0$$

但是$$\displaystyle \int_0^1 f_n(x) dx = n^2 \int_0^1 x(1-x)^n dx = n^2 \int_0^1 (1-t)t^n dt= \frac{n^2}{(n+1)(n+2)}$$

可得 $$\displaystyle \lim_{n \rightarrow \infty }\int_0^1 f_n(x) dx = 1$$

## 一致收斂的定義

> 有二種常見的定義：令函數序列$$\{f_n\}$$在集合$$S$$內一致收斂至函數$$f$$：
>
> 1. \[ε–delta 定義] $$\forall \epsilon > 0$$ $$\exists n_0 \in \mathbb{N}$$ ($$n_0$$只依賴與於$$\epsilon$$的選擇，與$$x$$的實值取值無關)$$\forall x \in S \ni |f_n(x) - f(x)|< \epsilon, ~\forall n \geq n_0$$&#x20;
> 2. \[上確界表示法] $$\displaystyle \forall \epsilon > 0, \exists n_0 \in \mathbb{N} \ni \sup_{x \in S}|f_n(x) - f(x)| < \epsilon~ \forall n \geq n_0$$。
>
> 2.1. \[範數表示法] 可表示為 $$\displaystyle \lim_{n \rightarrow \infty} \sup_{x \in S} \| f_n(x) - f(x) \| = 0$$。(此處的lim與sup是分開的，而非limsup。)。為了避免混肴，可寫成$$d_n=\displaystyle \sup_{x \in S} \| f_n(x) - f(x) \|$$，$$\displaystyle \lim_{n \rightarrow \infty}d_n=0$$。
>
> 2.2. \[範數表示法] 可再改寫為$$\sup_{x \in S}|f_n(x) - f(x)| \leq M_n$$，其中$$\{M_n\}$$為非負值且收斂至0的數列。
>
> 註：範數表示法的名稱是因為 $$\|f\|_{\infty} = \sup\{\|f(x)\| ~|~ x \in S \}$$為函數的上界範數(supremum norm)
>
> 3. \[完備空間中可用Cauchy定義] 函數序列$$f_n \rightarrow f$$在$$S$$一致收斂 ⟺ $$\{f_n\}$$ 為一致 Cauchy 序列，即$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni |f_m(x)-f_n(x)|<\epsilon, ~\forall m,n >n_0, ~ \forall x \in S$$
>
> <mark style="color:red;">重點在表達了“全域誤差”的最大值趨於零</mark>。
>
> 註：一致收斂的充要條件是$$\{f_n\}$$滿足Cauchy條件。$$\forall \epsilon > 0, ~\exists n_0 \in \mathbb{N} \ni |f_n(x)-f_m(x)|<\epsilon, ~ \forall m,n > n_0, \forall x \in S$$。

此處$$\epsilon$$的選擇是針定所有的點$$x$$均成立，與點態收斂中$$\epsilon$$可能依$$x$$變化不同。

由2的定義可看出對於$$\forall x \in S$$，只要$$n \geq n_0$$即可保證所有點的收斂速度一致；換句話說，只要$$S$$為閉集合，只要取$$n_0$$為集合內所有點收斂時的最大值即可滿足一致收斂的定義。

一致收斂在極限時可表示為只與$$n$$有關，而與$$x$$無關的函數，見以下範例。

<details>

<summary>proof: epsilon-delta與sup定義的等價性</summary>

proof=>

令$$\{f_n\}\rightarrow f$$在集合$$S$$一致收斂，由定義得給定$$\epsilon =1$$，存在$$n_0 \ni \mathbb{N} \ni |f_n(x) -f(x)|\leq 1 \forall n \geq n_0, \forall x \in S$$。

令$$\displaystyle M_n = \sup_{x_\in S} |f_n(x)-f(x)| \geq 0$$為有限非負值，$$\forall n \geq n_0$$。

定義在$$1\leq n \leq n_0-1$$時，$$M_n \geq 0$$為任意非負值。

由於函數一致收斂，因此$$n \geq n_0$$時，可得$$|f_n(x)-f(x)| < \epsilon$$，可得$$\displaystyle M_n = \sup_{x_\in S} |f_n(x)-f(x)| < \epsilon$$，因此$$\displaystyle \lim_{n \rightarrow \infty }M_n = 0$$ (QED)

proof <=

令$$\{M_n\}$$為非負數列$$\displaystyle \lim_{n \rightarrow \infty }M_n = 0$$，且$$\sup_{x \in S}|f_n(x) - f(x)| \leq M_n ~ \forall n \geq n_0$$

給定$$\epsilon > 0$$由數列收斂得$$\exists n_1 \in \mathbb{N} \ni M_n < \epsilon ~ \forall n \geq n_1$$

取$$n_2 \geq \max(n_0, n_1)+1$$，可得$$\displaystyle \sup_{x \in S}|f_n(x) - f(x)| \leq M_n <\epsilon ~ \forall n \geq n_2$$。

因此可得$$n \geq n_2$$時，$$|f_n(x)-f(x)|< \epsilon ~ \forall x \in S$$，因此為一致收斂(QED)

</details>

### 一致收斂為點斂收斂

> <mark style="color:red;">若</mark>$$\{f_n\} \rightarrow f$$<mark style="color:red;">一致收斂，則</mark>$${f_n} \rightarrow f$$<mark style="color:red;">點態收斂</mark>。

<details>

<summary>proof</summary>

要證明$$f_n$$ 點態收斂於$$f$$ ：任取一點$$x \in E$$ ，任選一個$$\epsilon >0$$，一定能夠找到正整數$$n_0$$ (依賴於$$x$$與$$\epsilon$$)，使得 $$n \geq n_0$$時可得$$|f_n(x) - f(x)|<\epsilon$$ 。所以關鍵在於怎麼找到滿足條件的正整數$$n_0$$ 。

因為$$f_n$$一致收斂於$$f$$ ，則由定義有：對每個$$\epsilon >0$$ ，存在正整數$$n_1$$ (只依賴於$$\epsilon$$)，使得$$n \geq n_1$$ ，對所有的$$x \in E$$ 可得$$|f_n(x) - f(x)|<\epsilon$$ 。

因此，只需取$$n_0= n_1$$ ，可得對於給定的$$x$$，確實有$$n \geq n_0$$ ，可得$$|f_n(x)-f(x)|<\epsilon$$  。

(QED)

</details>

<figure><img src="../../.gitbook/assets/pointwise_conv.jpg" alt=""><figcaption><p>點態收態，f與fn的距離在每一點x可能不同</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/uniform_conv.jpg" alt=""><figcaption><p>一致收斂，f與fn在定義域每一點都可保持在相同的距離內</p></figcaption></figure>

#### 範例

$$S=[-5,5]$$，$$f_n(x)=(2xn+(-1)^n x^2)/n$$，則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)=2x$$ uniformly.

$$\displaystyle \begin{aligned} |f_n(x) - f(x)| & = \left| \frac{2xn+(-1)^n x^2}{n} - 2x \right| \\ & = \left| \frac{(-1)^n x^2}{n} \right| \\ & = \frac{x^2}{n} \\ & \leq \frac{5^2}{n} ~ \because x \in [-5,5] \end{aligned}$$

因此給定$$\epsilon >0$$時，只要取$$n_0 \in \mathbb{N} \ni \frac{5^2}{n_0} < \epsilon$$，$$n_0 > \frac{5^2}{\epsilon}$$即為所求。

也可用$$\displaystyle d_n=\sup_{x \in S}|f_n(x)-f(x)| = \sup_{x \in S}\frac{x^2}{n} = \frac{25}{n}$$，可得$$\displaystyle \lim_{n \rightarrow \infty }d_n = 0$$為一致收斂。

#### 範例

$$S=\mathbb{R}$$，$$f_n(x)=\sin(nx)/\sqrt{n}$$，$$f(x)=0$$

$$\displaystyle \begin{aligned} |f_n(x) - f(x)| &= \| \frac{\sin(nx)}{\sqrt{n}} \| \\ &= \frac{|\sin(nx)|}{\sqrt{n}} \\ & \leq \frac{1}{\sqrt{n}} \end{aligned}$$

因此給定$$\epsilon >0$$，只要取$$\frac{1}{n_0} < \epsilon \Rightarrow n_0 > \frac{1}{\epsilon}$$即為所求。

也可用$$\displaystyle d_n=\sup_{x \in \mathbb{R}} \frac{\sin(nx)}{\sqrt{n}}=\frac{1}{\sqrt{n}}$$，可得$$\displaystyle \lim_{n \rightarrow \infty} d_n=0$$為一致收斂。

### \[一致連續性]連續函數序列若一致收斂仍為連續函數

> 假設所有的函數$$f_n$$均在點$$c \in S ~ \forall n \in \mathbb{N}$$連續，若$$f_n$$一致收斂至函數$$f$$，則$$f$$也在點$$c \in S$$連續。
>
> 若$$c$$為集合$$S$$的極限點，可得$$\displaystyle \lim_{x \rightarrow c}\lim_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} \lim_{x \rightarrow c} f_n(x)$$
>
> 在一般度量空間$$(S,d)$$也成立

<details>

<summary>proof: 可分c為孤立點和極限點的情形</summary>

若$$c$$為孤立點，則點$$f$$在$$c$$必定連續。

若$$c$$為極限點，由一致連續假設得$$\forall \epsilon >0 \forall x \in S ~\exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x) |< \epsilon$$

因為所有的函數序列均在$$c$$連續，因此存在開球$$B(c, r)$$滿足$$\forall x \in B(c,r) \cap S$$, $$|f_{n_0}(x) - f_{n_0}(c)| < \epsilon$$

由於 $$|f(x)-f(c)| \leq |f(x) - f_{n_0}(x)| + |f_{n_0}(x) - f_{n_0}(c)| + |f_{n_0}(c) - f(c)|$$

且當$$x \in B(c,r) \cap S$$可得$$|f(x) - f(c)|< 3 \epsilon$$ (QED)

</details>

### 一致收斂函數序列在加減法後仍為一致收斂

> $$\{f_n\} \rightarrow f$$ uniformly on $$S$$且$$\{g_n\} \rightarrow g$$ uniformly on $$S$$，則可得$$\{f_n \pm g_n\} \rightarrow f \pm g$$ uniformly on $$S$$。

#### 範例：一致收斂函數序列在乘法時沒有一致收斂的性質

$$f_n(x) = x + \frac{1}{n}, ~ x \in \mathbb{R}$$，則函數序列一致收斂至$$f(x)=x, ~\forall x \in \mathbb{R}$$。

$$g_n(x)=(f_n(x))^2 = x^2 + \frac{2x}{n} + \frac{1}{n^2}, ~ x \in \mathbb{R}$$，則函數序列點態收斂至$$g(x)=x^2, ~\forall x \in \mathbb{R}$$。

但是$$\displaystyle \forall n \in \mathbb{N}~, \sup_{x \in \mathbb{R}}\| g_n(x) - g(x) \| = \infty$$，並非一致收斂。

### 一致收斂與內積

> $$\{f_n: S \rightarrow \mathbb{R}^n \} \rightarrow f$$ uniformly且$$\{g_n: S \rightarrow \mathbb{R}^n\} \rightarrow g$$ uniformly，
>
> 若極限函數$$f,g$$均為有界函數，則內積函數序列$$\{ \langle f_n, g_n \rangle \}$$在$$S$$一致收斂至內積 $$\langle f,g \rangle$$。

## 逐點有界(pointwise bounded)

> 定義：函數$$\{f_n\}$$在集合$$S$$稱為逐點有界若存在有限值域函數$$g(x) >0 \ni ~|f_n(x)| \leq g(x), ~\forall x \in S, ~\forall n \in \mathbb{N}$$

對於定義在集合$$S$$上的函數序列$$\{f_n\}$$，對每一個固定的$$x \in S$$，存在一個與$$n$$無關的常數$$g(x)>0$$使得對所有的$$n$$都滿足$$|f_n(x)| \leq g(x)$$。

<mark style="color:red;">逐點有界的概念僅保證對於每個固定點，函式序列的值都不會無限制增大，但這個界限可能隨點而變</mark>。

## 一致有界(uniformly bounded)

> 定義：函數$$\{f_n\}$$在集合$$S$$稱為一致有界若存在常數$$M > 0, |f_n(x)| \leq M, ~ \forall x \in S, \forall n \in \mathbb{N}$$。

一致有界是對所有$$x \in S$$以及對所有$$f_n$$有共同的全域上下界，<mark style="color:red;">但點態收斂不保證極限函數會在此上下界中</mark>。

* 逐點有界對每一點$$x \in S$$，$$f_n(x)$$的上界會隨$$g(x)$$而變動。
* 而一致有界是對於所有的$$\forall x \in S$$，$$f_n(x)$$都有相同的上界$$M$$。
* <mark style="color:red;">簡單判斷函數數列是否為一致有界的方法是取</mark>$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)$$<mark style="color:red;">，然後看結果若只與</mark>$$n$$<mark style="color:red;">有關，則為一致有界，否則為逐點有界或無上/下界</mark>。

簡單地說，一致有界中的邊界$$M$$是一個固定量，而(逐點)有界中的$$M$$是允許隨其他量變化的。例如每一個常數函數都是有界函數，但是放在一起不是一致有界的。一致有界就是一堆函數有一個共同的界。

如果在平面上繪圖，將所有函數序列繪圖，如果能夠找到一條水平線$$f(x)=M$$蓋住所有的函數序列，則為一致有界。

範例：$$f_n(x)=\sin(nx)$$有界且一致有界因為$$|f_n(x)| \leq 1, \forall n$$。

範例：$$f_n(x)=n \cdot \sin(x)$$有界但不是一致有界。因為只能得到$$|f_n(x)| \leq n, ~\forall n, \forall x$$不存在固定的上界。

### 有界且一致有界但無上下界的函數序列仍可一致收斂

$$f_n(x) = x + \frac{1}{n}, ~ x \in \mathbb{R}$$，在$$\forall n \in \mathbb{N}$$均非有界函數。

而極限函數 $$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = \lim_{n \rightarrow \infty} x+ \frac{1}{n} = x$$非有界函數。

$$|f_n(x) - f(x)| = |x+\frac{1}{n} - x|\leq |\frac{1}{n}|$$只與$$n$$有關，因此為一致收斂。

### 一致收斂且個別函數有界時可得一致有界

> 令$$\{f_n\} \rightarrow f$$ 在集合$$S$$一致收斂，且$$f_n, ~\forall n \in \mathbb{N}$$在$$S$$上(逐點)有界，則$$f_n$$在集合$$S$$一致有界。

### 範例：一致有界函數序列不一定收斂

$$f_n(x)=\frac{x^2}{x^2+(1-nx)^2}$$

給定$$x \in [0,1]$$可得，$$|f_n(x)|=|\frac{x^2}{x^2+(1-nx)^2}|\leq 1$$。

因此$$M=1$$時，$$f_n(x)$$在$$[0,1]$$一致有界。

$$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=\lim_{n \rightarrow \infty} \frac{x^2}{x^2+(1-nx)^2}=\lim_{n \rightarrow \infty} \frac{1}{1+n^2}=0$$

但supnorm $$\|f_n(x)-0\|=\sup_{x \in [0,1]}|\frac{x^2}{x^+(1-nx)^2}|=1 \neq 0$$

所以不是一致收斂。

## 一致收斂的Cauchy條件

> 令$$\{f_n\}$$為定義在\[完備空間]集合$$S$$上的函數序列。
>
> 函數序列$$f_n \rightarrow f$$在$$S$$一致收斂 ⟺ 則$$\{f_n\}$$為一致 Cauchy 序列，即$$\forall \epsilon >0 \exists n_0 \in \mathbb{N} \ni |f_m(x)-f_n(x)|<\epsilon, ~\forall m,n >n_0, ~ \forall x \in S$$
>
> 即給定$$\epsilon$$後，集合$$S$$中的所有點只要在$$n \geq n_0$$項之後， 任兩個函數列中的函數均收斂。
>
> 在一般度量空間$$(S,d)$$中也成立。

註：可得$$\{f_n\}$$非一致收斂，即存在$$\{f_n\}$$的一個子函數列，以及$$S$$中的一個數列$$\{x_m\}$$使得子函列在$$\{x_m\}$$不收斂於0。

<details>

<summary>proof</summary>

\=> 令$$f_n \rightarrow f$$在點$$S$$上一致收斂，由定義得$$\forall \epsilon >0, ~\forall x \in S, ~\exists n_0 \in \mathbb{N} \ni |f_n(x) - f(x)| < \epsilon/2, ~ \forall n > n_0$$

同樣的田定義可得 $$|f_m (x) - f(x) | < \epsilon/2, ~ \forall m > n_0$$

合併上述兩式得$$\forall x s\in S, ~|f_m(x)-f_n(x)|<\epsilon$$ (QED)

<=

由Cauchy條件得$$\forall x \in S, ~\{f_n(x)\}$$收斂，令$$\displaystyle f(x)=\lim_{n \rightarrow \infty} f_n(x),~ x \in S$$。

當$$\epsilon>0$$，$$\forall x \in S$$，由Cauchy條件可得$$|f_n(x) - f_{n+k}(x)| < \epsilon/2, ~k=1,2,\dots$$

因此$$\displaystyle$$$$\displaystyle \lim_{k \rightarrow \infty }|f_n(x) - f_{n+k}(x)| = |f_n(x) - f(x)| < \epsilon/2$$

因此$$\forall n > n_0$$，$$\forall x \in S$$，可得$$|f_n(x) - f(x) | < \epsilon$$ (QED)

</details>

## 判定一致收斂方法: Dini

> 令 $$f_n : S \rightarrow \mathbb{R} ~ S \subseteq \mathbb{R}^n$$，若：
>
> 1. $$S$$為緊致集
> 2. $$\forall x \in S ~ \{f_n(x)\}$$均為收斂的遞減(或遞增)數列，其(點態收斂)極限函數為$$f(x)$$
> 3. $$f, f_n, ~\forall n$$均在$$S$$上連續。
>
> 則$$\{f_n\}$$在集合$$S$$上一致收斂至$$f$$。
>
> 此為測度論中 MCT的連續版本。

## 判定一致收斂方法: Polya

> $$\{ f_n: [a,b] \rightarrow \mathbb{R} \}$$，若
>
> 1. 所有$$f_n$$均為遞增函數
> 2. 函數序列$$\{f_n\}$$在$$[a,b]$$逐點收斂於函數$$f: [a,b] \rightarrow \mathbb{R}$$
> 3. 極限函數$$f$$在$$[a,b]$$為連續函數
>
> 則$$\{f_n\}$$在$$[a,b]$$上一致收斂至$$f$$。

## 一致收斂與Riemann-Stieltjes積分

> 令函數$$\alpha$$在閉區間$$[a,b]$$有界變差。
>
> 令實值函數序列$$\{f_n\}$$在$$[a,b]$$相對於$$\alpha$$Riemann-Stieltjes可積$$\forall n \in \mathbb{N}$$。
>
> 若$$f_n \rightarrow f$$在$$[a,b]$$一致收斂，且定義$$g_n(x)=\int_a^x f_n(t) d \alpha(t), x \in [a,b], n \in \mathbb{N}$$，則：
>
> 1. $$f$$在$$[a,b]$$相對於$$\alpha$$ RS可積。
> 2. $$g_n \rightarrow g$$在$$[a,b]$$一致收斂，$$g(x)=\int_a^x f(t) d \alpha(t)$$。
>
> 即$$\forall x \in [a,b]$$，可得$$\displaystyle \lim_{n \rightarrow \infty}\int_a^x f_n(t)d\alpha(t)=\int_a^x \lim_{n \rightarrow \infty} f_n(t)d \alpha(t)$$。

## 有界收斂(bounded convergence)

> 定義：函數序列$$\{f_n\}$$在集合$$S$$若為點態收斂(至$$f$$)($$\displaystyle \lim_{n \rightarrow \infty} f_n(x)=f(x)$$)且一致有界($$\exists M >0 \ni |f_n(x)| \leq M~\forall n,~\forall x \in S$$)，則稱$$\{f_n\}$$有界收斂。

### Arzela's bounded convergence theorem

> 函數序列$$\{f_n\}$$在閉區間$$[a,b]$$有界收斂，且所有的函數$$f_n$$在$$[a,b]$$均為Riemann可積分。
>
> 假設極限函數$$f$$在$$[a,b]$$也為Riemann可積分，則：
>
> $$\displaystyle \lim_{n \rightarrow \infty} \int_a^b f_n(x) dx = \int_a^b \lim_{n \rightarrow \infty} f_n(x) dx = \int_a^b f(x) dx$$

註：存在$$\{f_n\}$$在$$[a,b]$$有界收斂且Riemann可積，但$$f$$在$$[a,b]$$不可積分。

註：Lebesgue積分中，Bounded convergence theorem的條件為$$\{f_n\}$$為定義在有限測度集$$E$$($$m(E)<\infty$$)的可測函數，且$$\{f_n\}$$在$$E$$一致有界($$\exists M\geq 0 \ni |f_n(x)| \leq M, \forall n, \forall x \in E$$)。若$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)=f(x)$$則，$$\displaystyle \lim_{n \rightarrow \infty} \int_E f_n = \int_E f$$。 (但有可能兩側均不可積)



### 範例：函數序列有界收斂且可積分但極限函數不可積分

令$$\{r_1, r_2,\dots\} \subseteq [0,1]$$為有理數集合，令$$f_n(x) = \left\{ \begin{aligned} &1, ~\text{ if } x = r_k, ~k=1,2,\dots,n \\ &0, ~ \text{ otherwise } \end{aligned} \right.$$

可得$$\displaystyle \int_0^1 f_n(x)dx=0, ~ \forall n$$，但$$\lim_{n \rightarrow \infty} f$$在$$[0,1]$$不可Riemann積分(但可Lebesgue積分)。
