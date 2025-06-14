# 隨機過程

## 簡介

簡單來說，**隨機過程** 是一組隨機變數，這些隨機變數會隨著時間或其他索引引數而變化。您可以將其視為一個隨時間演變的隨機系統。

隨機過程的關鍵特性在於它結合了兩個基本元素：

1. 隨機性：系統在任何時間的狀態都具有不確定性
2. 時間演化：系統狀態隨時間變化

隨機過程可想像成一個隨時間（或其他索引）隨機變化的系統。在每一個時間點，系統的狀態都是一個隨機變數，其取值是不確定的，並遵循一定的機率分布。隨著時間的推移，這些隨機變數之間可能存在相互依賴的關係。

隨機過程可以根據時間和狀態的連續性或離散性進行分類：

* **時間與狀態均為離散**：例如投擲硬幣的結果。
* **時間離散但狀態連續**：例如離散時間下的正態分布。
* **時間連續但狀態離散**：例如一年內車禍理賠次數。
* **時間與狀態均為連續**：例如股票價格的波動。

在現實生活中有這樣一種不確定現象，它每次隨機試驗會持續一段時間，其可能結果是一個關於時間的函數。比如，我們收集$$t$$時間段內，電子元件的熱噪聲電壓。每次隨機試驗都可以得到一個$$X(t)$$的函數，而且每次試驗的函數曲線都不一樣。我們把試驗結果畫到同一個坐標系中，可以看到在$$t_0$$時刻，$$X(t_0)$$ 的結果有無數個且服從某一分佈，因此我們把這種不確定現象稱為隨機過程（Stochastic Process）。

機率論中，只討論隨機變數或是兩個隨機變數間的性質與分佈。而隨機過程討論是的一連串無限維度(離散或連續個)的隨機變數間的性質與分佈。

討論隨機過程有兩類方法：

1. 有限維隨機變數$$X_1, X_2, \dots, X_T$$的聯合機率分佈。
2. Σ域的公理化定義。

## 隨機過程（stochastic process）

> $$\{X(t),  \ t \in T\}$$為隨機變數的集合。隨機變數$$X(t)$$也常寫為$$X_t$$。
>
> * 指標$$t$$通常視為時間。<mark style="color:red;">而</mark>$$X_t \equiv X_t(\omega)$$<mark style="color:red;">稱為在時間</mark>$$t$$<mark style="color:red;">的狀態（state）</mark>。
> * 當索引集(index set) $$T$$為可數集合時，如$$T=\{0,1,2,\dots\}$$，稱為<mark style="color:blue;">離散時間隨機過程</mark>；當$$T$$為實數任一區間時，如$$T=[0,\infty), [0,a)$$，稱為<mark style="color:blue;">連續時間隨機過程</mark>。
> * 在任一時刻$$t$$的狀態，是連續型隨機變數或離散型隨機變數而分成連續變數隨機過程和離散變數隨機過程。
> * <mark style="color:red;">隨機過程除了考慮個別隨機變數</mark>$$X(t)$$<mark style="color:red;">的分佈外，還考慮了相異隨機變數</mark>$$X(t), X(s), t \neq s$$<mark style="color:red;">間的相關結構</mark>。
> * 在實際實驗中，常將連續時間隨機過程轉化為隨機數列處理，也即將引數集$$T$$劃分稱若干個離散的小區間$$T^{'}=\{ \Delta t, 2\Delta t, 3\Delta t, \ldots \}$$ 並在$$T^{'}$$上觀測樣本函數 $$X(t)$$ 。當$$\Delta t$$充分小時，這個隨機序列能夠近似描述連續引數隨機過程。
> * 對於樣本空間中的每一個特定的結果$$ω \in \Omega$$，當我們讓索引$$t$$在其定義域內變化時，我們會得到一個值的序列（如果時間是離散的）或一個函數（如果時間是連續的）。這個序列或函數稱為隨機過程的一個**樣本路徑(sample path)**&#x6216;**實現(realization)**。它代表了在特定隨機實驗結果下，隨機過程的演化過程。
>
> 公理化定義：
>
> 給定濾流(filitration)機率空間$$(\Omega, \mathcal{F}, \mathcal{F}_t, \mathrm{P})$$
>
> * 令$$X: [0, \infty) \times \Omega \rightarrow \mathbb{R}^d$$, $$(t, \omega) \mapsto X_t(\omega)$$。如果$$X$$是$$\mathcal{B}([0, \infty)) \otimes \mathcal{F}$$-可測函數（$$\mathcal{B}$$是Borel set），則稱$$X$$為隨機過程。
> * 給定$$\omega \in \Omega$$，$$X(\omega): [0, \infty) \rightarrow \mathbb{R}^d$$, $$t \mapsto X_t(\omega)$$稱為樣本路徑（sample path）。
> * 如果對於$$t \in [0, \infty)$$. $$X_t$$為$$\mathcal{F}_t$$-可測，則稱$$X$$為$$\{\mathcal{F}_t\}$$-的適應過程。
> * 假設全部的資訊$$\mathcal{F}$$已知，則$$X$$為$$\mathcal{F}$$可測，但隨機過程只能知道現在和過去已經發生的值，未來發發生的事件仍為隨機，因此為$$\mathcal{F}_t$$可測。

