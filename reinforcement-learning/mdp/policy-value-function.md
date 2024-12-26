---
description: policy and value functions
---

# 策略與價值函數

<mark style="color:red;">幾乎所有的強化學習演算法都涉及估計價值函數，即狀態或(狀態-行動)對的函數，這些函數估計代理人處於給定狀態有多好（或在給定狀態下執行給定行動有多好）</mark>。這裡的 "多好 "的概念是指可以預期的期望報酬。當然，代理人可望在未來獲得的回報取決於它將採取什麼行動。因此，價值函數是針對特定的行動方式（稱為策略(policy)）而定義的。

<mark style="color:red;">策略(policy)是一種從狀態到選擇每種可能行動的機率的對映</mark>。如果代理人在時間$$t$$遵循策略$$\pi$$，則$$\pi(a|s)$$是狀態$$S_t = s$$時，採取行動$$A_t = a$$的機率。

<mark style="color:red;">強化學習方法具體說明了代理人的策略是如何因其經驗而改變的</mark>。即根據經驗，學習在狀態$$s\in\mathcal{S}$$時，採取何種行動$$a \in \mathcal{A}(s)$$可使(長期)期望報酬最大化。

$$p(s^{'}, r|s, a) \equiv \mathrm{P}(S_{t+1}=s^{'}, R_{t+1}=r \vert S_t=s, A_t=a)$$

### 狀態的價值函數

<mark style="color:red;">狀態</mark>$$s$$​<mark style="color:red;">使用策略</mark>$$\pi$$​<mark style="color:red;">的價值函數記為</mark>$$v_{\pi}(s)$$<mark style="color:red;">(state value</mark> <mark style="color:red;">function for policy</mark> $$\pi$$)，其值為在狀態$$s$$​使用策略$$\pi$$​的期望報酬。其MDP定義如下：

$$\displaystyle \begin{aligned} v_{\pi}(s) & = \mathrm{E}_{\pi}(G_t ~|~ S_t = s) \\ 	& = \mathrm{E}_{\pi}\left[  		\sum_{k=0}^\infty \gamma^k R_{t+k+1} ~\big| S_t = s 	\right], ~ \forall s \in \mathcal{S} \end{aligned}$$

如果任務中有終止狀態時，則該狀態的價值函數必為0。

### 狀態-行動對的價值函數

<mark style="color:red;">狀態</mark>$$s$$​時，<mark style="color:red;">參考策略</mark>$$\pi$$<mark style="color:red;">而採取行動</mark>$$a$$<mark style="color:red;">的價值函數記為</mark>$$q_\pi(s,a)$$<mark style="color:red;">(action-value function for policy</mark> $$\pi$$)，同樣也是此行動對的期望報酬。其MDP定義如下：

$$\displaystyle \begin{aligned} q_{\pi}(s, a) & = \mathrm{E}_{\pi}(G_t ~|~ S_t = s, A_t = a) \\ 	& = \mathrm{E}_{\pi}\left[  		\sum_{k=0}^\infty \gamma^k R_{t+k+1} ~\big| S_t = s, A_t = a 	\right]  \end{aligned}$$

### 估計價值函數的方法

價值函數$$v_{\pi}$$和$$q_{\pi}$$可以根據經驗估計。例如，如果代理人遵循策略$$\pi$$，並為所遇到的每個狀態保持一個遵循該狀態的實際回報的平均值，那麼當遇到該狀態的次數接近無限時，該平均值將收斂於該狀態的值$$v_{\pi}(s)$$。如果對每個狀態下採取的每個行動都保持單獨的平均數，那麼這些平均數同樣會收斂到行動值$$q_{\pi}(s, a)$$。我們稱這種估計方法為<mark style="color:blue;">蒙地卡羅方法</mark>，因為它們涉及到許多實際收益的隨機樣本的平均化。

如果有非常多的狀態，那麼為每個狀態單獨保留平均數可能是不實際的。相反，代理人將不得不把$$v_{\pi}$$和$$q_{\pi}$$作為引數化的函數（引數比狀態少）來維護，並調整引數以更好地匹配觀察到的收益。這也可以產生准確的估計。

整個強化學習和動態規劃中使用的價值函數的一個基本屬性是，它們滿足類似於我們已經為報酬建立的遞迴關係。對於任何策略$$\pi$$和任何狀態$$s$$，在$$s$$的值和其可能的繼任狀態的值之間存在以下<mark style="color:red;">**一致性條件(Bellman equation for**</mark> $$v_{\pi}(s)$$<mark style="color:red;">**)**</mark>：

$$\displaystyle \begin{aligned} v_{\pi}(s) & = \mathrm{E}_{\pi}(G_t ~| ~ S_t =s ) \\ 	&= \mathrm{E}_{\pi}(R_{t+1} + \gamma G_{t+1} ~| ~ S_t =s ) \\ 	&= \sum_a \pi(a|s) \sum_{s^{'}} \sum_{r} \mathrm{P}(s^{'}, r ~|~ s, a)[r+ \gamma \mathrm{E}_{\pi}(G_{t+1} ~|~ S_{t+1} = s^{'}) ] \\ 		& = \sum_a \pi(a|s) \sum_{s^{'}} \sum_{r} \mathrm{P}(s^{'}, r ~|~ s, a)[r+ \gamma v_{\pi}(s^{'}) ], ~ \forall s \in \mathcal{S} \end{aligned}$$

上式最後一行可解釋為對於所有的三元組$$(a, s^{'}, r)$$，我們計算其機率$$\pi(a|s)\mathrm{P}(s^{'}, r ~|~ s, a)$$，此值可視為$$[r+\gamma v_{\pi}(s^{'})]$$的權重，計算後得期望報酬。
