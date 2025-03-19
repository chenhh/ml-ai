---
description: >-
  Vianney Perchet,  "Approachability, regret and calibration; implications and
  equivalences." arXiv preprint arXiv:1301.2663, 2013.
---

# 可接近性-遺憾-校準與等價問題

## 摘要

Blackwell可接近性、遺憾最小化和校準是評估一個策略（或算法）在不同序貫決策問題或玩家與自然之間重複賽局中的三個標準。雖然乍看之下它們似乎毫無關聯，但已經發現了它們之間的聯繫：一致且校準的策略都可以通過在某個輔助賽局中遵循可接近性策略來構造。我們收集了著名或最新的結果，並提供了新的結果，以發展和推廣Blackwell的優雅理論。最終目標是展示如何將其作為一個基本的強大工具，用於展示一類基於簡單幾何屬性的直觀新算法。為了完整起見，我們還證明了可接近性可以被視為一致或校準策略存在的副產品。

註：這是survey論文，整理了很多文獻和討論，數學量非常大，很值得精讀。

## 簡介

<mark style="color:red;">序列決策問題可以表示為玩家與自然（Nature）之間的重複賽局</mark>。在每個階段，玩家（根據上下文也稱為代理、決策者或預測者）從其決策集中選擇一個元素。同時，自然也會選擇一個世界狀態。這些選擇序列生成了一個結果序列，並為玩家帶來總體收益。

對手被稱為「自然」，因為我們不具體說明她的收益、目標或理性；我們對她的行為不做任何假設，未來的世界狀態無法從過去推斷。通常，環境不是隨機或貝氏式的，而是對抗性的；例如，自然可能代表一個惡意的對手，或者一組獨立（或相關）的玩家。<mark style="color:red;">這些模型的一個關鍵要求是，玩家的策略必須對於所有可能的世界狀態序列（或簡單來說，對於自然的所有策略）都是有效的（即滿足某些外生標準）</mark>。

根據結果對應的結構，玩家的總體目標可能會有所不同。Hannan \[30] 研究了這樣的情況：結果實際上是一個真實的收益值。玩家的目標是最大化其平均（或累積）收益。由於我們對自然的行為不做任何假設，玩家無法保證某個外生收益值，這與傳統的零和賽局不同，在零和賽局中收益值是可以保證的。例如，假設自然決定在玩家採取任何行動的情況下，每次都給玩家收益為零（或其他固定值），那麼玩家無法確保特定收益。

<mark style="color:red;">Hannan 引入的準則稱為</mark><mark style="color:red;">**遺憾值（regret）**</mark> ，<mark style="color:red;">它衡量的是玩家獲得的平均收益與如果玩家一直選擇相同行動所獲得的收益之間的差異</mark>。這與凸優化有關（如果自然反覆選擇相同的損失函式），更確切地說，與線上凸優化相關。Hannan \[30] 的主要成果是，存在一種一致的策略（即無遺憾的策略），並且他構造了一種這樣的策略。這一成果後來通過不同的技術和思想得到了廣泛改進和提升，特別是由 Foster & Vohra \[23]、Hart & Mas-Colell \[31]、Fudenberg & Levine \[28]、Lehrer \[43]、Auer, Cesa-Bianchi & Gentile \[3]、Cesa-Bianchi & Lugosi \[14]、Sorin \[71] 等人進一步發展。

當結果是向量收益（而非標量收益）時，問題與多目標優化密切相關，每個坐標代表一個不同的子目標。Blackwell \[9] 提出了一個新概念，而不是考慮某些外生的凸組合目標或按特定順序優化這些目標（將此框架納入前述框架）。他假設有一個目標集合，玩家的目標是使平均結果收斂到該集合；相反，自然試圖將其推離。形式上，一個給定的閉集是可接近的，如果玩家有一個策略，使得在某個可能很大的階段後，平均收益始終任意接近這個目標集合，無論自然的移動序列如何。

