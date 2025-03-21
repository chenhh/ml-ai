---
description: Multi-armedBandits
---

# 多臂吃角子老虎機

## 簡介

<mark style="color:red;">強化學習區別於其他型別學習的最重要特徵是，它使用的訓練資訊是對改採取的行動進行評估(以行動-報酬評估價值函數)，而不是通過給出正確的行動進行指導</mark>。這就是創造主動探索的需要，明確地尋找好的行為。純粹的評價性反饋表明改採取的行動有多好，但不表明它是最好還是最差的行動。

* 多臂老虎機是真實問題的簡化，它們有行動和獎勵（目標），但沒有輸入或順序性。
* 在無限次的時間步驟中，選擇一個動作並接收對應的實數獎勵。
* 每個動作的獎勵為獨立同分布（i.i.d.）(指的是相同動作的獎勵是同分佈，相異動作的分佈不必相同)，但實際分布未知。
* 目標是最大化總獎勵，需要平衡探索（explore）與利用（exploit）。
* 必須考慮基本的開發-探索權衡，𝜀貪婪行動選擇是最簡單的取捨方式。
* <mark style="background-color:red;">學習行動值(action value，即採取行動的期望報酬值)是解決方法的關鍵部分</mark>。

## k臂吃角子老虎機問題(k-armed bandit problem)

決策者反復(多期決策)面臨著在$$k$$個不同的選項，或行動中的選擇。每次選擇之後，決策者都會收到一個數值獎勵（<mark style="color:blue;">**註：只知道所選的行動的獎勵，沒有選擇的行動不知道其獎勵**</mark>），這個獎勵是從一個<mark style="color:blue;">**固定的機率分佈(均為非時變且未知型式的分佈，但k個行動可有相異的分佈)**</mark>中選出，取決於你所選擇的行動。你的目標是在某個時間段內做出選擇，以最大化預期總報酬。

<figure><img src="../../.gitbook/assets/image (24).png" alt="" width="540"><figcaption><p>5個行動的報酬分佈相異，但同一個行動的報酬是從固定分佈得出。</p></figcaption></figure>

#### <mark style="color:red;">問題關鍵假設</mark>

經典 k-armed bandit 的關鍵假設是：每個拉桿的報酬分佈是靜態的(非時變)、獨立的，且符合某種固定的機率分佈（如正態、伯努利分佈或其它分佈）。

* **每個拉桿的報酬分佈是固定的（靜態假設）。**&#x6BCF;個拉桿$$k$$ 報酬是根據某個固定的機率分佈生成的，該分佈在整個問題期間不變。可以擴充為報酬分佈隨時間變化（動態環境），不在目前的討論範圍。
* 常見的假設是每個拉桿的報酬分佈相互獨立。
* 每次拉桿的報酬是獨立生成的，與之前或之後的操作無關。
* 每次拉桿立即給出報酬。

<figure><img src="../../.gitbook/assets/image (84).png" alt=""><figcaption><p>k臂吃角子老虎機，只有選中的機器才知道報酬。</p></figcaption></figure>

在吃角子老虎機問題中，$$k$$個行動都有一個預期的或平均的獎勵，可稱為該行動的價值(value)。我們用$$A_t \in \{1,2,\dots,k\}$$(隨機變數)表示在時間步驟t上選擇的行動，用$$R_t \in \mathbb{R}$$(隨機變數)表示相應行動的報酬(只依賴於選擇的行動)。&#x20;

那麼，任意行動$$a$$(實現值)的期望價值可表示為$$q_{*}(a)$$，是指在$$a$$被選中的情況下的<mark style="color:red;">**(真實)期望報酬**</mark>：

$$q_{*}(a) \equiv \mathrm{E}(R_t ~|~ A_t = a), ~\forall a \in \{1,2,\dots,k\}$$

注意此處的期望報酬是在第$$t$$期決策選擇行動$$a$$的期望值(該行動分佈的期望值，但通常未知)，而不是當期的實現值。

<mark style="color:red;">如果你知道每個行動的價值</mark>$$q_*(a), ~\forall a$$<mark style="color:red;">，那麼解決吃角子老虎機問題將很簡單：每一次總是選擇期望價值最高的行動。但一般無法確切估計地知道行動的價值</mark>。我們把行動$$a$$在時間$$t$$的估計值表示為$$Q_t(a)$$，且希望$$Q_t(a)$$能夠逼近$$q_{*}(a)$$ ，即目標為$$Q_t(a) \approx q_{*}(a), ~\forall a$$。

### 利用與探索

