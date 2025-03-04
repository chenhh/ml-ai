# #13 Building a Probabilistic Programming Framework in Julia, with Chad Scherrer

這次訪談主要圍繞 Julia 程式語言在機率程式設計領域的應用，特別是 Chad Scherrer 開發的 Sauce 套件。以下是一些重點：

**Julia 的特點**：

* **模組化**： Julia 的套件之間可以很容易地混合和匹配，而不會有效能損失。
* **速度**： Julia 的 JIT 編譯和多型性使得它可以實現與低階語言相媲美的效能。
* **易學性**： Julia 的語法與 Python、C 和 Java 等主流語言相似，學習曲線相對平緩。

**Julia 的機率程式設計生態系統**：

* **Sauce**： Chad Scherrer 開發的輕量級機率程式設計套件，使用宣告式語法，並且與 Julia 的其他套件很好地整合。
* **Turing**： 另一個流行的 Julia 機率程式設計套件，提供 HMC 等推理演算法。
* **Gen**： MIT 開發的 Julia 機率程式設計套件，採用與 Sauce 相似的方法，將模型與推理分離。
* **Omega 和 Puo**： 其他 Julia 機率程式設計專案，分別採用抽象解釋和自動微分的 approach。
* **Steno**： 基於高斯過程的機率程式設計語言，與 Sauce 有潛在的整合空間。

**Sauce 的核心選擇和挑戰**：

* **宣告式語法**： Sauce 使用宣告式語法，這使得它可以靜態地分析模型，並生成優化後的程式碼。
* **模型與推理分離**： Sauce 將模型定義與觀察資料分離，這使得它可以更靈活地進行前向采樣和後驗預測。
* **程式碼生成**： Sauce 使用 SymPy 進行符號操作，並生成優化後的程式碼，以提高效能。
* **推理原語**： Sauce 提供了推理原語，例如生成隨機樣本和計算對數密度，這些可以與不同的推理演算法一起使用。

**Sauce 的未來發展**：

* **完善文件和測試**： Chad 希望 Sauce 能夠像 Stan 和 PyMC3 一樣擁有完善的文件和測試。
* **與其他 Julia 機率程式設計套件整合**： Chad 希望 Sauce 能夠與 Turing、Gen 等其他 Julia 機率程式設計套件更好地整合。
* **在 Relational AI 的應用**： Chad 希望 Sauce 的思想能夠在 Relational AI 的工作中得到應用。

**總結**：

Julia 是一種很有潛力的機率程式設計語言，Sauce 套件為 Julia 的機率程式設計生態系統做出了重要貢獻。Chad Scherrer 和他的同事們正在努力完善 Sauce，並探索其在不同領域的應用。
