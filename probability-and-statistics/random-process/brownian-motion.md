# 布朗運動(Brownian motion)

## 簡介

布朗運動是由Rober Brown(1828)首先觀察花粉分子存浮於液體內上下變動的一種物理過程。1990年時，Bachellier在他的博士論文中，將布朗運動運用在股價變動的模型。在1923年，由N.Wiener{維納）研究布朗運動的數學理論，嚴謹定義存在性，它是標度隨機漫步（scaled random walk）的極限隨機過程。因此布朗運動也稱為維納過程。Paul Samuelson（1970年諾貝爾經濟學獎得主）在1969年引入布朗運動研究財務經濟學的模型。

<mark style="color:red;">布朗運動為一特殊的高斯過程(Gaussian process)</mark>。

## 布朗運動

> 一個連續的隨機過程$$\{ B_t, 0 \leq t <\infty \}$$，在時間$$[0,\infty)$$稱為標準布朗運動（standard Brownian motion）必須滿足以下四個條件：
>
> 1. $$B_0=0$$，在起始點$$t=0$$時，其值為0。
> 2. \[獨立增量]，即在不相交的區間之下，其相互的增量是獨立的。
>    * 令$$0 \leq t_1  <t_2 <\ldots< t_n =T$$，增量為隨機變數$$B_{t_1}-B_{t_0}, B_{t_2}-B_{t_1}, \ldots, B_{t_n}-B_{t_{n-1}}$$是獨立的（可得相關係數為0）。
>    *
>
>        獨立增量指每一步的變化量彼此獨立，因此上一步與下一步無關，即$$\mathrm{P}(B_{t_i} -B_{t_{i-1}} |B_{t_{1}} - B_{t_{0}} , \ldots, B_{t_{i-1}} - B_{t_{i-2}}) = \mathrm{P}(B_{t_i} -B_{t_{i-1}})$$
> 3. \[平穩性]每一個隨機變數都是常態分佈，$$B_{t_i} - B_{t_{i-h}} \sim N(0, \sigma^2h)$$。當$$\sigma^2=1$$時，稱為標準布朗運動。
> 4. $$B_t$$是時間的連續函數，或者說$$B_t$$的樣本路徑連續。

> 第2點可弱化為獨立於區間$$[i, i+h)$$起始點$$i$$的布朗運動，$$B_{t_{i+h }} - B{t_i} \sim N(0, \sigma^2h)$$ 。

* 布朗運動為連續的函數，但處處（每一點）均不可微分。
* 由定義得在時間$$t$$，$$B_t - B_0 \sim N(0, \sigma^2t)$$，因此$$B_t \sim N(0,t)$$。

## Weiner過程

> 一個連續的隨機過程$$\{ W_t, 0 \leq t <\infty \}$$，在時間$$[0,\infty)$$稱為Weiner過程滿足以下條件：
>
> 1. $$W_0=0$$.&#x20;
> 2. \[均方可積且平賭] $$\mathrm{E}(W_t^2)<\infty$$, $$\mathrm{E}(W_t)=0$$ \[因為平賭過程的期望值必為常數]
> 3. $$\mathrm{E}(W_t-W_s)^2 = t-s, ~ s \leq t$$。
> 4. $$W_t$$的樣本路徑連續。

雖然布朗運動和Weiner過程第2、3點定義不同，但兩者為等價定義，因此Weinier過程為標準布朗運動的另一種定義法。

### 布朗運動

> 1. $$B_0=0$$
> 2. $$B_t-B_s \sim N(0, \sigma^2 (t-s))$$
> 3. $$\forall t>0, B_t \sim N(0, \sigma^2 t)$$
> 4. $$B(t)$$為時間的連續的函數



![黑線為布朗運動的實現值，也稱樣本路徑(sample path)](../../.gitbook/assets/diffusion-min.png)



### 布朗運動的定數轉換

> \[scaling property] $$a>0$$, $$a\cdot W(\frac{t}{a^2})$$是布朗運動。

* $$\because \mathrm{E}(a W(\frac{t}{a^2})) = a\mathrm{E}(W(\frac{t}{a^2})) = a \mathrm{E}(W(\frac{t}{a^2}) - W(0))=0, ~W(0)=0$$
* $$\mathrm{Var} (aW(\frac{t}{a^2}))=a^2 \mathrm{Var}(W(\frac{t}{a^2}) - W_0)= a^2 \frac{t}{a^2} = t$$
* 因此$$aW(\frac{t}{a^2}) \sim N(0, t)$$，且其它三個條件均符合布朗運動，因此為布朗運動。(QED)

> \[time inversion] $$t\cdot W(\frac{1}{t})$$是布朗運動。

* $$\mathrm{E}(tW(\frac{1}{t})) = t \mathrm{E}(W(\frac{1}{t})- W(0)) = 0$$
* $$\mathrm{Var} (t W (\frac{1}{t})) = t^2 \mathrm{Var} (W(\frac{1}{t}) - W(0))= t^2 \frac{1}{t}= t$$
* 因此$$tW(\frac{1}{t}) \sim N(0, t)$$，且其它三個條件均符合布朗運動，因此為布朗運動。(QED)

> \[time homogeneity] $$W(t+h) - W(t), ~ t \geq 0$$是布朗運動。



