---
description: >-
  Dean P. Foster and Rakesh Vohra. "Regret in the on-line decision problem."
  Games and Economic Behavior Vol. 29, No. 1-2, pp 7-35, 1999.
---

# paper: Regret in the On-Line Decision Problem

## 摘要

決策者在每個時間點都必須做出決策。一個時間點內因決策而獲得的報酬，取決於決策以及當時所處的世界狀態(state of world)。困難的是，決策必須在事先做出，甚至在對哪個世界狀態會出現的機率知識都沒有的情況下(無先驗)。各種學科的一系列問題都可以用這種方式來構建。在本文中，我們概述了獲得的主要結果，以及它們的一些應用。

<mark style="color:red;">註：本論文給出如何使用Blackwell approachability theorem計算在online decision problem中，保證有最小內部遺憾的演算法，而且有簡單的範例</mark>。

## 簡介

決策者在每個離散時間點$$t$$都必須做決策$$d_t$$(尚未知道世界狀態$$X_t$$)，之後得到損失$$L(d_t,X_t)$$是由已做出的決策$$d_t$$與當時的世界狀態$$X_t$$所決定。假設$$0\leq L(d_t, X_t ) < \infty$$。

決策者的目標是做出好的決策$$\{d_t\}_{t \geq 0}$$以最小化長期損失，即$$\min \sum_{t=0}^T L(d_t, X_t)$$，稱之為綀上決策問題(online decision problem, ODP)。

ODP 的定義尚未完全明確，將在後續章節中詳細闡述。<mark style="color:red;background-color:red;">與計算機科學中常見的線上問題不同，ODP 的關鍵特徵在於每個時期的損失與過去的決策無關</mark>。

ODP 具有廣泛的應用性，並以預測 0 和 1 序列的問題為例，解釋了如何將實際問題構建為 ODP。在這個例子中，決策者需要在每個時期預測 0 或 1，目標是最小化錯誤預測的次數。 ODP 在統計學、計算機科學等多個領域的研究歷史，這些研究在很大程度上是獨立進行的。

ODP 中決策者的初步目標是最小化總損失，但總損失的多少取決於實際發生的世界狀態序列。通過一個簡單的預測策略 (總是預測 1) 來說明，簡單策略的有效性會因應不同的狀態序列而異。因此，文章強調，需要設計能夠在多種不同的狀態序列下(註：考慮所有可能發生的狀態，不做機率分佈估計預測)都能維持較低平均損失的決策方案。

簡單的想法是考慮最差情況下的總損失$$\max_{t=0}^T L(d_t, X_t)$$，此處最大化是考慮所有可能世界狀態的序列，再想辦法最小化總損失，但此方法沒什麼用。

以 0-1 預測問題為例，對於任何確定性的預測方案，都存在一個 0 和 1 的序列，使得該方案永遠無法做出正確的預測。 因此，對於每個確定性的預測方案，時間平均損失在所有序列上的最大值都將是 1。

簡而言之，單純追求在最壞情況下（所有可能的世界狀態序列中）最小化總損失的目標是不切實際的，因為確定性策略容易被針對，導致在某些情況下表現極差。

如果我們不堅持使用確定性的預測方案，那麼顯然有一個解決方法，那就是隨機化。 因此，總損失$$\sum_{t=0}^T L(d_t,X_t)$$ 就會變成一個隨機變數。因此最差情況下變為期望總損失$$\max \mathrm{E}(\sum_{t=0}^T L(d_t, X_t))$$。

通過隨機化，預測方案不再是固定的，而是具有不確定性的。 這使得對手 (或者說「世界狀態序列」) 更難以針對性地制定策略來使你的預測方案表現糟糕。

不幸的是，隨機化方案所能達到的最佳結果是每回合平均損失 1/2。 當決策者在每回合以 50/50 的機率進行隨機化時，就能達到這個結果。 <mark style="color:red;">由於要找到一個方案，使其最大化期望總損失 小於 T/2 是不可能的</mark>，<mark style="color:red;">因此，另一種替代方法是通過與其他方案進行比較來衡量決策方案的成功程度</mark>。

&#x20;想像一下，我們已經有一系列可用的決策方案 F。 如果 S 是一個新的方案。 如果 S 的總損失與 F 中最佳方案的總損失 “相當”，那麼人們就會認為 S 是有吸引力的；無論實際出現什麼樣的世界狀態序列。

可比性的概念是基於外部有效性的概念來判斷一個方案的；也就是說，它是否與其他方案一樣好？ 在本文中，我們介紹了另一種替代方案，這種方案是基於方案的內部一致性來判斷方案的。 我們還將在內部一致性的概念和可比性的某種版本之間建立密切的聯繫，從而使我們能夠以統一的方式推導出幾個已知的結果。

## 遺憾(regret)

當我們意識到如果我們做了別的事情會更好時，我們就會感到遺憾。 任何方案的基本要求是，它應該避免或至少減少將會感受到的遺憾。&#x20;

令$$D = \{d_1, d_2, \dots, d_n\}$$ 為每個時間段中可能的決策集合。 將在時間$$t$$ 採取決策$$d_j$$ 所產生的損失記為$$L_t^j<\infty$$。 我們始終假設損失是有界的；為了簡化符號，假設對於所有$$d_j \in D$$ 和$$t \geq 0$$，$$L_t^j \leq 1$$。 請注意，我們在這裡省略了對時間 t 發生的世界狀態的依賴性。

