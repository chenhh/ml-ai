# 內積空間\(inner product space\)

## 內積算子\(inner product operator\)

> 向量空間$$V$$定義在體$$F$$，定義內積函數$$\langle \cdot, \cdot \rangle:V \times V \rightarrow F$$滿足：
>
> 1. $$\forall u,v, w \in V$$，$$\langle u+v, w\rangle = \langle u, w\rangle + \langle v, w\rangle$$。
> 2. $$\forall u,v \in V, c \in F$$，$$\langle cu, v\rangle = c \langle u, v\rangle$$。
> 3. $$\forall u,v \in V$$，$$\langle u, v\rangle = \overline{\langle u, v \rangle}$$ （共軛交換性）
> 4. $$\forall v \in V, v \neq 0$$，$$\langle v, v \rangle > 0$$。
>
> 註：內積算子為向量間角度的擴充，可得$$\langle u, v \rangle = \|u \| \|v\| \cos \theta$$，其中$$\theta$$為兩向量$$u, v$$間的夾角，$$\|v\|$$為向量的範數（norm, 長度的擴充）。

* $$\forall v \in V, ~\langle v, \rangle =0 \Leftrightarrow v=0$$。
  * 由於$$\langle v, v \rangle = \| v\| \| v\| \cos \theta =0$$，且向量$$v$$與$$v$$之間的夾角為0，所以$$\cos \theta=1$$，因此$$v=0$$。
* $$\forall u, v, w \in V, a,b \in F, \langle u, av+bw\rangle= \overline{a}\langle u ,v\rangle+\overline{b}\langle u,w\rangle$$
  * $$\langle u, av+bw\rangle = \overline{\langle av + bw, u\rangle} = \overline{a\langle v, u\rangle + b \langle w, u\rangle} = \overline{a\langle v,u\rangle}+\overline{b\langle w, u\rangle}=\overline{a} \langle u,v \rangle+ \overline{b} \langle u, w\rangle$$

### 常見內積

* $$V=\mathbb{C}^{N \times N}$$，$$\forall A,B \in V$$，定義方陣的內積為$$\langle A, B\rangle=tr(AB^{\mathrm {H}})$$。
* $$V=C[a,b]$$為定義在閉區間$$[a,b]$$的所有連續函數，$$F=\mathbb{C}$$，則$$\forall f,g \in V$$，定義函數內積$$\langle f, g \rangle=\int_a^b f(x)\overline{g(x)}dx$$。
* $$V=F^{N \times 1}, F = \mathbb{C}$$，標準（行向量）內積$$\langle x,  y\rangle =y^{\mathrm{H}}x=x_1\overline{y_1} + \dots + x_N\overline{y_N}$$。

## 內積空間\(inner product space\)

> 向量空間$$V$$定義在體$$F$$，若向量空間$$V$$上定義內積算子，則稱$$V$$為內積空間。

* 只有三維空間中，才有外積\(cross product\)的定義，且外積的值為向量而非純量。
*  兩個向量的內積，並不是個向量，而是個純量\(scalar\)。



