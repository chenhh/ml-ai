---
description: simple market model
---

# 簡單市場模型

## 常用符號

參考[投資組合策略](../convex-optimization/portfolio-strategy/)。

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

> 風險資產在未來的價格$$S(1)$$是隨機變數，至少有兩個以上的可能實現值。
>
> 無風險資產未來的價格$$A(1)$$為已知的值(因為在$$t=0$$時，已知利率，因此可由現在$$A(0)$$得到未來的價格)

### 價格的正性

> $$S(t) >0, ~ A(t) > 0, ~ t=0,1$$

此假設在一般的金融商品成立，但在2020年曾經出現石油價格為負值。

### 投資組合

> 投資人在時間$$t=0,1$$時，若持有$$x$$單位股票(風險資產)與$$y$$單位債券(無風險資產)，則$$(x,y)$$稱為投資組合(註：$$x>0$$為做多(long)，$$x<0$$時為做空(short)，$$x=0$$時為不持有資產，同理$$y$$也是相同解釋)。

令投資人在時間$$t$$的財產(wealth)為$$V(t)=xS(t)+yA(t)$$，則報酬率為$$R_V=\frac{V(1)}{V(0)}-1$$。

範例：

無風險資產價格$$A(0)=100, ~A(1)=110$$，因此報酬率為$$R_A=10\%$$。

風險資產價格$$S(0)=50$$，$$\displaystyle S(1) = \left\{ \begin{aligned} & \mathrm{P}(S(1)=52) = p \\ & \mathrm{P}(S(1)=48) = 1-p \end{aligned} \right.$$，對應的報酬為$$\displaystyle R_S = \left\{ \begin{aligned} & 0.04 &\text{ if stock goes up } \\ & -0.04& \text{ if stock goes down } \end{aligned} \right.$$

風險資產價格$$S(0)=50$$，$$\displaystyle S(1) = \left\{ \begin{aligned} & \mathrm{P}(S(1)=52) = p \\ & \mathrm{P}(S(1)=48) = 1-p  \end{aligned} \right.$$，對應的報酬為$$\displaystyle R_S = \left\{ \begin{aligned} & 4\% &\text{ if stock goes up } \\ & -4\%& \text{ if stock goes down }  \end{aligned} \right.$$

如果時間$$t=0$$的投資組合$$(x,y)=(20,10)$$，可得$$V(0)=20\times 50 + 10 \times 100 = 2000$$。

時間$$t=1$$時，投資組合的價值：$$\displaystyle V(1) = \left\{ \begin{aligned} 20 \times 52 + 10 \times 110 & = 2140 & \text{ if stock goes up } \\ 20 \times 48 + 10 \times 110 & = 2060 & \text{ if stock goes down}  \end{aligned}  \right.$$

因此投資組合的報酬率$$\displaystyle R_V = \left\{ \begin{aligned} 7\% & \text{ if stock goes up } \\ 3\% & \text{ if stock goes down}  \end{aligned}  \right.$$

### 可分性、流動性與放空

> 令$$x \in \mathbb{R}, ~ y \in \mathbb{R}$$，正值代表作多(long)，負值代表放空(short)，0代表不持有資產。

令持有數量為實數而非整數可避免NP-Complete或NP-Hard的問題，且當投資的部位夠大時，確實能夠逼近任意實數。

令持有數量為任意實數另一個考量就是不考慮流動性(bid-ask spread)的問題，以及大量買進或賣出時造成的市場衝擊(大量買進時會因為買進的行為造成股價上漲，反之會因為賣出的行為造成股價的下跌)。

### 償付能力

> 投資人的財產總是為非負值，即$$V(t) \geq 0, ~ t=0,1$$。

滿足此條件的投資組合$$(x,y)$$稱為可允許(admissable)的投資組合。

### 離散單位價格

> 風險資產的未來價格$$S(1)$$為有限多個值的隨機變數。

在當日漲跌沒有上/下限的股市此性質不一定成立，而台股有限值每日漲跌停為$$\pm 10\%$$，且股價有限制跳動點位，因此性質成立。

## 無套利原則(一價原則)(no-arbitrage principle)

> 假設市場不允許沒有初始投資的無風險利潤
>
> 即不存在可允許的投資組合$$(x,y)$$使得$$V(0)=0$$，但是$$V(1) >0$$的非0機率。

如果市場上出現了套利機會，且被人們發現，則此機會會因為人們為了套利的交易很快就消失(以現今市場電子交易的速度，大約1\~2秒內馬上消失)。

另一個無套利原則的應用是在使用抽樣分佈(情境，scenario)以及使用隨機規劃(stochastic programming)替投資組合建模時，如果情境中存在套利機會時，則可能會產生錯誤的投資組合解。

### 如果不可同時做多與放空時，不存在套利機會

> 若$$x \geq 0$$且$$y \geq 0$$時，不存在$$V(0)=0$$但$$V(1) >0$$的非0機率。
>
> 若$$x \leq 0$$且$$y \leq 0$$時，不存在$$V(0)=0$$但$$V(1) >0$$的非0機率。

proof:

不失一般性，只考慮做多的情形。

由價格的正性，即$$S(t) >0, A(t) >0 \forall t$$，可得$$V(0)=0 \Leftrightarrow x=0  \text{ and }  y=0$$

因此在$$(x,y)=(0,0)$$的情形下，無論$$S(1)$$與$$A(1)$$之值為0，必定得到$$V(1)=0$$，因此無套利機會(QED)。



範例：套利機會



## 單期二元樹模型

## 風險與報酬

## 遠期合約(forward contract)

## 買權與賣權(call and put)

## 參考資料

* Marek Capinski and Tomasz Zastawniak, Mathematics for finance: an introduction to financial engineering, 1st, Springer, 2002.
