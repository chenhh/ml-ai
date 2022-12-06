# 點估計（point estimation）

## 簡介

給定一隨機分佈，假設已知隨機樣本來自於機率密度函數為$$f(x|\theta)$$的母體（具有參數$$\theta$$的分佈，但不一定知道$$f$$的解析形式），其中參數(向量) $$\theta$$未知，而$$\theta \in \Omega$$（參數空間, parameter space）。

* 參數空間：一個參數（向量）所有可能數值構成的集合。而隨機變數分配的參數即為參數空間中特定的一個元素$$\theta$$。
* 點估計的目的就是使用觀察到的樣本$$X=(X_1,X_2, \ldots ,X_N)$$ 的函數（統計量）$$T(X)$$來估計參數$$\theta$$或是其函數$$q(\theta)$$  。
* 任一統計量若是用於估計參數，則稱為估計量(estimator)；而估計量仍然是一隨機變數，且估計量的分佈稱為抽樣分佈（sampling distribution）。

多餘參數(nuisance parameter)
-

<mark style="color:red;">多餘引數是指與感興趣參數無關，但在分析那些感興趣參數時必須考慮的所有參數</mark>。

假設模型參數為$$\left\{ f(x;\theta)~| \theta \in \Theta \subseteq \mathbb{R}^d \right\}$$，$$\theta=(\theta_1, \dots, \theta_k)$$為參數，這樣對參數模型進行推斷的問題就轉化為對參數估計的問題。通常我們僅對參數的函數$$T(\theta)$$感興趣。

例如，當常態分佈模型$$\{N(\mu,\sigma^2)~| ~ \mu \in \mathbb{R}, ~ \sigma^2 >0\}$$的參數$$T(\mu,\sigma^2)=\mu$$是首要關心的參數時，變異數$$\sigma^2$$就是一個多餘參數。多餘參數通常是變異數，但並不總是；

