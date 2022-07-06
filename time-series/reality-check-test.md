---
description: RC, SPA, MCS檢定
---

# 真實性檢定(Reality Check Test)

![RC檢定相關論文](../.gitbook/assets/rc\_spa\_mcs-min.png)

## 資料窺探的偏差(data snooping bias)

當一個給定的資料集被多次用於推理或模型選擇時，就會發生資料窺探。即所獲得的任何令人滿意的結果可能僅僅是由於運氣好，而不是由於產生結果的方法更好。

由於金融資料難以重複實驗的侷限性，個別的研究者通常利用相同的資料進行研究，卻忽略了將這種重複利用相同資料進行研究，所產生對資料的過度推論或是推論錯誤，稱為資料窺探(data snopping)問題。當模型(基金、股票或交易策略或是預測模型)數目眾多時，因資料窺探而產生的偏誤會更加嚴重。

## 真實性檢定(reality check test)

RC檢定必須要有一個基準模型，假設有$$m$$個要和基準模型比較的模型，且有$$n$$期的資料，則第$$i$$個模型在第$$t$$期和基準模型的輸出值的差值為$$D_{it}$$，而第$$i$$個模型和基準模型的平均差值為$$\overline{D}_i$$。

<mark style="color:red;">RC檢定的虛無假設為沒有任何一個比較模型表現比基準模型好，因此所有模型的差值平均值應小於等於0</mark>。

![](../.gitbook/assets/RC\_null-min.png)



## SPA(Superior Predictive Ability)檢定

因RC的檢定效力在所比較的規則集合中，若有過多沒有解釋（預測）能力的規則被加入，會大大降低檢定效力。而SPA將統計量正規化後解決了這個問題，故截至目前為止是用來檢定技術分析(交易策略)是否有效的首要工具。

## Stepwise-RC & Stepwise-SPA 檢定

Step-RC 檢定法可以透過多重階段，逐步找出所有顯著優於比較基準的模型。 然而Step-RC 檢定法的基礎是 RC 檢定法，所以其檢定力在各階段同樣容易受到較差模型影響。&#x20;

Hsu et al. 因此提出了 Step-SPA 檢定法，將各階段的檢定以 SPA 檢定法的方式加以調整。他們的數學證明與模擬結果均顯示，Step-SPA 檢定法可以增加 Step-RC 的檢定力。

## 參考資料

* \[Dieb95] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," Journal of Business & economic statistics, vol. 20, 1995.&#x20;
* \[West96] K. D. West, "Asymptotic inference about predictive ability," Econometrica: Journal of the Econometric Society, pp. 1067-1084, 1996.&#x20;
* \[Whit00] Halbert White, “A REALITY CHECK FOR DATA SNOOPING,” Econometrica, Vol. 68, No. 5, pp. 1097-1126, 2000
* \[Roma05] Romano, J. P. and M. Wolf,. “Stepwise multiple testing as formalized data snooping,” Econometrica, Vol . 73, pp. 1237–1282, 2005.&#x20;
* \[Hans05] P.R. Hansen, “A test for superior predictive ability, ” Journal of Business and Economic Statistics, Vol. 23, No. 4, pp. 365-380, 2005.&#x20;
* \[Hans11] P. R. Hansen, A. Lunde, and J. M. Nason, "The Model Confidence Set," Econometrica, vol. 79, pp. 453-497, 2011.
* \[Hsu10] Po-Hsuan Hsu , Yu-Chin Hsub, Chung-Ming Kuan, “Testing the predictive ability of technical analysis using a new stepwise test without data snooping bias,” Journal of Empirical Finance, Vol. 17, pp. 471-484, 2010.&#x20;
* \[Clar12] T. E. Clark and M. W. McCracken, "Reality checks and comparisons of nested predictive models," Journal of Business & Economic Statistics, vol. 30, 2012.&#x20;
* \[Mari12] R. S. Mariano and D. Preve, "Statistical tests for multiple forecast comparison," Journal of Econometrics, vol. 169, pp. 123-130, 7// 2012.

