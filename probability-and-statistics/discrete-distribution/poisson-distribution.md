---
description: 卜阿松分佈, Poisson distribution
---

# 泊松分佈

## 卜瓦松（泊松）分佈（Poisson distribution）

**泊松分佈**是一種用於描述在**固定時間(**(秒、小時、天、週、月、季、&#x5E74;**)或空間間隔(公分、公尺、公里)內**，以**恆定的平均速率**發生**獨立事件**的次數的離散機率分佈。

如某一服務設施在一定時間內受到的服務請求的次數、 電話交換機接到呼叫的次數、汽車站台的候客人數、機器出現的故障數、自然災害發生的次數、DNA序列的變異數、放射性原子核的衰變數、&#x20;雷射的光子數分佈等等。

<mark style="color:red;">泊松分佈發生兩次事件之間的時間間隔服從指數分佈</mark>。

泊松分佈通常適用於以下情況：

* **事件是隨機發生的。**
* **事件之間是相互獨立的。** 一個事件的發生不影響另一個事件發生的機率。
* **事件發生的平均速率**$$\lambda$$**在給定的間隔內是恆定的(非時變)。**
* **我們感興趣的是在一個固定的間隔（時間、空間等）內發生的事件次數。**

卜瓦松分佈的假設：

* 獨立增量性 (Independent Increments)：事件發生次數在任兩個不重疊的時段是相互獨立的。
* 平穩性 (Stationarity)：在某一極小時段內，事件只發生一次的機率與該時段的長度呈某一比例關係。
* 稀疏性 (Rarity)：在某一極小時段內，事件發生次數超過一次的機率值 （相對於相同時段內只發生一次的機率）非常小，所以可被忽略。（此假設即在極短的時間內，事件只會發生一次，而不會發生二次以上）。

卜瓦松分佈$$X \sim Poisson(\lambda)$$是二項分佈$$X \sim B(n,p)$$處理罕見事件的特殊情形，亦即樣本的數目趨向無窮大$$n \rightarrow \infty$$，事件發生的機率趨向無窮小$$p \rightarrow 0$$。在這情況下，二項分佈就可簡化成泊松分佈。

卜瓦松分佈有一個很方便的特徵：它的<mark style="color:red;">平均值就是變異數</mark>，再開平方根就是標準差。

### 估計參數方法

無先驗資訊時，直接使用樣本均值$$\bar{X}$$作為$$\lambda$$的估計。若資料量小或有歷史資訊，可嘗試貝氏方法。

| 方法         | 估計量公式                                                       | 適用場景           |
| ---------- | ----------------------------------------------------------- | -------------- |
| **最大似然估計** | $$\hat{\lambda}=\bar{X}$$                                   | 默認方法，無先驗資訊時使用  |
| **矩估計**    | $$\hat{\lambda}=\bar{X}$$                                   | 結果與MLE相同，理論驗證用 |
| **貝氏估計**   | $$\hat{\lambda}=\frac{\alpha + \sum_{i=1}^N X_i}{\beta+N}$$ | 有先驗知識時使用       |



## 泊松分佈定義

> 假設單位時間之內事件平均發生次數為$$\lambda$$，那麼在這區域中事件發生的次數$$X$$就符合Poisson分配，記為$$X \sim Poisson(\lambda)$$。
>
> 概率質量函數（PMF）為$$\mathrm{P}(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}, k=0,1,2,\dots,$$

* $$X$$：隨機變量，表示事件發生的次數（非負整數）。
* $$\lambda$$：分佈參數，表示單位時間或空間內事件的平均發生次數$$(\lambda > 0$$)。
* 均值$$\mathrm{E}(X)=\lambda$$。變異數$$\mathrm{Var}(X)=\lambda$$。
* <mark style="color:red;">泊松分佈的均值等於變異數，這是其獨特特徵</mark>。
* <mark style="color:red;">**泊松分佈發生兩次事件之間的時間間隔服從指數分佈**</mark>。由於泊松過程具有獨立增量性和平穩性，在第一次事件發生之後，等待下一個事件發生的時間的機率特性與從時間 0 開始等待第一個事件發生的機率特性相同。也就是說，過程「忘記」了之前發生了多少事件以及何時發生的。

### 獨立的泊松分佈隨機變數總和

> $$X\sim Poisson(\lambda_1 )$$, $$Y \sim Poisson(\lambda_2 )$$，且$$X,Y$$為獨立的隨機變數，則$$X+Y \sim Poisson(\lambda_1+ \lambda_2 )$$

由動差生成函數證明。

## <mark style="color:red;">泊松分佈機率質量函數可由二項分佈逼近</mark>

當一個事件，在單位時間內中可能發生的次數是$$\lambda$$ 。由假設可知經過時間$$\Delta t$$ ，該事件發生的期望次數是$$\mathrm{E} ( X )=\lambda \Delta t$$ 。&#x20;

若將這段時間$$T$$等分成$$n$$ 個時間段，當$$n \rightarrow \infty$$ 時，每個微小的時間段$$\Delta t = T/n$$內發生事件的機率約為$$\lambda \Delta t/n=\mu/n$$且發生多於一個事件的機率趨近於零。因此每個微小的時間段，可以視爲是一個Bernoulli實驗（事件發生或不發生）。

那麼這整段時間$$T$$ 內發生的事件可以視爲是一個二項分佈實驗，試驗次數$$N$$且試驗成功的機率為$$p=\mu/n$$。

* 若$$X \sim B(N,p)$$，則當$$N \rightarrow \infty$$ 且$$p \rightarrow 0$$時，  $$f_X(x| N,p) \rightarrow e^{-\lambda} \frac{\lambda^x}{x!}$$
* 即二項式分佈的隨機變數，在試驗次數$$N$$夠多且成功機率$$p$$夠小時（但$$Np < \infty$$），此隨機變數會近似於泊分佈。

$$n \rightarrow \infty$$​，在每個分割好的時間段內，事件發生的機率都是$$p=\frac{\lambda \Delta t}{n} = \mu/n$$。

$$\begin{aligned} \mathrm{P}(X=x) & =  \binom{n}{x} p^x (1-p)^{n-x} \\ 	& =  \binom{n}{x} (\frac{\mu}{n})^x (1-\frac{\mu}{n})^{n-x} \\ 	& =  \frac{n!}{x! (n-x)!} (\frac{\mu}{n})^x (1-\frac{\mu}{n})^{n-x} \\ 	& =  \frac{n!}{n^x (n-x)!} \frac{\mu ^x}{x!} (1-\frac{\mu}{n})^{n-x} \\  \end{aligned}$$

當 $$n \rightarrow \infty$$時且$$x << n$$​，可得

$$\frac{n!}{n^x (n-x)!} = \frac{n(n-1)\cdots(n-x+1) }{n^x} \rightarrow  1$$

所以$$(1-\frac{\mu}{n})^{n-x} \approx ((1-\frac{\mu}{n})^{n}) \rightarrow e^{- \mu}$$

因此$$\mathrm{P}(X=x) \rightarrow \frac{\mu^x}{x!}e^{-\mu}$$，其中$$\mu=\lambda t$$表示固定時間內的平均事件數。而在$$t=1$$(單位時間)$$\mu=\lambda$$ 為標準泊松分佈。



## 最大似然估計(MLE)參數估計

給定獨立同分佈泊松分佈的$$N$$個隨機變數$$X_1, \dots, X_N$$的樣本值$$x_1, \dots, x_n$$，希望得到從中推測出總體的泊松分佈參數$$\lambda$$的估計。

**對數似然函數(**&#x6C;og-likelihood function)

&#x20;$$\begin{aligned} \displaystyle l(\lambda|X) & =\log \bigg({\prod_{i=1}^N f(x_i | \lambda)} \bigg) \\ &=\sum_{i=1}^N \log \bigg(\frac{e^{- \lambda \lambda ^{x_i}}}{x_i !} \bigg) \\ &= -N \lambda + \bigg(\sum_{i=1}^N x_i\bigg) \log \lambda - \sum_{i=1}^N \log(x_i!) \end{aligned}$$

令$$\frac{\partial l}{\partial \lambda} = 0$$，得 $$-N + \bigg(\sum_{i=１}^N x_i\bigg) \frac{1}{\lambda}=0$$

所以 $$\hat{\lambda}_{MLE}= \frac{1}{N} \sum_{i=1}^N x_i$$。

<mark style="color:red;">即參數</mark>$$\lambda$$<mark style="color:red;">的最大似然估計是樣本均值</mark>$$\overline{X}$$。

## 動差參數估計（Method of Moments, MOM）

給定獨立同分佈泊松分佈的$$N$$個隨機變數$$X_1, \dots, X_N$$的樣本值$$x_1, \dots, x_n$$，希望得到從中推測出總體的泊松分佈參數$$\lambda$$的估計。

泊松分佈的理論均值：$$\mathrm{E}(X)=\lambda$$。

用樣本均值匹配理論均值：$$\overline{X}=\frac{1}{N}\sum_{i=1}^n x_i = \hat{\lambda}_{MOM}$$。

<mark style="color:red;">可得動差估計和最大似然估計的參數一致。</mark>

## 貝氏估計（Bayesian Estimation）

適用場景：當有先驗知識時，可結合先驗分佈更新估計。

泊松分佈的共軛先驗是 Gamma分佈$$Gamma(\alpha, \beta)$$，其機率密度函數為$$f(\lambda) = \frac{\beta^{\alpha}}{\Gamma(\alpha)} \lambda^{\alpha -1}e^{- \beta \lambda}$$。

給定隨機資料$$X_1, \dots, X_N$$後，後驗分佈為$$\lambda |X \sim Gamma(\alpha + \sum_{i=1}^N x_i, \beta +N)$$。

後驗均值估計：$$\hat{\lambda}_{Bayes} = \frac{\alpha + \sum_{i=1}^N X_i}{\beta+N}$$。

<mark style="color:red;">當</mark>$$\alpha \to 0, \beta \to 0$$<mark style="color:red;">時，（無資訊先驗）時，貝氏估計退化為MLE</mark>。

## 範例

電話呼叫：某呼叫中心每小時平均接到 5 通電話 (λ=5)，求某小時接到正好 3 通電話的機率。$$\mathrm{P}(X=4)=\frac{5^3 e^{-5}}{3!} \approx 0.1404$$。

交通事故：某路段每天平均發生 2 次事故 (λ=2)，求一天無事故的機率：$$\mathrm{P}(X=0)=\frac{2^0 e^{-2}}{0!}=e^{-2} \approx 0.1353$$。



