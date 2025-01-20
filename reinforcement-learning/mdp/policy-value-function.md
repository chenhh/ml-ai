---
description: policy and value functions
---

# 策略與價值函數

<mark style="color:red;">幾乎所有的強化學習演算法都涉及估計價值函數，即狀態或(狀態-行動)對的函數，這些函數估計代理人處於給定狀態有多好（或在給定狀態下執行給定行動有多好）</mark>。這裡的 "多好 "的概念是指可以預期的期望報酬。當然，代理人可望在未來獲得的回報取決於它將採取什麼行動。因此，價值函數是針對特定的行動方式（稱為策略(policy)）而定義的。

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="353"><figcaption><p>確定策略，可視為隨機策略在特定行動機率為1的特例。</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt="" width="448"><figcaption><p>隨機策略</p></figcaption></figure>

## 策略(policy)

<mark style="color:red;">策略(policy)是一種給定目前狀態</mark>$$S_t=s$$，<mark style="color:red;">選擇每種可能行動的機率分佈</mark>。如果代理人在時間$$t$$遵循策略$$\pi$$，則$$\pi(a|s)$$是狀態$$S_t = s$$時，採取行動$$A_t = a$$的機率。MDP中的策略，只需考慮目前的狀態，而不需考慮完整的歷史資料，而且策略為定態(非時變)的機率分佈，即$$A_t \sim \pi(\cdot |S_t), ~ \forall t > 0$$。

隨機策略π選擇行動的機率是主觀機率：

* 代理人的主動選擇。
* 基於代理人的學習經驗。
* 可以被代理人調整和優化。
* 反映代理人對行動價值的主觀評估。

<mark style="color:red;">強化學習方法具體說明了代理人的策略是如何因其經驗而改變的</mark>。即根據經驗，學習在狀態$$s\in\mathcal{S}$$時，採取何種行動$$a \in \mathcal{A}(s)$$可使(長期)期望報酬最大化。

## 策略與狀態行動對機率分佈獨立

