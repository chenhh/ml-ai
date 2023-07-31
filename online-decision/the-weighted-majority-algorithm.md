---
description: 加權多數演算法
---

# the weighted majority algorithm

加權多數演算法最初為所有專家分配相同的權重 1。在每一輪中，我們都會詢問所有專家的預測，並對兩種可能的預測（“正”或“負”）的權重求和。我們輸出具有較高權重的預測。然後，當我們看到實際結果時，我們將每個預測錯誤的專家的權重乘以 1/2。

假設專家總數為n，並且最好的專家在給定的取樣序列上犯的錯誤不超過m。然後我們可以證明加權多數演算法的錯誤總數為M，其界限為2.41\*(m + log2(n))。換句話說，加權多數演算法所犯的錯誤不會比最佳專家多，加上 log n因子乘以常數因子 2.41。

## 參考資料

#### 論文

* Nick Littlestone and Manfred K. Warmuth,  "The weighted majority algorithm," Information and computation, Vol. 108, Issue 2, pp. 212-261, 1994.&#x20;

#### 網頁

* [wikipedia](https://en.wikipedia.org/wiki/Weighted\_majority\_algorithm\_\(machine\_learning\))
* [https://zhuanlan.zhihu.com/p/47423225](https://zhuanlan.zhihu.com/p/47423225)
* [https://blog.csdn.net/weixin\_43781565/article/details/106728380](https://blog.csdn.net/weixin\_43781565/article/details/106728380)
* [https://www.zhihu.com/question/27940474/answer/621217738](https://www.zhihu.com/question/27940474/answer/621217738)
* [https://www.lesswrong.com/posts/AAqTP6Q5aeWnoAYr4/the-weighted-majority-algorithm](https://www.lesswrong.com/posts/AAqTP6Q5aeWnoAYr4/the-weighted-majority-algorithm)
