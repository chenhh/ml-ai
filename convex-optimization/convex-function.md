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

* 令 $$C \subseteq \mathbb{R}^n$$為凸集合，定義函數$$I_C: C \rightarrow \mathbb{R}$$為$$I_c(x) = 0, ~\forall x \in C$$。
* 其擴展值延伸為$$\tilde{I}_c(x) = \left \{  \begin{aligned} 0, ~ & ~ x \in C \\ \infty ~ & ~ x \notin C \end{aligned}  \right.$$。

可利用示性函數變換問題的定義域。比如函數$$f: \mathbb{R}^n \rightarrow \mathbb{R}$$，求函數$$f$$在集合$$C$$的極小值。等價於在$$\mathbb{R}^n$$上求$$f+\tilde{I}_C(x)$$的極小值。

## <mark style="color:red;">一階條件(first-order condition)</mark>

若函數$$f$$的定義域$$\mathrm{dom}f$$為開集合，且$$\forall x \in \mathrm{dom}f$$，梯度$$\nabla f(x) = \left(  \frac{\partial f(x)}{\partial x_1}, \frac{\partial f(x)}{\partial x_2}, \dots, \frac{\partial f(x)}{\partial x_n}  \right)$$存在，則稱<mark style="color:red;">函數</mark>$$f$$<mark style="color:red;">可微(differentiable)</mark>。

### 一階條件是凸函數的充份必要條件

> 令 $$f$$可微分，則：
>
> $$f$$為凸函數$$\Leftrightarrow$$ $$\mathrm{dom}f$$為凸集合，且$$\forall x, y \in \mathrm{dom}f$$，$$f(y) \geq f(x) + \nabla f(x)^\top (y-x)$$

![一階條件](../.gitbook/assets/first\_order\_condition-min.png)

* 如果$$\nabla f(x)=0$$，則$$\forall y \in \mathrm{dom}f$$，均可得$$f(y) \geq f(x)$$，即$$x$$為$$f$$的全局極小點(global minimum)。
* 可以用<mark style="color:red;">點斜式</mark>表示過點$$x$$的切線，令$$y$$在切線的定義域上，因此$$f^{'}(x) = \frac{f(y) - f(x)}{y-x}$$，所以在直線上的$$f(y) = f(x) +  f^{'}(x)(y-x)$$。

proof => (簡化為一維的條件)

* 令$$f$$可微分且為凸函數，$$x, y \in \mathrm{dom}f$$。
* 因為$$\mathrm{dom}f$$為凸集合，對於$$0<t \leq 1$$，可得$$x+t(y-x) \in \mathrm{dom}f$$。
* 因為$$f$$為凸函數，可得 $$f(x+t(y-x)) \leq (1-t)f(x) + tf(y)$$。
* 兩邊同除t可得$$f(y) \geq f(x) + \frac{1}{t} f(x+t(y-x)) - f(x)$$。
* 當$$t \rightarrow 0$$時，可得$$f(y) \geq f(x) + \nabla f(x)^{'} (y-x)$$。(QED)

proof <=&#x20;

* 假設$$\forall x,y \in \mathrm{dom}f$$均滿足 $$f(y) \geq f(x) + \nabla f(x)^{'} (y-x)$$。
* 選$$x \neq y, ~0 \leq c \leq 1,  ~ z = cx + (1-c)y \in \mathrm{dom} f$$
* 由一階條件可得$$f(x) \geq f(z) + f^{'}(z)(x-z)$$且$$f(y) \geq f(z) + f^{'}(z)(y-z)$$。
* 兩不等式相加可得$$cf(x) + (1-c)f(y) \geq f(z)$$ (QED)

## 二階條件(second-order conditions)
