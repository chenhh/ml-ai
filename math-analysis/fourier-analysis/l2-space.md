# L2與l2空間

## L2空間(平方可積函數空間)

> 定義：$$a \leq t \leq b$$，空間$$L^2([a,b])$$為定義在閉區間$$[a,b]$$上，平方可積分的函數：
>
> $$\displaystyle L^2([a,b])\equiv \left\{ f: [a,b] \rightarrow \mathbb{C} ~\big|~ \int_a^b |f(t)|^2 dt < \infty  \right\}$$$$f$$可為連續函數或可數點不連續的函數。

註：積分中的絕對值(模)不可省略，因為複數$$|z|^2=z\overline{z}$$。

平方可積函數可視為函數值(或訊號的總能量)(取平方避免正負值互相抵消)在區間$$[a,b]$$為有限值。

### L2的內積與範數

> $$f,~g \in L^2([a,b])$$，定義內積：$$\langle f, g \rangle = \int_a^b f(t) \overline{g(t)} dt$$
>
> $$\overline{g(t)}$$為$$g(t)$$的共軛函數

$$\lVert f\rVert ^2 = \langle f, f \rangle = \int_a^b f^2(t)dt$$

### L2空間為無限維度

> 不失一般性令$$[a,b]=[0,1]$$ ，則$$\{1, t, t^2, t^3,\dots\} \subseteq L^2([0,1])$$且均為線性獨立。

## l2空間(平方和為有限值的數列)

> $$l^2$$空間包含了所有滿足以下條件的數列集合$$X$$：
>
> * 數列：$$X=\dots, x_{-1}, x_0, x_{1}, \dots, ~~ x_i \in \mathbb{C}$$
> * &#x20;平方和為有限值：$$\displaystyle \sum_{i=-\infty}^\infty |x_i|^2 < \infty$$

內積：$$\displaystyle \langle X, Y \rangle = \sum_{i=-\infty}^\infty x_i \overline{y}_i$$
