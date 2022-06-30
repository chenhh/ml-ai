# 凸函數 (convex function)

## 凸函數

> 給定函數$$f:\mathbb{R}^n \rightarrow \mathbb{R}$$，
>
> * 若其定義域$$\mathrm{dom}f$$為凸集合，且$$f(\lambda x + (1-\lambda)y) \leq \lambda f(x)+(1-\lambda )f(y)$$，$$\forall x, y \in \mathrm{dom} f, ~ 0 \leq \lambda \leq 1$$，則稱$$f$$為凸函數(開口向上)。
> * 若滿足$$f(\lambda x + (1-\lambda)y) < \lambda f(x)+(1-\lambda )f(y)$$，$$\forall x, y \in \mathrm{dom} f, ~ x\neq y, ~ 0 < \lambda < 1$$，稱為嚴格凸函數(strictly convex function)。

* 若$$f$$為凸函數(開口向上)，則$$-f$$為凹函數(concave function)(開口向下)。

### 常見凸函數

#### 定義域在實數的凸函數

* affine: $$f(x)=ax+b, ~\forall x,a, b\in \mathbb{R}$$
* exponential: $$f(x)=e^{ax}, \forall a \in \mathbb{R}$$
* powers: $$f(x)=x^{\alpha}, x \in \mathbb{R}_{++}~\forall \alpha \geq 1 \text{ or } \alpha \leq 0$$
* power of absolute value: $$f(x)=|x|^p, x \in \mathbb{R}, ~ p \geq 1$$
* negative entropy: $$f(x) = x \log x, ~ x \in \mathbb{R}_{++}$$

#### 定義域在實數的凹函數

* affine: $$f(x)=ax+b, ~\forall x,a, b\in \mathbb{R}$$(只有直線可同時為凸與凹函數)
* powers: $$f(x)=x^\alpha, x \in \mathbb{R}_{++}, ~ 0 \leq \alpha \leq 1$$
* logarithm: $$f(x) = \log x, ~ x \in \mathbb{R}_{++}$$

#### 定義域為向量

* affine同時為凸函數與凹函數：$$\mathrm{dom}f \in \mathbb{R}^n$$, $$f(x)= a^\top x + b$$。
* norm均為凸函數 $$\displaystyle \|x\|_p = (\sum_{i=1}^p |x_i|^p)^{1/p} ~ \forall p \geq 1$$，且$$\|x\|_{\infty} = \max_{k} |x_k|$$。

#### 定義域為矩陣

* affine同時為凸函數與凹函數: $$\mathrm{dom}f \in \mathbb{R}^{m\times n}$$, $$\displaystyle f(X) = tr(A^\top X) +b = \sum_{i=1}^m \sum_{j=1}^n A_{ij} X_{ij} + b$$。
* spectral norm(max singular value)為凸函數: $$f(X) = \|X\|_2 = \sigma_{\max}(X) = (\lambda_{\max}(X^\top X))^{1/2}$$。

### 將函數轉換單變數函數判斷是否為凸函數

> $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$為凸函數 若且唯若 函數$$g: \mathbb{R} \rightarrow \mathbb{R}$$, $$g(t)=f(x+tv), ~ \mathrm{dom}g=\{t|x+tv \in \mathrm{dom} f \}$$為凸函數，
>
> $$\forall x \in \mathrm{dom}f, ~ v \in \mathbb{R}^n$$

簡單的說，如果$$f$$為凸函數，則給定$$x \in \mathrm{dom}f$$，不論往任何方向$$v$$移動，只要終點$$x+tv$$仍然在定義域內，則仍然滿足凸函數的條件，反之也成立。

範例：

* $$f: \mathbf{S}^n \rightarrow \mathbb{R}$$, $$f(X) = \log \det X$$, $$\mathrm{dom}f=\mathbf{S}_{++}^n$$
* 令$$\begin{aligned} g(t) & =\log\det(X+tV) \\     & = \log\det X + \log\det(I+tX^{-1/2}VX^{-1/2}) \\     & = \log\det X + \sum_{i=1}^n \log(1+t \lambda_i) \end{aligned}$$
* $$\lambda_i$$為$$X^{-1/2}VX^{-1/2}$$的特徵根。
* 可得$$g$$為凹函數($$\forall X \succ 0, \forall V$$), 因此$$f$$為凹函數。

## 擴展值延伸(extended-value extension)

可定義凸(凹)函數在定義域外的值為$$\infty$$($$-\infty$$)，將凸函數延伸到整個空間$$\mathbb{R}^n$$，<mark style="color:blue;">可簡化定義域的描述</mark>。

令$$\tilde{f}: \mathbb{R}^n \rightarrow \mathbb{R} \cup \{ \infty \}$$為凸函數$$f$$的擴展值延伸如下：$$\tilde{f} =  \left\{ \begin{aligned} f(x), ~& ~x \in \mathrm{dom} f \\ \infty, ~ & ~ x \not \in \mathrm{dom} f \end{aligned} \right.$$

因此$$\forall 0 \leq \lambda  \leq 1$$，$$\tilde{f}(\lambda x + (1-\lambda)y) \leq \lambda \tilde{f}(x) + (1-\lambda)\tilde{f}(y)$$，等同滿足了以下兩個條件：

* $$\mathrm{dom}f$$為凸集合(因為$$\mathrm{dom}\tilde{f} = \mathbb{R}^n$$)
* $${f}(\lambda x + (1-\lambda)y) \leq \lambda {f}(x) + (1-\lambda){f}(y)$$

例：令$$f_1, f_2: \mathbb{R}^n \rightarrow \mathbb{R}$$為凸函數，則逐點和函數$$f=f_1 + f_2$$的定義域為$$\mathrm{dom}f = \mathrm{dom}f_1 \cap \mathrm{dom}f_2$$。可簡寫為 $$\forall x \in \mathrm{dom}f$$，$$\tilde{f}=\tilde{f}_1 + \tilde{f}_2$$。因為當$$x \notin \mathrm{dom} f_1$$或$$x \notin \mathrm{dom} f_2$$時，$$\tilde{f}(x)=\infty$$仍然成立。

### 凸集合的示性函數(indicator function of a convex set)
