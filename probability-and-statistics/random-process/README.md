# 隨機過程

## 簡介

簡單來說，**隨機過程** 是一組隨機變數，這些隨機變數會隨著時間或其他索引引數而變化。您可以將其視為一個隨時間演變的隨機系統。

在現實生活中有這樣一種不確定現象，它每次隨機試驗會持續一段時間，其可能結果是一個關於時間的函數。比如，我們收集$$t$$時間段內，電子元件的熱噪聲電壓。每次隨機試驗都可以得到一個$$X(t)$$的函數，而且每次試驗的函數曲線都不一樣。我們把試驗結果畫到同一個坐標系中，可以看到在$$t_0$$時刻，$$X(t_0)$$ 的結果有無數個且服從某一分佈，因此我們把這種不確定現象稱為隨機過程（Stochastic Process）。

機率理論主要在研究一個(一維)或有限多個(多維)隨機變數間的統計規律。但現今的應用上，往往需連續不斷的觀察或研究某些事物在一段時間內的變化過程，這等於在考量無窮多維的向量空間，由此引出對隨機過程的探討。

機率論中，只討論隨機變數或是兩個隨機變數間的性質與分佈。而隨機過程討論是的一連串(離散或連續個)的隨機變數間的性質與分佈。

討論隨機過程有兩類方法：

1. 有限維隨機變數$$X_1, X_2, \dots, X_T$$的聯合機率分佈。
2. Σ域的公理化定義。

## 隨機過程（stochastic process）

> $$\{X(t),  \ t \in T\}$$為隨機變數的集合。隨機變數$$X(t)$$也常寫為$$X_t$$。
>
> * 指標$$t$$通常視為時間。<mark style="color:red;">而</mark>$$X_t$$<mark style="color:red;">稱為在時間</mark>$$t$$<mark style="color:red;">的狀態（state）</mark>。
> * 當$$T$$為可數集合時，如$$T=\{0,1,2,\dots\}$$，稱為<mark style="color:blue;">離散時間隨機過程</mark>；當$$T$$為實數任一區間時，如$$T=[0,\infty), [0,a)$$，稱為<mark style="color:blue;">連續時間隨機過程</mark>。
> * 在任一時刻的狀態，是連續型隨機變數或離散型隨機變數而分成連續變數隨機過程和離散變數隨機過程。
> * <mark style="color:red;">隨機過程除了考慮個別隨機變數</mark>$$X(t)$$<mark style="color:red;">的分佈外，還考慮了相異隨機變數</mark>$$X(t), X(s), t \neq s$$<mark style="color:red;">間的相關結構</mark>。
> * 在實際實驗中，常將連續時間隨機過程轉化為隨機數列處理，也即將引數集$$T$$劃分稱若干個離散的小區間$$T^{'}=\{ \Delta t, 2\Delta t, 3\Delta t, \ldots \}$$ 並在$$T^{'}$$上觀測樣本函數 $$X(t)$$ 。當$$\Delta t$$充分小時，這個隨機序列能夠近似描述連續引數隨機過程。
>
> 公理化定義：
>
> 給定filtered機率空間$$(\Omega, \mathcal{F}, \mathcal{F}_t, \mathrm{P})$$
>
> * 令$$X: [0, \infty) \times \Omega \rightarrow \mathbb{R}^d$$, $$(t, \omega) \mapsto X_t(\omega)$$。如果$$X$$是$$\mathcal{B}([0, \infty)) \otimes \mathcal{F}$$-可測函數（$$\mathcal{B}$$是Borel set），則稱$$X$$為隨機過程。
> * 給定$$\omega \in \Omega$$，$$X(\omega): [0, \infty) \rightarrow \mathbb{R}^d$$, $$t \mapsto X_t(\omega)$$稱為樣本路徑（sample path）。
> * 如果對於$$t \in [0, \infty)$$. $$X_t$$為$$\mathcal{F}_t$$-可測，則稱$$X$$為$$\{\mathcal{F}_t\}$$-的適應過程。
> * 假設全部的資訊$$\mathcal{F}$$已知，則$$X$$為$$\mathcal{F}$$可測，但隨機過程只能知道現在和過去已經發生的值，未來發發生的事件仍為隨機，因此為$$\mathcal{F}_t$$可測。

一個隨機過程 $$X$$有兩種理解方式。

1. . 對於每個時間點$$t$$，$$X_t$$是一個隨機變數。
2. 對於每個樣本$$\omega$$，$$X(\omega)$$是$$\mathbb{R}^d$$中的一條(實現)路徑。

### 過濾與適應過程(Filtrations and Adapted Processes)

什麼是$$X_t$$適應$$\mathcal{F}_t$$呢？那就是在同一時刻下，我能夠計算的機率不會超出我的知識範圍。隨著「能形成看待的事物的知識範圍」不斷增大，這樣就組成了一個filtration(過濾或資訊流)。

