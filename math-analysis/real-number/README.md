# 實數(real number)

## 簡介

把有理數比做直線，則直線上會充滿了間隙，它是不完備(非空有界集合不一定有上確界或收斂點列均收命斂在集合內)、不連續的。<mark style="color:blue;">而我們則把直線看成是沒有間隙的、 完備的和連續的</mark>。 直線的連續性是什麼意思？我們必須要有連續性的一個精確定義，使它可以成為邏輯推理的基礎。

## 實數集完備性的七個等價定理

實數集$$\mathbb{R}$$ 與有理數系$$\mathbb{Q}$$ 兩者都是有序體(totally-ordered field), <mark style="background-color:red;">但是兩者最大的差別在於實數集具有完備性(</mark>完備性指集合中不存在「空隙」或「缺失的點」<mark style="background-color:red;">)，而有理數集沒有完備性</mark>。

1. **Dedekind切割原理(Dedekind cut theorem)**：對於實數集的任何一個切割$$R$$的最小上界必定存在。
2. **確界原理（ supremum and infimum principle）也稱實數的完備性**： 設S<mark style="color:red;">為非空集合</mark>。<mark style="color:red;">若</mark>S<mark style="color:red;">有上界，則S必有上確界</mark>；<mark style="color:red;">若S有下界，則S必有下確界</mark>。可以由實數的無限小數公理或者 Dedeki~~n~~d 分割證明 。
3.  **區間套定理(Nested Intervals Theorem)**：實數集中的點可以被無限縮小的區間精確定位，而不會出現「空隙」。幾何意義是有一閉區間序列(兩個端點也屬於此區間)，滿足後一個閉區間包含於前一個閉區間(區間越來越小)以及閉區間長

    度的極限為零這兩個條件時，則這一序列區間存在唯一一個共同點(收斂至一點)。
4. **單調有界定理(The monotone bounded convergence theorem)**：單調(遞增或遞減)有界序列必收斂（有極限，且收斂在上(下)確界)。
5. **數列緊緻性定理 (compact sequence)**：有界數列必有收斂的子數列\[以二元切割法直接建構]。
6. **有限覆蓋定理(finite cover theorem, Heine-Borel theorem)**：有界閉區間(緊緻集)的任何一個開覆蓋(open cover)， 必存在有限個數的子覆蓋。
7. **柯西收斂準則(Cauchy converge criterion)**：柯西序列的項之間的距離隨著項數的增加而越來越小。無窮數列收斂的充分必要條件是無窮數列是Cauchy數列(因為實數的完備性可以保證Cauchy數列的收斂值為實數)。

這七個定理可以循環證明，因此均為實數集完備性公理的等價敘述。

## 實數集的稠密性

> $$\forall a,b \in \mathbb{R}, \ a <b$$ $$\exists u \in \mathbb{Q}, \ v \in \Gamma \ni a < u < b$$ 且 $$a < v < b$$。
>
> 任兩個不相等的實數之間，必定存在無理數與有理數。

<details>

<summary>proof:</summary>

給定$$a,b \in \mathbb{R}$$，由Archmidean性質得必存在$$x,y \in \mathbb{Z}$$滿足滿足$$x <y$$且$$[a,b] \subseteq I_1=[x,y]$$。

令$$t = (x+y)/2$$, 則$$t \in \mathbb{Q}$$為有理數。

將閉區間$$I_1$$分解為$$I_{11} \cup I_{12}$$, 其中$$I_{11}=[x, t]$$, $$I_{12} = [t,y]$$。

則以下三種狀況必定有一種符合：

* $$[a,b] \subseteq I_{11}$$
* $$[a,b] \subseteq I_{12}$$
* $$t\in (a,b)$$

如果$$t \in (a,b)$$，則得到$$u = t \in \mathbb{Q}$$，滿足 $$a< u < b$$。

如果$$[a,b] \in I_{11}$$，令$$I_2 = I_{11}$$，以上述方式繼續分解。 若存在某一區間$$\{I_n\}$$的中點$$u \in \mathbb{Q}$$ 使得 $$a < u <b$$，則得任意兩實數間必有一有理數 (QED 1)。

否則得一區間序列$$\{I_n\}$$，其滿足每一區間$$I_n$$的兩端點為有理數，且$$\displaystyle \lim_{n \rightarrow \infty} |I_n| =0$$。

因為區間長度$$b-a$$為一固定值，因此在分解區間$$m$$時，必定可得$$|I_m| < (b-a)$$，因此$$\{I_m\}$$ 必有一端點在$$(a,b)$$上 (QED 2)。

同理可得無理數$$v \in \Gamma \ni a < v < b$$ (QED 3)

</details>

## 實數集合

