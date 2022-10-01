---
description: measurable function
---

# 可測函數

## 可測函數定義

> 函數$$f: X \rightarrow \overline{\mathbb{R}}$$，$$(X, \Sigma)$$為可測空間，$$\overline{\mathbb{R}}=\mathbb{R}\cup\{\pm \infty\}$$為擴充實數集合。
>
> 對於實數上的任意開集合$$E\subseteq \mathbb{R}$$，若前像$$f^{-1}(E)=\{x \in X~|~f(x)\in E\} \in \Sigma$$且$$f^{-1}(\{+\infty\}) \in \Sigma$$，$$f^{-1}(\{-\infty\}) \in \Sigma,$$，則稱$$f$$為可測函數。

可測函數$$f$$在機率空間$$(X,\mathbb{F}, P)$$中為隨機變數。

## 可測函數的等價條件

> $$f: X \rightarrow \overline{\mathbb{R}}$$，則以下條件均等價：
>
> 1. $$f$$為可測函數
> 2. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c))=\{x \in X~|~ f(x)<c \} \in \Sigma$$
> 3. $$\forall c \in \mathbb{R}$$，$$f^{-1}((-\infty, c])=\{x \in X~|~ f(x)\leq c \} \in \Sigma$$
> 4. $$\forall c \in \mathbb{R}$$，$$f^{-1}((c, \infty))=\{x \in X~|~ f(x)>c \} \in \Sigma$$
> 5. $$\forall \in \mathbb{R}$$，$$f^{-1}([c, \infty))=\{x \in X~|~ f(x) \geq c \} \in \Sigma$$
> 6. $$f^{-1}(B) \in \mathbb{B}$$為Borel set(由實數上所有開(閉)區間形成的最小的sigma域)。

proof 1-> 2:

因為$$f$$為可測函數，由定義得給定$$c \in \mathbb{R}$$，$$f^{-1}(c) \in \Sigma$$，同理$$\forall d < c$$，$$f^{-1}(d) \in \Sigma$$。

因為$$\Sigma$$定義集合內任意元素的聯集仍為$$\Sigma$$內的元素，因此$$f^{-1}(c \cup d) \in \Sigma$$ (QED)

proof 2-> 3 (用開區間逼近閉區間)

$$(-\infty, c]=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})$$

由$$\Sigma$$的定義得$$f^{-1}((-\infty, c])=\bigcap_{n=1}^\infty (-\infty, c+\frac{1}{n})\in \Sigma$$ (QED)

proof 3->4 (補集)

$$f^{-1}((c, \infty))=f^{-1}((\mathbb{R} - (-\infty, c])=\mathbb{R}-f^{-1}((-\infty, c]) \in \Sigma$$ (QED)

proof 4->5 (用開區間逼近閉區間)

$$f^{-1}([c, \infty)=f^{-1}(\bigcap_{n=1}^\infty (c - \frac{1}{n}, \infty))=\bigcap_{n=1}^\infty f^{-1}(c-\frac{1}{n}, \infty) \in \Sigma$$ (QED)

