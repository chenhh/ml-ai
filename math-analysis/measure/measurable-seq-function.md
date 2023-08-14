# 可測的函數序列

## 簡介

依測度收斂看的是大局，也就是不管哪個點收斂哪個點不收斂，只要最後不收斂的點總數少到幾乎沒有就行；

幾乎處處收斂不僅看大局，還關注細節，在一開始就要確定一個“不收斂點集合$$E_0$$ ，這個集合中的點個數不僅要少到幾乎沒有，而且集合還得是固定的。也就是一開始沒在集合上的點之後也得一直收斂，不能突然又不收斂。所以說幾乎處處收斂的要求要比依測度收斂高。

幾乎處處收斂意味著不收斂的點很少很少（少到極限下測度為零）。依測度收斂意味著不收斂的點可以在極限處被控制在很小的範圍內。

依測度收斂無法保證幾乎處處收斂，因為在依測度收斂的條件下，每個離極限函數比較遠的點全體，此處稱為「壞集合」；壞集合的測度的確是越來越小的，但是你沒辦法控制壞集合的分佈，它們依然可以在定義域上漂來漂去，使得你取函數序列尾項的壞集合的聯集，仍然可以是整個定義域。

## 幾乎處處(almost everywhere a.e.)

給定可測空間$$(X,\Sigma)$$，若某性質$$P$$ almost everywhere成立，意思是 對所有非零測度集，此性質$$P$$都成立。(換言之，除零測度集之外，此性質$$P$$都成立。)

## 幾乎處處實值函數(a.e. real-valued function)

> 若可測函數$$f$$滿足$$\mu(\{x \in X ~|~ f(x)=\infty\})=0$$，則稱為幾乎處處實值函數。

## 幾乎處處點態收斂(convergence a.e.)

> 定義：函數序列$$\{f_n\}$$幾乎處點態收斂(pointwise convergent a.e.)至函數$$f$$：$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x) ~\text{a.e.}$$
>
> 即排除掉測度為0的定義域部份，函數序列的極限與$$f$$之值相等。
>
> $$\displaystyle  \mu( \{x \in X ~|~\lim_{n \rightarrow \infty} f_n(x) \neq (x)\}) = 0$$

## 幾乎處處一致收斂(almost uniform convergence)

> 函數序列$$\{f_n\}$$幾手乎處處一致收斂至函數$$f$$：
>
> $$\forall \epsilon > 0$$，存在可測集$$E_{\epsilon}$$且滿足$$\mu(E_{\epsilon})<\epsilon$$使得$$\displaystyle \lim_{n \rightarrow \infty} f_n(x) = f(x)$$uniformly on $$E_\epsilon^c$$。
>
> 或者說$$\displaystyle \sup_{x \in X - E_\epsilon^c}\| f_n(x) - f(x)\| < \epsilon$$。

#### 範例

考慮閉區間$$[0,1]$$的Borel set。$$f_n(x)=x^n$$為連續函數，則：

1. $$f_n \rightarrow f$$點態收斂。
2. $$f_n \rightarrow f$$ 幾乎處處一致收斂。

$$\displaystyle \lim_{n \rightarrow \infty}f_n(x)=f(x)=\left\{ \begin{aligned} 0 &, ~ x \in [0, 1) \\ 1 &, ~ x= 1 \end{aligned} \right.$$為點態收斂。

$$\displaystyle$$$$\displaystyle \sup_{x \in [0,1]} | f_n(x) - f(x) | = 1 \neq 0$$所以非一致收斂。

取$$\epsilon \in (0,1)$$，$$E_{\epsilon}=(1-\frac{\epsilon}{2}, 1]$$，$$\mu(E_\epsilon)= \frac{\epsilon}{2}$$，

且對於$$\forall x \in [0,1] - E_\epsilon$$，可得$$\displaystyle \sup_{x \in [0,1] - E_{\epsilon}}\|f_n(x) - f(x)\|=\sup_{x \in [0, 1-\epsilon]}\|x^n  - 0\|=\| 1- \frac{\epsilon}{2}\|^n \rightarrow 0$$ as $$n \rightarrow \infty$$。

### 幾乎處處一致收斂保證幾乎處處收斂



### 範例：幾乎處處收斂，但不依測度收斂

$$f_n(x)=\frac{x}{n}$$ 。則$$f_n(x)$$幾乎處處收斂於$$f(x)=0$$。但不依測度收斂。
