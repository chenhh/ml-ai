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