一個隨機過程 $$X$$有兩種理解方式。

1. . 對於每個時間點$$t$$，$$X_t$$是一個隨機變數。
2. 對於每個樣本$$\omega$$，$$X(\omega)$$是$$\mathbb{R}^d$$中的一條(實現)路徑。

### 過濾與適應過程(Filtrations and Adapted Processes)

什麼是$$X_t$$適應$$\mathcal{F}_t$$呢？那就是在同一時刻下，我能夠計算的機率不會超出我的知識範圍。隨著「能形成看待的事物的知識範圍」不斷增大，這樣就組成了一個filtration(濾流或資訊流)。此處的知識(資訊)依σ域的定義就是$$X_t(\omega)$$的實現值之前像為濾流$$\mathcal{F}_t$$中的元素，即$$X_t^{-1}(\omega) \in \mathcal{F}_t$$，或者寫為$$\sigma(X_t) \subseteq \mathcal{F}_t$$，換言之，就是$$X_t(\omega)$$的相異實現值對於$$\Omega$$形成了分割，而此分割必須是濾流中的元素才是可測(如果以離散的情境樹表示，在時間$$t$$的隨機變數$$X_t$$適應於$$\mathcal{F}_t$$，即$$X_t$$形成的路徑$$\omega$$，必須落在時間$$0 \sim t$$形成的情境樹的路徑中)。

而適應(adapted)則體現了$$X$$隨時間的可測性變化，也就是說，如果現在的時間是$$t$$ ，就能夠觀測(計算)$$X_t$$的值。

自然濾流<mark style="color:blue;">可以被想成是資訊的揭露</mark>。如$$\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2\subseteq \cdots$$，亦即表示在時間$$t=1$$的時候，我們亦可知道時間 $$t=0$$  的情況，亦即 $$t=1$$  的時候包含了  $$t=0$$  的資訊，但 不包含 $$t=2$$  (未來)的資訊。

一個隨機過程的自然濾流(natural filitration\_包含了該過程的所有過去歷史資訊。一個隨機過程適應於其自然濾流。因為隨機過程中的變數只能依賴歷史已發生的觀測值建模，對於但未來仍是隨機未知的。

任意的$$t<s$$ ，可得$$\mathcal{F}_t \subseteq \mathcal{F}_s$$ 。若是按照σ域作為隨機事件“資訊”的直觀理解，這實際上是說隨著時間的推進，我們對這個隨機過程所獲得的資訊是“單調增加”的。<mark style="color:blue;">通常我們會把</mark>$$\mathcal{F}_t$$ <mark style="color:blue;">看作（或者取作）截止到時間</mark>$$t$$ <mark style="color:blue;">所能獲取的所有有關這個隨機過程的資訊</mark>。那麼$$X_t$$ 適應於 $$\mathcal{F}_t$$ 的直觀意義是說在時間$$t$$我們才能知道$$X_t$$ 的值應該為何。

<mark style="color:red;">濾流</mark>$$\lbrace \mathcal{F}_t \rbrace_{t \in T }$$ <mark style="color:red;">​ 定義了資訊的流動，它告訴我們隨著時間的推移，哪些事件和隨機變數可以被「知道」或「確定」</mark>。適應過程$$\lbrace X_t \}_{t\in T}$$則是在這個資訊流中「合法」的過程，它的當前值不會「超前」於當前可用的資訊。

