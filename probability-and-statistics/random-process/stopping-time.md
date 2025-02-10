# 停時(stopping time)

## 簡介

Stopping Time（停時） 是一個隨機變數，而不是隨機過程。但定義停時會使用隨機過程。

* 停時 τ 的值是隨機的，因為它取決於隨機過程的實現（sample path）。例如，在布朗運動中，停時可能是粒子首次達到某個特定位置的時間。
* 停時的輸出是一個單一的數值（通常是時間點），而不是一個隨時間變化的函式。因此，停時是一個隨機變數，而不是隨機過程。

停時這是指一個隨機過程停止的時間點，因為無法事先知道過程何時會停止，這個時間點通常是個隨機變數。通常有一個事先訂好的停止條件，只要隨機過程符合此條件，隨機過程就停下來。

關於隨機過程$$X\equiv (X_t)_{t \in T}$$的停時是隨機變數$$\tau$$ ，這一隨機變數具有如下性質：對於每一個時間 ，事件 $$\tau=t$$ 的發生與否僅取決於$$\{X_s, ~ s \leq t\}$$ 的取值。簡單的說在任一特定時刻$$t$$，由現在的資訊$$\mathcal{F}_t$$可以判別在這一時刻隨機過程是否到了停時。

停時為隨機變數，且等價於停止過程(stopping process)，即初始值為1，在某時刻變為0隨機過程。討論詳見Fischer(2013)。

## 停時(stopping time)

> 定義：停時
>
> 給定$$\mathcal{T}=[0, \infty)$$與機率空間$$(\Omega, \mathcal{F}, \mathcal{F}_t, \mathrm{P})$$，則幾乎確定有限的隨機變數$$\tau: \Omega\rightarrow \mathcal{T} \cup \{\infty\}$$稱為停時，若滿足$$\forall t \in \mathcal{T}, \{ \tau \leq t \} \in \mathcal{F}_t$$。
>
> 等價於:
>
> * $$\forall t \in \mathcal{T}, \{\tau = t\} \in \mathcal{F}_t$$。
> * $$\forall t \in \mathcal{T}, \{\tau > t\} \in \mathcal{F}_t$$。

$$\forall t \in \mathcal{T}, ~$$$$\{\tau \leq t\} \in \mathcal{F}_t$$<mark style="color:red;">的意義就是，在每一個時間</mark>$$t$$<mark style="color:red;">所擁有的資訊</mark>$$\mathcal{F}_t$$<mark style="color:red;">，均足夠判斷是否在間</mark>$$t$$<mark style="color:red;">停下來，或者在之前就停下來，而不需要使用到未來</mark>$$\{\tau > t\}$$<mark style="color:red;">的資訊</mark>。停時就是滿足一定可測條件的隨機時間。截止到目前為止，所擁有的資訊能足夠做出決定是否停止。

某些停時可能永遠不會發生（例如，如果條件永遠不滿足），此時停時可能取值為無窮大（$$\tau = \infty$$）。

<details>

<summary>proof: 等價定義的證明</summary>

\=> 由$$\{ \tau = t \} \in \mathcal{F}_t \Rightarrow  \{ \tau \leq t \} \in \mathcal{F}_t$$

因為$$\forall t \in \mathcal{T}, ~\{ \tau = t \} \in \mathcal{F}_t$$

因此得$$\forall t \in \mathcal{T}, ~ \forall s \leq t, ~ \{\tau = s\} \in \mathcal{F}_s$$

由於$$\forall s \leq t, ~ \mathcal{F}_s \subseteq \mathcal{F}_t$$，因此$$\forall t \in \mathcal{T}, ~ \forall s \leq t, ~ \{\tau = s\} \in \mathcal{F}_t$$

由於σ域元素的可數聯集或交集仍為其元素，其實數的區間可表示為可數集合的聯集或交集，因此$$\forall t \in \mathcal{T}, ~ \bigcup_{s \leq t} \{ \tau = s\} \in \mathcal{F}_t$$

所以 $$\forall t \in \mathcal{T}, \{\tau \leq t\} \in \mathcal{F}_t$$

(QED)

<= 由$$\{ \tau \leq t \} \in \mathcal{F}_t \Rightarrow \{ \tau = t \} \in \mathcal{F}_t$$