Blackwell 的可接近性理論非常優雅，因為它依賴於簡單的幾何性質。這些性質使他能夠明確表徵可接近的凸集，並為非凸集提供了一個簡單的充分條件（這些集合被稱為 <mark style="color:red;">B-集合</mark>，以 Blackwell 命名）。Spinat \[73] 後來證明，這幾乎是一個必要條件。

這一理論的首次重要應用歸功於 Kohlberg \[39]。他使用這一簡單工具，為 Aumann 和 Maschler \[5] 提出的不完全資訊零和賽局中的未知情玩家構造了一個最優策略（更多細節可參考 Mertens, Sorin & Zamir \[55] 及相關文獻）。可接近性理論近年來也引起了賽局論和機器學習社群的廣泛興趣，相關工作包括 Vieille \[77]、Hart & Mas-Colell \[32]、Spinat \[73]、Lehrer \[42]、Benaïm, Hofbauer & Sorin \[7]、Mannor & Shimkin \[49]、Lehrer & Solan \[44, 46]、As Soulaimani, Quincampoix & Sorin \[2]、Mannor & Tsitsiklis \[53]、Perchet \[60, 61]、Rakhlin, Sridharan & Tewari \[66]、Perchet & Quincampoix \[63] 等。

另一個（也是最後一個在此討論的）準則是<mark style="color:red;">校準（calibration）</mark>，由 Dawid \[16] 在此框架下提出，並由 Foster & Vohra \[24]、Fudenberg & Levine \[27]、Lehrer \[41]、Sandroni, Smorodinsky & Vohra \[68]、Sorin \[71]、Perchet \[60]、Foster, Rakhlin, Sridharan & Tewari \[22] 等人進一步擴充套件。

在這裡，階段結果不是某種收益（無論是標量還是向量），而是自然選擇的世界狀態。<mark style="color:red;">玩家的總體目標是依次預測整個狀態序列，使得平均預測值與狀態的經驗分佈漸近地任意接近。</mark>在沒有其他限制的情況下，這其實相當容易：只需在某個階段預測前一階段的結果即可。

額外的要求可能是，例如，預測只能屬於某個有限（但可能很大）的集合，並且在進行特定預測的階段集合上，狀態的經驗分佈比其他任何可能的預測更接近該預測。一個常見的例子是氣象學家每天預測第二天降雨的機率。預測值屬於 0%、10%、20% 等，並且要求當氣象學家說降雨機率為 30% 時，實際降雨的平均次數應在 35% 到 45% 之間。

<mark style="color:red;">Oakes \[57] 和 Dawid \[17] 證明，任何確定性演算法都不可能實現校準（儘管這一強烈結論值得討論），而隨機演算法則可以實現</mark>，如 Foster & Vohra \[24] 所證明的。這種演算法的存在可以被視為一個負面結果，因為它表明一個非專業的戰略性氣象學家可以模仿專家（知道真實底層過程的人，如果存在）。大量文獻研究了這一問題，最近的成果匯總在 Olszewski \[58] 的綜述中。另一方面，這也可以被視為一個正面結果，因為它表明自然的長期行為可以漸近地預測，這可能引導另一類演算法和成果，如 Foster & Vohra \[23] 或 Perchet \[59, 62]。

<mark style="color:red;">**遺憾最小化和校準的一個共同特點是，它們可以被寫成某種輔助向量收益賽局中精心選擇的目標集合的可接近性問題的特殊情況。**</mark>最早注意到這一性質的是 Blackwell \[10]（這一想法已經在 Hannan \[30] 的開創性論文中提到，或在 Luce & Raiffa \[48] 中提到），然後由 Foster \[21]、Hart & Mas-Colell \[32]、Lehrer & Solan \[45]、Sorin \[71]、Perchet \[60]、Mannor & Stoltz \[50]、Abernathy, Barltlett & Hazan \[1] 等人進一步發展。

