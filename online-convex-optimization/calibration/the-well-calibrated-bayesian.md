# The Well-Calibrated Bayesian

## 摘要

假設一個預測者依次為事件分配機率。如果例如他對某些事件分配了 30% 的機率，而這些事件在長期中實際發生的比例確實為 30%，那麼他就被認為是**良好校準的（well calibrated）** 。我們證明了一個定理，表明一個一致的貝氏預測者期望自己是良好校準的，並探討這對於一致性理論的潛在破壞性影響。

## 簡介

主觀機率預測已在美國的氣象學界廣泛應用（Murphy & Winkler, 1977）。氣象預報員常提供機率性天氣預測，例如：「今日丹佛降水機率為 30%。」這些機率反映的是預報員在當前資訊下的**主觀信念程度**，而非來自明確建模的客觀機率。這些資訊可能包括來自氣候分析或電腦預測系統的**客觀預測**，但不一定涉及明確的數學模型。

此類機率預測符合 Bayesian 概念（de Finetti, 1975），其中「一致的主觀貝氏學派」認為可以對所有可能觀察的資料建立聯合機率分佈。預<mark style="color:red;">測本質上是根據現有資訊對未觀察資料進行條件機率推斷</mark>。

雖然本文主要討論天氣預測，但這種方法適用於任何需要反覆進行機率預測的領域。

***

**機率預測的評估標準**

根據 Murphy & Epstein (1967)，機率預測可透過多種標準來評估，本文**專注於校準性（calibration）**，又稱<mark style="color:red;">**可靠性（reliability）**</mark>：

* 若在長期（理論上無限次）天氣預報中，針對所有「降水機率為 𝜃%」的日子，實際降水比例為 p，則繪製 p 對 𝜃 的圖表稱為<mark style="color:red;">**經驗校準曲線**</mark><mark style="color:red;">（empirical calibration curve）</mark>。
* 若曲線為對角線（即 p=𝜃），則預測被稱為<mark style="color:red;">**經驗上良好校準**</mark><mark style="color:red;">（empirically well calibrated）。</mark>
* 相同概念適用於<mark style="color:red;">**信賴區間預測**</mark><mark style="color:red;">（credible interval forecasts）</mark>，例如若 75% 可信區間長期內能精準覆蓋 75% 的真實值，則稱其為良好校準。

校準標準與**頻率派（frequentist）機率定義相似**，但不需假設恆定條件下的重複試驗。此外：

* 主觀機率預測通常不被解釋為客觀機率估計，而是事件發生的「指標」（indicator）。
* 傳統頻率派試圖透過選取「所有條件相同的日子」來界定「真實機率」，但此方法在實務上困難且主觀，因為不同預報員可能會對「相同條件」的定義產生分歧。



<figure><img src="../../.gitbook/assets/empirical_calibration_curve.png" alt="" width="375"><figcaption><p>經驗校準曲線（Empirical Calibration Curve）。<br>實心線：表示某位預測員的經驗校準曲線。<br>虛線（y=x）：表示完美校準，即預測機率與實際發生率完全匹配。</p></figcaption></figure>

***

**氣象預報員的校準與應用**

研究顯示**有經驗的氣象預報員通常校準良好**（Murphy & Winkler, 1977）。然而，<mark style="color:red;">良好校準並不意味著預測本身「優秀」，因為即使一個預測員</mark><mark style="color:red;">**只提供長期平均降水機率**</mark><mark style="color:red;">，仍然可能表現為良好校準。</mark>

其他研究（Lichtenstein et al., 1977）則發現部分預測結果校準較差。因此，有人建議（如 Cox, 1958）**對校準不佳的機率預測進行轉換**：

* 例如，若預測員對某天的降水機率估計為 30%，但歷史資料顯示這類預測日的實際降水率為 20%，則使用者應將該預測視為 20%。

不過，如何最佳利用他人的機率預測仍屬於獨立研究領域（Morris, 1974; Lindley et al., 1979）。

***

**預報員的視角與一致性問題**

本文探討**預報員如何看待自身的校準性**，並指出：

* 若預報員**具有一致性（coherence）**，則他應該期望自己是良好校準的。
* 這對「一致性理論」（coherence theory）產生挑戰，因為理論上，一致的貝氏預測員不應預期自己的機率預測會出現系統性偏差，但現實中部分預測員的校準性仍存問題。

