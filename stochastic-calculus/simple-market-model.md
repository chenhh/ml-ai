---
description: simple market model
---

# 簡單市場模型

## 簡介

考慮風險資產(risky asset)如股票(stock)、無風險資產(risk-free asset)如債券(bond)或定存(deposit)、遠期合約(forward contract)與選擇權(option)形成的投資組合在無套利原則(no-arbitrage principle)下的定價模型。

## 常用符號

參考[投資組合策略](../online-convex-optimization/portfolio-strategy/)。

## 基本假設

* 隨機性/離散單位價格(randomness)：風險資產的未來價格為隨機變數，且風險資產的未來價格為有限個實現值。
* 價格的正性(positive of price)：所有資產價格大於等於0。
* 可分性、流動性與放空(divisibliy, liquidity and short selling)：一定可買賣任意數量(實數)的商品。
* 償付能力(solvency)：投資組合的價值在投資過程中必定大於等於0 。



* <mark style="color:red;">無套利原則(no-arbitrage principle)：不存在無初始資產的無風險利潤</mark>。

假設只有一個風險(risky)資產與一個無風險(risk-free)資產形成的投資組合(portfolio)，且投資只有兩期$$t=0$$是現在，$$t=1$$是未來。

* 風險資產的價格為$$S(t)$$，報酬率為$$R_s=\frac{S(1)}{S(0)}-1$$為隨機變數。
* 無風險資產的價格為$$A(t)$$，報酬率為$$R_A=\frac{A(1)}{A(0)}-1$$為已知的值。

### 隨機性/離散單位價格

> 風險資產在未來的價格$$S(1)$$是隨機變數，至少有兩個以上的可能實現值。
>
> 無風險資產未來的價格$$A(1)$$為已知的值(因為在$$t=0$$時，已知利率，因此可由現在$$A(0)$$得到未來的價格)
>
> 風險資產的未來價格$$S(1)$$為有限多個值的隨機變數。

離散單位價格在當日漲跌沒有上/下限的股市此性質不一定成立，而台股有限值每日漲跌停為$$\pm 10\%$$，且股價有限制最小跳動單位，因此性質成立。

### 價格的正性

> $$S(t) >0, ~ A(t) > 0, ~ t=0,1$$

此假設在一般的金融商品成立，<mark style="color:red;">但在2020年曾經出現石油價格為負值，而此存在資產為負值的選擇權定價模型</mark>。

### 投資組合(portfolio)

> 投資人在時間$$t=0,1$$時，若持有$$x$$單位股票(風險資產)與$$y$$單位債券(無風險資產)，則$$(x,y)$$稱為投資組合(註：$$x>0$$為做多(long)，$$x<0$$時為做空(short)，$$x=0$$時為不持有資產，同理$$y$$也是相同解釋)。

令投資人在時間$$t$$的財產(wealth)為$$V(t)=xS(t)+yA(t)$$，則報酬率為$$R_V=\frac{V(1)}{V(0)}-1$$。

範例：

無風險資產價格$$A(0)=100, ~A(1)=110$$，因此報酬率為$$R_A=10\%$$。

