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

