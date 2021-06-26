# 生成空間\(sapping space\)

## 線性組合\(linear combination\)

> $$(V, +, \cdot)$$為定義在體$$F$$的線性組合，$$v_1, \dots ,v_n \in V, c_1, \dots, c_n \in F$$，稱$$v=c_1v_1+\dots + c_n v_n =\sum_{i=1}^n c_i v_i$$為向量$$v_1,\dots, v_n$$之線性組合。

## 生成空間\(spanning space\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S \subseteq V$$，定義生成空間$$span(S)=\{ v| v \text{ is linear combination of S}\}$$。
>
> * 註：$$span(\emptyset)=\{0\}$$。
> * $$span(S)$$為使用集合內元素任意線性組合可得到所有結果的集合。

#### 範例

* $$span((1,0))=\{x(1,0)|x \in \mathbb{R}\} $$ \(x-axis\)
* $$span((0,1))=\{y(0,1)|y \in \mathbb{R} \} $$ \(y-axis\)
* $$span((1,0),(0,1))=\{x(0,1)+y(1,0)|x,y \in \mathbb{R}= \mathbb{R}^2\} $$
* $$span((2,0),(0,2))=\{x(0,2)+y(2,0)|x,y \in \mathbb{R}=\mathbb{R}^2\} $$

### 生成空間為子空間

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S \subseteq V$$，則$$span(S)$$為$$V$$的子空間。
>
> 若$$W$$為$$V$$的子空間，且$$S \subseteq W$$，則$$span(S) \subseteq W$$。

直觀的解釋為$$span(S)$$為由集合$$S$$生成的任意線性組合向量仍是$$span(S)$$的元素，因此$$span(S)$$為$$V$$的子空間。

## 生成集\(spanning set\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S \subseteq V$$，若$$span(S)=V$$，則稱集合$$S$$生成$$V$$，稱$$S$$為$$V$$的生成集合。

* 若$$S_1 \subseteq S_2$$，則$$span(S_1) \subseteq span(S_2)$$。
* $$S \subseteq span(S)$$。
* $$span(S_1 \cap S_2 ) \subseteq span(S_1) \cap span(S_2)$$。
* $$span(S_1 \cup S_2) \supseteq span(S_1) \cup span(S_2)$$。

### 和空間與生成集

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，$$S_1, S_2 \subseteq V$$。
>
> 若$$W_1 = span(S_1), W_2 = span(S_2)$$，則和空間$$W_1 + W_2 = span(S_1 \cup S_2)$$。
>
> 即$$span(S_1) + span(S_2) = span(S_1 \cup S_2)$$

### 行空間與列空間分別由矩陣的行與列生成

給定矩陣$$A \in F^{M \times N}$$，則：

* $$\begin{align} CS(A)  & = \{ Ax | x \in F^{N \times 1}\} \\ & = \begin{bmatrix} A_{:1} & \dots & A_{:N}\end{bmatrix} \begin{bmatrix}x_1 \\ \vdots \\ x_N \end{bmatrix} \\ & = \{x_1 A_{:1} + \dots + x_N A_{:N}\} \\ & = span(\{ A_{:1}, \dots ,A_{:N}\}) \end{align}$$
* 所以矩陣$$A$$的column　space　$$CS(A)$$為矩陣$$A$$的行向量所生成的空間。
* $$\begin{align} RS(A)  & = \{ xA | x \in F^{1 \times M}\} \\ & = \begin{bmatrix} x_1 & \dots & x_M\end{bmatrix} \begin{bmatrix} A_{1:} \\  \vdots \\ A_{M:} \end{bmatrix} \\ &= \{ x_1 A_{1:} + \dots + x_M A_{M:}\} \\ & = span(\{A_{1:}, \dots, A_{M:}\}) \end{align}$$
* 所以矩陣$$A$$的row　space　$$RS(A)$$為矩陣$$A$$的列向量所生成的空間。

## 線性獨立集\(linear independent set\)

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，且$$S \subseteq V$$。
>
> 令$$x_1, x_2, \dots , x_k \in S, ~~c_1, c_2, \dots, c_k \in F$$，若存在不全部為0的$$c_1,c_2, \dots, c_k$$使得$$c_1 x_1 + \dots + c_kx_k=0$$，則稱$$S$$為線性相依集。
>
> 若$$S$$不為線性相依性，則$$S$$為線性獨立集，可得$$c_1 x_1 + c_2 x_2 + \dots +c_k x_k = 0 \Leftrightarrow c_1 = c_2  = \dots = c_k = 0$$。

* 線性相依的直觀意義即$$x_1,x_2,\dots,x_k$$ 中的某些向量為其它向量的線性組合。
* 因此線性獨立指集合中的任一向量皆非其它向量的線性組合。

### 線性獨立集的性質

* $$S_1 \subseteq S_2$$，若$$S_2$$ 為線性獨立集合，則$$S_1$$也為線性獨立集合。
* $$S_1 \subseteq S_2$$，若$$S_1$$為線性相依集合，則$$S_2$$ 也為線性相依集合。
* 若$$0 \in S$$，則$$S$$為線性相依集合，因為$$1\cdot 0=0$$。
* 若$$S$$為線性獨立集合，則$$0 \notin S$$。





