因為$$\{ \tau \leq t\} = \{\tau < t \} \cup \{\tau = t\} \in \mathcal{F}_t$$且$$S_t \equiv \{\tau < t\} = \bigcup_{s < t}\{\tau =s \}  \in \mathcal{F}_t$$

可得$$\displaystyle  \begin{aligned} \{\tau = t\} & = \{\tau \leq t\} - S_t \\ & = \{\tau \leq t\} \cap S_t^c \\ & = \{\{\tau \leq  t\} \cup S\}^c \in \mathcal{F}_t  \end{aligned}$$

(QED)

</details>

### 範例：獨立的Bernoulli序列

&#x20;考慮獨立同分佈(i.i.d.)的Bernoulli序列$$X: \Omega \rightarrow \{0, 1\}^{\mathbb{N}}$$，且定義到時間$$n$$試驗成功的次數為$$S_n \equiv \sum_{i=1}^n X_i$$，則可定義停時為 $$T_k \equiv \min\{ n \in \mathbb{N} ~|~ S_n = k\}, ~ \forall \in \mathbb{N}$$為成功$$k$$次所需的最短時間。

由定義可得$$T_k$$幾乎確定有限，且$$\{T_k=n\} = \bigcap_{i=1}^{n-1} \{S_i < k\} \cap \{S_n =k\} \in \mathcal{F}_n$$

## 兩個停時取最小或最大運算仍為停時

> 令$$\tau_1, \tau_2$$為相對於filtration $$\mathcal{F}_t$$的停時，令:
>
> * $$\tau_{\max} = \max\{ \tau_1, \tau_2\}$$。
> * $$\tau_{\min} = \min\{\tau_1, \tau_2\}$$。
>
> 則$$\tau_{\max}, \tau_{\min}$$為相對於filtration $$\mathcal{F}_t$$的停時。

<details>

<summary>proof: 用停時的定義與filitration的性質證明</summary>

max

$$\{\tau_{\max} = t\}$$可能是因為$$\tau_1 \geq \tau_2$$而得到$$\{\tau_1 = t\}$$或是$$\tau _1 \leq \tau_2$$得到$$\{\tau_2 = t\}$$。

因此$$\{\tau_{\max} = t\}  =  [\{\tau_{1} = t\} \cap \{\tau_{2} \leq  t\}] \cup  [\{\tau_{1} \leq t\} \cap \{\tau_{2} =  t\}]$$

因為由停時定義得$$\{\tau_{1} = t\} \in \mathcal{F}_t$$且$$\{\tau_{2} \leq t\} \in \mathcal{F}_t$$且σ域內元素任意交集仍為其元素，因此$$[\{\tau_{1} = t\} \cap \{\tau_{2} \leq  t\}] \in \mathcal{F}_t$$。

同理可得$$[\{\tau_{1} \leq t\} \cap \{\tau_{2} =  t\}] \in \mathcal{F}_t$$

因此$$\{\tau_{\max} = t\}  =  [\{\tau_{1} = t\} \cap \{\tau_{2} \leq  t\}] \cup  [\{\tau_{1} \leq t\} \cap \{\tau_{2} =  t\}] \in \mathcal{F}_t, ~ \forall t \in \mathcal{T}$$

(QED)

min

$$\{\tau_{\min} = t\}$$可能是$$\tau_1 \leq \tau_2$$得到$$\{\tau_1 = t\}$$或是$$\tau _1 \geq \tau_2$$得到$$\{\tau_2 = t\}$$。

由於停時不能依賴於未來的資訊，因此再拆解為$$\tau_1 < \tau_2$$得到$$\{\tau_1 = t\}$$，$$\tau _1 > \tau_2$$得到$$\{\tau_2 = t\}$$，或者兩者相同$$\tau_1 = \tau_2$$得$$\{\tau_1 = t\} \cap \{\tau_2=t\}$$

因此$$\{\tau_{\min} = t\}  =  [\{\tau_{1} = t\} \cap \{\tau_{2} > t\}] \cup  [\{\tau_{1} > t\} \cap \{\tau_{2} =  t\}] \cup  [\{\tau_{1} = t\} \cap \{\tau_{2} =  t\}]$$

等號右側所有集合都是$$\mathcal{F}_t$$的元素，且σ域內元素任意交(聯集)集仍為其元素，因此$$\{\tau_{\min} = t\} ~\forall t \in \mathcal{T}$$。

(QED)

</details>

## 包含停時的σ域

