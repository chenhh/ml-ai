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

## 複數

\[虛數, imaginary number\] $$i=\sqrt{-1}, ~ i^2=−1, ~ i^3=−\sqrt{-1}, ~i^4=1$$

複數$$z \in \mathbb{C}$$有以下常用型式

* $$z=x+iy $$
* $$z=(x,y)$$
*  \[極坐標, polar form\] $$z=(r \cos \theta,r \sin\theta),~ r=\sqrt{x^2 + y^2}> 0,~ \theta\equiv \mathrm{arg}(z)=\tan^{−1}⁡\frac{y}{x} \in [−\pi, \pi]$$
* $$z=re^{i\theta}$$
* $$x=\mathrm{Re}(z), y=\mathrm{Im}(z)$$
* $$\mathrm{Re}(z)=\frac{z + \overline{z}}{2}, ~ \mathrm{Im}(z)=\frac{z− \overline{z}}{2i}$$

| 名稱 | 意義 | 符號 |
| :--- | :--- | :--- |
| modulus of $$z$$ | length $$r$$ of $$z$$ | $$|z|$$ |
| argument of $$z$$ | angle $$\theta$$ of $$z$$ | $$\mathrm{arg}(z)$$ |
| real part of $$z$$ | $$x$$ coordinate of $$z$$ | $$\mathrm{Re}(z)$$ |
| imaginary part of $$z$$ | $$y$$ coordinate of $$z$$ | $$\mathrm{Im}(z)$$ |
| imaginary number | real multiple of $$i$$ |  |
| complex conjugate of $$z$$ | reflection of $$z$$ in the real axis | $$\overline{z}$$ |

![&#x8907;&#x6578;&#x7B26;&#x865F;](../.gitbook/assets/complex-number-min.png)

