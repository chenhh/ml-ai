# Lagrange multipliers

## 簡介

Lagrange乘數法在數學中的最佳化問題中，是一種尋找多元函數在其變數受到一個或多個條件的限制時的區域性極值的方法。

這種方法中引入了一個或一組新的未知數，即Langrange乘數，它們是在轉換後的方程式，即限制方程式中作為梯度（gradient）的線性組合中各個向量的係數。

Lagrange乘數法所得的臨界點會包含原問題的所有臨界點，但並不保證每個拉格朗日乘數法所得的臨界點都是原問題的臨界點。

## 數學型式

給定凸最佳化問題標準型：

$$\displaystyle \begin{aligned} \min_{\mathbf{x}} ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_i(\mathbf{x}) =0, & i=1,2,\dots, p \end{aligned}$$

則決策變數$$x$$必定落在滿足以下條件的集合$${\displaystyle {\mathcal {X}}=\left\{x\in X\vert g_{1}(x),\ldots ,g_{m}(x)\leq 0\right\}}$$。

可得此問題的Langrangian function：$${\displaystyle L(x,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m})=\lambda _{0}f(x)+\lambda _{1}g_{1}(x)+\cdots +\lambda _{m}g_{m}(x)}$$

假設$$x^{*}$$為凸最化問題之解(註：可能有多個解)，對於每一個解均存在一組Langrange multiplier ($$\lambda_0, \lambda_1,\dots, \lambda_m$$)同時滿足以下條件：

1. $$x^{*}$$最小化$${\displaystyle L(y,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m}),~ \forall y \in X}$$。
2. $$\lambda_0, \lambda_1, \dots, \lambda_m \geq 0$$且至少一個$$\lambda_k > 0$$。
3. \[complementary slackness]$$\lambda_1 g_1(x) = \lambda_2 g_2(x) = \dots = \lambda_m g_m(x)$$

因此如果存在$$x\in X$$滿足條件1\~3，即$$\lambda_0=1$$且$$\lambda_1,\dots, \lambda_m \geq 0$$，則$$x$$必為最佳解。
