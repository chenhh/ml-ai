# 常態分佈檢定

## 簡介

以下檢定方法的**虛無假設**$$H_0$$ 都是：「資料**服從常態分佈**」。

| 方法名稱                              | 適用情況                   | 特點                                     | 實作                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | ---------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Shapiro-Wilk test**（最推薦）        | 小到中樣本（$$n \leq 2000$$） | 最常用、靈敏度高。但大樣本可能過於嚴格。                   | [scipy.stats.shapiro](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)                                                                                                                                                                                                                                                                                                   |
| **Kolmogorov-Smirnov test (K-S)** | 適用於一般情況                | 假設完整分佈已知，但對參數估計敏感。                     | [scipy.stats.kstest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html)                                                                                                                                                                                                                                                                                                     |
| **Lilliefors test**               | K-S 的變形，μ 和 σ 為未知      | 常見於軟體套件。                               | [statsmodels.stats.diagnostic.lilliefors](https://www.statsmodels.org/dev/generated/statsmodels.stats.diagnostic.lilliefors.html)                                                                                                                                                                                                                                                                      |
| **Anderson-Darling test**         | 小樣本也可用                 | 比 K-S 更重視尾部行為，但計算較複雜。                  | [scipy.stats.anderson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html)                                                                                                                                                                                                                                                                                                 |
| **Jarque-Bera test**              | 大樣本                    | 基於偏態與峰度（Skewness & Kurtosis），但對小樣本不敏感。 | [scipy.stats.jarque\_bera](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.jarque_bera.html)                                                                                                                                                                                                                                                                                          |
| **D'Agostino's K² test**          | 中至大樣本                  | 同樣基於偏態與峰度，檢定更全面                        | [scipy.stats.normaltest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html)                                                                                                                                                                                                                                                                                             |
| **QQ Plot（視覺）**                   | 輔助工具                   | 非正式，但直觀有效                              | <p></p><ul><li>Q-Q 圖：<a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html">scipy.stats.probplot</a></li><li>直方圖：<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html">matplotlib.pyplot.hist</a></li><li>箱型圖：<a href="https://app.gitbook.com/s/hxLbxPthAx6a1D9i59ud/economics/economics-reading">matplotlib.pyplot.boxplot</a></li></ul> |

### 檢定原理

**偏度和峰度檢查**

* 偏度（Skewness）衡量資料的對稱性，正態分佈的偏度為 0。
* 峰度（Kurtosis）衡量資料的尾部厚度，正態分佈的峰度為 3。
* 如果偏度和峰度顯著偏離理論值，則可能表明資料不服從正態分佈。

**經驗分佈函式（Empirical Distribution Function, EDF）**

* 比較樣本資料的經驗分佈函式與理論正態分佈的差異。
* K-S 檢定和 Anderson-Darling 檢定均屬於這一類。

### 選擇適當的檢定方法

**小樣本 (**$$n < 50$$**)**：優先使用 Shapiro-Wilk 檢定，輔以 Q-Q 圖。

**中等樣本 (**$$50 < n < 200$$**)**：Shapiro-Wilk 或 Anderson-Darling 檢定較合適。

**大樣本 (**$$n > 200$$**)**：Jarque-Bera 或 D’Agostino’s K² 檢定，因其對偏度和峰度敏感。

**未知引數**：Lilliefors 檢定或標準化後的 K-S 檢定。

**多方面確認**：結合圖形方法（如 Q-Q 圖）和統計檢定，避免單一檢定誤判。

**資料特性** ：

* 如果關心尾部分佈：Anderson-Darling 檢定。
* 如果需要快速圖形化檢查：QQ 圖。

**計算資源** ：

* Shapiro-Wilk 檢定計算複雜度較高，但精度高。

**樣本量影響**：小樣本檢定可能缺乏檢定力（power），大樣本則可能對微小偏差過於敏感。

* 小樣本容易導致假陰性（Type II Error），即無法檢測到非正態性。
* 大樣本容易導致假陽性（Type I Error），即過於敏感地拒絕正態性假設。

**資料特性**：若資料有異常值、離群點或明顯偏態，應先進行探索性分析（如直方圖或箱型圖）。

**檢定侷限**：拒絕 $$H_0$$ 不一定表示資料完全偏離常態，可能只是某部分特性（如尾部）不符。



\[Das 16] 在進行任何正式的統計分析之前，評估資料的正態性是至關重要的。否則我們可能會得出錯誤的推斷和錯誤的結論。正態性可以通過視覺和正態性檢驗來評估。大多數統計軟體包都會自動生成PP圖和QQ圖。由於圖形檢驗非常主觀，所以強烈建議使用分析檢驗。然而。<mark style="color:red;">但是，當我們在回歸和/或實驗設計中測試殘差的正常性時，Shapiro-Wilk和Jarque-Bera檢驗都不合適。在這方面，我們建議使用重標動差檢驗</mark>。

\[Hernandez21] 判斷一個資料樣本是否來自常態分配的群體是統計學和資料分析中的一個常見做法。到目前為止，科學文獻中已經提出了幾十種檢驗正態性的方法。因此，出現的一個共同問題是。什麼是檢驗樣本正態性的最佳方法？本報告的第一部分簡要回顧了用於檢驗正態性的最重要的方法類型。然後，通過對過去30年中發表的幾種正態性測試的力量對比的調查，對55種最常見的方法進行了排名。這項分析的總冠軍是基於回歸的Shapiro-Wilk（SW）正態性檢驗。(排名見Table 2)。

## 相關文獻

* Keya Rani Das and A. H. M. R. Imon. "A brief review of tests for normality," pp. 5-12, Vol. 5.1, American Journal of Theoretical and Applied Statistics, 2016.
* <mark style="color:red;">Hugo Hernandez, "Testing for normality: what is the best method," Vol. 6, 2021-05, ForsChem Research Reports, 2021</mark>.

