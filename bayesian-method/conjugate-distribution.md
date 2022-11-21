# 共軛分佈(conjugate distribution)

## 簡介

在貝氏定理中，在特殊情況下，存在一個分析解決方案，可不必計算貝氏定理中中分母所要求的積分。

| 先驗分佈(prior) | 資料分佈(data)  | 後驗分佈(posterior) |
| ----------- | ----------- | --------------- |
| Beta        | Binomial    | Beta            |
| Gamma       | Poisson     | Gamma           |
| Normal      | Normal      | Normal          |
| Dicichlet   | Multinomial | Dirichlet       |

## &#x20;Beta-binomial共軛範例：進入白宮的問題

假設一個平民在沒有預約的情形下，可以進入白宮拜訪總統的機率為$$p$$，總共拜訪$$n$$次，
則見到總統$$x$$次的機率分佈為$$\displaystyle \mathrm{P}(x; n, p) = \binom{n}{x}p^x(1-p)^{n-x}, ~ x=0,1,\dots, n$$。

問題的目標是要估計參數$$p$$，可使用貝氏方法如下:
1. 給定參數$$p$$的先驗分佈。(使用Beta分佈$$beta(\alpha, \beta)$$描述$$p \in (0,1)$$的假設)
2. 收集資訊，計算成功與失敗的次數。
3. 決定已觀察到資料的似然性。
4. 使用貝氏定理計算$$p$$的後驗分佈。

Beta分佈的pdf形式如下:
$$
\displaystyle f(x; \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha -1} (1-x)^{\beta-1}, ~ 0 < x < 1
$$
其中$$B$$為beta函數，是用於正規化機率值。

Beta分佈的平均值為$$\mu=\frac{\alpha}{\alpha + \beta}$$，
變異數為$$ \sigma^2 = \frac{\alpha \beta}{(\alpha + beta)^2 (\alpha + \beta + 1)}$$
