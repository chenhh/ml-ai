---
description: RC, SPA, MCS檢定
---

# 真實性檢定(Reality Check Test)

![RC檢定相關論文](../../.gitbook/assets/rc\_spa\_mcs-min.png)

## 簡介

技術分析在台指期貨市場中做空頭比做多頭有效。做多頭交易時，在樣本內有效的交易規則，在樣本外不一定持續有效。而在樣本內做空頭交易時，可顯著擊敗基準模型的最佳交易規則，在樣本外一樣可以擊敗基準模型。

在相對年輕的市場，技術分析並沒有比較有效。

SPA 檢定可用過去的研究做為基礎，並不需要一開始就運用大量的交易規則來檢驗。在尋找最佳交易規則時，可運用過去的研究為基礎，以過去的最佳交易規則與新研究的交易規則比較即可，排除掉過去表現不好的交易規則，並不須要一開始即採用大量的交易規則來檢驗。

在採用 SPA檢定時，若增加規則，不會造成 p 值大幅的增加。這是因為 SPA檢定比RC檢定更容易排除較差的交易規則。

若在小範圍的交易規則中已找到最佳交易規則，加入更多的交易規則還是會使 p 值慢慢增加。所以在檢驗前交易規則的挑選非常重要。就算被檢驗的交易規則數量較少，若其中已包含了最佳交易規則，則加入其它較差的規則，p 值雖然變化不大，但也會微幅增加。

#### 報酬率分佈

常用的假設報酬分佈主要有：

1. 常態分佈。
2. t分佈。
3. 廣義誤差分佈(general error distribution, GED)。
4. 有偏t分佈。

而實證結果中，報酬分佈具有厚尾(fat-tail)。

#### 損失函數

White的研究表明，基於樣本外預測結果的計量模型判定結論，比基於樣本內預測結果的模型判定更加可靠，也更具有實用性；

但是評價分佈有多種損失函數，如平均絕對誤差(mean absolute error)、平均誤差平方(mean square error)等，沒有一致的共識。

同時Hansen等的研究也表明，基於單一樣本的單一損失函數判斷法，往往會因為數據樣本中的少數奇異點，而嚴重影響損失函數的計算結果，從而導致對不同分布優劣的錯誤判斷。



## 資料窺探的偏差(data snooping bias)

當一個給定的資料集被多次用於推理或模型選擇時，就會發生資料窺探。即所獲得的任何令人滿意的結果可能僅僅是由於運氣好，而不是由於產生結果的方法更好。

由於金融資料難以重複實驗的侷限性，個別的研究者通常利用相同的資料進行研究，卻忽略了將這種重複利用相同資料進行研究，所產生對資料的過度推論或是推論錯誤，稱為資料窺探(data snopping)問題。當模型(基金、股票或交易策略或是預測模型)數目眾多時，因資料窺探而產生的偏誤會更加嚴重。

Brock、Lakonishok and LeBaron (1992)發表「<mark style="color:blue;">Simple technical trading rules and the stochastic properties of stock returns</mark>」這篇文章後，有關於技術分析的文章開始廣泛的被主流期刊所接受。金融市場上的確存在著 一些弱式效率市場無法解釋的現象，因此以效率市場來論斷技術分析無效還是無法平息爭議。過去文獻對技術分析可獲得超額報酬的結果,常有「靠運氣」的批評，而其中最嚴重的，乃是資料探勘(Data-Snooping) 的問題。

在金融議題的研究上常會出現這方面的問題,即如果持續使用同 一組樣本,會產生資料探勘的問題。過去的研究要解決資料探勘的問題主要採用兩種方法:

1. 採用不同但是可比較的資料樣本測試一個模型，以避免重複使用相同的資料樣本。但問題是金融市場很少有相似 且可互相比較的商品。另一種作法是將一長期的樣本拆開成為幾個不同的子期間樣本，然後再測試相同模型在不同子期間的成果。。但如將其拆開來比 較,其分割的時點就是一大問題,因為沒有客觀的切割標準,這樣做恐 怕會有「主觀」或「武斷」的問題。
2. 利用Bonferroni Inequality來比較所有可能的模型，並正確的控制測試的規模(即型 I 誤差)。問題是在技術分析的檢驗中，因為技術分析的方法太多了，所以通常會檢驗很多的模型，如此這方法將會變的無法使用。