這可能意味著，**即使在一致性框架下，仍可能需要機制來修正個別預測員的偏誤**，這是本文探討的重要議題之一。

### **重點整理**

1. **主觀機率預測** ：
   * 主觀機率預測已在氣象學家中廣泛應用，特別是在美國。
   * 預測員基於個人的主觀信念（degree of belief）提供機率，這些信念可能來自氣候分析或電腦預測系統。
2. **貝氏框架** ：
   * 貝氏主義者對所有可觀察量有一個聯合機率分佈。
   * 預測只是根據當前資訊總結未觀察到的條件分佈。
3. **校準標準** ：
   * 校準是指預測的機率是否與實際發生的頻率一致。
   * 如果預測的降雨機率為 30%，而實際降雨的比例也接近 30%，則預報員是良好校準的。
4. **經驗校準曲線** ：
   * 繪製預測機率與實際發生比例的關係曲線。
   * 如果曲線接近對角線，則預報員是良好校準的。
5. **信賴區間校準** ：
   * 信賴區間預測的校準要求預測的覆蓋率與宣告的機率一致（例如 75% 的可信區間應覆蓋 75% 的實際值）。
6. <mark style="color:red;">**校準 vs. 客觀機率**</mark> <mark style="color:red;"></mark><mark style="color:red;">：</mark>
   * <mark style="color:red;">校準標準不依賴於重複試驗或客觀機率。</mark>
   * <mark style="color:red;">主觀機率更適合視為對事件本身的估計，而非對「真實」機率的估計。</mark>
7. **經驗結果** ：
   * Murphy 和 Winkler 發現經驗豐富的預報員通常是良好校準的。
   * 校準不佳的預測可能需要調整（例如將 30% 的機率調整為 20%）。
8. **一致性與校準的矛盾** ：
   * 如果預報員是一致的，則他相信自己是良好校準的。
   * 這對一致性理論提出了挑戰，因為現實中可能存在校準失敗的情況。

***

## **獨立性與回饋**

* **獨立性假設問題** ：傳統方法假設不同事件是相互獨立的，但這可能不適用於序列預測（如天氣預報）。<mark style="color:red;">序列預測中，預測者會根據過去的經驗與結果調整未來的預測</mark>。
* **反饋效應** ：預測者每天都會根據截至今天的累積經驗進行明天的預測（例如是否下雨）來更新自己的預測模型。
* Harrison（1977)**的結論** ：認為潛在的未校準個體不可能保持一致性，因為他們無法完全信任未來的主觀機率分配。

數學結構如下。預測依序在第 0、1、2、... 天進行，每個預測指的是下一日可觀測到結果的事件或數量。

令$$\mathcal{B}_i$$為預測者在第$$i$$已知的資訊(σ代數，natural filtration)，可得$$\mathcal{B}_0 \subseteq \mathcal{B}_1 \subseteq \dots$$。

預測者的主觀機率分佈$$\Pi$$定義在$$\mathcal{B}_\infty =\bigcup_{i=0}^\infty \mathcal{B}_i$$上。預測者在第$$i-1$$日以條件機率$$\Pi(\cdot~|~ \mathcal{B}_{i-1})$$預測定義在$$\mathcal{B}_{i}$$上的事件或數量(註：以現在的所有知識估計未來事件的機率)。

令$$X_i$$為$$\mathcal{B}_i$$可測的數量$$i \in \mathbb{N}$$，例如台北第$$i$$日的最高氣溫，且令$$m_i$$為預測者在$$i-1$$日對$$X_i$$分佈評估的中位數。

令$$S_i$$為$$X_i > m_i$$的事件，則依定義$$\Pi(S_i ~|~ \mathcal{B}_{i-1})=\Pi(X_i > m_i ~|~ \mathcal{B}_{i-1})=1/2$$(預測者在$$i-1$$日對事件$$S_i$$的條件機率，因為$$m_i$$為$$X_i$$分佈的中位數，因此$$X_i > m_i$$的機率為1/2)。

