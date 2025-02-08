---
description: >-
  Qingsong Wen et al. "Onenet: Enhancing time series forecasting models under
  concept drift by online ensembling, " Advances in Neural Information
  Processing Systems Vol. 36, 2023).
---

# conference:OneNet: Enhancing Time Series Forecasting Models under Concept Drift by Online Ensembling

## 摘要

在線時間序列預測模型的更新旨在通過基於串流數據有效更新預測模型來解決概念漂移問題。許多演算法都是為在線時間序列預測而設計的，其中一些利用了跨變數依賴性，而另一些則假設變數之間是獨立的。鑑於每個數據假設在線上時間序列建模中都有其優缺點，我們提出了線上集成網路 (OneNet)。它動態更新並結合了兩個模型，其中一個側重於模擬時間維度上的依賴性，另一個側重於跨變數依賴性。我們的方法將基於強化學習的方法融入到傳統的線上凸規劃框架中，允許以動態調整的權重線性組合兩個模型。 OneNet 解決了經典線上學習方法的主要缺點，即它們在適應概念漂移時往往很慢。 實驗結果表明，與最先進 (SOTA) 的方法相比，OneNet 將在線預測誤差降低了 50% 以上。

1. **概念漂移（Concept Drift）**\
   時間序列資料的統計特性隨時間變化，導致傳統批次學習模型失效。例如，氣象預測或使用者行為模式變化。
2. **現有模型限制**
   * 主流模型（如TCN、Transformer）假設資料分佈靜態，無法適應動態環境。
   * 單一模型難以同時捕捉時間依賴（cross-time）和變數依賴（cross-variable），尤其在概念漂移下表現不穩。

**核心方法：OneNet**

1. **雙流架構（Two-Stream Architecture）**
   * **Cross-Time Forecaster**：專注時間維度依賴（如PatchTST），假設變數獨立。
   * **Cross-Variable Forecaster**：捕捉跨變數關聯（如TCN），忽略長期時間依賴。
   * **挑戰**：如何有效組合這兩種模型的預測結果？
2. **動態整合策略（Online Convex Programming, OCP）**
   * 傳統指數梯度下降（Exponentiated Gradient Descent, EGD）方法在處理概念漂移時適應速度較慢。
   * **問題**：EGD 依賴長期歷史資料，無法快速適應突變的環境變化（slow switch phenomenon）。
   * 使用**強化學習（RL）**&#x52D5;態調整兩模型權重，結合長期歷史表現（EGD更新）與短期環境變化（RL偏差項）。
   * **短期權重 (Short-term weight)**：透過 RL 進行離線學習，快速調整近期變化的影響。
   * **長期權重 (Long-term weight)**：透過 OCP 記錄歷史資料的表現。
   *   權重公式：$$\tilde{w}_{t,i}=\frac{w_{t,i} + b_{t,i}}{ \sum(w_{t,i} + b_{t,i}) }$$

       其中，$$w_{t,i}$$​為長期權重，$$b_{t,i}$$​為RL學習的短期偏差。
3. **解耦訓練策略**
   * 分開訓練兩個預測器和整合模組，避免模型退化（如某分支權重趨近零時停止更新）。

### **實驗結果**

#### **OneNet 相較於基線方法**

**MSE（均方誤差）比較**

| 方法           | ETTh2     | ETTm1     | WTH       | ECL       | 平均 MSE    |
| ------------ | --------- | --------- | --------- | --------- | --------- |
| FSNet (SOTA) | 0.846     | 0.127     | 0.223     | 7.034     | 1.594     |
| Time-TCN     | 1.307     | 0.308     | 0.308     | 5.230     | 1.549     |
| **OneNet**   | **0.609** | **0.108** | **0.200** | **2.201** | **0.747** |

OneNet 相較於 FSNet，MSE 平均降低 **53.1%**，證明其適應概念漂移的能力。

**MAE（平均絕對誤差）比較**

| 方法           | ETTh2     | ETTm1     | WTH       | ECL       | 平均 MAE    |
| ------------ | --------- | --------- | --------- | --------- | --------- |
| FSNet (SOTA) | 0.515     | 0.263     | 0.301     | 1.061     | 0.448     |
| Time-TCN     | 0.636     | 0.421     | 0.378     | 0.438     | 0.399     |
| **OneNet**   | **0.436** | **0.238** | **0.279** | **0.348** | **0.293** |

OneNet 相較於 FSNet，MAE 平均降低 **34.5%**。

1. **關鍵觀察**
   * **變數獨立性**：對高變數資料（如ECL）至關重要，但低變數資料需跨變數依賴。
   * **例項歸一化**：雖提升穩定性，但可能阻礙快速適應新分佈。
2. **輕量版OneNet-**
   * 引數更少（如投影頭維度降低），仍優於FSNet，適合資源受限場景。

### **強化學習與 OCP 的效果**

* **EGD（OCP 傳統方法）** 會慢慢適應概念漂移，但在急劇變化時效果不佳。
* **RL-W（僅使用強化學習）** 能快速適應，但長期表現不穩定。
* **OneNet (OCP + RL)** 透過結合長短期權重，取得最佳表現。

### **理論貢獻**

1. **遺憾界（Regret Bound）分析**
   * 證明EGD演算法的長期權重更新具有次線性遺憾界，但對突變適應慢。
   * 提出分階段重設權重的策略，改善短期適應能力。
2. **內部遺憾（Internal Regret）**
   * 通過RL調整權重，顯著降低模型切換延遲（如圖5實驗驗證）。

### **未來方向**

1. **歸一化技術改進**：平衡分佈穩定性與快速適應。
2. **高效調參方法**：結合NLP/CV中的提示（prompt）技術，減少全模型重訓練。
3. **多模型擴充套件**：驗證整合多於兩個模型的可行性（初步實驗顯示效能提升）。

## 參考資料

* [https://github.com/yfzhang114/OneNet](https://github.com/yfzhang114/OneNet)
* [conference paper pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/dd6a47bc0aad6f34aa5e77706d90cdc4-Paper-Conference.pdf).
* [補充資料pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/dd6a47bc0aad6f34aa5e77706d90cdc4-Supplemental-Conference.pdf).
* [\[arxiv\] Addressing Concept Shift in Online Time Series Forecasting: Detect-then-Adapt](https://arxiv.org/abs/2403.14949).&#x20;



