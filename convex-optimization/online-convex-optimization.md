---
description: 'online tw: 線上, cn:在線'
---

# 線上凸最佳化

## 簡介

online convex optimization(OCO)與game theory中的external regret, internal regret以及information theory中的universal portfolio的概念均有相關, 但是特別強化了對於一般化問題的最佳化方法。

在許多實際應用中，環境非常的復雜，以至於制定一個全面的理論模型並使用經典的演算法理論和數學最佳化通常是不可行的。因此採取穩健的方法是必要且有益的，即通過應用一種邊走邊學的最佳化方法，隨著問題的更多資料被觀察到，從經驗中學習。

## 線上凸最佳化模型（The online convex optimization model）

線上凸最佳化中，一個線上玩家迭代地（多期）做出決定。而在每一期做決定時，與選擇相對應的結果對玩家來說是未知的（<mark style="color:red;">選擇之後，才知道報酬/ 損失</mark>）。

在每一期作出決定後，玩家（決策者）會遭受損失：每個可能的決定都會產生一個（可能不同的）損失。這些損失對決策者來說是事先未知的。損失可以是對抗性選擇，甚至取決於決策者採取的行動。

因此為了使上述的決策框架合理有意義，以下兩個限制是必要的：

* 不允許對手給予玩家的損失是沒有界限的。否則，對手可以不斷增大玩家每次決定（行動）的損失規模，而無法使演算法從第一次決策的損失中恢復過來。<mark style="color:red;">**因此，我們假設損失位於某個有界的區域**</mark>。
* <mark style="color:red;">**決策集（行動集）必須有一定的界限和/或結構**</mark>，盡管不一定是有限的。  為了理解為什麼這一點是必要的，請考慮具有無限可能的決策集。對手可以無限期地給玩家選擇的所有策略分配較高損失，而把一些損失為零的策略分開。因此玩家不管怎麼選定決策，損失都會不斷擴大。

令人驚訝的是，有趣的結果和演算法可以在不超過這兩個限制的情況下得出。

### OCO模型結構

<mark style="color:red;">線上凸最佳化（online convex optimization, OCO）將決策(行動)集合建模為歐式空間</mark>$$\mathbb{R}^n$$<mark style="color:red;">中的凸集合</mark> $$\mathcal{K} \subseteq \mathbb{R}^n$$。<mark style="color:red;">而成本（cost）建模為以</mark>$$\mathcal{K}$$<mark style="color:red;">為定義域的有界凸函數集合</mark>$$\mathcal{F}$$。

**OCO可視為結構化的（雙人）重複賽局（structured repeated game）**，結構如下：

* 在第$$t$$期（決策）時，線上玩家從決策集合選取當期的行動$$\mathbf{x}_t \in \mathcal{K}$$，假設總共有$$T$$期($$T$$可趨近$$\infty$$)。
* 執行行動後，當期的成本函數 $$f_t \in \mathcal{F}: \mathcal{K} \rightarrow \mathbb{R}$$才會揭露。此處的$$\mathcal{F}$$是對手有界成本凸函數集合。而線上玩家本次決策的成本為$$f_t(\mathbf{x}_t)$$。

由於OCO使用了賽局理論的方法，因此演算法$$\mathcal{A}$$的評量也是使用賽局理論中的<mark style="color:red;">**遺憾（regret）**</mark>做為度量。<mark style="color:red;">**將決策者的遺憾定義為她所承擔的總成本與事後(in hindsight)的最佳固定行動(決策)的成本之間的差異**</mark>。

$$
regret_T(\mathcal{A})= \sup_{ \{f_1, f_2, \ldots, F_T\} \subseteq \mathcal{F}} \bigg\{  \sum_{t=1}^Tf_t(\mathbf{x}_t^{\mathcal{A}}) - \min_{x \in \mathcal{K}} \sum_{t=1}^T f_t(\mathbf{x})  \bigg\}
$$

事後最佳固定決策指的是假設玩家已經事先看到對手所有的資料與結果$$f_1, f_2, \ldots, f_T$$，每一期都採取固定行動後，有最小成本的某個固定行動$$\mathbf{x}$$。