一個過程是否是適應的， 總是相對於一個特定的濾流而言的。 同一個隨機過程，相對於不同的濾流，可能會有不同的適應性。 通常，當我們說一個過程是「適應的」而沒有明確指定濾流時， 我們通常指的是它相對於其 **自然濾波** 是適應的。

#### 樣本空間不變

注意隨機過程中樣本空間$$\Omega$$是固定不變的：隨機過程的性質通常由其有限維分佈（即$$\{X(t_1,), X(t_2), \dots, X(t_n)\}, ~ t_i \in T$$) 的聯合分佈，這些分佈是在同一$$\Omega$$上定義的，但具體的測度或分佈可能隨$$t$$不同而變化，這不意味著$$\Omega$$本身改變。

同理濾流$$\mathcal{F}_t \subseteq \mathcal{F}$$是隨$$t$$增長的σ域，。但這只是描述資訊隨時間的演進(或者解釋為對$$\Omega$$中的分割的細化)，$$\Omega$$仍然是固定的。

## 有限維分佈(finite-dimensional distributions, FDDs)

隨機過程是一系列隨機變量的集合，通常以時間為索引。要完整描述這樣的過程，我們需要知道所有可能時間點上隨機變量的聯合分佈。然而，直接描述無窮多時間點的聯合分佈在數學上非常複雜，甚至可能是不可行的。因此，隨機過程的性質通常通過其**有限維分佈（finite-dimensional distributions, FDDs）** 來定義過程在有限個時間點上的聯合分佈。這些有限維分佈提供了關於隨機過程在不同時間點上的統計性質的資訊。

一個隨機過程的有限維分佈族是指由所有可能的有限時間點集合及其對應的聯合機率分佈所構成的集合。這個族包含了隨機過程在任何有限時間切片上的完整機率資訊。

Kolmogorov擴充定理指出，如果給定滿足一致性條件的有限維分佈，那麼就存在一個隨機過程具有這些指定的有限維分佈。這一定理在理論上證明了為什麼僅僅通過指定隨機過程的所有有限維分佈就能完全確定該過程的機率規律。這種方法對於構建和處理隨機過程特別有用，尤其是在無法直接描述整個過程的分佈的情況下。

更詳細的說，Kolmogorov 擴展定理的方法給定一段時間區間$$T$$，取出任意個有限時間點$$t_1, t_2, \dots, t_n$$。然後把時間點對應到一堆隨機變數$$(X_{t_1}, \dots, X_{t_n})$$，接著將每個時間區間$$T$$的隨機變數們視為一個有限維聯合機率分佈。假設這些有限維分佈都滿足一致性條件，我們就能建構出一個隨機過程與對應的機率空間。

如果兩個隨機過程具有相同的有限維分佈族（對於所有可能的有限時間點集合和所有$$n \neq 1$$），那麼它們在機率意義上是無法區分的。這意味著它們具有相同的統計特性和行為。

雖然隨機過程本身可能在無限的時間範圍內演化（如果索引集$$T$$是無限的，例如$$[0,\infty)$$），但我們可以通過研究其在任意有限個時間點上的行為來逐步理解其整體的隨機特性。

給定隨機過程$$X_t \equiv \{X_t, ~ t\in T\}$$，

在$$t=t_1$$時，對$$X_t$$而言，$$X_{t_1}$$為一維的隨機變數，其分佈函數為$$F_{t_1}(x_1)=\mathrm{P}(X_{t_1} \leq x_1)$$且機率密度函數為$$f_{t_1}(x_1)=\frac{\partial F_{t_1}(x_1)}{\partial x_1}$$。以此類推，可得一族機率分佈，稱為有限維機率分布函數。

