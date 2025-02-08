---
description: >-
  Qingsong Wen et al. "Onenet: Enhancing time series forecasting models under
  concept drift by online ensembling, " Advances in Neural Information
  Processing Systems Vol. 36, 2023).
---

# NIPS paper:OneNet: Enhancing Time Series Forecasting Models under Concept Drift by Online Ensembling

## 摘要

在線時間序列預測模型的更新旨在通過基於串流數據有效更新預測模型來解決概念漂移問題。許多演算法都是為在線時間序列預測而設計的，其中一些利用了跨變數依賴性，而另一些則假設變數之間是獨立的。鑑於每個數據假設在線上時間序列建模中都有其優缺點，我們提出了線上集成網路 (OneNet)。它動態更新並結合了兩個模型，其中一個側重於模擬時間維度上的依賴性，另一個側重於跨變數依賴性。我們的方法將基於強化學習的方法融入到傳統的線上凸規劃框架中，允許以動態調整的權重線性組合兩個模型。 OneNet 解決了經典線上學習方法的主要缺點，即它們在適應概念漂移時往往很慢。 實驗結果表明，與最先進 (SOTA) 的方法相比，OneNet 將在線預測誤差降低了 50% 以上。

## 參考資料

* [https://github.com/yfzhang114/OneNet](https://github.com/yfzhang114/OneNet)
* [conference paper pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/dd6a47bc0aad6f34aa5e77706d90cdc4-Paper-Conference.pdf).
* [補充資料pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/dd6a47bc0aad6f34aa5e77706d90cdc4-Supplemental-Conference.pdf).
* [\[arxiv\] Addressing Concept Shift in Online Time Series Forecasting: Detect-then-Adapt](https://arxiv.org/abs/2403.14949).&#x20;



