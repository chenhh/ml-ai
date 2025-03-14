---
description: goal and reward
---

# 目標與報酬

短期報酬$$R_t$$與累積報酬$$G_t$$，會影響到問題目標學習時的的行為$$\pi(a|s)$$的選擇。

## 目標與報酬(goal and rewards)

在強化學習中，代理人的目的或目標是以一種特殊的訊號（稱為獎賞）形式化的，從環境傳遞到代理人。在每個時間步驟中，獎勵是一個簡單的數字$$R_t \in \mathbb{ R}$$。<mark style="color:red;">這意味著最大化的不是眼前的獎勵，而是</mark><mark style="color:red;">**長期的累積獎勵**</mark><mark style="color:red;">。我們可以把這個非正式的想法清楚地表述為獎勵假說(reward hypothesis)</mark>。

> 強化學習的核心思想是尋找**最優策略**$$\pi^{*}$$，使得在任意狀態下，代理的長期累積獎勵最大化。
>
> $$\displaystyle \pi^{*}=\argmax_{\pi} \mathrm{E}(\sum_{t=0}^\infty \gamma^t r_t)$$

使用獎勵訊號來正式確定目標的想法是強化學習的最顯著特徵之一。

獎勵的定義不僅描述了「成功」的標準，也自然而然地將代理人的行動與結果連結起來。

### 獎勵作為訓練的目標的重要原因

* **提供行動的評價訊號與明確的目標** ：獎勵提供了一個明確的目標，使代理人（Agent）能夠知道哪些行動（Actions）是有益的，哪些是有害的。通過最大化累積獎勵，代理人可以學習到最優的策略（Policy），以在特定環境中取得最佳的表現。<mark style="color:red;">我們設定的獎勵要真正表明我們想要完成的事情</mark>。
  * **正獎勵**：鼓勵代理採取有助於目標的行動。
  * **負獎勵**：懲罰代理採取有害於目標的行動。
  * 獎勵訊號是你向機器人傳達你希望它實現什麼的方式，而不是你希望它如何實現。
  * 例如，下棋的代理人應該只因實際獲勝而得到獎勵，而不是因實現諸如拿走對手的棋子或獲得棋盤中心的控制權等次級目標而得到獎勵。對於一個學習下跳棋或國際象棋的代理人來說，自然的獎勵是贏了+1，輸了-1，平局和所有非終端位置都是0。
  * 例如，為了讓機器人學會走路，研究人員在每個時間步驟上提供與機器人向前運動成比例的獎勵。在讓機器人學習如何從迷宮中逃脫時，獎勵往往是在逃脫前的每一個時間步驟中都是-1；這鼓勵代理人盡可能快地逃脫。
* **反饋機制**：獎勵提供了一種反饋機制，使代理人能夠根據環境的反饋來調整其策略。當代理人選擇一個行動後，環境會根據該行動的結果給出一個獎勵值。代理人可以根據這個獎勵值來評估其行動的優劣，並進行策略調整。
* **長期優化(延遲反饋)**：獎勵不僅考慮當前的報酬，還考慮未來的報酬(代理當前的一個動作可能需要多步之後才能看到效果。)。通過使用累積獎勵作為目標，代理人可以進行長期優化，以最大化總體報酬。這種長期視角有助於代理人學習到更加穩定和可靠的策略。
* **易於處理稀疏性和長期目標**：在許多工作中，獎勵可能是稀疏的（例如遊戲中只有在勝利時才有獎勵），但強化學習可以利用時間差分方法（TD Learning）等技術來學習延遲獎勵的價值，逐步逼近目標。
* **探索與利用的平衡**：代理人需要在探索新的行動和利用已知的高報酬行動之間找到平衡。通過獎勵機制，代理人可以在探索新策略的同時，也能夠利用已知的高報酬策略，從而達到更好的表現。
* **可擴充性**：獎勵機制具有很好的可擴充套件性，可以應用於各種不同的問題和環境中。無論是在簡單的環境中，還是在複雜的環境中，獎勵機制都能有效地指導代理人學習和優化策略。
* **生物學啟發**：類似於生物的學習機制（大腦獎勵系統）。模仿了自然界中的學習過程，正向強化有助於形成期望的行為模式。

## MDP 的限制

