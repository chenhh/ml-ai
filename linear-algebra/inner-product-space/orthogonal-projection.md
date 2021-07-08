# 正交投影\(orthogonal projection\)

正交投影除了幾何上的意義之外，在最佳化的時候（如最小二乘法或求最短距離）時經常被使用。

## 正交投影向量\(orthogonal projection vector\)

> $$V$$為定義在體$$F$$上的內積空間，$$W$$為$$V$$的子空間。
>
> 向量$$v \in V$$，若存在$$v_0 \in W \ni \langle v-v_0, w\rangle =0, ~ \forall w \in W$$，則稱$$v_0$$為$$v$$在$$W$$上的（正交）投影向量，記為$$v_0=\mathrm{proj}_W(v)$$。

![&#x6B63;&#x4EA4;&#x6295;&#x5F71;](../../.gitbook/assets/orthogonal_projection-min.png)

* 此性質告訴我們向量$$v$$相對於向量空間$$W \subseteq V$$可拆解成投影向量$$\mathrm{proj}_W (v)$$與正交向量$$v−\mathrm{proj}_W (v)$$兩部份。
* $$v=\mathrm{proj}_W(v)+(v-\mathrm{proj}_W(v)) = \mathrm{proj}_W(v) + \mathrm{proj}_{W^\bot}(v)$$

