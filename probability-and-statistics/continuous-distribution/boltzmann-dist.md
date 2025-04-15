---
description: 波茲曼分佈
---

# Boltzmann分佈

## 簡介

波茲曼分佈是統計力學中的一個核心概念，用於描述在熱平衡狀態下，系統中粒子的能量分佈情況。它由奧地利物理學家Ludwig Boltzmann提出，並廣泛應用於物理、化學、生物學以及工程領域。

<mark style="color:red;">Boltzmann 分佈描述的是：在</mark><mark style="color:red;">**熱平衡**</mark><mark style="color:red;">下，一個系統出現在能量為</mark>$$E$$<mark style="color:red;">的某個「狀態」的機率是多少</mark>？

狀態（state）就是系統某一個可能的具體組態（configuration），它代表了系統裡「每個粒子（或元件）」的具體情況。每個狀態都有一個對應的能量$$E_i$$，而 Boltzmann 分佈告訴我們：在溫度$$𝑇$$\
下，系統會以多大的機率出現在這個狀態。例如：

|  系統                     | 狀態的意義               |
| ----------------------- | ------------------- |
| 氣體分子系統                  | 所有分子的位置和動量（微觀態）     |
| 自旋系統（Ising model）       | 每個自旋是 +1 或 -1 的排列組合 |
| 機器學習（Boltzmann machine） | 每個神經元是 0 或 1 的一種組合  |
| 隨機跳躍模型（Markov chain）    | 系統當下所處的離散狀態         |
| 分子排列                    | 每個原子在晶格中的位置組合       |

