# Lagrange multipliers

## 簡介

Lagrange乘數法在數學中的最佳化問題中，是一種尋找多元函數在其變數受到一個或多個條件的限制時的區域性極值的方法。

這種方法中引入了一個或一組新的未知數，即Langrange乘數，它們是在轉換後的方程式，即限制方程式中作為梯度（gradient）的線性組合中各個向量的係數。

Lagrange乘數法所得的臨界點會包含原問題的所有臨界點，但並不保證每個拉格朗日乘數法所得的臨界點都是原問題的臨界點。

## Lagrange theorem

設函數$$f,g$$有連續的一次偏導數。如果函數$$f$$在連續限制曲線$$g(x,y)=c$$上的點$$(x_0, y_0)$$有極值，則存在$$\lambda \in \mathbb{R}$$滿足$$\nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0)$$且$$\nabla g(x_0, y_0) \neq 0$$。

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

## 幾何解釋

簡化問題，假設決策變數為二維$$(x,y)$$，且要在限制式$$g(x,y)=c$$的條件下，求函數$$f(x,y)$$的極值(最大或最小值)。

給定$$d_1\in \mathbb{R}$$，在沒有限制式的情形下，則可以得到滿足$$f(x,y)=d_1$$的可行解(等高線)集合$$D_1=\{(x,y) \in \mathbb{R}^2 ~|~ f(x,y)=d_1\}$$。

而滿足$$g(x,y)=c$$的可行解集合為$$G=\{(x,y) \in \mathbb{R}^2 ~|~ g(x,y)=c\}$$。

在一般情形下，$$D_1 \cap G = \empty$$，但是我們可以調整函數$$f$$的值，假設為$$d_i$$，使得$$D_i \cap G \neq \empty$$。

而假設我們調整函數$$f$$的值，假設為$$d_k$$，使得$$D_k \cap G$$正<mark style="color:red;">好交於一點(相切)，而這一點恰好會是滿足問題條件的極值或鞍點</mark>。

以向量的形式來說，兩集合相切，表示$$f$$與$$g$$的切線在切點平行，因此兩函數的梯度向量有常數的關係，即：

* $$\nabla f(x,y)=-\lambda \nabla (g(x,y)-c)$$。
* 整理得$${\displaystyle \nabla {\Big [}f\left(x,y\right)+\lambda \left(g\left(x,y\right)-c\right){\Big ]}={\boldsymbol {0}}}$$
* 可求出$$\lambda$$之值。

令$$L(x,y,\lambda)=f(x,y)+\lambda (g(x,y)-c)$$，因為已求出$$\lambda$$之值，因此可在無限制條件下的極值和對應的極值點。

$$L(x,y,\lambda)$$在達到極值時與$$f(x,y)$$之值相等，因為$$L(x,y,\lambda)$$在達到極值時$$\nabla L(x,y,\lambda) =0$$，而$${\displaystyle {\frac {\partial L}{\partial \lambda }}=g\left(x,y\right)-c}$$，即$${\displaystyle g(x,y)-c}=0$$。

### 範例

> $$f(x,y)=x+y$$ s.t. $$x^2+y^2=1$$

限制式可改寫為 $$g(x,y)=x^2-y^2-1 = 0$$

Lagrange function $$L(x,y, \lambda)=f(x,y)+\lambda g(x,y) = x+y + \lambda (x^2+y^2 -1)$$

令偏微分均為0得三個方程式：

* $$\displaystyle \frac{\partial L}{\partial x} = 1+ 2 \lambda x = 0$$
* $$\displaystyle \frac{\partial L}{\partial y} = 1 + 2\lambda y = 0$$
* $$\displaystyle \frac{\partial L}{\partial \lambda} = x^2 + y^2 - 1 = 0$$

可得$$x=y=\frac{-1}{2\lambda}, ~ \lambda \neq 0$$代入得$$\lambda = \pm \frac{1}{\sqrt{2}}$$

可得點$$(x,y,\lambda)=(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}, \frac{-1}{\sqrt{2}}) \text{ or } (\frac{-\sqrt{2}}{2}, \frac{-\sqrt{2}}{2}, \frac{1}{\sqrt{2}})$$

因此函數$$f$$在限制式的極值為$$f(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}) = \sqrt{2}$$或$$f(\frac{-\sqrt{2}}{2}, \frac{-\sqrt{2}}{2}) = -\sqrt{2}$$。