* 因為$$(S_1, S_2, \dots, S_{i-1}) \in \mathcal{B}_{i-1}$$，而$$\Pi$$是預測者對所有可觀測量的聯合分佈。根據一致性（coherence），$$\Pi$$必須滿足機率的基本性質，例如條件機率的定義和馬可夫性質（在序列預測中）。
* 根據 Pratt (1962) 的結果，這些$$S_i$$在$$\Pi$$下是獨立的，且每個$$\Pi(S_i)=1/2$$。因為每次預測的中位數$$m_i$$是基於$$\mathcal{B}_{i-1}$$計算的，而$$S_i$$的機率完全由條件分佈$$\Pi(\cdot|\mathcal{B}_{i-1})$$決定。在一致的框架下，過去的結果$$(S_1, S_2, \dots, S_{i-1})$$不會改變中位數定義的基本性質，因此$$S_i$$與過去的$$S_j, j<i$$獨立。
* 如果預測者是「well-calibrated」（校準良好的），那麼長期來看，事件$$S_i$$發生的比例應該接近他預測的機率1/2。例如，若他預測了 1000 天，其中每天$$X_i > m_i$$的機率都是1/2，那麼大約 500 天應該滿足這個條件。
* 若實際上有 80% 的天數$$X_i$$超過$$𝑚_i$$，則預測者的校準顯然失敗，這與他認為自己機率1/2的預測相矛盾。這揭示了 coherence 和 calibration 之間的潛在衝突。

## **通用的校準定理**

在本節中，我們提出一個非常通用的結果，進一步擴展了前述關於一致性（coherence）與校準（calibration）之間的聯繫。我們再次假設預測是根據一個固定的機率分佈\
$$\Pi$$按序列進行的，但不再做其他假設。

對於每一天$$𝑖$$，我們有一個相關的事件$$S_i \in \mathcal{B}_i$$，例如第$$i$$天的降雨事件(註：第$$i$$天才發生的事件在事前無法精確得知，只能估計)。

以$$Y_i$$做為$$S_i$$的指標(indicator)，且$$\hat{Y}_i = \Pi(S_i ~|~ \mathcal{B}_{i-1}) = \mathrm{E}(S_i ~|~ \mathcal{B}_{i-1})$$，即在第$$(i-1)$$日對$$S_i$$的機率預測。

比較預測與現實的一種方法是選出某個相當隨意的測試集合，並在該集合中比較：

1. 相關事件實際發生的日子比例$$p$$。
2. 與這些日子平均預測機率$$\pi$$。形式上，我們引入指示變數$$\xi_1, \xi_2, \dots$$由預測者自行選擇，來表示某特定日子$$i$$ 是否包含在測試集合中：若包含，則$$\xi_i=1$$，；若不包含，則$$\xi_i=0$$。

我們可以事先一次性選定測試集合。然而，允許$$\xi_i$$按序列逐步確定是一個有用的擴展；因此，是否包含第$$i$$天的決定只需在第$$(i−1)$$天做出，並可根據截至第$$(i−1)$$ 天的知識任意決定。形式上，$$\xi_i$$必須是$$\mathcal{B}_{i-1}$$-可測的（measurable）。除此之外，對測試集合的日子選擇沒有限制。我們稱這種選擇過程為<mark style="color:red;">「可接受的」（admissible）</mark>。

整理：

* $$S_i$$：第$$i$$ 天的某事件（如降雨），屬於$$\mathcal{B}_i$$可測（第$$𝑖$$ 天可知資訊）。
* $$Y_i$$：$$S_i$$的指標（發生為 1，未發生為 0）。
* $$\hat{Y}_i=\Pi(S_i| \mathcal{B}_{i-1})$$：第$$i-1$$天對$$S_i$$的預測機率。
* $$\xi_i$$：指示第$$i$$天是否被選入測試集合，必須基於$$\mathcal{B}_{i-1}$$（即前一天資訊）決定，稱為「可接受的」（admissible）。

限定在截至第$$k$$天被選入測試集合的日子中：

* $$\displaystyle v_k=\sum_{i=1}^k \xi_i$$，為被選入測試集日子數量。
* $$\displaystyle p_k = \frac{\sum_{i=1}^k \xi_i Y_i}{v_k}$$，為相關事件實際發生的比例。
* $$\displaystyle \pi_k = \frac{\sum_{i=1}^k \xi_i \hat{Y}_i}{v_k}$$，為平均預測機率。

則有以下定理：

