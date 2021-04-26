# 函數\(function\)

## 關係\(relation\)

> $$X$$為一集合，若$$\mathbf{R}\subseteq X \times X$$，稱$$\mathbf{R}$$為集合$$X$$的一個關係。
>
> 若$$(x,y)\in \mathbf{R}$$，稱$$x$$與$$y$$具有$$\mathbf{R}$$的關係，記為$$x\mathbf{R}y$$。

note: relation比function更一般化，因為可為一對多的對應。

![&#x95DC;&#x4FC2;&#x53EF;&#x70BA;&#x4E00;&#x5C0D;&#x591A;&#x7684;&#x5C0D;&#x61C9;](../.gitbook/assets/math_relation-min-1-.png)

### 等價關係\(equivalence relation\)

> 令$$\mathbb{R}$$為集合$$X$$的關係，且滿足
>
> * \[反身性, reflexive\] $$\forall x \in X,\ x \mathbf{R}x$$
> * \[對稱性, symmetric\] $$x,y\in X, \ x\mathbf{R}y \Leftrightarrow y \mathbf{R}x$$
> * \[遞移性, transitive\] $$x,y,z \in X, \  x \mathbf{R}y\ \land \ y \mathbf{R} z \Rightarrow x  \mathbf{R} z $$

e.g. $$ n \in \mathbb{N},\ X \in \mathbb{Z}, \mathbf{R} = \{ (x-y) \ \vert \ n(x-y) \}$$為等價關係。

## 函數 \(function\)

> $$X,Y$$為兩集合\(相同或相異均可\)，函數$$f: X \rightarrow Y$$定義對於$$X$$中的每一個元素$$x$$，均存在唯一的函數值$$f(x) \in Y$$。$$\forall x \in X, \exists! y \in Y \ni f(x)=y$$
>
> * $$X$$為函數$$f$$的定義域\(domain\)。
> * $$Y$$為函數$$f$$的對應域\(codomain\)。
> * $$f(X) = \{ f(x), x\in X \} \subseteq Y$$為函數$$f$$的值域，其中等號成立於$$f$$為映成函數。

