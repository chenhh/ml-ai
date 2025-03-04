# 緊緻集合(compact set)

## 有界集合(bounded set)

> $$S \subseteq \mathbb{R}$$為有界集, 則存在$$M > 0 \ni \forall x \in S$$, $$|x| < M$$。&#x20;
>
> 或者$$S \subseteq \mathbb{R}^n$$為有界集，則存在$$M > 0, p \in \mathbb{R}^n \ni S \subseteq B_M(p)$$。

## 緊緻集合(compact set)

> 定義：$$S\subseteq \mathbb{R}^n$$ 稱為緊致集合若且唯若集合$$S$$的任意開覆蓋均存在有限個數的子開覆蓋。
>
> 即$$S\subseteq \mathbb{R}^n$$為緊緻集合 $$\Leftrightarrow \exists \{I_1, I_2,\ldots, I_m\}$$為開集合族且 $$S\subseteq \bigcup_{k=1}^m I_k$$。

若存在一組開覆蓋且不能有限個數的子開覆蓋時，則$$S$$不為緊緻集合。

[Heine-Borel覆蓋定理證明任意有界閉集合均存在有限個數的子開覆蓋](covering.md#heineborel-fu-gai-ding-li)；以下會證明反向也成立，即若均存在有限個數的子開覆蓋集合$$S$$，則$$S$$為有界閉集合。<mark style="color:red;">因此在歐式空間中，緊緻集合與閉集合等價</mark>。

#### 範例

* $$\mathbb{N}=\{1,2,3,\ldots\}$$, 而$$I_k=(\frac{k−1}{2^k} ,\frac{k+1}{2^k} ), ~k \in \mathbb{N}$$為$$\mathbb{N}$$的可數開覆蓋，但不存在有限開覆蓋，因此自然數不是緊緻集。
* $$A=(0,1), F=(\frac{1}{k}, \frac{2}{k}), ~ k \in \mathbb{N}$$ 為$$A$$的可數開覆蓋，但不存在有限開覆蓋，因此$$A$$不是緊緻集。
* 空集合$$\emptyset$$ 為緊致集。
* $$A=\{\frac{1}{k}, ~k \in \mathbb{N}\}$$不是緊緻集。因為 $$I_k=(\frac{1}{k}−\frac{1}{2^k} ,\frac{1}{k}+\frac{1}{2^k} ), F=\{I_k, ~k\in \mathbb{N}\}$$為$$A$$的可數開覆蓋，但不是有限開覆蓋。

## 歐式空間中緊緻集合的充要條件

> $$S \subseteq \mathbb{R}^n$$, 則以下三個性質等價：
>
> 1. $$S$$為緊致集合。
> 2. $$S$$為有界閉集合(closed and bounded set)($$\exists M >0, \exists x\in S \ni S \subseteq N_r (x)$$且 $$S$$為閉集合)。
> 3. $$S$$的任意無窮子集合均存在一個極限點$$x$$，且$$x \in S$$. (Bolzano-Weierstrass定理，任意有界無窮集合均存在極限點(in $$\mathbb{R}^n$$) 。$$\forall r>0 (N_r (x)\cap S)\setminus \{x\} \neq \emptyset$$，則$$x$$為$$S$$的極限點。

<mark style="color:red;">而在任意度量空間中，只能保證1->2, 1->3 與3->1,無法保證2->1</mark> (但在$$\mathbb{R}^n$$ 成立)

有界集合不一定是閉集合，如$$S=(1,2) \subseteq \mathbb{R}$$為有界開集合。

閉集合不一定有界，如$$\mathbb{R}$$，$$\mathbb{N}$$等均為無界閉集合。

Heine-Borel覆蓋定理證明任意有界閉集合均存在有限個數的子開覆蓋；因此2->1成立。

<details>

<summary>proof: 緊致集合->有界閉集合(一般度量空間成立)</summary>

令$$p \in S$$, 可得球集合族 $$\{N_1 (p), N_2 (p),\ldots, N_k (p), \ldots\}, k \in \mathbb{N}$$為$$S$$的可數開覆蓋。

由緊致集合條件可得有限子集合族為$$S$$的開覆蓋，即 $$S \subseteq \bigcup_{k=1}^m N_k (p)$$。

因此可得$$S$$為有界集合 -- (1)。

(反證法) 假設$$S$$不為閉集合

由[閉集合包含其所有極限點的或質 ](../metric-space/closed-set.md#bi-ji-he-bao-han-qi-suo-you-ji-xian-dian)知存在$$S$$的極限點$$y$$且$$y \notin S$$。

若$$x\in S$$, 因為$$y \notin S$$, 可得$$r_x=\|x−y\|/2>0, ~ \forall x$$, 且$$\{N_{r_x } (x), ~ x∈S\}$$為$$S$$的開覆蓋。

由為$$S$$為緊緻集，由定義得存在有限個開球集合覆蓋$$S$$, 即 $$S\subseteq \bigcup_{k=1}^m N_{r_k} (x_k)$$。

令$$r=\min \{r_1,r_2,\ldots,r_m \}$$, 可得$$N_r (y) \cap N_{r_k} (x_k )= \emptyset$$。

$$x \in N_r (y) \Rightarrow \|x−y\|<r \leq r_k$$

由三角不等式得 $$\| y−x_k \| \leq \|y−x\|+\|x−x_k\|$$

所以 $$\| x−x_k \| \geq \|y−x_k \|−\|x−y\|=2r_k−\|x−y\|>k$$

因此 $$x \notin N_{r_k} (x_k)$$

即$$N_r (y) \cap S=\emptyset$$，此與$$y$$為$$S$$的極限點矛盾，因此$$S$$為閉集合--(2)

由(1)(2)得2成立 (QED)

</details>

<details>

<summary>proof: 有界閉集合->任意無限子集必有極限點 (一般度量空間的證明)</summary>

反證法：

令$$T \subseteq S$$為無限多點的子集合，且假設$$T$$沒有極限點(in $$S$$或$$T$$)。

則$$\forall x \in S, ~ \exists r > 0 \ni B_r(x) \cap T - \{x\} = \empty$$if $$x \notin T$$。

將滿足上述條件的開球$$B_r(x)$$取聯集，可得集合$$\displaystyle S \bigcup_{x \in S} B_r(x)$$的開覆蓋。

因為$$S$$為緊緻集，因此必存在可數開覆蓋$$S \displaystyle \bigcup_{i=1}^n B_{r_i}(x_i), ~ x_i \in S$$。

因此可得 $$\displaystyle T \subseteq \bigcup_{i=1}^n B_{r_i}(x_i)$$。

但因為每個開球$$B_{r_i}(x_i)$$與集合$$T$$沒有交集，與假設不符，因此$$T$$必有極限點(QED)

</details>

<details>

<summary>proof: 有界閉集合->任意無限子集必有極限點 (歐式空間的證明)</summary>

令 $$T\subseteq S$$, 且$$T$$中有無限多個元素。因為$$S$$為有界集合，因此$$T$$為有界集合。

由[Bolzano-Weierstrass定理](bolzano-weierstrass-theorem.md) 得若$$T \subseteq \mathbb{R}^n$$ 為有界集合且$$T$$包含了無窮多個點，則存在至少一點$$x \in \mathbb{R}^n$$為$$T$$的極限點。

令$$x$$為$$T$$的極限點且$$T \subseteq S$$，則$$x$$為$$S$$的極限點。

因為$$S$$為閉集合，因此所有$$S$$的極限點均為$$S$$的元素，而$$x$$為$$S$$的極限點，因此$$x \in S$$ (QED)

</details>

<details>

<summary>proof: 有界閉集合->緊緻集合 (只在歐式空間成立)</summary>

可由Heine-Borel覆蓋定理證明任意有界閉集合均存在有限個數的子開覆蓋得出。

</details>

<details>

<summary>proof: 任意無限子集必有極限點->有界閉集合(一般度量空間成立)</summary>

若$$S$$為無界集合，則$$∀m>0 ~\exists x_m \in S \ni \|x_m\|>m$$

取$$T=\{x_1,x_2,\ldots\}$$為$$S$$的無窮子集合，由條件3可知$$T$$存在極限點$$y \in S$$。

取$$m>1+\|y\|$$, 可得 $$\|x_m−y\| \geq \|x_m \|−\|y\|>m−\|y\|>1$$, 即$$y$$不是$$T$$的極限點（矛盾），因此$$S$$為有界集合。--(1)

令$$x$$為集合$$S$$的極限點，因為$$\forall r > 0, ~ B_r(x) \cap S$$包含了$$S$$的無限多個點。

定義開球為$$\forall k \in \mathbb{N}, ~B_{1/k}(x)$$, 且從相異開球中取出相異點$$x_k \in B_{1/k}(x)$$形成集合$$T=\{x_1, x_2, \dots, \} \subseteq S$$，可得$$\displaystyle \lim_{k \rightarrow \infty} x_k = x$$。

因為$$T$$為$$S$$的無限子集，由給定條件得必存在極限點 --(2)

令 $$y \neq x$$為相異極限點, 由三角不等式得 $$|y-x| \leq |y-x_k| + |x_k - x| \leq |y-x_k| + 1/k$$ if $$x_k \in T$$。

當$$k_0$$足夠大使得$$1/k < 1/2 |y-x|, ~\forall k > k_0$$時，取$$r=1/2|y-x|$$可得$$x_k \neq B_r(x), ~ \forall k \geq k_0$$。

因此$$y$$不是集合$$T$$的極限點，因此$$x$$為唯一的極限點--(3)

由(2,3)得$$S$$為閉集合 --(4)

由(1,4)得$$S$$為有界閉集合(QED)

(QED)

</details>

### 範例：一般度量空間中有界閉集合不一定為緊緻集

> 給定有理數集合$$\mathbb{Q}$$與實數的度量$$d(x,y)=\lVert x - y \rVert$$。
>
> 令$$S=\{r \in \mathbb{Q} ~|~ r \in (a,b), ~a, b \in \mathbb{R- Q} \}$$為開區間$$(a,b)$$間的所有有理數，且$$a,b$$均為無理數。
>
> 則$$S$$為有理數集$$\mathbb{Q}$$的有界閉集合，但非緊緻集合。

## 緊緻集的任一閉子集仍為緊緻集

> $$S\subseteq \mathbb{R}^n$$為緊緻集，若$$K \subseteq S$$為閉集合，則$$K$$為緊緻集。
>
> 一般度量空間均成立

<details>

<summary>proof: 一般度量空間</summary>

令$$\{O_i\}_{i \in I}$$為集合$$K$$的開覆蓋，即$$\displaystyle K \subseteq \bigcup_{i \in I}O_i$$。

可得$$\displaystyle S \subseteq \bigcup_{i \in I} O_i \cup K^c$$。

因為$$S$$為緊緻集，由定義得存在有限開覆蓋 $$\displaystyle S \subseteq \bigcup_{i=1}^n O_i \cup K^c$$

因此可得$$\displaystyle K \subseteq \bigcup_{i=1}^n O_i$$ (QED)

</details>

<details>

<summary>proof: 歐式空間可用Heine-Borel定理證明</summary>

因為$$S$$為緊緻集，所以$$S$$為有界閉集合。

因為$$K \subseteq S$$且$$S$$為有界集合，所以$$K$$為有界集合。

因為$$K$$為有界閉集合，依Heine-Borel定理得$$K$$為緊緻集合。(QED)

</details>

## 緊緻集必存在收斂子數列

> $$S \subseteq \mathbb{R}^n$$為緊緻集，且$$\{x_n\} \subseteq S$$為一數列(不一定收斂)，則存在一子序列$$\{x_{n_i}\}$$與點$$x \in S \ni \displaystyle \lim_{i \rightarrow \infty} x_{n_i} = x$$

<details>

<summary>proof:</summary>

若數列$$\{x_n\}$$為有限集，則可直接使用其上(下)界得出$$x_{n_1} = x_{n_2} = \dots = x$$。

如列為$$\{x_n\}$$為無限集，因為$$S$$為緊緻集，則其無限子集必有一極限點。(QED)

</details>

## 緊緻集合的有限聯集仍為緊緻集

> $$S_i,~ \subseteq \mathbb{R}^n ~ i=1,2,\dots,n$$為緊緻集，則$$\displaystyle \bigcup_{i=1}^n S_i$$仍為緊緻集。
>
> 一般度量空間也成立。

<details>

<summary>proof: 直接以緊緻集定義證明</summary>

因為$$S_i$$為緊緻集，令$$S_i \subseteq \displaystyle \bigcup_{j=1}^k O_{ij}$$, $$O_{ij} \subseteq \mathbb{R}^n$$為開集合。

可得$$\displaystyle \bigcup_{i=1}^n S_i \subseteq \bigcup_{i=1}^n \bigcup_{j=1}^k O_{ij}$$。

因為任意開集合的聯集仍為開集合，可得$$\displaystyle \bigcup_{i=1}^n S_i$$為緊緻集(QED)

</details>

## 緊緻集合的任意交集仍為緊緻集

> $$S_i, \subseteq \mathbb{R}^n~ i \in \mathbb{N}$$為緊緻集，則$$\displaystyle \bigcap_{i=1}^\infty S_i$$仍為緊緻集。
>
> 一般度量空間也成立。

<details>

<summary>proof:</summary>



</details>

## 緊緻集與閉集合的交集仍為緊緻集

> $$S$$為緊緻集合且$$T$$為閉集合，則$$S \cap T$$為緊緻集合。
>
> 一般度量空間也成立。

<details>

<summary>proof:</summary>

因為$$S$$為緊緻集合，所以$$S$$為有界閉集合。

因為閉集合的任意交集仍為閉集合，因此$$S \cap T$$為閉集合 --(1)

令$$\{O_i\}, i \in I$$為$$S \cap T$$的開覆蓋，即$$S \cap T \subseteq \displaystyle \bigcup_{i in I} O_i$$。

因為$$S \cap T \subseteq S$$，且$$S$$為緊緻集，由緊緻集的任一閉子集仍為緊緻集的性質得$$S\cap T$$為緊致集 (QED)

</details>
