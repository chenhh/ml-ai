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

## Monte Carlo方法

蒙特卡羅方法於20世紀40年代美國在第二次世界大戰中研製原子彈的「曼哈頓計畫」計畫時首先提出，為保密選擇用賭城摩納哥的Monte Carlo作為代號。

假設在1平方公尺的正方形內有一不規則圖形，則使用MC方法可簡單近似其面積：在正方形內均勻生成$$N$$個點，假設有$$p$$個點落在不規則圖形內，則圖形面積近似於$$\frac{p}{N}$$。

## Markov chain

MC假設某一時刻狀態轉移的機率只依賴於它的前一個狀態。

$$\mathrm{P}(X_{t+1}|X_{1}, X_{2},\dots, X_{t})=\mathrm{P}(X_{t+1}|X_{t})$$

因為某一時刻狀態轉移只依賴於它的前一個狀態，那麼我們只要能求出系統中任意兩個狀態之間的轉移機率，最終可得到狀態轉移機率矩陣。



馬可夫鏈的收斂性質：

如果一個非週期的馬可夫鏈有狀態轉移矩陣 ，並且他的任何兩個狀態是連通的，則：$$\displaystyle \lim_{n \rightarrow \infty} P_{ij}^n$$與初始狀態$$i$$無關。

* 非週期(acyclic)的馬可夫鏈：這個主要是指馬可夫鏈的狀態轉化不是循環的，如果是循環的則永遠不會收斂。
* 何兩個狀態是連通的：這個指的是從任意一個狀態可以通過有限步到達其他的任意一個狀態，不會出現條件機率一直為0導致不可達的情況，即$$P^n$$中任意一個元素都大於零。
* 馬可夫鏈的狀態數可以是有限的，也可以是無限的。因此可以用於連續機率分佈和離散機率分佈。而一般範例為了說明會使用有限的狀態分佈。

### 馬可夫鏈的細緻平穩條件(Detailed Balance Condition)

給定馬可夫鏈的狀態轉移矩陣$$P$$，與狀態的分佈$$\pi$$，如果非週期馬可鏈的$$P$$與$$\pi$$對所有的狀態$$i,j$$均滿足以下條件時，稱$$\pi$$為$$P$$的平穩分佈(stationary distribution)。

$$
\pi(i)P(i,j) = \pi(j)P(j,i)~ ,\forall i, j
$$



## 參考資料

### 軟體

* [PyMC](https://www.pymc.io/welcome.html)
* \[知乎[\]告別數學公式，圖文解讀什麼是馬爾可夫鏈蒙特卡羅方法（MCMC）](https://zhuanlan.zhihu.com/p/32982140)
* [\[知乎\]馬爾可夫鏈蒙特卡羅演算法（MCMC）](https://zhuanlan.zhihu.com/p/37121528)
