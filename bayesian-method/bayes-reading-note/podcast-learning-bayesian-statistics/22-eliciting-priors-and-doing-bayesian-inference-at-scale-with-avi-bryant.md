# #22 Eliciting Priors and Doing Bayesian Inference at Scale, with Avi Bryant

\[[youtube](https://www.youtube.com/watch?v=nQPDELDbckM\&ab_channel=LearningBayesianStatistics)]

#### **訪談背景**

* 訪談嘉賓是 **Avi Bryant**，他是工程師背景出身的貝氏建模專家，目前專注於機器學習和工程應用，尤其是在大型系統中的貝氏推論。
* 主題涵蓋：
  * 貝氏推論的實際應用。
  * Priors（先驗分佈）的設計和選取。
  * 如何在工業規模上實施貝氏方法。

***

#### **核心內容**

**1. Avi 的背景與經歷**

* **工程與統計的結合**：
  * Avi 起初的專業是電腦科學，並在 Twitter 和 Stripe 等公司參與大型資料系統的建構。
  * 他帶領 Stripe 團隊建造貝氏推論框架 **Rineer**，專注於在 Scala 平台上進行大規模推論。

**2. Rineer 的誕生與挑戰**

* **設計動機**：
  * Stripe 的一個關鍵問題是如何為每個商家（如電子商務網站）建立個性化的風險模型，例如防止商家倒閉造成的資金損失。
  * 解決方案需要處理數百萬個獨立模型，因此選擇了 Scala 作為工具，以實現與 JVM 生態系統的無縫整合。
* **實現過程**：
  * 初期的實驗以簡單的 Monte Carlo 方法為基礎，後來進一步實現了 Hamiltonian Monte Carlo（HMC）取樣器。
  * 為了提高效率，採用了基於靜態計算圖（DAG）的計算模型，類似於 TensorFlow 的運作方式，但針對 JVM 最佳化。

**3. 工業應用中的挑戰**

* **部署與使用障礙**：
  * 雖然 Rineer 在技術上成功解決了大規模推論的問題，但在內部的廣泛採用受到限制，主要原因是許多工程師缺乏統計背景。
  * Avi 指出，設計一個簡化的使用者介面，幫助非統計專家使用貝氏模型，是未來的重要方向。
* **建模過程的複雜性**：
  * <mark style="color:red;">新增新特徵或變數時，貝氏模型需要更多的推理與設計，這與傳統的隨機森林或深度學習模型「快速試錯」的特性不同</mark>。

***

#### **貝氏推論的未來方向**

1. **降低學習門檻**：
   * 開發更直觀的工具（例如透過圖形介面）來幫助使用者設計先驗分佈。
   * 提出一種基於使用者輸入分佈形狀、最大值/最小值的方式生成先驗，而不是要求使用者直接選擇數學分佈。
2. **更好的決策支援系統**：
   * 不僅關注模型的建構，還要提升基於後驗分佈進行決策的工具，讓更多非專家能夠有效應用貝氏決策理論。
3. **工業環境的部署最佳化**：
   * 將工具整合到現有的工業系統中（例如 Spark 或 JVM），並提高其效能與穩定性。

***

#### **Avi 的觀點**

* **對初學者的建議**：
  * 理解不確定性是學習貝氏方法的關鍵，且早期的困惑是正常的。
  * 可以從簡單的模擬開始，逐步深入到貝氏建模的核心概念。
* **對 PPL（機率程式語言）的願景**：
  * 未來的 PPL 可能更像電子表格，提供簡單直接的介面來幫助使用者進行生成模型的設計。
  * 強調為不同使用者群體（如工程師或社會科學家）量身定製的工具。

***

**總結**\
Avi 的工作展示了如何將貝氏推論方法應用於實際工程場景，並強調了工具設計與使用者教育的重要性。他認為未來的挑戰在於讓貝氏方法對非專家更具可存取性，並讓其更高效地融入工業環境。