> 定義：有限維分佈的隨機變數
>
> 給定任選的時間點集合$$t_1, t_2, \dots, t_n \in T$$，$$n \geq 1$$，則$$\{X_{t_1}, X_{t_2}, \dots, X_{t_n}\}$$為隨機過程$$X_t$$的有限維分佈的隨機變數族。
>
> 而聯合分佈$$\mathrm{P}(X_{t_1}, \dots, X_{t_n})$$為有限維分佈。

可得有限維(累積)分佈為$$F_{t_1,  \dots, t_n}(x_1, \dots, x_n)=\mathrm{P}(X_{t_1}\leq x_1,  \dots, X_{t_n} \leq x_n)$$。

其機率密度函數為$$f_{t_1, \dots, t_n}(x_1,\dots, x_n)=\frac{\partial^n}{\partial x_1  \dots \partial x_n}  F_{t_1, \dots, t_n}(x_1, \dots, x_n)$$。

注意到這樣的有限維分佈有無限個，因為對於$$n \in [1, \infty]$$，任意的$$t_1, \dots ,t_n$$均有各自的有限維分佈。而隨機過程的隨機性，就是由所有的有限維分佈刻畫的，兩者相互等價。

用無限個有限邊緣分佈來刻畫一個隨機過程的隨機性，此個概念看起來不好理解，可參考高斯過程，高斯過程的任意有限邊緣分佈都是高斯分佈, 因此才被稱作高斯過程。

相當類似於隨機向量的分佈函數與機率密度函數。<mark style="color:blue;">但有限維分佈中的</mark>$$t_1, \dots, t_n$$<mark style="color:blue;">是任意選出的，並沒有特定的選擇方式，與隨機向量中要求序列性不同</mark>。

此做法類似於分析極限時，當$$n \rightarrow \infty$$時，事實上等同於分析$$X_t$$無限維度的性質。但有部份性質如隨機過程的樣本不連續或跳躍的性質無法用有限維分佈分析，因此有限維分佈還需滿足以下兩個一致性條件(consistency conditions)：

#### 對稱性(symmetric)：聯合分佈函數與時間點的順序無關

對於$$t_1, \dots, t_n$$的任意排列$$t_{\pi(1)}, \dots, t_{\pi(n)}$$，若有：

* $$F_{t_1, \dots, t_n}(x_1,\dots, x_n)=F_{t_{\pi(1)}, \dots, t_{\pi(n)}}(x_{\pi(1)},\dots, x_{\pi(n)})$$或
* $$\mathrm{P}(X_{t_1}\leq x_1, X_{t_2} \leq t_2, \dots, X_{t_n} \leq x_n) = \mathrm{P}(X_{t_{\pi(1)}}\leq x_{t_{\pi(1)}},  \dots, X_{t_{\pi(n)}} \leq x_{t_{\pi(n)}})$$

即將$$X_t$$分佈的各個時間點$$t_i$$任意排列，其分佈並未因此改變，則此有限維分佈滿足對稱性條件。這意味著聯合分佈函數與時間點的順序無關。

<mark style="color:red;">對稱性確保了我們對隨機過程在不同時間點上的聯合行為的描述是內在一致的，不會因為我們列出時間點的順序不同而產生不同的機率</mark>。

#### 相容性或邊際化(compatibility or marginalization)：如果從n 個時間點的分佈中消去一些變數（例如通過積分或取極限），得到的邊際分佈應與較少時間點的有限維分佈一致。

對於$$m < n$$，若有：$$F_{t_1, t_2, \dots, t_m}(x_1, x_2, \dots, x_m)=F_{t_1, t_2, \dots, t_m, t_{m+1}, \dots, t_n}(x_1, x_2, \dots, x_m, \infty, \dots, \infty)$$

即將觀察時刻任意增加，有限維分佈也不會因此改變。也就是說，當你考慮更少的時間點時，分佈函數應該是通過邊緣化（即積分或取極限）得到的。

相容性條件（也稱為邊際化條件）要求當我們從一個包含更多時間點的聯合分佈中「忽略」掉某些時間點時，得到的邊際分佈必須與我們在只考慮這些剩餘時間點的有限維分佈族中直接指定的分佈一致。

