---
description: maximum entropy
---

# 最大熵

## 簡介

資訊理論在部份資訊的基礎上，建立機率分佈提供了一個標準，並得到一種被稱為最大熵(maximum entropy)的統計推理方法。它是在給定資訊上可能出現的最小偏差的估計。如果我們把統計力學看作是統計推理的一種形式，而不是一種物理理論，可發現從確定分區函數開始，就是最大熵原則的直接結果。無論結果是否與實驗一致，最大熵仍然代表在現有資訊基礎上可以做出的最佳估計。

## 最大熵估計

給定離散隨機變數$$x_i, ~i=1,2,\dots,n$$與對應的發生機率$$p_i$$, $$\sum_{i=1}^n p_i=1$$，則函數$$f(x)$$的期望值為$$\mathrm{E}(f(x))=\sum_{i=1}^n p_i f(x_i)$$

在根據部份資訊下，使用在已經的條件下具有最大熵的機率分佈，這是我們能做出的唯一無偏見的分佈，因為使用其它的分佈都相當於使用了我們不知道的資訊做出的主觀分佈。最大熵有一個重要的特性，即沒有任何的可能性被忽略，對於每一種沒有被給定資訊絕對排除的情況都給於正值，與遍歷的特性相似。



## 參考資料

* Jaynes, Edwin T. "Information theory and statististical mechanics." Physical review 106.4 (1957): 620.
* Jaynes, Edwin T. "Information theory and statistical mechanics. II." Physical review 108.2 (1957): 171.
* Jaynes, Edwin T. "On the rationale of maximum-entropy methods." Proceedings of the IEEE 70.9 (1982): 939-952.
* Jaynes, E. T. "The relation of Bayesian and maximum entropy methods." Maximum-entropy and Bayesian methods in science and engineering. Springer, Dordrecht, 1988. 25-29.
