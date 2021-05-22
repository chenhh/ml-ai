---
description: 'online tw: 線上, cn:在線'
---

# 線上凸最佳化

## 簡介

online convex optimization與game theory中的external regret, internal regret以及information theory中的universal portfolio的概念均有相關, 但是特別強化了對於一般化問題的最佳化方法。

在許多實際應用中，環境非常的復雜，以至於制定一個全面的理論模型並使用經典的演算法理論和數學最佳化通常是不可行的。因此採取穩健的方法是必要且有益的，即通過應用一種邊走邊學的最佳化方法，隨著問題的更多資料被觀察到，從經驗中學習。

## 線上凸最佳化模型（The online convex optimization model）

線上凸最佳化中，一個線上玩家迭代地（多期）做出決定。而在每一期做決定時，與選擇相對應的結果對玩家來說是未知的（選擇之後，才知道報酬/ 損失）。

在每一期作出決定後，玩家（決策者）會遭受損失：每個可能的決定都會產生一個（可能不同的）損失。這些損失對決策者來說是事先未知的。損失可以是對抗性選擇，甚至取決於決策者採取的行動。

因此為了使上述的決策框架合理有意義，以下兩個限制是必要的：

* 不允許對手給予玩家的損失是沒有界限的。否則，對手可以不斷增大玩家每次決定（行動）的損失規模，而無法使演算法從第一次決策的損失中恢復過來。**因此，我們假設損失位於某個有界的區域**。
* **決策集（行動集）必須有一定的界限和/或結構**，盡管不一定是有限的。  為了理解為什麼這一點是必要的，請考慮具有無限可能的決策集。對手可以無限期地給玩家選擇的所有策略分配較高損失，而把一些損失為零的策略分開。因此玩家不管怎麼選定決策，損失都會不斷擴大。

令人驚訝的是，有趣的結果和演算法可以在不超過這兩個限制的情況下得出。

線上凸最佳化（online convex optimization, OCO）







## 參考資料

* \[\*\*\*\]Elad Hazan, "Introduction to online convex optimization." arXiv preprint arXiv:1909.05207 \(2019\).
* Nicolo Cesa-Bianchi and Gabor Lugosi. Prediction, Learning, and

  Games. Cambridge University Press, 2006.

* S. Boyd and L. Vandenberghe. Convex Optimization. Cambridge

  University Press, March 2004.

