# 隨機變數的收斂

## 簡介

隨機變數的收斂\(convergence of random variable\)被稱為隨機收斂，表示一系列本質上隨機不可預測的事件所發生的模式可以在樣本數量足夠大的時候得到合理可靠的預測。各種不同的收斂定義實際上是表示預測時不同的刻畫方式。

## 分佈收斂\(convergence in distribution\)

> $$\displaystyle \lim_{ n \rightarrow \infty}F_n(x) = F(x)$$

依分佈收斂是個完全不同的概念。依分佈收斂是一個分佈函數收斂的概念。所以$$X_n$$與$$X$$甚至都可以不被定義在同一個機率空間之內。

## 機率收斂\(convergence in probability\)

> $$\displaystyle \lim_{n \rightarrow \infty}\mathrm{P}(\| X_n -X\|>\epsilon) = 0$$

機率收斂的意思是，當$$n$$趨向無窮，$$X_n$$與$$X$$之間不相等的部分機率趨向於0（即$$X_n$$與$$X$$仍然可能不相等，但次數少到可以忽略）。

## L-P收斂\(L-p convergence\)

## 依均值收斂\(convergence in mean\)

> $$\displaystyle \lim_{n \rightarrow \infty} \mathrm{E}(| X_n -X|^2)=0$$

可以理解為兩個隨機變量的距離隨著$$n$$趨向於無窮而變為0。均方收斂可以推出依機率收斂，但是相反不成立。當然，如果加上一定的可積條件的話，依機率收斂可以推出均方收斂。

## 幾乎確定收斂\(機率1收斂\)\(almost sure convergence\)

> $$\displaystyle \mathrm{P}(\lim_{n \rightarrow \infty}X_n = X)=1$$

而幾乎確定\(almost sure\)的意思是，當$$n$$趨向於無窮，$$X_n$$不收斂到$$X$$的機率為0。a.s.收斂可以推出依機率收斂。

## 測度收斂\(convergence in measure\)



