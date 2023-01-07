---
description: follow-the-winner投資組合策略
---

# 投資組合策略CRP,UP

## 策略分類

* follow-the-winner: UP, EG, AUP, ONS。
* follow-the-loser: Anticor, PAMR, OLMAR, robust mean, CWMR。
* pattern-matching: B-H, B-K, B-S, B-NN, B-MV, B-GV。
* meta: follow the leading history, OGU, ONU。

賽局理論中，regret-minimization algorithm也可以用於投資組合中，但要注意是否有考慮到手續費。不考慮手續費的模型只適用於理論收斂性質分析或是meta方法，而其子方法必須有考慮手續費才行。

## 基本符號

投資標的為$$M$$個資產，且市場在離散時間$$t=1,2,\dots, T$$演變。

價格的相對向量(price relative vector)$$\mathbf{x}_t=(x_{1,t}, x_{2,t}, \dots, x_{M,t}) \in \mathbb{R}_{++}^{M}$$，$$\displaystyle x_{i,t}=\frac{p_{i,t}}{p_{i, t-1}}=r_{i,t} + 1$$為當期與前期收盤價的比值。由連續複利公式得$$\log x_{i,t} \approx r_{i,t}$$。

令時間$$t$$的投資組合策略(portoflio strategy)或權重(weight)向量為$$\mathbf{w}_t(\mathbf{x}_{1:t})\equiv \mathbf{w}_t =(w_{1,t}, w_{2,t}, \dots, w_{M,t}) \in \Delta_M~ t=1,2,\dots, T$$，其中

* 期初的權重$$\mathbf{w}_0$$為使用者自行決定要配置權重，通常設為相同權重。
* 在決定當期的權重$$\mathbf{w}_t$$時，會參考資產的歷史價格變動資料$$\mathbf{x}_{1:t}$$，而決定第$$t$$期權重的時間點是在第$$t$$期的收盤價已知時，使用當期的價格決定權重。
* $$\Delta_M=\left\{ \mathbf{w} \in \mathbb{R}_{+}^M ~|~ \mathbf{w}^\top \mathbf{1} = 1 \right\}$$(M維simplex)，即時間$$t$$時，投資在$$M$$筆資產的權重總和必須為1且$$\mathbf{w}_t \succeq \mathbf{0}$$表示只能做多或空手，不能放空。
* 注意在第$$t$$期決定權重$$\mathbf{w}_t$$後，到第$$t+1$$期收盤價已知時，權重會因為$$\mathbf{x}_{t+1}$$的變化，使得調整前的權重總合不為1，調整前的權重為$$\displaystyle \tilde{\mathbf{w}}_{t+1}=\frac{\mathbf{w}_t}{\mathbf{w}_t^\top \mathbf{x}_{t+1}}$$，而調整後的權重為$$\mathbf{w}_{t+1}$$。

## 不考慮手續費的投資組合

由於每期的權重$$\mathbf{w}_{t}$$在經過價格變動$$\mathbf{x}_{t+1}$$後，不會與$$\mathbf{w}_{t+1}$$一致，因此需要進行買進或賣出，此處先不考慮交易手續費的模型。

令初始投資組合的資金(wealth)為$$v_{(p),0} >0$$，在經過$$T$$期的投資組合$$\mathbf{w}_{1:T}$$後，總資金變為$$\displaystyle v_{(p),T} \equiv v_{(p),T}(\mathbf{w}_{1:T}) =v_{(p),0} \prod_{t=1}^T \mathbf{w}_{t-1}^\top \mathbf{x}_t =v_{(p),0} \prod_{t=1}^T \left( \sum_{i=1}^M w_{i,t-1} x_{i,t} \right)$$

可得此投資組合$$T$$期j的平均報酬率為$$\displaystyle \overline{r}_{(p),T} = \frac{1}{T}\log \frac{v_{(p),T}} {v_{(p),0} } = \frac{1}{T}(\log v_{(p),T} - \log v_{(p),0}) =\frac{1}{T}\sum_{t=1}^T \log \left( \sum_{i=1}^M w_{i,t-1} x_{i,t} \right)$$

## 考慮手續費的投資組合

假設買進和買出的交易費用與交易金額成比例，令買進與賣出交易稅分別為$$c_{i,t}^{(buy)}, c_{i,t}^{(sell)}$$通常此費用不會變動，因此可省略下標$$t$$。

在時間$$t$$調整權重前，投資組合的資金為$$\displaystyle \tilde{v}_{(p),t} = v_{(p),t-1}\sum_{i=1}^M w_{i, t-1}x_{i,t}$$

投資人的目標是將調整前的權重$$\tilde{\mathbf{w}}_t$$調整為指定的權重$$\mathbf{w}_t$$，如果：

* 第$$i$$個資產在調整前的資金小於調整後的資金，表示買進該資產。即$$\tilde{v}_{(p),t}\tilde{w_{i,t}} < v_{(p),t} w_{i,t}$$。
* 反之若調整前的資金大於調整後的資金，表示賣出該資產，即$$\tilde{v}_{(p),t}\tilde{w_{i,t}} > v_{(p),t} w_{i,t}$$。
* 如果權重不變，表示不調整該資產。

