---
description: prediction with expert advice
---

# 以專家的建議預測

## 架構簡介

決策者的目標是預測未知序列的元素$$y_1, y_2, \dots$$，其中$$y_t \in \mathcal{Y}$$為出像空間(outcome space)。

而決策者的預測值$$\hat{p}_1, \hat{p}_2,\dots$$，其中$$\hat{p}_t \in \mathcal{D}$$為決策空間(decision space)，通常假設為向量空間中的凸集合。

在一些特殊的應用中，會假設$$\mathcal{Y} = \mathcal{D}$$，但在一般的情形下，通常$$\mathcal{Y} \neq \mathcal{D}$$。

決策者以順序方式計算其預測值，並將其預測結果與一組參考專家的預測結果進行比較。

<mark style="background-color:orange;">更準確的說，在時間</mark>$$t$$<mark style="background-color:orange;">，決策者可參考一群專家的預測值</mark>$$\{f_{E, t} \in \mathcal{D}, ~\forall E \in \mathcal{E}\}$$<mark style="background-color:orange;">。而決策者在參考專家們的預測後，再計算出自已的預測值</mark>$$\hat{p}_t$$<mark style="background-color:orange;">，之後才得到結果</mark>$$y_t$$(註：此處限制$$y_t$$必須在$$\hat{p}_t$$之前就先決定了，只是決策者未知其值，以避免$$y_t$$參考$$\hat{p}_t$$的值總是給出相反的答案)<mark style="background-color:orange;">。</mark>

使用非負的損失函數(loss function)$$\mathcal{l}: \mathcal{D} \times \mathcal{Y} \rightarrow \mathbb{R}^{+}$$$$\mathbb{}$$計算決策者和專家們的預測性能。

在此架構下，可視為決策者(給出預測值$$\hat{p}_t$$)與環境(給出專家們的建議$$\{f_{E,t}, ~ \forall E \in \mathcal{E}\}$$與給出結果$$y_t$$)的重複賽局。

### 架構流程

已知參數：決策空間$$\mathcal{D}$$，出像空間$$\mathcal{Y}$$，損失函數$$\mathcal{l}$$，(有限個)專家群$$\mathcal{E}=\{1,2,\dots, N\}$$。

在每一時間點$$t=1,2,\dots$$

1. 環境先決定當期的結果$$y_t$$，但不讓決策者知道；與專家們的建議$$\{f_{E,t} \in \mathcal{D}, ~ \forall E \in \mathcal{E} \}$$且讓決策者知道。
2. 決策者給出其預測值$$\hat{p}_t \in \mathcal{D}$$。
3. 環境秀出當期的結果$$y_t \in \mathcal{Y}$$。
4. 計算決策者與每一個專家的損失，$$\mathcal{l}(\hat{p},y_t)$$與$$\mathcal{l}(f_{E,t},y_t), ~\forall E \in \mathcal{E}$$。

<mark style="background-color:red;">決策者的目標是最小化相對於每一個專家的累積遺憾(cumulative regret)</mark>。

* $$\displaystyle \max_{i=1,2,\dots, N} R_{i,n}=o(n)$$ 或
* $$\displaystyle \frac{1}{n} \left( \hat{L}_n - \min_{i=1,2,\dots, N} L_{i,n}  \xrightarrow {n \rightarrow \infty} 0  \right)$$



<mark style="color:red;">決策者相對於專家</mark>$$E$$<mark style="color:red;">預測</mark>$$n$$<mark style="color:red;">期的累積遺憾</mark>(越小越好)定義為：$$\displaystyle  R_{E,n} = \sum_{t=1}^n (\mathcal{l}(\hat{p}_t, y_t) - \mathcal{l}(f_{E,t}, y_t))  \equiv \hat{L}_n - L_{E,n}$$

* $$\displaystyle  \hat{L}_n \equiv \sum_{t=1}^n \mathcal{l}(\hat{p}_t, y_t)$$為決策者的累積損失，越接近0越好。
* $$\displaystyle  L_{E,n} \equiv \sum_{t=1}^n \mathcal{l}(f_{E,t}, y_t)$$為專家$$E$$的累積損失，越接近0越好。

可定義立即遺憾(instantaneous regret)為：$$\displaystyle  r_{E,t} = \mathcal{l}(\hat{p}_t, y_t) - \mathcal{l}(f_{E,t}, y_t)$$。

* 可得$$\displaystyle  R_{E,n} = \sum_{t=1}^n r_{E,t}$$。
* 可以將$$r_{E,t}$$視為決策者在第$$t$$個結果$$y_t$$ 揭曉後，對於沒有立即聽取專家$$E$$的建議所感到的遺憾。

## 加權平均預測(weighted average prediction)

