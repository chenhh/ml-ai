# OCO架構與常見應用

賽局理論中，雙人零和賽局，且報酬為向量時，Blackwell approachability性質可使用OCO建模。而此性質也可用資訊理論描述。

online learning(包含classification與regression)均可使用OCO建模。

如果考慮相對誤差(遺憾, regret)，即和專家群中最佳的專家比較性能而不考慮絕對誤差時，存在演算法可保證在不知道那一個專家表現最好時，演算法和此最佳專家的遺憾會收斂至0。

### 常見應用

* \[分類]Prediction from expert advice(根據專家建議進行預測)
* \[分類]Online spam filtering(在線垃圾郵件過濾)
* \[迴歸]Online shortest paths(在線最短路徑)
* \[迴歸]online portfolio selection(在線投資組合選擇)
* \[迴歸]Matrix completion and recommendation systems(矩陣補全與推薦系統)
