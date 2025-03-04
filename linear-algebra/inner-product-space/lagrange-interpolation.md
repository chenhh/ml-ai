# Lagrange內插法(interpolation formula)

## &#x20;Lagrange多項式

> $$t_0, t_1,\dots, t_N \in F$$為$$N+1$$個相異元素，定義：$$\displaystyle f_i(x)=-\frac{(x-t_0)\cdots (x-t_{i-1})(x-t_{i+1})\cdots (x-t_N)}{(t_i-t_0) \cdots (t_i-t_{i-1})(t_i-t_{i+1})\cdot (t_i-t_N) } = \prod_{j=0, j\neq i}^N \frac{x-t_j}{t_j - t_i}$$$$f_0, f_1, \dots, f_N \in F_N[x]$$（$$N$$階多項式向量空間）。

範例：$$5, -7, -6, 0$$的Lagrange多項式

* $$f_0(x)=\frac{(x+7)(x+6)(x-0)}{(5+7)(5+6)(5-0)}$$
* $$f_1(x)=\frac{(x-5)(x+6)(x-0)}{(-7-5)(-7+6)(-7-0)}$$
* $$f_2(x)=\frac{(x-5)(x+7)(x-0)}{(-6-5)(-6+7)(-6-0)}$$
* $$f_3(x)=\frac{(x-5)(x+7)(x+6)}{(0-5)(0+7)(0+6)}$$

### Lagrange多項式形成多項式空間的基底

> $$t_0,t_1 \dots ,t_N\in F$$為$$N+1$$個相異元素，$$f_0,f_1,\dots,f_N$$ 為Langrange多項式。則$$\{f_0,f_1,\dots,f_N \}$$為$$F_N [x]$$的基底> 。

Proof:

* 因為$$N$$階多項式空間$$\dim⁡(F_N [x])=N+1=|\{f_0,f_1,\dots,f_N \}|$$。
* 所以只須證明$$\{f_0,f_1,\dots,f_N \}$$為線性獨立集即可(因基底為最大個數的線性獨立集)  。
* 令$$\sum_{i=0}^N a_i f_i=0$$。
* 所以$$0=\sum_{i=0}^N a_i f_i (t_j ) =\sum_{i=0}^N a_i \delta_{ij}=c_j , ~\forall j=0,1,\dots,N$$ (QED).

### Lagrange's 內插法公式(interpolation formula)

> $$t_0,t_1,\dots,t_N \in F$$為$$N+1$$個相異元素> ，$$c_0,c_1,\dots ,c_N \in F$$，則> 唯一存在一多項式$$f∈F_N [x] \ni f(t_j )=c_j, ~ j=0,1,\dots,N$$。
>
> Lagrange內插公式告訴我們如何求一$$F_N [x]$$上的多項式其經過給定的$$N+1$$個點。>

