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