風險資產價格$$S(0)=50$$，$$\displaystyle S(1) = \left\{ \begin{aligned} & \mathrm{P}(S(1)=52) = p \\ & \mathrm{P}(S(1)=48) = 1-p  \end{aligned} \right.$$，對應的報酬為$$\displaystyle R_S = \begin{cases}  4\% &\text{ if stock goes up } \\  -4\%& \text{ if stock goes down }  \end{cases}$$

如果時間$$t=0$$的投資組合$$(x,y)=(20,10)$$，可得$$V(0)=20\times 50 + 10 \times 100 = 2000$$。

時間$$t=1$$時，投資組合的價值：$$\displaystyle V(1) =  \begin{cases} 20 \times 52 + 10 \times 110 & = 2140 & \text{ if stock goes up } \\ 20 \times 48 + 10 \times 110 & = 2060 & \text{ if stock goes down}  \end{cases}$$

因此投資組合的報酬率$$\displaystyle R_V = \left\{ \begin{aligned} 7\% & \text{ if stock goes up } \\ 3\% & \text{ if stock goes down}  \end{aligned}  \right.$$

### 可分性、流動性與放空

> 令$$x \in \mathbb{R}, ~ y \in \mathbb{R}$$，正值代表作多(long)，負值代表放空(short)，0代表不持有資產。

令持有數量為實數而非整數可避免NP-Complete或NP-Hard的計算複雜度問題，<mark style="color:red;">且當投資的部位夠大時，確實能夠逼近任意實數</mark>。

令持有數量為任意實數另一個考量就是不考慮流動性(bid-ask spread)的問題，以及大量買進或賣出時造成的市場衝擊(market impact)(大量買進時會因為買進的行為造成股價上漲，反之會因為賣出的行為造成股價的下跌)。

### 償付能力

> 投資人的財產總是為非負值，即$$V(t) \geq 0, ~ t=0,1$$。

滿足此條件的投資組合$$(x,y)$$稱為<mark style="color:red;">可允許(admissable)</mark>的投資組合。

## 無套利原則(一價原則)(no-arbitrage principle)

> 假設市場不允許沒有初始投資的無風險利潤
>
> 即不存在可允許的投資組合$$(x,y)$$使得$$V(0)=0$$，但是$$V(1) >0$$的非0機率。

如果市場上出現了套利機會，且被人們發現，則此機會會因為人們為了套利的交易很快就消失(以現今市場電子交易的速度，大約1\~2秒內馬上消失)。

<mark style="color:red;">另一個無套利原則的應用是在使用抽樣分佈(情境，scenario)以及使用隨機規劃(stochastic programming)替投資組合建模時，如果情境中存在套利機會時，則可能會產生錯誤的投資組合解</mark>。

### 如果不可同時做多與放空時，不存在套利機會

> 若$$x \geq 0$$且$$y \geq 0$$時，不存在$$V(0)=0$$但$$V(1) >0$$的非0機率。
>
> 若$$x \leq 0$$且$$y \leq 0$$時，不存在$$V(0)=0$$但$$V(1) >0$$的非0機率。

proof:

不失一般性，只考慮做多的情形。

由價格的正性，即$$S(t) >0, A(t) >0 \forall t$$，可得$$V(0)=0 \Leftrightarrow x=0  \text{ and }  y=0$$

因此在$$(x,y)=(0,0)$$的情形下，無論$$S(1)$$與$$A(1)$$之值為0，必定得到$$V(1)=0$$，因此無套利機會(QED)。



範例：套利機會

## 單期二元樹模型(one-step binomial model)的無套利原則

> 令時間$$t=0$$風險與無風險資產價格分別為$$S(0)$$與$$A(0)$$。
>
> 風險資產在時間$$t=1$$的價格為$$\displaystyle S(1) =  \begin{cases}  \mathrm{P}(S^u) =p  \\  \mathrm{P}(S^d) =1-p \end{cases}$$，$$S^d < S^u, ~ 0 < p <1$$。
>
> 不失一般性令$$S(0)=A(0)$$，則$$S^d < A(1) < S^u$$時不存在套利機會。
>
> 即若$$A(1) \leq S^d$$或$$S^u \leq A(1)$$時，存在投資組合$$V(0)=0, ~V(1) > 0$$。

註：從投資角度說，如果一資產的報酬顯著優於另一資產報酬時，則存在套利機會(買進便宜的資產，同時放空貴的資產)。

## 投資組合的報酬與風險

以期望值和標準差(變異數)做為投資組合未來的報酬和風險。

## 遠期合約(forward contract)

獲利結構和期貨(future)相似，主要差別是在契約、商品和交易場所的不同。

遠期合約是投資人和對手約定在交割日(delivery future)，以現在約定的遠價價格$$F$$(forward price)交易風險資產的契約。

如果在$$t=1$$時，以價格$$F$$買進(做多)遠期合約時，且風險資產為$$S(1)$$，則報酬(payoff)為$$S(1) - F$$。如果是以價格$$F$$賣出(放空)遠期合約時，則報酬為$$F-S(1)$$。

<mark style="color:red;">遠期合約的模型於期初建立部位時，不需付錢，而是在交割日時依合約結算</mark>。

令投資組合中各資產的數量分別為(風險資產、無風險資產、遠期合約)=$$(x,y,z) \in \mathbb{R}^3$$。

* $$V(0)=xS(0) + yA(0)$$
* $$V(1)=xS(1)+yA(1)+z(S(1)-F)$$

## 買權與賣權(call and put)

令投資組合中各資產的數量分別為(風險資產、無風險資產、買權或賣權)=$$(x,y,z) \in \mathbb{R}^3$$。

買權(call)：

* $$V(0)=xS(0)+yA(0)+zC(0)$$
* $$V(1)=xS(1)+yA(1)+zC(1)$$

已知$$S(1)$$的可能實現值，且$$A(1), C(1)$$已知，可由複製選擇權和反向定價得$$C(0)$$。

* (replicating the option) 由$$xS(1)+yA(1)=C(1)$$，求解得$$(x,y)$$。
* (pricing the option) 使用$$(x,y)$$代入$$xS(0)+yA(0)=C(0)$$得$$C(0)$$。

## 參考資料

* Marek Capinski and Tomasz Zastawniak, Mathematics for finance: an introduction to financial engineering, 1st, Springer, 2002.
