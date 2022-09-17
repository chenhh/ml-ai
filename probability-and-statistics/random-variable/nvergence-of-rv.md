# 隨機變數的收斂

## 簡介

隨機變數的收斂(convergence of random variable)被稱為隨機收斂，表示一系列本質上隨機不可預測的事件所發生的模式可以在樣本數量足夠大的時候得到合理可靠的預測。各種不同的收斂定義實際上是表示預測時不同的刻畫方式。

當樣本數無止盡的增大， 一些關於樣本的量會有什麼極限的結果？ 雖然無限的樣本數只是一理論上的假設，但極限之下的結果，常可做為有限樣本數之下很好的近似值。

## 分佈收斂(convergence in distribution)

> $$\displaystyle \lim_{ n \rightarrow \infty}F_n(x) = F(x)$$

依分佈收斂是個完全不同的概念。依分佈收斂是一個分佈函數收斂的概念。所以$$X_n$$與$$X$$甚至都可以不被定義在同一個機率空間之內。

* 當$$n$$很大的時候，$$X_n$$的累積分佈函數和$$X$$的累積分佈函數差不多。
* 直觀上而言，依分佈收斂只在乎隨機變量的分佈，而不在乎他們之間的相互關系。
* 依分佈收斂的隨機變數序列$$X_n$$在機率空間上不一定收斂於$$X$$。

## 機率收斂(convergence in probability)

> 設 $$X_1,X_2, \cdots$$為一數列之隨機變數（不必為i.i.d.），若存在一隨機變數 $$X$$，使得
>
> $$\displaystyle \forall \epsilon >0, ~\lim_{n \rightarrow \infty}\mathrm{P}(\| X_n -X\|>\epsilon) = 0$$  等價於
>
> * $$\displaystyle \forall \epsilon >0, ~ \lim_{n \rightarrow \infty} \mathrm{P}(|X_n -X| \geq \epsilon) = 0$$
> * $$\displaystyle \forall \epsilon >0, ~ \lim_{n \rightarrow \infty} \mathrm{P}(|X_n -X| < \epsilon) = 1$$
> * $$\displaystyle \forall \epsilon >0, ~ \lim_{n \rightarrow \infty} \mathrm{P}(|X_n -X| \leq \epsilon) = 1$$

機率收斂的意思是，當$$n$$趨向無窮，$$X_n$$與$$X$$之間不相等的部分機率趨向於0（對任意的結果$$\omega$$，$$|(X_n -X)(\omega) |$$很小)。<mark style="color:red;">即在序列夠長(樣本夠多)時，</mark>$$X_n$$<mark style="color:red;">會逐漸收斂至</mark>$$X$$<mark style="color:red;">，偶爾</mark>$$X_n$$<mark style="color:red;">會偏離</mark>$$X$$<mark style="color:red;">，但次數很少在機率上可忽略不計</mark>。

機率中一個十分讓人困惑的點就是某個事件發生的機率為0，但它能發生。

和處處收斂的區別是，由於誤差的存在，$$X_n$$可能在某次結果出現偏離$$X$$的情況，只不過這種可能性或許會越來越小，但不能保證不發生。也就是不能保證$$X_n$$從哪一個時刻其永遠保持恆定狀態。

### 機率收斂和幾乎確定收斂的範例

