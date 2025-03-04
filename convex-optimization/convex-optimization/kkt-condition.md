# Karush-Kuhn-Tucker (KKT) 條件

## 簡介

KKT條件是在滿足一些有規則的條件下，一個非線性規劃（Nonlinear Programming）問題能有最佳化解法的一個必要條件。

給定非線性規劃如下：

$$\displaystyle \begin{aligned} \min_{\mathbf{x} \in \mathbb{R}^n} ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_j(\mathbf{x}) =0, & j=1,2,\dots, p \end{aligned}$$

對應的Lagrange functionb為$$L(\mathbf{x}, \mathbf{\mu}, \mathbf{\lambda}) = f(\mathbf{x})+\mathbf{\mu}^\top g(\mathbf{x}) + \mathbf{\lambda}^\top h(\mathbf{x})$$

## 必要條件

假設$$f, g_i, h_j$$均在$$x^{*}$$連續可微。若$$x^{*}$$是局部極小值，則會存在一組Lagrange乘數$$\lambda \geq 0$$，$$\mu_i \geq 0, ~i=1,2\dots, m$$，$$\nu_j, ~j=1,\dots, p$$滿足以下條件：

$$\begin{aligned} & \lambda + \sum_{i=1}^m \mu_i + \sum_{j=1}^p |\nu_j| > 0, \\ & \lambda \nabla f(x^{*}) + \sum_{i=1}^m \mu_i \nabla g_i (x^{*}) + \sum_{j=1}^p \nu_j \nabla h_j (x^{*}) = 0, \\ & \mu_i g_i (x^{*}) = 0, ~ i=1,2,\dots, m  \end{aligned}$$
