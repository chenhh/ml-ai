# 生成空間\(sapping space\)

## 線性組合\(linear combination\)

> $$(V, +, \cdot)$$為定義在體$$F$$的線性組合，$$v_1, \dots ,v_n \in V, c_1, \dots, c_n \in F$$，稱$$v=c_1v_1+\dots + c_n v_n =\sum_{i=1}^n c_i v_i$$為向量$$v_1,\dots, v_n$$之線性組合。

## 生成空間\(spanning space\)

> $$(V, +, \cdot)$$為定義在體$$F$$的線性組合，$$S \subseteq V$$，定義生成空間$$span(S)=\{ v| v \text{ is linear combination of S}\}$$。
>
> * 註：$$span(\emptyset)=\{0\}$$。
> * $$span(S)$$為使用集合內元素任意線性組合可得到所有結果的集合。

#### 範例

* $$span((1,0))=\{x(1,0)|x \in \mathbb{R}\} $$ \(x-axis\)
* $$span((0,1))=\{y(0,1)|y \in \mathbb{R} \} $$ \(y-axis\)
* $$span((1,0),(0,1))=\{x(0,1)+y(1,0)|x,y \in \mathbb{R}= \mathbb{R}^2\} $$
* $$span((2,0),(0,2))=\{x(0,2)+y(2,0)|x,y \in \mathbb{R}=\mathbb{R}^2\} $$

### 生成空間為子空間

> $$(V, +, \cdot)$$為定義在體$$F$$的線性組合，$$S \subseteq V$$，則$$span(S)$$為$$V$$的子空間。
>
> 若$$W$$為$$V$$的子空間，且$$S \subseteq W$$，則$$span(S) \subseteq W$$。





