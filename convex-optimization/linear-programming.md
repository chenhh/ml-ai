---
description: linear programming
---

# 線性規劃

## 什麼是線性規劃?

目標函數(ojective function)為線性函數，且限制式由線性函數組成的規劃問題。

由凸最佳化問題可得多個線性限制式的可行解區域(feasible domain)會形成單純形(simplex)，為一凸集合或是無解。

由於可行解空間為單純形(凸集合)，且是由線性限制式形成，而目標函數為線性函數，因此最佳值必落在單純形的某一個交點上。

### 歷史

G.B. Danzig(1947)年提出線性規劃的概念，用於美國空軍的後勤規劃。

由T.C. Koopmans與G.B. Danzig(1948)將此概念命名為線性規劃。

G.B. Danzig(1948)提出單純形法(simplex method)求解。最糟情形下求解為指數時間的算法，但在大多數問題上可快速求解。

LH：Khachian(1979)年提出橢圓形法(ellipsiod method)求解，為線性規劃的第一個多項式時間求解決演算法，但實作複雜度仍高。

N. Karmarkar(1984)提出內點法(interior-point method)求解，是容易實作且為多項式時間的求解演算法。



### 範例

$$\displaystyle  \begin{aligned} \min_{x_1, x_2}~ &~ x_1 - 2 x_2 \\ \text{s.t.} ~&~ x_1 + x_2 \leq 40 \\     & 2 x_1 + x_2 \leq 60 \\     & x_1, ~ x_2 \geq 0 \end{aligned}$$

<figure><img src="../.gitbook/assets/feasible_domain-min.png" alt=""><figcaption><p>線性規劃可行域為單純形，且最佳解落在某一個交點</p></figcaption></figure>

## 線性規劃標準型

### 目標函數

#### 多項式型

$$\displaystyle \min_{x_1, x_2, \dots, x_n} c_1 x_1 + c_2 x_2 + \dots + c_n x_n$$

#### 矩陣型

$$\displaystyle \min_{\mathbf{x}} \mathbf{c^\top x}$$

### 限制式

#### 多項式型

$$\displaystyle  \begin{aligned} & a_{11}x_1 + a_{12}x_2 + \dots + a_{1n} x_n  &= b_1 \\ & a_{21}x_1 + a_{22}x_2 + \dots + a_{1n} x_n  &= b_2 \\ & \vdots  & \vdots \\ & a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn} x_n  &= b_m \\ & x_1, x_2, \dots, x_n & \geq 0 \end{aligned}$$

如果決策變數$$y_j \leq 0$$，只要令$$x_j = -y_j \geq 0$$或者改變限制式中與$$y_j$$有限的系數正負號即可。

如果限制式$$\leq 0$$或$$\geq 0$$時，可增加鬆弛變數(slack variables)使得限制式$$=0$$，同時也要將鬆弛變數加入目標函數中。

#### 矩陣式

$$\displaystyle  \begin{aligned} & \mathbf{Ax = b} \\ & \mathbf{x \succeq 0} \end{aligned}$$



## 參考資料

* \[陽明交通大學] 方述誠-線性規劃。
