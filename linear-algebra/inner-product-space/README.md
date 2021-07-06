# 內積空間\(inner product space\)

## 內積算子\(inner product operator\)

> 向量空間$$V$$定義在體$$F$$，定義內積函數$$\langle \cdot, \cdot \rangle:V \times V \rightarrow F$$滿足：
>
> 1. $$\forall u,v, w \in V$$，$$\langle u+v, w\rangle = \langle u, w\rangle + \langle v, w\rangle$$。
> 2. $$\forall u,v \in V, c \in F$$，$$\langle cu, v\rangle = c \langle u, v\rangle$$。
> 3. $$\forall u,v \in V$$，$$\langle u, v\rangle = \overline{\langle u, v \rangle}$$ （共軛交換性）
> 4. $$\forall v \in V, v \neq 0$$，$$\langle v, v \rangle > 0$$。
>
> 註：內積算子為向量間角度的擴充，可得$$\langle u, v \rangle = \|u \| \|v\| \cos \theta$$，其中$$\theta$$為兩向量$$u, v$$間的夾角，$$\|v\|$$為向量的範數（norm, 長度的擴充）。

* $$\forall v \in V, ~\langle v, \rangle =0 \Leftrightarrow v=0$$。
  * 由於$$\langle v, v \rangle = \| v\| \| v\| \cos \theta =0$$，且向量$$v$$與$$v$$之間的夾角為0，所以$$\cos \theta=1$$，因此$$v=0$$。
* $$\forall u, v, w \in V, a,b \in F, \langle u, av+bw\rangle= \overline{a}\langle u ,v\rangle+\overline{b}\langle u,w\rangle$$
  * $$\langle u, av+bw\rangle = \overline{\langle av + bw, u\rangle} = \overline{a\langle v, u\rangle + b \langle w, u\rangle} = \overline{a\langle v,u\rangle}+\overline{b\langle w, u\rangle}=\overline{a} \langle u,v \rangle+ \overline{b} \langle u, w\rangle$$

### 常見內積

* $$V=\mathbb{C}^{N \times N}$$，$$\forall A,B \in V$$，定義方陣的內積為$$\langle A, B\rangle=tr(AB^{\mathrm {H}})$$。
* $$V=C[a,b]$$為定義在閉區間$$[a,b]$$的所有連續函數，$$F=\mathbb{C}$$，則$$\forall f,g \in V$$，定義函數內積$$\langle f, g \rangle=\int_a^b f(x)\overline{g(x)}dx$$。
* $$V=F^{N \times 1}, F = \mathbb{C}$$，標準（行向量）內積$$\langle x,  y\rangle =y^{\mathrm{H}}x=x_1\overline{y_1} + \dots + x_N\overline{y_N}$$。

## 內積空間\(inner product space\)

> 向量空間$$V$$定義在體$$F$$，若向量空間$$V$$上定義內積算子，則稱$$V$$為內積空間。
>
> 註：向量空間只有定義0向量、向量的合成與縮放。其維度是由基底（同時為最小生成集與最大獨立集）決定。向量間的角度是由內積決定（但內積之值為純量），向量的長度由範數決定。
>
> 度量空間的距離函數是定義在集合上，不必為向量空間，但也可以用在向量空間上。

* 只有三維空間中，才有外積\(cross product\)的定義，且外積的值為向量而非純量。
*  兩個向量的內積，並不是個向量，而是個純量\(scalar\)。

### 內積算子的性質

> $$V$$為定義在體$$F$$的內積空間，$$B=\{b_1, \dots, b_N\}$$為$$V$$的基底。
>
> 1.  $$\forall v \in V, \langle v,0 \rangle=\langle 0,v \rangle=0$$ （零向量的內積必為0）
> 2. $$\forall u,v \in V, \langle u,v \rangle=0 \Leftrightarrow \langle v, u \rangle=0   $$
> 3. $$\displaystyle \forall u_i,v \in V, c_i \in F, ~ \left \langle \sum_{i=1}^K c_i u_i,v \right\rangle =\sum_{i=1}^K c_i  \langle u_i, v\rangle $$
> 4. $$\forall u,v \in V, c \in F, ~ \langle u, cv\rangle = \overline{\langle cv, u\rangle} = \overline{c} \langle u, v\rangle$$
> 5. $$\displaystyle ∀u,v_i \in V, c_i \in F, ~  \left\langle u, \sum_{i=1}^K c_iv_i \right\rangle  =\sum_{i=1}^K \overline{c_i} \langle u, v_i \rangle$$
> 6. $$\langle u,v\rangle=0, \forall v \in V\Leftrightarrow u=0$$ （只有零向量與所有向量內積為0）
> 7. $$\langle u,v \rangle = \langle w,v\rangle, \forall v \in V \Leftrightarrow u=w   $$（$$\forall v \in V$$是必須的條件，否則有可能是剛好選到讓$$u,w$$內積相同的$$v$$）
> 8. $$u=0 \Leftrightarrow  \langle u,b_i \rangle=0, ~\forall i=1,2,\dots,N$$    （因為向量空間間所有的向量均可由基底生成，而只有0向量與所有向量內積為0）

Proof \(1\)

* $$\langle u,0 \rangle= \langle u,0+0 \rangle= \langle u,0 \rangle+ \langle u,0 \rangle \Rightarrow \langle u,0\rangle=0 $$
* 同理$$\langle 0,u \rangle=0$$ \(QED\)

Proof \(6\):

* 若$$f \langle u,v \rangle =0,~\forall v \in V$$
* 則$$\langle u,u \rangle=0 \Rightarrow u=0$$ 
* 反之若$$u=0 \Rightarrow \langle u,v \rangle =0, ~\forall v \in V$$  \(QED\)

Proof \(7\):

* 若$$ u=w$$，則$$\langle u,v \rangle=\langle w,v \rangle$$
* 若$$ \langle u,v \rangle= \langle w,v \rangle, ~ \forall v \in V$$
* 可得$$\langle u,v \rangle− \langle w,v \rangle=0, ~\forall v \in V$$
* 整理得 $$\langle u−w,v \rangle =0, ~\forall v \in V$$
* 由\(6\)知$$u−w=0 \Rightarrow u=w$$ \(QED\)

### 範數\(norm\)

> $$V$$為定義在體$$F$$的內積空間，定義$$\|v\|_2 = \sqrt{\langle v, v \rangle}, ~ \forall v \in V$$為向量$$v$$的長度（範數）。
>
> 兩個向量間的距離為$$\| u -v \| = \| v - u\|$$
>
> • 也可以不使用內積定義向量空間元素的長度，只要定義函數$$\|\cdot\|: V\rightarrow F$$滿足範數的條件即可：
>
> * \(faithfulness\) $$\|x\|=0\Leftrightarrow x=0$$（只有0向量長度為0）
> *  \(homogeneity\) $$\forall c \in F, ~\|cx\|=|c|\|x\|$$
> *  \(subadditivity\) $$\|x+y\| \leq |x\|+\|y\|$$
>
> 因此可定義p-norm為$$\displaystyle \|x\|_p = \left(\sum_{i=1}^N  |x_i|^p \right)^{\frac{1}{p}}$$，此處$$\|x_i|$$的絕對值不可省略，因為$$x_i \$$可為複數。











