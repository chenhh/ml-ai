# #20 Regression and Other Stories, with Andrew Gelman, Jennifer Hill & Aki Vehtari

\[[youtube](https://www.youtube.com/watch?v=OJyoXJzxTGs\&ab_channel=LearningBayesianStatistics)]

#### **訪談背景**

* 訪談嘉賓包括 **Andrew Gelman**、**Jennifer Hill** 和 **Aki Vehtari**，他們是書籍《Regression and Other Stories》的作者。
* Andrew Gelman：哥倫比亞大學教授，統計學和政治科學專家。
* Jennifer Hill：紐約大學教授，應用統計學專家。
* Aki Vehtari：芬蘭阿爾託大學教授，計算機率建模專家。
* 這本書聚焦於迴歸分析的應用、建模策略，以及如何將迴歸與實際資料結合，對因果推論和模型改進也有所著墨。

***

#### **關於書籍**

1. **書籍目標**：
   * 這本書針對有統計基礎且希望深入理解迴歸分析的讀者，特別是那些希望應用這些方法於實際資料的使用者。
   * 強調從基礎迴歸到進階模型的逐步學習，並提供大量範例和實用建議。
2. **主要內容**：
   * 如何構建迴歸模型並解釋結果。
   * 迴歸的限制及如何應對常見挑戰。
   * 整合了傳統迴歸與貝葉斯（Bayesian）方法的視角，並解釋了兩者的聯絡。
3. **附錄 B：迴歸建模的十個快速技巧**：
   * 作者總結了改進迴歸建模的十個重要技巧，並在訪談中逐一討論。

***

#### **核心觀點與技巧**

**1. 考慮資料的變異與複製性**

* 不要將分析視為單一實驗，而是嵌入更大的資料流程中。
* 重視模型在不同資料集上的表現，以檢查結論的穩定性。

**2. 忽略「統計顯著性」**

* 反對將資料簡化為「顯著」與「不顯著」的二元分類。
* 強調效應大小與不確定性的全面評估，而非過度依賴 ppp 值。

**3. 繪製相關的圖表**

* 將模型結果與資料放在同一圖表中進行比較。
* 圖表應該是為瞭解決特定問題而設計，而非僅僅滿足習慣或規範。

**4. 解釋迴歸係數為「比較」**

* 將迴歸係數解釋為在特定條件下的平均差異，而非因果效應。
* 這種表述更貼近現實資料的描述性特徵。

**5. 使用模擬資料**

* 在真實資料分析之前，先對模型進行模擬測試。
* 模擬可以幫助檢查模型假設並發現潛在問題。

**6. 測試多個模型**

* 從簡單模型開始，逐步增加複雜度，以漸進方式理解資料。
* 在面對不確定的模型假設時，考慮對模型空間進行整合。

**7. 建立計算工作流程**

* 明確分析的步驟，記錄每一步操作，確保可重現性。
* 考慮計算資源的限制，例如記憶體與時間。

**8. 使用變數變換**

* 適當的變換可以改善模型的擬合效果並滿足假設（如線性關係）。
* 提及常見變換（對數、冪函式等）及其應用情境。

**9. 針對性進行因果推論**

* 若目標是回答因果問題，需明確設計對應的研究方法，而非將回歸結果當作因果推論。
* 闡明處理變數與假設的合理性，避免「菜色沙拉」式的迴歸分析。

**10. 通過例項學習**

* 利用真實案例或模擬情境學習模型方法。
* 在課堂中結合專案制學習，讓學生處理自己感興趣的資料問題。

***

#### **迴歸的限制與挑戰**

* 真實世界中的資料通常比書中的範例更複雜，需要額外考慮測量誤差、缺失資料等問題。
* 線性迴歸對非線性效應或互動項的處理能力有限，需結合正則化或非引數模型進行擴充套件。

***

**總結**：\
這次訪談探討了《Regression and Other Stories》的核心理念與作者的實踐經驗。他們強調了迴歸建模的靈活性和應用挑戰，並提供了實用的改進建議。該書不僅適合初學者，也為高級讀者提供了深入探討迴歸問題的機會。