如果你保持對行動價值的估計，那麼在任何時間點，至少有一個行動的估計值是最大的。我們稱這些為<mark style="color:blue;">貪婪的行動 (greedy action)，即</mark>$$A_t^{*} = \argmax_{a} Q_t(a)$$。

* 當你選擇貪婪行動時，即$$A_t = A_t^{*}$$，則說是在利用(exploiting)你對行動價值的現有知識。
* 如果不選擇了非貪婪的行動，即$$A_t \neq A_t^{*}$$，則說是在探索(exploring)，因為這使我們能夠提高對非貪婪行動價值的估計。
* 利<mark style="color:red;">用是為了最大化一步達到的預期回報，但探索可能會在長遠看產生更高的總回報</mark>。

在探索過程中，短期回報較低，但長期回報較高，因為在你發現更好的行動後，你可以多次利用它們。<mark style="color:blue;">由於不可能既探索又利用任何單一的行動選擇，人們經常提到探索和利用之間的「沖突」</mark>。​

在任何特定情況下，是否應該選擇探索還是利用，都取決於<mark style="color:red;">估計值、不確定性以及剩餘步驟</mark>數等因素，這是一個複雜的問題。

對於k臂老虎機問題及相關問題的特定數學形式化，有許多高級方法可以平衡探索與利用。然而，大多數這些方法對於定態（stationarity）和先驗知識做出了強烈的假設，而這些假設在實際應用中要麼被違反，要麼根本無法驗證。這些方法所提供的優化或有界損失保證，在理論假設不適用的情況下，毫無幫助。

## 行動-價值方法(action-value method)

<mark style="color:red;">行動價值法是利用已經採取的行動與得到的報酬估計行動的期望報酬的方法，不必假設行動-價值的機率分佈</mark>。

一個行動的真實價值是該行動被選中時的平均獎勵。估算的一個自然方法是對實際收到的獎勵進行平均化：

* $$\begin{aligned} Q_t(a)&=\frac{\text{時間t之前採取行動a的報酬總和} }{\text{時間t之前採取行動a的次數} } \\ &= \frac{\sum_{i=1}^{t-1} R_i \cdot \mathrm{I}(A_i = a) }{\sum_{i=1}^{t-1} \mathrm{I}(A_i = a) } \end{aligned}, ~ \forall a \in \{1,2,\dots, k\}$$
* 若分母為0時，令$$Q_t(a)=0$$。​
* <mark style="color:blue;">註：此方法在行動集合</mark>$$A$$<mark style="color:blue;">有很多元素時，必須要有很多的資料才能得到較好的估計值</mark>。
* 如果採取無限次的動作，行動的樣本平均報酬值會接近真實期望報酬值，即$$\displaystyle  \lim_{N_t(a) \rightarrow \infty} Q_t(a) = q_{*}(a)$$。

最簡單的行動選擇規則是選擇具有最高估計值的行動之一。<mark style="color:red;">貪婪行動選擇方法</mark>寫成：

$$\displaystyle A_t \equiv \argmax_a Q_t(a)$$

貪婪的行動選擇總是利用當前的知識來最大化眼前的回報；它根本不花時間去抽查明顯較差的行動，看看它們是否真的會更好。

一個簡單的替代方案是在大多數時候表現得很貪婪，但每隔一段時間，比如說以小機率$$\epsilon$$，而從所有的行動中隨機選擇機率相同的行動，與行動價值估計無關。稱為「$$\epsilon$$-<mark style="color:red;">貪婪方法</mark>」。

這些方法的一個優點是，在極限情況下，隨著步驟數的增加，每一個行動都會被執行無限次，可確保所有的$$Q_t(a)$$都收斂到$$q_{*}(a)$$。這當然意味著選擇最佳行動的機率會收斂到大於$$1-\epsilon$$，然而，這些只是漸進的保證，對於這些方法的實際有效性沒有說明什麼。

## 價值函數估計式的漸近實作

以下討論的問題是，獎勵的樣本平均數平均值在恆定記憶體和恆定每步時間計算的情況下如何計算。

考慮單一行動，為了簡化符號，令$$R_i$$為第$$i$$​次選擇該行動的報酬，$$Q_n$$​為該行動已被選擇$$n-1$$​次後的估計價值，即：

$$Q_n\equiv \frac{R_1 + R_2 + \dots + R_{n-1}}{n}$$

上式為有批次資料時的計算方式，如果資料是逐漸在線進入時，計算方法可改為：

