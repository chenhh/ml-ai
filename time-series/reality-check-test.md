---
description: RC, SPA, MCS檢定
---

# 真實性檢定(Reality Check Test)

![RC檢定相關論文](../.gitbook/assets/rc\_spa\_mcs-min.png)

## 資料窺探的偏差(data snooping bias)

當一個給定的資料集被多次用於推理或模型選擇時，就會發生資料窺探。即所獲得的任何令人滿意的結果可能僅僅是由於運氣好，而不是由於產生結果的方法更好。

由於金融資料難以重複實驗的侷限性，個別的研究者通常利用相同的資料進行研究，卻忽略了將這種重複利用相同資料進行研究，所產生對資料的過度推論或是推論錯誤，稱為資料窺探(data snopping)問題。當模型(基金、股票或交易策略或是預測模型)數目眾多時，因資料窺探而產生的偏誤會更加嚴重。

## 真實性檢定(reality check test)

RC檢定必須要有一個基準模型，假設有$$m$$個要和基準模型比較的模型，且有$$n$$期的資料，則第$$i$$個模型在第$$t$$期和基準模型的輸出值的差值為$$d_{it}$$，而第$$i$$個模型和基準模型的平均差值為$$\overline{d}_i$$。

<mark style="color:red;">RC檢定的虛無假設為沒有任何一個比較模型表現比基準模型好，因此所有模型的差值平均值應小於等於0</mark>。

![](../.gitbook/assets/RC\_null-min.png)



## SPA(Superior Predictive Ability)檢定

因RC的檢定效力在所比較的規則集合中，若有過多沒有解釋（預測）能力的規則被加入，會大大降低檢定效力。而SPA將統計量正規化後解決了這個問題，故截至目前為止是用來檢定技術分析(交易策略)是否有效的首要工具。

## Stepwise-RC & Stepwise-SPA 檢定

Step-RC 檢定法可以透過多重階段，逐步找出所有顯著優於比較基準的模型。 然而Step-RC 檢定法的基礎是 RC 檢定法，所以其檢定力在各階段同樣容易受到較差模型影響。&#x20;

Hsu et al. 因此提出了 Step-SPA 檢定法，將各階段的檢定以 SPA 檢定法的方式加以調整。他們的數學證明與模擬結果均顯示，Step-SPA 檢定法可以增加 Step-RC 的檢定力。

## MCS檢定

許多應用中，通常不會產生一個明顯優於其它所有競爭者的單一模型，因為資訊量不夠大，無法對這個問題給出明確的答案。

MCS檢定程序

* &#x20;確定模型集合，內有競爭模型與最佳模型。
* 最佳的指標是以用戶指定的標准來定義的。
* MCS產生一個模型信賴區間集合，包含具有給定信賴區間度量的最佳模型們。

## RC檢定基本框架

從第$$R$$期至第$$T$$期(共$$n$$期，因此$$T=R+n-1$$)做預測，每期預測未來$$\tau$$期的結果。(即第$$R$$期預測第$$R+\tau$$期之值，第$$R+1$$期預測第$$R+1+\tau$$之值，以此類推第$$T$$期預測第$$T+\tau$$期之值)。

* 在第$$R$$期時，使用第$$1 \sim R$$期的資料算出參數$$\hat{\beta}_R$$。
* 在第$$R+1$$期時，使用第$$1 \sim R+1$$期的資料算出參數$$\hat{\beta}_{R+1}$$。
* 在第$$T$$期時，使用第$$1 \sim T$$期的資料算出參數$$\hat{\beta}_T$$。

假設隨機向量$$\mathbf{Z}=(\mathbf{Y, X})$$由應變向量$$\mathbf{Y}$$與自變向量$$\mathbf{X}$$所組成。$$\mathbf{Z}_t$$為第$$t$$期的隨機向量(資料為隨機向量的觀測值)。

假設檢定是計算$$l \times 1$$維的期望向量$$\mathrm{E}(\mathbf{f^{*}})$$，其中第$$k$$個函數$$\mathbf{f^{*}}_k \equiv f_k(\mathbf{Z, \beta^{*}})$$，$$\beta^{*} = \mathrm{plim} \hat{\beta}_T$$ 表示$$\hat{\beta}_t$$機率收斂至$$\beta^{*}$$。注意此處$$l$$個函數(模型)使用相同的參數$$\mathbf{Z}$$與$$\beta^{*}$$，只有內部結構不同而已。