> **定理**：設選擇過程$$\{\xi_i\}$$ 是可接受的。以$$\Pi$$機率 1，若$$v_k \to \infty$$，則$$p_k - \pi_k \to 0$$。
>
> 這意味著，一致的預測者相信自己的預測機率長期會與實際頻率吻合，即他預期自己是校準良好的。

若允許$$\xi_i$$依賴於$$Y_i$$(根據事件是否發生來選擇日子)，則此結果一般不成立，因為這樣可以強制$$p_k=0$$(人為操縱結果)。

這個定理不僅限於天氣預報，而是適用於所有序列主觀機率預測的情境。它表明，一致的貝葉斯預測者在理論上無法承認自己可能長期誤校準（miscalibrated）

***

## 應用

### **經驗校準(empirical Calibration)**

**目標：**&#x5177;體探討「經驗校準」（empirical calibration），即預測機率與實際發生頻率的長期一致性。以天氣預報為例，驗證預測者是否能在特定機率值（如ω）附近保持校準。

經驗校準是衡量預測者表現的直觀標準，例如天氣預報員說「降雨機率 30%」的日子，長期應有約 30% 下雨。定理表明，一致的貝氏預測者（coherent Bayesian）主觀認為自己必然滿足這種校準，因為$$\Pi$$給予誤校準的機率為 0。

給定固定的目標機率值 $$\omega \in (0,1)$$，與允許偏差範圍$$\delta > 0$$，並定義$$\xi_i = 1$$，若且唯若$$|\hat{Y}_i - \omega| \leq \delta$$，即在第$$i$$天滿足誤差條件時，選入測試集合中。

也就是說，我們的測試日子集合僅包括那些相關事件的評估機率與某個給定值 $$\omega$$ 足夠接近的日子。這是可接受的（admissible），因為決定 $$\xi_i$$​ 的條件可以在第 $$(i-1)$$天確定。對於這種選擇，$$|\pi_k - \omega| \leq \delta$$。因此，由定理可知，以 $$\Pi$$-機率 1，假設選擇條件被無窮多次滿足，則對於所有足夠大的$$k$$，$$p_k$$​ 將接近$$\omega$$。換句話說，一致的序列預測者相信他將會是經驗上校準良好的（empirically well calibrated）。

進一步的擴展是，當選擇$$\xi_i = 1$$ 時，條件為$$|\hat{Y}_i - \omega| \leq \delta_i$$​，其中$$\delta_i$$ 可以依據截至第 $$(i-1)$$天的資訊而變動，且$$\delta_i \to 0$$。結論是，以 $$\Pi$$-機率 1，若選中的日子序列是無窮的，則 $$p_k \to \omega$$。

### 可變事件校準(v**ariable Event Calibration)**

可變事件校準」（variable event calibration），即事件$$S_i$$不是固定的，而是由預測者在預測時動態選擇的情況。

例如，天氣預報員每天給出「75% 機率溫度在 63°F 至 67°F 之間」，長期應有 75% 的日子滿足此預測。

$$X_i$$為台北第$$i$$天的最高溫度。預測者基於$$\mathcal{B}_{i-1}$$(前一天的資訊)計算$$X_i$$的條件分佈，並構造一個75%的信賴區間$$A_i$$。

定義$$S_i="X_i \in A_i"$$，事件定義為$$X_i$$落在該區間中。需確保$$S_i$$的定義不依賴當天結果$$Y_i$$，否則可能違反「可接受性」條件。

$$\hat{Y}_i=\Pi(S_i|\mathcal{B}_{i-1})=0.75$$，因為$$A_i$$為75%的信賴區間。

乍看之下，$$S_i$$是動態選擇的，似乎超出定理範圍。但因$$S_i$$在第$$𝑖$$ 天確定並屬於$$\mathcal{B}_i$$\
，且$$\hat{Y}_i$$基於$$\mathcal{B}_{i-1}$$，仍滿足定理的條件（$$\xi_i$$可接受性）。

唯一要求是$$S_i$$的選擇在第$$i$$天之前完成（例如在第$$𝑖−1$$天根據條件分佈確定\
$$A_i$$），這在例子中已滿足。

**4.3 Model-Based Forecasts**

* **基於模型的預測** ：如果資料來自某客觀分佈P，且模型包含真實分佈，則預測將是良好校準的。
* **反例** ：若校準失敗，則整個模型可能需要被修正。

***

#### **5. Recalibration?**

