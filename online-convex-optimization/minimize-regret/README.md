# 最小遺憾

## 簡介

Hannon在重複向量報酬賽局的背景下首次提出了外部遺憾最小化策略的概念，而重複賽局的（外部和內部）遺憾最小化策略略可以作為可接近性問題的一個特殊實例得出。

遺憾是指當決策者意識到她採取其它行動可能會有更好結果時的感覺。在不確定的環境中，<mark style="color:red;">遺憾的概念是決策者採取某種策略所獲得的報酬與該狀態下的最大可得報酬之間的差異，後者是決策者本可以獲得但沒有獲得的報酬</mark>。任何策略的基本要求是避免或至少減少遺憾。

在雙人零和重複賽局$$\Gamma$$​中，玩家的目標是選取好的混合策略$$s_{1,t} \in \Delta(\mathcal{A}_1),t=1,2,\dots,T$$​以最大化累積報酬$$\sum_{t=1}^T u(s_{1,t}, s_{2,t}), ~ \forall s_{2,t} \in \Delta(\mathcal{A}_2), t=1,2,\dots, T$$。此處最大化報酬是考慮對手在每一期可能採取的所有策略$$s_{2,t}$$。

<mark style="color:red;">更具體地說，玩家的外部遺憾是指在對手的一系列行動中，實際獲得的累積報酬與事後看到的最佳固定策略所能獲得的報酬之差值。外部遺憾最小化策略保證在面對任何對手的策略時，它的表現(報酬)幾乎與事後已知的最佳固定策略一樣好，這樣的策略也稱為Hannan一致策略。</mark>一個外部遺憾最小化策略保證了遺憾在時間上的亞線性增長，也就是說，其遺憾的增長速度為$$o(T)$$。

因為在解釋遺憾的概念時，使用一組策略與一組行動具有相同的意義，為了簡化符號，在下面的討論中會使用行動的集合。外部遺憾和外部遺憾最小化策略的定義如下。

<mark style="color:red;">外部遺憾</mark>：假設有$$P$$​個專家，若已經知道$$T$$​期中第$$i$$​個專家的專家預測能力最好，則外部遺憾為固定第$$i$$​個專家在$$1 \sim T$$​期的累積報酬與使用演算法$$s_{1, 1:T}\equiv\{s_{1,1}, s_{1,2}, \dots, s_{1,T}\}$$配置權重後累積報酬，兩者的差值。

<mark style="color:red;">內部遺憾</mark>：

* 外部遺憾中，演算法$$s_{1, 1:T}$$比較的對象是單一專家(行動或單純策略)的累積報酬，即使該專家在途中可能部份期間報酬不高，但只要累積報酬夠高，仍然會被選中。
* 內部遺憾中，演算法$$s_{1, 1:T}$$比較的對象是自已採取第$$i$$​個行動，換成採取第$$j$$​個行動，但權重不變時的累積報酬，比較的對象是演算法內部的行動。而$$i \rightarrow j$$​的修改策略只有更換一個行動的權重而已。比較更換全部行動的策略稱為交換遺憾(swap regret)。

比如說在年初投資三個股票台積電、聯發科、鴻海，使用演算法動態調整權重到年底。可依投資在三隻股票上的權重計算累積報酬且算出投資組合報酬。

* 外部遺憾就是比較只投資其中一隻股票的最大報酬與投資組合報酬的差值。
* 因為有3隻股票，可得到6個修改策略權重(0, 台積電+聯發科, 鴻海)，(0, 聯發科, 台積電+鴻海)，(台積電+聯發科,0,鴻海)，(台積電,0, 聯發科+鴻海 ), (台積電+鴻海, 聯發科, 0)，(台積電，聯發科+鴻海, )，可得6個修改策略的累積報酬，其中最大的累積報酬與投資組合累積報酬的差值即為內部遺憾。

## 外部遺憾與最小外部遺憾演算法(external regret and external regret miimization algorithm)

> 考慮雙人零和重複賽局$$\Gamma$$​，玩家的行動集合為$$\mathcal{A}_1=\{a_{1}^1,a_{1}^2,\dots, a_{1}^{P}\}$$。玩家的外部遺憾為一混合策略$$s_{1,t}$$的累積報酬相對於已知$$\mathcal{A}_1$$最佳固定行動的累積報酬之差值：
>
> * $$\displaystyle \mathrm{ER}(s_{1, 1:T}) = \max_{a_1^i \in \mathcal{A}_1} \sum_{t=1}^T u(a_1^i, s_{2,t}) - \sum_{t=1}^T u(s_{1,t}, s_{2,t})$$
> * &#x20;其中$$s_{1, 1:T}=\{s_{1,1}, s_{1,2}, \dots, s_{1,T} \}$$為玩家在時間1至$$T$$的策略軌跡(strategy trajectory或歷史history)。​

