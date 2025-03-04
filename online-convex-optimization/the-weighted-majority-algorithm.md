---
description: 加權多數演算法
---

# the weighted majority algorithm

## 簡介

已知專家(演算法)集合$$\mathcal{P}$$，共做出$$T$$期的預測，其中預測最好的專家(但事先不知道是那一個專家)總共犯錯$$m$$次，而加權多數決演算法可保證最多犯$$c(\log|P|+m)$$次錯誤，$$P=|\mathcal{P}|$$且$$c$$為固定的常數。

每次試驗的總體流程如下： 池中的所有演算法都會收到相同的實例。每個演算法都會做出預測，然後將這些預測組合在一起，形成一個實例，饋送給主演算法。然後，主演算法做出預測並獲得一個標籤，並將其傳遞給整個演算法池。我們對實例和標籤的選擇不做任何概率假設；也就是說，我們在本文中證明的關於各種演算法預測性能的界限，都是在實例和標籤的最壞情況序列下成立的。

我們的目標可以看作是構建一種學習演算法，學會利用輸入中的模式來減少錯誤。我們提出的演算法組合方案具有通用性，即無論演算法庫中有哪些類型的模式可以處理，這些模式都可以由由此產生的演算法組合來處理。我們提供兩種結果：相對結果和絕對結果。相對結果給出了主演算法的錯誤數與演算法池成員錯誤數的函數關係；這些結果不依賴於演算法所處理模式的任何細節。要應用相對結果，我們首先要建立一個演算法庫，其中包含一個或多個成員，能夠處理我們面臨的任何輸入而不會出現很多錯誤。如果這個演算法庫不大，那麼將主演算法應用於演算法庫所形成的組合演算法就不會犯很多錯誤。此外，如果演算法池中的所有演算法都是高效的，而且演算法池足夠小，那麼產生的演算法將是高效的。

對於絕對結果，我們會對輸入做出特定的假設，並尋找在這些假設條件下表現良好的集合。我們特別關注學習者所看到的資訊模式，其中標籤（通常）在功能上取決於實例。從實例映射到標籤的函數稱為目標函數。如果試驗的標籤是由試驗實例的值 給出的，我們就說該試驗符合特定的目標函數 f。給定一類潛在的目標函數（目標類），我們感興趣的演算法是，當遇到與從該類中選擇的目標函數相一致的任何試驗序列時，能很少犯錯的演算法。有時，我們也會給目標類添加額外的結構，要求演算法對一類函數中的某些函數（例如，我們認為比較簡單的函數）所犯的錯誤少於對其他函數所犯的錯誤。在本文中，我們將討論通過將主演算法應用於為給定目標類量身定制的池，為各種目標類構建此類演算法。

## 參考資料

#### 論文

* Nick Littlestone and Manfred K. Warmuth,  "The weighted majority algorithm," Information and computation, Vol. 108, Issue 2, pp. 212-261, 1994.&#x20;

#### 網頁

* [wikipedia](https://en.wikipedia.org/wiki/Weighted_majority_algorithm_\(machine_learning\))
* [https://zhuanlan.zhihu.com/p/47423225](https://zhuanlan.zhihu.com/p/47423225)
* [https://blog.csdn.net/weixin\_43781565/article/details/106728380](https://blog.csdn.net/weixin_43781565/article/details/106728380)
* [https://www.zhihu.com/question/27940474/answer/621217738](https://www.zhihu.com/question/27940474/answer/621217738)
* [https://www.lesswrong.com/posts/AAqTP6Q5aeWnoAYr4/the-weighted-majority-algorithm](https://www.lesswrong.com/posts/AAqTP6Q5aeWnoAYr4/the-weighted-majority-algorithm)
* [https://blog.csdn.net/TgqDT3gGaMdkHasLZv/article/details/78876242?spm=1001.2101.3001.6650.6\&utm\_medium=distribute.pc\_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78876242-blog-106728380.235%5Ev38%5Epc\_relevant\_sort\&depth\_1-utm\_source=distribute.pc\_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78876242-blog-106728380.235%5Ev38%5Epc\_relevant\_sort\&utm\_relevant\_index=7](https://blog.csdn.net/TgqDT3gGaMdkHasLZv/article/details/78876242?spm=1001.2101.3001.6650.6\&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78876242-blog-106728380.235%5Ev38%5Epc_relevant_sort\&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-78876242-blog-106728380.235%5Ev38%5Epc_relevant_sort\&utm_relevant_index=7)
