# 開集合

## 開集合\(open set\)

> $$(X,d)$$為度量空間，稱集合$$S \subseteq X$$為開集合，若所有在集合$$S$$內的點均為其內點，即
>
> * $$a∈S$$為內點，則$$\exists r>0 \ni N_r (a) \subset S $$
> * $$S$$為開集合，則 $$\forall a \in S, a \in int(S)$$

如果$$S$$不為開集合，則 $$\exists a \in S \ni \forall r > 0, N_r(a) \not \subset S$$

### 邊界點非開集合中的元素

* 若$$a$$為集合$$S$$的邊界點（$$a \in \partial(S)$$），則$$\forall r > 0 ~ N_r(a) \cap S \neq \emptyset ~\land ~N_r(a) \cap S^c \neq \emptyset$$。
* 因此$$a$$不為$$S$$的內點，所以不是開集合內的元素 \(QED\)

### 鄰域為開集合

> •$$(X,d)$$為度量空間, 給定$$x \in X$$，則$$N_r (x)=\{y \in X, d(x,y)<r \}$$為開集合。

* 令$$y \in N_r(x)$$，則$$d(x,y) < r$$
* 令$$h=r-d(x,y) > 0 $$，取$$p\in X, d(y,p)<h$$
* 可得 $$d(x,p) \leq d(x,y)+d(y,p) < d(x,y)+r -d(x,y) <r$$
* 因此$$p \in X$$為內點，所以$$N_r(x)$$為開集合 \(QED\)