在MDP中，狀態選擇行動的機率 $$\pi(a∣s)$$ 和選擇行動後得到的報酬與下一狀態的條件機率$$𝑝 ( 𝑠^{'}, 𝑟 ∣ 𝑠 , 𝑎 )$$ 是獨立的，這是由 MDP 的假設和數學結構決定的。

即聯合機率分佈$$p(s^{'}r,a|s)=p(a|s) \cdot p(s^{'},r|s,a)$$。

決策過程的順序性：

1. 先觀察當前狀態$$s$$。
2. 根據策略$$\pi$$選擇行動$$a$$。
3. 環境根據$$(s,a)$$產生新狀態和獎勵$$(s^{'}, r)$$。

### 策略和環境的分離

* 策略$$\pi(a∣s)$$代理人決定在狀態 $$s$$下選擇行動 $$a$$的機率分佈，是代理人對行動選擇的主觀決策，基於代理人的目標和學到的經驗，由代理人自己控制。
* 環境轉移動態$$p(s^{′},r|s,a)$$給定當前狀態 $$s$$ 和行動 $$a$$，環境決定下一狀態 $$s^{′}$$ 和報酬 $$r$$ 的機率分佈，這由環境本身確定，是環境對行動的客觀響應，與代理人的主觀決策無關。。
* 這種分離意味著，行動選擇過程和環境如何響應行動是兩個相互獨立的機制。

### 因果依賴結構

* 行動選擇依賴於當前狀態：$$\pi(a|s)$$ 只依賴於當前狀態 $$s$$，不直接依賴於未來狀態 $$s^{'}$$ 或報酬$$𝑟$$。
* **狀態和報酬的轉移依賴於當前狀態和行動**：$$p(s^{′},r∣s,a)$$只依賴於當前狀態$$s$$和選擇的行動 $$a$$，不依賴於策略 $$\pi$$。

### 代理人對環境的未知性

在強化學習的背景下，代理人通常對環境的轉移機率 $$p(s^{′},r∣s,a)$$是未知的。代理人只能觀察到自己的選擇$$𝑎$$和由環境返回的$$s^{ }$$′ 與$$𝑟$$。因此，代理人設計的策略 $$\pi(a|s)$$不依賴於$$p(s^{′},r∣s,a)$$ ，而是根據觀察到的回饋來調整。

### 討論

#### 優點

* 分離關注點：這樣的分離簡化了模型設計和分析。
* 模組化設計：假設這兩個機率分佈是獨立的，可以讓我們更靈活地改變其中一個而不影響另一個。
* 數學上的便利性：在求解最優策略時，我們可以專注於找到最大化預期累積獎勵的策略，而無需同時考慮環境的具體轉移機制。
* 實際應用中的合理性：例如在機器人導航任務中，機器人的移動方向（策略）與它是否能成功到達目標位置並獲得獎勵（環境動態）是分開考慮的。

#### 潛在問題

雖然在標準 MDP 模型中假定了這種獨立性，但在某些情況下，策略的選擇可能會影響環境動態。

例如，在一些複雜環境中，智慧體的行為可能會改變環境的結構或者參數。在這種情況下，我們就進入了更為複雜的建模領域，如分層強化學習或元學習等高級主題。但就經典的 MDP 定義而言，$$\pi(a|s)$$ 和 $$p(s^{′},r∣s,a)$$ 是被視作獨立的。

## 狀態執行動作後的(下一期)期望報酬

目前狀態$$S_t=s$$，且動作$$A_t$$是依據隨機策略$$\pi$$選擇，則報酬$$R_{t+1}$$的期望值可表示為$$\pi(a|s)$$與$$p(s^{'}, r|s,a)$$的形式：

$$\displaystyle \mathrm{E}_{\pi} (R_{t+1}|S_t=s)=\sum_{a \in A(s)} \pi(a|s) \sum_{s^{'}, r} r \cdot p(s^{'},r|s,a)$$

* 在目前的狀態$$s$$，選擇行動$$a \in A(s)$$的機率為$$\pi(a|s)$$。
* 在選定行動$$a$$後，得到報酬$$r$$且轉移到下一狀態為$$s^{'}$$的機率為$$p(s^{'}, r|s,a)$$
* 轉移機率$$p(s^{'}, r|s, a) \equiv \mathrm{P}(S_{t+1}=s^{'}, R_{t+1}=r \vert S_t=s, A_t=a)$$，是給定目前狀態$$S_t=s$$與行動$$A_t=a$$後的機率。
* 內部的加總$$\sum_{s^{'}, r} r \cdot p(s^{'},r|s,a)$$這一部分表示在狀態$$𝑠$$執行動作 $$𝑎$$時，根據轉移動作的機率分佈計算的期望獎勵。
* 外部的加總$$\sum_{a \in A(s)} \pi(a|s)$$是對於狀態$$𝑠$$下的所有可能動作$$𝑎$$，根據策略選擇的機率權重進行加權平均。

## 狀態的價值函數

<mark style="color:red;">狀態</mark>$$s$$​<mark style="color:red;">使用策略</mark>$$\pi$$​<mark style="color:red;">的價值函數記為</mark>$$v_{\pi}(s)$$<mark style="color:red;">(state value</mark> <mark style="color:red;">function for policy</mark> $$\pi$$)，其值為在狀態$$s$$​使用策略$$\pi$$​的(長期)期望報酬。其定義如下：

$$\begin{aligned} G_t & = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} +\dots \\ 		& = R_{t+1}  + \gamma G_{t+1} \end{aligned}$$

$$\displaystyle \begin{aligned}  v_{\pi}(s) & = \mathrm{E}_{\pi}(G_t ~|~ S_t = s) \\ 	 & = \mathrm{E}_{\pi}\left[\sum_{k=0}^\infty \gamma^k R_{t+k+1} ~\big| S_t = s 	\right] ~  \\  & = \mathrm{E}_{\pi}(R_{t+1} + \gamma G_{t+1} ~|~ S_t = s) \\ 	 & = \sum_{a \in A(s)} \pi(a|s) \sum_{s^{'} \in \mathcal{S}} \sum_{r\in \mathcal{R}} p(s^{'}, r|s,a)[r+ \gamma \mathrm{E}_{\pi} (G_{t+1} ~|~ S_{t+1}=s^{'})] \\ & = \sum_{a \in A(s)} \pi(a|s) \sum_{s^{'} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s^{'}, r|s,a)[r+ \gamma v_{\pi}(s^{'})], ~ \forall s \in \mathcal{S} \end{aligned}$$

如果任務中有終止狀態時，則該狀態的價值函數必為0。

## 狀態-行動對的價值函數

<mark style="color:red;">狀態</mark>$$s$$​時，<mark style="color:red;">參考策略</mark>$$\pi$$<mark style="color:red;">而採取行動</mark>$$a$$<mark style="color:red;">的價值函數記為</mark>$$q_\pi(s,a)$$<mark style="color:red;">(action-value function for policy</mark> $$\pi$$)，同樣也是此行動對的期望報酬。其定義如下：

$$\displaystyle \begin{aligned} q_{\pi}(s, a) & = \mathrm{E}_{\pi}(G_t ~|~ S_t = s, A_t = a) \\ 	& = \mathrm{E}_{\pi}\left[  		\sum_{k=0}^\infty \gamma^k R_{t+k+1} ~\big| S_t = s, A_t = a 	\right]  \end{aligned}$$



### 狀態價值函數以狀態-行動價值函數表示

$$\displaystyle v_{\pi}(s)=\sum_{a \in A(s)} \pi(a|s) q_{\pi}(s,a)$$

在狀態$$S_t=s$$下，其價值$$v_{\pi}(s)$$是該狀態的所有可能行動價值$$q_{\pi}(s,a)$$的加權平均值，而權重是由策略$$\pi(a|s)$$決定。

<mark style="background-color:red;">換句話說，狀態值是根據當前策略選擇行動後的期望總回報</mark>。

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt="" width="229"><figcaption><p>狀態的價值是(狀態-行動)對的期望值</p></figcaption></figure>

### 狀態-行動價值函數以狀態價值函數表示

$$\displaystyle  \begin{aligned} q_{\pi}(s,a) & = \mathrm{E} (R_{t+1} + \gamma v_{\pi}(s_{t+1}) | S_t=s, A_t=a)\\     & = \sum_{s^{'} \in \mathcal{S}} p(s^{'},r|s,a)(r+\gamma v_{\pi}(s^{'})) \end{aligned}$$

$$q_{\pi} (s,a)$$ 表示從狀態$$𝑠$$遵循策略$$\pi$$執行動作$$𝑎$$ 的期望回報，可以分解為：

* 當前立即獲得的報酬$$R_{t+1}$$。
* 後續狀態$$S_{t+1}$$的價值$$v_{\pi}(s^{'})$$，折扣因子$$\gamma$$用於考慮未來的回。

### 估計價值函數的方法

價值函數$$v_{\pi}$$和$$q_{\pi}$$可以根據經驗估計。例如，如果代理人遵循策略$$\pi$$，並為所遇到的每個狀態保持一個遵循該狀態的實際回報的平均值，那麼當遇到該狀態的次數接近無限時，該平均值將收斂於該狀態的值$$v_{\pi}(s)$$。如果對每個狀態下採取的每個行動都保持單獨的平均數，那麼這些平均數同樣會收斂到行動值$$q_{\pi}(s, a)$$。我們稱這種估計方法為<mark style="color:blue;">蒙地卡羅方法</mark>，因為它們涉及到許多實際收益的隨機樣本的平均化。

如果有非常多的狀態，那麼為每個狀態單獨保留平均數可能是不實際的。相反，代理人將不得不把$$v_{\pi}$$和$$q_{\pi}$$作為引數化的函數（引數比狀態少）來維護，並調整引數以更好地匹配觀察到的收益。這也可以產生准確的估計。

整個強化學習和動態規劃中使用的價值函數的一個基本屬性是，它們滿足類似於我們已經為報酬建立的遞迴關係。對於任何策略$$\pi$$和任何狀態$$s$$，在$$s$$的值和其可能的繼任狀態的值之間存在以下<mark style="color:red;">**一致性條件(Bellman equation for**</mark> $$v_{\pi}(s)$$<mark style="color:red;">**)**</mark>：

$$\displaystyle \begin{aligned} v_{\pi}(s) & = \mathrm{E}_{\pi}(G_t ~| ~ S_t =s ) \\ 	&= \mathrm{E}_{\pi}(R_{t+1} + \gamma G_{t+1} ~| ~ S_t =s ) \\ 	&= \sum_a \pi(a|s) \sum_{s^{'}} \sum_{r} \mathrm{P}(s^{'}, r ~|~ s, a)[r+ \gamma \mathrm{E}_{\pi}(G_{t+1} ~|~ S_{t+1} = s^{'}) ] \\ 		& = \sum_a \pi(a|s) \sum_{s^{'}} \sum_{r} \mathrm{P}(s^{'}, r ~|~ s, a)[r+ \gamma v_{\pi}(s^{'}) ], ~ \forall s \in \mathcal{S} \end{aligned}$$

上式最後一行可解釋為對於所有的三元組$$(a, s^{'}, r)$$，我們計算其機率$$\pi(a|s)\mathrm{P}(s^{'}, r ~|~ s, a)$$，此值可視為$$[r+\gamma v_{\pi}(s^{'})]$$的權重，計算後得期望報酬。