&#x20;更準確的說，是檢定在$$l \times 1$$維的統計量 $$\displaystyle \overline{f} = \frac{1}{n} \sum_{t=R}^T \hat{f}_{t+\tau}$$，其中$$\hat{f}_{t+\tau} = f(\mathbf{Z}_{t+\tau}, \hat{\beta}_t)$$，且觀察資料是由$$\{ \mathbf{Z}_t \}$$，為定態[α](https://tw.piliapp.com/symbols/alpha/)混合([α](https://tw.piliapp.com/symbols/alpha/)-mixing)序列\[鄰近的隨機變數有相關性，但隨著$$n$$變大則逐漸獨立或不相關]且有和$$\mathbf{Z}$$(在時間$$t$$)相同邊際分佈所產生。

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
\sqrt{n} (\overline{f} - \mathrm{E}(f^{*})) \Rightarrow N(0, \Omega) \text{ as } T \rightarrow 
\infty
$$

且變異數矩陣$$\Omega \in \mathbb{R}^{l \times l}$$如下：

$$
\displaystyle 
\Omega = \lim_{T \rightarrow \infty} \mathrm{Var} \left[
\frac{1}{\sqrt{n}} \sum_{t=R}^T f(\mathbf{Z}_{t+\tau}, \beta^{*})
\right]
$$
其中 $$ F = \equiv \mathrm{E}\left[ \frac{\partial}{\partial \beta} f(\mathbf{Z}, \beta^{*})\right]
=0$$ 或 $$ \frac{n}{R} \rightarrow 0$$ 當$$ T \rightarrow \infty$$。

當上述條件不成立時，West論文中的Theorem 4.1(b)仍然可以得到相同的結論，但是$$\Omega$$的形式更複雜。

從上述理論中，West得到的標準漸近卡方統計量$$ n \overline{f}^\top \hat{\Omega}^{-1}\overline{f} $$為虛無假設$$\mathrm{E}(f^{*}) = 0$$的統計量。
其中$$\hat{\Omega}$$ 為$$\Omega$$的一致估計量。

而我們感興趣的是虛無假設$$\mathrm{E}(f^{*}) \leq 0$$, 可得出基於$$\displaystyle \max_{k=1,\dots, l} \overline{f}_k$$的檢定。

可檢定$$\mathrm{E}(f^{*}) =0$$的方法可直接用於我們感興趣的虛無假設。為了簡潔起來，以下限制檢定為$$\mathrm{E}(f^{*}) \leq 0$$。

我們的第一個結果表明，當存在最佳預測模型時，使用最佳預測模型選擇標準選擇模型確實可以識別出最佳模型。

### Proposition 2.1

> 假設 $$\sqrt{n} (\overline{f} - \mathrm{E}(f^{*})) \Rightarrow N(0, \Omega)$$
> 且 $$\Omega$$為正半定矩陣(Appendix的假設A成立)，則：
> 1. 若$$\mathrm{E}(f^{*}) >0$$ for some $$1 \leq k \leq l$$, 則$$\forall 0 \leq c < \mathrm{E}
     > (f_k^{*})$$, $$ \mathrm{P}(\overline{f}_k <c ) \rightarrow 1 \text{ as } T \rightarrow 
     > \infty$$。
> 2. 若$$l > 1$$ 且$$\mathrm{E}(f_1^{*}) >\mathrm{E}(f_k^{*}), \foralll k=2,\dots, l$$, 則$$\mathrm
     > {P}(\overline{f}_1 > \overline{f}_k, ~ \forall k=2,\dots, l) \rightarrow 1 \text{ as } T 
     > \rightarrow \infty$$。 

## 參考資料

* \[Dieb95] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," Journal of Business & economic statistics, vol. 20, 1995.&#x20;
* <mark style="color:red;"> \[West96] K. D. West, "Asymptotic inference about predictive ability,
" Econometrica: Journal of the Econometric Society, pp. 1067-1084, 1996. </mark>
* \[Whit00] Halbert White, “A REALITY CHECK FOR DATA SNOOPING,” Econometrica, Vol. 68, No. 5, pp. 1097-1126, 2000
* \[Roma05] Romano, J. P. and M. Wolf,. “Stepwise multiple testing as formalized data snooping,” Econometrica, Vol . 73, pp. 1237–1282, 2005.&#x20;
* \[Hans05] P.R. Hansen, “A test for superior predictive ability, ” Journal of Business and Economic Statistics, Vol. 23, No. 4, pp. 365-380, 2005.
* \[Hans11] P. R. Hansen, A. Lunde, and J. M. Nason, "The Model Confidence Set," Econometrica, vol. 79, pp. 453-497, 2011.
* \[Hsu10] Po-Hsuan Hsu , Yu-Chin Hsub, Chung-Ming Kuan, “Testing the predictive ability of technical analysis using a new stepwise test without data snooping bias,” Journal of Empirical Finance, Vol. 17, pp. 471-484, 2010.&#x20;
* \[Clar12] T. E. Clark and M. W. McCracken, "Reality checks and comparisons of nested predictive models," Journal of Business & Economic Statistics, vol. 30, 2012.&#x20;
* \[Mari12] R. S. Mariano and D. Preve, "Statistical tests for multiple forecast comparison," Journal of Econometrics, vol. 169, pp. 123-130, 7, 2012.

