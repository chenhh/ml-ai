# 有理數

## 有理數集合

> $$\mathbb{Q} = \big\{ \frac{m}{n} | m \in \mathbb{Z}, n \in \mathbb{N}, \operatorname{gcd}(p,q)=1 \big\}$$



## 有理數體\(field\)

有理數集合可定義加法與乘法運算，形成有理數體$$(\mathbb{Q}, +, \cdot)$$。

* 加法交換律\(commutative law\)：$$\forall a,b \in \mathbb{Q}$$, $$a+b=b+a$$。
* 加法結合律\(associative law\)：$$\forall a,b,c \in \mathbb{Q}$$, $$(a+b)+c=a+(b+c)$$。
* 加法單位元素\(additive identity\)：$$\exists 0 \in \mathbb{Q} \ni \forall a \in \mathbb{Q},\ a+0=0+a=a$$。
* 加法反元素\(additive inverse\)：$$\forall a \in \mathbb{Q} \exists -a \ni \mathbb{Q} \ni a+(-a) = (-a)+a=0$$
* 乘法交換律：$$\forall a,b \in \mathbb{Q}$$, $$a \cdot b = b \cdot a$$
* 乘法結合律：$$\forall a,b,c \in \mathbb{Q}$$, $$(a \cdot b) \cdot c=a \cdot (b \cdot c)$$。
* 乘法單位元素：$$\exists 1 \in \mathbb{Q} \ni \forall a \in \mathbb{Q},\ a\cdot 1 = 1 \cdot a = a$$。
* 乘法反元素：$$\forall a \in \mathbb{Q}, a \neq 0 \exists a^{-1} \in \mathbb{Q} \ni a \cdot a^{-1} = a^{-1} \cdot a = 1$$。
* 乘法對加法的分配律：$$\forall a,b,c \in \mathbb{Q}$$, $$a \cdot (b+c)=a\cdot b + a \cdot c$$。

## 有理數系\(rational number system\)

因為有理數體為[全序集](partial-total-order-set.md#quan-xu-ji-total-order-set)\(集合中任意兩個元素可以比較大小\)，而把$$(\mathbb{Q}, + , \cdot, \leq)$$稱為有理數系。

### 有理數的稠密性：任兩個不相等的有理數之間必存在第三個有理數

> $$\forall x,y \in \mathbb{Q}, x < y$$, let $$z=\frac{x+y}{2}$$, then $$x < z < y$$ and $$z \in \mathbb{Q}$$。

## 有理數的十進位表示法

> 給定有限位數實數$$r_n=a_0.a_1 a_2\ldots a_n, ~ a_0 \in \mathbb{Z}^{+}, a_i \in \{0,1,\ldots, 9\}, ~ i=1,2,\ldots, n $$可表示成$$r_n=a_0+\frac{a_1}{10}+\frac{a_2}{10^2} +\cdots +\frac{a_n}{10^n}$$ 
>
> 無限位數表示法為$$r=a_0.a_1 a_2 a_3\cdots $$

### 實數可被任意精確度的有理數逼近

> • 給定$$x \in \mathbb{R}^+$$, 則$$\forall n \in \mathbb{N}, ~ \exists r_n=a_0.a_1 a_2 \cdots a_n \ni r_n \leq x < r_n+\frac{1}{10^n} $$

Proof:

* 令$$S=\{y \in \mathbb{N}, ~y\leq x\}\neq \emptyset$$ 為整數的子集合，因此S有上界, 由實數完備性得最小上界存在，令$$\sup(⁡S)=a_0$$。
* 因為$$a_0 \in \mathbb{Z}^+ \Rightarrow a_0 \in S$$, 令$$a_0=[x]$$  ，即$$ a_0 \leq x<a_0+1  $$。
* 令$$a_1=[10x−10a_0 ]$$  依序建造下去即可\(QED\)