> $$\displaystyle  \hat{p}_t = \frac{\sum_{i=1}^N w_{i,t-1} f_{i,t} }{ \sum_{j=1}^N w_{j,t-1} }$$
>
> $$\displaystyle  w_{1,t-1}, \dots, w_{N, t-1} \geq 0, ~t=1,2,\dots, n$$為N個專家在時間$$t$$的權重。(註：時間1的權重由使用者自訂)。
>
> 根據專家們當期的權重，對這一期的專家們預測值加權後再正規化。

因為$$f_{i,t} \in \mathcal{D}$$，其中決策空間$$\mathcal{D}$$假設為凸集合且$$\hat{p}_t$$為$$f_{i,t}$$的凸組合，因此$$\hat{p}_t \in \mathcal{D}$$。

### 表達權重為遺憾的一次可微分非負遞增凸函數

我們的目標是最小化遺憾，因此選擇權重$$w_{i,t-1}$$很自然的會依據累積遺憾$$R_{i,t-1}$$。

* 如果$$R_{i,t-1}$$的值很大，表示專家$$i$$預測比決策者好，因此權重$$w_{i,t-1}$$應該要高一點，反之權重要低一點。<mark style="color:red;">所以權重</mark>$$w_{i,t-1}$$<mark style="color:red;">應該是累積遺憾</mark>$$R_{i,t-1}$$<mark style="color:red;">的遞增函數</mark>。
* 因此令此遞增函數為非負遞增凸函數$$\phi: \mathbb{R} \rightarrow \mathbb{R}$$ 的微分函數$$\phi^{'}$$，即$$w_{i,t-1}=\phi^{'} (R_{i,t-1})$$。
  * $$\displaystyle    \phi(\lambda x+(1-\lambda)y) \leq \lambda\phi(x) +(1-\lambda) \phi(y), ~ 0 \leq \lambda \leq 1$$ 且$$x \geq y \Rightarrow \phi(x) \leq \phi(y)$$且$$\phi(x) \geq 0 ~ \forall x$$。
  * 非負與遞增是權重的自然限制，而凸函數限制是因為可變成凸函數最佳化問題，數學性質較好處理。
    * 對於非負遞增凸函數，其微分函數 $$\phi{’}(x)$$ 滿足以下性質：
      * $$\phi{'}(x) \geq 0$$，非負（遞增性）。
      * $$\phi^{''}(x) \geq 0$$，非遞減（凸性）。
      * 如果 $$\phi^{''}(x) >0$$，則函數嚴格凸且增長速率不斷加快。
    * 例如：$$\phi(x)=x^2$$；$$\phi(x)=e^x$$；$$\phi(x)=\ln(x), x>1$$。

<mark style="background-color:red;">可改寫預測值</mark> $$\displaystyle  \hat{p}_t = \frac{\sum_{i=1}^N \phi^{'}(R_{i,t-1}) f_{i,t} }{ \sum_{j=1}^N \phi^{'}(R_{j,t-1}) }$$<mark style="background-color:red;">。權重為遺憾的一次可微分非負遞增凸函數</mark>。

### lemma: blackwell condition

> 如果損失函數$$l$$對於第一個參數為凸函數時，即$$\mathcal{l}(\lambda \hat{p}_t + (1-\lambda ) \lambda \hat{q}_t, y_t) \leq  \lambda  \mathcal{l}(\hat{p}_t, y_t) +   (1-\lambda ) \mathcal{l}(\hat{q}_t, y_t)$$，則得
>
> $$\displaystyle    \sup_{y_t \in \mathcal{Y}} \sum_{i=1}^N r_{i,t} \phi^{'}(R_{i,t-1}) \leq 0$$。
>
> 或以位勢函數寫為 $$\mathbf{r}_t \cdot \nabla \Phi (\mathbf{R}_{t-1}) \leq 0$$。
>
> 註：兩向量內積=0表示正交，小於0時表示夾角小於90度。
>
> 損失函數$$l$$對於第一個參數為凸函數可解釋為使用多個預測的加權值(加權共識)的損失，會比單個預測損失的加權值低。
>
> <mark style="color:red;">上述不等式為 Blackwell 條件，因為它與著名的 Blackwell 可接近性定理證明中使用的一個關鍵屬性相似</mark>。

Jensen不等式：變數平均值代入凸函數，其值會小於等於先套用凸函數後再平均。平均後再套用凸函式的效果，比直接套用凸函式後再平均“更保守”（數值更低）。

$$\phi(\mathrm{E}(X)) \leq \mathrm{E}(\phi(X))$$。

$$\displaystyle  r_{i,t} = \mathcal{l}(\hat{p}_t, y_t) - \mathcal{l}(f_{i,t}, y_t)$$

$$\displaystyle     \forall y \in \mathcal{Y}, ~      \mathcal{l}(\hat{p}_t, y) =      \mathcal{l}\left(\frac{\sum_{i=1}^N \phi^{'}(R_{i,t-1}) f_{i,t} }{\sum_{j=1}^N \phi^{'}(R_{j,t-1})},y \right) \leq           \frac{\sum_{i=1}^N \phi^{'}(R_{i,t-1}) \mathcal{l}(f_{i,t},y) }{\sum_{j=1}^N \phi^{'}(R_{j,t-1})}$$

因為$$\mathcal{l}(\hat{p}_t, y) \geq 0$$為非負函數，移項得$$\displaystyle      \mathcal{l}(\hat{p}_t, y) \sum_{j=1}^N \phi^{'}(R_{j,t-1}) \leq \sum_{i=1}^N \phi^{'}(R_{i,t-1}) \mathcal{l}(f_{i,t},y)$$

整理得$$\displaystyle       \sum_{i=1}^N \mathcal{l}(\hat{p}_t, y) \phi^{'}(R_{i,t-1}) -\sum_{i=1}^N \phi^{'}(R_{i,t-1}) \mathcal{l}(f_{i,t},y) \leq  0$$

所以$$\displaystyle       \sum_{i=1}^N [\mathcal{l}(\hat{p}_t, y)      - \mathcal{l}(f_{i,t},y)     ] \phi^{'}(R_{i,t-1})  \leq  0, ~\forall y \in \mathcal{Y}$$

因此$$\displaystyle    \sup_{y_t \in \mathcal{Y}} \sum_{i=1}^N r_{i,t} \phi^{'}(R_{i,t-1}) \leq 0$$ (QED)

## 位勢函數(potential function)

### 表達權重為遺憾的二次可微分非負遞增函數

立即遺憾$$\displaystyle  r_{i,t} = \mathcal{l}(\hat{p}_t, y_t) - \mathcal{l}(f_{i,t}, y_t)$$。

令立即遺憾向量(instantaneous regret vector) $$\mathbf{r}_t=(r_{1,t}, \dots, r_{N,t}) \in \mathbb{R}^N$$與(累積)遺憾向量$$\mathbf{R}_n= \sum_{t=1}^n \mathbf{r}_{t} \in \mathbb{R}^N$$。

定義位勢函數$$\Phi: \mathbb{R}^N \rightarrow \mathbb{R}$$為$$\displaystyle  \Phi(\mathbf{u}) = \psi \left(  \sum_{i=1}^N \phi (u_i)\right)$$，

* $$\phi: \mathbb{R} \rightarrow \mathbb{R}$$為非負、遞增、二次可微函數(註：比前述定義權重為累積遺憾的微分函數$$w_{i,t-1}=\phi^{'} (R_{i,t-1})$$再嚴格一點要求二次可微分，<mark style="color:red;">但不要求為凸函數</mark>)。
* $$\psi: \mathbb{R} \rightarrow \mathbb{R}$$為非負、嚴格遞增、凹函數(concave function)、二次可微輔助函數(在分析時很重要)。
* $$\displaystyle    \Phi(\mathbf{R}_n)   = \Phi (\sum_{t=1}^n \mathbf{r}_{t})  = \Phi (\sum_{t=1}^n (r_{1,t},  r_{2,t}, \dots, r_{N,t}))  = \psi \left(  \sum_{i=1}^N \phi (\sum_{t=1}^n r_{i,t})\right)$$

<mark style="background-color:red;">可改寫預測值定義在位勢函數</mark>$$\Phi$$<mark style="background-color:red;">上</mark> $$\displaystyle  \hat{p}_t =  \frac{\sum_{i=1}^N \nabla \Phi(\mathbf{R}_{t-1})_i f_{i,t} } { \sum_{j=1}^N \nabla \Phi(\mathbf{R}_{t-1})_j }$$。

其中$$\displaystyle   \nabla \Phi(\mathbf{R}_{t-1})_i = \frac{\partial \Phi(\mathbf{R}_{t-1})}{\partial R_{i,t-1}}$$。

$$\displaystyle   \nabla \Phi(\mathbf{R}_{t-1}) =  \begin{bmatrix}  \frac{\partial \Phi(\mathbf{R}_{t-1})}{\partial R_{1,t-1}} \\  \frac{\partial \Phi(\mathbf{R}_{t-1})}{\partial R_{2,t-1}} \\  \vdots \\  \frac{\partial \Phi(\mathbf{R}_{t-1})}{\partial R_{N,t-1}} \\  \end{bmatrix}$$為梯度向量。

## 多項式加權平均預測器(polynomially weighted average forecaster)

## 指數加權平均預測器(exponentially weighted average forecaster)

## 最佳遺憾界限(optimal bound)
