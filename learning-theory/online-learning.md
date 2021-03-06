# 在線學習\(online learning\)

## 簡介

傳統機器學習中的分類演算法，如支持向量機（SVMs）算法，大都是在批次學習模式下設計的，即假設學習前擁有全部訓練樣本且可以通過一次學習得到最終決策模型。但實際中如果數據集過大不能一次性處理或是僅因為新資料的到達而要放棄以前的學習成果，重新對全部資料進行學習，將會耗費大量的時間和空間資源。

線上學習模式下，樣本是以順序方式接收的。在每輪中演算法先對當前樣本進行類別預測，當接收到真實類別後，該演算法再選擇是否預測機制進行更新。

## constant rebalanced portfolio \(CRP\)

資產增長模型，於1956年由美國貝爾實驗室的 Kelly提出，旨在研究長期中使資產增長速度最快的最優投資比例，即最優增長路徑問題，開始了動態研究投資組合問題。

1991年，基於Kelly的增長策略 \(Constant Rebalanced Portfolio, CRP\)，Cover在對未來價格分佈不做任何假定的情況下提出了泛證券投資組合策略，強調每一天根據股市變化來調整組合內各證券的投資比例，投資者可以獲取漸進於最優的\(best constant rebalanced portfolio, BCRP\)的收益率。

它是一種主動的、線上的投資策略，投資比例隨著過去行情變化而改變。同時，考慮市場出現最壞的情形，因此，該投資策略代表投資者的類型是風險極端厭惡型。儘管Cover提出的泛證券投資組合理論具有很強的理論指導意義，但由於其對證券市場不做任何限制，也不考慮或甚少考慮任何其它信息，所以在實驗研究中發現收益並不高。

Cover將線上金融問題和線上理論方法相結合，以最終財富的增長倍數最大化為目標，提出universal portfolio，建立了一種泛證券投資組合選擇模型。

由於不存在可以不斷真實地模擬實際證券市場的證券價格模型，Cover 就摒棄了證券市場上的證券價格所遵循的任何模型，充分利用證券的歷史價格資訊，通過在線學習的方法來逐步優化投資組合策略，進而達到或者接近於最大的投資收益。



#### 參考資料

* J. L. Kelly, "A new interpretation of information rate," Information Theory, IRE Transactions on, vol. 2, pp. 185-189, 1956.
* T. M. Cover, "Universal portfolios," Mathematical finance, vol. 1, pp. 1-29, 1991.







