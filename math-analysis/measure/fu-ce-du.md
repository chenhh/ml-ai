---
description: complex measure
---

# 複測度

## 簡介



## 複測度(complex measure)

> 給定可測空間$$(X, \Sigma)$$，複測度$$\mu: \Sigma \rightarrow \mathbb{C}$$滿足σ可加性：
>
> * $$\forall E_n \in \Sigma, ~ E=\bigcup_{n=1}^\infty E_n, E_i \cap E_j =\emptyset, \forall i \neq j$$則，$$\displaystyle \mu(E)=\sum_{n=1}^\infty \mu(E_n) \in \mathbb{C}$$。(因為不為無窮大，且對於$$E_n$$的任意排列均收斂，因此級數為絕對收斂)。

滿足σ可加性時，可得$$\mu(\emptyset)=0$$。因為$$\emptyset=\emptyset \cup \emptyset$$。得$$\mu(\emptyset)=2\mu(\emptyset) \in \mathbb{C} \implies \mu(\emptyset)=0$$。

而複測度$$\mu$$可寫成實數與虛數兩個符號測度，$$\mu=\mu_r+i\mu_i$$，其中$$\mu_r, \mu_i$$為符號測度。

由定義可知$$\mu$$的值域為複數，因此不包含$$\infty$$<mark style="color:red;">。即</mark>$$\mu$$<mark style="color:red;">的值域必然是包含在複平面上某個半徑有限的圓盤內 (disc of finite radius) - 這一性質也被稱為有界變差 ( bounded variation)</mark>。許多定理可以直接從符號測度推廣到複測度上，且定理的條件自動滿足。

### 複測度: 複數函數的積分

給定$$(X, \Sigma, \mu)$$為σ-finite測度空間。$$f:X \rightarrow \mathbb{C}$$為可積分函數。定義複測度為函數的積分：$$\displaystyle \mu(E)=\int_E f d\mu = \int_E f d\mu_r +i \int_E f d\mu_i$$。

## 複測度的全變差測度

> $$\mu: \Sigma \rightarrow \mathbb{C}$$為複測度，則全變差測度定義為：
>
> $$\displaystyle |\mu|(E)=\sup_{\{E_i\} \in \mathbf{E}} \sum_{i=1}^\infty |\mu(E_i)|$$。
>
> 其中$$\displaystyle \bigcup_{i=1}^\infty E_i = E, ~ E_i \cap E_j = \emptyset ~ \forall i \neq j$$為$$E$$的可數分割。
>
> $$|\mu|: \Sigma \rightarrow [0, \infty)$$<mark style="color:red;">為有限正測度</mark>。

註：在\[符號測度/有限符號測度的Jordan分解是測度的最小上界/最大下界]已經證明過此性質。

可得$$|\mu(E)| \leq |\mu|(E), \forall E \in \Sigma$$。

* 因為$$\{E, \emptyset, \emptyset, \cdots\}$$形成一組$$E$$的可數分割。由定義得$$|\mu|(E) \geq \|\mu(E)|+\sum_{n=2}^\infty |\mu(\emptyset)|=|\mu(E)|$$

## 複測度的全變差測度為有限正測度

> 要分成兩部份證明：
>
> 1. 全變差測度為正測度。
> 2. 全變差測度為有限正測度。

##



## 參考資料

* [https://en.wikipedia.org/wiki/Complex\_measure](https://en.wikipedia.org/wiki/Complex\_measure)
* [https://zhuanlan.zhihu.com/p/71775089](https://zhuanlan.zhihu.com/p/71775089)
* [https://math.stackexchange.com/questions/3788084/applications-of-signed-complex-measures](https://math.stackexchange.com/questions/3788084/applications-of-signed-complex-measures)