* 無法處理非上帝視角的問題：我們生活的世界中，有很多東西是我們還無法觀測到的（比如人內心的想法、比如宇宙中的暗物質），所以我們無法描述這世界的真實狀態，這種問題就由更進階的 Partially Observable Markov Decision Processes 來嘗試建模。
* 只考慮到報酬，沒考慮到採取行動的成本(cost)：我們在採取行動時，除了會考慮獲得的報酬，也會考慮付出的代價。

## 回合(episode or trial)與連續任務

<mark style="color:red;">代理人的目標是使其在長期內獲得的累積獎勵最大化</mark>。

| 因素        | 回合性任務(有限期數)                | 持續性任務(無限期數)             |
| --------- | -------------------------- | ----------------------- |
| 問題是否有自然終點 | 有明確終點，適合回合性任務。             | 沒有明確終點，適合持續性任務。         |
| 需要長期最佳化嗎？ | 通常最佳化每一集的回報，但對長期策略可能不敏感。   | 最佳化長期回報，適合持續性最佳化需求的任務。  |
| 計算複雜性     | 每次模擬可以通過終止狀態重設，較容易控制計算複雜性。 | 持續任務可能需要更高效的狀態更新和儲存機制。  |
| 任務週期      | 短期任務可以設計為情節性任務。            | 長期任務更適合持續性形式。           |
| 獎勵訊號設計    | 獎勵訊號可以集中於終止狀態和重要行為。        | 獎勵訊號需要設計成平滑且適合長期最佳化的形式。 |

### **回合性任務（episodic task）**

如果在時間步驟$$t$$之後收到的(隨機)獎勵序列表示為$$R_{t+1},R_{t+2},R_{t+3}, \dots$$，<mark style="color:red;">一般來說，我們尋求期望報酬(expected return)的最大化，其中報酬表示為</mark>$$G_t$$。在最簡單的情況下，報酬是獎勵的總和，$$T$$為期末時間：

$$Gt =R_{t+1}+ R_{t+2}+  \dots + R_{T}$$

可以不必考慮折現率$$\gamma$$。

這種方法在有最終時間步驟的自然概念的應用中是有意義的，也就是說，<mark style="color:red;">當代理人與環境的互動自然地分成子序列時，我們稱之為回合(episodeor trial)</mark>，比如玩游戲、穿越迷宮或任何形式的重復互動。

每個回合都在終止狀態結束，然後被重置到一個標准的起始狀態或一個標准的起始狀態分佈。即使回合是以不同的狀態結束，比如游戲的輸贏，下一個回合的開始也與前一個回合的結束狀態無關。

不同的回合有不同的獎勵。這些任務被稱為<mark style="color:red;">情節任務(episode task)</mark>。在情節任務中，我們有時需要區分所有非終端狀態的集合（表示為$$\mathcal{S}$$）和所有狀態加終端狀態的集合（表示為$$\mathcal{S}^{+}$$）。終止的時間$$T$$，是一個隨機變數，通常在不同的回合中會有所不同。

### 特性

* 有明確的開始和結束（例如遊戲結束、機器人完成某個任務）。每個情節（episode）從一個初始狀態開始，持續到終止狀態。
* 回報中包含失敗的負獎勵，並且這種負獎勵的影響因時間差距而折扣衰減。
* 回報的形式依賴於失敗時刻，且回報最終趨向於0（因為沒有持續的獎勵）。

### 使用情境

* 任務有明確的結束條件
  * 遊戲輸贏有明確判定
  * 機器人完成特定動作序列
  * 達到目標狀態後結束
* 需要重設學習環境
  * 錯誤後需要重新開始
  * 每輪實驗需要相同的初始條件
  * 安全考量要求及時終止
* 評估方便
  * 容易計算每個回合的總回報
  * 方便比較不同策略的表現
  * 便於設定階段性的學習目標

### 持續任務（continuing task）

<mark style="color:red;">另一方面在許多情況下，代理人與環境的互動並不自然地分成回合，而是無限制地持續進行</mark>。這些任務稱為<mark style="color:red;">持續任務(continuing task)</mark>。因為時間是無限的，所以將報酬改為折現率(discounted)的形式如下：

* $$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots = \sum_{k=0}^\infty \gamma^k R_{t+k+1}, ~ 0 \leq \gamma \leq 1$$
* 當$$\gamma <1$$且$$R_t=1, ~\forall t$$時，收斂為 $$G_t = \sum_{k=0}^\infty \gamma^k = \frac{1}{1-\gamma}$$

