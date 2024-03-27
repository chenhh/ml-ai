---
description: chi-distribution
---

# 卡方分佈

## 簡介

常用的三大抽樣分佈之一，t分佈，卡方分佈，F分佈。

假設檢定時，當資料為名目（nominal）變數時，而要檢驗一個自變項對應變項的效果為何，就需要使用到卡方分布。

卡方分布由Pearson提出，由常態分布中所變化出來的，卡方分佈就是標準常態分佈變數$$Z \sim N(0,1)$$的平方所得到。

* 假設從常態分佈$$N(0, 1)$$中，每次獨立抽取一樣本$$z_i$$，令其平方值為隨機變數$$\chi_1^2 = Z^2$$，則$$\chi_1^2$$為自由度為1的卡方分佈。
* 假設從常態分佈$$N(0, 1)$$中，每次獨立抽取二個樣本$$z_i$$，令隨機變數為樣本平方後相加$$\chi_2^2 = \sum_{i=1}^2 Z_i^2$$，則$$\chi_2^2$$為自由度為2的卡方分佈。
* 同理從常態分佈$$N(0, 1)$$中，每次抽取$$k$$個樣本$$z_i$$，令隨機變數為樣本平方後相加$$\chi_k^2 = \sum_{i=1}^k Z_i^2$$，則$$\chi_k^2$$為自由度為$$k$$的卡方分佈。
* 當自由度$$k$$很大時，$$X_k^2$$分佈近似為常態分佈。

設想一個$$k$$維向量$$(X_1,\dots,X_k)$$，每個維度都是按標準常態分佈隨機生成，則從原點到它的長度的平方分佈就是卡方分佈。



## 參考資料

* [https://www.cnblogs.com/think-and-do/p/6509239.html](https://www.cnblogs.com/think-and-do/p/6509239.html)
* [https://www.zhihu.com/question/20358827](https://www.zhihu.com/question/20358827)
* [https://www.zhihu.com/question/332394712](https://www.zhihu.com/question/332394712)
