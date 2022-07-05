---
description: 可接近性理論
---

# Blackwell's Approachability Theorem

## 簡介

對抗性預測的歷史始於數學家David Blackwell和James Hannan的開創性工作。接近性理論起源於Blackwell的工作，並與Hannan的工作同時被發現。 幾十年來，人們對一般凸賽局中的遺憾最小化和Blackwell可接近性之間的關係並不完全瞭解。通常的想法是，事實上，Blackwell可接近性是一個更強的概念。在這一章中，<mark style="color:red;">我們表明可接近性和線上凸最佳化在強烈的意義上是等價的：兩者的演算法是等價的，而且沒有計算效率的損失</mark>。



## Minmax理論

> 給定雙人賽局，玩家1,2的行動集合分別有$$r,s$$個行動，
>
> * 玩家1的混合策略為$$\mathbf{p}=(p_1, p_2, \dots, p_r) \in \mathbf{P}, ~p_i \geq 0, ~ \sum p_i = 1$$。
> * 玩家2的混合策略為$$\mathbf{q}=(q_1, q_2, \dots, q_s) \in \mathbf{Q}, ~q_j \geq 0, ~ \sum q_j = 1$$。
> * $$m(i,j) \in \mathbb{R}$$為玩家1,2採取行動$$i,j$$時，玩家1的報酬(零和遊戲，所以玩家2的報酬為$$-m(i,j)$$)。
>
> 則存在$$\mathbf{p} \in \mathbb{R}_{+}^r, ~ \mathbf{q} \in \mathbb{R}_{+}^s, ~ v \in \mathbb{R}$$ 滿足$$\sum_{i=1}^r p_i m(i, j) \geq v \geq \sum_{j=1}^s q_j m(i,j), ~ \forall i, j$$
>
> * 即玩家1存在一混合策略可保證報酬大於等於$$v$$。
> * 玩家2也存在一混合策略可保證損失不會超過$$v$$。

$$\forall \epsilon > 0$$，在多期雙人零合賽局(報酬矩陣為$$M$$), 當$$t \rightarrow \infty$$，玩家1的報酬會以機率1大於$$v-\epsilon$$，而玩家2的損失會以機率1小於$$v+\epsilon$$。

## 向量報酬

<mark style="color:blue;">單一的混合策略不能確保向量報酬位於某個給定的集合中。然而，這並不排除一個漸進的概念，如果我們允許賽局無限期地重復，並詢問是否存在一種策略來確保平均報酬向量位於某個集合中，或者至少在歐氏距離上接近它。這正是Blackwell提出的解決方案概念</mark>。

在實數中的雙人零和賽局，玩家1、2可依minmax定理逼近賽局的報酬$$v$$。<mark style="color:red;">而在向量報酬中，問題變成玩家1、2是否可逼近一個特定集合</mark>$$S$$。

現在考慮雙人向量(非零和)賽局中，$$m(i,j) \in \mathbb{R}^N$$為向量報酬的情形。報酬矩陣$$\mathbf{M}=[m(i,j)], ~1 \leq i \leq r, ~ 1 \leq j \leq s$$為$$r\times s$$的矩陣，矩陣中每個元素為$$N$$維的向量。

報酬矩陣$$\mathbf{M}$$中的$$r\times s$$個向量點，可形成$$\mathbb{R}^N$$空間中的(有界)凸包(bounded convex hull)，記為$$X \subseteq \mathbb{R}^N$$。

玩家1使用混合策略$$f_n: (x_1, x_2, \dots, x_n) \rightarrow \mathbf{P}, ~x_i \in X$$，其中$$(x_1,x_2,\dots, x_n)$$為到第$$n$$時已觀察到的報酬。

而$$f_0$$因為沒有參考資料，所以為$$\mathbf{P}$$中的任意值，玩家1的混合策略為$$\{f_0, f_1(\mathbf{x}_1), f_2(\mathbf{x}_1, \mathbf{x}_2),f_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$。

同理玩家2的的混合策略為$$\{q_0, q_1(\mathbf{x}_1), q_2(\mathbf{x}_1, \mathbf{x}_2),q_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3) , \dots \}$$

注意此處報酬是使用\$$\第第第



。令$$S \subseteq \mathbb{R}^N$$為任意集合。





## 參考資料

* <mark style="background-color:red;">\[\*\*\*]Blackwell, David. "An analog of the minimax theorem for vector payoffs." Pacific Journal of Mathematics 6.1 (1956): 1-8</mark>.
* <mark style="background-color:red;">Hannan, James. "Approximation to Bayes risk in repeated play." Contributions to the Theory of Games 3.2 (1957): 97-139</mark>.
* Abernethy, Jacob, Peter L. Bartlett, and Elad Hazan. "Blackwell approachability and no-regret learning are equivalent." Proceedings of the 24th Annual Conference on Learning Theory. JMLR Workshop and Conference Proceedings, 2011.
