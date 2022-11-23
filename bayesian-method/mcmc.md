---
description: Markov Chain Monte Carlo，蒙地卡羅馬可夫鏈
---

# MCMC

## 簡介

使用蒙地卡羅方法進行抽樣之前，需要考慮一個問題：抽樣的動機是什麼？

在機器學習中經常會從資料中學習出一個函數 ，需要使用生成新的資料。比如說機器視覺中的生成模型，可生成一些新的圖片，就是從學習好的機率分佈中抽樣生成新的圖片。

$$P(x) = \frac{\hat{P}(x)}{z} = \frac{\hat{P}(x)}{\int \hat{P}(x)dx}$$

當資料$$x \in \mathbb{R}^p$$為高維樣本時，劃分函數(partition function)分母的很難求出。直接抽樣的話必須是可以根據機率密度函數（pdf）求出累積分佈函數（cdf），然後在cdf上抽樣。但實際上，大部分機率密度函數都無法直接求出其cdf。

### Inference（推論）

假設看到觀測資料(observed data)$$X$$ ，以及有一些隱變數(latent variable)$$Z$$，給這些隱變數一個先驗分佈$$\mathrm{P}(Z)$$，然後依據這些觀測資料去推斷後驗分佈$$\mathrm{P}(Z|X)$$ 。

## Markov chain

MC假設某一時刻狀態轉移的機率只依賴於它的前一個狀態。

$$\mathrm{P}(X_{t+1}|X_{1}, X_{2},\dots, X_{t})=\mathrm{P}(X_{t+1}|X_{t})$$

因為某一時刻狀態轉移只依賴於它的前一個狀態，那麼我們只要能求出系統中任意兩個狀態之間的轉移機率，最終可得到狀態轉移機率矩陣。

## 參考資料

### 軟體

* [PyMC](https://www.pymc.io/welcome.html)
* \[知乎[\]告別數學公式，圖文解讀什麼是馬爾可夫鏈蒙特卡羅方法（MCMC）](https://zhuanlan.zhihu.com/p/32982140)
* [\[知乎\]馬爾可夫鏈蒙特卡羅演算法（MCMC）](https://zhuanlan.zhihu.com/p/37121528)
