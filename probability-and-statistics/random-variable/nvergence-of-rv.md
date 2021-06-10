# 隨機變數的收斂

## 簡介

隨機變數的收斂\(convergence of random variable\)被稱為隨機收斂，表示一系列本質上隨機不可預測的事件所發生的模式可以在樣本數量足夠大的時候得到合理可靠的預測。各種不同的收斂定義實際上是表示預測時不同的刻畫方式。

## 分佈收斂\(convergence in distribution\)

> $$\displaystyle \lim_{ n \rightarrow \infty}F_n(x) = F(x)$$

依分佈收斂是個完全不同的概念。依分佈收斂是一個分佈函數收斂的概念。所以$$X_n$$與$$X$$甚至都可以不被定義在同一個機率空間之內。

* 當$$n$$很大的時候，$$X_n$$的累積分佈函數和$$X$$的累積分佈函數差不多。
* 直觀上而言，依分佈收斂只在乎隨機變量的分佈，而不在乎他們之間的相互關系。

## 機率收斂\(convergence in probability\)

> $$\displaystyle \lim_{n \rightarrow \infty}\mathrm{P}(\| X_n -X\|>\epsilon) = 0$$

機率收斂的意思是，當$$n$$趨向無窮，$$X_n$$與$$X$$之間不相等的部分機率趨向於0（對任意的結果$$\omega$$，$$|(X_n -X)(\omega) |$$很小\)。

和處處收斂的區別是，由於誤差的存在，$$X_n$$可能在某次結果出現偏離$$X$$的情況，只不過這種可能性或許會越來越小，但不能保證不發生。也就是不能保證$$X_n$$從哪一個時刻其永遠保持恆定狀態。

## L-P收斂\(L-p convergence\)

> $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(|X_n -X|^p)=0, ~p\geq 1$$

### 依均值收斂\(convergence in mean\)

> $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(| X_n -X|^2)=0$$

為L-P收斂，$$p=2$$的特例。可以理解為兩個隨機變量的距離隨著$$n$$趨向於無窮而變為0。

直觀上而言，均方收斂在乎的也是隨機變量的值，但其要求比依機率收斂更加嚴格。因為機率測度可以被均方測度所限制。

均方收斂可以推出依機率收斂，但是相反不成立。當然，如果加上一定的可積條件的話，依機率收斂可以推出均方收斂。

## 幾乎確定收斂\(almost sure convergence\)

> $$\displaystyle \mathrm{P}(\lim_{n \rightarrow \infty}X_n = X)=1$$

而幾乎確定\(almost sure\)的意思是，當$$n$$趨向於無窮，$$X_n$$不收斂到$$X$$的機率為0。a.s.收斂可以推出依機率收斂。

直觀上而言，幾乎處處收斂在乎的也是隨機變量的值，但其要求也比依機率收斂更加嚴格。

## 測度收斂\(convergence in measure\)



