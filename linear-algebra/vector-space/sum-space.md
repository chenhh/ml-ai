# 和空間\(sum space\)

## 和空間

> * $$(V, + , \cdot)$$是定義在體$$F$$上的向量空間。
> * $$W_i, ~ i=1,2,\ldots, K$$為$$V$$的子空間，定義$$W_1+W_2+\dots + W_K=\{w_1+w_2+\dots+w_K|w_i \in W_i, i=1,2,\dots, K\}$$稱為$$W_i, ~ i=1,2,\dots, K$$的和空間。

### 聯集空間為和空間的子集合

> $$\bigcup_{i=1}^K W_i \subseteq \sum_{i=1}^K W_i$$

註：和空間的概念為兩個向量空間中的元素，任意線性組合得出的新空間\($$span(W_1+W_2 )=span(W_1 )+span(W_2 )$$\)，因此和空間所包含的元素，會比單純兩個空間元素的聯集還要多。

proof:

* $$W_1+W_2=\{w_1+w_2 |w_1 \in W_1, ~w_2\in W_2 \} $$
* $$\forall w_1 \in W_1, w_1=w_1+0,  ~0 \in W_2\Rightarrow w_1∈W_1+W_2 $$
* 所以$$W_1\subseteq W_1+W_2  $$
* 同理得$$W_2 \subseteq W_1+W_2  $$
* 所以 $$W_1 \cup W_2 \subseteq W_1+W_2$$
* 可推廣至$$\bigcup_{i=1}^K W_i \subseteq \sum_{i=1}^K W_i  $$ \(QED\)

