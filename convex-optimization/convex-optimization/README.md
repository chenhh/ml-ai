---
description: 凸最佳化、凸函數最佳化
---

# 凸優化(convex optimization)

## 標準型式(standard form)

$$\displaystyle \begin{aligned} \min_{\mathbf{x}} ~& ~ f(\color{red}{\mathbf{x}}) &  \\ s.t. ~&~ g_i(\mathbf{x}) \leq 0, & i=1,2,\dots, m \\ 	 ~&~ h_i(\mathbf{x}) =0, & i=1,2,\dots, p \end{aligned}$$

* $$\mathbb{x} \in \mathbf{R}^n$$為決策變數。
* 目標函數$$f: D \in \mathbb{R}^n \rightarrow \mathbb{R}$$為凸函數，$$D$$為凸集合。
* 不等式限制函數$$g_i: \mathbb{R}^n \rightarrow \mathbb{R}, ~i=1,2,\dots, m$$為凸函數。
* 等式限制函數$$h_i : \mathbb{R}^n \rightarrow \mathbb{R}, ~i=1,2,\dots, p$$為仿射函數，即函數的型式為$$h_i(\mathbb{x})=\langle \mathbf{a}, \mathbf{x} \rangle - b_i$$。
* 凸最佳化問題可能沒有解、唯一解，或是無限多解。

### 最佳值(optimal value)

$$p^{*} = \inf \{f_0(x) | g_i \leq 0, i=1,2,\dots,m, h_j(x) =0, j=1,2,\dots, p \}$$

* 若<mark style="color:blue;">問題無解(infeasible)</mark>，即沒有$$x$$可滿足所有限制式，則$$p^{*} = \infty$$。
* 若<mark style="color:blue;">問題沒有下界(unbounded below)</mark>，則$$p^{*} = -\infty$$。

## 應用：ordinary least square

此類問題沒有約束條件，且目標函數是若干項的平方和，每一項有$$a_i^\top x -b_i$$的形式：

* $$\min f_o(\mathbf{x})=\| A \mathbf{x} - \mathbf{b} \|_2^2 = \sum_{i=1}^k (a_i^\top x - b_i)^2$$
* $$A =\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_k \end{bmatrix}=\in \mathbb{R}^{k \times n}~ k \geq n$$

在線性代數中討論過此問題，可得解析解 $$x^{*} = (A^\top A)^{-1} A^\top b$$。

判斷是否為OLS問題問題很簡單，只要檢驗目標函數是為二次函數，然後檢驗此函數是否為半正定即可。

### OLS變型：加權OLS

* $$\min f_o(\mathbf{x})= \sum_{i=1}^k w_i (a_i^\top x - b_i)^2$$
* $$w_1, w_2, \dots, w_k > 0$$，反應了各項的重要程度。

### OLS變型：懲罰函數(正規項)

* $$\min f_o(\mathbf{x})= \sum_{i=1}^k (a_i^\top x - b_i)^2 + \rho \sum_{i=1}^n x_i^2, ~\rho > 0$$

使用懲罰項避免向量$$\mathbf{x}$$中，單一元素值過大。

為什麼凸最佳化重要?


凸最佳化性質好，許多日常生活中的非凸最佳化問題，目前最有效的辦法也只能是利用凸最佳化的思路去近似求解。

例如：

* 帶整數變量的最佳化問題，鬆弛之後變成凸最佳化問題（所以原問題其實是凸最佳化問題+整數變量）；
* 任意帶約束的非凸連續最佳化問題，其對偶問題作為原問題解的一個下界，一定是凸最佳化問題。
* 針對帶有隱藏變數的近似求解maximum likelihood estimate (MLE)的EM演演算法，或者貝式版本裡頭所謂的variational Bayes(VB) inference。而原本的MLE其實是非凸最佳化問題，所以EM和VB演演算法都是找到了一個比較好最佳化的concave lower bound對這個lower bound進行最佳化。