我們隱含地假設玩家觀察到世界狀態的序列；這實際上是一個關鍵假設，有時被稱為完全監控。特別是，我們不會考慮部分監控（或強盜問題）或隨機賽局（例如，整個結果序列可能取決於某個階段的單一選擇）。這些也是有趣的主題，但超出了本文的範圍。

***

**重點整理**

1. **序列決策問題與重複賽局**
   * 序列決策問題可建模為玩家與自然之間的重複賽局。
   * 在每個階段，玩家（根據上下文也稱為代理、決策者或預測者）從其決策集中選擇一個行動，而「自然」則選擇一個世界狀態。
   * 「自然」的行為沒有任何假設，未來的狀態無法從過去推斷，且環境通常是非隨機的、對抗性的（例如，可能代表一個惡意對手或多個獨立或相關的玩家）。
   * 玩家的策略必須對抗任何可能的世界狀態序列（或「自然」的任何策略）都表現良好。
2. **Hannan 的遺憾值理論**
   * Hannan 研究了玩家目標是最大化平均（或累積）收益的情況。
   * 由於對「自然」的行為沒有假設，玩家無法保證獲得特定的收益（與傳統零和賽局不同）。遺憾值衡量玩家獲得的平均收益與最佳固定策略收益之間的差距。
   * 這與凸優化（特別是線上凸優化）相關。
   * Hannan 證明了無遺憾策略的存在性，並構造了一種實現方法。
3. **Blackwell 的可接近性理論**
   * 當結果是向量收益時，問題與多目標優化相關。
   * Blackwell 引入了「可接近性」（approachability）的概念，玩家的目標是使平均收益收斂到某個目標集合，而「自然」則試圖將其推離。
   * 可接近性理論基於簡單的幾何性質，Blackwell 明確描述了可接近的凸集，並提供了非凸集（B-集）的簡單充分條件。
4. **校準理論**
   * 校準衡量玩家的預測是否與實際結果的經驗分佈一致。
   * 校準問題中，玩家的目標是預測「自然」選擇的世界狀態序列，使得預測的平均值與狀態的經驗分佈漸近接近。
   * Oakes 和 Dawid 證明不存在確定性的校準演算法，但 Foster 和 Vohra 證明隨機演算法可以實現校準。
   * 這可以被視為負面結果（非專家可以模仿專家），也可以被視為正面結果（「自然」的長期行為可以被預測）。
5. **遺憾最小化與校準的聯絡**
   * 遺憾最小化和校準都可以寫為某種輔助向量收益賽局中的可接近性問題。
   * 本文假設玩家可以觀察到世界狀態序列（完全監控），未考慮部分監控或隨機賽局等更複雜的情況。
6. **完全監控假設的重要性**
   * 玩家需要觀察到世界狀態的完整序列，這是理論成立的關鍵假設。
   * 部分監控或隨機賽局的情況不在本文討論範圍內。



## 參考資料

* \[Perchet13] Vianney Perchet,  "[Approachability, regret and calibration; implications and equivalences](https://arxiv.org/abs/1301.2663)." arXiv preprint arXiv:1301.2663, 2013.
* \[Abernethy11] Jacob Abernethy, Peter L. Bartlett, and Elad Hazan. "[Blackwell approachability and no-regret learning are equivalent](https://proceedings.mlr.press/v19/abernethy11b.html)," Proceedings of the 24th Annual Conference on Learning Theory. JMLR Workshop and Conference Proceedings, 2011.
* \[Foster99] Dean P. Foster,  "A proof of calibration via Blackwell's approachability theorem," Games and Economic Behavior, Vol. 29, No. 1-2, pp. 73-78, 1999.
* \[Dann24] Christoph Dann et al. "[Rate-preserving reductions for blackwell approachability](https://arxiv.org/abs/2406.07585)." arXiv preprint arXiv:2406.07585, 2024.
* [https://stephofx.github.io/2023/02/17/blackwell-approachability-theorem.html](https://stephofx.github.io/2023/02/17/blackwell-approachability-theorem.html)
