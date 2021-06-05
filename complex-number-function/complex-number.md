# 複數\(complex number\)

## 複數空間

複數空間$$\mathbb{C}^n$$ 為向量空間, 也稱為線性空間\(linear space\)

* 令$$V$$為非空集合，$$F$$為域\(field\)，定義二個運算$$+$$與$$\cdot$$，其中
  *  $$+:V \times V \rightarrow V$$為一函數，稱為向量加法\(vector addition\)。
  * $$\cdot:F \times V  \rightarrow V$$為一函數，稱為純量積\(scalar multiplication\)。
  * 即滿足 $$\forall u,v \in V$$ 唯一存在$$u+v \in V$$且$$\forall \alpha  \in F, ~ v \in V,$$唯一存在$$\alpha v \in V$$

若上述二個運算滿足以下八個性質，稱V is a vector space over field F

1. 向量加法交換性 $$\forall u,v \in V, u+v=v+u$$
2. 向量加法結合性 $$\forall u,v,w \in V,~ (u+v)+w=u+(v+w)$$
3. 向量加法單位元素 $$\exists 0 \in V \ni \forall v \in V,~ v+0=0=0+v=v$$
4. 向量加法反元素 $$\forall v \in V,~ \exists −v \in V \ni v+(−v)=(−v)+v=0$$
5. 純量積對向量加法分配性 $$\forall \alpha \in F, ~ u,v \in V, ~ \alpha\ \cdot (u+v)=\alpha \cdot u+\alpha \cdot v$$
6. 純量積對純量加法分配性 $$\forall \alpha ,\beta \in F,~ v \in V, ~ (\alpha+\beta)\cdot v=\alpha \cdot v+\beta \cdot v$$
7. 純量乘法對純量積結合性 $$\forall \alpha ,\beta \in F~ v \in V ~ (\alpha \beta)\cdot v=\alpha \cdot (\beta v)$$
8. 單位純量積之單位元素 $$\forall v \in V ~ 1\cdot v=v$$

