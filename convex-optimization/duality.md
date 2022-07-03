# 對偶性(duality)

## 簡介

在約束最最佳化問題中，常常利用拉格朗日對偶性(Lagrange duality)將原始問題轉為對偶問題，通過解決對偶問題而得到原始問題的解。

對偶問題有非常良好的性質，以下列舉幾個：

* 對偶問題的對偶是原問題；&#x20;
* 無論原始問題是否是凸的，對偶問題都是凸最佳化問題；&#x20;
* 對偶問題可以給出原始問題一個下界；&#x20;
* 當滿足一定條件時，原始問題與對偶問題的解是完全等價的；

實數域上的所有最佳化問題都有對偶問題，只不過當原問題為非凸問題時，由對偶問題得到的解只是原問題解的一個下界。KKT條件都可以用，當對偶間隙不為0時，所確定的是可行解，為0時是最優解。

如果原問題不是凸最佳化問題，那麼KKT只是必要條件，不是充分條件，最優解一定滿足KKT，但滿足KKT的不一定是最優解，不能由KKT說明原問題和對偶問題一致。

## 問題標準型式(standard form, 不必為凸最佳化問題)

$$\displaystyle \begin{aligned} \min_{\mathbf{x} \in \mathbb{R}^n } ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_i(\mathbf{x}) =0, & i=1,2,\dots, p \end{aligned}$$

問題的可行域為$$\mathcal{D} = \mathrm{dom}f \cap_{i=1}^m \mathrm{dom}g_i \cap_{j=1}^p \mathrm{dom}h_i$$為非空集合，最佳值為$$p^{*}$$，而<mark style="color:red;">問題不必為凸最佳化問題</mark>。

## Lagrange函數

標準型的Lagrange函數$$L: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \rightarrow \mathbb{R}$$如下：

$$\displaystyle L(x, \lambda, \nu) = f_o(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \nu_j h_j(x)$$

* 定義域為$$\mathrm{dom} L = \mathcal{D} \times \mathbb{R}^m \times \mathbb{R}^p$$
* $$\lambda_i \in \mathbb{R}$$為第$$i$$個不等式約束$$g_i (x) \leq 0$$對應的<mark style="color:red;">Lagrange乘數(multiplier)，此處不限制</mark>$$\lambda_i$$<mark style="color:red;">為正數</mark>。
* $$\nu_j \in \mathbb{R}$$為第$$j$$個等式約束$$h_j(x) =0$$對應的<mark style="color:red;">Lagrange乘數</mark>。

拉格朗日函數$$L$$如果看成是關於$$x$$ 的函數，那它其實就是對原始問題中目標函數與約束條件進行線性加權，目標函數的權重係數是1，約束條件的權系數是$$\lambda_i$$或 $$\nu_i$$ ；&#x20;

如果 $$L$$看成是關於$$\lambda$$或$$\nu$$的函數，則其餘部分可看成常數， $$L$$ 就可看作是一個關於$$\lambda$$或 $$\nu$$的仿射函數（即最高次冪為1的多項式函數）。

#### 範例

> 原問題：$$\min x^\top x$$ s.t. $$Ax=b$$ $$x \in \mathbb{R}^n ~, b \in \mathbb{R}^p ~ A \in \mathbb{R}^{p \times n}$$

Langrage函數 $$L(x, \nu)= x^\top x + \nu^\top (Ax - b)$$

對偶函數$$\displaystyle  \begin{aligned} g(\nu) &= \inf_{x} \{  x^\top x + \nu^\top (Ax - b) \} \\ 	& = \inf_{x} \{x^\top x + \nu^\top A x - \nu^\top b \} \\ 	& = -\frac{1}{4} \nu^\top A A^\top \nu - b^\top \nu  \end{aligned}$$為凹函數。

#### 範例

> 原問題： $$\min c^\top x$$ s.t. $$Ax=b, ~ x \succeq 0$$

Lagrange函數$$L(x, \lambda ,\nu) = c^\top X - \lambda^\top x + \nu (Ax-b)$$。

對偶函數：$$\displaystyle \begin{aligned} g(\lambda, \nu) & = \inf_{x} \{ c^\top -\lambda^\top x + \nu^\top (Ax-b)\} \\ 	& = \inf_{x} \{  (c^\top-\lambda^\top + \nu^\top A)x - \nu^\top b \} \\ 	& = \left\{  		\begin{aligned} 		& -b^\top v	& \text{ if } A^\top +c - \lambda = 0 \\ 		& -\infty	& \text { otherwise} 		\end{aligned} 	 	\right.  \end{aligned}$$

## 拉格朗日對偶函數（ Lagrange dual function）

拉格朗日對偶函數（簡稱對偶函數）通過對拉格朗日函數關於$$x$$取下確界(最小值)得到，即

$$\displaystyle g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$

$$\inf$$符號表示取下確界。求解析式可先將$$L$$看成是關於$$x$$的函數，而將拉格朗日乘子看作常數，求出$$L$$的極小值點，再將該點代入$$L$$ ，得到的關於$$\lambda$$和$$\nu$$的表達式就是對偶函數。

## 對偶函數的兩條重要性質

### 對偶函數一定是凹函數，其凹性與原目標函數和約束函數凹凸與否無關

![對偶函數必為凹函數](../.gitbook/assets/lagrange\_dual\_func-min.jpg)

因為$$g(\lambda, \nu)$$為凹函數，因此取$$\max$$可取到最大值。



### 對偶函數值必小於等於原問題最優解對應的目標函數值

> * $$\forall \lambda \succeq 0, \forall \nu$$，若原問題的最佳值為$$p^{*}$$，則$$g(\lambda, \nu) \leq p^{*}$$。&#x20;
> * 對偶函數沒有限制$$\lambda \succeq 0$$，<mark style="color:red;">而此處必須限制</mark>$$\lambda$$<mark style="color:red;">為非負值才有此性質</mark>。
> * 對偶函式為原問題的最佳值定義了一個下界。。

proof:

* 若$$\tilde{x}$$為可行性(feasible solution)，則原問題的限制式$$g_i (\tilde{x}) \leq 0$$且$$h_j(\tilde{x})=0$$。
* 因為Lagrange函數$$\displaystyle L(x, \lambda, \nu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \nu_j h_j(x)$$
* 若令$$\lambda \succeq 0$$，可得$$\sum_{i=1}^m \lambda_i g_i(\tilde{x}) + \sum_{j=1}^p \nu_j h_j(\tilde{x}) \leq 0$$。
* 因此可得$$f(\tilde{x}) \geq L(\tilde{x}, \lambda, \nu )$$--(1)
* 根據對偶函數定義得$$L(\tilde{x}, \lambda, \nu ) \geq \inf_{x \in \mathcal{D}} L(x, \lambda, \nu) = g(\lambda, \nu)$$--(2)
* 因此$$g(\lambda, \nu) \leq L(\tilde{x}, \lambda, \nu), ~ \forall x \in \mathcal{D}$$
* 若$$x^{*} = \tilde{x}$$，$$L(\tilde{x}, \lambda, \nu) = p^{*}$$
* 因此 $$g(\lambda, \nu) \leq p^{*}$$ (QED)

## 參考資料

* [\[知乎\]如何通俗地講解對偶問題，尤其是拉格朗日對偶 lagrangian duality？](https://www.zhihu.com/question/58584814)
