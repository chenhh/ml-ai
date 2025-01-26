# Wasserstein distance

## 簡介

Wasserstein distance（也稱為 Earth Mover's Distance, EMD）是一種在機率論和最優傳輸理論中常用的距離度量，用來衡量兩個機率分佈之間的差異。它得名於「搬運土方」問題（Earth Mover's Problem），<mark style="color:red;">其核心思想是計算將一個分佈轉換為另一個分佈所需的最小“工作量”，即如何以最小的成本（如能量、距離）將“質量”（機率密度）從一個分佈轉移到另一個分佈</mark>。

假設有兩個沙堆（分佈），Wasserstein 距離表示將一個沙堆搬運成另一個沙堆所需的最小工作量。搬運成本由沙土移動的距離和搬運量決定。如果兩個分佈形狀相似且位置接近，距離較小；反之則較大。

相較於其他距離度量方式，例如歐氏距離，Wasserstein 距離在處理分佈之間的差異時，能提供更細緻的度量。尤其當兩個分佈沒有重疊或重疊部分很少時(支撐集不重疊)，Wasserstein 距離仍然能提供有意義的數值，這在某些情況下非常重要。

## 定義

asserstein distance 定義為最優傳輸問題的解，其目標是找到一種「搬運計劃」，使得將一個分佈變成另一個分佈的總成本最小化。

對於兩個在空間 𝑅 𝑑 R d 上的機率分佈 $$\mu$$ 和 $$\nu$$，以及給定的距離度量$$d(x,y)$$，p-Wasserstein距離定義為：

$$\displaystyle W_p(\mu, \nu)=\left(  \inf_{\gamma \in \prod(\mu, \nu)}  \int_{\mathbb{R}^d \times \mathbb{R}^d} d(x,y)^p d \gamma(x,y)  \right)^{1/p}$$

* $$\prod(\mu, \nu)$$是邊際分佈$$\mu, \nu$$的聯合分佈。
* $$d(x,y)$$為距離度量函數。
* $$p \geq 1$$為參數(實數)。

### python實作

[https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein\_distance.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)

```python
from scipy.stats import wasserstein_distance

# 定義兩個分佈
distribution_1 = [0, 1, 3, 7, 10]
distribution_2 = [1, 2, 4, 6, 9]

# 計算 Wasserstein 距離
distance = wasserstein_distance(distribution_1, distribution_2)

print(f"Wasserstein distance: {distance}") 
# 輸出 Wasserstein distance: 1.0
```

### **直觀解釋**

1. **分佈的解讀**：將兩個機率分佈視為兩堆土壤，分佈的值代表土壤的重量。
2. **搬運土壤**：Wasserstein距離量化了將一堆土壤（來源分佈）「重新分配」成另一堆土壤（目標分佈）所需的最小成本。
3. **成本計算**：每單位重量的搬運成本由距離決定即 $$d(x,y)$$，總成本則是所有搬運過程的累積。

### **特性**

1. **穩健性**：Wasserstein距離在比較分佈時對小的位移特別敏感，能捕捉分佈形狀的差異。
2. **考慮幾何結構**：不僅比較機率值，還考慮分佈支撐集的空間關係。
3. **連續性**：即使分佈中有少量的噪聲，該距離仍具有良好的穩定性。
4. **對稱且滿足三角不等式**：是嚴格的度量函數（與 KL 散度不同）。
5. <mark style="color:red;">**弱收斂敏感**</mark><mark style="color:red;">：即使分佈支撐集不重疊，也能提供有意義的距離（如生成對抗網路中的穩定訓練）</mark>。

### **與其他距離的對比**

| 度量方法           | 優點               | 缺點           |
| -------------- | ---------------- | ------------ |
| KL 散度          | 計算簡單             | 不對稱；對無重疊分佈失效 |
| JS 散度          | 對稱               | 對無重疊分佈梯度消失   |
| Wasserstein 距離 | 幾何敏感；梯度穩定；分佈無需重疊 | 計算複雜度高       |

## 特例：1-Wasserstein距離

當 p=1 時，1-Wasserstein距離（又稱 Kantorovich-Rubinstein 距離）公式簡化為：

$$\displaystyle W_1(\mu, \nu)= \inf_{\gamma \in \prod(\mu, \nu)}  \int_{\mathbb{R}^d \times \mathbb{R}^d} d(x,y) d \gamma(x,y)$$

這個版本的距離計算更加直觀，尤其適用於分佈的「質量中心」有小幅位移的情況。

對偶型式：

$$\displaystyle W_1(\mu, \nu)= \sup_{\|f\|_L \leq 1}  \left| \mathrm{E}_{x \sim \mu} (f(x))  - \mathrm{E}_{y \sim \nu} (f(x))   \right|$$

其中$$f$$是Lipschitz 函數，滿足$$|f(x) - f(y)| \leq \| x - y\|$$。

#### 範例

設 P={1,2}, Q={3,4}，每個點的質量均為 0.5。 Wasserstein-1 距離為:

$$W_1= 0.5 (|1-3| + |2-4|) = 2$$。

## 參考資料

* [https://lilianweng.github.io/posts/2017-08-20-gan/#what-is-wasserstein-distance](https://lilianweng.github.io/posts/2017-08-20-gan/#what-is-wasserstein-distance)
* Ramdas, Garcia, Cuturi “On Wasserstein Two Sample Testing and Related Families of Nonparametric Tests” (2015). [arXiv:1509.02237](https://arxiv.org/abs/1509.02237).
