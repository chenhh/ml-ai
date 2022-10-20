# 摺積(convolution)

## 簡介

摺積（疊積、褶積或旋積），是透過兩個函數$$f$$ 和$$g$$ 生成第三個函式的一種數學運算元，表徵函數$$f$$ 與經過翻轉和平移的$$g$$ 的乘積函數所圍成的曲邊梯形的面積。如果將參加摺積的一個函式看作區間的指示函式，摺積還可以被看作是「滑動平均」的推廣。

### 摺積定義

> 令 $${\displaystyle f,g}$$是定義在 $${\displaystyle \mathbb {R} ^{n}}$$上的可測函數(measurable function)。定義摺積$$\displaystyle h(t)\equiv (f*g)(t) \equiv \int_{\mathbb{R}^n} f(\tau) g(t-\tau) d \tau$$

在實數$$\mathbb{R}$$，可證明幾乎所有$$t \in (-\infty, \infty)$$的積分均存在。

交換性：$$\displaystyle  (f*g)(t) = (g*f)(t)$$

#### 摺積圖解

1. 給定兩函數$$f(\tau), ~g(\tau)$$。
2. 將$$g(\tau)$$向左移動$$t$$單位得$$g(\tau+t)$$，再將該函數以縱軸映射得$$g(t-\tau)$$。
3. 讓變數$$t$$由$$-\infty$$變動到$$+\infty$$，當$$g(t-\tau)$$與$$f(\tau)$$兩函數有相交時，計算兩函數的乘積的積分值。即計算一個滑動的加權總和。
4. 因此$$(f*g)(t)$$為給定$$t$$時的，兩函數$$f(\tau)$$與$$g(t-\tau)$$乘積的積分值(如果兩函數不相交，則積分為0)。
