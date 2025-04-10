# 停時(stopping time)

## 簡介

Stopping Time（停時） 是一個隨機變數，而不是隨機過程。但定義停時會使用隨機過程。其發生與否只能依賴當前及過去的信息$$\{\tau \leq t \} \in \mathcal{F}_t \equiv \{\omega \in \Omega ~|~ \tau(\omega) \leq t \} \in \mathcal{F}_t$$。

* $$t$$：是一個特定的時間點（在離散時間中通常是整數，在連續時間中是非負實數）。
* $$\{\omega \in \Omega~|~ \tau (\omega) \leq t\}$$：表示所有使得停時$$\tau$$ 的值小於或等於$$t$$ 的樣本點 ω 的集合。換句話說，這是事件「停時在時間 $$t$$或之前發生」。
* $$\mathcal{F}_t$$：表示在時間$$t$$ 或之前可獲得的所有信息的 σ域。事件屬於$$\mathcal{F}_t$$意味著我們可以僅僅基於到時間$$t$$ 為止的信息來判斷該事件是否發生。
* 停時 τ 的值是隨機的，因為它取決於隨機過程的實現（sample path）。例如，在布朗運動中，停時可能是粒子首次達到某個特定位置的時間。
* 停時的輸出是一個單一的數值（通常是時間點），而不是一個隨時間變化的函數。因此，停時是一個隨機變數，而不是隨機過程。
* 它捕捉了隨機過程中「首次事件」的時間，具有因果性質。
* <mark style="background-color:red;">一個依賴於未來信息的隨機時間不是停時</mark>。

停時為隨機變數，且等價於停止過程(stopping process)，即初始值為1，在某時刻變為0隨機過程。討論詳見Fischer(2013)。

## 停時(stopping time)

> 定義：停時
>
> 給定$$\mathcal{T}=[0, \infty)$$與機率空間$$(\Omega, \mathcal{F}, \mathcal{F}_t, \mathrm{P})$$，則幾乎確定有限的隨機變數$$\tau: \Omega\rightarrow \mathcal{T} \cup \{\infty\}$$稱為停時，若滿足$$\forall t \in \mathcal{T}, \{ \tau \leq t \} \in \mathcal{F}_t$$。表示在某個隨機過程中停止觀察或採取行動的時間點。
>
> 因為$$\mathcal{F}_t$$為σ域，因此等價於:
>
> * $$\forall t \in \mathcal{T}, \{\tau = t\} = \{\tau \leq t\} \setminus \{\tau < t\} \in \mathcal{F}_t$$。
> * $$\forall t \in \mathcal{T}, \{\tau > t\} \in \mathcal{F}_t$$。

$$\forall t \in \mathcal{T}, ~$$$$\{\tau \leq t\} \in \mathcal{F}_t$$<mark style="color:red;">的意義就是，在每一個時間</mark>$$t$$<mark style="color:red;">所擁有的資訊</mark>$$\mathcal{F}_t$$<mark style="color:red;">，均足夠判斷是否在間</mark>$$t$$<mark style="color:red;">停下來或者說事件是否已發生，或者在之前就停下來，而不需要使用到未來</mark>$$\{\tau > t\}$$<mark style="color:red;">的資訊</mark>。停時就是滿足一定可測條件的隨機時間。截止到目前為止，所擁有的資訊能足夠做出決定是否停止。

停時的本質是「不提前偷看未來」。決定$$\tau$$是否發生只能依賴當前及之前的資訊$$\mathcal{F}_t$$，而不能依賴未來的資訊。例如，$$\tau$$可以是某個隨機過程首次達到某個值的時間，但這個決定必須基於當時的觀測。

停時用來描述在隨機過程中某個事件首次發生的時間。它與濾流（filtration）密切相關，運用在鞅理論、次鞅、超鞅以及隨機分析中。

某些停時可能永遠不會發生（例如，如果條件永遠不滿足），此時停時可能取值為無窮大（$$\tau = \infty$$）。

什麼不是停時：一個依賴於未來信息的隨機時間不是停時。例如$$\{B_t\}$$為布朗運動，$$\tau=\inf\{ t \in (0,1] ~|~B_t = \max_{s \in [0,1]}B_s\}$$不是一個停時，因為要判斷$$\tau \leq t$$，們需要知道$$B$$在整個時間區間$$[0,1]$$的最大值，這包括了時間$$t$$之後的信息。

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

## 範例：首次到達時間

設$$\{X_t\}$$是簡單隨機遊走（每次以機率$$𝑝$$增加 1，以$$1−p$$ 減少 1），定義$$\tau = \inf\{t \geq 0, X_t=1\}$$為首次到達 1 的時間。

$$\{\tau \leq t\} = \{X_0 = 1 \} \cup \{X_1 \cup 1 \} \cup \dots \cup \{X_t \leq 1\}$$，由於$$X_k$$是$$\mathcal{F}_k$$可測，且$$\mathcal{F}_k \subseteq F_{t}$$，可得$$\{\tau \leq t \} \in \mathcal{F}_t$$為停時。



## 兩個停時取最小或最大運算仍為停時