> 定義非空實數集合$$\mathbb{R}$$滿足十個公理（axioms），且可分為三類：field axioms, order axioms, completeness axioms。

### field axioms

$$\forall x,y,z \in \mathbb{R}$$，定義加法與乘法兩個二元算子性質如下：

1. \[交換律] $$x+y=y+x$$, $$xy=yx$$
2. \[結合律] $$x+(y+z)=(x+y)+z$$, $$(xy)z=x(yz)$$
3. \[分配律] $$x(y+z)=xy+xz$$
4. \[加法反元素] $$\forall x, y \in \mathbb{R}$$, $$\exists z \in \mathbb{R} \ni x+z=y$$, 記為$$z=y-x$$。$$x-x$$記為0。當$$y=0$$時，$$z$$為$$x$$的加法反元素。
5. \[乘法反元素] 若 $$x,y \in \mathbb{R}$$且$$x \neq 0$$, 則存在$$z \in \mathbb{R}$$使得$$xz=y$$，記為$$z=\frac{y}{x}$$。當$$y=1$$時，$$z=x^{-1}$$為其乘法反元素。

### order axioms

$$\forall x,y,z \in \mathbb{R}$$，有序關係性質如下：

1. \[三一律] $$x=y, x > y, x<y$$三者同時只有一個性質為真。
2. 若 $$x <y$$，則$$\forall z\in \mathbb{R}, ~ x+z < y+z$$。
3. 若$$x >0$$且 $$y >0$$則$$xy >0$$。
4. 若$$x>y$$且 $$y >z$$，則$$x > z$$。

* 當$$x>0$$時稱為正數（positive number）；$$x<0$$時稱為負數（negative number）。
* $$x \leq y \Leftrightarrow x<y \lor x = y$$。

### 有序性質

> $$\forall a,b \in \mathbb{R}$$，若 $$a \leq b + \epsilon, ~ \forall \epsilon >0$$，則$$a \leq b$$。
>
> 反之若 $$a > b$$時，則$$\exists \epsilon > 0 \ni a > b+ \epsilon$$。
>
> 在證明時經常會使用此性質，比如$$\forall \epsilon >0, a -\epsilon \leq a_n \leq a +\epsilon$$，可得$$a_n \leq a$$且 $$a \leq a_n$$，由三一律得$$a_n =a$$。

若$$b < a$$，令$$\epsilon = \frac{b-a}{2}$$，則 $$b+\epsilon = b+ \frac{a-b}{2} = \frac{a+b}{2} < \frac{a+a}{2}=a$$(QED)。

## 絕對值(absolute value)

> 定義$$|x| = \left\{ \begin{align} x, \text{ if } x \geq 0 \\ -x, \text{ if } x <0\end{align}\right.$$$$a \geq 0$$且$$|x| \leq a$$ $$\Leftrightarrow -a \leq x \leq a$$。

## 不等式

以下不等式在Banach空間(complete normed linear space)一般都會成立。

### 三角不等式

> * $$\forall x,y \in \mathbb{R}$$, $$|x+y| \leq |x| + |y|$$
> * $$|x_1 + x_2 + \cdots +x_n | \leq |x_1| + |x_2| +\cdots +|x_n|$$
> * $$|x_1 +x_2 + \cdots + x_n| \geq |x_1| - |x_2| - \cdots - |x_n|$$

<details>

<summary>proof</summary>

$$-|x| \leq x \leq |x|, ~ -|y| \leq y \leq |y|$$。

$$-(|x| + |y) \leq x + y \leq |x|+ |y|$$，可得 $$|x+y| \leq |x| +|y|$$。(QED)

</details>

### Cauchy-Schwarz不等式

> 若$$a_1 ,a_2, \ldots, a_n$$且$$b_1, b_2, \ldots, b_n$$為任意實數，可得 $$\displaystyle \left(\sum_{k=1}^n a_k b_k\right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
>
> 若將數列視為向量，可將上式改寫為 $$\langle \mathbf{a}, \mathbf{b} \rangle^2 \leq \| \mathbf{a} \|^2 \| \mathbf{b}\|^2$$

### Lagrange不等式

> $$\displaystyle \left(\sum_{k=1}^n a_k b_k\right)^2 = \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) - \sum_{1 \leq k < j \leq n} (a_k b_j - a_j b_k)^2$$

### Minkowski不等式

> $$\displaystyle \left(\sum_{k=1}^n (a_k b_k)^2\right)^{1/2} \leq \left( \sum_{k=1}^n a_k^2 \right)^{1/2} \left( \sum_{k=1}^n b_k^2 \right)^{1/2}$$
>
> 此為$$n$$維空間的三角不等式 $$\| \mathbf{a} + \mathbf{b}\| \leq \|\mathbf{a}\|+\|\mathbf{b}\|$$
