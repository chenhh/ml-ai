---
description: 資金管理 × 凱利法則金剛經, 吳牧恩與謝明華，旗標，2024
---

# book:數學公式裡的好野人

## 序

投資最重要的事：

* 新手：賺大錢。
* 老手：懂停損。
* 大神：資金管理。

交易聖盃=趨勢為友、情緒為敵+資金管理。

資產的累積，關鍵的因素在複利。

## 資料科學

一次性的準確預測，不代表長期都是穩定的準確預測。

真正的關鍵，要在金融市場做好交易，除了準確的預估各種事件的機率外，更重要的是根據預估的結做出相對應的動作，包括買進、賣出、加碼、減碼、停利、停損，這些動作都與部位大小有關。

爆倉經典範例：LTCM公司。

<mark style="background-color:red;">一個賺錢的策略，經常勝率<50%，也就是輸多贏少，因為其特徵是多次小賠與少次小賺，但是有幾次少數的大賺</mark>。(正期望值，與Tom Hougarrd的Best loser wins書中提到的相同)。

資金管理範例：有一穩定交易策略，會進出場3次，每次報酬損益為{2,2,-1}，為交易的報酬倍數，如果初始資金為100萬。

交易者A：所有資金100%全押：

* 第一次: 100->300萬 (賺2倍)。
* 第二次: 300->900萬。
* 第三次：900->0元 (全輸光)。

交易者B: 只押目前50%。

* 第一次：下注50->150，現金50->50，總資金200萬。
* 第二次：下注100>300，現金100->100，總資金400萬。
* 第三次：下注200->200，現金200->200，總資金200萬。

<mark style="background-color:red;">交易獲利的關鍵：獲利時儘量大賺，賠錢時小賠</mark>。

<mark style="background-color:orange;">真實的賭局中，最佳化必須考量到有限次的下注</mark>。

## 銅板賭局

賭局有固定的勝率與賠率(賺賠比)，而金融交易通常兩者均為未知。

**賠率(odds)**：下注50元，贏了拿回150元(含本金) ，輸了全輸，則賠率為100/50=2。

**勝率(winning rate)**：由大數法則得出，而非真實獲勝的次數，會有誤差。

只考慮輸贏時，可用二項式分佈表示勝率：$$\binom{n}{k} p^{k}(1-p)^{n-k}$$。

<mark style="background-color:red;">任何賭局在給定勝率</mark>$$p$$<mark style="background-color:red;">與次數</mark>$$n$$<mark style="background-color:red;">後，贏</mark>$$k$$<mark style="background-color:red;">次的機率都可以計算出來</mark>。

```python
from scipy.stats import binom

# 參數設置
n = 10  # 試驗次數
p = 0.5  # 成功的機率
k = 5  # 成功的次數

# 計算 PMF
pmf_value = binom.pmf(k, n, p)
print(f"二項式分佈 PMF P(X={k}) = {pmf_value}")
```

但是此處的$$p$$通常是由$$n \rightarrow \infty$$所估計得出(已實現的歷史)，在有限次賭局$$(n < \infty)$$時要稍為修改。

一般估計勝率，是**過去已發生**的輸贏事件中，所統計的贏的比例，不代表未來不會變動(可能是時變分佈)。<mark style="background-color:red;">所以通常會假設未來的</mark>$$p$$<mark style="background-color:red;">和歷史所估計值似近。</mark>

### 弱大數法則(weak law of large numbers, WLLN)

弱大數法則描述了在大量獨立重複試驗中，樣本平均值趨近於期望值的現象。

在隨機試驗中，當我們重複多次獨立且相同分佈（i.i.d.）的試驗後，樣本平均值會「以機率的形式」趨近於母體的期望值，隨著樣本數量無限增加，樣本平均值與期望值之間的差距變得可以忽略不計。

在$$T$$次獨立重複試驗中，事件$$X$$發生的次數為$$N_T$$，事件$$X$$在每次試驗中發生的真實(母體)機率為$$p$$，則：

$$\forall \epsilon >0, ~\exists N_\epsilon \in \mathbb{N} \ni ~|\frac{N_T}{T}-p{}|<\epsilon, ~\forall T > N_\epsilon$$。

可寫為機率收率形式 $$\displaystyle \lim_{T \rightarrow \infty} \mathrm{P}\left\{   \left| \frac{N_T}{T} - p\right| < \epsilon \right\} = 1$$。

簡單的說，當試驗次數$$T$$越多時，樣本平均值接近期望值的機率越高。<mark style="color:red;">反之若</mark>$$T$$<mark style="color:red;">不夠大時，則無法保證機率收斂</mark>。

### 小樣本時的平均值逼近期望值的誤差

考慮$$p=0.5$$的賭局，取$$\epsilon =0.01$$。

#### 考慮$$T=1$$

則$$N_1=0 \text{ or } 1$$，所以$$\left| \frac{N_1}{1} - 0.5 \right|=0.5$$。

因此$$\mathrm{P}\left\{ \left| \frac{N_1}{1} - 0.5 \right|  < 0.01\right\} =0$$ 誤差非常大。

考慮$$T=2$$

$$N_2=0 \text{ or } 1 \text{ or } 2$$。

* 當$$N_2=1$$，則$$\left| \frac{N_2}{2} - 0.5 \right| = 0$$
* 當$$N_2=0 \text{ or }2$$，則$$\left| \frac{N_2}{2} - 0.5 \right| = 0.5$$

因此有$$1/3$$的機率$$\mathrm{P}\left\{ \left| \frac{N_2}{2} - 0.5 \right|  < 0.01\right\} =1$$。

### 有限次數下賭局的獲利次數機率

由WLLN中，可得賭局勝率為$$p$$，玩$$T$$次，直覺上(玩無限次)認為會贏$$T \times p$$次。

但由二式項定理得$$\mathrm{P}(X_T = T \times p) = \binom{T}{ t=T \times p} p^t (1-p)^{T-t}$$。

<mark style="color:red;">以</mark>$$T=10, p=0.5$$<mark style="color:red;">的賭局來說，剛好贏5次的機率約24.6%，比想像中低很多</mark>!!

以下列出贏0\~10次的機率：

```
二項式分佈 PMF P(X=0) =  0.10%
二項式分佈 PMF P(X=1) =  0.98%
二項式分佈 PMF P(X=2) =  4.39%
二項式分佈 PMF P(X=3) =  11.72%
二項式分佈 PMF P(X=4) =  20.51%
二項式分佈 PMF P(X=5) =  24.61%
二項式分佈 PMF P(X=6) =  20.51%
二項式分佈 PMF P(X=7) =  11.72%
二項式分佈 PMF P(X=8) =  4.39%
二項式分佈 PMF P(X=9) =  0.98%
二項式分佈 PMF P(X=10) =  0.10%
```

## 賠率(odds)

賠率是在贏的時候，淨賺的下注資金倍數。是事先由莊家訂好，沒有隨機性的數值。

傳統賭局中，勝率和賠率互相抑制。高勝率：低賠率或低勝率：高賠率。

一般討論策略，只考慮到勝率，而沒有考慮賠率。

<mark style="background-color:red;">穩定的策略，損益多為「小賺」、「小賠」、「大賺」，而不會出現「大賠」。但滿足前三樣特性的策略，其勝率通常不高</mark>。因為一個交易策略要滿足以上性質，必定要控制好「停損」，會造成勝率降低。
