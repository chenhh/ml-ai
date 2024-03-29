# 自然數

## 自然數集合

* 自然數是人類最早認識的數，它有兩個主要功能: <mark style="color:red;">計數與排序</mark>。
* 滿足Peano公理的集合稱為自然數，有些定義自然數會定0開始，即Peano公理的第一項改為0。
* 自然數集合 $$\mathbb{N} = \{1,2,\cdots\}$$
* <mark style="color:red;">自然的計數，且為個數最少的無限(可數)集(因為無限集的充要條件是和自然數集存在1-1的函數)</mark>。

## Peano 公理(Peano axioms)

> 1. <mark style="color:blue;">\[1為自然數)]</mark> $$1 \in \mathbb{N}$$ (有些定義是從0開始，即$$0 \in \mathbb{N}$$)。
> 2. <mark style="color:blue;">\[每個自然數都必定有後繼數]</mark> 若$$n_1 \in \mathbb{N}$$且$$n_2$$ 為$$n_1$$的後繼數(successor,$$n_2 = n_1 ++$$)，則$$n_2 \in \mathbb{N}$$。
> 3. $$1$$<mark style="color:blue;">不為任何自然數的繼數</mark>。
> 4. <mark style="color:blue;">\[兩自然數的後繼數相等時，此兩自然數必相等]</mark> 若$$n_1,m_1 \in \mathbb{N}$$, $$n_2,m_2$$ 分別為$$n_1,m_1$$ 的後繼數，且$$n_2=m_2$$，則$$n_1=m_1$$。
> 5. <mark style="color:blue;">\[數學規納法(mathematical induction)]</mark> 令$$S \subset \mathbb{N}$$, 若$$1 \in S$$, $$n_1 \in S$$且可得出$$n_1$$的後繼數$$n_2 \in S$$，則$$S=\mathbb{N}$$。

根據Peano公設，我們可以為自然數定義加法運算、乘法運算與次序關系，並證明與自然數系相關的各種性質。

再來可證明出整數系$$\mathbb{Z}$$的性質，再由整數系證明有理數系的加法運算、乘法運算與次序關系，且證明有理數系為有序體。

最後再由有理數系證明實數系也滿足此性質。

## 強歸納或第二數學歸納法

假設關於自然數$$n$$的命題$$P(n)$$滿足以下兩個條件：

1. $$P(1)$$成立。
2. 若對於小於自然數$$m$$的所有自然數$$k$$，$$P(k)$$均成立，則$$P(m)$$也成立。

## 正整數的良序性(well-ordering principle)

> 非空的自然數子集(正整數集)必有最小元素。$$\emptyset \neq S \subseteq \mathbb{N} \Rightarrow \exists a \in S \ni \forall x \in S, a \leq x$$

<details>

<summary>proof:</summary>

令$$P(n)$$為以下命題：對於自然數的任意子集，若包含某一自然數$$a \leq n$$，則此集合必包含一最小元素。

考慮集合$$S=\{m \in \mathbb{N} \vert P(m)\}$$，由定義可知$$1 \in S$$。

假設集合$$S$$包含至$$n$$, 欲證明$$S$$亦包含$$n+1$$

令集合$$C \subseteq \mathbb{N}$$且包含某一$$i \leq n+1$$

若$$C$$不包含$$i<n+1$$，則$$i=n+1$$為集合$$C$$的最小元素。

若$$C$$包含某個$$i<n+1$$，則 $$i \leq n$$，由歸納假設知成立。

因此良序性成立(QED)

</details>

註：

* 整數集$$\mathbb{Z}$$在通常序下不是良序集，因該集合本身就沒有一個最小元素。
* 在良序集合中，除了整體上最大的那個元（如果存在的話），則所有的元素都有一個唯一的後繼數：比它大的元素組成的集合中，最小的元素。
