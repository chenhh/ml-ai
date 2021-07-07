# Gram-schmidt正交化

Gram-schmidt正交化的功能是將一個任意集合轉換成正交集合（所有元素彼此正交）。

## 正交基底的係數\(Fourier coefficient\)

> 內積空間$$V$$定義在體$$F$$，$$S=\{v_1, \dots, v_K\} \subseteq V$$為不含$$0$$向量的正交集（線性獨立集）。
>
> 若$$v=span(S)$$，令$$v=\sum_{i=1}^K c_i v_i$$，則係數$$c_j=\frac{\langle v, v_j \rangle}{\langle v_j, v_j\rangle}=\frac{\langle v, v_j \rangle}{\|v_j\|^2}, ~j=1,2,\dots, K$$。
>
> 註：Fourier級數是此方法求各基底或生成集的係數，所以上述方法得出的參數稱Fourier coefficient。
>
> 如果$$S$$為單範正交集時，因為$$\|v_j\|=1$$，所以$$c_j=\langle v, v_j \rangle$$。

proof:

* $$\langle v, v_j\rangle=\langle \sum_{i=1}^K c_i v_i, v_j\rangle = \sum_{i=1}^K c_i \langle v_i, v_j \rangle=c_j \langle v_j, v_j  \rangle$$
* 所以$$c_j=\frac{\langle v, v_j \rangle}{\langle v_j, v_j\rangle}=\frac{\langle v, v_j \rangle}{\|v_j\|^2}$$ \(QED\)