而演算法$$\mathcal{A}$$在每一期採用的是混合策略$$\mathbf{x}_t^{\mathcal{A}} = \mathcal{A}(f_1, \dots, f_{t-1}) \in \mathcal{K}$$或簡寫為$$\mathbf{x}_t$$，每期依照歷史(已實現)成本動態調整行動。在賽局理論中，兩者行動總成本的差值稱為<mark style="color:red;">外部遺憾（external regret）</mark>。

如果演算法的遺憾相對於時間$$T$$為<mark style="color:blue;">次線性（sublinear）</mark>，即$$regret_T(\mathcal{A}) = o(T)$$( $$\lim_{T\rightarrow \infty} \frac{regret_T(\mathcal{A})}{T} = 0$$)，表示演算法的遺憾增長速度比時間$$T$$慢，因此只要$$T$$夠大，演算法的遺憾相對於$$T$$最後會收斂至0，<mark style="color:blue;">即演算法的表現最後會和事先看到最佳固定行動一樣好</mark>。

演算法$$\mathcal{A}$$在第$$t$$期產生行動$$\mathbf{x}_t$$的時間複雜度，與$$t \in T$$有關（可能要使用到$$1,2,\ldots, t$$期的歷史資料），與$$\mathbf{x}_t$$的維度$$n$$有關，與總決策期數$$T$$有關，以及成本函數$$f_t$$的維度有關。

## 線上凸最佳化（OCO）的範例

### 從專家建議中預測（experts problem）

<mark style="color:red;">決策者每期要從</mark>$$n$$<mark style="color:red;">個專家中的建議，選一個做為行動，而在行動之後，會得到損失0或1</mark>。每一期行動後，每個專家建議的行動獲得的損失均不相同（專家的建議甚至可能是故意說錯的，以誤導決策者），**決策者的目標是要和（事後來看）最佳的決策者表現的一樣好**。

* 決策集合$$\mathcal{K}$$有$$n$$個元素（專家），因此決策集合為$$n$$維的單純形(simplex)，$$\mathcal{K}=\Delta_n=\{ \mathbf{x} \in \mathbb{R}^n,~ \sum_{i=1}^n x_i = 1, ~ x_i \geq 0 \}$$，是$$n$$個元素的任意線性組合集合。
* 令第$$i$$個專家在第$$t$$的損失（成本）為$$g_t(i) \in \{ 0, 1\}$$，$$\mathbf{g}_t \equiv[g_t(1), g_t(2), \ldots, g_t(n)]$$為第$$t$$期時，$$n$$個專家的損失（成本）向量。則第$$t$$期的成本函數為$$f_t(\mathbf{x})=\mathbf{g}_t^{\top} \mathbf{x}$$。