例如有一個只有 3 個粒子的 Ising 系統，每個粒子可以是$$+1$$或$$−1$$，那所有可能狀態有$$2^3=8$$種，每一種排列(即一個具體狀態）都有對應的能量$$E_i$$可以用 Boltzmann 分佈計算它們的出現機率。

Boltzmann分佈是Gibbs分佈的一個特例。當系統包含多個粒子且粒子間存在相互作用時，需要用Gibbs分佈來描述整個系統的狀態分佈。

在高溫極限下（$$k_BT≫E_i$$），玻爾茲曼分佈可以近似為均勻分佈，這意味著粒子在各能量狀態之間的分佈趨於均勻。

<mark style="color:red;">Boltzmann分佈描述了在溫度</mark>$$T$$<mark style="color:red;">下，系統中處於某個能量狀態</mark>$$E_i$$<mark style="color:red;">的粒子數量或機率，與該能量狀態的指數函式成正比</mark>。

$$\mathrm{P}(E_i) \propto \exp(-\frac{E_i}{k_BT})$$ 或

&#x20;$$\mathrm{P}(E_i) =\frac{e^(-\frac{E_i}{k_BT})}{Z}$$。

其中

* $$\mathrm{P}(E_i)$$：系統處於能量狀態$$E_i$$的機率。
* $$E_i$$：粒子的能量狀態(指速度或溫度)。
* $$T$$：絕對溫度(K)。
* $$k_B$$：Boltzmann常數，大約為$$1.38 \times 10^{-23} \text{J/K}$$。&#x20;
* $$Z$$：配分函數(partition function)，用於正規化機率。$$\displaystyle Z=\sum_i e^{-\frac{E_i}{k_BT}}$$。配分函數$$Z$$ 是Boltzmann分佈的核心，它包含了系統所有可能狀態的資訊。許多熱力學量都可以從配分函式中匯出。

## 物理意義

<mark style="color:red;">Boltzmann分佈表明，在熱平衡條件下，系統中的粒子傾向於分佈在低能量狀態，但隨著溫度升高，粒子分佈到高能量狀態的機率也會增加</mark>。這是因為指數函式$$e^(-\frac{E_i}{k_BT})$$隨著$$T$$的增加而變得平坦。

通過Boltzmann分佈，可以計算系統的宏觀性質，例如平均能量、熵、自由能等。

### 能量與溫度的關係

* 在低溫時，粒子主要集中在最低能量狀態（基態）。
* 在高溫時，粒子更均勻地分佈在不同能量狀態之間。粒子越容易佔據高能態（分佈更均勻）。
* 能量越低的狀態，機率越高（指數衰減）。

<mark style="color:red;">類似於“自然界傾向於低能量狀態，但熱擾動（溫度）會使系統探索高能態”</mark>。

## 推導背景

Boltzmann分佈可從最大熵原理或正則系綜（Canonical Ensemble）匯出。

Boltzmann分佈源於統計力學的基本假設——<mark style="color:red;">系統處於熱平衡時，各微觀狀態出現的機率與該狀態的能量呈指數關係</mark>。

1. **系統的總能量固定** ：考慮一個孤立系統，其總能量$$E_{total}$$ 固定。
2. **最大熵原理** ：根據統計力學，系統在熱平衡時會達到最大熵狀態。
3. **能量與機率的關係** ：利用拉格朗日乘數法，可以得到粒子處於某個能量狀態的機率與指數函式成正比。

最終結果就是Boltzmann分佈的形式。

### 正則系綜法（Canonical Ensemble）

考慮一個由$$N$$個粒子組成的系統。系統的能量狀態可以用$$E_i$$ 表示，其中 $$i=1,2,\dots$$是不同的能量狀態。在熱平衡條件下，系統與外界環境保持能量交換，但總能量固定。

系統屬於正則系綜（Canonical Ensemble），即系統可以與外界進行能量交換，但粒子數和體積保持不變。系統的溫度$$T$$固定，且外界環境是一個熱庫。

### 最大熵法(maximum entropy)

考慮一個由$$N$$個粒子組成的系統。系統的能量狀態可以用$$E_i$$ 表示，其中 $$i=1,2,\dots$$是不同的能量狀態。在熱平衡條件下，系統與外界環境保持能量交換，但總能量固定。

在熱平衡條件下，系統會達到最大機率的微觀狀態分佈。系統中每個微觀狀態出現的機率與該狀態的能量呈指數關係。

假設系統處於某個能量狀態$$E_i$$的機率為$$\mathrm{P}(E_i)$$。我們希望找到$$\mathrm{P}(E_i)$$的具體形式。

為了確定機率分佈，我們需要引入兩個約束條件：

1. \[機率總和為1] $$\sum_i \mathrm{P}(E_i) = 1$$。所有可能狀態的機率總和為 1。
2. \[能量均值(期望值)] $$\displaystyle \mathrm{P}(E_i) E_i = \langle E\rangle$$。系統的平均能量由機率分佈決定。

根據最大熵原理，在滿足上述約束條件的情況下，系統的熵$$S$$應該最大化。熵的定義為：

$$S = - k_B \sum_i \mathrm{P}(E_i) \log \mathrm{P}(E_i)$$，其中$$k_B$$為Boltzmann常數。

此為有兩個限制式的最佳化問題，使用Langrange乘數求解：

$$L = -k_B \sum_i \mathrm{P}(E_i) \log \mathrm{P}(E_i) + \lambda_1 (\sum_{i} \mathrm{P}(E_i) - 1) + \lambda_2 (\sum_i \mathrm{P}(E_i ) E_i - \langle E \rangle)$$，其中：$$L$$為熵(entropy)。$$\lambda_i, i=1,2$$為Langrange乘法。

對$$\mathrm{P}(E_i)$$求偏導數且令其值為0：$$\frac{\partial L}{\partial \mathrm{P}(E_i) } = -k_B (\log \mathrm{P}(E_i) + 1) + \lambda_1 + \lambda_2 E_i = 0$$。

整理得$$\log \mathrm{P}(E_i) = -1 + \frac{\lambda_1}{k_B} + \frac{\lambda_2}{k_B} E_i$$ 。

兩邊取指數得$$\mathrm{P}(E_i) = e^{-1+ \frac{\lambda_1}{k_B}}e^{\frac{\lambda_2}{k_B}E_i}$$。

令$$C= e^{-1+ \frac{\lambda_1}{k_B}}$$為歸一化常數，則$$\mathrm{P}(E_i) =Ce^{\frac{\lambda_2}{k_B}E_i}$$。

利用歸一化條件$$\sum_i \mathrm{P}(E_i)=1$$可得$$C \sum_{i} e^{\frac{\lambda_2}{k_B} E_i} = 1$$，移項得$$C = \frac{1}{\sum_i e^{\frac{\lambda_2}{k_B}E_i}}$$

