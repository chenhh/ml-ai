# 單根檢定(unit root test)

## 簡介

一般的定態序列的定義以弱定態為主，也就是一個隨機變數$$y_t$$的無條件期望值非時變$$\mathrm{E}(y_t)=\mu$$、變異數無條件期望值恆定$$\mathrm{Var}(y_t)=\sigma^2 <\infty$$且共變異數不隨時間改變，只與時間跨度有關$$\mathrm{Cov}(y_t, y_{t-k})=\gamma_k$$。

常見的定態序列，如ARMA：$$y_t=A(L)y_{t-1}+B(L)e_t$$，整理後可得$$y_t=\frac{B(L)e_t}{1-A(L)}$$，為差分方程式的一個解。而此差分方程式要定態，其解應該在單位圓內。如果有根在單位圓上，那就是有單位根了。

如隨機漫步模型 $$y_t = y_{t-1} + e_t$$，其特徵根為1。得解$$y_t=\sum_{i=0}^\infty e_{t-i}$$, 以看到這種情況下，離當前時間$$t$$很久遠的時刻的一個隨機沖擊對現在的影響仍然沒有衰減，這樣就是單位根過程了。

<mark style="color:blue;">如果時間序列存在這種情況，對時間序列的未來值的預測就難以進行。再從平穩的定義看，此時隨機變數的變異數就會逐漸增大到無窮大，而不會是有限的變異數，這樣長期的時間序列就沒有預測意義了</mark>。

## 差分方程式

在單變數的模型$$ARMA(p,q)$$，序列為一差分方程：

$$y_t=a_0+\sum_{i=0}^p a_i y_{t-i} + \sum_{j=0}^q b_j e_{t-j}$$

而平穩性意味著滿足了差分方程的穩定性條件（stability condition），從而差分方程的齊次解（homogeneous solution）是零。

而離散數學中，已知$$y_t$$的解分成兩部份，<mark style="color:red;">分別是齊次解（homogeneous solution）和特解（particular solution）</mark>。

求解的過程我們會用到特徵方程（characteristic equation）和特徵根（characteristic root）。

假設方程有m個重根(repeated roots)的齊次解為：

* $$\alpha \sum_{i=1}^m c_i t^i+\sum_{j=1+m}^p d_j \alpha_j^t$$
* 其中$$c_i$$為任意常數，$$\alpha_j$$為相異特徵根，$$\alpha$$是重根。

如果這個齊次根的任何一部分不是零，則這個差分方程的解的均值、變異數和共變異數就會依賴於時間$$t$$ （time-dependent）。

$$y_t$$的特解為：

* $$y_t=(a_0+\sum_{i=1}^q h_i e_{t-i}) / (1-\sum_{i=1}^p a_i L^i)$$

展開後會得到$$MA(\infty)$$過程，必需要讓這個展開收斂，這樣差分方程才能滿足穩定性條件。

因此需要有$$1-\sum_{i=1}^p a_i L^i = 0$$的根在單位圓之外，即$$\alpha^p - \sum_{i=1}^p a_i \alpha^{p-i} = 0$$的根在單位圓內。

因此平穩性的必要條件是$$\sum_{i=1}^p a_i <1$$，充分條件是$$\sum_{i=1}^p |a_i| < 1$$。

<mark style="color:red;">單位根（unit root）檢驗就是檢驗該差分方程的特徵方程（characteristic equation）的各個特徵根（characteristic root）是否小於1，即是否在單位圓（unit circle）內</mark>。

