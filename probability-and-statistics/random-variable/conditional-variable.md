# 條件期望值

## 簡介

在初等機率論裡，我們可以定義某個事件對另一個事件的條件概率，比如P(骰子點數是3或4|骰子點數是偶數)。其實就是把原先的樣本空間$$\Omega$$限制到當做條件的事件上，做個歸一化，當做一個新的概率空間。於是有貝式公式 $$\mathrm{P}(A|B)=\frac{\mathrm{P}(A \cap B)}{\mathrm{P}(B)}$$。

對於事件$$A$$，考慮其示性函數（為隨機變數）$$\mathbf{1}_A(\omega) = \left\{  \begin{aligned} 1, \text{ if } \omega \in A \\  0,  \text{ if } \omega \not \in A \end{aligned}\right.$$。可得$$\mathrm{P}(A) = \mathrm{E}(\mathbf{1}_A)$$。同理可得$$\mathrm{P}(A|B)=\mathrm{E}(\mathbf{1}_A|B)$$。所以條件機率只是條件期望的一個特例，以下我們只考慮條件期望。

目前為止，條件期望只是把原先的變數限制在$$\Omega$$的一個子集上，把概率歸一化了之後求期望，算出來是一個實數。

對於兩個離散型隨機變數$$X,Y$$，$$\mathrm{E}(X|Y=y)$$也是一樣的道理，限制在子集$$\{ \omega : Y(\omega)=y\}$$上求期望。但注意到這個值是$$Y$$的取值，即$$y$$的函數，即$$f(y)=\mathrm{E}(X|Y=y)$$。於是我們可以把$$\mathrm{E}(X|Y)$$看做$$Y$$的函數，一個隨機變數$$f(Y)$$。

## 條件期望值

條件期望值有三種形式：

1. $$\mathrm{E}(c|Y)$$​為一實數值。
2. $$\mathrm{E}(X|Y=y)$$​為一實數值。
3. $$\mathrm{E}(X|Y)$$為一依賴於$$Y$$​的隨機變數。

> * $$\displaystyle \mathrm{E}(Y|X=k)=\sum_{h} h \cdot\mathrm{P}(Y=h|X=k)$$，在事件$$X=k$$下，$$Y$$的條件期望值。
> * $$\displaystyle \mathrm{E}(Y|X=k)=\int_{-\infty}^{\infty}y\cdot f_{Y|X}(y|x)dy$$
> * $$\mathrm{P}(Y=h|X=k) = \frac{\mathrm{P}(Y=h \cap X=k)}{\mathrm{P}(X=k)}$$

* 條件期望值$$\mathrm{E}(Y|X=k)$$在$$X=k$$給定後，其值已經決定了，因此為$$k$$的函數，即$$\mathrm{E}(Y|X=k) = f(k)$$。如果$$X$$之值未定時，則$$\mathrm{E}(Y|X) = g(X)$$。

### 條件期望值的性質

> 給定$$a_1, a_2 \in \mathbb{R}$$
>
> 1. $$\mathrm{E}(a_1Y_1+a_2Y_2|X)=a_1 \mathrm{E}(Y_1|X) + a_2 \mathrm{E}(Y_2|X)$$
> 2. $$\mathrm{E}(f(X)Y|X)=f(x)\mathrm{E}(Y|X)$$
> 3. 對於任意函數$$g$$，$$\mathrm{E}(\mathrm{E}(Y|X) g(X))=\mathrm{E}(Yg(X))$$
> 4. 若$$X,Y$$獨立，$$\mathrm{E}(Y|X)=\mathrm{E}(Y)$$
> 5. $$C$$為常數，$$\mathrm{E}(C|X)=C$$
> 6. $$\mathrm{E}(\mathrm{E}(Z|X,Y)|X)=\mathrm{E}(Z|X)$$
> 7. $$X,Y$$為i.i.d.隨機變數，$$\mathrm{E}(X|X+Y)=\frac{1}{2}(X+Y)$$
> 8.

### 條件期望值為最佳預測值

> $$\displaystyle \mathrm{E}(Y|X) = \arg \min_{g(X)} \mathrm{E}(Y-g(X))^2$$，即$$\mathrm{E}(Y|X)$$為對於$$Y$$的最佳預測值。

### 重複期望值定理

> $$\mathrm{E}(\mathrm{E}(X|Y))=\mathrm{E}(X)$$

## 參考資料

* [\[知乎\] 淺談條件期望](https://zhuanlan.zhihu.com/p/23670286)
* [\[statlect\] Conditional probability with respect to a sigma-algebra](https://www.statlect.com/fundamentals-of-probability/conditional-probability-as-a-random-variable)
* [\[wiki\] conditional expectation](https://en.wikipedia.org/wiki/Conditional\_expectation#Conditional\_expectation\_with\_respect\_to\_a\_.CF.83-algebra)
* [\[知乎\] 條件期望與全期望公式](https://zhuanlan.zhihu.com/p/417592820)
* [\[知乎\] 重期望公式及實例運用](https://zhuanlan.zhihu.com/p/163363352)
* [\[譚升的部落格\] 條件期望](https://face2ai.com/Math-Probability-4-7-Conditional-Expectation/)
* [Lecture 10 Conditional Expectation](https://web.ma.utexas.edu/users/gordanz/notes/conditional\_expectation.pdf)
  * [https://web.ma.utexas.edu/users/gordanz/lecture\_notes\_page.html](https://web.ma.utexas.edu/users/gordanz/lecture\_notes\_page.html)
* [Conditional expectation toy example](https://people.maths.bris.ac.uk/\~mb13434/cond\_expn\_example\_balazs.pdf)





