---
description: convergence in the mean
---

# 平均收斂

## 平均收斂

> 定義在集合$$E$$的可積分函數序列$$\{f_n\}$$滿足以下條件時，稱為Cauchy (sequence) in the mean。
>
> $$\displaystyle \lim_{n,m \rightarrow \infty} \int_E |f_n(x) - f_m(x)|dx=0$$。
>
> 若存在可積分函數$$f$$滿足以下條件時，稱$$\{f_n\}$$平均收斂至函數$$f$$。$$\displaystyle \lim_{n \rightarrow \infty} \int_E |f_n(x) - f(x)|dx = 0$$

### \[等價條件]Cauchy (sequence) in the mean若且唯若平均收斂

> 定義在集合$$E$$的可積分函數序列$$\{f_n\}$$與可積分函數$$f$$，則：
>
> $$\displaystyle \lim_{n,m \rightarrow \infty} \int_E |f_n(x) - f_m(x)|dx=0 \Leftrightarrow \lim_{n \rightarrow \infty} \int_E |f_n(x) - f(x)|dx=0$$

## 有限測度空間中，處處有限可測函數序列測度收斂至0若且唯若積分收斂至0

> 在有限測度空間$$m(X)< \infty$$中，處處有限可測函數序列$$\{f_n\}$$測度收斂至0若且唯若$$\displaystyle \lim_{n \rightarrow \infty}\int_X \frac{|f_n(x)|}{1+|f_n(x)|}dx=0$$。
