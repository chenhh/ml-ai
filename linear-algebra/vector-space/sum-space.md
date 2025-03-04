# 和空間(sum space)

## 和空間

> * $$(V, + , \cdot)$$是定義在體$$F$$上的向量空間。
> * $$W_i, ~ i=1,2,\ldots, n$$為$$V$$的子空間，定義$$W_1+W_2+\dots + W_n=\{w_1+w_2+\dots+w_n|w_i \in W_i, i=1,2,\dots, n\}$$稱為$$W_i, ~ i=1,2,\dots, n$$的和空間。

### 聯集空間為和空間的子集合

> $$\bigcup_{i=1}^n W_i \subseteq \sum_{i=1}^n W_i$$

註：和空間的概念為兩個向量空間中的元素，任意線性組合得出的新空間($$span(W_1+W_2 )=span(W_1 )+span(W_2 )$$)，因此和空間所包含的元素，會比單純兩個空間元素的聯集還要多。

* 例如：$$W_1=\{ (x,0)| x \in \mathbb{R}\}$$，$$W_2 = \{(0,y)|y \in \mathbb{R}\}$$
* $$W_1 + W_2 = \mathbb{R}^2$$
* $$W_1 \cup W_2$$為$$x$$軸聯集$$y$$軸。

proof:

* $$W_1+W_2=\{w_1+w_2 |w_1 \in W_1, ~w_2\in W_2 \}$$
* $$\forall w_1 \in W_1, w_1=w_1+0,  ~0 \in W_2\Rightarrow w_1∈W_1+W_2$$
* 所以$$W_1\subseteq W_1+W_2$$
* 同理得$$W_2 \subseteq W_1+W_2$$
* 所以 $$W_1 \cup W_2 \subseteq W_1+W_2$$
* 可推廣至$$\bigcup_{i=1}^n W_i \subseteq \sum_{i=1}^n W_i$$ (QED)

### 和空間為原向量空間的子空間

> * $$(V, + , \cdot)$$是定義在體$$F$$上的向量空間。$$W_1, W_2$$為$$V$$的子空間，則$$W_1+W_2$$為$$V$$的子空間（$$W_1+W_2$$元素的任意線性組合仍在同空間中）。
> * 可推廣至$$\sum_{i=1}^n  W_i$$為$$V$$的子空間，且子空間為凸集合。

註：因為和空間為子空間的任意線性組合，以生成集來看和空間的元素不可能比原向量空間還多，因此和空間為原向量空間的子空間。

proof:

* 因為$$0 = 0 + 0 \in W_1 + W_2$$，所以$$W_1 + W_2 \neq \emptyset$$
* $$\forall x, y \in W_1 + W_2, ~ a,b \in F$$ $$\exists x_1, y_1 \in W_1, x_2, y_2 \in W_2 \ni x=x_1+x_2, y=y_1+y_2$$
* 所以$$ax+by=a(x_1+x_2)+b(y_1+y_2)=(ax_1+by_1)+(ax_2+by_2)$$
* 因為$$W_1$$為子空間，所以$$(ax_1+by_1) \in W_1$$。
* 因為$$W_2$$為子空間，所以$$(ax_2+by_2) \in W_2$$
* 因此$$ax+by \in W_1 + W_2$$(QED)



### 和空間的維度

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令$$W_1, W_2$$為$$V$$的子空間，則$$\dim(W_1 +W_2) = \dim(W_1) + \dim(W_2) -\dim(W_1 \cap W_2)$$

Proof:

* $$W_1 \cap W_2$$ 為$$V$$的子空間(因為$$W_1\cap W_2$$ 中任意元素的線性組合必定仍在此集合中)。
* 取$$\{v_1,\dots,v_k \}$$為$$W_1 \cap W_2$$ 的基底。
* 因為$$W_1 \cap W_2 \subseteq W_1$$，所以$$\{v_1, \dots ,v_k \}$$為$$W_1$$中的線性獨立集。
* 若$$span(W_1 \cap W_2 ) \neq W_1$$，則存在$$x_1,x_2, \dots ,x_m \in W_1 \ni B_1=\{v_1,\dots,v_k,x_1,\dots,x_m \}$$為$$W_1$$ 的基底。
* 同理存在$$y_1, \dots ,y_n \in W_2 \ni B_2=\{v_1,\dots ,v_k,y_1,\dots ,y_n \}$$為$$W_2$$的基底。
* 所以$$\dim⁡(W_1 \cap W_2 )=k$$，$$\dim⁡(W_1)=k+m$$，$$\dim⁡(W_2 )=k+n$$

要證明 $$B=B_1 \cup B_2=\{v_1,\dots ,v_k,x_1, \dots ,x_m,y_1,\dots ,y_n \}$$為$$W_1+W_2$$ 的基底。

* 生成集
  * $$W_1=span(B_1 ), ~ W_2=span(B_2 ) \Rightarrow W_1+W_2=span(B_1 \cup B_2 )=span(B)$$
* 線性獨立
  * 令 $$\sum_{i=1}^k a_i v_i +\sum_{j=1}^m b_j x_j +\sum_{l=1}^n c_l y_l =0 \Rightarrow  \sum_{i=1}^k a_i v_i+\sum_{j=1}^m b_j x_j =−\sum_{l=1}^n c_l y_l$$
  * 因為$$\sum_{i=1}^k a_i v_i +\sum_{j=1}^m b_j x_j \in W_1$$且 $$−\sum_{l=1}^n c_l y_l \in W_2$$
  * 所以$$\sum_{i=1}^k a_i v_i +\sum_{j=1}^m b_j x_j =− \sum_{l=1}^n c_l y_l \in W_1 \cap W_2$$
  * 因此存在$$d_1,\dots ,d_k\in F \ni −\sum_{l=1}^n c_l y_l =\sum_{s=1}^k d_s v_s  \Rightarrow \sum_{s=1}^k   d_s v_s +\sum_{l=1}^n c_l y_l =0$$
  * 因為$$B_2$$ 為線性獨立集，可得$$d_s=c_l=0,  \forall s,l$$
  * 代回得$$\sum_{i=1}^k a_i v_i +\sum_{j=1}^m b_j x_j=0$$
  * 同理因$$B_1$$ 為線性獨立集，所以$$a_i,b_j=0, \forall i,j$$
  * 因此$$B$$為線性獨立集。
* 由於$$span(B)=W_1+W_2$$ 且$$B$$為線性獨立集，所以$$B$$為$$W_1+W_2$$ 的基底 (QED)



