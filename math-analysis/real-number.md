# 實數\(real number\)

有很多理論都可以建立實數系，而戴德金切割法\(Dedekind cut method\) 建構實數為最簡單。此法的特色是以有理數系為基礎，然後只利用了集合與邏輯性質建構實數系。

## 實數集完備性的七個等價定理

實數集$$\mathbb{R}$$ 與有理數系$$\mathbb{Q}$$ 兩者都是有序體\(totally-ordered field\), 但是兩者最大的差別在於實數集具有完備性\(所有收斂數列均收斂在集合中\)，而有理數集沒有完備性。

1. **Dedekind切割原理\(Dedekind cut theorem\)**：對於實數集的任何一個切割$$R$$的最小上界存在。
2. **確界原理（ supremum and infimum principle ）**： 設S為非空數集。若S有上界，則S必有上確界；若S有下界，則S必有下確界。可以由實數的無限小數公理或者 Dedekind 分割證明   。
3. **區間套定理\(Nested Intervals Theorem\)**：實數連續性的一種描述，幾何意義是，有一數列閉區間\(兩個端點也屬於此區間\)，滿足後一個閉區間包含於前一個閉區間\(區間越來越小\)以及閉區間長

   度的極限為零這兩個條件時，則這一數列區間存在唯一一個共同點。

4. **單調有界定理\(The monotone bounded convergence theorem\)**：單調\(遞增或遞減\)有界數列必收斂（有極限）。
5. **有限覆蓋定理\(finite cover theorem\)**：有界閉區間的任何一個開覆蓋\(open cover\)， 必存在有限個數的子覆蓋。
6. **數列緊緻性定理 \(compact sequence\)**：有界數列必有收斂的子數列。
7. **柯西收斂準則\(Cauchy converge criterion\)**：無窮數列收斂的充分必要條件是無窮數列是柯西數列。

這七個定理可以循環證明，因此均為實數集完備性公理的等價敘述。





## 阿基米德性質\(Archimedean property\)

> $$\forall 0 < a, b \in \mathbb{R} \Rightarrow \exists n \in \mathbb{N} \ni na > b$$。

* 若$$a>b$$，則取$$n=1$$可得$$a>b$$。
* 不論$$a$$有多小，$$b$$有多大，必定可以找到$$n \in \mathbb{N} \ni na>b$$  。

![&#x963F;&#x57FA;&#x7C73;&#x5FB7;&#x6027;&#x8CEA;](../.gitbook/assets/archimedean_property.png)

##  實數集的稠密性

> $$\forall a,b \in \mathbb{R}, \ a <b$$ $$ \exists u \in \mathbb{Q}, \ v \in \Gamma \ni a < u < b$$ 且 $$ a < v < b$$。
>
> 任兩個不相等的實數之間，必定存在無理數或有理數。





