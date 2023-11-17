---
description: topological space
---

# 拓樸空間

## 簡介

度量空間$$(X,d)$$，開集合$$E$$包含了所有內點，且可數個開集合的聯集仍為開集合，有限個開集合的聯集仍為開集合。

而拓樸空間使用開集合的性質，定義了更一般化的空間。類似於σ代數，<mark style="color:red;">只使用開集合的聯集與交集性質定義拓樸(topology)，而不需使用度量</mark>$$d$$。

拓撲空間賦予「一點附近」這個概念的抽象數學結構，由此可以定義出如收斂、連通、連續等概念。

## 拓樸(topology)

> 給定集合$$X$$，拓樸$$\mathcal{T}$$為滿足以下條件的集合族(開集合公理):
>
> 1. \[空集合/宇集合均同時為開/閉集合]$$\emptyset \in \mathcal{T}$$、$$X \in \mathcal{T}$$。
> 2. \[可數集合聯集的封閉性]$$E_i \in \mathcal{T}, \forall i \in \mathbb{N}$$，則可數聯集仍為拓樸中的元素，$$\bigcup_{i \in \mathbb{N}} E_i \in \mathcal{T}$$。
> 3. \[有限集合交集的封閉性]$$E_i \in \mathcal{T}, i=1,2,\dots,n$$，則有限交集仍為拓樸中的元素$$\bigcap_{i=1}^n E_i \in \mathcal{T}$$。
>
> 註：由於開集合的補集為閉集合，也可以用閉集合定義。

$$(X, \mathcal{T})$$<mark style="color:red;">稱為拓樸空間</mark>，且稱元素$$E \in \mathcal{T}$$為開集合。

若$$x \in X$$且$$E \subseteq X, ~ E \in \mathcal{T}$$滿足$$x \in E$$，則稱$$E$$為$$x$$的<mark style="color:red;">開鄰域(open neighborhood</mark>)。

### 拓樸和σ代數的比較

集合$$X$$的σ代數$$\Sigma$$滿足：

1. $$\emptyset \in \Sigma$$。
2. $$\forall E \in \Sigma \implies E^c \in \Sigma$$。
3. $$\forall E_i \in \Sigma, ~i \in \mathbb{N} \implies \bigcup_{i \in \mathbb{N}} E_i \in \Sigma$$。

## 參考資料

* [台灣師範大學數學系: 拓樸導論](https://www.google.com.tw/url?sa=t\&rct=j\&q=\&esrc=s\&source=web\&cd=\&cad=rja\&uact=8\&ved=2ahUKEwi3qabdvMqCAxWMd\_UHHSErAQMQFnoECAoQAQ\&url=https%3A%2F%2Fmath.ntnu.edu.tw%2F\~li%2FTopology%2FTopology.pdf\&usg=AOvVaw0RhUQulup4SZA2j3iomw4U\&opi=89978449)。
* [https://zh.wikipedia.org/zh-tw/%E6%8B%93%E6%89%91%E7%A9%BA%E9%97%B4](https://zh.wikipedia.org/zh-tw/%E6%8B%93%E6%89%91%E7%A9%BA%E9%97%B4)

