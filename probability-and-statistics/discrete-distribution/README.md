# 離散分佈

## 資料類型

數據類型（統計學裡也叫隨機變數）有兩種。**離散與連續資料**。

離散資料就是資料的取值是不連續的。例如擲硬幣就是一個典型的離散數據，因為拋硬幣的就2種數值（正面或反面）。

連續資料能取任意的數值。例如時間就是一個典型的連續數據1.25分鐘、1.251分鐘，1.2512分鐘，它能無限分割。

資料在統計圖中的形狀，叫做它的**分佈（distribution）**。

## 二項式分佈（bionomial distribution）

* 當遇到發生次數固定的事件，而感興趣的是事件成功（或）的次數，那麼就可以用二項分佈的公式快速計算出機率來。
* 假設事件次數$$N$$，令每一次成功的機率都是相等的，成功的機率用$$p$$表示。目標是算出$$N$$次事件中，成功$$k$$次的機率。
* 記為$$X \sim B(N, p)$$。

負二項分佈(Negative binomial distribution)


「負二項式分佈」與「二項分佈」的區別在於：

* 二項分佈是固定試驗總次數$$N$$的獨立試驗中，成功次數$$k$$的機率分佈；
* 負二項分布是所有到成功$$r$$次時即終止的獨立試驗中，失敗次數$$k$$的機率分佈。

### 分佈與統計量

* 隨機變數$$X \sim NB(r, p)$$
* 機率質量函數$$f(k | r,p)≡\mathrm{P}⁡(X=k)=\binom{k+r-1}{k}p^k(1-p)^r, ~ k=-0,1,2,\ldots$$
  * 已知一個事件在Bernouli試驗中每次的出現機率是$$p$$，在一連串試驗中，一件事件剛好在第$$r+k$$次試驗出現第$$r$$次成功的機率。
  * 已確定第$$r+k$$次試驗為成功，所以第1次至第$$r+k-1$$次試驗所有可能的情形為$$r−1$$次成功與$$k$$次失敗試驗的排列組合個數，共有$$\binom{r+k-1}{k}$$種組合。

## 幾何分佈（geometric distribution）

參數$$N,p$$意義同二次分佈，如果需要知道嘗試多次，能取得第一次成功的機率，則為幾何分佈，如：射擊，首次擊中目標時的次數。有兩種型式：

* 在伯努利試驗中，得到第一次成功所需要的試驗次數$$X$$。$$X$$的值域是$$\{ 1, 2, 3, \ldots \}$$。
  * 如果每次試驗的成功機率是$$p$$，那麼$$k$$次試驗中，第$$k$$次才得到成功的機率是$$\mathrm{P}(X=k)=(1-p)^{k-1}p$$, $$k=1,2,\cdots$$。
* 在得到第一次成功之前所經歷的失敗次數$$Y = X − 1$$。$$Y$$的值域是$$\{0,1,2,3,\ldots\}$$。
  * $$\mathrm{P}(Y=k)=(1-p)^k p$$, $$k=0,1,2,\ldots,$$。

實際使用中指的是哪一個取決於慣例和使用方便。這兩種分布不應該混淆。前一種形式（$$X$$的分布）經常被稱作shifted geometric distribution；但是，為了避免歧義，最好明確地說明取值範圍。

### 分佈與統計量

* 隨機變數 $$X \sim G(p)$$
* 期望值 $$\mathrm{E}(X)=\frac{1}{p}$$
* 變異數 $$\mathrm{Var}(X)=\frac{1-p}{p^2}$$

### 幾何分布具有非記憶性的性質（Memoryless Property）

如果一個隨機變數呈幾何分布，它的條件機率遵循：$$\displaystyle \mathrm{P}(T>s+t\;|\;T>t)= \mathrm{P}(T>s) ~ \forall s, t  \in \mathbb{N}.$$

## 超幾何分布（Hypergeometric distribution）

它描述了由有限個物件中抽出$$n$$個物件，成功抽出$$k$$次指定種類的物件的機率（抽出不放回 （without replacement））。

假設袋子中有$$N$$個球，其中有$$K$$個白球，$$N-K$$個非白球，則從袋中隨機取$$n$$個球，每次取後不放回，令隨機變數$$X$$為取中白球的個數。

### 分佈與統計量

* 隨機變數$$X \sim H(N,K,n)$$
* 機率質量函數為 $$\mathrm{P}(X=x |N, K, n) =\frac{\binom{K}{x} \binom{N-K}{n-x}}{\binom{N}{n}}, ~ \max\{0, n-N+k\} \leq x \leq \min \{n, k\}$$
  * &#x20;因為最多取$$n$$個球，且白球只有$$K$$個，所以x的上限為$$\min⁡\{n,K\}$$。
  * &#x20;取中非白球的數量$$n−x$$不能超過全部非白球數量$$N−K$$，即$$n−x \leq N−K \Rightarrow x \geq n−N+K$$。
* 期望值 $$\mathrm{E}(X) = \frac{nK}{N}$$
*   變異數 $$\mathrm{Var}(X) = \frac{nK(N-n)(N-K)}{N^2 (N-1)}$$





## 卜瓦松（泊松）分佈（Poisson distribution）

卜瓦松分佈適合於描述單位(秒、小時、天、週、月、季、年等)時間內隨機事件發生的次數（頻率）的機率分佈。

如某一服務設施在一定時間內受到的服務請求的次數、 電話交換機接到呼叫的次數、汽車站台的候客人數、機器出現的故障數、自然災害發生的次數、DNA序列的變異數、放射性原子核的衰變數、&#x20;雷射的光子數分佈等等。

卜瓦松分佈是二項分佈處理罕見事件的特殊情形，亦即樣本的數目趨向無窮大$$n \rightarrow \infty$$，事件發生的機率趨向無窮小$$p \rightarrow 0$$。在這情況下，二項分佈就可簡化成卜瓦松分佈。

卜瓦松分佈有一個很方便的特徵：它的<mark style="color:red;">平均值就是變異數</mark>，再開平方根就是標準差。

卜瓦松分佈的假設：

* 事件發生次數在任兩個不重疊的時段是相互獨立的。
* 在某一極小時段內，事件只發生一次的機率與該時段的長度呈某一比例關係。
* 在某一極小時段內，事件發生次數超過一次的機率值 （相對於相同時段內只發生一次的機率）非常小，所以可被忽略。（此假設即在極短的時間內，事件只會發生一次，而不會發生二次以上）。

假設單位時間之內事件平均發生次數為$$\lambda$$，那麼在這區域中事件發生的次數$$X$$就符合Poisson分配，記為$$X \sim P(\lambda)$$。

### 獨立的卜瓦松分佈隨機變數總和

> $$X\sim P(\lambda_1 )$$, $$Y \sim P(\lambda_2 )$$，且$$X,Y$$為獨立的隨機變數，則$$X+Y \sim P(\lambda_1+ \lambda_2 )$$

由動差生成函數證明。

### &#x20;卜瓦松分佈可由二項分佈逼近

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

