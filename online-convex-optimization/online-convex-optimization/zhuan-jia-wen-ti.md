---
description: the expert problem
---

# 專家問題

在每個時間點$$t=1,2,\dots,T$$,決策者每期都咨詢$$N$$個專家的建議，從兩個行動選一個執行$$x_t \in \{A, B\}$$ 。在決定行動後，決策者會得到損失，如果是正確的行動，則損失為0，否則損失為1。

* 如果決策者以50%的機率隨機選擇行動，則平均的損失為$$\frac{T}{2}$$，且正確率平均為50%。
* 就錯誤的數量而言，在最壞的情況下，沒有任何演算法可以做得比$$\frac{T}{2}$$更好。
* 因此，我們有動力去考慮一個<mark style="color:blue;">相對的效能指標</mark>：<mark style="color:red;">決策者在事後能不能像最佳專家一樣少犯錯誤</mark>？

## Theorem：決定性算法不存在錯誤上界

> 令 $$L \leq \frac{T}{2}$$為事先知道最佳的專家在決策所犯的錯誤總數。則不存在在決定性的演算法可保證所犯的錯誤數小於$$2L$$個。

假設只有兩個專家，其中一個專家每次都選行動$$A$$，另一個專家每次都選行動$$B$$。若對手每次都依決策者的做出的行動，總是給出相反的答案，則總錯誤數為$$T$$。

而最佳的專家犯錯的次數不會超過$$\frac{T}{2}$$。因此沒有確定性的算法可以保證所犯的錯誤數小於$$2L$$。(QED)



如果決策者總是依確定性的算法做出行動，對手有可能破解算法，而給予決策者最大的損失，因此應使用<mark style="color:blue;">機率式(隨機)的方式做出行動</mark>。

> 令$$\epsilon \in (0, 1/2)$$ 且最佳的專家犯$$L$$個錯誤，則
>
> * 存在確定性演算法可保證犯錯次數小於$$2(1+\epsilon) L + \frac{2 \log N}{\epsilon}$$
> * 存在隨機演算法期望犯錯次數最多為$$(1+\epsilon)L+\frac{\log N}{\epsilon}$$

## 加權多數決演算法(the weighted majority algorithm)

> * 每個專家$$i$$在時間$$t$$的權重為$$W_t(i)$$，初始權重為$$W_1(i)=1, ~\forall i \in [N]$$。
> * 令$$S_t(A), S_t(B) \subseteq [N] ~ \forall t \in [T]$$為時間$$t$$選擇行動$$A, B$$的專家形成的集合。
> * 定義$$W_t(A)=\sum_{i \in S_t(A)}W_t(i), ~ W_t(B)=\sum_{i \in S_t(B)}W_t(i)$$為加權後的權重。
> * 則行動$$a_t= \left \{ \begin{aligned} A & \text{ if } W_t(A) \geq W_t(B) \\ B & \text{ otherwise} \end{aligned}  \right .$$
> * 更新$$W_t(i)$$下一期權重，$$\epsilon$$為算法的參數: $$W_{t+1}(i) = \left \{ \begin{aligned} &W_t(i), & \text{ if expert } i \text{ was correct } \\ &W_t(i)(1-\epsilon), & \text{ if expert } i \text{ was wrong } \end{aligned}  \right .$$

### Lemma: 最好專家犯錯的錯誤上限與WM參數epsilon的關係式

> 令$$M_t$$為演算法到時間$$t$$所算的錯誤總數，而$$M_t(i)$$為專家$$i$$到時間$$t$$所犯的錯誤總數。
>
> 則$$\forall i \in [N]$$，可得$$M_T \leq 2(1+\epsilon) M_T(i) + \frac{2 \log N}{\epsilon}$$。
>
> 可調整參數$$\epsilon$$降低演算法的錯誤上界。

在$$\epsilon^{*} = \sqrt{\frac{\log N}{M_T(i)}}$$時可得最小錯誤。

考慮最佳的專家$$i^{*}$$，則$$M_T \leq 2 M_T(i^{*}) + O(\sqrt{M_T(i^{*}) \log N})$$。

但我們無法在事先就知道最好的專家的錯誤總數，因此只能用目前已知的資訊逼近最佳的結果。

proof:

令$$\phi_t=\sum_{i=1}^N W_t(i), ~\forall  t \in [T]$$為時間$$t$$時的權重總合，$$\phi_1=N$$。

因為$$W_{t+1}(i) = \left \{ \begin{aligned} &W_t(i), & \text{ if expert } i \text{ was correct } \\ &W_t(i)(1-\epsilon), & \text{ if expert } i \text{ was wrong } \end{aligned}  \right .$$

所以$$\phi_{t+1} \leq \phi_t$$為遞減數列，等號成立於當期所有專家全部預測正確。

而每一期加權多數決算法預測錯誤時，可得$$\phi_{t+1}  \leq   \frac{1}{2} \phi_t(1-\epsilon) + \frac{1}{2}\phi_t \leq \phi_t(1-\frac{\epsilon}{2})$$，因為至少有一半以上的專家權重給出錯誤的預測，因此必須降權重。

因為$$\phi_t \leq \phi_1 (1-\frac{\epsilon}{2})^{M_t} = N(1-\frac{\epsilon}{2})^{M_t}$$。而對於任一專家$$i$$，由定義可得$$W_T(i) = (1 - \epsilon)^{M_T(i)}$$。

因為$$W_T(i)$$必定小於權重總和$$\phi_T$$，可得$$(1-\epsilon)^{M_T(i)} = W_T(i) \leq phi_T \leq N(1-\frac{\epsilon}{2})^{M_T}$$。

兩邊取對數得 $$M_T(i) \log (1-\epsilon) \leq \log N + M_T \log(1-\frac{\epsilon}{2})$$。

使用對數的近似關係式 $$-x-x^2 \leq \log (1-x) \leq -x, ~ 0 < x < \frac{1}{2}$$。

最後可得$$-M_T(i) (\epsilon + \epsilon^2) \leq \log N - M_T \frac{\epsilon}{2}$$ (QED)

## 隨機加權多數決演算法(randomized weighted majority algorithm)

令在時間$$t$$選擇專家$$i$$的機率為$$p(i) = \frac{W_t(i)}{\sum_{j=1}^N W_t(j)}$$。

### Lemma: 隨機加權多數決演算法犯錯總數的上限

令$$M_t$$為隨機加權多數決演算法(RWM)到時間$$t$$犯錯的總數。

則對於所有的專家$$i \in [N]$$​，可得$$\mathrm{E}(M_T) \leq (1+ \epsilon) M_T(i) + \frac{\log N}{\epsilon}$$