折現率決定了未來獎勵的現值：在未來$$k$$個時間步驟中收到的獎勵，其價值僅為立即收到的價值的$$\gamma^{k-1}$$倍。

<mark style="color:orange;">總結來說，在回合性任務中，失敗的影響是一次性的，體現在一個有限的折扣回報上；而在持續折扣任務中，失敗可能被平滑分散到長期回報中，策略最佳化的目標會有所不同</mark>。

### 特色

* 任務視為無限長，回報計算通常基於持續狀態。沒有明確的終點，任務持續進行，強調長期行為。
* 在這種形式中，失敗的負獎勵可能被視為系統行為的一部分，或者設計為週期性發生，從而對長期策略形成影響。
* 因為任務沒有明確的終止點，策略目標更多地最佳化長期回報而不是單次情節的結果。

### 使用情境

* 任務本質上無終點
  * 機器人持續控制系統
  * 持續性服務系統
  * 無限期執行的程式
* 環境持續變化
  * 需要適應動態環境
  * 任務目標隨時間改變
  * 與真實世界持續互動
* 重設代價高
  * 實體系統重設困難
  * 重設會造成衣務中斷
  * 學習過程不能中斷

### 短視近利或遠視的取捨

* 如果$$\gamma<1$$，只要獎勵序列$$|R_k| < \infty$$是有界的，$$G_t$$中的無限和就有一個有限的值。
* 如果$$\gamma=0$$，代理人是 「短視近利(myopic」的，只關心即時獎勵的最大化：在這種情況下，它的目標是學習如何選擇$$A_t$$，以最大化$$R_{t+1}$$。<mark style="color:blue;">但是一般來說，為使眼前的回報最大化而行動，會減少對未來的累積報酬，從而使總報酬減少</mark>。
* 當$$\gamma \rightarrow 1$$時，報酬目標更強烈地考慮到未來的回報；代理人變得更加遠視(farsighted)。

在連續的時間步驟中的報酬可寫成以下遞迴的形式：

$$\begin{aligned} G_t & = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} +\dots \\ 	& = R_{t+1} + \gamma (R_{t+2} + \gamma R_{t+3}+ \dots) \\ 	& = R_{t+1}  + \gamma G_{t+1} \end{aligned}$$

此遞迴定義法在$$t<T$$都可使用，定義$$G_T=0$$。

例如$$\gamma=0.5$$，$$R_1=-1, R_2=2, R_3=6, R_4=3, R_5=2, T=5$$，則：

* $$G_5=0$$。
* $$G_4=R_5+\gamma G_5 = 2+ 0.5 \times 0=2$$
* $$G_3 = R_4+\gamma G_4 = 3 + 0.5 \times 2 = 4$$
* $$G_2 = R_3+\gamma G_3 = 6 + 0.5 \times 4= 8$$
* $$G_1 = R_2+\gamma G_2 = 2 + 0.5 \times 8 = 6$$
* $$G_0 = R_1+\gamma G_1 = -1+ 0.5 \times 6 = 2$$

### 範例: 極點平衡(pole balancing)

<figure><img src="../../.gitbook/assets/image (89).png" alt=""><figcaption><p>學習目標是左右移動小車，不讓桿子倒下。</p></figcaption></figure>

這項任務的目標是對沿軌道移動的小車施加力，以使鉸接在小車上的桿子不致倒下。<mark style="color:blue;">如果桿子從垂直方向跌落超過一個給定的角度，或者如果小車跑到軌道外，就說發生了故障</mark>。

每次失敗後，桿子會被重置為垂直狀態。這項任務可以被視為回合事件，其中每一回合是反復嘗試平衡桿子的過程。在這種情況下，沒有發生故障的每一個時間步驟的獎勵可以是+1，因此，每次的回報將是直到故障的步驟數。在這種情況下，永遠成功的平衡將意味著無窮大的回報。

**工作獎勵機制**

* 除了最後失敗的時間步，所有時間步的獎勵均為 0。
* 在失敗時（最後的時間步$$T$$），獎勵為 $$r_T=-1$$，**折扣因子**：$$\gamma \in (0,1)$$。
* 失敗時 $$G_t=-1$$。
  * $$T-1$$時$$G_{t-1}=0+\gamma (-1)=- \gamma$$
  * $$T-2$$時$$G_{t-2}=0+\gamma(0+\gamma (-1))=- \gamma^2$$
  * $$T-3$$時$$G_{t-3}=- \gamma^3$$
  * 因此在時間$$T=t$$時，$$G_t=-\gamma^{T-t}$$

