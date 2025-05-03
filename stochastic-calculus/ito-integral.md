---
description: Ito integral
---

# Ito積分

## 簡介

伊藤積分（Itô Integral）用於定義對布朗運動（Wiener Process）或其他隨機過程的積分。它由日本數學家伊藤清（Kiyoshi Itô）於1940年代提出，是分析隨機微分方程（SDE）和金融數學（如布萊克-斯科爾斯模型）的基礎。與普通黎曼積分不同，伊藤積分處理的是隨機過程的不規則性質，特別是布朗運動的非平滑性和無限變差。

在傳統的 Riemann 積分或 Lebesgue 積分中，積分的對象(被積函數, integrand)是確定性的函數，積分(函數, integrator)是關於一個確定性的測度（例如時間或空間）。在隨機分析中，我們經常需要對那些本身就是隨機過程的函數，關於另一個隨機過程（特別是像布朗運動這樣具有高度不規則性的過程）進行積分。由於布朗運動的路徑幾乎處處不可微，傳統的積分定義在這裡失效。

與傳統積分的一個重要區別在於，<mark style="color:red;">Itô 積分的定義中，在劃分時間區間時，被積函數的值是取在區間的</mark><mark style="color:red;">**左端點**</mark>。這種選擇方式雖然看似有些不自然，但它確保了 Itô 積分具有一些良好的性質，例如它是鞅（Martingale）的性質（在特定條件下)。

而Stratonovich積分使用區間中點，適用於物理系統，但失去鞅性質，與伊藤積分可相互轉換。



伊藤積分可分為以下類型：

* $$\int_a^b B_t df(t)$$：只有被積分函數(integrand)為布朗運動變數，積分函數為確定函數。
* $$\int_a^b f(t)d B_t$$：同樣只有一個布朗運動變數，由於分部積分性質，可積條件與上式同。
* $$\int_a^b f(B_t)dB_t$$：被積分與積分函數均為布朗運動變數，必須使用Ito積分求解。
* $$\int_a^b f(t,B_t)dB_t$$：被積分與積分函數均為布朗運動變數，必須使用Ito積分求解。

切定義域區間$$[t_{i-1}, t_i]$$，取左端點$$t_i$$定義的積分為Ito積分，取中點$$\frac{t_{i-1}+t_i}{2}$$定義積分為Fisk-Stratonvich積分，取右端點$$t_i$$定義的積分為倒向Ito積分(backward Ito integral)。

對於一個時間區間$$[0,T]$$，假設函數$$f(t)$$適應於布朗運動$$B_t$$ (即$$f(t)$$在時間$$t$$只依賴於$$B_s, s \leq t$$)且滿足平方可積條件$$\mathrm{E}(\int_0^T f^2(t) dt) < \infty$$，伊藤積分定義為：

$$\displaystyle \int_0^T f(t) dB_t = \lim_{n \to \infty} f(t_{i-1})(B_{t_i} - B_{t_{i-1}})$$

* $$t_i = i \cdot \frac{T}{n}$$是$$[0,T]$$的均勻分割。
* 積分點選左端點$$f({t_{i-1}})$$，這使得伊藤積分是非預期性（non-anticipating）的，符合隨機過程的因果性。

## 主要性質

### 鞅性質（Martingale Property)

### 伊藤同態公式（Itô Isometry）

### 二次變差（Quadratic Variation）

### 非標準鏈式法則

## 參考資料

* [https://stats.stackexchange.com/questions/518286/plain-english-explanation-of-itos-integral](https://stats.stackexchange.com/questions/518286/plain-english-explanation-of-itos-integral)
* [https://mathoverflow.net/questions/29750/intuition-and-or-visualisation-of-it%C3%B4-integral-it%C3%B4s-lemma](https://mathoverflow.net/questions/29750/intuition-and-or-visualisation-of-it%C3%B4-integral-it%C3%B4s-lemma)
* [https://zhuanlan.zhihu.com/p/566442832](https://zhuanlan.zhihu.com/p/566442832)
* [https://zhuanlan.zhihu.com/p/138399188](https://zhuanlan.zhihu.com/p/138399188)
