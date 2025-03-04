---
description: Ito integral
---

# Ito積分

## 簡介

布朗運動積分可分為以下類型：

* $$\int_a^b W_t df(t)$$：只有被積分函數(integrand)為布朗運動變數，積分函數為確定函數。
* $$\int_a^b f(t)d W_t$$：同樣只有一個布朗運動變數，由於分部積分性質，可積條件與上式同。
* $$\int_a^b f(W_t)dW_t$$：被積分與積分函數均為布朗運動變數，必須使用Ito積分求解。
* $$\int_a^b f(t,W_t)dW_t$$：被積分與積分函數均為布朗運動變數，必須使用Ito積分求解。

切定義域區間$$[t_{i-1}, t_i]$$，取左端點$$t_i$$定義的積分為Ito積分，取中點$$\frac{t_{i-1}+t_i}{2}$$定義積分為Fisk-Stratonvich積分，取右端點$$t_i$$定義的積分為倒向Ito積分(backward Ito integral)。

## 參考資料

* [https://stats.stackexchange.com/questions/518286/plain-english-explanation-of-itos-integral](https://stats.stackexchange.com/questions/518286/plain-english-explanation-of-itos-integral)
* [https://mathoverflow.net/questions/29750/intuition-and-or-visualisation-of-it%C3%B4-integral-it%C3%B4s-lemma](https://mathoverflow.net/questions/29750/intuition-and-or-visualisation-of-it%C3%B4-integral-it%C3%B4s-lemma)
* [https://zhuanlan.zhihu.com/p/566442832](https://zhuanlan.zhihu.com/p/566442832)
* [https://zhuanlan.zhihu.com/p/138399188](https://zhuanlan.zhihu.com/p/138399188)
