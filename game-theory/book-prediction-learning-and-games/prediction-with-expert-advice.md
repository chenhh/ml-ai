---
description: prediction with expert advice
---

# 以專家的建議預測

## 架構簡介

決策者的目標是預測未知序列的元素$$y_1, y_2, \dots$$，其中$$y_t \in \mathcal{Y}$$為出像空間(outcome space)。

而決策者的預測值$$\hat{p}_1, \hat{p}_2,\dots$$，其中$$\hat{p}_t \in \mathcal{D}$$為決策空間(decision space)，通常假設為向量空間中的凸集合。

在一些特殊的應用中，會假設$$\mathcal{Y} = \mathcal{D}$$，但在一般的情形下，通常$$\mathcal{Y} \neq \mathcal{D}$$。

決策者以順序方式計算其預測值，並將其預測結果與一組參考專家的預測結果進行比較。

<mark style="background-color:orange;">更準確的說，在時間</mark>$$t$$<mark style="background-color:orange;">，決策者可參考一群專家的預測值</mark>$$\{f_{E, t} \in \mathcal{D}, ~\forall E \in \mathcal{E}\}$$<mark style="background-color:orange;">。而決策者在參考專家們的預測後，再計算出自已的預測值</mark>$$\hat{p}_t$$<mark style="background-color:orange;">，之後才得到結果</mark>$$y_t$$<mark style="background-color:orange;">。</mark>

使用非負的損失函數(loss function)$$\mathcal{l}: \mathcal{D} \times \mathcal{Y} \rightarrow \mathbb{R}^{+}$$$$\mathbb{}$$計算決策者和專家們的預測性能。

在此架構下，可視為決策者(給出預測值$$\hat{p}_t$$)與環境(給出專家們的建議$$\{f_{E,t}, ~ \forall E \in \mathcal{E}\}$$與給出結果$$y_t$$)的重複賽局。

