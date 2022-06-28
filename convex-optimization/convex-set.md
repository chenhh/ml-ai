# 凸集合 (convex set)

## 凸集合(convex set)

> definition: convex set
>
> $$C$$ is convex set if $$\forall x_1, x_2 \in C, \lambda \in [0,1] \Rightarrow \lambda x_1 + (1-\lambda) x_2 \in C$$.

* $$\lambda x_1 + (1-\lambda) x_2,\ \lambda \in [0,1]$$ 為端點 $$x_1, x_2$$形成的線段。
* 由定義可知向量空間必為凸集合，因為向量空間$$V$$必須滿足$$\forall a \in F$$, $$\forall u,v \in V \Rightarrow au+v \in V$$。
* <mark style="color:red;">註：如果是在平面上的集合，任意兩點間畫一直線均落在集合內時，則為凸集合</mark>。

![凸集合與非凸集合](../.gitbook/assets/convex\_set-min.png)

有些集合在相異參數時為凸集合或非凸集合。如 $$C_p = \{ (x,y)\ \vert \ (|x|^p + |y|^p)^{1/p} \leq 1 \}$$。在 $$p < 1$$時為不是凸集合。而在$$p \geq 1$$時為凸集合。

![參數可調整為凸集合或非凸集合](../.gitbook/assets/param\_convex\_set-min.png)

## 仿射集合(affine set)

> definition: affine set
>
> $$C$$ is affine set if $$C = \{ \lambda x_1 + (1-\lambda) x_2 , \forall \lambda \in \mathbb{R}, \forall x_1, x_2 \in X \}$$.

$$\lambda \in \mathbb{R}$$時， $$\lambda x_1 + (1-\lambda) x_2$$為由點 $$x_1, x_2$$形成的直線，而非線段。因此 $$C$$ 為集合$$X$$中任意兩點的直線集合。

* 例：線性方程式的解集合 $$\{\mathbf{x}\ \vert \ \mathbf{Ax = b} \}$$。
* 例：歐式空間$$\mathbb{R}^3$$中的平面以及空集合$$\phi$$。

凸集是在仿射集的定義中，對$$\lambda$$的範圍進行了限定，導致的結果是:<mark style="color:red;">仿射集要求的是集合中經過任意兩點的</mark><mark style="color:red;background-color:red;">**直線**</mark><mark style="color:red;">上的任意點都在集合中</mark>；而，<mark style="color:red;">凸集只是要求連接任意集合中兩點的</mark><mark style="color:red;background-color:red;">線段</mark><mark style="color:red;">上的點在集合中</mark>；所以對凸集定義比仿射集的定義更加苛刻，但是條件更加的苛刻不等於就是子集，不等於他們就是同一類。

仿射集要求集合當中任意兩點的係數和為1的線性組合（即過任意兩點的直線上的點）仍在集合中，凸集在仿射集的要求上增加了一個“係數非負”的條件，幾何直觀來說是任意兩點連成線段上的點仍在集合中，增加的這個條件反而降低了要求，不需要任意係數和為1的線性組合仍在集合內、而是只有係數非負而係數和為1的線性組合在集合內就可以。

### 仿射集合與向量空間中的生成集合(spanning set)的關係

> definition: spanning set S
>
> * $$span(S) = \{\mathbf{v} \ \vert \ \mathbf{v} \text{ is a linear combination of set } S\}$$.&#x20;
> * i.e. $$\forall \mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_n \in V$$, $$\lambda_1, \lambda_2, \cdots, \lambda_n \in F$$, $$\mathbf{v} = \sum_{i=1}^n \lambda_i \mathbf{v}_i$$.

向量空間$$V$$的子空間$$S$$為滿足線性組合封閉性的空間, 即 $$\forall \lambda_1, \lambda_2 \in F, u,v \in S, \lambda_1 u + \lambda_2 v \in S$$. 而$$S$$為子空間的必要條件是：

* $$\mathbf{0} \in S$$ (只要取線性組合的權重均為0即可得出。即 $$\lambda_1=\lambda_2=\cdots=\lambda_n = 0$$)
* 若 $$\mathbf{v} \in S$$，則 $$\mathbf{-v} \in S$$&#x20;

因此仿射空間為子空間的平移(translation)，而任意子空間必定為仿射空間。



## 參考資料

* Boyd, Stephen, Stephen P. Boyd, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004. \[[website](https://web.stanford.edu/\~boyd/cvxbook/)]
  * [\[Stanford\] EE364a: Convex Optimization I](https://web.stanford.edu/class/ee364a/)
  * [\[Stanford\] EE364b - Convex Optimization II](https://web.stanford.edu/class/ee364b/)
* [\[MIT\] Dimitri Bertsekas](https://www.mit.edu/\~dimitrib/home.html)
* Nesterov, Yurii. Introductory lectures on convex optimization: A basic course. Vol. 87. Springer Science & Business Media, 2003.
