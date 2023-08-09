# 條件期望值

## 簡介

在機率論中，可定義某個事件對另一個事件的條件機率，比如P(骰子點數是3或4|骰子點數是偶數)。其實就是把原先的樣本空間$$\Omega$$限制到給定條定件的事件上，做正規化，視為一個新的機率空間。於是有貝式公式 $$\mathrm{P}(A|B)=\frac{\mathrm{P}(A \cap B)}{\mathrm{P}(B)} = \frac{\mathrm{E}(A\mathbf{1}_B)}{\mathrm{P}(B)}$$。

### 事件集合的條件期望值

對於事件$$A$$，考慮其指示函數（為隨機變數）$$\mathbf{1}_A(\omega) = \left\{  \begin{aligned} 1, \text{ if } \omega \in A \\  0,  \text{ if } \omega \not \in A \end{aligned}\right.$$。可得$$\mathrm{P}_{\Omega}(A) = \mathrm{E}_{\Omega}(\mathbf{1}_A)$$。同理可得$$\mathrm{P}_{\Omega}(A|B)=\mathrm{E}_{\Omega}(\mathbf{1}_A|B)$$。<mark style="color:blue;">所以條件機率只是條件期望值的一個特例，以下我們只考慮條件期望值</mark>。

目前為止，條件期望只是把原先的變數限制在$$\Omega$$的一個子集上，把機率正規化了之後求期望值，為一實數值。

### 隨機變數的條件期望值

定義在機率空間$$(\Omega, \mathcal{F}, \mathrm{P})$$的隨機變數$$X$$的期望值$$\displaystyle \mathrm{E}_{\Omega}(X)\equiv \int_\Omega X d \mathrm{P}$$

對於離散隨機變數$$X,Y$$，$$\mathrm{E}(X|Y=y)$$也是一樣的道理，限制在子集$$\{ \omega ~|~ Y(\omega)=y\}$$上求期望值，而連續隨機變數也只是限制在$$\{\omega ~|~ a \leq Y(\omega) \leq b\}$$，概念相同。但注意到此值是$$Y$$的實現值，因此期望值是$$y$$的函數，即$$f(y)=\mathrm{E}(X|Y=y)$$。於是我們可以把$$\mathrm{E}(X|Y)$$看做$$Y$$的函數，一個隨機變數$$f(Y)$$。

即使取$$X$$的函數值$$g(X)$$，條件期望值仍然為$$Y$$的函數，即$$\mathrm{E}(g(X)|Y)=h(Y)$$為$$Y$$的隨機變數。

### 隨機變數σ域的條件期望值

在隨機變數的條件期望值中，兩個結果$$\omega_1, \omega_2$$是否有相同的條件期望值，取決於$$Y(\omega_1)$$是否與$$Y(\omega_2)$$有相同的函數值。因此不必考慮$$Y(\omega_1)$$的實際值為何，只需考慮$$\omega$$如何對宇集合$$\Omega$$做分割(partition)。

而能夠記錄$$Y$$的相異取值而不記錄實際取值為何，就是$$\sigma(Y)$$，即宇集合$$\Omega$$中使得$$Y$$可測的最小的σ域。因此$$\mathrm{E}(g(X)|Y)$$可寫成$$\mathrm{E}(g(X)|\sigma(Y))$$。

既然條件期望值只用了σ域的資訊，那麼不必管這個σ域是由那個隨機變數生成，直接對σ域定義條件期望即可。

### 一般σ域的條件期望值

考慮測度空間$$(\Omega, \mathcal{F}_0, \mathrm{P})$$的隨機變數$$X$$，且$$\mathrm{E}(|X|) < \infty$$。

#### 描述性定義

考慮子σ域$$\mathcal{F} \subset \mathcal{F}_0$$。若條件期望$$\mathrm{E}(X|\mathcal{F})=Y$$為$$Y$$的隨機變數，且滿足：

1. 隨機變數$$Y$$在$$\mathcal{F}$$可測；
2. $$\forall A \in \mathcal{F}$$，可得$$\displaystyle \int_A X d\mathrm{P} = \int_A Y d\mathrm{P}$$或寫成$$\mathrm{E}(X\mathbf{1}_A)=\mathrm{E}(Y\mathbf{1}_A)$$。

<mark style="color:red;">稱隨機變數</mark>$$Y$$<mark style="color:red;">為</mark>$$X$$<mark style="color:red;">關於</mark>$$\mathcal{F}$$<mark style="color:red;">的條件期望值。</mark>

<mark style="color:red;">條件期望值不唯一，但任兩個版本的條件期望值只在零測集上相異</mark>。

proof: 條件期望值存在性會用到Ryadon-Nikodym定理

> 令$$\mu, \nu$$為可測空間$$(\Omega, \mathcal{F})$$上的兩個σ-finite測度。
>
> 如果$$\nu \ll \mu$$ ($$\nu$$對$$\mu$$絕對連續，$$\forall A \in \mathcal{F}$$，若$$\mu(A)=0$$可得$$\nu(A)=0$$)
>
> 則存在$$\mathcal{F}$$可測的函數$$0\leq f <\infty$$使得$$\forall A \in \mathcal{F}$$，有$$\displaystyle \int_Af d\mu=\nu(A)$$，$$f$$記為$$\displaystyle \frac{d\nu}{d\mu}$$稱為Randon-Nikodym導數。
>
> 常見範例。$$f$$為在實數區間$$A$$有定義的連續函數，$$\mu$$為Lebesgue測度，則$$\int_Af d\mu$$為函數在區間$$A$$的積分值，而$$\nu(A)$$可解釋為某函數在此區間$$A$$的面積。

假設隨機變數$$X \geq 0$$且令$$\mu = \mathrm{P}$$，$$\displaystyle  \nu(A)=\int_A X d \mathrm{P},~ \forall A \in \mathcal{F}$$

可得$$\nu$$為σ-finite測度且$$\nu \ll \mu$$ (todo)。

由Raydon-Nikodym定理可得存在$$\displaystyle g=\frac{d \nu}{d \mu}$$使得$$\displaystyle \int_Af d \mathrm{P} = \nu(A) = \int_A \frac{d\nu}{d \mu} d \mathrm{P}$$

可得$$g$$為所求的條件期望。(QED)

#### 構造性定義

令σ域$$\mathcal{F}$$中的可測序數$$\{B_n, n\in \mathbb{N}\}$$是宇集合$$\Omega$$的一組分割。令$$\mathcal{g}=\sigma(\{B_n, n \in \mathbb{N}\})$$為此序列生成的σ域。令隨機變數$$X$$的積分存在，則：

$$\displaystyle \mathrm{E}(X|\mathcal{g}) = \sum_{j=1}^\infty \left(  \frac{1}{\mathrm{P}(B_j)} \int_{B_j} X(\omega)d\mathrm{P}(\omega)  \right) \mathbf{I}_{B_j} = \sum_{j=1}^\infty \mathrm{E(X| B_j)}\mathbf{I}_{B_j}$$

### 範例

給定測度空間$$(\Omega, \mathcal{F}, \mathrm{P})$$，$$\Omega=[0,1]$$，$$\mathrm{P}$$為Lebesgue測度。

令σ域$$A=\mathcal{F}$$，$$B$$為由終端端點$$\{0, 1/4, 1/2, 3/4,1\}$$的區間形成的σ域，$$C$$由終端端點$$\{0, 1/2, 1\}$$的區間形成的σ域。

即$$B=\sigma([0,1/4], [1/4,1/2], [1/2, 3/4], [3/4, 1])$$，$$C=\sigma([0,1/2], [1/2,1])$$。

因為$$X \in \mathcal{F}$$，所以$$\mathrm{E}(X|A)=X$$

$$\displaystyle \begin{aligned} \mathrm{E}(X|B)  	& =\mathrm{E}(X|[0,1/4])\cdot\mathbf{1}_{[0,1/4]}  \\ 	& +\mathrm{E}(X|[1/4,1/2])\cdot\mathbf{1}_{[1/4,1/2]} \\ 	& +\mathrm{E}(X|[1/2,3/4])\cdot\mathbf{1}_{[1/2,3/4]} \\ 	& +\mathrm{E}(X|[3/4,1])\cdot\mathbf{1}_{[3/4,1]} \\ 	& = 4 \int_{0}^{1/4} X(x)dx \cdot\mathbf{1}_{[0,1/4]} \\ 	& + 4 \int_{1/4}^{1/2} X(x)dx \cdot\mathbf{1}_{[1/4, 1/2]} \\ 	& + 4 \int_{1/2}^{3/4} X(x)dx \cdot\mathbf{1}_{[1/2, 3/4]} \\ 	& + 4 \int_{3/4}^{1} X(x)dx \cdot\mathbf{1}_{[3/4, 1]} \\ \end{aligned}$$

## 簡單範例

令$$\Omega=\{1,2,\dots, 12\}$$，$$\mathcal{F}=\text{power set of }\Omega$$，$$\mathrm{P}(\{1\})=\dots=\mathrm{P}(\{12\})=1/12$$。

定義隨機變數：

$$Y = \mathrm{ceil}(\frac{\omega}{4}) =  \left\{ \begin{aligned} 1,& \text{ if } \omega =1,2,3,4, \\  2,& \text{ if } \omega =5,6,7,8, \\ 3,& \text{ if } \omega =9,10,11,12, \\  \end{aligned} \right.$$

$$X = \mathrm{ceil}(\frac{\omega}{2}) =  \left\{ \begin{aligned} 1,& \text{ if } \omega =1,2, \\  2,& \text{ if } \omega =3,4 \\ 3,& \text{ if } \omega =5,6, \\ 4,& \text{ if } \omega =7,8, \\ 5,& \text{ if } \omega =9,10, \\ 6,& \text{ if } \omega =11,12, \\  \end{aligned} \right.$$

可得$$\begin{aligned} \sigma(Y) &=\sigma(Y^{-1}(B(\mathbb{R})) \\&= \sigma(\{1,2,3,4\},\{5,6,7,8\},\{9,10,11,12\}) \\ 	& = \{\empty, \{1,2,3,4\}, \{5,6,7,8\}, \{9,10,11,12\}, \\ 	 &\{1,2,3,4,5,6,7,8\}, \{1,2,3,4,9,10,11,12\}, \{5,6,7,8,9,10,11,12\}, \Omega\} \end{aligned}$$

同理可得：$$\begin{aligned} \sigma(X) &=\sigma(X^{-1}(B(\mathbb{R})) \\&= \sigma(\{1,2\},\{3,4\},\{5,6\},\{7,8\},\{9,10\},\{11,12\}) \\ 	 \end{aligned}$$

性質如下：

* $$Y$$為$$\sigma(Y)$$可測(由定義可得)。
* $$Y$$為$$\sigma(X)$$可測(因為$$\sigma(X) \subset \sigma(Y)$$)
* $$X$$為$$\sigma(X)$$可測(由定義可得)。
* $$X$$不是$$\sigma(Y)$$可測，因為$$X^{-1}(\{1\})=\{1,2\} \notin \sigma(Y)$$。

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





