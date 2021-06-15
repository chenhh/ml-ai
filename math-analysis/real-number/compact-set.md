# 緊緻集合\(compact set\)

##  緊緻集合\(compact set\)

> * $$S\subseteq \mathbb{R}^n$$ 稱為緊致集合若且唯若集合$$S$$的任意開覆蓋均存在有限個數的子開覆蓋。
> * 即$$S\subseteq \mathbb{R}^n$$為緊緻集合 $$\Leftrightarrow \exists \{I_1, I_2,\ldots, I_m\}$$為開集合族且 $$S\subseteq \bigcup_{k=1}^m I_k$$。

* 若存在一組開覆蓋不存在有限個數的子開覆蓋時，則$$S$$不為緊緻集合。
* [Heine-Borel覆蓋定理證明任意有界閉集合均存在有限個數的子開覆蓋](covering.md#heineborel-fu-gai-ding-li)；以下會證明反向也成立，即若均存在有限個數的子開覆蓋集合$$S$$，則$$S$$為有界閉集合。因此在歐式空間中，緊緻集合與閉集合等價。

#### 範例

* $$\mathbb{N}=\{1,2,3,\ldots\}$$, 而$$I_k=(\frac{k−1}{2^k} ,\frac{k+1}{2^k} ), ~k \in \mathbb{N}$$為$$\mathbb{N}$$的可數開覆蓋，但不存在有限開覆蓋，因此自然數不是緊緻集。
* $$A=(0,1), F=(\frac{1}{k}, \frac{2}{k}), ~ k \in \mathbb{N}$$  為$$A$$的可數開覆蓋，但不存在有限開覆蓋，因此$$A$$不是緊緻集。
* 空集合$$\emptyset$$ 為緊致集。
* $$A=\{\frac{1}{k}, ~k \in \mathbb{N}\}$$不是緊緻集。因為 $$I_k=(\frac{1}{k}−\frac{1}{2^k} ,\frac{1}{k}+\frac{1}{2^k} ), F=\{I_k, ~k\in \mathbb{N}\}$$為$$A$$的可數開覆蓋，但不是有限開覆蓋。

##  緊緻集合的充要條件

> $$S \subseteq \mathbb{R}^n$$, 則以下三個性質等價：
>
> 1. $$S$$為緊致集合。
> 2. $$S$$為有界閉集合\(closed and bounded set\)\($$\exists M >0, \exists x\in S \ni S \subseteq N_r (x) $$且 $$S$$為閉集合\)。
> 3. $$S$$的任意無窮子集合均存在極限點$$x$$，且$$x∈S$$.  \(Bolzano-Weierstrass定理，任意有界無窮集合均存在極限點\(in $$\mathbb{R}^n$$\)   。$$\forall r>0 (N_r (x)\cap S)\setminus \{x\} \neq \emptyset$$，則$$x$$為$$S$$的極限點。

* 而在任意度量空間中，只能保證1-&gt;2, 3 與3-&gt;1,無法保證2-&gt;1 \(但在$$\mathbb{R}^n$$ 成立\)
* 有界集合不一定是閉集合，如$$S=(1,2) \subseteq \mathbb{R}$$為有界開集合。
*  Heine-Borel覆蓋定理證明任意有界閉集合均存在有限個數的子開覆蓋；因此2-&gt;1成立。

Proof 1-&gt;2:

* 令$$p \in S$$, 可得球集合族 $$\{N_1 (p), N_2 (p),\ldots, N_k (p), \ldots\}, k \in \mathbb{N}$$為$$S$$的可數開覆蓋。
* 由緊致集合條件可得有限子集合族為$$S$$的開覆蓋，即 $$S \subseteq \bigcup_{k=1}^m N_k (p)$$。
* 因此可得$$S$$為有界集合 -- \(1\)。
*  \(反證法\) 假設$$S$$不為閉集合
* 由[閉集合包含其所有極限點的或質 ](../metric-space/closed-set.md#bi-ji-he-bao-han-qi-suo-you-ji-xian-dian)知存在$$S$$的極限點$$y$$且$$y \notin S$$。

	• 若x∈S, 因為y∉S, 可得r\_x=‖x−y‖/2&gt;0,∀x, 且{N\_\(r\_x \) \(x\), x∈S}為S的開覆蓋.

	• 由為S為緊緻集，所以存在有限個開球集合覆蓋S, 即 S⊆∪\_\(k=1\)^m N\_\(r\_k \) \(x\_k\).

	• 令r=min⁡{r\_1,r\_2,⋯,r\_m }, 可得N\_r \(y\)∩N\_\(r\_k \) \(x\_k \)=ϕ.

		○  ∵x∈N\_r \(y\)⇒‖x−y‖&lt;r≤r\_k

		○ 由三角不等式得 ‖ y−x\_k ‖≤‖y−x‖+‖x−x\_k ‖

		○ ∴‖x−x\_k ‖≥‖y−x\_k ‖−‖x−y‖=2r\_k−‖x−y‖&gt;k

		○ ∴x∉N\_\(r\_k \) \(x\_k\).

	• ∴N\_r \(y\)∩S=ϕ, 此與y為S的極限點矛盾, 因此S為閉合 \(QED\)





>





