# 最小遺憾

## 簡介

Hannon在重複向量報酬賽局的背景下首次提出了外部遺憾最小化策略的概念，而重複賽局的（外部和內部）遺憾最小化策略略可以作為可接近性問題的一個特殊實例得出。

遺憾是指當決策者意識到她採取其它行動可能會有更好結果時的感覺。在不確定的環境中，<mark style="color:red;">遺憾的概念是決策者採取某種策略所獲得的報酬與該狀態下的最大可得報酬之間的差異，後者是決策者本可以獲得但沒有獲得的報酬</mark>。任何策略的基本要求是避免或至少減少遺憾。

在雙人零和重複賽局$$\Gamma$$​中，玩家的目標是選取好的策略$$s_{1,t} \in \Delta(\mathcal{A}_1)$$​以最大化累積報酬$$\sum_{t=1}^T u(s_{1,t}, s_{2,t}), ~ s_{2,t} \in \Delta(\mathcal{A}_2)$$。此處最大化報酬是考慮對手在每一期可能採取的所有策略$$s_{2,t}$$。

<mark style="color:red;">更具體地說，玩家的外部遺憾是指在對手的一系列行動中，實際獲得的累積報酬與事後看到的最佳固定策略所能獲得的報酬之差值。外部遺憾最小化策略保證在面對任何對手的策略時，它的表現(報酬)幾乎與事後已知的最佳固定策略一樣好，這樣的策略也稱為Hannan一致策略。</mark>一個外部遺憾最小化策略保證了遺憾在時間上的亞線性增長，也就是說，其遺憾的增長速度為$$o(T)$$。

因為在解釋遺憾的概念時，使用一組策略與一組行動具有相同的意義，為了簡化符號，在下面的討論中會使用行動的集合。外部遺憾和外部遺憾最小化策略的定義如下。

外部遺憾：假設有$$P$$​個專家，若已經知道$$T$$​期中第$$i$$​個專家的專家預測能力最好，則外部遺憾為固定第$$i$$​個專家在$$1 \sim T$$​期的累積報酬與使用演算法\$$用$$s_{1, 1:T}\equiv\{s_{1,1}, s_{1,2}, \dots, s_{1,T}\}$$配置權重後累積報酬，兩者的差值。

內部遺憾：

* 外部遺憾中，演算法$$s_{1, 1:T}$$比較的對象是單一專家(行動或單純策略)的累積報酬，即使該專家在途中可能部份期間報酬不高，但只要累積報酬夠高，仍然會被選中。
* 內部遺憾中，演算法$$s_{1, 1:T}$$比較的對象是一組專家加權後(混合策略)的累積報酬

## 外部遺憾與最小外部遺憾演算法(external regret and external regret miimization algorithm)

> 考慮雙人零和重複賽局$$\Gamma$$​，玩家的行動集合為$$\mathcal{A}_1=\{a_{1}^1,a_{1}^2,\dots, a_{1}^{p}\}$$。玩家的外部遺憾為一混合策略$$s_{1,t}$$的累積報酬相對於已知$$\mathcal{A}_1$$最佳固定行動的累積報酬之差值：
>
> * $$\displaystyle \mathrm{ER}(s_{1, 1:T}) = \max_{a_1^i \in \mathcal{A}_1} \sum_{t=1}^T u(a_1^i, s_{2,t}) - \sum_{t=1}^T u(s_{1,t}, s_{2,t})$$
> * &#x20;其中$$s_{1, 1:T}=\{s_{1,1}, s_{1,2}, \dots, s_{1,T} \}$$為玩家在時間1至$$T$$的策略軌跡。​

一個外部遺憾最小化的策略$$s_{1,t}$$​滿足$$\mathrm{ER}(s_{1, 1:T}) = o(T)$$。即$$\displaystyle \lim_{T \rightarrow \infty } \frac{1}{T} \mathrm{ER}(s_{1, 1:T}) = 0$$。

納許均衡正是一組相互之間都沒有外部遺憾的策略。然而，有許多簡單的賽局，其最小化遺憾的策略並不接近納許均衡，甚至比任何納許均衡的表現都要差得多。在一個雙人零和賽局中，一個外部遺憾最小化策略可以保證接近或超過賽局的最小值。

## 內部遺憾與最小內部遺憾演算法(internal regret and internal regret minimization algorithm)

外部遺憾的一種更強形式是內部遺憾。內部遺憾允許玩家修改線上行動序列，將每一個給定的行動改為一個替代行動。