$$\begin{aligned} Q_{n+1} & = \frac{1}{n} \sum_{i=1}^n R_i \\ 	& = \frac{1}{n } (R_n + (n-1) \frac{1}{n-1} \sum_{i=1}^{n-1} R_i) \\ 	& = \frac{1}{n } (R_n + (n-1) Q_n) \\ 	& = Q_n + \frac{1}{n} (R_n - Q_n) \end{aligned}$$

此為學習-更新的標準步驟：

<mark style="background-color:orange;">NewEstimate <= OldEstimeate + StepSize \[Target - oldEstimate]</mark>。

因此可得$$\epsilon$$-貪婪的吃角子老虎機演算法的虛擬碼如下：

```python
for a = 1 to k:
    Q(a) = 0  # 行動a的價值函數估計值
    N(a) = 0  # 行動a被執行的次數
	

while(true){
    A = argmax_{a} Q(a) with probability 1 - e 
        or a random action with probability e
    R = bandit(A)  # 以行動A玩老虎機，得到報酬R
    N(A) = N(A) + 1
    Q(A) = Q(A) + 1/N(A)[R-Q(A)]
}
```

## 追踨非定態問題(tracking a non-stationary problem)

上述討論的平均方法適合獎勵機率分佈不隨時間變化的老虎機問題。<mark style="color:red;">而我們經常遇到的強化學習問題實際上是非穩態(non-stationary, 非定態，即真實的動作報酬分佈會隨著時間改變)。在這種情況下，給最近的獎勵比給過去的獎勵更多的權重是有意義的</mark>。

#### 簡單平均

* **特性**：
  * 所有過去的觀測值權重相等。
  * 對於非定態問題，無法快速響應序列變化。
* **優點**：
  * 計算簡單，容易實現。
  * 在定態問題中（即期望值穩定）能有效收斂到真實值。
* **缺點**：在非定態問題中，因過去數據的影響過重，對近期變化不敏感。

#### 加權平均

* **特性**：
  * 最近的觀測值被賦予更高的權重。
  * 權重隨時間指數衰減，過去的觀測值影響逐漸減弱。
* **優點**：
  * 對於非定態問題，能快速響應動作價值的變化。
  * 不需要儲存完整的觀測數據，只需更新當前估計值。
* **缺點**：需要選擇適當的步長參數 α，不當選擇可能導致收斂速度慢或震盪。

### 固定權重加權平均(exponential, recency-weighted average)

常用方法之一是使用一個恆定的步長引數。例如，用於更新$$n-1$$個過去獎勵的平均值$$Q_n$$的增量更新規則被修改為：

* $$Q_{n+1} = Q_n  + \alpha [R_n - Q_n], ~ \alpha \in (0, 1]$$
* $$\alpha$$為固定的常數。

因此$$Q_{n+1}$$為過去報酬的加權平均值如下。

$$\begin{aligned} Q_{n+1} & = Q_n  + \alpha [R_n - Q_n]  \\ 	& = \alpha R_n + (1-\alpha) Q_n \\ 	& = \alpha R_n + (1-\alpha )[\alpha R_{n-1} + (1-\alpha )Q_{n-1}]  \\ 	& = \alpha R_n + (1-\alpha) \alpha R_{n-1} + (1-\alpha)^2 Q_{n-1} \\ 	& \dots \\ 	& = (1-\alpha)^n Q_1 + \sum_{i=1}^n \alpha (1-\alpha)^{n-i}R_i  \end{aligned}$$

因為$$(1-\alpha)^n  + \sum_{i=1}^n \alpha(1-\alpha)^{n-i}=1$$，所以稱為加權平均。事實上，權重是按照指數$$1-\alpha$$衰減的。因此，這有時被稱為<mark style="color:red;">指數化的時間加權平均值</mark>。

### 變動權重加權平均

令$$\alpha_n(a)$$表示用於處理第$$n$$次選擇行動$$a$$後收到的獎勵的步長參數。當$$\alpha_n(a)=\frac{1}{n}$$時退化為簡單平均法。但當然不能保證對序列$$\{\alpha_n(a)\}$$的所有選擇都能收斂。

<mark style="color:red;">因為</mark>$$\alpha_n$$的值為隨機變數，<mark style="color:red;">保證機率收斂所需的條件為</mark>：

$$\begin{aligned}  & \displaystyle \sum_{n=1}^\infty \alpha_n(a) = \infty \\  & \sum_{n=1}^\infty \alpha_n^2 (a) < \infty \end{aligned}$$

第一個條件是為了保證步長足夠大，以最終克服任何初始條件或隨機波動。第二個條件保證最終步長變得足夠小，以保證收斂。

