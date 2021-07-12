# 伴隨算子\(adjoint operator\)

##  伴隨算子\(adjoint operator\)

> 內積空間$$V$$定義在體$$F$$上，線性轉換$$T \in L(V,V)$$。
>
> 若存在線性轉換$$T^{*} : V \rightarrow V$$滿足$$\langle T(x), y \rangle = \langle x, T^{*}(y) \rangle, ~\forall x,y \in V$$，則稱$$T^{*}$$為$$T$$的伴隨算子（存在且唯一）。
>
> 也可表示為$$\langle x, T(y) \rangle= \langle T^{*}(x), y\rangle, ~\forall x,y \in V$$。
>
> * 此為Hermetian \(transpose\) matrix線性映射的版本。
> * 伴隨算子必定存在且唯一。
> * 內積算子必須滿足$$\langle x, y \rangle = \overline{\langle y,x \rangle}$$

* 若給定向量空間的基底$$B$$，且令$$A=[T]_B$$，則$$\langle [T]_B(x), y\rangle=\langle Ax, y\rangle=y^\mathrm{H} (Ax) =\overline{ x^\mathrm{H} (A^\mathrm{H}y)} = \langle A^\mathrm{H}y, x \rangle$$。

### 給定內積與單一向量時，另一向量的存在性與唯一性

> 內積空間$$V$$定義在體$$F$$上，線性泛函:$$f: V \rightarrow F$$，則存在唯一$$v \in V \ni f(u) = \langle u, v \rangle, \forall u \in V$$。（給定向量$$u$$，且$$f(u)$$之值已經知道時，則$$v \in V$$存在且唯一。）
>
> 如果$$v$$為單範正交基底中的元素，即$$\|v\|=1$$，則$$f(u)$$為將向量$$u$$投影到此基底元素的係數，$$f(u) = a = \frac{\langle u, v \rangle}{\langle v, v \rangle} = \langle u, v \rangle$$。

Proof:

* 令$$B=\{v_1,\dots,v_N \}$$為$$V$$的一組單範正交基底，取$$v=\sum_{i=1}^N \overline{f(v_i)}v_i$$
* 定義$$ g:V \rightarrow F, ~g(u)=\langle u,v \rangle,  \forall u \in V$$。
* 所以$$j=1,2,\dots,N, g(v_j )=\langle v_j,v\rangle=\langle v_j,\sum_{i=1}^N \overline{f(v_i) }v_i\rangle=\sum_{i=1}^N f(v_i )\langle v_j,v_i \rangle =\sum_{i=1}^N f(v_i )  \delta_{ij}=f(v_j )$$
* 因此可得$$g=f$$，證明了存在性。
* 若$$\exists v^′ \in V \ni f(u)=\langle u,v^′\rangle, \forall u \in V$$
* 可得$$\langle u,v\rangle= \langle u,v^′\rangle ,~ \forall u \in V$$
* 所以$$\langle v,u \rangle=\langle v^′,u\rangle ,~\forall u \in V$$
* 因此$$v=v^′$$，證明了唯一性 \(QED\)



