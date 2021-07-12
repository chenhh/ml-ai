# Lagrange內插法\(interpolation formula\)

##  Lagrange多項式

> $$t_0, t_1,\dots, t_N \in F$$為$$N+1$$個相異元素，定義：$$\displaystyle f_i(x)=-\frac{(x-t_0)\cdots (x-t_{i-1})(x-t_{i+1})\cdots (x-t_N)}{(t_i-t_0) \cdots (t_i-t_{i-1})(t_i-t_{i+1})\cdot (t_i-t_N) } = \prod_{j=0, j\neq i}^N \frac{x-t_j}{t_j - t_i}$$$$f_0, f_1, \dots, f_N \in F_N[x]$$（$$N$$階多項式向量空間）。

範例：$$5, -7, -6, 0$$的Lagrange多項式

* $$f_0(x)=\frac{(x+7)(x+6)(x-0)}{(5+7)(5+6)(5-0)}$$
* $$f_1(x)=\frac{(x-5)(x+6)(x-0)}{(-7-5)(-7+6)(-7-0)}$$
* $$f_2(x)=\frac{(x-5)(x+7)(x-0)}{(-6-5)(-6+7)(-6-0)}$$
* $$f_3(x)=\frac{(x-5)(x+7)(x+6)}{(0-5)(0+7)(0+6)}$$