任何用於選擇決策的方案（確定性的或隨機的）都可以用在時間$$t$$ 選擇決策$$j$$ 的機率$$w_t^j$$ 來描述。 讓$$w_t$$ 表示時間$$t$$ 的$$n$$ 元組機率。 <mark style="color:red;">請記住，</mark>$$w_t$$ <mark style="color:red;">必須僅使用在時間</mark> $$t-1$$ <mark style="color:red;">之前獲得的數據來推導出來</mark>。

現在考慮一個用於選擇決策的隨機方案$$S$$。 設$$\{w_t\}_{t \geq 0}$$ 為該方案所隱含的機率權重序列。 那麼，使用方案$$S$$ 在$$T$$個時期內的期望損失將為：$$\displaystyle L(S) = \sum_{t=1}^T \sum_{d_j \in D} w_t^j L_t^j$$。

想像一下，我們已經將方案$$S$$應用了$$T$$個時期。 現在，我們回顧並檢查我們的表現。 如果我們以不同的方式做事，我們是否有可能獲得更小的損失？ 具體來說，在方案$$S$$ 說我們應該以機率$$w_t^j$$ 選擇決策$$d_j$$ 的每個時間點$$t$$，如果我們改選擇決策$$d_i$$，我們會做得更好嗎？

期望損失會變為：$$\displaystyle L(S) - \left( \sum_{t=1}^T w_t^j L_t^j - \sum_{t=1}^T w_t^j L_t^i  \right)$$。

如果$$\displaystyle     \sum_{t=1}^T w_t^j L_t^j - \sum_{t=1}^T w_t^j L_t^i =   \sum_{t=1}^T w_t^j(L_t^j - L_t^i)  >0$$，則表示決策$$d_j$$換成$$d_i$$會表現更好(對決策$$d_j$$而不是$$d_i$$感到遺憾)。

因此定義方案$$S$$使用決策$$d_j$$的遺憾為：$$\displaystyle R_T^j(S) = \sum_{i \in D} \max \left\{  0,  \sum_{t=1}^T w_t^j (L_t^j - L_t^i)  \right\}$$。

而方案$$S$$的遺憾為$$R_T(S) = \sum_{j \in D} R_T^j (S)$$。

<mark style="color:red;">若方案</mark>$$S$$<mark style="color:red;">的期望遺憾非常小，即</mark>$$R_T(S) = o(T)$$<mark style="color:red;">，則稱方案</mark>$$S$$<mark style="color:red;">無內部遺憾(no internal regret)</mark>。即$$\displaystyle \lim_{T \rightarrow \infty} \frac{R_T(S)}{T} =0$$。

無內部遺憾方案的存在性首先由 Foster 和 Vohra (1998) 確立。 在這裡描述的證明歸功於 Hart 和 Mas-Collel (1996)，並使用了線上決策問題中的後悔概念以及 David Blackwell 的approachability定理。

## 考慮只有兩個決策的情形

定義指示函數(indicator) $$I(j,t)= \begin{cases} 1 &  d_j \text{ chosen at time } t. \\ 0 & \text{ else} \end{cases}$$

定義從決策$$d_j$$換為$$d_i$$的已實現成對遺憾(realied pairwise regret)為：$$\displaystyle R_T^{j \rightarrow i}(S) = \sum_{t=1}^T I(j,t)L_t^j - \sum_{t=1}^T I(j,t) L_t^i$$

* $$R_T^{j \rightarrow i}(S) >0$$表示決策$$d_j$$換成$$d_i$$比較好($$d_i$$優於$$d_j$$)。
* $$R_T^{j \rightarrow i}(S) =0$$表示$$d_i$$與$$d_j$$表現一樣好。
* $$R_T^{j \rightarrow i}(S)<0$$表示決策$$d_j$$比$$d_i$$好，不應更換決策。

由定義得$$R_T^{i \rightarrow i}(S) =0$$。期望值為$$\displaystyle \mathbb{E}(R_T^{j \rightarrow i}(S)) = \sum_{t=1}^T w_t^j (L_t^j - L_t^i)$$。

註：方案$$S$$中，可能只有部份時間的決策為$$d_j$$，如果選$$d_j$$時換成選$$d_i$$時的遺憾。

<mark style="color:red;">我們的目標是找出無內部遺憾的隨機化的方案</mark>$$S$$。

首先考慮$$|D|=2$$的情形。只需考慮$$R_T^{1 \rightarrow 0}(S), R_T^{0 \rightarrow 1}(S)$$即可，其餘兩種遺憾為0。

定義賽局和目標集合如下：

* 決策者在時間$$t$$，使用策略0(決策$$d_0$$)的向量報酬(payoff)為$$(L_t^0- L_t^1, 0)$$。
* 決策者在時間$$t$$，使用策略1(決策$$d_1$$)的向量報酬(payoff)為$$(0, L_t^1- L_t^0)$$。

假設決策者使用(隨機)方案$$S$$在時間$$t$$以機率$$w_t$$選擇策略0，則$$T$$期後的實現平均報酬為：$$\displaystyle \left( \frac{\sum_{t=1}^T w_t (L_t^0- L_t^1)}{T}, \frac{\sum_{t=1}^T (1-w_t) (L_t^1- L_t^0)}{T}  \right) =   \left( \frac{R_T^{0 \rightarrow 1}(S)}{T}, \frac{R_T^{1 \rightarrow 0}(S)}{T}  \right)$$

因為我們的目標是無內部遺憾，因此<mark style="color:red;background-color:red;">目標集合為第三象限</mark>。