## 真實性檢定(reality check test)

White’s RC 是將所有的模型視為一個集合，評價這個集合在每次拔靴(自舉)樣本中表現最好的模型之績效分佈，用來檢定模型的有效性。

RC檢定必須要有一個基準模型，假設有$$m$$個要和基準模型比較的模型，且有$$n$$期的資料，則第$$i$$個模型在第$$t$$期和基準模型的輸出值的差值為$$d_{it}$$，而第$$i$$個模型和基準模型的平均差值為$$\overline{d}_i$$。

<mark style="color:red;">RC檢定的虛無假設為沒有任何一個比較模型表現比基準模型好，因此所有模型的差值平均值應小於等於0</mark>。

![](../../.gitbook/assets/RC\_null-min.png)

## SPA(Superior Predictive Ability)檢定

White’s RC 有兩個問題：

1. 平均報酬並沒有標準化。
2. RC 是根據最不利構形(Least Favorable Configuration)為基礎，故交易規則的期望報酬率都等於基準模型的報酬率。因此當比較差的交易規則包含在裡面時，White’s RC 所檢驗出來的結果反而更差。也就是說，雖然所有檢定的交易規則中有少數可以擊敗基準模型，但因為加 入了過多不具解釋力的交易規則,使得 White’s RC 的臨界值上升，p值跟著變大，這也使得交易規則和基準模型績效相同的虛無假設被拒絕的機率降低。

而SPA將統計量正規化(檢定統計量考慮標準差)後解決了這個問題，故截至目前為止是用來檢定技術分析(交易策略)是否有效的首要工具。

## Stepwise-RC & Stepwise-SPA 檢定

Step-RC 檢定法可以透過多重階段，逐步找出所有顯著優於比較基準的模型。 然而Step-RC 檢定法的基礎是 RC 檢定法，所以其檢定力在各階段同樣容易受到較差模型影響。

Hsu et al. 因此提出了 Step-SPA 檢定法，將各階段的檢定以 SPA 檢定法的方式加以調整。他們的數學證明與模擬結果均顯示，Step-SPA 檢定法可以增加 Step-RC 的檢定力。

## MCS檢定

許多應用中，通常不會產生一個明顯優於其它所有競爭者的單一模型，因為資訊量不夠大，無法對這個問題給出明確的答案。

MCS檢定程序

* 確定模型集合，內有競爭模型與最佳模型。
* 最佳的指標是以用戶指定的標准來定義的。
* MCS產生一個模型信賴區間集合，包含具有給定信賴區間度量的最佳模型們。

## RC檢定基本框架

從第$$R$$期至第$$T$$期(共$$n$$期，因此$$T=R+n-1$$)做預測，每期預測未來$$\tau$$期的結果。(即第$$R$$期預測第$$R+\tau$$期之值，第$$R+1$$期預測第$$R+1+\tau$$之值，以此類推第$$T$$期預測第$$T+\tau$$期之值)。

* 在第$$R$$期時，使用第$$1 \sim R$$期的資料算出參數$$\hat{\beta}_R$$。
* 在第$$R+1$$期時，使用第$$1 \sim R+1$$期的資料算出參數$$\hat{\beta}_{R+1}$$。
* 在第$$T$$期時，使用第$$1 \sim T$$期的資料算出參數$$\hat{\beta}_T$$。

假設隨機向量$$\mathbf{Z}=(\mathbf{Y, X})$$由應變向量$$\mathbf{Y}$$與自變向量$$\mathbf{X}$$所組成。$$\mathbf{Z}_t$$為第$$t$$期的隨機向量(資料為隨機向量的觀測值)。

假設檢定是計算$$l \times 1$$維的期望向量$$\mathrm{E}(\mathbf{f^{*}})$$，其中第$$k$$個函數$$\mathbf{f^{*}}_k \equiv f_k(\mathbf{Z, \beta^{*}})$$，$$\beta^{*} = \mathrm{plim} \hat{\beta}_T$$ 表示$$\hat{\beta}_t$$機率收斂至$$\beta^{*}$$。注意此處$$l$$個函數(模型)使用相同的參數$$\mathbf{Z}$$與$$\beta^{*}$$，只有內部結構不同而已。

