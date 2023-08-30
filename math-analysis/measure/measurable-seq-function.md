# 可測函數序列

## 簡介

依測度收斂看的是大局，<mark style="color:blue;">即不限定收斂點是否位於特定的集合當中</mark>，只要最後不收斂的點總數少到幾乎沒有就行；

幾乎處處收斂不僅看大局，還關注細節，在<mark style="color:blue;">一開始就要確定一個“不收斂點集合</mark>$$E_0$$ <mark style="color:blue;">，這個集合中的點個數不僅要少到幾乎沒有，而且集合還得是固定的</mark>。也就是一開始沒在集合上的點之後也得一直收斂，不能突然又不收斂。所以說幾乎處處收斂的要求要比依測度收斂高。

依測度收斂無法保證幾乎處處收斂，因為在依測度收斂的條件下，每個離極限函數比較遠的點全體，此處稱為「壞集合」；壞集合的測度的確是越來越小的，但是你沒辦法控制壞集合的出現的區域，它們依然可以在定義域上漂來漂去，使得你取函數序列尾項的壞集合的聯集，仍然可以是整個定義域。

## 幾乎處處(almost everywhere a.e.)

給定可測空間$$(X,\Sigma)$$，若某性質$$P$$ almost everywhere成立，意思是對所有非零測度集，此性質$$P$$都成立。(換言之，除零測度集之外，此性質$$P$$都成立。)

## 幾乎處處有限、幾乎處處有界(finite a.e, bounded a.e.)

> 若可測函數$$f$$滿足$$\mu(\{x \in X ~|~ f(x)=\infty\})=0$$，則稱為幾乎處處有限函數，記為$$|f(x)|<\infty \text{ a.e. }  \forall x \in E$$。
>
> 若可測函數$$f$$存在正實數$$M > 0 \ni |f(x)|<M \text{ a.e. } \forall x \in E$$，則稱為幾乎處處有界函數。

<mark style="color:red;">註：幾乎處處有界函數=> 幾乎處處有限函數，反之不一定成立。</mark>

範例：$$f(x) = x, ~ x \in \mathbb{R}$$為幾乎處處有限，但非幾乎處處有界函數，因為$$\mu(\{x \in \mathbb{R} ~|~ f(x) = \infty\})=0$$。

## 幾乎處處(點態)收斂(convergence a.e.)

> 定義：函數序列$$\{f_n\}$$幾乎處點態收斂(pointwise convergent a.e.)至函數$$f$$：$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~\text{a.e. on } E$$&#x20;
>
> 即排除掉測度為0的定義域部份，記為$$E_0$$，函數序列的極限與$$f$$之值相等。
>
> $$\displaystyle E_0 = \{x \in X ~|~ \lim_{n \rightarrow \infty} f_n(x) \neq f(x)\}$$，$$\displaystyle  \mu(E_0) = 0$$。

<mark style="color:blue;">因為函數序列</mark>$$\{f_n(x)\}$$<mark style="color:blue;">與</mark>$$f$$<mark style="color:blue;">在極限時只有在零測度集合</mark>$$E_0$$<mark style="color:blue;">不相等，而在</mark>$$E-E_0$$<mark style="color:blue;">均相等，因此若</mark>$$\{f_n(x)\}$$<mark style="color:blue;">為可測函數序列，則可得</mark>$$f$$<mark style="color:blue;">為可測函數</mark>。

## 幾乎一致收斂(almost uniform convergence)

> 函數序列$$\{f_n\}$$幾手乎處處一致收斂至函數$$f$$：
>
> $$\forall \epsilon > 0$$，存在可測集$$E_{\epsilon}$$且滿足$$\mu(E_{\epsilon})<\epsilon$$使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)$$uniformly on $$E_\epsilon^c$$。
>
> 或者說$$\forall \epsilon >0, \ni n_0 \in \mathbb{N}\ni \forall n \geq n_0$$$$\displaystyle \sup_{x \in X - E_\epsilon^c}\| f_n(x) - f(x)\| < \epsilon$$。

註：<mark style="color:blue;">幾乎一致收斂，只要求一致收斂不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度很小，即</mark> $$\mu(E_\epsilon)< \epsilon$$<mark style="color:blue;">。而幾乎處處有性質</mark>$$P(x)$$<mark style="color:blue;">，則要求</mark>$$P(x)$$<mark style="color:blue;">不成立的集合</mark>$$E_\epsilon$$<mark style="color:blue;">的測度為0，即</mark>$$\mu(E_\epsilon)=0$$ <mark style="color:blue;">。因此「幾乎一致收斂」絕對不可以說成「幾乎一致收斂」，兩者不是等價定義</mark>。

因此幾乎一致收斂不可寫為$$\exists E_\epsilon \subseteq E, ~ \mu(E_\epsilon)=0 \ni f_n \rightarrow f \text{ uniformly  on } E-E_0$$；

但如果可得$$\displaystyle \sup_{x \in E-E_0}|f_n(x) - f(x)|=0, \forall n \geq n_0$$時，為一致收斂。

#### 範例