* **重新校準的挑戰** ：如果預測者的經驗校準曲線偏離理想對角線，是否可以通過重新校準改進？
* **矛盾** ：重新校準會導致不一致性，因為它意味著對同一事件賦予兩個不同的機率。
* **結論** ：即使重新校準成功，也不能保證對任意選擇過程都成立。

***

#### **6. Coherence and Cromwell's Rule**

* **一致性與零機率** ：理論上，一致性要求預測者不能對可能事件賦予零機率（即遵循Cromwell法則）。
* **悖論** ：然而，在現實中，預測者通常對非忽視事件（如未校準）賦予零機率，這與Cromwell法則衝突。
* **反思** ：作者對一致性理論的普遍適用性提出質疑，認為現有理論尚不足以處理複雜引數空間的統計模型。

***

#### **7. Coherence or Calibration?**

* **兩難困境** ：一致性與校準之間存在衝突。預測者可能需要在兩者之間做出取捨。
* **建議** ：預測者應像對待外部統計系統一樣，以暫時的方式對待自己的主觀分佈II。當發現未校準時，應修改或替換該分佈。
* **未來方向** ：探討如何設計一個既能保持一致性又能自我校準的分佈。

***

#### **Appendix: Proof of Theorem**

* **技術細節** ：附錄提供了定理的數學證明，基於鞅收斂定理和Kronecker引理。
* **結論** ：證明了在適當條件下，預測者的實際表現將收斂到其預測機率。

***

#### **References**

* 文章引用了多篇相關文獻，涵蓋決策分析、貝葉斯統計、校準理論等領域。

***

#### **Comment by Joseph B. Kadane**

* Kadane教授對文章進行了評論，指出：
  1. 完全一致性分佈的構建在實踐中幾乎不可能實現。
  2. 預測者需考慮所有可能的未來資料與發現，這超出了人類能力範圍。
  3. 即使如此，文章的結論（預測者相信自己將是良好校準的）仍具有合理性。

***

總結：本文的核心在於探討貝葉斯預測者的一致性與校準之間的關係，並提出了校準定理，揭示了兩者之間的矛盾與挑戰，同時呼籲進一步完善一致性理論以解決現實問題。

## **例子：天氣預報**

假設有一位天氣預報員每天預測某地「降雨機率」，並根據他的預測記錄一段時間內的結果。

**步驟 1：收集資料**

* 預報員在過去一年中做了 365 次降雨預測。
* 我們將這些預測分組，例如：
  * 當他預測「降雨機率為 30%」時，這類預測總共出現了 100 天。
  * 在這 100 天中，實際上降雨的天數是 30 天。

**步驟 2：計算實際發生的比例**

* 對於「降雨機率為 30%」的預測，實際降雨的比例是：實際降雨比例=總天數降雨天數​=10030​=0.3
* 也就是說，實際降雨的比例（30%）與預測的降雨機率（30%）是一致的。

**步驟 3：檢查其他機率**

* 再來看其他機率的情況：
  * 如果預報員預測「降雨機率為 70%」的天數有 50 天，其中降雨的天數是 35 天，則實際降雨比例為：5035​=0.7這也與預測的 70% 一致。

**步驟 4：繪製校準曲線**

* 為了更直觀地檢查校準性，我們可以繪製一條「校準曲線」：
  * 橫軸：預測的降雨機率（例如 30%、50%、70% 等）。
  * 縱軸：實際降雨的比例。
* 如果預測是良好校準的，那麼這條曲線應該接近對角線（即預測值 = 實際值）。

***

#### **結論**

* 如果預測者的校準曲線接近對角線，表示他是「良好校準」的。
* 如果曲線偏離對角線，例如預測的降雨機率總是高於實際降雨比例，則表示預測者過於樂觀（或保守），需要調整預測方法。

#### **應用到其他領域**

這個概念不僅適用於天氣預報，還可以用於其他領域，例如：

* **醫療診斷** ：醫生預測某患者患病的機率，並檢查這些預測是否與實際診斷結果一致。
* **金融預測** ：分析師預測某股票上漲的機率，並檢查這些預測是否與實際市場走勢相符。

## 參考資料

* &#x20;A. Philip. Dawid, "The well-calibrated Bayesian," _Journal of the American statistical Association_ Vol.77, No.379,pp. 605-610, 1982.
