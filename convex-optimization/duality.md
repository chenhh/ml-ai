# 對偶性(duality)

## 簡介

在約束最最佳化問題中，常常利用拉格朗日對偶性(Lagrange duality)將原始問題轉為對偶問題，通過解決對偶問題而得到原始問題的解。

對偶問題有非常良好的性質，以下列舉幾個：

* 對偶問題的對偶是原問題；&#x20;
* 無論原始問題是否是凸的，對偶問題都是凸最佳化問題；&#x20;
* 對偶問題可以給出原始問題一個下界；&#x20;
* 當滿足一定條件時，原始問題與對偶問題的解是完全等價的；

## 問題標準型式(standard form, 不必為凸最佳化問題)

$$\displaystyle \begin{aligned} \min_{\mathbf{x} \in \mathbb{R}^n } ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_i(\mathbf{x}) =0, & i=1,2,\dots, p \end{aligned}$$

問題的可行域為$$\mathcal{D} = \mathrm{dom}f \cap_{i=1}^m \mathrm{dom}g_i \cap_{j=1}^p \mathrm{dom}h_i$$為非空集合，最佳值為$$p^{*}$$，而問題不必為凸最佳化問題。

## Lagrange函數

標準型的Lagrange函數$$L: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \rightarrow \mathbb{R}$$如下：

$$\displaystyle L(x, \lambda, \nu) = f_o(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \nu_j h_j(x)$$

* 定義域為$$\mathrm{dom} L = \mathcal{D} \times \mathbb{R}^m \times \mathbb{R}^p$$
* $$\lambda_i$$為第$$i$$個不等式約束$$g_i (x) \leq 0$$對應的<mark style="color:red;">Lagrange乘子(multiplier)</mark>。
* $$\nu_j$$為第$$j$$個等式約束$$h_j(x) =0$$對應的<mark style="color:red;">Lagrange乘子</mark>。



