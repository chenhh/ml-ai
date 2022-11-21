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

假設一個平民在沒有預約的情形下，可以進入白宮拜訪總統的機率為$$p$$，總共拜訪$$n$$次，則見到總統$$x$$次的機率分佈為$$\displaystyle \mathrm{P}(x; n, p) = \binom{n}{x}p^x(1-p)^{n-x}, ~ x=0,1,\dots, n$$。

