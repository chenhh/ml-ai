---
description: >-
  Avrim Blum and Yishay Mansour, "From external to internal regret," Journal of
  Machine Learning Research, Vol.8, No. 6, pp. 1307-1324, 2007.
---

# paper:From External to Internal Regret

## 摘要

外部遺憾（External regret）將一個線上演算法的效能（該演算法從 N 個動作中選擇）與事後最佳動作的效能進行比較。內部遺憾（Internal regret）則將一個線上演算法的損失與另一個修改後的線上演算法的損失進行比較，其中修改後的演算法始終用某個動作替換另一個動作。

在本文中，我們提出了一種簡單且通用的歸約方法，<mark style="color:red;">該方法基於解決外部遺憾問題的演算法，將其轉化為一種高效的內部遺憾問題線上演算法</mark>。我們的方法既適用於完全資訊模型 （即每個時間步驟都能觀察到每個動作的損失），也適用於部分資訊模型 （即每次只能觀察到所選動作的損失，例如強盜(bandit)問題模型）。<mark style="color:red;">內部遺憾在賽局論中的重要性在於，在一般的賽局中，如果每個玩家的內部遺憾是次線性的，那麼經驗頻率將收斂到相關均衡（correlated equilibrium）</mark>。

對於外部遺憾，我們還推匯出了一個非常廣泛設定下的定量遺憾界。這一設定包括一組任意的修改規則（可能對線上演算法進行修改）和一組任意的時間選擇函式（每個函式對每個時間步驟賦予不同的權重）。對於給定的時間選擇函式和修改規則，遺憾被定義為線上演算法的成本與修改後的線上演算法的成本之間的差異，其中成本由時間選擇函式加權。這可以被視為先前研究的「休眠專家」（sleeping experts）設定的一種推廣。

## 參考資料

Avrim Blum and Yishay Mansour, "From external to internal regret," Journal of Machine Learning Research, Vol.8, No. 6, pp. 1307-1324, 2007.
