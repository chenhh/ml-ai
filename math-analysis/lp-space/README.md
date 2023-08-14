# Lp空間

## 簡介

考慮測度空間 $$(X, \mathcal{F}, \mu)$$，一個廣義實值函數函數$$f: E \rightarrow \overline{\mathbb{R}}$$ 為$$E$$上的可測函數。

定義<mark style="color:red;">p範數</mark> $$\displaystyle  \|f\|_p = \left( \int_E |f(x)|^p d\mu(x)\right)^{\frac{1}{p}}, ~ 0 < p < \infty$$，此處$$p$$為正實數值而不是自然數。

但此定義嚴格來說上式子並不滿足範數的定義， 因為它的計算值可能是無窮大，且也不能得到$$\|f\|_p=0 \Rightarrow f=0$$ 的結論。因此必須再加上其它條件。

## Lp空間

令集合$$E$$上的可積函數集合為$$L(E)$$。

記$$L^p(X, \mathcal{F}, \mu)=\{ f \in L(E) ~|~ \|f\|_p < \infty\}, ~ 0<p < \infty$$為Lp空間。

定義$$\|f\|_\infty= \inf \{ M \in \mathbb{R}^+ ~|~ f < M \text{ a.e. }  \}$$與$$L^\infty(X, \mathcal{F}, \mu)=\{ f \in L(E) ~|~ \|f\|_\infty < \infty\}, ~ 0<p < \infty$$。

$$L^p(X, \mathcal{F}, \mu)$$與$$L^\infty(X, \mathcal{F}, \mu)$$統稱為Lp空間, 我們感興趣的是$$1 \leq p < \infty$$ 的情形。

## Holder不等式

> 共軛指標
>
> 若$$p,q \geq 1$$且滿足$$\frac{1}{p}+\frac{1}{q} = 1$$，則稱$$p,q$$為共軛指標。
>
> 可定義$$p=1$$時，$$q=\infty$$。

> Holder不等式
>
> $$p,q$$為共軛指標，$$1 \leq p \leq \infty$$且$$f \in L^p(E), g \in L^q(E)$$，可得
>
> $$\|fg\|_1 \leq \|f\|_p \|g\|_q$$。

$$p=q=2$$<mark style="color:red;">稱，Holder不等式為Schawarz不等式</mark>。

$$\displaystyle  \int_E |f(x) g(x) | \leq  \left( \int_E |f(x)|^2 dx \right)^{\frac{1}{2}} \left( \int_E |g(x)|^2 dx \right)^{\frac{1}{2}}$$

## Minkowski不等式

若$$f,g \in L^p(E), ~ 1 \leq p \leq \infty$$，則$$\|f+g\|_p \leq \|f\|_p + \|g\|_p$$。
