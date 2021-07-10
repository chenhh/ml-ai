# 正交補空間\(orthogonal complement space\)

##  正交補空間

> $$V$$為定義在體$$F$$的內積空間，$$S \subseteq V$$為子集合（不必為子空間）。
>
> 定義$$S^\bot=\{v \in V ~|~ \langle v, s \rangle = 0, ~\forall s \in S \}$$，稱為$$S$$的正交集空間。
>
> 正交集空間必為向量空間$$V$$的子空間。

#### 範例：歐式平面

* $$V=\mathbb{R}^2$$，$$S=\left\{  \begin{bmatrix} 1 \\ 0\end{bmatrix} \right\}$$，則$$S^\bot=\left\{ \begin{bmatrix} 0 \\y \end{bmatrix} | y \in \mathbb{R}  \right\}$$\(正交補空間為$$y$$軸\)。
* $$W=\left\{ \begin{bmatrix} x \\ 0 \end{bmatrix} | x \in \mathbb{R}\right\}$$，則$$W^\bot=\left\{ \begin{bmatrix} 0 \\ y \end{bmatrix} | y \in \mathbb{R}\right\}$$

### 正交補空間的性質

> $$V$$為定義在體$$F$$的內積空間，$$S \subseteq V$$為子集合，則：
>
> 1. $$\{0\}^\bot = V$$，$$V^\bot =\{0\}$$（只有0向量與所有向量內積為0）
> 2. $$S^\bot$$為$$V$$的子空間（因為$$0 \in S^\bot$$，且$$\forall u,v \in S^\bot, cu+v \in S^\bot$$）
> 3. $$S \subseteq S^{\bot \bot}$$，$$S^{\bot \bot}=(S^\bot)^\bot$$（兩次正交補空間不一定為空間）
> 4. $$S \cap S^\bot =\left\{  \begin{align} &\{0\}, & \text{ if } 0 \in S, \\& \emptyset, & \text{ if } 0 \notin S \end{align} \right.$$
> 5. 若$$W$$為$$V$$的子空間，且$$B=\{b_1, \dots, b_K\}$$為$$W$$的一組基底，則 $$v \in W^\bot \Leftrightarrow \langle v, b_i \rangle =0, ~i=1,2,\dots, K$$。

proof \(1\):

* $$\forall v \in V, \langle 0, v \rangle=0$$，所以$$\{0\}^\bot=V$$，同理$$V^\bot =\{0\}$$\(QED\)

proof\(2\)：

* 由定義得$$S^\bot \subseteq V$$且$$\langle 0, s\rangle =0, ~\forall s \in S$$，所以$$0 \in S^\bot$$。
* $$\forall c \in F, u, v \in S^\bot$$，$$\langle u,s \rangle = \langle v,s\rangle=0$$
* 所以$$\langle cu+ v, s\rangle=c\langle u, s\rangle+ \langle v,s \rangle=0$$
* 因此$$cu+v \in S^\bot$$ \(QED\)

proof \(3\)：

* $$\forall v \in S^\bot, \langle v,s \rangle =0, ~\forall s \in S$$
* 所以$$\forall s \in S, \langle v, s \rangle =0 \Rightarrow \langle s, v \rangle = 0, s \in S^{\bot\bot}$$ \(QED\)

Proof \(4\)

* 只需證明$$S \cap S^{\bot} \subseteq \{0\}$$
* $$\forall s \in S\cap S^{\bot}$$，$$\langle s,v \rangle=0, ~\forall v \in S^{\bot} $$$$\Rightarrow \langle s,s \rangle=0 \Rightarrow s=0$$ \(QED\).

#### 範例

* $$S=span\left \{ v_1=\begin{bmatrix} 1 \\0 \\ 1 \\0\end{bmatrix}, v_2=\begin{bmatrix} 1 \\ 1 \\1\\ 0\end{bmatrix}\right\}$$
* $$\forall x=\begin{bmatrix} a\\b\\c\\d\end{bmatrix} \in S^\bot$$，$$\langle x, v_1 \rangle = \langle x, v_2 \rangle=0$$
* $$a+c=0, a+b+c=0$$，所以$$x=\begin{bmatrix} -c \\0 \\c \\d\end{bmatrix}$$，取$$S^\bot=span\left\{   \begin{bmatrix} -1 \\0 \\1 \\0\end{bmatrix},  \begin{bmatrix} 0 \\0 \\0 \\1\end{bmatrix}   \right\}$$

### 正交投影算子的性質

> $$V$$為定義在體$$F$$的內積空間，$$W$$為$$V$$的子空間，$$P\equiv \mathrm{proj}_W(v)$$為$$V$$在$$W$$上的正交投影算子，則：
>
> 1. $$ker(P)=W^\bot$$（$$ker(P)$$為投影到正交空間的集合）
> 2. $$V = W \oplus W^\bot$$（向量空間必可分解成投影空間與其正交補空間）
> 3. $$\dim(V) = \dim(W) + \dim(W^\bot)$$
> 4. $$W^{\bot\bot}=W$$
> 5. $$\forall v \in W ~ \exists !w \in W, u\in W^\bot \ni v=u+w$$\(正交投影分解唯一性\)
> 6. $$v-P(v)$$為$$v$$在$$W^\bot$$上的正交投影向量
> 7. $$I-P$$為$$v$$在$$W^\bot$$的正交投影算子\($$\forall v \in V, I(v)=v$$\)

proof \(1\)：

* $$v \in ker(P)$$，由定義得$$P(v)\equiv \mathrm{proj}_W(v)=0$$
* 即$$v \bot W$$，因此$$v \in W^\bot$$，所以$$ker(P) \subseteq W^\bot$$
* 反之可得$$W^\bot \subseteq ker(P)$$
* 因此$$ker(P) = W^\bot $$ \(QED\)

#### 





