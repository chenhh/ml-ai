# 布朗運動(Brownian motion)

## 簡介

布朗運動是由Rober Brown(1828)首先觀察花粉分子存浮於液體內上下變動的一種物理過程。1990年時，Bachellier在他的博士論文中，將布朗運動運用在股價變動的模型。在1923年，由N.Wiener{維納）研究布朗運動的數學理論，嚴謹定義存在性，它是標度隨機漫步（scaled random walk）的極限隨機過程。因此布朗運動也稱為維納過程。Paul Samuelson（1970年諾貝爾經濟學獎得主）在1969年引入布朗運動研究財務經濟學的模型。

## 標準布朗運動

> 一個連續的隨機過程$$\{ W(t), 0 \leq t <T \}$$，在時間$$[0,T)$$稱為標準布朗運動（standard Brownian motion）必須滿足以下四個條件：
>
> 1. $$W(0)=0$$，在起始點$$t=0$$時，其值為0。
> 2. 獨立增量，即在不相交的區間之下，其相互的增量是獨立的。
>    * 令$$0 \leq t_1  <t_2 <\ldots, t_n =T$$，增量為隨機變數$$W(t_1)-W(t_0), W(t_2)-W(t_1), \ldots, W(t_n)-W(t_{n-1})$$是獨立的（相關係數為0）。
>    *
>
>        獨立增量指每一步的變化量彼此獨立，因此上一步與下一步無關，即$$\mathrm{P}(W(t_i) -W(t_{i-1}) |W(t_{1}) - W(t_{0}) , \ldots, W(t_{i-1}) - W(t_{i-2})) = \mathrm{P}(W(t_i) -W(t_{i-1}) )$$
> 3. 每一個隨機變數都是常態分佈，$$W(t_i) - W(t_{i-h}) \sim N(0, h)$$。
> 4. 在機率空間$$(\Omega, \mathcal{F}, \mathrm{P})$$中，$$W(t)$$是時間的連續函數。

> 第2點可弱化為獨立於區間$$[i, i+h)$$起始點$$i$$的布朗運動，$$W(t_{i+h }) - W(t_i) \sim N(0, h)$$ 。

* 布朗運動為連續的函數，但處處（每一點）均不可微分。
* 由定義得在時間$$t$$，$$W(t) - W(0) \sim N(0, t)$$，因此$$W(t) \sim N(0,t)$$。

### 布朗運動

> 1. $$B(0)=0$$
> 2. $$B(t)-B(s) \sim N(0, \sigma^2 (t-s))$$
> 3. $$\forall t>0, B(t) \sim N(0, \sigma^2 t)$$
> 4. $$B(t)$$為時間的連續的函數

* $$\{B(t)\}$$在變異數$$\sigma^2=1$$時為標準布朗運動$$\{W(t)\}$$



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



