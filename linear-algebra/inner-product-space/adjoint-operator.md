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

