---
description: 卜阿松分佈, Poisson distribution
---

# 泊松分佈

## 卜瓦松（泊松）分佈（Poisson distribution）

卜瓦松分佈適合於描述單位(秒、小時、天、週、月、季、年等)時間內隨機事件發生的次數（頻率）的機率分佈。

如某一服務設施在一定時間內受到的服務請求的次數、 電話交換機接到呼叫的次數、汽車站台的候客人數、機器出現的故障數、自然災害發生的次數、DNA序列的變異數、放射性原子核的衰變數、&#x20;雷射的光子數分佈等等。

卜瓦松分佈$$X \sim P(\lambda)$$是二項分佈$$X \sim B(n,p)$$處理罕見事件的特殊情形，亦即樣本的數目趨向無窮大$$n \rightarrow \infty$$，事件發生的機率趨向無窮小$$p \rightarrow 0$$。在這情況下，二項分佈就可簡化成卜瓦松分佈。

卜瓦松分佈有一個很方便的特徵：它的<mark style="color:red;">平均值就是變異數</mark>，再開平方根就是標準差。

卜瓦松分佈的假設：

* 事件發生次數在任兩個不重疊的時段是相互獨立的。
* 在某一極小時段內，事件只發生一次的機率與該時段的長度呈某一比例關係。
* 在某一極小時段內，事件發生次數超過一次的機率值 （相對於相同時段內只發生一次的機率）非常小，所以可被忽略。（此假設即在極短的時間內，事件只會發生一次，而不會發生二次以上）。

假設單位時間之內事件平均發生次數為$$\lambda$$，那麼在這區域中事件發生的次數$$X$$就符合Poisson分配，記為$$X \sim P(\lambda)$$。

### 獨立的卜瓦松分佈隨機變數總和

> $$X\sim P(\lambda_1 )$$, $$Y \sim P(\lambda_2 )$$，且$$X,Y$$為獨立的隨機變數，則$$X+Y \sim P(\lambda_1+ \lambda_2 )$$

由動差生成函數證明。

### &#x20;<mark style="color:red;">卜瓦松分佈可由二項分佈逼近</mark>

當一個事件，在一段時間$$T$$ 中可能發生的次數是$$\lambda$$ 。那麼可以認爲，經過時間$$T$$ ，該事件發生的期望次數是$$\mathrm{E} ( X )=\lambda T$$ 。&#x20;

若將這段時間$$T$$等分成$$n$$ 個時間段，當$$n \rightarrow \infty$$ 時，每個微小的時間段內最多發生一次該事件。那麼每每個微小的時間段，可以視爲是一個Bernoulli實驗（事件發生或不發生），那麼這整段時間\
$$T$$ 內發生的事件可以視爲是一個二項分佈實驗。

* 若$$X \sim B(N,p)$$，則當$$N \rightarrow \infty$$ 且$$p \rightarrow 0$$時，  $$f_X(x| N,p) \rightarrow e^{-\lambda} \frac{\lambda^x}{x!}$$
* 即二項式分佈的隨機變數，在試驗次數$$N$$夠多且成功機率$$p$$夠小時（但$$Np < \infty$$），此隨機變數會近似於卜瓦松分佈。

$$n \rightarrow \infty$$​，$$n$$​為時間段。在每個分割好的時間段內，事件發生的機率都是$$p=\frac{\lambda T}{n}$$。

$$\begin{aligned} \mathrm{P}(X=x) & =  \binom{n}{x} p^x (1-p)^{n-x} \\ 	& =  \binom{n}{x} (\frac{\mu}{n})^x (1-\frac{\mu}{n})^{n-x} \\ 	& =  \frac{n!}{x! (n-x)!} (\frac{\mu}{n})^x (1-\frac{\mu}{n})^{n-x} \\ 	& =  \frac{n!}{x! (n-x)!} \frac{\mu ^x}{x!} (1-\frac{\mu}{n})^{n-x} \\  \end{aligned}$$

當 $$n \rightarrow \infty$$時且$$x << n$$​，可得

$$\frac{n!}{n^x (n-x)!} = \frac{n(n-1)\cdots(n-x+1) }{n^x} \rightarrow  1$$

所以$$(1-\frac{\mu}{n})^{n-x} \approx ((1-\frac{\mu}{n})^{n}) \rightarrow e^{- \mu}$$

因此$$\mathrm{P}(X=x) \rightarrow \frac{\mu^x}{x!}e^{-\mu}$$

​



### MLE參數估計

給定獨立同卜瓦松分佈的$$N$$個隨機樣本值，希望得到從中推測出總體的卜瓦松分佈參數$$\lambda$$的估計。

* log-likelihood function $$\begin{aligned} \displaystyle l(\lambda|X) & =\log \bigg({\prod_{i=1}^N f(x_i | \lambda)} \bigg) \\ &=\sum_{i=1}^N \log \bigg(\frac{e^{- \lambda \lambda ^{x_i}}}{x_i !} \bigg) \\ &= -N \lambda + \bigg(\sum_{i=1}^N x_i\bigg) \log \lambda - \sum_{i=1}^N \log(x_i!) \end{aligned}$$
* 令$$\frac{\partial l}{\partial \lambda} = 0$$，得 $$-N + \bigg(\sum_{i=１}^N x_i\bigg) \frac{1}{\lambda}=0$$
* 所以 $$\hat{\lambda}_{MLE}= \frac{1}{N} \sum_{i=1}^N x_i$$。



[https://wangcc.me/LSHTMlearningnote/poisson.html](https://wangcc.me/LSHTMlearningnote/poisson.html)