> 令$$\tau$$為機率空間$$(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathrm{P})$$的停時隨機變數，則$$\mathcal{F}\tau =\{ A \in \mathcal{F} ~|~ A \cap \{\tau \leq t \} \in \mathcal{F}_t, ~ \forall t \geq 0\}$$為其σ域。其中$$\mathcal{F} \equiv \mathcal{F}_\infty$$為全局的σ域。
>
> 此定義即停時的σ域，是由停止時間$$\tau$$發生之前事件形成的資訊集合。

<details>

<summary>proof: 證明<span class="math">\mathcal{F}_\tau</span>滿足σ域的三個條件</summary>

1. 證明$$\Omega \in \mathcal{F}_\tau$$。

因為$$\mathcal{F}$$為σ域，可得$$\Omega \in \mathcal{F}$$。同理$$\mathcal{F}_t, \forall t \in \mathcal{T}$$都是σ域，因此$$\Omega \in \mathcal{F}_t, ~ \forall t \in \mathcal{T}$$。

因此可得$$\Omega \in \mathcal{F}_\tau$$ (QED)

2. 證明$$E \in \mathcal{F}_\tau \Rightarrow E^c \in \mathcal{F}_\tau$$

令$$E \in \mathcal{F}_\tau$$，由定義可得$$E\cap \{\tau \leq t \} \in \mathcal{F}_t, ~ \forall t \geq 0$$--(1)

因為$$\{\tau \leq t\} = [\{\tau \leq t\} \cap E] \cup [\{\tau \leq t\} \cap E^c], ~\forall t \geq 0$$--(2)

已知$$[\{\tau \leq t\} \cap E]  \in \mathcal{F}_t$$，因此只需考慮$$\{\tau \leq t\} \cap E^c$$。

而$$\{\tau \leq t\} \cap E^c =  \{\tau \leq t\} \cap [\{\tau \leq t\} \cap E]^c = [\{\tau \leq t\}^c \cup [\{\tau \leq t\} \cap E]]^c, ~\forall t \geq 0$$--(3)

因為$$\{\tau \leq  t \} \in \mathcal{F}_t$$且$$\mathcal{F}_t$$為σ域，因此$$\{\tau \leq t\}^c \in \mathcal{F}_t$$--(4)

由(1,3,4)得$$\{\tau \leq t\} \cap E]^c \in \mathcal{F}_t$$ (QED)

3. 證明元素可數聯集封閉性

令$$E_1, E_2, \dots \in \mathcal{F}_\tau$$，由定義得$$\forall n \in \mathbb{N}, ~ E_n \cap \{\tau \leq t \} \in \mathcal{F}_t, ~ \forall t \geq 0$$

&#x20;因為$$\mathcal{F}_t$$為σ域，可數個元素的聯集仍在集合中， 可得$$\bigcup_{n \in \mathbb{N}} [E_n \cap \{\tau \leq t \}] \in \mathcal{F}_t, ~\forall t \geq 0$$。

整理後可得$$[\bigcup_{n \in \mathbb{N}} E_n] \cap \{\tau \leq t\} \in \mathcal{F}_t, ~\forall t  \geq 0$$。

由定義可得$$[\bigcup_{n \in \mathbb{N}} E_n] \in \mathcal{F}_\tau$$ (QED).

</details>

### 停時σ域的單調性

> 給定機率空間$$(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathrm{P})$$與隨機過程$$X: \Omega \rightarrow \mathcal{X}^{\mathcal{T}}$$，令$$\tau, \tau_1, \tau_2$$均為停時，則：
>
> 1. 若$$\tau_1 \leq \tau_2$$ a.s.，則$$\mathcal{F}{\tau_1} \subseteq  \mathcal{F}{\tau_2}$$。
> 2. $$\sigma(\tau) \subseteq \mathcal{F}_\tau$$且$$\sigma(X_\tau) \subseteq \mathcal{F}_\tau$$。

<details>

<summary>proof</summary>

proof 1

因為$$\tau_1 \leq \tau_2$$ a.s. 即$$\mathrm{P}(\tau_1(\omega) \leq \tau_2(\omega))=1, ~ \forall \omega  \in \Omega - \Omega_0$$