而適應(adapted)則體現了$$X$$隨時間的可測性變化，也就是說，如果現在的時間是$$t$$ ，就能夠觀測(計算)$$X_t$$的值。

舉例來說，一個隨機過程的natural filitration包含了該過程的所有過去歷史資訊。一個隨機過程是與它的natural filtration adapted的。

在一個適應的世界中，過去和現在的事件和實現值是已知且不可改變的，但未來是隨機的和未知的。這就是它的全部內容。數學建模必須尊重這一現實世界的事實。

<mark style="color:blue;">Filtration 可以被想成是資訊的揭露</mark>。如$$\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2\subseteq \cdots$$，亦即表示在時間$$t=1$$的時候，我們亦可知道時間 $$t=0$$  的情況，亦即 $$t=1$$  的時候包含了  $$t=0$$  的資訊，但 不包含 $$t=2$$  (未來)的資訊。

任意的$$t<s$$ ，可得$$\mathcal{F}_t \subseteq \mathcal{F}_s$$ 。若是按照sigma代數作為隨機事件“資訊”的直觀理解，這實際上是說隨著時間的推進，我們對這個隨機過程所獲得的資訊是“單調增加”的。<mark style="color:blue;">通常我們會把</mark>$$\mathcal{F}_t$$ <mark style="color:blue;">看作（或者取作）截止到時間</mark>$$t$$ <mark style="color:blue;">所能獲取的所有有關這個隨機過程的資訊</mark>。那麼$$X_t$$ adapted to $$\mathcal{F}_t$$ 的直觀意思實際上就很簡單了，就是說在時間$$t$$我們才能知道$$X_t$$ 的值應該是多少。

<mark style="color:red;">濾波</mark>$$\lbrace \mathcal{F}_t \rbrace_{t \in T }$$ <mark style="color:red;">​ 定義了資訊的流動，它告訴我們隨著時間的推移，哪些事件和隨機變數可以被「知道」或「確定」</mark>。適應過程$$\lbrace X_t \}_{t\in T}$$則是在這個資訊流中「合法」的過程，它的當前值不會「超前」於當前可用的資訊。

一個過程是否是適應的， 總是相對於一個特定的濾波而言的。 同一個隨機過程，相對於不同的濾波，可能會有不同的適應性。 通常，當我們說一個過程是「適應的」而沒有明確指定濾波時， 我們通常指的是它相對於其 **自然濾波** 是適應的。

## 有限維分佈(finite-dimensional distributions, FDDs)

隨機過程是一個在實線上具索引值(index)的隨機變數集合。 簡單地說，就是「一堆用時間（index）連接起來的隨機變數」，但是它並不容易去表述性質，因為隨機過程是由無限個隨機變數組成的。

隨機過程的 **有限維分佈（finite-dimensional distributions, FDDs）** 是描述隨機過程行為的一種方式，它定義了過程在有限個時間點上的聯合分佈。這些有限維分佈提供了關於隨機過程在不同時間點上的統計性質的資訊。

Kolmogorov存在定理指出，如果給定了一系列滿足一致性條件的有限維分佈，那麼就存在一個隨機過程具有這些指定的有限維分佈。這一定理在理論上證明了為什麼僅僅通過指定隨機過程的所有有限維分佈就能完全確定該過程的機率規律。這種方法對於構建和處理隨機過程特別有用，尤其是在無法直接描述整個過程的分佈的情況下。

Kolmogorov 存在定理的方法是，將一段時間區間$$T$$，看成一堆離散的時間點$$t_1, t_2, \dots, t_n$$。然後把時間點對應到一堆隨機變數，接著將每個時間區間$$T$$的隨機變數各視為一個有限維分佈。假設這些有限維分佈都滿足一致性，我們就能建構出一個隨機過程、找到這過程對應的機率空間。

給定隨機過程$$X_t \equiv \{X_t, ~ t\in I\}$$，

在$$t=t_1$$時，對$$X_t$$而言，$$X_{t_1}$$為一維的隨機變數，其分佈函數為$$F_1(x_1)=\mathrm{P}(X_{t_1} \leq x_1)$$且機率密度函數為$$f_1(x_1)=\frac{\partial F_1(x_1)}{\partial x_1}$$。以此類推，可得一族機率分佈，稱為有限維機率分布函數。

> 定義：有限維分佈的隨機變數
>
> 給定任選的時間點集合$$t_1, t_2, \dots, t_n \in I$$，$$n \geq 1$$，則$$\{X_{t_1}, X_{t_2}, \dots, X_{t_n}\}$$為隨機過程$$X_t$$的有限維分佈的隨機變數族。
>
> 而聯合分佈$$\mathrm{P}(X_{t_1}, \dots, X_{t_n})$$為有限維分佈。

可得有限維(累積)分佈為$$F_n(x_1, x_2, \dots, x_n; t_1, t_2, \dots, t_n)=\mathrm{P}(X_{t_1}\leq x_1, X_{t_2} \leq t_2, \dots, X_{t_n} \leq x_n)$$。

