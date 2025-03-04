# 幾乎處處收斂

## 簡介

依測度收斂看的是大局，<mark style="color:blue;">即不限定收斂點是否位於特定的集合當中</mark>，只要最後不收斂的點總數少到幾乎沒有就行；

幾乎處處收斂不僅看大局，還關注細節，在<mark style="color:blue;">一開始就要確定一個“不收斂點集合</mark>$$E_0$$ <mark style="color:blue;">，這個集合中的點個數不僅要少到幾乎沒有，而且集合還得是固定的</mark>。也就是一開始沒在集合上的點之後也得一直收斂，不能突然又不收斂。所以說幾乎處處收斂的要求要比依測度收斂高。

依測度收斂無法保證幾乎處處收斂，因為在依測度收斂的條件下，每個離極限函數比較遠的點全體，此處稱為「壞集合」；壞集合的測度的確是越來越小的，但是你沒辦法控制壞集合的出現的區域，它們依然可以在定義域上漂來漂去，使得你取函數序列尾項的壞集合的聯集，仍然可以是整個定義域。

## 幾乎處處(almost everywhere, a.e.)

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

### 範例：無限測度空間中幾乎處處收斂，但不依測度收斂&#x20;

$$f_n(x)=\frac{x}{n}$$ 。則$$f_n(x)$$幾乎處處收斂於$$f(x)=0$$。但不依測度收斂。



## 有限測度空間中，幾乎處處收斂可得測度收斂



## 參考資料

* [https://proofwiki.org/wiki/Definition:Uniform\_Convergence](https://proofwiki.org/wiki/Definition:Uniform_Convergence)
