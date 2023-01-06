---
description: simple market model
---

# 簡單市場模型

## 常用符號

參考[投資組合策略](../convex-optimization/portfolio-strategy.md)。



## 基本假設

* 隨機性(randomness)
* 價格的正性(positive of price)
* 可分性、流動性與放空(divisibliy, liquidity and short selling)
* 償付能力(solvency)
* 離散單位價格
* 無套利原則(no-arbitrage principle)

假設只有一個風險(risky)資產與一個無風險(risk-free)資產形成的投資組合(portfolio)，且投資只有兩期$$t=0$$是現在，$$t=1$$是未來。

* 風險資產的價格為$$S(t)$$，報酬率為$$R_s=\frac{S(1)}{S(0)}-1$$為隨機變數。
* 無風險資產的價格為$$A(t)$$，報酬率為$$R_A=\frac{A(1)}{A(0)}-1$$為已知的值。

### 隨機性

風險資產在未來的價格$$S(1)$$是隨機變數，至少有兩個以上的可能實現值。

無風險資產未來的價格$$A(1)$$為已知的值(因為在$$t=0$$時，已知利率，因此可由現在$$A(0)$$得到未來的價格)

### 價格的正性

$$S(t) >0, ~ A(t) > 0, ~ t=0,1$$

此假設在一般的金融商品成立，但在2020年曾經出現石油價格為負值。

### 投資組合

投資人在時間$$t=0,1$$時，若持有$$x$$單位股票(風險資產)與$$y$$單位債券(無風險資產)，則$$(x,y)$$稱為投資組合(註：$$x>0$$為做多(long)，$$x<0$$時為做空(short)，$$x=0$$時為不持有資產，同理$$y$$也是相同解釋)。

令投資人在時間$$t$$的財產(wealth)為$$V(t)=xS(t)+yA(t)$$，則報酬率為$$R_V=\frac{V(1)}{V(0)}-1$$。

範例：

無風險資產價格$$A(0)=100, ~A(1)=110$$，因此報酬率為$$R_A=10%$$。

風險資產價格$$S(0)=50$$，$$\displaystyle S(1) = \left\{ \begin{aligned} & \mathrm{P}(S(1)=52) = p \\ & \mathrm{P}(S(1)=48) = 1-p  \end{aligned} \right.$$，對應的報酬為$$\displaystyle R_S = \left\{ \begin{aligned} & 0.04 &\text{ if stock goes up } \\ & -0.04& \text{ if stock goes down }  \end{aligned} \right.$$

如果時間$$t=0$$的投資組合$$(x,y)=(20,10)$$，可得$$V(0)=20\times 50 + 10 \times 100 = 2000$$。

時間$$t=1$$時









## 無套利原則(一價原則)(no-arbitrage principle)



## 單期二元樹模型

## 風險與報酬

## 遠期合約(forward contract)

## 買權與賣權(call and put)



## 參考資料

* Marek Capinski and Tomasz Zastawniak, Mathematics for finance: an introduction to financial engineering, 1st, Springer, 2002.
