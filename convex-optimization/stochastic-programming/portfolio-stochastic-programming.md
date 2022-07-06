# Portfolio stochastic programming

## 多期隨機規劃模型

### 目標函數(objective function)

$$\displaystyle  \max \frac{1}{T} \sum_{t=1}^T \left( {\color{red}z_{t+1}} - \frac{1}{(1-{\color{blue}\alpha})S_{t+1}} \sum_{s_{t+1}=1}^{S_{t+1}} {\color{green}y_{t+1}^{s_t+1}} \right)$$

目標函式是最大化在指定條件風險值(conditional value at risk, CVaR)的信心水準$$\alpha$$下的期末報酬率。

* $$T$$為投資的總期數。
* $$z_{t+1}$$為求解後，在第$$t+1$$期的風險值(VaR)。
* $$s_t$$為在時間$$t$$的第$$s_t$$個情境(scenario)，總共有$$S_t$$個情境。
* $$y_{t+1}^{s_{t+1}}$$為在時間$$t+1$$期時，第$$s_{t+1}$$個情境中投資組合的資產值(portfolio wealth)。
* $$S_1=1$$，為所有資產在決策前的已實現報酬。

### 限制式：超過VaR的投資組合資產值才用於計算CVaR

$$\displaystyle  \begin{aligned}  & y_{t+1}^{s_{t+1}}   \geq  z_{t+1} - \sum_{i=1}^{M_c} \overline{w}_{i,t} (1+r_{i, t+1}^{s_{t+1}}), ~ y_{t+1}^{s_{t+1}}  \geq  0 \\ & s_t  =  1,2,\dots, S_t, ~t  = 1,2,\dots, T  \end{aligned}$$

### 限制式：當期資產的價值等於前一期已配置的資產乘以報酬率加減買進賣出量
