# 概念漂移（Concept Drift）

## **概念漂移 vs. 結構點轉變**&#x20;

| 特徵         | 概念漂移 (Concept Drift) | 結構點轉變 (Structural Break)  |
| ---------- | -------------------- | ------------------------- |
| **關注點**    | 目標變數的統計特性變化          | 統計模型中底層關係或引數的結構性變化        |
| **核心問題**   | 模型預測效能隨時間下降          | 模型結構穩定性受到破壞，模型假設不再成立      |
| **變化型別**   | 突然、漸進、增量、週期性         | 突發性、漸進性                   |
| **處理方法**   | 漂移偵測、線上學習、模型適應       | 結構點檢測、分段模型、時變引數模型、穩健方法    |
| **模型調整目標** | 維持預測準確性、提高模型泛化能力     | 保持模型結構的有效性、準確估計模型引數       |
| **影響**     | 模型預測精度下降，需要持續監控和更新模型 | 影響模型解釋能力和預測能力，需要重新評估模型適用性 |
| **資料特性**   | 通常用於流資料、動態環境中的資料     | 通常用於時間序列資料、經濟和金融資料        |

傳統機器學習分為訓練和預測兩個階段，而概念漂移研究引入了三個新元件：漂移檢測、漂移理解和漂移適應。

概念漂移（Concept Drift）涵蓋了概念漂移的檢測（Detection）、理解（Understanding）和適應（Adaptation）。

## 概念漂移的定義與來源

* 概念漂移指的是目標變數的統計屬性隨時間發生不可預測的變化，導致模型在新資料上的表現變差。
* 主要來源：
  * **虛擬漂移（Virtual Drift）**：特徵分佈$$P(X)$$變化，但決策邊界未變$$P(y|X)$$。
  * **實際漂移（Real Drift）**：決策邊界$$P(y|X)$$變化，影響模型預測準確性。
  * **混合漂移（Hybrid Drift）**：特徵分佈與決策邊界同時變化。

### 概念漂移的型別

* **突發性漂移（Sudden Drift）**：短時間內出現新概念（例如：政策改變）。
* **漸變性漂移（Gradual Drift）**：新概念逐步取代舊概念（例如：市場需求變化）。
* **增量漂移（Incremental Drift）**：概念逐步改變（例如：客戶行為變化）。
* **重現漂移（Recurring Drift）**：舊概念在一段時間後重新出現（例如：季節性模式）。

## 概念漂移檢測（Concept Drift Detection）

* **基於錯誤率的方法**（Error Rate-based）：監控模型錯誤率變化，例如：
  * **DDM**（Drift Detection Method）
  * **EDDM**（Early Drift Detection Method）
  * **ADWIN**（Adaptive Windowing）
* **基於資料分佈的方法**（Data Distribution-based）：通過統計方法比較新舊資料分佈，例如：
  * **Kullback-Leibler 散度**（KL Divergence）
  * **Relativized Discrepancy**
  * **PCA-based Change Detection**
* **多重假設檢測方法**（Multiple Hypothesis Testing）：結合多種假設檢測，例如：
  * **JIT**（Just-In-Time adaptive classifiers）
  * **HLFR**（Hierarchical Linear Four Rate）

## 概念漂移理解（Concept Drift Understanding）

* **漂移發生的時間（When）**：檢測概念漂移的發生時間點，決定應對措施。
* **漂移嚴重程度（How）**：使用度量函式（如 KL Divergence、Competence Distance）衡量漂移幅度。
* **漂移影響範圍（Where）**：識別資料特徵空間中發生漂移的區域（如決策邊界變化）。

## 概念漂移適應（Concept Drift Adaptation）

#### (1) **模型重訓練（Retraining Models）**

* 直接使用新資料訓練新模型，替換舊模型。
* **Paired Learners** 方法：同時維護穩定模型和反應模型，根據變化更新模型。

#### (2) **整合學習（Ensemble Learning）**

* 適用於重現漂移，通過儲存歷史模型來應對重複出現的概念。
* **方法舉例：**
  * **Leveraging Bagging**（基於 ADWIN）
  * **Adaptive Random Forest (ARF)**
  * **DWM**（Dynamic Weighted Majority）

#### (3) **區域性模型更新（Model Adjustment）**

* 針對區域性區域漂移進行模型更新，例如：
  * **CVFDT**（Concept-adapting Very Fast Decision Tree）：對決策樹節點進行替換和剪枝。

## 評估方法與資料集

* **評估指標**
  * 預測準確率、Kappa 統計量（處理類別不平衡問題）、Prequential AUC。
  * 偵測準確性（如：真檢測率、假檢測率、檢測延遲）。
* **資料集**
  * **合成資料集（Synthetic Datasets）**：SEA、Hyperplane、STAGGER。
  * **真實資料集（Real-world Datasets）**：電商交易資料、股票市場資料、電信詐騙檢測資料。

## &#x20;未來研究方向

* **自適應學習方法**（Adaptive Learning Models）：開發更高效的概念漂移應對策略。
* **解釋性人工智慧（Explainable AI）**：讓概念漂移的決策更具可解釋性。
* **高維資料的概念漂移**：處理影像、語音等非結構化資料中的概念漂移。

## **資料漂移（Data Drift）**

定義：資料漂移指的是模型的輸入特徵可能會隨著時間而變化，這種變化可能導致模型性能下降，因為模型是基於舊的資料分佈進行訓練的。

舉例

* 房地產價格預測模型：原本的訓練資料中的房屋特徵分佈隨著時間發生變化，由於房屋越蓋越大，新的資料中房屋面積普遍變得更大，導致模型的預測失準。
* 社交媒體的情感分析模型：隨著新詞彙、表情符號和網路用語的出現，原本用來建立模型的數據和現有文本已經不同，這種語言使用演變就是資料漂移的一個例子。

檢測和處理：為了避免這個狀況，我們需要定期監控輸入數據的統計特性，或是定期重新訓練模型以適應新的數據分佈。

## **概念漂移（Concept Drift）**

定義：概念漂移指的是輸入特徵（X）與目標類別（Y）之間的映射關係發生變化，這種變化可能導致模型的預測規則不再有效，即使輸入數據的分佈保持不變。

舉例

* 音樂推薦系統：用戶的喜好可能隨時間而改變，例如，用戶的音樂品味隨年齡增長而變化，即使用戶的人口統計學特徵（輸入）沒有變化，但這些特徵與音樂喜好（輸出）的關係發生了變化。
* 以新冠疫情為例，疫情前後消費者的網購行為發生了巨大變化，這會影響基於過去消費行為建立的模型。

檢測和處理：為了處理這個問題，我們需要持續監控模型性能，也可以使用滑動窗口（sliding window）或加權樣本來強調最近數據。另外，也需要定期重新評估和更新特徵工程。

## 參考資料

* [Jie Lu et al. "Learning under concept drift: A review." _IEEE transactions on knowledge and data engineering,_  Vol. 31, No. 12 , pp2346-2363, 2018](https://arxiv.org/pdf/2004.05785).
* [João Gamaet al. "A survey on concept drift adaptation." ACM computing surveys (CSUR), Vol. 46, No..4 pp. 1-37, 2014](http://repositorio.inesctec.pt/bitstream/123456789/5370/1/P-009-DVX.pdf).