更準確的說，是檢定在$$l \times 1$$維的統計量 $$\displaystyle \overline{f} = \frac{1}{n} \sum_{t=R}^T \hat{f}_{t+\tau}$$，其中$$\hat{f}_{t+\tau} = f(\mathbf{Z}_{t+\tau}, \hat{\beta}_t)$$，且觀察資料是由$$\{ \mathbf{Z}_t \}$$，為定態[α](https://tw.piliapp.com/symbols/alpha/)混合([α](https://tw.piliapp.com/symbols/alpha/)-mixing)序列\[鄰近的隨機變數有相關性，但隨著$$n$$變大則逐漸獨立或不相關]且有和$$\mathbf{Z}$$(在時間$$t$$)相同邊際分佈所產生。

給定選定的函數(的差值)$$f_1,f_2,\dots, f_l$$，<mark style="color:red;">虛無假設</mark>$$H_0: \mathrm{E}(f^{*}) \leq 0$$<mark style="color:red;">表示沒有函數的預測表現(性能)比基準模型好</mark>。(<mark style="color:red;">注意此處的</mark>$$f_k$$<mark style="color:red;">不是函數之值，而是函數與基準模型預測的差值</mark>)

West(1996)使用$$\beta^{*}$$建構假設檢定。但是對於有限樣本來說，$$\beta^{*}$$未必是最相關的參數。反之估計參數$$\hat{\beta}_t$$與建構預測函數(模型)直接相關。因此替代的方法為$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(\overline{f}) \leq 0$$即$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(\overline{f} ~|~ \mathbf{Z_1, \dots, Z_R}) \leq 0$$或者 $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(f_{t+\tau} ~|~ \mathbf{Z_1, \dots, Z_t}) \leq 0$$。

#### 範例：MSE

令$$\tau=1$$(預測下一期之值)以及$$l=1$$(只有一個預測函數)

檢驗一組特定變數在均方誤差(MSE, 越小越好)方面是否具有優於基準回歸模型的預測能力。

$$\hat{f}_{t+1}=-(y_{t+1} - X^{\top}_{1,t+1} \hat{\beta}_{1,t})^2+(y_{t+1} - X^{\top}_{0,t+1} \hat{\beta}_{0,t})^2$$

* $$y_{t+1} \in \mathbb{R}$$為應變數。
* $$\hat{\beta}_{1,t}$$是模型1使用OLS方法依據$$\{ (y_s, X_{1,s}), ~s=1,2,\dots, t\}$$算出的估計參數。與給定的參數向量$$X^{\top}_{1,t+1}$$內積可得$$t+1$$期的預測值$$\hat{y}_{t+1} \equiv X^{\top}{1,t+1} \hat{\beta}{1,t}$$
* $$\hat{\beta}_{0,t}$$是模型0(基準模型)使用OLS方法依據$$\{ (y_s, X_{0,s}), ~s=1,2,\dots, t\}$$算出的估計參數。
* 此處$$\hat{\beta}_t=\begin{bmatrix} \beta_{0,t}^\top \\ \beta_{1,t}^\top \end{bmatrix}$$，注意模型1與模型0不可為巢狀模型(nested model)。

#### 範例：交易策略

$$\hat{f}_{t+1} = \log(1+y_{t+1} S_1(X_{1, t+1}, \beta_1^{*})) - \log(1+y_{t+1} S_0(X_{0, t+1}, \beta_0^{*}))$$

* $$y_{t+1}$$為資產時間$$t+1$$的報酬，取$$\log$$表示連續報酬(continuous return)。
* $$S_0, S_1$$為訊號函數，其值域為$$\{-1, 0, 1\}$$，-1表示放空(short)，0表示不動作(neutral)，1表示買進(long)。其分別使用$$X_{0,t+1}, \beta_0^{*}$$與$$X_{1, t+1}, \beta_1^{*}$$做為參數求值。
* $$S_0=1, ~\forall t$$表示買進持有(buy-and-hold)策略。

#### 範例：MLE

$$\hat{f}_{t+1} = \log L_1(y_{t+1}, X_{1, t+1}, \hat{\beta}_{1,t}) - \log L_0(y_{t+1}, X_{0, t+1}, \hat{\beta}_{0,t})$$

不僅在虛無假設$$\mathrm{E}(f^{*}) \leq 0$$下其它模型沒有比基準模型有更好的預測能力，且動差函數可做做為篩選模型的準則。即將$$k=1,2,\dots, l$$個模型，，在時間$$t+1$$時，每個模型獨立和基準模型比較，可得$$l$$個差值$$\hat{f}_{k, t+1}, k=1,2,\dots, l$$。

如果表現最佳的模型之值仍然比基準模型差時，則可判定其它模型沒有比基準模型有更好的預測能力；因此虛無假設為$$\displaystyle H_0: \max_{k=1,2,\dots, l} \mathrm{E}(f_k^{*}) \leq 0$$ (多重假設檢定)，反之對立假設為至少有一個模型表現比基準模型好。

上述的方法，也可使用AIC(Akake Information Criterion)方法控制變數的數量，只要將變數的數量計算為預測損失的一部分即可。

我們的目標是一種不依賴於界值（如 Bonferroni 或其改進），而是直接提供（至少在漸近線上）適當 $$p$$ 值的方法。

### 理論基礎

只要經過適當標准化的$$\overline{f}$$具有連續的極限分布，我們就能提供上述的假設檢定方法。

West(1996)的論文中，Theorem 4.1給定了正規條件可保證分佈收斂：

$$
\sqrt{n} (\overline{f} - \mathrm{E}(f^{*})) \Rightarrow N(0, \Omega) \text{ as } T \rightarrow \infty
$$

且變異數矩陣$$\Omega \in \mathbb{R}^{l \times l}$$如下：

$$
\displaystyle \Omega = \lim_{T \rightarrow \infty} \mathrm{Var} \left[ \frac{1}{\sqrt{n}} \sum_{t=R}^T f(\mathbf{Z}_{t+\tau}, \beta^{*}) \right]
$$

其中 $$F = \equiv \mathrm{E}\left[ \frac{\partial}{\partial \beta} f(\mathbf{Z}, \beta^{*})\right] =0$$ 或 $$\frac{n}{R} \rightarrow 0$$ 當$$T \rightarrow \infty$$。

當上述條件不成立時，West論文中的Theorem 4.1(b)仍然可以得到相同的結論，但是$$\Omega$$的形式更複雜。

從上述理論中，West得到的標準漸近卡方統計量$$n \overline{f}^\top \hat{\Omega}^{-1}\overline{f}$$為虛無假設$$\mathrm{E}(f^{*}) = 0$$的統計量。 其中$$\hat{\Omega}$$ 為$$\Omega$$的一致估計量。

而我們感興趣的是虛無假設$$\mathrm{E}(f^{*}) \leq 0$$, 可得出基於$$\displaystyle \max_{k=1,\dots, l} \overline{f}_k$$的檢定。

可檢定$$\mathrm{E}(f^{*}) =0$$的方法可直接用於我們感興趣的虛無假設。為了簡潔起來，以下限制檢定為$$\mathrm{E}(f^{*}) \leq 0$$。

我們的第一個結果表明，當存在最佳預測模型時，使用最佳預測模型選擇標準選擇模型確實可以識別出最佳模型。

### Proposition 2.1

> 假設 $$\sqrt{n} (\overline{f} - \mathrm{E}(f^{*})) \Rightarrow N(0, \Omega)$$ 且 $$\Omega$$為正半定矩陣(Appendix的假設A成立)，則：
>
> 1. 若$$\mathrm{E}(f^{*}) >0$$ for some $$1 \leq k \leq l$$, 則$$\forall 0 \leq c < \mathrm{E}(f_k^{*})$$, $$\mathrm{P}(\overline{f}_k <c ) \rightarrow 1 \text{ as } T \rightarrow > \infty$$。
> 2. 若$$l > 1$$ 且$$\mathrm{E}(f_1^{*}) >\mathrm{E}(f_k^{*}), \forall k=2,\dots, l$$, 則$$\mathrm{P}(\overline{f}_1 > \overline{f}_k, ~ \forall k=2,\dots, l) \rightarrow 1$$ as $$T \rightarrow \infty$$。

第1部分指出，如果某個模型（最佳模型）優於基準模型，那么最終會得到正值的估計相對績效(即最佳模型的損失小於基準模型)。

當 $$l =1$$ 時，這一結果類似於 Rivers 和 Vuong（1991）在非預測環境下的模型選擇結果。當 ##l \geq 1\$$ 時，它也類似於 Kloek（1972 年）的模型選擇結果。

第2部分說，最佳模型最終具有相對於基準的最佳估計效能，其機率接近1。

對預測模型選擇標準的虛無假設$$H_0$$檢驗來自以下命題。

### Proposition 2.2

> 假設$$\sqrt{n} (\overline{f} - \mathrm{E}(f^{*})) \Rightarrow N(0, \Omega)$$ 且 $$\Omega$$為正半定矩陣(Appendix的假設A成立)，則當$$T \rightarrow \infty$$，可得：
>
> 1. $$\displaystyle \max_{k=1,2,\dots, l} \sqrt{n}\left\{ \overline{f}_k - \mathrm{E}(f_k^{*})      \right\} \Rightarrow  V_l \equiv \max_{k=1,2,\dots, l} {\mathcal{Z}_k}$$
> 2. $$\displaystyle \min_{k=1,2,\dots, l} \sqrt{n} \left\{ \overline{f}_k - \mathrm{E}(f_k^{*})\right\} \Rightarrow  W_l \equiv \min_{k=1,2,\dots, l} {\mathcal{Z}_k}$$
>
> 其中 $$\mathcal{Z}=[\mathcal{Z}_1, \dots, \mathcal{Z}_l]^\top \sim N(0, \Omega)$$為$$l \times 1$$維的向量。

鑒於漸近常態分佈，無論虛無假設還是對立假設為真，結論都成立。

因此使用這樣一個事實來進行虛無假設檢定，即虛無假設中，相對於對立假設的最不利條件(least favorite configuration)為$$\mathrm{E}(f_k^{*})=0,~ \forall k$$。即所有的模型表現和基準模型一樣好，不存在表現特別好的模型。

因此$$\displaystyle \overline{V}_l \equiv \max_{k=1,\dots, l} \sqrt{n} \overline{f}_k$$在最不利條件下，當$$T \rightarrow \infty$$時可得漸近$$p$$值。通過以這種方式執行處無假設，我們以類似於$$\max_l (f_k^{*})$$的信賴區間反轉的方式獲得檢定的臨界值。此稱方式計算$$H_0: E(f^{*}) \leq 0$$的$$p$$值稱為真實性檢定(reality check test)。

實現真實性檢定的挑戰是虛無假設的分佈，即一般情況下相關常態向量的極限值，是未知的。真實性檢定的分析方法是不可行的。

然而，至少有兩種方法可以獲得期望的p值。

#### Monte Carlo Reality Check

首先是蒙特卡羅模擬求$$\Omega$$的一致估計式$$\hat{\Omega}$$。可從$$N(0, \hat{\Omega})$$中，以區塊自舉法(block bootstrap method)抽出大量樣本得樣本分佈後求p值。

#### Bootstrap Reality Check

## 參考資料

* \[Dieb95] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," Journal of Business & economic statistics, vol. 20, 1995.
* <mark style="color:red;">\[West96] K. D. West, "Asymptotic inference about predictive ability, " Econometrica: Journal of the Econometric Society, pp. 1067-1084, 1996.</mark>
* \[Whit00] Halbert White, “A REALITY CHECK FOR DATA SNOOPING,” Econometrica, Vol. 68, No. 5, pp. 1097-1126, 2000
* \[Roma05] Romano, J. P. and M. Wolf,. “Stepwise multiple testing as formalized data snooping,” Econometrica, Vol . 73, pp. 1237–1282, 2005.
* \[Hans05] P.R. Hansen, “A test for superior predictive ability, ” Journal of Business and Economic Statistics, Vol. 23, No. 4, pp. 365-380, 2005.
* \[Hans11] P. R. Hansen, A. Lunde, and J. M. Nason, "The Model Confidence Set," Econometrica, vol. 79, pp. 453-497, 2011.
* \[Hsu10] Po-Hsuan Hsu , Yu-Chin Hsub, Chung-Ming Kuan, “Testing the predictive ability of technical analysis using a new stepwise test without data snooping bias,” Journal of Empirical Finance, Vol. 17, pp. 471-484, 2010.
* \[Clar12] T. E. Clark and M. W. McCracken, "Reality checks and comparisons of nested predictive models," Journal of Business & Economic Statistics, vol. 30, 2012.
* \[Mari12] R. S. Mariano and D. Preve, "Statistical tests for multiple forecast comparison," Journal of Econometrics, vol. 169, pp. 123-130, 7, 2012.