請注意，這兩個收斂條件在樣本平均的情況下成立$$\alpha_n(a)=\frac{1}{n}$$，但在恆定步長引數的情況下不成立$$\alpha_n(a)=\alpha$$。

若$$\alpha_n=n^{-p}, ~ p \in (0,1)$$，可得最佳收斂速度$$O(\frac{1}{\sqrt{n}})$$。

<mark style="color:red;">在後一種情況下，第二個條件沒有得到滿足，這表明估計值從未完全收斂，而是繼續隨著最近收到的獎勵而變化</mark>。正如我們上面提到的，這在非平穩環境中實際上是可取的，而實際上非平穩的問題是強化學習中最常見的。

<mark style="color:blue;">此外，滿足上述條件的步長引數序列往往收斂得很慢，或者需要相當的調整才能獲得滿意的收斂率</mark>。盡管滿足這些收斂條件的步長引數序列經常被用於理論工作中，但它們很少被用於應用和實證研究中。

## 樂觀的行動價值函數初始值

到目前為止，我們所討論的所有方法都在一定程度上依賴於初始行動價值的估計，$$Q_1(a)$$。

用統計學的語言來說，這些方法都因其初始估計值而有偏差。對於樣本平均法來說，一旦所有的行動都被選擇了至少一次，這種偏差就會消失，但是對於常數$$\alpha$$的方法來說，這種偏差是永久性的，盡管隨著時間的推移而減少影響。

<mark style="color:blue;">在實踐中，這種偏差通常不是一個問題，有時可能非常有幫助。缺點是初始估計值在中成為一組必須由用戶挑選的參數，如果只是為了將它們全部設置為零的話</mark>。好處是，它們提供了一種簡單的方法來提供一些關於可以預期的獎勵水平的預先知識。

初始動作值也可以作為鼓勵探索的一種簡單方式來使用。假設我們沒有像在10臂老虎機中那樣將初始行動值設置為零，而是將它們全部設置為+5。回顧一下，這個問題中的$$q_{*}(a)$$是從均值為0、變異數為1的常態分佈中選出的。因此，+5的初始估計是非常樂觀的。但這種樂觀主義鼓勵了行動價值方法的探索。無論最初選擇哪種行動，獎勵都小於初始估計值；學習者切換到其他行動，對它所得到的獎勵感到 "失望"。其結果是，在價值估計收斂之前，所有的行動都要嘗試幾次。即使一直選擇貪婪的行動，該系統也會進行相當數量的探索。

## 小結

本章中介紹了幾種平衡探索和利用的簡單方法。

* $$\epsilon$$-貪婪方法在一小部分時間內是隨機選擇的。
* UCB方法是確定選擇的，但通過在每一步巧妙地偏向於迄今為止收到較少樣本的行動來實現探索。
* 梯度老虎機演算法估計的不是行動的價值，而是行動的偏好，並以一種分級的、機率性的方式使用軟最大分佈偏向於更多的行動。
* 以樂觀的態度初始化估計的簡單權宜之計，甚至使貪婪的方法也有了明顯的探索。

<mark style="color:red;">在評估一種方法時，我們不僅要關注它在最佳參數設定下的表現，還要關注它對引數值的敏感程度</mark>。所有這些演算法都相當不敏感，在大約一個數量級的引數值變化范圍內表現良好。總的來說，在這個問題上，UCB似乎表現最好。

在k臂老虎機問題中平衡探索和利用的一種被充分研究的方法是計算一種特殊的行動值，稱為<mark style="color:red;">Gittins指數</mark>。<mark style="color:blue;">在某些重要的特殊情況下，這種計算是可操作的，並直接導致最佳解，盡管它確實需要對可能的問題的先驗分佈有完整的瞭解，而我們通常認為這是不可能的</mark>。此外，這種方法的理論和計算的可操作性似乎都不能推廣到我們在其餘部分考慮的全部強化學習問題。

Gittins指數方法是貝式方法的一個例項，它假定行動值有一個已知的初始分佈，然後在每一步之後精確地更新分佈（假定真實的行動值是定態的的分佈）。一般來說，更新計算可能非常復雜，但對於某些特殊的分佈（稱為共軛先驗），它們很容易。一種可能性是在每一步根據其作為最佳行動的後驗機率來選擇行動。這種方法有時被稱為後驗抽樣或Thompson抽樣，通常與我們在本章中介紹的最好的無分佈方法有類似的表現。

## 參考資料

* Richard Suttion and Andrew G. Barto, "Reinforcement Learning: An Introduction," 2nd, 2018, chapter 2.
