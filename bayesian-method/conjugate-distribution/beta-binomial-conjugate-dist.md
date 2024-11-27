# Beta-binomial共軛分佈

先驗、後驗分佈：beta

資料分佈：binomial

在貝氏統計中，Beta-binomial共軛分佈描述了一個這樣的場景：

* 我們對一個事件發生的機率並不完全確定，因此我們給這個機率賦予一個Beta分佈作為先驗分佈。
* 然後，我們進行了一系列伯努利試驗，得到了一定的資料，基於這些資料，我們可以更新對該機率的信念，得到一個後驗分佈。
* 神奇的是，這個後驗分佈仍然是一個Beta分佈，這就是Beta-binomial共軛關係。

## 先驗分佈：Beta分佈

假設我們對一個事件發生的機率θ並不完全確定，我們用Beta分佈來描述我們對θ的先驗知識：

$$\theta \sim Beta(\alpha, \beta)$$

其中α和β是Beta分佈的引數，控制著分佈的形狀。

## 似然函數：二項分佈

我們進行了n次伯努利試驗，其中有x次成功，則似然函式為：$$\mathrm{P}(x|\theta)=\binom{n}{x}\theta^x (1-\theta)^{n-x}$$。

## 後驗分佈：Beta分佈

根據貝氏定理，後驗分佈正比於先驗分佈乘以似然函式：$$\mathrm{P}(\theta|k) \propto \mathrm{P}(k|\theta)  \times \mathrm{P}(\theta)$$。

將Beta分佈和二項分佈代入，經過一系列的推導和化簡，可以得到：

