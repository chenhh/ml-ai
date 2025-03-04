# 點估計（point estimation）

## 簡介

給定一隨機分佈，假設已知隨機樣本來自於機率密度函數為$$f(x|\theta)$$的母體（具有參數$$\theta$$的分佈，但不一定知道$$f$$的解析形式），其中參數(向量) $$\theta$$未知，而$$\theta \in \Omega$$（參數空間, parameter space）。

* 參數空間：一個參數（向量）所有可能數值構成的集合。而隨機變數分配的參數即為參數空間中特定的一個元素$$\theta$$。
* 點估計的<mark style="background-color:red;">目的</mark>就是使用觀察到的樣本$$X=(X_1,X_2, \ldots ,X_N)$$ 的函數（統計量）$$T=T(X_1, X_2, \dots, X_N)$$來估計參數$$\theta$$或是其函數$$q(\theta)$$  。
* 任一統計量若是用於估計參數，則稱為<mark style="color:red;">估計量(estimator)</mark>；而估計量仍然是一隨機變數，且估計量的分佈稱為抽樣分佈（sampling distribution）。

#### 範例：水果重量合格比例

令$$X_1, X_2, \dots,$$(獨立同分佈)為取出水果的重量，假設其值要超過$$a$$才算合格，若要估計$$N$$個水果中合格的比例$$\theta$$，則估計值為$$T_N=T(X_1, \dots, X_N )=\frac{1}{N} \sum_{i=1}^N I_{X_i > a}$$。

若假設重量為常態分佈$$N(\mu, \sigma^2)$$，且用樣本平均$$\overline{X}_N$$與樣本變異數$$S_N^2$$為參數近似值，則以統計量$$T_N=T(X_1, \dots, X_N)=1-\Phi(\frac{a-\overline{X}N}{S_N})$$為估計量。

可見對同一個參數有多種估計量。

#### 範例：順序統計量(統計量必存在)

令$$X_1, \dots, X_N$$為由均勻分佈$$U(0, \theta)$$產生的隨機樣本，$$\theta >0$$。

1. 可將$$N$$個樣本由小至大排序，得順序統計量$$X_{(1)} \leq \dots \leq X_{(N)}$$。則$$T_1=X_{(N)}$$。此法簡單，但是缺點為低估$$\theta$$之值。
2. 因為$$N$$個樣本在數量夠多時，會將區間$$[0, \theta]$$分成$$N+1$$個等長子區間，因此修正的估計值為$$T_2 = \frac{n+1}{n}X_{(N)}$$。或者用$$T_3 = X_{(1)} +X_{(N)}$$，$$T_4 = (n+1)X_{(1)}$$。
3. 樣本平均可能會接近中點$$\theta/2$$，因此也可用$$T_5= 2 \overline{X}_N$$。

### 選擇估計量的方法

估計量品質是包括不偏性 (unbiasedness)、一致性 (consistency)、有效性 (efficiency)。

* 一個母體參數的不偏估計式 (unbiased estimator) 是一個估計量的(樣本分佈)期望值會等於(母體)參數的估計式。$$\mathrm{E}(\overline{X}_N)=\theta$$.&#x20;
* 假如隨著樣本大小$$N$$的增加，估計量與參數間的差異會隨之變小，此不偏估計量被稱為是一致的( consistent)。&#x20;
* 如果一個參數有兩個不偏估計式，具有變異數比較小的不偏估計式，被稱為是相對的比較有效 (relatively more efficient)。

多餘參數(nuisance parameter)
-

<mark style="color:red;">多餘引數是指與感興趣參數無關，但在分析那些感興趣參數時必須考慮的所有參數</mark>。

假設模型參數為$$\left\{ f(x;\theta)~| \theta \in \Theta \subseteq \mathbb{R}^d \right\}$$，$$\theta=(\theta_1, \dots, \theta_k)$$為參數，這樣對參數模型進行推斷的問題就轉化為對參數估計的問題。通常我們僅對參數的函數$$T(\theta)$$感興趣。

例如，當常態分佈模型$$\{N(\mu,\sigma^2)~| ~ \mu \in \mathbb{R}, ~ \sigma^2 >0\}$$的參數$$T(\mu,\sigma^2)=\mu$$是首要關心的參數時，變異數$$\sigma^2$$就是一個多餘參數。多餘參數通常是變異數，但並不總是；



## 參考資料

黃文璋，數理統計，第六章。