註：在賽局理論中，行動為$$n$$個行動的線性組合指的是<mark style="color:red;">混合策略（mixed strategy）</mark>，即第$$i$$個行動被選中的機率為$$x_i$$。行動被選中的機率符從[Dirichlet分佈](https://en.wikipedia.org/wiki/Dirichlet\_distribution)。

### 線上垃圾郵件過濾（online spam filtering）

電子郵件進入系統的時候，會自動被分類為垃圾/有效（spam/valid）郵件，而廣告商會依系統的特性，動態產生郵件的內容以避免被判定為垃圾郵件。

首先確定字典檔有$$d$$個單字，因此得輸入向量$$\mathbf{x} \in \mathbb{R}^d$$，$$\mathbf{x}$$每一個元素預設值均為0。電子郵件中出現的單字若有出現在字典中，則在$$\mathbf{x}$$對應的索引值改為1。

假設目前有過濾器$$\mathbf{x} \in \mathbb{R}^d$$（實務中通常會限定此向量的Euclidean norm的範圍），給定郵件$$\mathbf{a} \in \mathbb{R}^d$$，計算兩者的內積得 $$\hat{y} = \mathrm{sign} \langle x, a\rangle \in \{-1,1\}$$，$$\hat{y}=1$$表示有效郵件，$$\hat{y}=-1$$表示垃圾郵件。

* 決策集合$$\mathcal{K}$$為過濾器$$\mathbf{x}$$事件訂定的Euclidean norm範圍，通常為Eucildean ball。
* 令郵件與其真實的類別為$$(\mathbf{a}, y)$$，而過濾器的成本為$$f(\mathbf{x})=l(\hat{y}, y)$$, $$l(\cdot, \cdot)$$是凸函數，常用$$l(\hat{y}, y)=(\hat{y} - y)^2$$。

### 線上最短路徑（online shortest path）

給定有向圖$$G=(V,E)$$以及起點、終點$$u, v \in V$$。

* 在每一期$$t$$決策時，決策者都必須選擇一條圖中由$$u$$至$$v$$的路徑$$p_t \in \mathcal{P}_{u,v}$$，其中 $$\mathcal{P}_{u,v} \subseteq E^{|V|}$$為圖中所有由$$u$$至$$v$$路徑的集合，長度可能為$$1,2,\ldots, |V|$$。
* 而對手可獨立的選擇圖中任意邊的權重向量$$\mathbf{w}_t : E \rightarrow \mathbb{R}, ~ \mathbf{w}_t \in \mathbb{R}^{|E|}$$
* 因此玩家每次決定路徑後的損失為該路徑所有權重的總和，即 $$\sum_{e \in p_t} \mathbf{w}_t(e)$$。

將這個問題離散地描述為一個專家問題，即我們對每條路徑都有一個專家，這對效率是一個挑戰。就圖的大小而言，可能有許多路徑是指數級的。

* \[flow的值為1]$$\displaystyle \sum_{e=(u,w), ~w \in V} x_e = 1 = \sum_{e=(w,v)~ w\in V} x_e$$
* \[flow convervation] $$\displaystyle \forall w \in V - \{u, v\} ~ \sum_{e=(v,x) \in V} x_e = 1 = \sum_{e=(x,v) \in E} x_e$$
* \[capacity constraints] $$\forall e \in E, ~ 0 \leq x_e \leq 1$$

### 投資組合選取（portfolio selection）

Universal portfolio (UP)模型不對股票市場做任何統計假設（與標准的股票價格幾何布朗運動模型相反)。

在每一回合$$t \in [T]$$，投資人對他的$$n$$個資產權重選定分佈(權重)$$x_t \in \Delta n$$(simplex)。而對手(大盤)會獨立的給出此$$n$$個資產當期的報酬$$r_t \in \mathbb{R}^n$$(嚴格的說是相對價格$$p_t = r_t+1$$)。

而投資人的財產變化為$$r_t^\top x_t$$，因為多期的報酬是連乘，一般會取對數變成相加得$$\log(r_t^\top x_t)$$。

註：即使投資人兩期的權重相等，如$$x_t=x_{t+1}$$，但是因此資產的價格會變動，因此在$$t+1$$時即使權重不變，還是要調整配置在資產上的金額才會滿足條件。

* 目標函數為最小化遺憾 $$\displaystyle \min \left\{  \max_{x^{*} \in \Delta_n} \sum_{t=1}^T \log(r_t^\top x^{*}) - \sum_{t=1}^T \log(r_t^\top x_t)  \right\}$$
* 第一項為使用已知最佳固定權重$$x^{*}$$投資$$T$$期的總資產，雖然每一期權重固定，但仍必須每期調整資產，因此稱為constant rebalanced portfolio (CRP)。
* 第二項是決策者每期調整權重$$\{x_1, x_2, \dots, x_T\}$$投資$$T$$期後的總資產。
* 而Cover提出的UP模型可得$$o(T)$$的演算法使得遺憾對時間為次線性，但UP的缺點是對於資產$$n$$較大時，取樣值為指數成長，因此有些論文針對此缺點改善。

### 矩陣完成和推薦系統（matrix completion and recommendation systems）













## 參考資料

* \[\*\*\*]Elad Hazan, "Introduction to online convex optimization." arXiv preprint arXiv:1909.05207 (2019).
*   Nicolo Cesa-Bianchi and Gabor Lugosi. Prediction, Learning, and

    Games. Cambridge University Press, 2006.
*   S. Boyd and L. Vandenberghe. Convex Optimization. Cambridge

    University Press, March 2004.
