---
description: online convex optimization, oco
---

# 在線凸最佳化相關資料

## 論文

* Martin Zinkevich, "Online convex programming and generalized infinitesimal gradient ascent," In Proceedings of the 20th International Conference on Machine Learning, Washinton DC, pp. 928–936, 2003. \[第一篇定義OCO架構的論文]
* Leo Breiman, " Statistical modeling: The two cultures (with comments and a rejoinder by the author), " Statistical science, Vol. 16, No. 3, pp. 199-231, 2001.\[比較了數據建模的兩種文化：數據模型文化（基於假設分佈）和算法模型文化（基於預測性能）。Breiman 主張算法模型（如隨機森林）在複雜數據中更具優勢，強調預測準確性而非模型解釋性，並呼籲統計學界更重視算法模型的研究與應用。]



regret

* Blum, Avrim, and Yishay Mansour. "From external to internal regret." Journal of Machine Learning Research 8.6 (2007).
* Dagan, Yuval, et al. "From External to Swap Regret 2.0: An Efficient Reduction for Large Action Spaces." Proceedings of the 56th Annual ACM Symposium on Theory of Computing. 2024.
* Peng, Binghui, and Aviad Rubinstein. "Fast swap regret minimization and applications to approximate correlated equilibria." _Proceedings of the 56th Annual ACM Symposium on Theory of Computing_. 2024.
* Arunachaleswaran, Eshwar Ram, Natalie Collina, and Jon Schneider. "Learning to Play Against Unknown Opponents." _arXiv preprint arXiv:2412.18297_ (2024).

### survey

* Shai Shalev-Shwartz, "[Online learning and online convex optimization](https://www.cs.huji.ac.il/~shais/papers/OLsurvey.pdf)," Foundations and Trends in Machine Learning, Vol. 4 No. 2, pp. 107–194, 2011.
* Elad Hazan,  "A survey: The convex optimization approach to regret minimization," In Suvrit Sra, Sebastian Nowozin, and Stephen J. Wright, editors, Optimization for Machine Learning, pp. 287–302. MIT Press, 2011.
* Elad Hazan, "Introduction to online convex optimization, MIT Press, 2022 \[[arxiv](https://arxiv.org/abs/1909.05207)].

## 研究團隊

* [Elad Hazan, Princeton University](https://www.ehazan.com/).
  * Follow The Leader and Mirror Descent: Equivalence Theorems and L1 Regularization：由 Hazan 和 Kale 提出，深入探討了 Follow The Leader (FTL) 和 Mirror Descent 演算法之間的等價關係，並提出了 FTRL 演算法的框架。FTRL 演算法及其變體已成為許多現代機器學習和線上優化方法的核心。
  * Efficient Learning: Algorithms, Theory, and Online Experiments：由 Hazan 合著的書籍，全面介紹了線上凸優化、遺憾最小化和相關演算法的理論與應用。
* [Shai Shalev-Shwartz, The Hebrew University of Jerusalem](https://www.cs.huji.ac.il/~shais/).
* [張利軍(Lijun Zhang), 南京大學](https://cs.nju.edu.cn/zlj/index.htm).
* [趙鵬(Peng Zhao), 南京大學](https://www.lamda.nju.edu.cn/zhaop/?AspxAutoDetectCookieSupport=1).
* [Martin Zinkevich, google](https://martin.zinkevich.org/). 在2003年提出了線上凸優化中的後悔最小化算法，為線上學習領域奠定了基礎。
* Peter Auer、Nicolo Cesa-Bianchi 和 Paul Fischer：在2002年發表了關於多臂賭徒問題的論文，提出了上置信界（UCB）算法，這是後悔最小化在強化學習中的重要應用。
* Xu-Hui Liu：在2021年提出了在離線策略強化學習中應用後悔最小化的經驗回放方法，為強化學習中的經驗重用提供了新思路。Liu, X.-H., Xue, Z., Pang, J.-C., Jiang, S., Xu, F., & Yu, Y. (2021). Regret Minimization Experience Replay in Off-Policy Reinforcement Learning. arXiv preprint arXiv:2105.07253.
* Raymond Chi-Wing Wong 團隊 該團隊在資料庫和資料探勘領域有深入研究，特別是在多目標決策和後悔最小化查詢演算法方面提出了多項重要成果。團隊成員包括 Min Xie 等，發表了多篇關於後悔最小化演算法的高水平論文，例如在 SIGMOD、VLDBJ 等頂級會議和期刊上的工作
  * Strongly Truthful Interactive Regret Minimization，提出了一種強真實性的互動式後悔最小化演算法，適用於高維資料環境。
* Ioannis Anagnostides 團隊 該團隊專注於賽局理論和線上學習中的後悔最小化問題，特別是在計算下界和均衡收斂性方面有重要貢獻。其研究涉及稀疏相關均衡的計算複雜性和後悔最小化演算法的最佳化
  * Computational Lower Bounds for Regret Minimization in Normal-Form Games：探討了正規形式賽局中後悔最小化演算法的計算下界，證明了現有演算法（如乘性權重更新）的接近最優性。
* Kai Li 團隊 該團隊致力於不完美資訊賽局中的反事實後悔最小化（CFR）演算法研究，提出了 AutoCFR 框架，通過元學習和進化演算法自動設計高效的 CFR 變體，顯著提升了演算法的收斂速度和通用性
