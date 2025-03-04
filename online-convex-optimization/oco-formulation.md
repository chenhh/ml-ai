# OCO架構與常見應用

## 簡介

賽局理論中，雙人零和賽局，且報酬為向量時，Blackwell approachability性質可使用OCO建模。而此性質也可用資訊理論描述。

online learning(包含classification與regression)均可使用OCO建模。

如果考慮相對誤差(遺憾, regret)，即和專家群中最佳的專家比較性能而不考慮絕對誤差時，存在演算法可保證在不知道那一個專家表現最好時，演算法和此最佳專家的遺憾會收斂至0。

### 常見應用

* \[分類]Prediction from expert advice(根據專家建議進行預測)
* \[分類]Online spam filtering(在線垃圾郵件過濾)
* \[迴歸]Online shortest paths(在線最短路徑)
* \[迴歸]online portfolio selection(在線投資組合選擇)
* \[迴歸]Matrix completion and recommendation systems(矩陣補全與推薦系統)

## 架構

OCO為玩家與對手的雙人零和賽局，但有一些限制避免無法分析的特殊情形。

* 在時間$$t=1,2,\dots, T$$，玩家(player)給出行動$$\mathbf{w}_t \in \mathcal{K}$$，其中$$\mathcal{K}$$為<mark style="color:red;">凸集合</mark>。
  * 此處的行動如果是使用演算法$$\mathcal{A}$$參考已實現損失所得出時，可寫成：$$\mathbf{x}_t^{\mathcal{A}}=\mathcal{A}(f_1, \dots, f_{t-1}) \in \mathcal{K}$$
* 對手(adversary)選擇<mark style="color:red;">凸損失函數</mark>$$f_t(\cdot): \mathcal{K} \rightarrow \mathbb{R}$$(有限損失)，之後玩家可得到損失$$f_t(\mathbf{w}_t)$$。有時也使用$$l_t(\cdot)$$。

玩家的目標是最小化遺憾：$$\displaystyle R(T) = \sum_{t=1}^T f_t(\mathbf{w}_t) - \min_{\mathbf{w} \in \mathcal{K}} \sum_{t=1}^T f_t(\mathbf{w})$$