$$X_n= \left\{  \begin{aligned} 1, & \text{with prob }\frac{1}{n} \\ 0, & \text{with prob } 1-\frac{1}{n}  \end{aligned}  \right.$$

則$$\displaystyle  \lim_{n \rightarrow \infty} \mathrm{P} (|X_n - 0| > \epsilon) =  \lim_{n \rightarrow \infty}  \frac{1}{n} = 0$$

當$$n \rightarrow \infty$$時，$$X_n=1$$的機率為0，但是$$X_n=1$$仍然有可能發生。

以測度論來說，$$\{\omega| X(\omega)=1\}$$這個事件的集合是零測度集，而依機率收論就是允許不收斂的$$X_n$$集合是零測度集。

而幾乎處處收斂$$\displaystyle \lim_{n \rightarrow \infty}X_n= X$$不收斂的集合也是零測度集，但是零測度集為空集合$$(\exists n_0 \ni \mathbb{N} \ni \{\omega ~|~ X_n(\omega) \neq X(\omega) | n \geq n_0\} = \empty$$。

整理可得：

* 機率為0的事件仍可能會發生。
* 測度為0的集合為零測度集，但是零測度度不一定是空集合。

### 範例：丟硬幣

令$$X_i= \left\{  \begin{aligned} 1, & \text{第i次出現正面} \\ 0, & \text{第i次出現反面 } \end{aligned}  \right.$$$$i=1,2,\dots, n$$

則正面出現的總次數為$$\sum_{i=1}^n X_i$$次。正面出現的機率為$$f_n(A)=\frac{1}{n}\sum_{i=1}^n X_i$$為隨機變數序列。

而$$\forall \epsilon >0$$，只要$$n$$足夠大，可得$$|f_n(A) - 1/2| \geq \epsilon$$不成立的情形顯然有可能發生，因此不滿足點態收斂的定義。

不論$$n$$多大，，雖然機率很小，但有可能丟出全部為正面或反面的結果，此時$$f_n(A)=1$$或0，若給定$$\epsilon =0.2$$，則$$|f_n(A)-1/2|-0.5 \geq \epsilon$$發生。

但可算出$$\mathrm{P}(n\text{次全為正面或反面})=\frac{1}{2^{n-1}} \rightarrow 0$$。

雖然隨機變數無法直接收斂，但可將條件減弱為$$\forall \epsilon > 0$$，雖然事件$$|X_n - X| \geq \epsilon$$有可能發生，但只要$$n$$足夠大，可保證發生的機率足夠小，即$$\mathrm{P}(|X_n - X| \geq \epsilon) \rightarrow 0$$。

因此機率收斂可解釋為：

* $$n$$很大時，$$X_n$$ 與$$X$$出現較大偏差的可能性很小。
* $$n$$很大時，有很高可能性$$X_n$$與$$X$$很接近。

### 經驗分佈為分佈的良好估計式

對同一分佈函數$$F$$，雖每次會有不同的觀測值，因此會得到不同的經驗分佈$$F_n(x) = \frac{X_i \leq x}{n}, ~ \forall x \in \mathbb{R}$$。則$$\forall x \in \mathbb{R}, ~\forall \epsilon >0 ,  \mathrm{P}(|F_n(x) - F(x)| < \epsilon) \geq 1 - \frac{1}{4n\epsilon^2}$$

因此當$$n \rightarrow \infty$$，可得$$\forall \epsilon >0, \lim_{n \rightarrow \infty} \mathrm{P}(|F_n - F| < \epsilon ) = 1$$。

### 弱大數法則

令$$X_1, X_2, \dots$$為獨立同分佈的隨機變數，且$$\mathrm{E}(X) =\mu$$​存在，則樣本平均$$\overline{X}_n$$機率收斂至$$\mu$$。

假設變異數$$Var(X)=\sigma^2$$存在，因為$$\mathrm{E}(\overline{X}_n)=\mu$$，$$\mathrm{Var}(\overline{X}_n)=\frac{\sigma^2}{n}$$，由柴比雪夫不等式得$$n \rightarrow \infty$$時，$$\forall \epsilon >0, \mathrm{P}(|\overline{X}_n - \mu| \geq \epsilon ) \leq \frac{\mathrm{Var}(\overline{X}_n)}{\epsilon^2} = \frac{\sigma^2}{n \epsilon^2} \rightarrow 0$$。

條件可再弱化，不必為獨立的隨機變數仍成立。

## L-P收斂(L-p convergence)

> $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(|X_n -X|^p)=0, ~p\geq 1$$

### 依均值收斂(convergence in mean)

> $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(| X_n -X|^2)=0$$

為L-P收斂，$$p=2$$的特例。可以理解為兩個隨機變量的距離隨著$$n$$趨向於無窮而變為0。

直觀上而言，均方收斂在乎的也是隨機變量的值，但其要求比依機率收斂更加嚴格。因為機率測度可以被均方測度所限制。

均方收斂可以推出依機率收斂，但是相反不成立。當然，如果加上一定的可積條件的話，依機率收斂可以推出均方收斂。

## 幾乎確定收斂(almost sure convergence)

> $$\displaystyle \mathrm{P}(\lim_{n \rightarrow \infty}X_n = X)=1$$

設$$E$$ 為一事件，如果 $$P (E) = 1$$，則稱 E "happen almost surely" (a.s.)。

* 而幾乎確定(almost sure)的意思是，當$$n$$趨向於無窮，$$X_n$$<mark style="color:red;">不收斂到</mark>$$X$$<mark style="color:red;">的事件集合機率為0</mark>。收斂機率等於1不像點態收斂(處處收斂)那麼嚴格，個別點不收斂(機率為0)不影響機率等於1的事件。
* a.s.收斂可以推出依機率收斂。
* 直觀上而言，幾乎處處收斂在乎的也是隨機變量的值，但其要求也比依機率收斂更加嚴格。

## 測度收斂(convergence in measure)



## 參考資料

* [\[知乎\] 通俗理解依機率收斂、有效性、無偏性和一致性](https://zhuanlan.zhihu.com/p/66658725)。
