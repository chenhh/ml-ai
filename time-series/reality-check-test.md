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

&#x20;更準確的說，是檢定在$$l \times 1$$維的統計量 $$\displaystyle \overline{f} = \frac{1}{n} \sum_{t=R}^T \hat{f}_{t+\tau}$$，其中$$\hat{f}_{t+\tau} = f(\mathbf{Z}_{t+\tau}, \hat{\beta}_t)$$，且觀察資料是由$$\{ \mathbf{Z}_t \}$$，為定態[α](https://tw.piliapp.com/symbols/alpha/)混合([α](https://tw.piliapp.com/symbols/alpha/)-mixing)序列且有和$$\mathbf{Z}$$(在時間$$t$$)相同邊際分佈所產生。

給定選定的函數(的差值)$$f_1,f_2,\dots, f_l$$，<mark style="color:red;">虛無假設</mark>$$H_0: \mathrm{E}(f^{*}) \leq 0$$<mark style="color:red;">表示沒有函數的預測表現(性能)比基準模型好</mark>。(<mark style="color:red;">注意此處的</mark>$$f_k$$<mark style="color:red;">不是函數之值，而是函數與基準模型預測的差值</mark>)

West(1996)使用$$\beta^{*}$$建構假設檢定。但是對於有限樣本來說，$$\beta^{*}$$未必是最相關的參數。反之估計參數$$\hat{\beta}_t$$與建構預測函數(模型)直接相關。因此替代的方法為$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(\overline{f}) \leq 0$$即$$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(\overline{f} ~|~ \mathbf{Z_1, \dots, Z_R}) \leq 0$$或者 $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(f_{t+\tau} ~|~ \mathbf{Z_1, \dots, Z_t}) \leq 0$$。

#### 範例：令$$\tau=1$$(預測下一期之值)以及$$l=1$$(只有一個預測函數)

檢驗一組特定變數在均方誤差方面是否具有優於基準回歸模型的預測能力。

$$\hat{f}_{t+1}=-(y_{t+1} - X^{\top}_{1,t+1} \hat{\beta}_{1,t})+(y_{t+1} - X^{\top}_{0,t+1} \hat{\beta}_{0,t})$$

* $$y_{t+1} \in \mathbb{R}$$為應變數。
* $$\hat{\beta}_{1,t}$$是模型1使用OLS方法依據$$\{ (y_s, X_{1,s}), ~s=1,2,\dots, t\}$$算出的估計參數。與給定的參數向量$$X^{\top}_{1,t+1}$$內積可得$$t+1$$期的預測值$$\hat{y}_{t+1} \equiv X^{\top}{1,t+1} \hat{\beta}{1,t}$$
* $$\hat{\beta}_{0,t}$$是模型0(基準模型)使用OLS方法依據$$\{ (y_s, X_{0,s}), ~s=1,2,\dots, t\}$$算出的估計參數。
* 此處$$\hat{\beta}_t=\begin{bmatrix} \beta_{0,t}^\top \\ \beta_{1,t}^\top \end{bmatrix}$$，注意模型1與模型0不可為巢狀模型(nested model)。



## 參考資料

* \[Dieb95] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," Journal of Business & economic statistics, vol. 20, 1995.&#x20;
* \[West96] K. D. West, "Asymptotic inference about predictive ability," Econometrica: Journal of the Econometric Society, pp. 1067-1084, 1996.&#x20;
* \[Whit00] Halbert White, “A REALITY CHECK FOR DATA SNOOPING,” Econometrica, Vol. 68, No. 5, pp. 1097-1126, 2000
* \[Roma05] Romano, J. P. and M. Wolf,. “Stepwise multiple testing as formalized data snooping,” Econometrica, Vol . 73, pp. 1237–1282, 2005.&#x20;
* \[Hans05] P.R. Hansen, “A test for superior predictive ability, ” Journal of Business and Economic Statistics, Vol. 23, No. 4, pp. 365-380, 2005.&#x20;
* \[Hans11] P. R. Hansen, A. Lunde, and J. M. Nason, "The Model Confidence Set," Econometrica, vol. 79, pp. 453-497, 2011.
* \[Hsu10] Po-Hsuan Hsu , Yu-Chin Hsub, Chung-Ming Kuan, “Testing the predictive ability of technical analysis using a new stepwise test without data snooping bias,” Journal of Empirical Finance, Vol. 17, pp. 471-484, 2010.&#x20;
* \[Clar12] T. E. Clark and M. W. McCracken, "Reality checks and comparisons of nested predictive models," Journal of Business & Economic Statistics, vol. 30, 2012.&#x20;
* \[Mari12] R. S. Mariano and D. Preve, "Statistical tests for multiple forecast comparison," Journal of Econometrics, vol. 169, pp. 123-130, 7, 2012.

