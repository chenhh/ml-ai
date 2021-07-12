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

###  存在性與唯一性

> 內積空間$$V$$定義在體$$F$$上，線性泛函:$$f: V \rightarrow F$$，則存在唯一$$v \in V \ni f(u) = \langle u, v \rangle, \forall u \in V$$。（給定向量$$u$$，且$$f(u)$$之值已經時，則$$v \in V$$存在且唯一。）
>
> 如果$$v$$為單範正交基底中的元素，即$$\|v\|=1$$，則$$f(u)$$為將向量$$u$$投影到此基底元素的系數，$$f(u) = a = \frac{\langle u, v \rangle}{\langle v, v \rangle} = \langle u, v \rangle$$

