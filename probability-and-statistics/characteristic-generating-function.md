# 特徵生成函數(characteristic generating function)

## 簡介

特徵函數是機率論中描述隨機變數的分佈特性。它通過傅立葉變換的形式，將隨機變數的分佈編碼到一個複數函式中，從而方便進行分析和計算。

1. **唯一性** ： 如果兩個隨機變數的特徵函式相同，則它們的分佈也相同。這意味著特徵函式可以唯一地確定一個隨機變數的分佈。
2. **總是存在** ： 不同於動差生成函式（MGF），特徵函式對於所有隨機變數都存在，因為 $$e^{itX}$$，積分或求和總是收斂的。
3. **計算動差（Moments）** ： 特徵函式可以用來計算隨機變數的各階動差。
4. **獨立隨機變數的加法性**
5. <mark style="color:red;">**與傅立葉變換的關係**</mark> <mark style="color:red;"></mark><mark style="color:red;">： 特徵函式本質上是機率密度函式的傅立葉變換（Fourier Transform）。因此，它可以看作是一種頻域表示</mark>。

| 形式  | $$\mathrm{E}[e^{itX}]$$ | $$\mathrm{E}[e^{tX}]$$ |
| --- | ----------------------- | ---------------------- |
| 存在性 | 對所有機率分佈都存在              | 並非總是存在                 |
| 實用面 | 更適合極限定理、傅立葉分析           | 更直觀用於求期望與矩             |
| 值域  | 複數值                     | 實數值                    |

## 特徵函數(characterisic function)

<mark style="color:red;">任何隨機變數的特徵函數(c.f.)必定存在且唯一</mark>。

$$\phi_X(t)=\mathrm{E}(e^{itX}), ~ t \in \mathbb{R}$$

* 連續型：$$\displaystyle\phi_X(t)= \mathrm{E}(e^{itX})=\int_{-\infty}^\infty e^{itx} dF_X(x)$$，$$F_X(x)$$為(累積)分佈函數。
* 離散型：$$\displaystyle\phi_X(t)= \mathrm{E}(e^{itX})=\sum_{i} e^{itx_i} \mathrm{P}(X=x_i)$$

如果機率密度函數(pdf)$$f_X$$存在時，上式可改寫為：$$\displaystyle \mathrm{E}(e^{itX})=\int_{-\infty}^\infty e^{itx} f_X(x)dx$$。

$$e^{itX} = \cos(tX) + i \sin(tX)$$

$$\phi_X(0)=1$$，因為$$e^{i0X}=1$$。

$$\phi_{aX+b}(t)=e^{itb}\phi_X(at)$$

## 機率測度的特徵函數存在性

> 機率測度函數$$P : \Omega \to \mathbb{R}$$滿足以下三個條件：
>
> * $$\mathrm{P}(E) \geq 0, ~E \in \mathcal{F}$$。
> * $$\mathrm{P}(\Omega) = 1$$。
> * $$\mathrm{P}(\bigcup_{i \in \mathbb{N}} E_i ) =\sum_{i \in \mathbb{N}} \mathrm{P}(E_i), ~ E_i \cap E_j = \emptyset, ~ \forall i \neq j$$。
>
> 因為機率密度函數$$f \in L^1(\mathbb{R})$$，即$$\int_{-\infty}^{\infty}|f(x)|dx =1 < \infty$$(絕對收斂)，因此$$f$$的傅立葉轉換必定存在。

## 獨立隨機變數和的特徵函數

> 若$$X, Y$$是獨立的隨機變數，則它們的和$$X+Y$$的特徵函數為：
>
> $$\phi_{X+Y}(t)=\phi_X(t)\phi_Y(t)$$。

## 與動差生成函數的關係

$$\phi_X(t)=M_X(it)=\mathrm{E}(e^{itX})$$

因此，當 MGF 存在時，特徵函數可以通過簡單替換$$t \to it$$得到。

然而，特徵函數比 MGF 更通用，因為它總是存在，而 MGF 可能在某些情況下不存在（例如柯西分佈）。