如果不滿足相容性條件，我們可能會在描述同一組隨機變數的機率行為時得到不同的結果，這取決於我們是否將它們看作是更大集合的一部分。這表明我們指定的分布族並非來自一個單一的、一致的隨機過程。

對稱性保證了時間點順序的無關性，而相容性保證了不同維度的分佈之間的一致性，使得我們能夠從局部（有限個時間點）的機率行為推斷出整體（隨時間演化）的隨機過程的性質。

<mark style="background-color:red;">根據Kolmogorov存在定理，如果一組有限維分佈滿足上述一致性條件，那麼就存在一個機率空間</mark>$$(\Omega, \mathcal{F}, \mathrm{P})$$<mark style="background-color:red;">和一個定義在此空間上的隨機過程</mark>$$\{X_t\}_{t \in T}$$<mark style="background-color:red;">，使得任意個有限時間點</mark>$$t_1, \dots, t_n \in T$$，隨機變數$$(X_{t_1}, \dots, X_{t_n}$$)的聯合分佈<mark style="background-color:red;">就是給定的分佈</mark>。

### 有限維分佈的例子

* 設$$\{B_t, t\geq 0\}$$ 是一個標準布朗運動(連續時間與狀態的隨機過程)。布朗運動的任何有限維分佈都是明確的多元常態分佈。
* 設$$\{N_t, t \geq 0\}$$ 是一個強度為$$\lambda$$的泊松過程(連續時間與離散狀態的隨機過程)。我們可以很容易地描述其任意有限維時間點上的聯合機率。
* 對於一個離散時間馬可夫鏈$$\{X_t, ~t \in \mathbb{N}\}$$，其有限維分佈由初始分佈$$\mathrm{P}(X_0 = i)$$ 和轉移機率$$\mathrm{P}(X_{t+1} = j | X_t = i)$$ 完全決定。

## 隨機過程與時間序列的比較

| 項目       | 隨機過程(Stochastic Process）              | 時間序列（Time Series）                     |
| -------- | ------------------------------------- | ------------------------------------- |
| **定義**   | 一組隨機變量的集合，通常以時間或其他索引標記，描述隨機現象的演變。     | 一組按時間順序排列的觀測數據，通常是隨機過程在特定時間點上的實現（樣本）。 |
| **本質**   | 理論概念，表示隨機變量的概率分佈及其隨時間的依賴關係。           | 實際數據，是隨機過程的具體觀測結果或實例。                 |
| **範圍**   | 可以是連續時間（如布朗運動）或離散時間（如馬爾可夫鏈）。          | 通常是離散時間的數據點（如每日溫度、每月銷售額）。             |
| **數學描述** | $$F_{t_1, t_2, \ldots, t_n}$$定義其統計特性。 | $$x_1, x_2, \ldots, x_n$$表示。          |
| **例子**   | 布朗運動、泊松過程、高斯過程。                       | 股票價格的日收盤價、年度氣溫記錄。                     |
| **隨機性**  | 強調隨機性，關注概率分佈和隨機變量間的關係（如獨立性、平穩性）。      | 是隨機過程的單個實現，可能包含隨機性和確定性成分。             |
| **研究目的** | 建立模型，分析隨機現象的統計性質（如均值、協方差）。            | 分析數據趨勢、週期性、預測未來值。                     |
| **工具**   | 概率論（如 Kolmogorov 擴展定理）、馬爾可夫性、平穩性分析。   | 統計方法（如自相關、平滑技術）、時間序列模型（如 ARIMA）。      |
| **關係**   | 隨機過程是時間序列的理論基礎，提供概率框架。                | 時間序列是隨機過程的可觀測數據，是隨機過程的樣本路徑。           |
| **應用場景** | 理論建模（如金融中的價格波動、物理中的粒子運動）。             | 實際預測與分析（如經濟預測、天氣預報）                   |

## 參考資料

[https://www.zhihu.com/question/22717561/answer/661424720](https://www.zhihu.com/question/22717561/answer/661424720)