因此可得：$$\displaystyle \begin{aligned} v_{(p),t} & = \tilde{v}_{(p),t} \\ & - \sum_{i=1}^M c_{i,t}^{(buy)} (v_{(p),t}w_{i,t} - \tilde{v}_{(p),t} \tilde{w}_{i,t})_{+} \\ & - \sum_{i=1}^M c_{i,t}^{(sell)} (\tilde{v}_{(p),t} \tilde{w}_{i,t} - v_{(p),t}w_{i,t} )_{+} \end{aligned}$$--(1)

上式可利用交易費用因子(transaction cost factor) $$\displaystyle \gamma_t = \frac{v_{(p),t}}{\tilde{v}_{(p),t}} \in (0,1]$$簡化。

將(1)左右同除以$$\tilde{v}_{(p),t}$$可得：$$\displaystyle \gamma_t = 1 - \sum_{i=1}^M c_{i,t}^{(buy)} (v_{(p),t}w_{i,t} - \tilde{v}_{(p),t} \tilde{w}_{i,t})_{+} \\ - \sum_{i=1}^M c_{i,t}^{(sell)} (\tilde{v}_{(p),t} \tilde{w}_{i,t} - v_{(p),t}w_{i,t} )_{+}$$

由上式得$$\gamma_t$$可用$$\displaystyle \mathbf{w}_{t-1}, ~\mathbf{w}_t, ~\mathbf{x}_t$$唯一決定。

使用交易費用因子，期末投資組合資金可改寫為：$$\displaystyle v_{(p),T} \equiv v_{(p),T}(\mathbf{w}_{1:T}) =v_{(p),0} \prod_{t=1}^T \gamma_t \mathbf{w}_{t-1}^\top \mathbf{x}_t =v_{(p),0} \prod_{t=1}^T \left( \gamma_t \sum_{i=1}^M w_{i,t-1} x_{i,t} \right)$$

當上式$$\gamma_t=1, ~\forall t$$表示不考慮交易費用，則等價於不考慮交易費用的模型。

## 買進持有策略(buy-and-hold strategy)

給定初始權重$$\mathbf{w}_0$$，期間不重新調整投資組合的策略稱為買進持有(BAH)策略。經過$$T$$期後，資金變為：

$$\displaystyle v_{(p),T}^{(BAH)} \equiv v_{(p),T}^{(BAH)}(\mathbf{w}_0) = \sum_{i=1}^M \left( w_{i, 0} \prod_{t=1}^T x_{i,t} \right)$$

## 恆定再平衡投資組合(constant rebalanced portfolio)

CRP策略在期初決定好一組固定的權重$$\mathbf{w}$$，且在每一期經過價格變動$$\mathbf{x}_t$$後，再重新調整為指定的權重$$\mathbf{w}$$，因此須要付出高額的交易費用。

假設不考慮交易費用，則經過$$T$$期後，資金變為：

$$\displaystyle v_{(p),T}^{(CRP)} \equiv v_{(p),T}^{(CRP)}(\mathbf{w}) = \prod_{t=1}^T \left( \sum_{i=1}^M w_{i} x_{i,t} \right)$$

如果投資人已經知道未來所有的價格變動，即$$\displaystyle \mathbf{x}_{1:T}=\{\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T\}$$均為已知時，可反推得到具有最高報酬的權重$$\mathbf{w}^{*}$$，此權重稱為best CRP(BCRP)。

BCRP經過$$T$$期後，資金變為：

* $$\displaystyle \mathbf{w}^{*} = \argmax_{\mathbf{w} \in \Delta_M} \left( v_{(p), T}^{(CRP)}(\mathbf{w}) \right)$$
* $$\displaystyle v_{(p),T}^{(BCRP)} \equiv v_{(p),T}^{(BCRP)}(\mathbf{w}^{*}) = \prod_{t=1}^T \left( \sum_{i=1}^M w_{i}^{*} x_{i,t} \right)$$

由定義可得$$\displaystyle v_{(p),T}^{(CRP)}\leq v_{(p),T}^{(BCRP)} ~ \forall \mathbf{w} \in \Delta_M$$，且CRP策略中，可得到價格變動向量無論怎麼排列，都不會影到到期末的投資組合資金。

因為投資人不可能事先得知所有的價格變動向量，因此BCRP在實務上是不可能計算得出，但BCRP可做為基準值，投資人可調整權重使得$$T$$期之後的報酬相對於BCRP差距為0。

## 泛化投資組合(Universal portfolio)



## 參考資料

* T. M. Cover, “Universal portfolios,” Mathematical finance, vol. 1, pp. 1-29, 1991. \[第一篇提出UP的論文]&#x20;
* T. M. Cover and E. Ordentlich, "Universal portfolios with side information," Information Theory, IEEE Transactions on, vol. 42, pp. 348-363, 1996.&#x20;
* V. Vovk and C. Watkins, "Universal portfolio selection," in Proceedings of the eleventh annual conference on Computational learning theory, pp. 12-23, 1998 .&#x20;
* A. Blum and A. Kalai, "Universal portfolios with and without transaction costs," Machine Learning, vol. 35, pp. 193-205, 1999.
* [https://github.com/Marigold/universal-portfolios](https://github.com/Marigold/universal-portfolios)