一個外部遺憾最小化的策略$$s_{1,t}$$​滿足$$\mathrm{ER}(s_{1, 1:T}) = o(T)$$。即$$\displaystyle \lim_{T \rightarrow \infty } \frac{1}{T} \mathrm{ER}(s_{1, 1:T}) = 0$$。

納許均衡正是一組相互之間都沒有外部遺憾的策略。然而，有許多簡單的賽局，其最小化遺憾的策略並不接近納許均衡，甚至比任何納許均衡的表現都要差得多。在一個雙人零和賽局中，一個外部遺憾最小化策略可以保證接近或超過賽局的最小值。

## 內部遺憾與最小內部遺憾演算法(internal regret and internal regret minimization algorithm)

外部遺憾的一種更強形式是內部遺憾。內部遺憾允許玩家修改線上行動序列，將每一個給定的行動改為一個替代行動。

> 考慮雙人零和重複賽局$$\gamma$$​，玩家的行動集合為$$\mathcal{A}_1=\{a_{1}^1,a_{1}^2,\dots, a_{1}^{P}\}$$。
>
> 混合策略$$s_{1,t}$$​的累積報酬可寫為以下形式：
>
> * $$\displaystyle  \sum_{t=1}^t u(s_{1,t}, s_{2,t}) = \sum_{t=1}^T \sum_{i=1}^P s_{1,t}[i](u(a_1^i, s_{2,t})$$
> * 其中$$s_{1,t}[i]$$為混合策略中，第$$i$$個行動$$a_1^i$$被選中的機率。
>
> <mark style="color:red;">玩家的內部遺憾是一混合策略</mark>$$s_{1,t}$$​<mark style="color:red;">的累積報酬，相對於在事先知道該混合策略每一個時間點應使用行動</mark>$$a_1^j$$​<mark style="color:red;">而不是行動</mark>$$a_1^i$$​<mark style="color:red;">的累積報酬，記為</mark>$$s_{1,t}^{i \rightarrow j}$$。
>
> 混合策略$$s_{1,t}^{i \rightarrow j}$$即將策略$$s_{1,t}$$中，行動$$a_1^i$$的機率設為0，而行動$$a_1^j$$的機率為加總值$$s_{1,t}[i] + s_{1,t}[j]$$，而其它行動的機率不變。也稱為$$i \rightarrow j$$​修改策略(modified strategy)。
>
> 因為行動集合有$$P$$​的元素，因此修改策略有$$P \times (P-1)$$​種組合(因為$$i \rightarrow i$$​和原始策略相同)，注意修改策略只有考慮更換一個行動機率，而不是多個行動的機率。
>
>
>
> 可得玩家的內部遺憾為：
>
> * $$\displaystyle  \mathrm{IR}(s_{1, 1:T}) = \max_{(a_1^i,a_1^j) \in \mathcal{A}_1 \times \mathcal{A}_1} \sum_{t=1}^T u(s_{1,t}^{i \rightarrow j}, u_{2,t}) - \sum_{t=1}^T u(s_{1,t}, s_{2,t})$$
> * 由定義可內部遺憾是在全部結果已知時，把演算法策略軌跡$$s_{1,1:T}$$中，$$P \times (P-1)$$種修改策略均計算累積報酬，其中具有最大累積報酬的修改策略與演算法的累積報酬之差值。

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

> 定義累積成對遺憾$$\displaystyle R_{s_{1, 1:T}}^{i \rightarrow j} = \sum_{t=1}^T s_{1,t}[i] (u(a_1^j, s_{2,t}) -  u(a_1^i, s_{2,t}))$$
>
> 時間$$t$$​的成對遺憾為$$\displaystyle R_{s_{1, t}}^{i \rightarrow j} =  s_{1,t}[i] (u(a_1^j, s_{2,t}) -  u(a_1^i, s_{2,t}))$$
>
> 此處的$$u(\cdot, \cdot)$$是報酬函數，價值越高越好；如果是損失函數$$d(\cdot, \cdot)$$則是損失越小越好。

* 若$$R_{s_{1, 1:T}}^{i \rightarrow j}  >0$$，表示玩家選擇行動$$i$$​的累積報酬小於選行動$$j$$​的累積報酬，因此玩家對於選行動$$i$$而不是行動$$j$$感到遺憾。
* 反之$$R_{s_{1, 1:T}}^{i \rightarrow j}  \leq 0$$表示玩家對選擇行動$$i$$​不會感到遺憾。
* 因此玩家只要注意$$(R_{s_{1, 1:T}}^{i \rightarrow j} )^{+} \equiv \max(0, R_{s_{1, 1:T}}^{i \rightarrow j})$$即可。

當玩家的混合策略$$s_{1,t}$$​滿足$$\displaystyle \lim_{T \rightarrow \infty} \frac{1}{T} R_{s_{1, 1:T}}^{i \rightarrow j} =0 \text{ a.s. }$$時，則$$\mathrm{IR}(s_{1,1:T}) = o(T)$$，即$$s_{1,t}$$​為內部遺憾最小化的策略。



## 雙人零和重複賽局必存在內部遺憾最小化的策略

為了使用[Blackwell可接近定理](../../game-theory/blackwells-approachability-theorem/#blackwell-ke-jie-jin-ding-li-approachability-theorem-bat)證明內部遺憾最小化策略的存在性，先定義雙人零和重複向量賽局$$\Gamma_v$$​與目標集合$$S$$​。

因為玩家的行動集合$$\mathcal{A}_1 = \{a_1^1, a_1^2, \dots, a_1^P \}$$有$$P$$​個元素，可得$$P^2$$​個修改策略$$s_{t}^{i \rightarrow j}$$，注意修改策略$$s_{1,t}^{i \rightarrow i} \equiv s_{1,t}$$，且成對遺憾(pairwise regret)，其中$$R_{s_{1, 1:T}}^{i \rightarrow i} =0, ~ i=1,2,\dots, P$$。

令在時間$$t$$​時，玩家採取第$$i$$個行動$$a_1^i$$​的報酬向量為$$\mathbf{u}_t \in \mathbb{R}^{P^2}$$，其中前$$(i-1)P$$個元素值為0；第$$(i-1)P+k$$個元素值等於$$u(a_1^k, s_{2,t}) - u(a_1^i, s_{2,t}), ~ k=1,2,\dots, P$$；剩下的元素值均為0。

* 例如$$\mathcal{A}_1 = \{1,2,3 \}$$,&#x20;
* 第1個行動報酬向量為$$(u(a_1^1, s_{2,t}) - u(a_1^1, s_{2,t}), u(a_1^2, s_{2,t}) - u(a_1^1, s_{2,t}), u(a_1^1, s_{2,t}) - u(a_1^3, s_{2,t}), 0, 0, 0, 0, 0, 0)$$。
* 成對遺憾寫法為$$s_{1,t}[1]( R_{t}^{1 \rightarrow 1}, R_{t}^{1 \rightarrow 2}, R_{t}^{1 \rightarrow 3}, 0,0,0,0,0,0)$$，因為權重不影響向量方向，所以可省略。
* 第2個行動報酬向量為$$(0, 0, 0,  u(a_1^1, s_{2,t}) - u(a_1^2, s_{2,t}), u(a_1^2, s_{2,t}) - u(a_1^2, s_{2,t}), u(a_1^2, s_{2,t}) - u(a_1^3, s_{2,t}) , 0, 0, 0)$$。
* 成對遺憾寫法為$$s_{1,t}[2]( 0,0,0, R_{t}^{2 \rightarrow 1}, R_{t}^{2 \rightarrow 2}, R_{t}^{2 \rightarrow 3} ,0,0,0)$$。
* 第三個行動報酬向量為：$$(0, 0, 0, 0, 0, 0, u(a_1^1, s_{2,t}) - u(a_1^3, s_{2,t}), u(a_1^2, s_{2,t}) - u(a_1^3, s_{2,t}), u(a_1^3, s_{2,t}) - u(a_1^3, s_{2,t})  )$$
* 成對遺憾寫法為$$s_{1,t}[3]( 0,0,0, 0,0,0, R_{t}^{3 \rightarrow 1}, R_{t}^{3 \rightarrow 2}, R_{t}^{3 \rightarrow 3}  )$$。

<mark style="color:red;">目標集合為負象限</mark> $$S=\mathbb{R}_{-}^{P^2} \equiv \left\{  x \in \mathbb{R}^{P^2} \big| x_i \leq 0, i=1,2,\dots, P^2 \right\}$$。

* 假設平均報酬最後落在零點，則所有的成對遺憾$$R_{s_{1, 1:T}}^{i \rightarrow j}  =0$$，因此沒有內部遺憾。
* 如果平均報酬落在某個$$-x_i$$軸上時，表示行動$$i$$​的報酬比某些行動(但不是全部的行動)​的報酬高(>)，而與其它行動的報酬差不多(=)，即$$R_{s_{1, 1:T}}^{i \rightarrow j} \leq 0, ~\forall j \neq i$$。

為了接近集合$$S$$​，使用[Blackwell可接近演算法](../../game-theory/blackwells-approachability-theorem/#blackwell-adaptive-strategy-shou-lian-xing-fen-xi)令現在向量平均成對遺憾為$$\overline{u}_t \in \mathbb{R}^{P^2}$$，則向量內的元素為時間$$1 \sim t$$​的平均成對遺憾平均值$$\frac{1}{t}\{R^{i \rightarrow j}_{s_{1, 1:t}} \}$$所組成。定義$$y_t= \mathrm{proj}_{S}(\overline{u}_t)$$為平均成對遺憾投影至集合的點。因此超平面法向量為$$w_t = (\overline{u}_t  -  y_t)^{+} = [\frac{1}{t} R_{s_{1, 1:t}}^{i \rightarrow j}]^{+}, ~ \forall i, j$$。

* 如果$$\overline{u}_t \in \mathbb{R}^{P^2 +}$$，則$$w_t = \overline{u}_t - y_t$$，則$$y_t=0$$。
* 如同上述3個行動的範例，在每一期時，可得3個行動報酬，經過$$t$$​期後，可得每個行動的累積報酬，因為為實數值，必可排名，假設是2 > 1 >3，則第2個行動向量報酬小於0，第1個行動向量中有1個元素大於0，第3個行動向量中有兩個元素大於0，而我們只需要處理大於0的元素即可。

為了決定$$t+1$$​期時的混合策略$$s_{1,t+1}$$​使得報酬$$u_{t+1}$$​必定落在半空間$$H_{\overline{u}_t ~ y_t}^{(L)}$$，首先考慮當$$u_{t+1}=\left[R^{i \rightarrow j}_{s_{1, t+1}} \right] = [s_{1, t+1}[i](u(a_1^j, s_{2,t+1}- u(a_1^i, s_{2,t+1}))], ~\forall i, j$$​直接落在超平面$$H_{\overline{u}_t ~ y_t} =\left\{  z \in \mathbb{R}^{P^2} \big| w_t^\top z = 0 \right\}$$的情形，因為集合$$S$$為非負象限，因此超平面必定經過0點，所以超平面截距項為0。

* 為何$$s_{1,t+1}$$使得$$u_{t+1}$$落在$$H_{\overline{u}_t ~ y_t}$$超平面上? 因為根據Blackwell可接近定理，當玩家選定策略$$s_{1,t+1}$$​後，不論對手使用任意策略$$s_{2,t+1}$$​，報酬必須落在$$H_{\overline{u}_t ~ y_t}^{(L)}$$​才能保證集合$$S$$​的可接近性。因此假設$$u_{t+1}$$​落在超平面$$H_{\overline{u}_t ~ y_t}$$​隱含著報酬$$u(s_{1,t+1}, s_{2,t+1})$$是能夠使$$\overline{u}_t$$​接近集合$$S$$速度最慢的報酬(最差的報酬)，只要對手不是使用此特定混合策略，$$\overline{u}_t$$接近速度會更快。

當向量$$s_{1,t+1}$$在每一期$$t$$都滿足下式時，則$$S$$為可接近集合：$$\displaystyle  \sum_{i=1}^P \sum_{j=1}^P s_{1,t+1}[i] (u(a_1^j, s_{2,t+1})- u(a_1^i, s_{2,t+1})) \frac{1}{t} (R_{s_{1,1:t}}^{i \rightarrow j})^{+} =0$$

可改寫為：$$\displaystyle \begin{aligned} & \sum_{i=1}^P \sum_{j=1}^P s_{1,t+1}[i] u(a_1^j, s_{2,t+1}) \frac{1}{t} (R_{s_{1,1:t}}^{i \rightarrow j})^{+}  -  \\ & \sum_{j=1}^P \sum_{i=1}^P s_{1,t+1}[j]  u(a_1^j, s_{2,t+1}) \frac{1}{t} (R_{s_{1,1:t}}^{j \rightarrow i})^{+}  = 0  \\ & \rightarrow \sum_{i=1}^P \sum_{j=1}^P u(a_1^j, s_{2,t+1}) \left[   s_{1,t+1}[i] R_{s_{1,1:t}}^{i \rightarrow j})^{+} -    s_{1,t+1}[j] R_{s_{1,1:t}}^{j \rightarrow i})^{+}   \right] = 0   \end{aligned}$$

因為對手在時間$$t+1$$​可能採取任意行動$$s_{2,t+1} \in \Delta(\mathcal{A}_2)$$，因此$$u(a_1^j, s_{2,t+1}) \neq 0$$， ,為了使上式為0，對於玩家的所有行動$$i$$​必須滿足：

$$\displaystyle \sum_{j=1}^P  \left[ s_{1,t+1}[i] (R_{s_{1, 1:t}}^{i \rightarrow j})^{+}  - s_{1,t+1}[j] (R_{s_{1, 1:t}}^{j \rightarrow i})^{+}   \right] = 0$$

令矩陣$$\mathbf{A} = [a_{ij}] \in \mathbb{R}^{P^2}$$為$$a_{ij} = R_{s_{1,1:t}}^{j \rightarrow i}, ~ \forall i \neq j$$且$$\displaystyle a_{ii} = - \sum_{j=1, j \neq i}^P R_{s_{1,1:t}}^{i \rightarrow j}$$，注意矩陣每一列(row)的總和為0。

* 以3個行動為例，$$\mathbf{A}=  \begin{bmatrix}  -R_{s_{1, 1:t}^{1 \rightarrow 2}} - R_{s_{1, 1:t}^{1 \rightarrow 3}}    & R_{s_{1, 1:t}^{2 \rightarrow 1}} & R_{s_{1, 1:t}^{3 \rightarrow 1}} \\ R_{s_{1, 1:t}^{1 \rightarrow 2}} &  R_{s_{1, 1:t}^{2 \rightarrow 1}} - R_{s_{1, 1:t}^{2 \rightarrow 3}}  & R_{s_{1, 1:t}^{3 \rightarrow 2}} \\ R_{s_{1, 1:t}^{1 \rightarrow 3}} & R_{s_{1, 1:t}^{2 \rightarrow 3}} &  - R_{s_{1, 1:t}^{3 \rightarrow 1}} - R_{s_{1, 1:t}^{3 \rightarrow 2}} \end{bmatrix}$$

則上式可改寫為矩陣式$$\mathbf{A} s_{1, t+1} = 0$$且我們要得到非簡單解$$s_{1,t+1} \succeq 0$$。

將矩陣$$\mathbf{A}$$​正規化為$$\tilde{A}$$，其中$$\displaystyle \tilde{a}_{ij}=\frac{a_{ij}}{\max_{i,j}|a_{ij}|}$$，因此$$\tilde{a}_{ij} \leq 1$$且$$\sum_{i=1}^P \tilde{a}_{ij} =0$$。

令矩陣$$\mathbf{P = \tilde{A} + I}$$ ，$$I$$為$$P \times P$$維的單位矩陣，則$$\mathbf{P}$$為每一列(row)總和為1的機率矩陣(row stochastic matrix)，則存在非負的機率向量$$s_{1, t+1}$$滿足$$\mathbf{P}s_{1, t+1} = s_{1, t+1}$$。

求上式的特徵值分解如下：

$$\begin{aligned}  & \mathbf{P}s_{1, t+1} & = s_{1, t+1} \\ \Rightarrow & (\mathbf{\tilde{A} + I}) s_{1, t+1} & = s_{1, t+1} \\ \Rightarrow & \mathbf{\tilde{A}} s_{1, t+1} & = \mathbf{0} \\ \Rightarrow & \mathbf{A} s_{1, t+1} & = \mathbf{0} \\ \end{aligned}$$

因此$$s_{1, t+1}$$可由$$\mathbf{A}s_{1, t+1} = s_{1, t+1}$$的特徵值分解中$$\lambda=1$$​的特徵向量求得(QED)。