### 現在各種深度強化學習、深度學習的最佳化問題都是極其復雜的非凸最佳化問題，不是大家也能解的挺好？

簡單來說是這樣，目前對於這些非凸最佳化問題取得的演算法理論方面的突破，大致其實歸結於找到這些非凸最佳化問題中“凸”的結構。這也是為什麼我們看到一階演演算法（SGD, ADAM等）仍然大行其道，而分析這些非凸最佳化演演算法的時候其實很多的lemma（引理）仍然是凸最佳化（凸分析）裡的引理或者引申。

### 現有的最佳化方法不是都能解決（凸最佳化）嗎？那凸最佳化又有什麼用呢？

相比非凸最佳化，各種NP-complete問題，凸最佳化裡各種P問題，那肯定是簡單的。然而，在實際當中，我們完全不可能滿足於有一個“多項式時間演演算法”就好了。

我們知道，作業管理，最佳化問題，反映到現實世界裡面就是各種**數學建模問題**。這些問題，普遍地出現在航空業、金融業、廣告業、電商零售業、能源業、醫療業、交通業等各個領域。我們必須要明確一點，**計算復雜性理論（P、NP）在工程當中其實是沒什麼用處的**。NP hard，NP complete問題很難，沒有多項式時間演演算法，但如果你實際的問題規模不太大，比如幾十個城市的旅行商問題（TSP, travelling salesman problem），這樣規模NP-complete問題，在2019年的iphone上下載concorde 的TSP app，一部手機只須幾秒鐘就能算出最佳解。（實際上這個app，1000個左右城市的TSP， iphone也頂多要算個幾小時就能找到全域性最優解，無近似）。

與此相對應的，即使是一個P問題，但是如果實際當中問題規模超級大呢？實際上反而這個問題更難處理。

舉個例子，比如現在優酷、天貓、京東、亞馬遜這些個平台，每天你登陸網站，它在推薦欄都需要根據你的歷史活動記錄決定推薦哪些產品給你。這個在線推薦演演算法，本質上只是需要求解一個線性規劃問題（LP, linear programming, 比一般的凸最佳化還簡單），甚至還不是一個一般的線性規劃，有個專門的名字叫做packing LP，這類packing LP理論上可以有跟問題規模呈線性的復雜度的演算法（忽略log項，跟排個序差不多）。聽起來是不是很簡單？然而，**實際這些問題的規模無比巨大，每天這些平台上線人次數以億記，這些平台可以推薦的商品也是至少百萬千萬規模的**。**而且實際問題還有各種各樣的現實約束**，比如我們希望我們的演演算法可以完全在線更新（online，甚至是streaming algorithm），我們的演算法需要靈活運用存儲數據的數據結構，需要利用計算叢集的並行能力，分佈式能力，這也是需要非常非常專門的（一階）最佳化演演算法設計的。

因此即使現有的方法能解決所有的凸最佳化問題，但從實際應用的角度其實還須要改善很多地方。事實上，目前的大公司面對如此規模的最佳化問題，也就LP還可以勉強可用，其它如second-order cone programming (SOCP)，semidefinite programming (SDP)根本目前實際中都不可能大規模求解。而這兩類問題在理論上還仍然都是「線性」的，因為可以寫成linear conic programming，所以就更不要說一般的帶約束的凸最佳化問題了。

在這個方面，**無論是求解器（solver）還是更好的理論演演算法的開發都還有大量的研究空間**。比如，SDP實際當中的大規模演演算法設計目前來看還基本一片空白，有很多很基本的問題都還沒有在理論上得到滿意的解答（像SDP其實和另一類凸最佳化問題只有一絲之隔，copositive programming，而這類凸最佳化問題的計算復雜度卻是NP complete的，所以即使是凸最佳化也未必復雜度就容易。實際上，所有mixed 0/1 nonconvex quadratic program都可以寫成copositive program這個凸最佳化的形式。兩者的演演算法設計也因此都很困難）。還有這麼多沒有解決的問題，又如何能說凸最佳化的問題都已經被“解決”了呢。