其機率密度函數為$$f_n(x_1, x_2, \dots, x_n; t_1, t_2, \dots, t_n)=\frac{\partial^n}{\partial x_1 \partial x_2 \dots \partial x_n} F_n(x_1, x_2, \dots, x_n; t_1, t_2, \dots, t_n)$$。

注意到這樣的有限維分佈有無限個，因為對於$$n \in [1, \infty]$$，任意的$$t_1, \dots ,t_n$$均有各自的有限維分佈。而隨機過程的隨機性，就是由所有的有限維分佈刻畫的，兩者相互等價。

用無限個有限邊緣分佈來刻畫一個隨機過程的隨機性，此個概念看起來不好理解，可參考高斯過程，高斯過程的任意有限邊緣分佈都是高斯分佈, 因此才被稱作高斯過程。

相當類似於隨機向量的分佈函數與機率密度函數。<mark style="color:blue;">但有限維分佈中的</mark>$$t_1, \dots, t_n$$<mark style="color:blue;">是任意選出的，並沒有特定的選擇方式，與隨機向量中要求序列性不同</mark>。

此做法類似於分析極限時，當$$n \rightarrow \infty$$時，事實上等同於分析$$X_t$$無限維度的性質。但有部份性質如隨機過程的樣本不連續或跳躍的性質無法用FDDs分析，因此FDDs還需滿足以下性質：

#### 對稱性(symmetric)

對於$$1,2,\dots, n$$的任意排列$$i_1, i_2, \dots, i_n$$，若有：

* $$F_n(x_1, x_2, \dots, x_n; t_1, t_2, \dots, t_n)=F_n(x_{i_1}, x_{i_2}, \dots, x_{i_n}; t_{i_1}, t_{i_2}, \dots, t_{i_n})$$或
* $$\mathrm{P}(X_{t_1}\leq x_1, X_{t_2} \leq t_2, \dots, X_{t_n} \leq x_n) = \mathrm{P}(X_{t_{i_1}}\leq x_{i_1}, X_{t_{i_2}} \leq t_{i_2}, \dots, X_{t_{i_n}} \leq x_{i_n})$$

即將$$X_t$$分佈的各個時間點$$t_i$$任意排列，其分佈並未因此改變，則此FDDs滿足對稱性條件。這意味著聯合分佈函數與時間點的順序無關。

#### 一致性(consistency)

對於$$m < n$$，若有：$$F_m(x_1, x_2, \dots, x_m; t_1, t_2, \dots, t_m)=F_n(x_1, x_2, \dots, x_m, \infty, \dots, \infty ; t_1, t_2, \dots, t_m, t_{m+1}, \dots, t_n)$$

即將觀察時刻任意增加，FDDs也不會因此改變。

也就是說，當你考慮更少的時間點時，分佈函數應該是通過邊緣化（即積分或取極限）得到的。

<mark style="background-color:red;">根據Kolmogorov存在定理，如果一組有限維分佈滿足上述對稱性和一致性條件，那麼就存在一個機率空間和一個定義在此空間上的隨機過程，其有限維分佈正好就是給定的那些分佈</mark>。

### 有限維分佈的例子

* 設 {B(t), t ≥ 0} 是一個標準布朗運動。布朗運動的任何有限維分佈都是明確的多元常態分佈。
* 設 {N(t), t ≥ 0} 是一個強度為 λ 的卜瓦松過程。我們可以很容易地描述其任意有限維時間點上的聯合機率。
* 對於一個離散時間馬可夫鏈 {Xn, n = 0, 1, 2, ...}，其有限維分佈由初始分佈 P(X0 = i) 和轉移機率 P(Xn+1 = j | Xn = i) 完全決定。

## 隨機過程與時間序列的比較

| **比較專案** | **隨機過程（Stochastic Process）** | **時間序列（Time Series）** |
| -------- | ---------------------------- | --------------------- |

| **性質** | 一組隨機變數的集合 | 隨機過程的一個實現 |
| ------ | --------- | --------- |

| **數學描述** | $$X_t$$ 是隨機變數 | $$x_t$$​ 是確定性數值 |
| -------- | ------------- | --------------- |

| **時間範圍** | 可為無限長 | 通常有限長  |
| -------- | ----- | ------ |

| **型別** | 可能為連續時間或離散時間 | 一般為離散時間 |
| ------ | ------------ | ------- |

| **應用領域** | 理論建模、金融數學、物理系統 | 實際資料分析、經濟學、工程學 |
| -------- | -------------- | -------------- |

| **例子** | 布朗運動、泊松過程、馬可夫鏈 | 股票價格、氣溫記錄、GDP 變化 |
| ------ | -------------- | ---------------- |



## 參考資料

[https://www.zhihu.com/question/22717561/answer/661424720](https://www.zhihu.com/question/22717561/answer/661424720)




