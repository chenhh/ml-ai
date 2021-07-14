# 雙線性型式\(bilinear form\)

## 雙線性\(函數\)型式

> $$V$$為定義在體$$F$$的向量空間，函數$$f: V \times V \rightarrow F$$滿足$$\forall x,y,z \in V, a,b \in F$$：
>
> * $$f(ax+by,z)=af(x,z)+bf(y,z)$$
> * $$f(x,ay+bz)=af(x,y)+b(x,z)$$
>
> 則稱$$f$$為$$V$$上的雙線性函數。令$$B(V)$$為$$V$$上所有雙線性函數所形成的集合。
>
> 此為雙變數函數$$f(x,y)$$的線性算子形式。

* 例如$$A\in F^{N \times N}, V=F^{N \times 1}$$，定義$$f(x,y)=y^{\top}Ax$$或$$f(x,y)=x^{\top}Ax \in B(V), \forall x, y \in V$$

### 雙線性函數形成向量空間

> 雙線性函數$$f \in B(V)$$，則$$f(x, 0)=(0,x)=0, \forall x \in V$$。
>
> 定義$$B(V)$$上的加法與純量積為：
>
> * $$\forall f_1, f_2 \in B(V), (f_1+f_2)(x,y)=f_1(x,y)+f_2(x,y)$$
> * $$\forall f \in B(V), c \in F, ~(cf)(x,y) = cf(x,y)$$
>
> 則$$B(V)$$滿足向量空間的定義（包含0向量與任意線性組合的所有元素）。

### Sesqui型式

> $$V$$為定義在體$$F$$的向量空間，函數$$f: V \times V \rightarrow F$$滿足$$\forall x,y,z \in V, a,b \in F$$：
>
> * $$f(ax+by, z)=af(x,z)+bf(y,z)$$
> * $$f(x, ay+bz)=\overline{a}f(x,y)+\overline{b}f(x,z)$$
>
> 則稱$$f$$為$$V$$上的sesqui型式，或是簡稱為型式。令$$F(V)$$為$$V$$上所有sesqui型式函數所成的集合。

> 同雙線性型式定義加法與純量積，則$$F(V)$$也為向量空間（包含0向量與任意線性組合的所有元素）。

* 當$$F=\mathbb{R}$$時，雙線性型式等於Sesqui型式。
* 當$$F = \mathbb{C}$$時，$$B(V) \cap F(V) = \{0\}$$

  * 若$$ f \in B(V) \cap F(V)$$
  * 則$$f(x,y)=f(x, i(−i)y)=i(x,(−i)y)$$\[因為$$f \in β(V)]=i^2 f(x,y)$$\[因為$$f \in F(V)]=−f(x,y)    $$
  * 可得$$f(x,y)=−f(x,y)$$，所以$$f(x,y)=0,  \forall x,y \in V$$。

#### 範例

*  $$A \in \mathbb{C}^{N \times N}, V=\mathbb{C}^{N \times 1}$$，定義$$ f:V \times V \rightarrow F$$，$$ f(x,y)=y^\mathrm{H} Ax,~ \forall x,y \in V$$，則$$f(x,y) \in F(V)$$。

  * $$\forall a,b \in F, x,y \in V$$
  * $$f(ax+by,z)=z^\mathrm{H} A(ax+by)=az^\mathrm{H} Ax+bz^\mathrm{H} Ay=af(x,z)+bf(y,z)    $$
  * $$ f(x,ay+bz)=(ay+bz)^\mathrm{H} Ax＝（\overline{a}y^\mathrm{H}+\overline{b}z^\mathrm{H} ）Ax=\overline{a}y^\mathrm{H} Ax+\overline{b}z^\mathrm{H} Ax=\overline{a} f(x,y)+ \overline{b} f(x,z)    $$
  * 所以$$f \in F(V)    $$

### Sesqui型式函數與線性轉換的對應關係

> $$V$$為定義在體$$F$$的內積空間，$$f \in F(V)$$為Sesqui型式，則唯一存在線性轉換$$T \in L(V,V)$$使得$$f(x,y)=\langle T(x), y \rangle~ \forall x,y \in V$$

Proof:

* $$\forall v \in V$$，定義$$g(u)=f(u,v), ~\forall u \in V$$，則$$g$$為線性函數。
* 因此得唯一存在$$v^′ \in V \ni g(u)=\langle u,v^′\rangle, ~\forall u \in V$$
*  定義 $$U:V \rightarrow V, ~U(v)=v^{′}$$
* 所以$$f(u, av_1+bv_2 )=\langle u, U(av_1+bv_2 ) \rangle, ~\forall a,b \in F, u,v_1,v_2 \in V$$
* 而且 $$f(u, av_1+bv_2 )=\overline{a} f(u,v_1 )+\overline{b} f(u,v_2 )=\overline{a} \langle u, U(v_1) \rangle +\overline{b} \langle u,U(v_2) \rangle= \langle u, aU(v_1 )+bU(v_2 ) \rangle$$
* 所以$$\langle u, U(av_1+bv_2 )\rangle=\langle u, aU(v_1 )+bU(v_2 )\rangle$$
* 可得$$U(av_1+bv_2 )=aU(v_1 )+bU(v_2 )$$，因此$$U$$為線性。
* 取$$T=U^{*}$$ \($$U$$的伴隨算子\)，則$$f(u,v)=\langle u, U(v) \rangle=\langle U^{*} (u),v \rangle=\langle T(u),v \rangle, \forall u,v \in V$$，因此$$T$$存在。
*  唯一性
* 若存在$$T^{′} \in L(V,V)\ni f(u,v)=\langle T^{'} (u),v\rangle, \forall u,v \in V$$
* 可得$$\langle T(u),v \rangle= \langle T^{′}(u),v \rangle, ~\forall u,v \in V$$
* 所以$$\langle T(u)−T^{′} (u),v \rangle=0$$
* 因此$$T(u)−T^{′} (u)=0$$
* 所以$$T(u)=T^{′} (u), ~\forall u\in V$$
* 即$$T=T^{′}$$，所以$$T$$唯一。 \(QED\)



