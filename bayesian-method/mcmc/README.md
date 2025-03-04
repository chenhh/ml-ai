---
description: Markov Chain Monte Carlo，蒙地卡羅馬可夫鏈
---

# 蒙地卡羅馬可夫鏈(MCMC)

## 簡介

<mark style="color:red;">**使用MCMC的目的：用於透過機率空間中的隨機取樣來近似感興趣引數的後驗分佈**</mark>。

### 抽樣的動機是什麼？

在機器學習中經常會從資料中學習出一個函數 ，需要使用生成新的資料。比如說機器視覺中的生成模型，可生成一些新的圖片，就是從學習好的機率分佈中抽樣生成新的圖片。

$$P(x) = \frac{\hat{P}(x)}{z} = \frac{\hat{P}(x)}{\int \hat{P}(x)dx}$$

當資料$$x \in \mathbb{R}^p$$為高維樣本時，劃分函數(partition function)分母的很難求出。直接抽樣的話必須是可以根據機率密度函數（pdf）求出累積分佈函數（cdf），然後在cdf上抽樣。但實際上，大部分機率密度函數都無法直接求出其cdf。

### 貝氏推論

假設看到觀測資料(observed data)$$X$$ ，以及有一些隱變數(latent variable)$$Z$$，給這些隱變數一個先驗分佈$$\mathrm{P}(Z)$$，然後依據這些觀測資料去推斷後驗分佈$$\mathrm{P}(Z|X)$$ 。

### Monte Carlo方法

蒙特卡羅方法於20世紀40年代美國在第二次世界大戰中研製原子彈的「曼哈頓計畫」計畫時首先提出，為保密選擇用賭城摩納哥的Monte Carlo作為代號。

假設在1平方公尺的正方形內有一不規則圖形，則使用MC方法可簡單近似其面積：在正方形內均勻生成$$N$$個點，假設有$$p$$個點落在不規則圖形內，則圖形面積近似於$$\frac{p}{N}$$。

## 馬可夫鏈(Markov chain)

### **狀態空間(state space)**

**狀態的定義：**<mark style="color:blue;">狀態是描述系統在某個時間點上的系統特徵或條件的標識</mark>。它可以是一個具體的數值、類別標籤、位置、或其他任何可以用來描述系統狀況的資訊。

狀態空間描述了隱藏的（不可觀測的）系統內部的狀態(離散或連續)。

每個狀態可以看作是一個特定的組態或情形，系統可以在這些狀態之間轉移。

通常使用<mark style="color:red;">符號</mark>$$\mathcal{S}=\{s_1, s_2, \dots ,s_n\}$$<mark style="color:red;">(有限集合)或</mark>$$\mathcal{S}=\{s_1, s_2, \dots \}$$(<mark style="color:red;">可數集合</mark>)或$$\mathcal{S}$$(<mark style="color:red;">不可數集合)</mark>做為狀態空間集合。

#### 範例

* \[有限狀態]天氣模型，狀態空間$$\mathcal{S}=\{\text{晴天}, \text{陰天}, \text{雨天} \}$$。
* \[連續狀態，不可數] 一個粒子的位置和速度的狀態空間可能是實數軸上的一個區間，$$\mathcal{S}=[a,b] \subseteq \mathbb{R}$$。

#### 狀態空間的特點

1. **離散性**：狀態空間可以是有限$$\mathcal{S}=\{s_1, s_2, \dots ,s_n\}$$的或無限的(可數或不可數)，但通常是離散集合(便於計算與說明)。這意味著狀態的數量要麼是有限的，要麼是可以列舉的（例如整數集）。
2. **互斥性**：每個狀態都是相互排斥的，即系統在同一時間只能處於一個特定的狀態。
3. **窮盡性**：狀態空間包含了系統所有可能的狀態，因此系統總是在狀態空間中的某個狀態內。

### 無記憶性

如果在狀態空間中，一個狀態轉移的隨機過程只與當前狀態有關(或者只與前幾步狀態有關，但不是所有的歷史狀態)，稱為無記憶性，則可稱之為<mark style="color:red;">**馬可夫鏈(Markov Chain)**</mark>。

這種性質簡化了對系統的數學描述，使得可以通過轉移機率矩陣來描述從一個狀態到另一個狀態的變化。

極端的例子就是隨機漫步(random walk)，你永遠不可能預測下次狀態如何改變，僅能從當前的狀態去猜測可能的方向。

離散馬可夫鏈假設某一時刻狀態轉移的機率只依賴於它的前一個狀態：

$$\mathrm{P}(X_{t+1}=x_{t+1}|X_{1}=x_1, X_{2}=x_2,\dots, X_{t}=x_t)=\mathrm{P}(X_{t+1}=x_{t+1}|X_{t}=x_t)$$

因為某一時刻狀態轉移只依賴於它的前一個狀態，那麼我們只要能求出系統中任意兩個狀態之間的轉移機率，最終可得到狀態轉移機率矩陣。

### 馬可夫鏈的收斂性質

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
* [https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50](https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50)