另外，我們也可以把極點平衡當作一項持續的任務。在這種情況下，每次故障時的回報將是-1，其他時間的回報是0。那麼，每次的回報將與$$-\gamma^K$$有關，其中$$K$$是失敗前的時間步數。在任何一種情況下，通過盡可能長時間地保持極點的平衡，可使報酬是最大化。

### 範例：機器人走迷宮

在設計一個機器人來跑迷宮時，你決定給它通過迷宮時的獎勵設為+1分，而在其他時候獎勵為0。這樣的任務自然地劃分為回合，即機器人通過迷宮的連續嘗試。目標是最大化期望的總報酬$$G_t = R_{t+1} + \cdots + R_T$$。然而，在運行學習代理一段時間後，你發現它在逃離迷宮方面沒有表現出任何改進。問題出在哪裡？你是否有效地傳達了你希望它實現的目標？

#### 問題根源

1. **代理人無法區分路徑的好壞(**&#x734E;勵太稀疏（sparse reward）**)**：由於所有非終點的狀態的獎勵都是 0，代理人無法從環境中獲得有用的學習訊號。換句話說，代理人無法判斷哪些狀態或行動能夠促進其更快地到達終點。
2. **回報延遲問題**：唯一的獎勵 +1是在完成整個迷宮後才獲得，這導致回報的延遲過長。代理人在學習時難以將回報與特定的狀態或行動關聯起來。
3. **探索不足**：如果代理人主要探索隨機的路徑，它可能無法頻繁地接近迷宮出口，導致學習訊號進一步稀疏。
4. **未有效傳達目標**：目標是讓代理人學會快速逃出迷宮，但當前的獎勵設計僅反映了「逃出迷宮」這一結果，卻未能指引代理人如何到達出口。

<mark style="color:red;">這個設計沒有有效地向代理人傳達我們的期望：我們不只是要它逃出迷宮，還希望它能儘快找到出路。單純的終點獎勵無法提供足夠的學習訊號</mark>。

#### 改進建議

* 新增階段性獎勵（shaping rewards）
  * 接近出口時給予小額正獎勵
  * 遠離出口時給予小額負獎勵
  * 例如$$R(s,a)=-(\text{the distance from current location to exit})$$ 或$$R_T=1/完成所需步數$$
* 引入時間懲罰
  * 每個時間步給予小額負獎勵
  * 鼓勵找到更短的路徑
* 設計更密集的獎勵訊號
  * 根據與目標的距離給獎勵
  * 為發現新區域提供獎勵
* 在學習初期增加探索行為，例如使用 𝜖 ϵ-貪婪策略或 UCB（Upper Confidence Bound）等方法，確保代理人能探索更多可能的路徑。
* 使用分層目標：將整個迷宮任務分解為多個子目標，例如設定一系列「中繼站」，每到達一個中繼站給予小獎勵。

## 符號的統一

兩種強化學習任務，一種是代理人與環境的互動自然分解為一連串獨立的有限回合（回合性任務），另一種是持續性任務。

對每一情節的時間步驟從0開始進行編號。因此，我們不僅要參考時間$$t$$的狀態$$S_t$$，還要參考第$$i$$個回合時間t的狀態$$S_{t,i}$$（類似的還有$$A_{t,i}, R_{t,i}, \pi_{t,i}, T_i$$等）。然而，在討論回合性任務時，大多數不需區分相異的回合(除非是討論bootstrap等方法)。通常是考慮特定的單一回合。因此在實踐中，可放棄對回合編號的明確提及。也就是說，我們用$$S_t$$來替代$$S_{t,i}$$，以此類推。

在回合情況下，將報酬定義為有限數量項的總和；在連續情況下，定義報酬為無限數量項的總和。這兩種情況可以統一起來，即把回合終止看作是進入一個特殊的吸收狀態，該狀態只向自身轉換，並且只產生零的獎勵。

$$G_t = \sum_{k=t+1}^T \gamma^{k-t-1}R_k$$，其中$$T=\infty$$或$$\gamma=1$$(但不可同時)也包含在此定義中。

<figure><img src="../../.gitbook/assets/image (90).png" alt="" width="563"><figcaption><p>深色的方塊為虛擬的終止狀態</p></figcaption></figure>
