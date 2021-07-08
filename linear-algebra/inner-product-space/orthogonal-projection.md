# 正交投影\(orthogonal projection\)

正交投影除了幾何上的意義之外，在最佳化的時候（如最小二乘法或求最短距離）時經常被使用。

## 正交投影向量\(orthogonal projection vector\)

> $$V$$為定義在體$$F$$上的內積空間，$$W$$為$$V$$的子空間。
>
> 向量$$v \in V$$，若存在$$v_0 \in W \ni \langle v-v_0, w\rangle =0, ~ \forall w \in W$$，則稱$$v_0$$為$$v$$在$$W$$上的（正交）投影向量，記為$$v_0=\mathrm{proj}_W(v)$$。

![&#x6B63;&#x4EA4;&#x6295;&#x5F71;](../../.gitbook/assets/orthogonal_projection-min.png)

* 此性質告訴我們向量$$v$$相對於向量空間$$W \subseteq V$$可拆解成投影向量$$\mathrm{proj}_W (v)$$與正交向量$$v−\mathrm{proj}_W (v)$$兩部份。
* $$v=\mathrm{proj}_W(v)+(v-\mathrm{proj}_W(v)) = \mathrm{proj}_W(v) + \mathrm{proj}_{W^\bot}(v)$$

### 向量v與空間W正交若且唯若向量v與空間W所有基底向量正交

> $$V$$為定義在體$$F$$上的內積空間，$$W$$為$$V$$的子空間。令$$B=\{b_1, b_2, \dots, b_K\}$$為$$W$$的一組基底，$$v \in V$$，則向量$$v$$與空間$$W$$正交，即$$\langle v, w \rangle=0,~ \forall v \in W \Leftrightarrow \langle v ,b_i \rangle=0, ~i=1,2,\dots, K$$。

proof =&gt;: 由定義得出。

proof &lt;=:

* $$\forall w \in W, w=\sum_{i=1}^K c_i b_i$$
* 所以$$\langle v,w \rangle = \langle v, \sum_{i=1}^Kc_i b_i \rangle = \sum_{i=1}^K \overline{c_i}\langle v, b_i \rangle=\sum_{i=1}^K \overline{c_i} \cdot 0 = 0$$\(QED\)

### 正交投影公式

> $$V$$為定義在體$$F$$上的內積空間，$$W$$為$$V$$的子空間。令$$B=\{b_1, b_2, \dots, b_K\}$$為$$W$$的一組正交基底（即$$\langle b_i, b_j \rangle =0, ~\forall i \neq j$$），$$v \in V$$，則：
>
> * $$\mathrm{proj}_W(v)\equiv v_0=\sum_{i=1}^K \frac{\langle v, b_i \rangle}{\langle b_i, b_i \rangle} b_i \in W$$為$$v$$在向量空間$$W$$上的正交投影向量（即$$v−v_0$$ 與所有$$W$$中的元素正交）。
> * $$v$$在$$W$$上的正交投影向量唯一。
>
>  若生成集或基底非正交時，可使用Gram-Schmidt正交化預處理。

Proof \(1\)

* 因為$$v_0\in W$$ 為基底的線性組合，所以$$v_0 \in span\{b_1,b_2,\dots,b_K \}=W  $$。
* $$\forall j=1,2, \dots,K$$
  * $$\begin{aligned} \langle v−v_0,b_j \rangle &= \langle v−\sum_{i=1}^K \frac{\langle v,b_i \rangle}{\langle b_i,b_i \rangle}  b_i,b_j ⟩ \\ &=\langle v,b_j \rangle−\langle \sum_{i=1}^K\frac{\langle v,b_i \rangle}{ \langle b_i,b_i \rangle}  b_i,b_j \rangle \\ &=\langle v,b_j \rangle−\sum_{i=1}^K \frac{\langle v,b_i \rangle}{\langle b_i, b_i \rangle} \langle b_i,b_j \rangle \{\because \langle b_i,b_j \rangle=0, ~\forall i \neq j\} \\ &=\langle v,b_j \rangle−\frac{\langle v,b_j \rangle}{\langle b_j,b_j \rangle}  \langle b_j,b_j \rangle \\ & =\langle v,b_j \rangle− \langle v,b_j \rangle=0  \end{aligned}$$
  * 由上一個定理知$$\langle v−v_0,w \rangle=0, ~ \forall w \in W$$，所以$$v_0$$ 為$$v$$在$$W$$上的投影向量。\(QED\)