> 令$$\tau_1, \tau_2$$為相對於濾流 $$\mathcal{F}_t$$的停時，令:
>
> * $$\tau_{\max} = \max\{ \tau_1, \tau_2\}$$。
> * $$\tau_{\min} = \min\{\tau_1, \tau_2\}$$。
>
> 則$$\tau_{\max}, \tau_{\min}$$為相對於filtration $$\mathcal{F}_t$$的停時。
>
> 因為$$\{ \max(\tau_1, \tau_2) \leq t \} = \{ \tau_1 \leq t \} \cup \{ \tau_2 \leq t\} \in \mathcal{F}_t$$。
>
> $$\{ \min(\tau_1, \tau_2) \leq t \} = \{ \tau_1 \leq t \} \cap \{ \tau_2 \leq t\} \in \mathcal{F}_t$$。
>
> <mark style="background-color:red;">注：由於常數</mark>$$c \geq 0$$<mark style="background-color:red;">是停時，因此</mark>$$\min(\tau, c), \max(\tau, c)$$<mark style="background-color:red;">也是停時</mark>。

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

## 有限和

> 令$$\tau_1, \tau_2$$為相對於濾流 $$\mathcal{F}_t$$的停時，則$$\tau_1 + \tau_2$$不一定是停時。
>
> 因為$$\{\tau_1 + \tau_2  \leq t\}$$可能依賴於未來信息。
>
> 例如$$\tau_1$$為布朗運動第一次到達1，$$\tau_2$$是布朗連動第一次到達2，則$$\tau_1 + \tau_2$$需要$$\tau_2$$的值，可能非$$\mathcal{F}_t$$可測。

## 停時序列

> 如果$$\{\tau_t\}_{t \geq 1}$$為停時序列，則：
>
> * 上確界$$\sup_{t \geq 1} \tau_t$$是停時。
> * 下確界在離散時間$$\inf_{t \geq 1} \tau_t$$是停時，但在連續時間不一定成立。
> * 極限在特定條件下為停時：如果$$\{\tau_t\}$$為遞增(減)序列，$$\tau_t \to \tau$$ 且$$\tau < \infty$$，則$$\tau$$為停時。
>   * $$\liminf_{t \to \infty} \tau_n < \infty$$或$$\limsup_{t \to \infty} \tau_n < \infty$$也是停時。

## 停時的σ域

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

## 停止過程 (Stopped Process)

> 停止過程 (Stopped Process) 是一個由原始隨機過程和一個停時共同定義的新隨機過程。簡單來說，停止過程就是將原始過程在停時發生的那一刻「凍結」或「停止」下來。
>
> 如果$$\{X_t\}$$是$$\mathcal{F}_t$$可測的隨機過程，且$$\tau$$為一停時(定義在同一濾流上)，則定義停止過程$$\{X_{ t \land \tau }\}_{t \geq 0}$$仍是$$\mathcal{F}_t$$可測(保證了停止過程在任何時間$$t$$的值都是基於到時間$$t$$ 為止的信息確定的)，其中$$X_{t \land \tau} \equiv X_{\min(t, \tau)} \equiv X_t^\tau$$。

停止過程$$X_{t \land \tau}$$的行為如下：

* 在時間$$t$$ 小於停時$$\tau$$ 時，停止過程與原始過程$$X_t$$的行為完全相同。
* 在時間 大於或等於停時$$\tau$$時，停止過程的值保持在停時$$\tau$$時原始過程的值$$X_{\tau}$$不變。

換句話說，停時$$\tau$$就像一個開關，它在隨機的時間點$$\tau$$將過程$$X$$停止。

主要應用：

* 分析過程在特定隨機時間之前的行為(例如，首次到達某個水平、首次離開某個區域等)。
* 使過程具有更好的性質： 有時原始過程可能不具有某些良好的數學性質（例如，有界性、可積性等）。通過在一個合適的停時停止它，我們可以得到一個具有更好性質的過程。
* 模型建立： 在某些實際應用中，過程可能會在一個隨機的時間點終止。

## 停時範例

* 首達時間（First Passage Time） ：研究隨機過程首次達到某個狀態的時間。
* 馬爾可夫鏈中的吸收時間 ：研究隨機過程進入吸收態的時間。
* 金融數學中的最佳停止問題 ：例如，決定何時買入或賣出股票以最大化收益。
  * 如果我們知道明天股票會虧本於是我們選在在今天賣，那麼賣的時間不是一個停時。
  * 為了讓賣出時間成為停時，決策的依據必須調整為 僅僅基於當前和過去的資訊。例如：固定時間賣出、達到目標價格賣出、虧損達到一定比例賣出 (止損)。

## 參考資料

* [https://www.zhihu.com/question/24358372](https://www.zhihu.com/question/24358372)
* [https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6](https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6)
* [https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf](https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf)
* [https://ece.iisc.ac.in/\~parimal/2020/spqt/lecture-04.pdf](https://ece.iisc.ac.in/~parimal/2020/spqt/lecture-04.pdf)
* [Tom Fischer, "On simple representations of stopping times and stopping time sigma-algebras," _Statistics & Probability Letters_, Vol. _83, No._ 1,pp. 345-349, 2013](https://doi.org/10.1016/j.spl.2012.09.024).
