# 共軛分佈(conjugate distribution)

## 簡介

在貝氏定理中，在特殊情況下，存在一個分析解決方案，可不必計算貝氏定理中中分母所要求的積分。

$$
\displaystyle \mathrm{P}(\theta|X)=
\frac{\mathrm{P}(X|\theta) \mathrm{P}(\theta)}
{\int_0^1 \mathrm{P}(X|\theta_p)\mathrm{P}(\theta_p)d\theta_p}
$$

使用時機：所需估計的參數來自特定的分佈，如Binomial, Poisson, Normal, Multinomial分佈時，
使用這些分佈的似然函數(likelihood)且使用對應的先驗和後驗分佈，可得參數估計值的機率分佈，
且可計算參數估計值的信賴區間，而不只是點估計式。


| 先驗分佈(prior)             | 資料分佈(data)  | 後驗分佈(posterior) |
|-------------------------| ----------- | --------------- |
| Beta | Binomial    | Beta            |
| Gamma                   | Poisson     | Gamma           |
| Normal                  | Normal      | Normal          |
| Dicichlet               | Multinomial | Dirichlet       |

## Beta-binomial共軛範例：進入白宮的問題

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

假設Beta先驗分佈的參數為$$\alpha_0, \beta_0$$，經過$$n$$次試驗後，成功$$x$$次時，
可得後驗分佈也是Betap分佈，不必計算積分，且可得參數更新公式如下：
* $$ \alpha_{\text{posterior}} = \alpha_0 + x $$
* $$ \beta_{\text{posterior}} = \beta_0 + n - x $$

### 貝氏更新

給定beta分佈的初始超參數(hyperparameters)$$\alpha_0=0.5$$, $$\beta_0=0.5$$。

如果進行一次試驗(n=1)，且結果為失敗$$x=0$$，則可得更新後的超參數為：
* $$\alpha_1 = \alpha_0 + x = 0.5 + 0 = 0.5$$
* $$\beta_1 = \beta_0 + n - x = 0.5 +1 - 0 = 1.5$$

若再進行一次試驗，且結果還是失敗，可得更新後的超參數為：
* $$\alpha_2 = \alpha_1 + x = 0.5 + 0 = 0.5$$
* $$\beta_2 = \beta_1 + n - x = 1.5 +1 - 0 = 2.5$$

此時由Beta分佈的均值$$\mu=\frac{\alpha}{\alpha+\beta}=\frac{0.5}{0.5+2.5}=0.1667$$
與變異數$$\sigma^2 = \frac{\alpha \beta}{(\alpha + beta)^2 (\alpha + \beta + 1)} =0.0617 $$
可用beta分佈得到二項式分佈參數$$p$$的信賴區間。

如果在給定先驗後，直接進行兩次試驗，且兩次均為失敗時，也可得到相同的結果：
* $$\alpha_2 = \alpha_0 + x = 0.5 + 0 = 0.5$$
* $$\beta_2 = \beta_0 + n - x = 0.5 +2 - 0 = 2.5$$

在這裡，你可以看到貝氏推理的主要好處：隨著我們收集更多的資料，我們更新我們的信念。
我們從先驗開始，收集資料，然後使用貝氏定理來產生後驗。這些後驗值然後成為下一輪資料收集的先驗值。


## Gamma-poisson共軛範例: 鯊魚攻擊問題

Poisson分佈$$P(\lambda)$$，其中參數$$\lambda$$為單位時間內，事件發生的平均次數。
其pdf如下：

$$
\displaystyle \mathrm{P}(X=x; \lambda) = \frac{\lambda^x e^{-\lambda}}{x!}, ~ x=0,1,2,\dots
$$


| 年 | 鯊魚攻擊次數 | 
|----|----------| 
| 1  | 1        | 
| 2  | 0        | 
| 3  | 2        | 
| 4  | 1        | 
| 5  | 1        |
| 6  | 3        |
| 7  | 2        |
| 8  | 3        |
| 9  | 4        |
| 10 | 4        |
| 平均值| 2.1     |

由歷史資料可得下一次發生3次攻擊的機率為$$ \mathrm{P}(3;2.1) = \frac{2.1^{3} e^{2.1}}{3!}=0.189$$

如果在今年觀測到5次鯊魚攻擊，則在不同$$\lambda$$相異假設下，觀察到5次鯊魚襲擊的可能性是多少？鯊魚襲擊的可能性是多少？
當似然函數為Poisson分佈時，先驗/後驗分佈是Gamma分佈$$\Gamma(k, \theta)$$時為共軛分佈。

Gamma分佈的兩個參數$$k, \theta$$有三種常見的使用方式：
* $$k$$為形狀(shape)參數，$$\theta$$為規模(scale)參數。
* [貝氏機率使用] 形狀參數$$\alpha = k $$，速度(rate)參數$$\beta = \frac{1}{\theta}$$。
* 形狀參數$$k $$，平均參數$$ \mu = \frac{k}{\beta}$$。

平均值$$\mu = k\theta$$或$$ \frac{\alpha}{\beta}$$. 

