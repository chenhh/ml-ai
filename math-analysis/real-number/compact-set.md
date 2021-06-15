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





