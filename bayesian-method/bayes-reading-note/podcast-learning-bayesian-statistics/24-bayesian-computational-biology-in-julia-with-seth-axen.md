# #24 Bayesian Computational Biology in Julia, with Seth Axen

\[[youtube](https://www.youtube.com/watch?v=JLy6_twCUN0\&ab_channel=LearningBayesianStatistics)]

**Seth Axen 的背景和經歷**：

* 對數學和統計學充滿熱情，正在加州大學舊金山分校攻讀生物資訊學博士學位。
* 研究領域涵蓋計算生物學的各個方面，目前研究重點是推斷蛋白質結構。
* 積極參與開源發展，為 Julia 生態系統中的許多開源軟體包做出貢獻，尤其是 rv.jl（ArviZ 的 Julia 版本）。

**計算生物學和蛋白質結構**：

* 計算生物學利用電腦科學、數學和統計學來理解生物系統。
* 蛋白質是細胞中最重要的分子機器，其功能和互動取決於其三維結構。
* 研究蛋白質結構有助於瞭解其功能，並在藥物設計、疾病研究和蛋白質工程等領域具有應用價值。

**Seth Axen 的研究**：

* 他使用貝葉斯方法來推斷蛋白質結構，並開發了新的演算法和模型。
* 他的研究重點是建立能夠模擬蛋白質結構分佈的模型，而不僅僅是單個結構。
* 他使用各種資料型別，例如核磁共振資料，來推斷蛋白質結構的相關距離和相對方向。

**Julia 和機率程式設計**：

* Seth Axen 是 Julia 語言的擁護者，並認為它在開發效率和效能方面具有優勢。
* 他喜歡 Julia 的通用性和多分派特性，這使得不同的軟體包可以輕鬆地組合在一起。
* 他使用 Julia 來實現自動微分，這是機率程式設計和機器學習中的關鍵技術。

**rv.jl**：

* rv.jl 是 ArviZ 的 Julia 版本，ArviZ 是一個用於分析和診斷機率模型的 Python 包。
* rv.jl 讓 Julia 開發者能夠使用 ArviZ 的功能，例如標準資料格式、標準分析和有用的圖表。
* rv.jl 的優勢在於其易用性和與其他 Julia 包的相容性，但其弱點在於它實際上是 Python 包的包裝器，這可能會導致一些相容性問題。

**自動微分**：

* 自動微分是一種計算函式導數的技術，它比手動微分或符號微分更有效率和準確。
* 自動微分是動態哈密頓蒙特卡羅（HMC）等機率程式設計技術的關鍵，HMC 需要計算對數機率的梯度。
* Seth Axen 喜歡自動微分，因為它讓開發者能夠輕鬆地計算導數，而無需擔心數值穩定性和效率問題。

**訪談結束前的問答**：

* Seth Axen 表示，如果他有無限的時間和資源，他會致力於使數值積分像自動微分一樣容易，從而開拓新的研究領域。
* 他最想與阿蘭·圖靈共進晚餐，因為圖靈是電腦科學和機率論的先驅，並且對貝葉斯方法的發展做出了貢獻。