$$f_n(x)=x^n$$ on $$[0,1]$$，可得點態收斂$$\displaystyle \lim_{n \rightarrow \infty} f_n(x)= \left\{ \begin{aligned} 0&, \text{ if } 0 \leq x < 1, \\ 1&, \text{ if } x = 1  \end{aligned} \right.$$為非連續函數，但即使去除掉$$x=1$$，考慮$$f_n(x)=x^n ~ \text{ on } [0,1)$$也非一致收斂(由sup的定義可得$$\displaystyle \sup_{x \in [0,1)}x^n = \sup_{x \in (0,1)}x^n = \sup_{x \in (0,1)}x^n =1$$)；更進一步可得不存在集合$$S$$使得$$f_n \rightarrow f$$ uniformly on $$[0,1]-S$$。

令$$0 < \epsilon <1$$，取$$x = \frac{1+\epsilon}{2}$$，可得$$\epsilon < x < 1$$。

$$x^n = \frac{1+\epsilon}{2}^n=\frac{1}{2^n}(1+\epsilon)^n=\frac{1}{2^n} \sum_{k=0}^n \binom{n}{k}\epsilon^k > \frac{1}{2^n} \epsilon \sum_{k=0}^n \binom{n}{k} = \frac{1}{2^n} 2^n \epsilon = \epsilon$$

此時不存在$$n_0 \in \mathbb{N}$$使得$$x^{n_0} < \epsilon~\forall 0 < \epsilon < 1$$，因此不為一致收斂。

#### 幾乎一致收斂定義的討論

* [https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition](https://math.stackexchange.com/questions/4727429/almost-uniform-convergence-equivalent-definition)
* [https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence](https://math.stackexchange.com/questions/4414448/doubts-regarding-almost-uniform-convergence)
* [https://math.stackexchange.com/questions/3198020/does-xn-converges-uniformly-on-0-1](https://math.stackexchange.com/questions/3198020/does-xn-converges-uniformly-on-0-1)
* [https://math.stackexchange.com/questions/1254285/why-is-f-nx-xn-not-uniformly-convergent-on-0-1](https://math.stackexchange.com/questions/1254285/why-is-f-nx-xn-not-uniformly-convergent-on-0-1)

#### 範例

考慮閉區間$$[0,1]$$的Borel set。$$f_n(x)=x^n$$為連續函數，則：

1. $$f_n \rightarrow f$$點態收斂。
2. $$f_n \rightarrow f$$ 幾乎處處一致收斂。

$$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=f(x)=\left\{ \begin{aligned} 0 &, ~ x \in [0, 1) \\ 1 &, ~ x= 1 \end{aligned} \right.$$為點態收斂。

$$\displaystyle$$$$\displaystyle \sup_{x \in [0,1]} | f_n(x) - f(x) | = 1 \neq 0$$所以非一致收斂。

取$$\epsilon \in (0,1)$$，$$E_{\epsilon}=(1-\frac{\epsilon}{2}, 1]$$，$$\mu(E_\epsilon)= \frac{\epsilon}{2}$$，

且對於$$\forall x \in [0,1] - E_\epsilon$$，可得$$\displaystyle \sup_{x \in [0,1] - E_{\epsilon}}\|f_n(x) - f(x)\|=\sup_{x \in [0, 1-\epsilon]}\|x^n  - 0\|=\| 1- \frac{\epsilon}{2}\|^n \rightarrow 0$$ as $$n \rightarrow \infty$$。

### 幾乎一致收斂保證幾乎處處收斂

> 定義在集合$$E$$的幾乎處處實值(有限)的可測函數序列$$\{f_n\}$$幾乎一致收斂於可測函數$$f$$ ，則$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~\text{a.e. on } E$$ 。
>
> <mark style="color:blue;">註：此處的</mark>$$\mu(E)$$<mark style="color:blue;">可為無窮大，即不限定在有限測度空間</mark>。

<details>

<summary>proof</summary>

因為$$\{f_n\}$$幾乎一致收斂於$$f$$，由定義得存在集合$$E_\epsilon \subseteq E$$滿足$$\forall \epsilon > 0$$，$$\mu(E_\epsilon) < \epsilon$$ $$\displaystyle \exists n_0 \in \mathbb{N} \ni \forall n \geq n_0, \sup_{x \in E-E_\epsilon}|f_n(x) - f(x)|=0$$。

因為$$\{f_n\}$$在$$E-E_\epsilon$$一致收斂至$$f$$，因此$$\{f_n\}$$在$$E -E_\epsilon$$上點態收斂至$$f$$。

而由於上述收斂性質在$$\forall \epsilon >0, \mu(E_\epsilon)<\epsilon$$均成立，因此可得$$\{f_n\}$$在$$f$$幾乎處處收斂&#x20;

(QED)

</details>

### 範例：幾乎處處收斂，但不依測度收斂&#x20;

$$f_n(x)=\frac{x}{n}$$ 。則$$f_n(x)$$幾乎處處收斂於$$f(x)=0$$。但不依測度收斂。



## 參考資料

* [https://proofwiki.org/wiki/Definition:Uniform\_Convergence](https://proofwiki.org/wiki/Definition:Uniform\_Convergence)
