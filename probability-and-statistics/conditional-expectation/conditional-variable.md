# 一般化的條件期望值

## 簡介

在機率論中，可定義某個事件對另一個事件的條件機率，比如P(骰子點數是3或4|骰子點數是偶數)。其實就是把原先的樣本空間$$\Omega$$限制到給定條定件的事件上做正規化，視為一個新的機率空間。於是有貝氏公式 $$\mathrm{P}(X|Y)=\frac{\mathrm{P}(X \cap Y)}{\mathrm{P}(Y)} = \frac{\mathrm{E}(X \mathbf{1}_Y)}{\mathrm{P}(Y)}$$。

<mark style="color:blue;">但貝氏公式無法計算零機率的事件的條件機率，即無法計算</mark>$$\mathrm{P}(Y)=0$$的條件機率。

條件期望值可分為以下幾類：

1. 依賴隨機變數的特定實現值$$\mathrm{E}(X|Y=y)$$。
2. 依賴於隨機變數的值域$$\mathrm{E}(X|Y)=f(y)$$。
3. 依賴於給定的σ域  $$\mathrm{E}(X|\sigma(Y))$$，該定義的主要優點是它允許我們以零機率事件為條件。

### 事件集合的條件期望值

對於事件集合$$E \subseteq \Omega$$，考慮其指示(示性)函數（為隨機變數）$$\mathbf{1}_E(\omega) = \left\{  \begin{aligned} 1, \text{ if } \omega \in E \\  0,  \text{ if } \omega \not \in E \end{aligned}\right.$$。可得$$\mathrm{P}_{\Omega}(E) = \mathrm{E}_{\Omega}(\mathbf{1}_E)$$。同理可得$$\mathrm{P}_{\Omega}(E|F)=\mathrm{E}_{\Omega}(\mathbf{1}_E|F)$$。<mark style="color:blue;">所以條件機率只是條件期望值的一個特例，以下我們只考慮條件期望值</mark>。

目前為止，條件期望只是把原先的變數限制在$$\Omega$$的一個子集上，把機率正規化了之後求期望值，為一實數值。

### 隨機變數的條件期望值

定義在機率空間$$(\Omega, \mathcal{F}, \mathrm{P})$$的隨機變數$$X$$的期望值$$\displaystyle \mathrm{E}_{\Omega}(X)\equiv \int_\Omega X d \mathrm{P} \equiv \int_\Omega X(\omega) d \mathrm{P}(\omega)$$

對於離散隨機變數$$X,Y$$，條件期望值$$\mathrm{E}(X|Y=y)$$也是一樣的道理，限制在子集$$\{ \omega ~|~ Y(\omega)=y\}$$上求$$X(\omega)$$的期望值，而連續隨機變數也只是限制在$$\{\omega ~|~ a \leq Y(\omega) \leq b\}$$，概念相同。<mark style="color:red;">但注意到條件期望值之值依賴於</mark>$$Y$$<mark style="color:red;">的實現值，因此期望值是</mark>$$y$$<mark style="color:red;">的函數，即</mark>$$f(y)=\mathrm{E}(X|Y=y)$$。於是我們可以把$$\mathrm{E}(X|Y)$$看做$$Y$$的函數，一個隨機變數$$f(Y)$$。

即使取$$X$$的函數值$$g(X)$$，條件期望值仍然為$$Y$$的函數，即$$\mathrm{E}(g(X)|Y)=h(Y)$$為$$Y$$的隨機變數。

### 隨機變數σ域的條件期望值

在隨機變數的條件期望值中，兩個結果$$\omega_1, \omega_2$$是否有相同的條件期望值，取決於$$Y(\omega_1)$$是否與$$Y(\omega_2)$$有相同的函數值。因此不必考慮$$Y(\omega_1)$$的實際值為何，只需考慮$$\omega$$如何對宇集合$$\Omega$$做分割(partition)。

<mark style="color:red;">而能夠記錄</mark>$$Y$$<mark style="color:red;">的相異取值而不記錄實際取值為何，就是</mark>$$\sigma(Y)$$<mark style="color:red;">，即宇集合</mark>$$\Omega$$<mark style="color:red;">中使得</mark>$$Y$$<mark style="color:red;">可測的最小的σ域。因此</mark>$$\mathrm{E}(g(X)|Y)$$<mark style="color:red;">可寫成</mark>$$\mathrm{E}(g(X)|\sigma(Y))$$。

既然條件期望值只用了σ域的資訊，那麼不必管這個σ域是由那個隨機變數生成，直接對σ域定義條件期望即可。

### 將σ域解釋為資訊集合

令$$Y, Y_1, Y_2$$為可測空間$$(\Omega, \mathcal{F})$$隨機變數、隨機向量或隨機過程。則：

* 若$$\sigma(Y) \subseteq \mathcal{F}$$，則稱$$Y$$的資訊已包含在$$\mathcal{F}$$內(the information of Y is contained in F)，或者說$$Y$$沒有比$$\mathcal{F}$$更多的資訊。
* 若$$\sigma(Y_1) \subseteq \sigma(Y_2)$$，則 稱$$Y_2$$比$$Y_1$$有更多的資訊量。

由於知道了更多的資訊可知如何將$$Y_1$$中的事件分割更細得到$$Y_2$$，因此可得$$\sigma(Y_1) \subseteq \sigma(Y_2)$$。

### 一般σ域的條件期望值

考慮測度空間$$(\Omega, \mathcal{F}_0, \mathrm{P})$$的隨機變數$$X$$，且$$\mathrm{E}(|X|) < \infty$$。

#### 條件期望值隨機變數的存在性

考慮子σ域$$\mathcal{F} \subset \mathcal{F}_0$$。若條件期望$$\mathrm{E}(X|\mathcal{F})=Z$$為$$Z$$的隨機變數，且滿足：

1. 隨機變數$$Z$$在$$\mathcal{F}$$可測；或者寫成$$\sigma(Z) \subseteq \mathcal{F}$$。
2. $$\forall A \in \mathcal{F}$$，可得$$\displaystyle \int_A X d\mathrm{P} = \int_A Z d\mathrm{P}\equiv \int_A\mathrm{E}(X|\mathcal{F})dP$$或寫成$$\mathrm{E}(X\mathbf{1}_A)=\mathrm{E}(Z\mathbf{1}_A)$$。

<mark style="color:red;">稱隨機變數</mark>$$Z$$<mark style="color:red;">為</mark>$$X$$相對於$$\mathcal{F}$$<mark style="color:red;">的條件期望值。</mark>

<mark style="color:red;">而</mark>$$\mathrm{E}(I_A|\mathcal{F})$$<mark style="color:red;">稱為事件</mark>$$A\in \mathcal{F_0}$$相對於$$\mathcal{F}$$<mark style="color:red;">的條件機率，記為</mark>$$\mathrm{P}(A|\mathcal{F})$$。

<mark style="color:red;">條件期望值不唯一，對於任意的隨機變數，只要滿足條件(1,2)都是條件期望值的一個版本(a version of</mark> $$\mathrm{E}(X|\mathcal{F})$$。而<mark style="color:red;">任兩個版本的條件期望值只在零測集上相異(</mark>$$Z_1 = Z_2$$ <mark style="color:red;">almost surely)</mark>。

<details>

<summary>proof: 條件期望值存在性會用到Ryadon-Nikodym定理</summary>

<mark style="color:blue;">測度絕對連續</mark>：

令$$\mu, \nu$$分別為可測空間$$(\Omega, \mathcal{F})$$上的符號測度與測度，若$$\forall A \in \mathcal{F}$$，可得$$\mu(A) =0 \Rightarrow \nu(A)=0$$，則稱$$\nu$$

對$$\mu$$絕對連續，記為$$\nu \ll \mu$$。

<mark style="color:blue;">Ryadon-Nikodym定理</mark>

令$$\mu, \nu$$為可測空間$$(\Omega, \mathcal{F})$$上的兩個σ-finite測度。

如果$$\nu \ll \mu$$ ($$\nu$$對$$\mu$$絕對連續，$$\forall A \in \mathcal{F}$$，若$$\mu(A)=0$$可得$$\nu(A)=0$$)

則存在$$\mathcal{F}$$可測的函數$$f: \mathcal{F}\rightarrow [0, \infty)$$使得$$\forall A \in \mathcal{F}$$，有$$\displaystyle \int_Af d\mu=\nu(A)$$，$$f$$記為$$\displaystyle \frac{d\nu}{d\mu}$$稱為Randon-Nikodym導數。

常見範例。$$f$$為在實數區間$$A$$有定義的連續函數，$$\mu$$為Lebesgue測度，則$$\int_Af d\mu$$為函數在區間$$A$$的積分值，而$$\nu(A)$$可解釋為某函數在此區間$$A$$的面積。

<mark style="color:blue;">proof</mark>:

假設隨機變數$$X \geq 0$$且可積分，令$$\mu = \mathrm{P}$$，$$\displaystyle  \nu(A)=\int_A X d \mathrm{P},~ \forall A \in \mathcal{F}$$

可得$$\nu$$為σ-finite測度且當$$\mathrm{P}(A)=0$$時，可得$$\nu(A)=0$$，因此$$\nu \ll \mathrm{P}$$ 。

由Raydon-Nikodym定理可得存在可測函數$$\displaystyle Z=\frac{d \nu}{d \mu}$$使得$$\displaystyle \int_A X d \mathrm{P} = \nu(A) = \int_A \frac{d\nu}{d \mu} d \mathrm{P}$$

可得$$g$$為所求的條件期望。

對於$$X \in \mathbb{R}$$的情形，只要使用$$X=X^{+} - X^{-}$$的性質即為所求。

(QED)

</details>

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

### 條件期望值為最佳預測值

> $$\displaystyle \mathrm{E}(Y|X) = \arg \min_{g(X)} \mathrm{E}(Y-g(X))^2$$，即$$\mathrm{E}(Y|X)$$為對於$$Y$$的最佳預測值。



<details>

<summary>proof: 離散隨機變數</summary>

$$\displaystyle  \begin{aligned}  \mathrm{E}[(g(X)-Y)^2] & = \mathrm{E}[(g(X)- \mathrm{E}(Y|X) + \mathrm{E}(Y|X) - Y)^2] \\         & = E[(g(X) - \mathrm{E}(Y|X)^2)] \\         & + 2 \mathrm{E}[(g(X) - \mathrm{E}(Y|X))(\mathrm{E}(Y|X)- Y)] \\         & + \mathrm{E}[(\mathrm{E}(Y|X)-Y)^2] \end{aligned}$$

其中第二項展開後得：$$\displaystyle  \begin{aligned} \mathrm{E}[(g(X) - \mathrm{E}(Y|X))(\mathrm{E}(Y|X)- Y)] &= \mathrm{E}[g(X) \mathrm{E}(Y|X) ] \\     & -\mathrm{E}[\mathrm{E}(Y|X) \mathrm{E}(Y|X)] \\     & - \mathrm{E}[g(X)Y] \\     & + \mathrm{E}[Y \mathrm{E}(Y|X)] \\     & = \mathrm{E}[g(X)Y] - \mathrm{E}[Y\mathrm{E}(Y|X)] - \mathrm{E}[g(X)Y] + \mathrm{E}[Y\mathrm{E}(Y|X)] \\     & = 0 \end{aligned}$$而第三項與$$g(X)$$無關。

因此第一項為0時，可得$$\mathrm{E}[(Y-g(X))^2]$$有最小值，即$$g(X) = \mathrm{E}(Y|X)$$ (QED)

</details>

### 重複期望值定理(law of iterated expectation, Law of total expectation)

> &#x20;$$\mathrm{E}(\mathrm{E}(X|Y))=\mathrm{E}(X)$$
>
> 簡單地說，$$X$$的平均值等於條件平均值的加權平均值。

<details>

<summary>proof: 離散隨機變數</summary>

$$\displaystyle {\begin{aligned} \mathrm {E}\left(\mathrm {E}(X|Y)\right)&{}=\sum \limits _{y}\mathrm {E}(X|Y=y)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\left(\sum \limits _{x}x\cdot \mathrm {P}(X=x|Y=y)\right)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\sum \limits _{x}x\cdot \mathrm {P}(X=x|Y=y)\cdot \mathrm {P}(Y=y)\\&{}=\sum \limits _{y}\sum \limits _{x}x\cdot \mathrm {P}(Y=y|X=x)\cdot \mathrm {P}(X=x)\\&{}=\sum \limits _{x}\sum \limits _{y}x\cdot \mathrm {P}(Y=y|X=x)\cdot \mathrm {P}(X=x)\\&{}=\sum \limits _{x}x\cdot \mathrm {P}(X=x)\cdot \left(\sum \limits _{y}\mathrm {P}(Y=y|X=x)\right)\\&{}=\sum \limits _{x}x\cdot \mathrm {P}(X=x)\\&{}=\mathrm {E}(X).\end{aligned}}$$

</details>

<details>

<summary>proof: 連續隨機變數</summary>

$${\displaystyle {\begin{aligned}\mathrm {E} (X)&=\int x\Pr[X=x]~dx\\\mathrm {E} (X\mid Y=y)&=\int x\Pr[X=x\mid Y=y]~dx\\\mathrm {E} (\mathrm {E} (X\mid Y))&=\int \left(\int x\Pr[X=x\mid Y=y]~dx\right)\Pr[Y=y]~dy\\&=\int \int x\Pr[X=x,Y=y]~dx~dy\\&=\int x\left(\int \Pr[X=x,Y=y]~dy\right)~dx\\&=\int x\Pr[X=x]~dx\\&=\mathrm {E} (X)\,.\end{aligned}}}$$

</details>

## 參考資料

* [\[知乎\] 淺談條件期望](https://zhuanlan.zhihu.com/p/23670286)
* [\[知乎\] 條件期望值的初步理解](https://zhuanlan.zhihu.com/p/50757083)
* [\[statlect\] Conditional probability with respect to a sigma-algebra](https://www.statlect.com/fundamentals-of-probability/conditional-probability-as-a-random-variable)
* [\[wiki\] conditional expectation](https://en.wikipedia.org/wiki/Conditional\_expectation#Conditional\_expectation\_with\_respect\_to\_a\_.CF.83-algebra)
* [\[知乎\] 條件期望與全期望公式](https://zhuanlan.zhihu.com/p/417592820)
* [\[知乎\] 重期望公式及實例運用](https://zhuanlan.zhihu.com/p/163363352)
* [\[譚升的部落格\] 條件期望](https://face2ai.com/Math-Probability-4-7-Conditional-Expectation/)
* [Lecture 10 Conditional Expectation](https://web.ma.utexas.edu/users/gordanz/notes/conditional\_expectation.pdf)
  * [https://web.ma.utexas.edu/users/gordanz/lecture\_notes\_page.html](https://web.ma.utexas.edu/users/gordanz/lecture\_notes\_page.html)
* [Conditional expectation toy example](https://people.maths.bris.ac.uk/\~mb13434/cond\_expn\_example\_balazs.pdf)





