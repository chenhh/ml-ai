# 透過預測可接近性加快賽局求解速度

## 摘要

**Blackwell可接近性框架**\
Blackwell可接近性是一種用於分析具有向量值收益的重複賽局的理論框架。本文引入了「預測性Blackwell可接近性」，其中決策者根據對下一個收益向量的估計來調整策略，從而基於估計的準確性提升效能。

**四種演算法之間的聯絡**\
研究揭示了四種常見演算法之間的重要關聯：

* **FTRL（Follow-the-regularized-leader）** 和 **OMD（Online Mirror Descent）** 是線上凸優化中最常用的遺憾最小化演算法。
* **RM（Regret Matching）** 和 **RM+（Regret Matching+）** 則是在大規模賽局求解中被廣泛使用的演算法（特別是在反事實後悔最小化框架中作為區域性後悔最小化器）。\
  本文證明，RM和RM+分別是通過執行FTRL和OMD來選擇在Blackwell可接近性賽局中需要強制的半空間所得到的結果。

**預測性演算法的提出**\
基於上述聯絡，研究將FTRL和OMD的預測變體應用於Blackwell可接近性框架，提出了「預測性Blackwell可接近性演算法」以及RM和RM+的預測變體。

**實驗結果**\
在18個常見的零和擴充套件形式基準遊戲中進行實驗，結果表明：結合預測性RM+與反事實後悔最小化（CFR）的演算法在大多數遊戲中收斂速度遠快於現有的最快演算法（如CFR+、DCFR、LCFR），除了兩個撲克遊戲外，有時快達兩個數量級以上。

***

#### 核心貢獻：

* 提出了預測性Blackwell可接近性框架，並展示了如何利用收益向量的估計來提升賽局中的效能。
* 揭示了FTRL、OMD與RM、RM+之間的理論聯絡，為設計新演算法提供了基礎。
* 實驗驗證了預測性RM+的高效性，特別是在大規模零和賽局中的快速收斂能力。

**總結** ：這項研究不僅深化了對Blackwell可接近性理論的理解，還通過引入預測性方法顯著提升了賽局求解的效率，為人工智慧在賽局論中的應用提供了新的工具。

## 參考資料

Gabriele Farina, Christian Kroer, and Tuomas Sandholm. "[Faster game solving via predictive blackwell approachability: Connecting regret matching and mirror descent](https://ojs.aaai.org/index.php/AAAI/article/view/16676)." _Proceedings of the AAAI Conference on Artificial Intelligence_. Vol. 35. No. 6. 2021.
