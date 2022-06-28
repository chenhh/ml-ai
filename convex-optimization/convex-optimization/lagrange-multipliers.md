# Lagrange multipliers

給定凸最佳化問題標準型：

$$\displaystyle \begin{aligned} \min_{\mathbf{x}} ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_i(\mathbf{x}) =0, & i=1,2,\dots, p \end{aligned}$$

則決策變數$$x$$必定落在滿足以下條件的集合$${\displaystyle {\mathcal {X}}=\left\{x\in X\vert g_{1}(x),\ldots ,g_{m}(x)\leq 0\right\}}$$。

可得此問題的Langrangian function：$${\displaystyle L(x,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m})=\lambda _{0}f(x)+\lambda _{1}g_{1}(x)+\cdots +\lambda _{m}g_{m}(x)}$$

假設$$x^{*}$$為凸最化問題之解(註：可能有多個解)，對於每一個解均存在一組Langrange multiplier ($$\lambda_0, \lambda_1,\dots, \lambda_m$$)同時滿足以下條件：

1. $$x^{*}$$最小化$${\displaystyle L(y,\lambda _{0},\lambda _{1},\ldots ,\lambda _{m}),~ \forall y \in X}$$。
2. $$\lambda_0, \lambda_1, \dots, \lambda_m \geq 0$$且至少一個$$\lambda_k > 0$$。
3. \$$\lambda\_1
