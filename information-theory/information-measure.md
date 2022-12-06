# 資訊度量

## 訊息量

當我們觀測到或聽到一個事件發生時(由信源發出)，就得到了一些「訊息」。「訊息量」指的是：該訊息的內涵多寡，也可以這麼說：「訊息」的內涵是用來表達某事件之各種可能結果可能性大小。

<mark style="color:red;">**當事件越明確時，關於此事件所包含的訊息量越小**</mark>**。**而當事件越模糊(機率接近0.5或1/n，均勻分配)時，提供一件可供判斷的參考就含有較多的訊息。&#x20;<mark style="color:red;">當機率越平均時，也就是個事件發生機率越均勻(即越無法預測，也越模糊)，「不確定性」(uncertainty)最高，此時訊息熵最大</mark>。

故「訊息」可以視為「不確定性」或「訊息選擇的自由度」之度量。(Information is a measure of one's freedom of choice when one selects a message)一條資訊的信息量大小和它的不確定性有直接的關係，與事件發生的機率有關。

比如說，我們要了解一件非常非常不確定的事，或是我們一無所知的事情，就需要瞭解大量的資訊。相反，如果我們對某件事已經有了較多的瞭解，我們不需要太多的資訊就能把它搞清楚。所以，<mark style="color:red;">從這個角度來說，我們可以將不確定性(自由度)的多寡做為信息量的度量。簡單的說，</mark><mark style="color:red;">**變數的不確定性越大，熵也就越大**</mark>。

接收者收到訊息，實際上就是從不確定到比較確定或完全確定的過程，因此獲得訊息的過程，就會有不確性減小的程度。因此可觀察到<mark style="color:red;">**訊息量為不確定程度的減少量**</mark>。因此可推出不確定性程度和事件發生的機率有關，事件發生機率越小，不確定性越大，因此訊息量越大。

Hartley(1928)提出了一個資訊的對數度量。他的度量標准基本上是字母表大小的對數。即$$\mathrm{H}(X)=K \log (\frac{1}{\mathrm{p}})$$, 通常$$K=1$$，因此$$\mathrm{H}(x_i)=- \log(\mathrm{P}(x_i)$$為不確定量的基本關係式。有兩種解釋方法：

* 在事件$$x_i$$發生之前，其值等於事件$$x_i$$的不確定量。
* 在事件$$x_i$$發生之後，其值表示事件$$x_i$$所含有或所能提供的訊息量。

![熵、聯合熵、條件熵、互資訊的關係](../.gitbook/assets/information\_measure\_set-min.png)



| 名稱   | 符號                                     | 關係                                                                                                                                                                                                                                                                    |
| ---- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 無條件熵 | $$\mathrm{H}(X)$$                      | <ul><li><span class="math">\mathrm{H}(X) = \mathrm{H}(X|Y) + \mathrm{I}(X;Y) \geq \mathrm{H}(X|Y)</span></li><li><span class="math">\mathrm{H}(X) = \mathrm{H}(X,Y) - \mathrm{H}(Y|X)</span></li></ul>                                                                |
| 無條件熵 | $$\mathrm{H}(Y)$$                      | <ul><li><span class="math">\mathrm{H}(Y) = \mathrm{H}(Y|X) + \mathrm{I}(X;Y) \geq \mathrm{H}(Y|X)</span></li><li><span class="math">\mathrm{H}(Y) = \mathrm{H}(X,Y) - \mathrm{H}(X|Y)</span></li></ul>                                                                |
| 條件熵  | $$\mathrm{H}(X|Y)$$                    | $$\mathrm{H}(X|Y) = \mathrm{H}(X,Y) - \mathrm{H}(Y) = \mathrm{H}(X) - \mathrm{I}(X;Y)$$                                                                                                                                                                               |
| 條件熵  | $$\mathrm{H}(Y|X)$$                    | $$\mathrm{H}(Y|X) = \mathrm{H}(X,Y) - \mathrm{H}(X) = \mathrm{H}(Y) - \mathrm{I}(X;Y)$$                                                                                                                                                                               |
| 聯合熵  | $$\mathrm{H}(X,Y) =  \mathrm{H}(Y,X)$$ | $$\begin{aligned}  & \mathrm{H}(X,Y)  \\  &=  \mathrm{H}(X) + \mathrm{H}(Y|X) \\     & = \mathrm{H}(Y) + \mathrm{H}(X|Y) \\     & = \mathrm{H}(X)+ \mathrm{H}(Y) - \mathrm{I}(X;Y) \\     & = \mathrm{H}(X|Y) + \mathrm{H}(Y|X) + \mathrm{I}(X;Y)  \end{aligned}$$    |
| 互資訊  | $$\mathrm{I}(X;Y) = \mathrm{I}(Y;X)$$  | $$\begin{aligned}  &  \mathrm{I}(X;Y)  \\  &=  \mathrm{H}(X) - \mathrm{H}(X|Y) \\     & = \mathrm{H}(Y) - \mathrm{H}(Y|X) \\     & = \mathrm{H}(X,Y )-  \mathrm{H}(Y|X) - \mathrm{H}(X|Y) \\     & = \mathrm{H}(X) + \mathrm{H}(Y) - \mathrm{I}(X;Y)  \end{aligned}$$ |

## 資訊熵

> <mark style="color:red;">definition: information (Shannon) entropy</mark>
>
> $$\displaystyle \mathrm{H}(X) = -\sum_{x \in X} \mathrm{P}(x) \log \mathrm{P}(x)$$, $$X$$為離散隨機變數$$x$$的樣本空間。
>
> 令 $$0 \log 0 \equiv 0$$($$\because x \log x \rightarrow 0 \text{ as } x \rightarrow 0$$)

由於隨機變數$$X$$為函數，因此$$\mathrm{H}(\cdot)$$為泛函(functional)，且熵的計算與隨機變數$$X$$的實現值$$x$$無關，而與其機率$$\mathrm{P}(X=x)$$有關。

熵是隨機變數的不確定性的平均度量值，隨機變數變異數越大，即隨機變數越「亂」，則熵之值越大。

熵最大值發生在隨機變數為平均分佈(uniform distribution)時 (參考 maxinum entropy principle)。

公式中，$$\log$$以2為底時，$$\mathrm{H}(X)$$之值的單位為bit；而以自然數$$e$$為底時，$$\mathrm{H}(X)$$之值的單位為nats，以10為基底時，單位為Hartley。

熵的值可解釋為使用二進位編碼隨機變數時，其值等於變數的平均編碼長度。

### 熵必為正實數

> $$\mathrm{H}(X) \geq 0$$

$$\because 0\leq \mathrm{P}(x) \leq1 ~ \therefore \log \mathrm{P}(x) \leq0$$

$$\therefore \displaystyle  \mathrm{H}(x) = -\sum_{x \in X} \mathrm{P}(x) \log \mathrm{P}(x) \geq 0$$(QED)

### 熵可改寫為期望值型式

> $$\begin{aligned} \mathrm{H}(X) &= - \sum_{x \in X}\mathrm{P}(x) \log \mathrm{P}(x) \\ &=\mathrm{E_P}\big(\log \frac{1}{\mathrm{P}(x)} \big) \\& = -\mathrm{E_P}(\log \mathrm{P}(x)) \end{aligned}$$

### 不同對數基底的熵的差異為常數倍

> $$\mathrm{H}_b(X) = (\log_b(a))\mathrm{H}_a(X)$$

### 熵值為0若且唯若隨機變數退化為確定值

> $$\mathrm{H}(X) = 0 \Leftrightarrow$$$$X$$的實現值為確定值。

### 熵為凹函數(開口向下)

> $$\mathrm{H}(\lambda X_1 + (1-\lambda)X_2) \geq \lambda \mathrm{H}(X_1) + (1-\lambda)\mathrm{H}(X_2)$$

### 熵與聯合熵的關係(鏈法則)

> * $$\mathrm{H}(X,Y) = \mathrm{H}(X) + \mathrm{H}(Y|X) = \mathrm{H}(Y) + \mathrm{H}(X|Y)$$



> $$\displaystyle \mathrm{H}(X_1, X_2, \ldots, X_N) = \sum_{i=1}^N \mathrm{H}(X_i |X_{i-1}, \ldots, X_2, X_1)$$

* $$\mathrm{H}(X_1, H_2)= \mathrm{H}(X_1)+\mathrm{H}(X_2| X_1)$$
* $$\begin{align} \mathrm{H}(X_1, X_2, X_3) & =\mathrm{H}(X_1)+\mathrm{H}(X_2,X_3|X_1)\\ & =\mathrm{H}(X_1)+\mathrm{H}(X_2|X_1)+\mathrm{H}(X_3|X_1, X_2) \\ \end{align}$$



### 熵的上界受限於隨機變數實現值集合的大小

> 隨機變數$$X$$熵$$\mathrm{H}(X)$$的上界，受限於該隨機變數的實現值集合 $$\mathcal{X}$$的機率分佈。>

> 對於任意的隨機變數$$X$$, $$\mathrm{H}(X)≤log⁡(|\mathcal{X}|)$$，$$|\cdot|$$為集合的基數。
>
> 等號成立於$$X$$在$$\mathcal{X}$$中發生的機率均等時。

## 聯合熵(joint entropy)

> 兩個隨機變數$$X,Y$$的<mark style="color:red;">聯合熵，可解釋為兩個隨機變數包含的資訊總量</mark>。
>
> 令$$\mathrm{P}(X,Y)$$為聯合機率密度函數，$$\displaystyle \mathrm{H}(X,Y) = - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(x,y) = - \mathrm{E}(\log \mathrm{P}(x,y))$$

### 獨立隨機變數熵的總和為其聯合熵的上界

> * $$\displaystyle \mathrm{H}(X,Y) \leq  \mathrm{H}(X) +  \mathrm{H}(Y)$$
> * $$\displaystyle \mathrm{H}(X_1, X_2, \ldots, X_N ) \leq \sum_{i=1}^{N} \mathrm{H}(X_i)$$
>
> 等號成立於$$X_i$$與$$X_j$$為兩兩獨立的隨機變數。
>
> 以資訊總量的觀點解釋為當隨機變數兩兩獨立時，資訊總量為可直接加總

### 聯合熵的鏈法則

> 令隨機變數$$X_1, X_2,\dots, X_N$$的聯合分佈$$\mathrm{P}(x_1,x_2,\dots, x_n)$$，則 $$\mathrm{H}(X_1, X_2, \dots, X_n) = \sum_{i=1}^n H(X_i | X_{1}, X_2, \dots, X_{i-1})$$。

* $$\mathrm{H}(X_1, X_2) =  \mathrm{H}(X_1) + \mathrm{H}(X_2|X_1)$$
* $$\mathrm{H}(X_1, X_2, X_3) =  \mathrm{H}(X_1) + \mathrm{H}(X_2|X_1) +  \mathrm{H}(X_3|X_1, X_2)$$
* 以此類推可得
* $$\mathrm{H}(X_1, X_2, \dots, X_n) =  \mathrm{H}(X_1) + \mathrm{H}(X_2|X_1) +  \mathrm{H}(X_3|X_1, X_2) + \dots + \mathrm{H}(X_n|X_1, X_2, \dots, X_{n-1})$$(QED)



## 條件熵 (conditional entropy)

> <mark style="color:red;">條件熵</mark>$$\mathrm{H}(X|Y)$$<mark style="color:red;">可解釋為給定隨機變數</mark>$$Y$$<mark style="color:red;">的資訊後，</mark>$$X$$<mark style="color:red;">殘餘的資訊量</mark>。

* $$\begin{align} \mathrm{H}(Y|X) &= -\sum_{x \in X} \mathrm{P}(x)\mathrm{H}(Y|X=x) \\  &= -\sum_{x \in X} \mathrm{P}(x) \sum_{y \in Y} \mathrm{P}(y|x)\log \mathrm{P}(y|x) \\ & = -\sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(y|x) \\ &= -\mathrm{E}(\log \mathrm{P}(Y|X)) \end{align}$$
* $$\begin{align} \mathrm{H}(X|Y)      & = -\sum_{y \in Y} \sum_{x \in X} \mathrm{P}(x,y) \log \mathrm{P}(x|y) \\      &= -\mathrm{E}(\log \mathrm{P}(X|Y)) \end{align}$$

### 聯合熵、條件熵、與互資訊的關係(chain rule)

> * $$\begin{aligned} \mathrm{H}(X,Y) & = \mathrm{H}(X) + \mathrm{H}(Y|X)  \\     & = \mathrm{H}(Y) + \mathrm{H}(X|Y) \end{aligned}$$
> * $$\begin{aligned} \mathrm{I}(X,Y) & = \mathrm{H}(X) + \mathrm{H}(X|Y)  \\     & = \mathrm{H}(Y) + \mathrm{H}(Y|X) \end{aligned}$$

$$\mathrm{H}(X)−\mathrm{H}(X|Y)$$為隨機變數$$X$$的資訊量減去給定隨機變數$$Y$$後$$X$$的資訊量，此時剩下的為$$X$$與$$Y$$共同含有的資訊量$$\mathrm{I}(X;Y)$$，也等於$$\mathrm{H}(Y)-\mathrm{H}(Y|X)$$。

註：此處給定的$$X$$或$$Y$$是隨機變數，而不是固定的值。

proof:

$$\displaystyle  \begin{aligned} \mathrm{H}(X,Y) &= - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(x,y) \\     & = - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \left(\mathrm{P}(x) \mathrm{P}(y|x)  \right) \\     & = - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(x)           - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(y|x) \\     & = - \sum_{x \in X} \mathrm{P}(x) \log \mathrm{P}(x)           - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(y|x) \\     & = \mathrm{H}(X) + \mathrm{H}(Y|X) \end{aligned}$$(QED)

### 條件熵不具有交換性&#xD;

> $$\mathrm{H}(X|Y) \neq \mathrm{H}(Y|X)$$，因相異隨機變數的資訊量不相等。

### 兩隨機變數的聯合熵等於單個隨機變數的熵加上條件熵(chain rule)&#xD;

> * $$\mathrm{H}(X,Y)=\mathrm{H}(X) +\mathrm{H}(Y|X) = \mathrm{H}(Y) +\mathrm{H}(X|Y)$$
> * 可寫成$$\log_{\mathrm{P}}(X,Y) = \log_{\mathrm{P}}(X) + \log_{\mathrm{P}}(Y|X)= \log_{\mathrm{P}}(Y) + \log_{\mathrm{P}}(X|Y)$$

推廣可得 $$\mathrm{H}(X,Y|Z)=\mathrm{H}(X|Z) +\mathrm{H}(Y|X,Z)$$

### 條件熵為0若且若且隨機變數為給定隨機變數的函數

> $$\mathrm{H}(Y|X) = 0 \Leftrightarrow  \exists f \ni f(X)=Y$$
>
> 若隨機變數$$Y$$為給定隨機變數$$X$$的函數時，即$$Y=f(X)$$，則$$X=x$$的實現值已知時，$$Y$$的實現值$$y=f(x)$$也可得出，不再具有隨機性，因此條件熵為0。

### 給定條件資訊不會增加熵的量(給定資訊可減少不確定性)

> * $$\mathrm{H}(Y|X) \leq \mathrm{H}(Y)$$&#x20;
> * $$\mathrm{H}(X|Y) \leq \mathrm{H}(X)$$

* <mark style="color:red;">等號成立在</mark>$$X$$<mark style="color:red;">與</mark>$$Y$$<mark style="color:red;">為獨立時</mark>，即$$\mathrm{I}(X;Y)=0$$。
* $$\mathrm{H}(Y|X) \leq \mathrm{H}(Y)$$ 是考慮所有實現值的<mark style="color:red;">平均值</mark>，而非特定實現值$$Y=y$$時的不等式，因此在特定的$$y$$，此不等式不成立。

proof:

$$\displaystyle  \begin{aligned} \mathrm{H}(X|Y) &= - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \mathrm{P}(x|y) \\     & = - \sum_{x \in X} \sum_{y \in Y} \mathrm{P}(y) \mathrm{P}(x|y) \log \mathrm{P}(x|y) \\     & = - \sum_{y \in Y} \mathrm{P}(y) \sum_{x \in X}  \mathrm{P}(x|y) \log \mathrm{P}(x|y) \\     & \leq - \sum_{y \in Y} \mathrm{P}(y) \sum_{x \in X}  \mathrm{P}(x|y) \log \mathrm{P}(x) \\     & = \sum_{x \in X}  \sum_{y \in Y}  \mathrm{P}(y) \mathrm{P}(x|y) \log \mathrm{P}(x) \\     & = \sum_{x \in X}  \sum_{y \in Y}  \mathrm{P}(x, y) \log \mathrm{P}(x) \\     & = \mathrm{H}(X) \end{aligned}$$(QED)

## 互資訊(mutual information)

> <mark style="color:red;">互資訊為兩個隨機變數中相同的資訊量，可想成集合論中的交集部份</mark>。
>
> $$\begin{align} \mathrm{I}(X;Y) &=\sum_{x \in X}  \sum_{y \in Y}\mathrm{P}(x,y) \log{\frac{\mathrm{P}(x,y)}{\mathrm{P}(x)\mathrm{P}(y)}} \\ &=\mathrm{D}(\mathrm{P}(x,y)\| \mathrm{P}(x)\mathrm{P}(y)) \\ & =\mathrm{E}_{\mathrm{P}(x,y)}\left( \frac{\mathrm{P}(x,y)}{\mathrm{P}(x)\mathrm{P}(y)}\right) \end{align}$$

* $$\mathrm{D}(\mathrm{P}(x,y) \| \mathrm{P}(x)\mathrm{P}(y))$$: 可解釋為聯合分佈相對於兩變數為獨立分佈的分散程度。

### 互資訊為兩隨機變數中相同的資訊量

> * $$\mathrm{H}(X,Y)= \mathrm{H}(X)+\mathrm{H}(Y|X)=\mathrm{H}(Y) + \mathrm{H}(X|Y)$$
> * $$\mathrm{I}(X;Y)=\mathrm{H}(Y) - \mathrm{H}(X|Y)=\mathrm{H}(X) - \mathrm{H}(Y|X)=\mathrm{H}(X)+\mathrm{H}(Y)-\mathrm{H}(X,Y)$$

$$\begin{align}  \mathrm{I}(X;Y)      &=\sum_{x \in X}  \sum_{y \in Y}\mathrm{P}(x,y) \log{\frac{\mathrm{P}(x,y)}{\mathrm{P}(x)\mathrm{P}(y)}} \\      &=\sum_{x \in X}  \sum_{y \in Y} \mathrm{P}(x,y) \log{\frac{\mathrm{P}(x|y)}{\mathrm{P}(x)}} \\      & = -\sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log{\mathrm{P}(x)} +\sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log{\mathrm{P}(x|y)} \\     & = -\sum_{x \in X} \mathrm{P}(x) \log{\mathrm{P}(x)} +\sum_{x \in X} \sum_{y \in Y} \mathrm{P}(x,y) \log{\mathrm{P}(x|y)} \\     & = \mathrm{H}(X) -  \mathrm{H}(X|Y) \end{align}$$

(QED)

### 互資訊有對稱性

> $$\mathrm{I}(X;Y) = \mathrm{I}(Y;X)$$
>
> 因為互資訊為兩個隨機變數共同的資訊量，因此有對稱性。$$\displaystyle \mathrm{I}(X;Y) = \sum_x \sum_y \mathrm{P}(x,y) \log{\frac{\mathrm{P}(x,y)} {\mathrm{P}(x)\mathrm{P}(y)}} = \sum_y \sum_x \mathrm{P}(x,y) \log{\frac{\mathrm{P}(x,y)} {\mathrm{P}(x)\mathrm{P}(y)}} = \mathrm{I}(Y;X)$$(QED)

### 互資訊為0若且唯若兩隨機變數獨立

> * 對於任意隨機變數$$X,Y$$, $$\mathrm{I}(X;Y) \geq 0$$
> * $$\mathrm{I}(X;Y) = 0 \Leftrightarrow \log{\frac{\mathrm{P}(x,y)}{\mathrm{P}(x)\mathrm{P}(y)}}=0$$

$$\mathrm{P}(x,y)=\mathrm{P}(x)\mathrm{P}(y)$$, 即兩隨機變數獨立(independent)，因為彼此之間沒有任何相關的訊息。

Proof:

* 因為$$\mathrm{I}(X;Y) = \mathrm{D}(\mathrm{P}(x,y) \parallel \mathrm{P}(x)\mathrm{P}(y)) \geq 0$$
* 而上式等號成立於$$\mathrm{P}(x,y) =\mathrm{P}(x)\mathrm{P}(y)$$，即兩隨機變數獨立(QED)

### 資訊本體(self information)

> * $$\mathrm{I}(X;X)=\mathrm{H}(X)-\mathrm{H}(X|X)=\mathrm{H}(X)-0=\mathrm{H}(X)$$
> * $$\mathrm{I}(X;X)=\mathrm{E}\big( \log{\frac{\mathrm{P}(X)}{\mathrm{P}(X)^2}}\big) = -\mathrm{E}(\log \mathrm{P}(X))=\mathrm{H}(X)$$

$$\mathrm{H}(X|X)$$解釋為給定隨機變數$$X$$的訊息後，因為已經有$$X$$的所有資訊，所以$$\mathrm{H}(X|X)$$不含任何資訊量，因此值為0。

$$\mathrm{I}(X;X)$$為隨機變數$$X$$和隨機變數$$X$$共有的資訊量，等於隨機變數$$X$$的資訊量$$\mathrm{H}(X)$$。

### 互資訊鏈法則

> $$\mathrm{I}(X_1, X_2,\ldots, X_N; Y)=\sum_{i=1}^N \mathrm{I}(X_i;Y|X_{i-1}, \ldots, X_2, X_1)$$

* $$\mathrm{I}(X_1,X_2;Y)=\mathrm{I}(X_1;Y)+\mathrm{I}(X_2;Y|X_1)$$
* $$\mathrm{I}(X_1,X_2,X_3;Y)=\mathrm{I}(X_1;Y)+\mathrm{I}(X_2;Y|X_1)+\mathrm{I}(X_3;Y|X_1,X_2)$$

## 條件互資訊(conditional mutual information)

> $$\begin{align} \mathrm{I}(X;Y|Z) & =\mathrm{H}(X|Z)-\mathrm{H}(X|Y,Z) \\& =\mathrm{H}(Y|Z) - \mathrm{H}(Y|X,Z) \\ &=\mathrm{H}(X|Z)+\mathrm{H}(Y|Z)-\mathrm{H}(X,Y|Z) \\& =\mathrm{E}_{\mathrm{P}(X,Y,Z)}\big( \log{\frac{\mathrm{P}(X,Y|Z)}{\mathrm{P}(X|Z) \mathrm{P}(Y|Z)}} \big) \end{align}$$隨機變數$$X$$與$$Y$$，再給定$$Z$$後的互資訊。

$$\mathrm{I}(X;Y|Z) \geq 0$$，且等號成立於$$X$$與$$Y$$在給定$$Z$$之後條件獨立。

## 相對熵(relative entropy)、Kullback-Leibler距離

> definition: KL-distance
>
> * $$\begin{aligned} \mathrm{D}(P \parallel Q) &= \sum_{x \in X} \mathrm{P}(x) \log \frac{\mathrm{P}(x)}{\mathrm{Q}(x)} \\ & = \mathrm{E}_{\mathrm{P}} \log \frac{\mathrm{P}(x)}{\mathrm{Q}(x)}  \end{aligned}$$
> * 令$$0 \log \frac{0}{0} = 0$$、$$0 \log \frac{0}{\mathrm{Q}} = 0$$、$$\mathrm{P} \log \frac{\mathrm{P}}{0} = \infty$$。
> * 因此若$$\mathrm{P}(x) > 0$$且 $$\mathrm{Q}(x)=0$$則 $$\mathrm{D}(P \parallel Q) =\infty$$

* 相對熵是兩個分佈之間遠離程度的度量(和距離度量相似，但不滿足交換性)。
* 由於$$\log \frac{\mathrm{P}(x)}{\mathrm{Q}(x)} \neq \log \frac{\mathrm{Q}(x)}{\mathrm{P}(x)}$$，因此$$\mathrm{D}(P \parallel Q) \neq \mathrm{D}(Q \parallel P)$$。
* <mark style="color:red;">機器學習中，經常將</mark>$$Q$$<mark style="color:red;">視為資料的真實分佈</mark>，<mark style="color:red;">而</mark>$$P$$<mark style="color:red;">為學習模型的分佈，目標函數為最小化</mark>$$\mathrm{D}(P \parallel Q)$$，<mark style="color:red;">將</mark>$$P$$<mark style="color:red;">逐漸逼近</mark>$$Q$$。

### 兩機率分佈的KL距離為0若且唯若兩分佈相等

> 令$$\mathrm{P}(x), ~ \mathrm{Q}(x), ~ x \in X$$為兩機率分佈，則&#x20;
>
> * $$\mathrm{D}(\mathrm{P} \parallel \mathrm{Q} )\geq 0$$，且
> * $$\mathrm{D}(\mathrm{P} \parallel \mathrm{Q} ) = 0 \Leftrightarrow \mathrm{P}(x) = \mathrm{Q}(x), ~ \forall x \in X$$

proof:

* 令$$A = \{ x| \mathrm{P}(x) > 0\}$$為分佈$$\mathrm{P}(x)$$的支撐集。
* $$\begin{aligned} - \mathrm{D}(\mathrm{P} \parallel \mathrm{Q} )  	& = - \sum_{x \in A} \mathrm{P}(x) \log \frac{\mathrm{P}(x)}{\mathrm{Q}(x)} \\ 	& =  \sum_{x \in A} \mathrm{P}(x) \log \frac{\mathrm{Q}(x)}{\mathrm{P}(x)} \\ \text{[Jensen's ineq.]}	& \leq \log \sum_{x \in A} \mathrm{P}(x) \frac{\mathrm{Q}(x)}{\mathrm{P}(x)}  \\ 	& = \log \sum_{x \in A} \mathrm{Q}(x) \\ 	& \leq \log \sum_{x \in X} \mathrm{Q}(x) \\ 	& = \log 1 \\ 	& = 0  \end{aligned}$$(QED)

### 條件相對熵(conditional relative entropy)

> $$\mathrm{D}(\mathrm{P}(x,y) \parallel \mathrm{Q}(x,y)) = \mathrm{D}(\mathrm{P}(x) \parallel \mathrm{Q}(x))  +  \mathrm{D}(\mathrm{P}(y|x) \parallel \mathrm{Q}(y|x))$$

proof:

$$\begin{aligned}  & \mathrm{D}(\mathrm{P}(x,y) \parallel \mathrm{Q}(x,y))  \\ & = \sum_{x\in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \frac{\mathrm{P}(x,y)}{\mathrm{Q}(x,y)} \\ & = \sum_{x\in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \frac{\mathrm{P}(x)\mathrm{P}(y|x)}{\mathrm{Q}(x)\mathrm{Q}(y|x)} \\ & = \sum_{x\in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \frac{\mathrm{P}(x)}{\mathrm{Q}(x)} + 	\sum_{x\in X} \sum_{y \in Y} \mathrm{P}(x,y) \log \frac{\mathrm{P}(y|x)}{\mathrm{Q}(y|x)} \\ & = \mathrm{D}(\mathrm{P}(x) \parallel \mathrm{Q}(x))  +  \mathrm{D}(\mathrm{P}(y|x) \parallel \mathrm{Q}(y|x))   \end{aligned}$$(QED)

## 參考資料

* Hartley, Ralph VL. "Transmission of information 1." Bell System technical journal 7.3 (1928): 535-563.
* [\[香港中文大學\] Prof. Yeung Wai-Ho, Raymond 楊偉豪教授](https://www.ie.cuhk.edu.hk/people/raymond.shtml)。
