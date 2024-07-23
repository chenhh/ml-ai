# 函數不連續的分類

## 簡介

函數$$f: E \rightarrow \mathbb{R}$$在點$$x \in E$$連續若且唯若$$\forall \epsilon > 0 \exists \delta > 0 \ni |x-c|< \delta \Rightarrow |f(x) -f(c)| < \epsilon$$。

通常記為$$\displaystyle \lim_{x \rightarrow c} f(x)=f(c)$$。

函數所有不連續點的集合可以是離散集合，也可以是密集集合，甚至可以是函數的整個定義域。

根據不連續點的性質，通常把不連續點分為兩類：

<mark style="color:red;">第一類不連續點</mark>：&#x20;

* <mark style="color:blue;">可移除不連續點(removable discontinuity)</mark>：不連續點兩側函式的極限存在且相等 。&#x20;
* <mark style="color:blue;">跳躍不連續點(jump discontinuity</mark><mark style="color:red;">)</mark>：不連續點兩側函式的極限存在，但不相等；&#x20;

<mark style="color:red;">第二類不連續點</mark>：

不屬於第一類不連續點的任何一種不連續點都屬於第二類不連續點。第二類不連續點可以進一步分為無<mark style="color:red;">窮不連續點</mark>和<mark style="color:red;">震盪不連續點</mark>。

## 可移除不連續點(removable discontinuity)

範例：

$${\displaystyle f(x)={\begin{cases}x^{2}&{\text{ for }}x<1\\0&{\text{ for }}x=1\\2-x&{\text{ for }}x>1\end{cases}}}$$

則點$$x_0=1$$為可移除的不連續點。

<mark style="color:blue;">其中左極限與右極限存在且為有限值，左右極限相等但是不等於該點的函數值</mark>。$$\displaystyle \lim _{x\to x_{0}^{-}}f(x) =\lim _{x\to x_{0}^{+}}f(x) \neq f(x_0)$$。

<mark style="color:red;">注意函數</mark>$$f(x)$$<mark style="color:red;">依定義是在</mark>$$x_0$$<mark style="color:red;">(點態)連續</mark>。

<figure><img src="../../.gitbook/assets/image (24).png" alt="" width="375"><figcaption><p>可移除不連續點</p></figcaption></figure>

## 跳躍不連續點(jump discontinuity)

$${\displaystyle f(x)={\begin{cases}x^{2}&{\mbox{ for }}x<1\\0&{\mbox{ for }}x=1\\2-(x-1)^{2}&{\mbox{ for }}x>1\end{cases}}}$$$$\displaystyle f(x)={\begin{cases}x^{2}&{\text{ for }}x<1\\0&{\text{ for }}x=1\\2-(x-1)^{2}&{\text{ for }}x>1\end{cases}}$$

則點$$x_0=1$$為跳躍不連續點。

<mark style="color:blue;">其中左極限與右極限存在且為有限值，但是左右極限不相等，因此函數在該點的極限不存在。</mark>

$$\displaystyle \lim _{x\to x_{0}^{-}}f(x) \neq \lim _{x\to x_{0}^{+}}f(x)$$

<mark style="color:red;">因為函數在</mark>$$x_0$$<mark style="color:red;">的左、右極限不相等，極限不存在，得</mark>$$f(x)$$<mark style="color:red;">在</mark>$$x_0$$<mark style="color:red;">不連續</mark>。

## 本質不連續點(Essential discontinuity)

函數在點$$x_0$$兩側至少有一側的極限不存在(極限值為$$\pm \infty$$)時。

$${\displaystyle f(x)={\begin{cases}\sin {\frac {5}{x-1}}&{\text{ for }}x<1\\0&{\text{ for }}x=1\\{\frac {1}{x-1}}&{\text{ for }}x>1.\end{cases}}}$$

則點$$x_0=1$$為本質不連續點。

<figure><img src="../../.gitbook/assets/image (25).png" alt="" width="375"><figcaption><p>震蕩不連續點</p></figcaption></figure>

## 參考資料

[https://en.wikipedia.org/wiki/Classification\_of\_discontinuities](https://en.wikipedia.org/wiki/Classification\_of\_discontinuities)