因此給定$$t \in \mathcal{T}$$時，$$\forall \omega -\Omega_0, \tau_2(\omega) \leq t$$可保證$$\tau_1(\omega) \leq t$$。因此$$\{\tau_2 \leq t\} \subseteq \{\tau_1 \leq t\}$$ a.s.

所以$$\forall A \in \mathcal{F}_{\tau_1}$$，可得$$A \cap \{\tau_2 \leq t\} = A \cap [\{\tau_2 \leq t\} \cap \{\tau_1 \leq t\}] \in \mathcal{F}_t$$ (QED)

proof 2:

$$\sigma(\tau)$$是由$$\{\tau \leq s\} \equiv \{\omega \in \Omega~|~ \tau(\omega) \leq s\}, ~ s \in \mathbb{R}$$所生成的最小σ域。

令$$A \in \sigma(\tau)$$，由$$\mathcal{F}\tau =\{ A \in \mathcal{F} ~|~ A \cap \{\tau \leq t \} \in \mathcal{F}_t, ~ \forall t \geq 0\}$$的定義得$$\{\tau \leq s\} \cap \{\tau \leq t\} = \{\tau \leq \min{s,t\}} \in \mathcal{F}_t$$。所以$$A \in \mathcal{F}_\tau$$  (QED )

</details>

## 停時範例

* 首達時間（First Passage Time） ：研究隨機過程首次達到某個狀態的時間。
* 馬爾可夫鏈中的吸收時間 ：研究隨機過程進入吸收態的時間。
* 金融數學中的最佳停止問題 ：例如，決定何時買入或賣出股票以最大化收益。
  * 如果我們知道明天股票會虧本於是我們選在在今天賣，那麼賣的時間不是一個停時。
  * 為了讓賣出時間成為停時，決策的依據必須調整為 僅僅基於當前和過去的資訊。例如：固定時間賣出、達到目標價格賣出、虧損達到一定比例賣出 (止損)。
  *
* 現實生活中停時的例子如賭徒離開賭桌的時刻，這一時刻可能是賭徒以前贏得錢財的函數（例如在賭徒沒有錢時，他才可能離開賭桌），但是他不可能根據還未完成的賽局的結果來選擇離開還是留下。
* 假設你現在準備從機場坐車回家，這時候家人打電話問：「還有多久到家呀？」，你當然回答不了一個精準的時間了，這時候你選擇下車的時間$$\tau$$就是一個隨機變數。而在回家路上的每個時間$$t$$ ，你都能夠判斷下車或者不下車。此已經滿足$$\{\tau \leq t \} \in \mathcal{F}_t$$，因為在時間$$t$$你所有的資訊足夠用以判斷是否應該下車了，所以$$\tau$$是停時(可選擇)。
* 如果出發十分鐘後，車子突然爆胎，那你選擇下車的時間還是停時嗎？依定義將$$\tau$$限制在{出發十分鐘後爆胎}這個集合上還是停時。因為在每個時刻$$t$$你都能夠判斷是否下車。即使爆胎了之後，你也能夠做出“下車”這個判斷。
* 如果剛上車後不久你發現車上的油只夠跑十公里了。假設你對你家離機場的距離沒有概念，那麼你選擇下車的時間 $$\tau$$不是停時。因為你此時難以判斷是否應該下車：如果你家離機場只有五公里，那麼不下車是最方便的。但如果你家離機場有二十公里，你就應該下車，因為出機場以後說不定就不好打車了。也就是說，這時候$$\tau$$ 是“無法做出選擇”的，所以不是停時。
* 假設你在坐地鐵，但是地鐵上沒有任何站名提醒，你只知道要在倒數第二站下車。你選擇下車的時間依然用$$\tau$$表示，此時你在途中任何時刻$$t$$ 都不能判斷是否應該下車，因為直到終點你才會知道哪站是倒數第二站。所以說$$\tau$$不是一個停時。

## 參考資料

* [https://www.zhihu.com/question/24358372](https://www.zhihu.com/question/24358372)
* [https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6](https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6)
* [https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf](https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf)
* [https://ece.iisc.ac.in/\~parimal/2020/spqt/lecture-04.pdf](https://ece.iisc.ac.in/~parimal/2020/spqt/lecture-04.pdf)
* [Tom Fischer, "On simple representations of stopping times and stopping time sigma-algebras," _Statistics & Probability Letters_, Vol. _83, No._ 1,pp. 345-349, 2013](https://doi.org/10.1016/j.spl.2012.09.024).
