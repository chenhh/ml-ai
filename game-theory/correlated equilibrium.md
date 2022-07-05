# 相關均衡(correlated equilibrium)

## 簡介

在現實生活中，當人們遇到多個納什均衡選擇困難時，特別是在長期反復遇到類似問題時，人們往往通過收集更多的資訊，形成特定的機制和規則來解決問題，從而找到自己的出路。通過這一概念，Aumann首次提出了賽局中的相關均衡。<mark style="color:red;">賽局者之間長期互動的性質表明，賽局的不同階段是相互依存的，這使得理性的賽局者的決定不僅受到他們過去經驗的影響，而且還受到可能的未來的影響</mark>。如果賽局中的參與者可以<mark style="color:blue;">根據一個共同的觀察信號</mark>，相關的均衡就可能出現。

在相關均衡的定義中，它假設玩家對狀態發生的機率有共同的信念。

> 定義：相關均衡
>
> 靜態賽局$$\Gamma=(\mathcal{N}, (\mathcal{A}_i)_{i \in \mathcal{N}}, (u_i)_{i \in \mathcal{N}})$$中，定義於行動方案集合$$\mathcal{A}$$的機率分佈$$\phi$$稱為相關均衡，若$$\phi$$滿足以下條件：
>
> * 對所有的玩家$$i \in \mathcal{N}$$, 所有玩家的行動$$j,k\in \mathcal{A}_i$$
> * $$\displaystyle \sum_{\{\mathbf{a} \in \mathcal{A} ~|~ a_i =j\}}\phi(\mathbb{a})(u_i(k, \mathbf{a}_{-i})- u_i(\mathbf{a})) \leq 0$$

納許均衡對應於$$\phi$$是乘法度量的特殊情況，也就是說，相關均衡中的觀察信號是獨立產生的。因為混合策略納許均衡作為一種穩定狀態，其中每個參與者的行動取決於他從環境中重新獲得的信號。因此，這些信號是私人的、獨立的。

根據納許均衡是相關均衡的一個特例的結論，混合策略納什均衡存在於有限靜態賽局中，那麼相關均衡也存在於有限靜態賽局中。相關均衡的存在也可以擴展到無限賽局，包括無限的玩家和無限的行動。

## 參考資料

* <mark style="background-color:red;">Aumann, Robert J. "Subjectivity and correlation in randomized strategies." Journal of mathematical Economics 1.1 (1974): 67-96</mark>.