> 考慮雙人零和重複賽局$$\gamma$$​，玩家的行動集合為$$\mathcal{A}_1=\{a_{1}^1,a_{1}^2,\dots, a_{1}^{p}\}$$。
>
> 混合策略$$s_{1,t}$$​的累積報酬可寫為以下形式：
>
> * $$\displaystyle  \sum_{t=1}^t u(s_{1,t}, s_{2,t}) = \sum_{t=1}^T \sum_{i=1}^P s_{1,t}[a_1^i](u(a_1^i, s_{2,t})$$
> * 其中$$s_{1,t}[a_1^i]$$為混合策略中，行動$$a_1^i$$被選中的機率。
>
> <mark style="color:red;">玩家的內部遺憾是一混合策略</mark>$$s_{1,t}$$​<mark style="color:red;">的累積報酬，相對於在事先知道該混合策略每一個時間點應使用行動</mark>$$a_1^j$$​<mark style="color:red;">而不是行動</mark>$$a_1^i$$​<mark style="color:red;">的累積報酬，記為</mark>$$s_{1,t}^{i \rightarrow j}$$。
>
> 混合策略$$s_{1,t}^{i \rightarrow j}$$即將策略$$s_{1,t}$$中，行動$$a_1^i$$的機率設為0，而行動$$a_1^j$$的機率為加總值$$s_{1,t}[a_1^i] + s_{1,t}[a_1^j]$$，而其它行動的機率不變。也稱為$$i \rightarrow j$$​修改策略(modified strategy)。
>
> 可得玩家的內部遺憾為：
>
> * $$\displaystyle  \mathrm{IR}(s_{1, 1:T}) = \max_{(a_1^i,a_1^j) \in \mathcal{A}_1 \times \mathcal{A}_1} \sum_{t=1}^T u(s_{1,t}^{i \rightarrow j}, u_{2,t}) - \sum_{t=1}^T u(s_{1,t}, s_{2,t})$$
> * 由定義可得每期$$t$$​都可依累積報酬調整是否要將機率(權重)由$$i \rightarrow j$$。

一個內部遺憾最小化的策略$$s_{1,t}$$​滿足$$\mathrm{IR}(s_{1,1:T})=o(T)$$。

### 外部遺憾與內部遺憾的不等式

> 玩家的混合策略$$s_{1,t}$$​的外部遺憾，必定不會大於$$P$$​倍的相同混合策略的內部遺憾。
>
> 即 $$\mathrm{ER}(s_{1, 1:T}) \leq P \times \mathrm{IR}(s_{1, 1:T})$$。

proof:

玩家混合策略$$s_{1,t}$$​的外部遺憾為：

$$\displaystyle  \begin{aligned} \mathrm{ER}(s_{1,1:T}) & = \max_{i=1,2,\dots, P} \sum_{t=1}^T u(a_1^i, s_{2,t}) - \sum_{t=1}^T u(s_{1,t} - u_{2,t}) \\ 	& =  \max_{i=1,2,\dots, P} \sum_{t=1}^T u(a_1^i, s_{2,t}) - \sum_{t=1}^T \sum_{j=1}^P s_{1,t}[a_1^j]u(a_1^j, s_{2,2}) \\ 	& = \max_{i=1,2,\dots, P} \left\{  		\sum_{j=1}^P \sum_{t=1}^T s_{1,t}[a_1^j](u(a_1^i, s_{2,t}) - u(a_1^j, s_{2,t})) 	\right\} \\ 	& = \max_{j=1,2,\dots, P} \left\{  		\sum_{i=1}^P \sum_{t=1}^T s_{1,t}[a_1^i](u(a_1^j, s_{2,t}) - u(a_1^i, s_{2,t})) 	\right\} \\ \end{aligned}$$相同混合策略的內部遺憾為：

$$\displaystyle  \begin{aligned} \mathrm{IR}(s_{1,1:T}) & = \max_{(a_1^i, a_1^j) \in \mathcal{A}_1 \times \mathcal{A}_1} 	\sum_{t=1}^T u(s_{1,t}^{i \rightarrow j}, s_{2,t}) - \sum_{t=1}^T u(s_{1,t}, s_{2,t}) \\ 	& =  \max_{(a_1^i, a_1^j) \in \mathcal{A}_1 \times \mathcal{A}_1} 	\sum_{t=1}^T s_{1,t}[a_1^i] (u(a_1^j, s_{2,t}) - u(a_1^i, s_{2,t})) \end{aligned}$$

比較上述$$\mathrm{ER}(s_{1,1:T})$$與$$\mathrm{IR}(s_{1,1:T})$$可得不等式：

$$\displaystyle    \max_{j=1,2,\dots, P} \left\{  		\sum_{i=1}^P \sum_{t=1}^T s_{1,t}[a_1^i](u(a_1^j, s_{2,t}) - u(a_1^i, s_{2,t})) 	\right\} \leq P \times \max_{(a_1^i, a_1^j) \in \mathcal{A}_1 \times \mathcal{A}_1} 	\sum_{t=1}^T s_{1,t}[a_1^i] (u(a_1^j, s_{2,t}) - u(a_1^i, s_{2,t}))$$(QED)

### 成對遺憾(pairwise regret)

> 定義成對遺憾$$\displaystyle R_{s_{1, 1:T}}^{i \rightarrow j} = \sum_{t=1}^T s_{1,t}[a_1^i] (u(a_1^j, s_{2,t}) -  u(a_1^i, s_{2,t}))$$

* 若$$R_{s_{1, 1:T}}^{i \rightarrow j}  >0$$，表示玩家選擇行動$$i$$​的累積報酬小於選行動$$j$$​的累積報酬，因此玩家對於選行動$$i$$而不是行動$$j$$感到遺憾。
* 反之$$R_{s_{1, 1:T}}^{i \rightarrow j}  \leq 0$$表示玩家對選擇行動$$i$$​不會感到遺憾。
* 因此玩家只要注意$$(R_{s_{1, 1:T}}^{i \rightarrow j} )^{+}$$即可。

當玩家的混合策略$$s_{1,t}$$​滿足$$\displaystyle \lim_{T \rightarrow \infty} \frac{1}{T} R_{s_{1, 1:T}}^{i \rightarrow j} =0 \text{ a.s. }$$時，則$$\mathrm{IR}(s_{1,1:T}) = o(T)$$，即$$s_{1,t}$$​為內部遺憾最小化的策略。



## 雙人零和重複賽局必存在內部遺憾最小化的策略
