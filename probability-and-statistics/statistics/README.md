# 統計量(statistics)

## 簡介

統計學是一門將資料匯總為統計量（平均數等）或圖表，以獲取其特徵的學問。起源於國家在徵稅時進行的國情（人口）調查。

統計學分為用於獲取手中資料特徵的描述統計學，通過樣本獲取總體 特徵的推論(推理)統計學，以及在市場行銷中備受關注的貝氏統計學等。

### 描述統計學

幫助我們掌握手頭資料的特徵（平均數、離散程度）或趨勢。是以大量資料為對象的統計學。

算術平均數：$$\displaystyle \overline{X}=\frac{1}{n} \sum_{i=1}^n X_i$$。資料的中心。

幾何平均數：$$\displaystyle \overline{X}_G=\left( \prod{i=1}^n X_i \right)^{1/n}$$。計算年增長率和同比值的平均數。

調和平均數：$$\displaystyle \overline{X}_H=\frac{n}{\sum_{i=1}^n \frac{1}{X_i}}$$。計算給定距離的平均速度。

算數平均 >= 幾何平均 >= 調和平均。

分位數：將$$n$$筆資料由小至大排序後，分為$$k$$等份，位於分割點的數值稱為分位數。常用四分位數($$Q_1, Q_2, Q_3)$$，其中$$Q_2$$為中位數。

偏差(bias)：$$d_i=|X_i - \overline{X}|$$，為資料距離平均值的差值。

變異數：$$S_n^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \overline{X})^2$$。

離群值：偏移平均值很大的資料稱為離群值。

變異係數(coefficient of variation)：用於比較兩筆資料的離散程度，$$CV=\frac{S_n}{\overline{X}}$$。

Pearson相關係數(correlation coefficient): 兩筆(實數)資料間的線性相關程度。介於-1(完全負相關)與1(完全正相關)。

Spearman/Kendall相關係數：將資料各自排名後，計算兩筆資料間排名的相關程度。

### 推論統計學

根據樣本資訊來推斷總體(母體)的特徵。主要內容有無偏點估計、信賴區間估計和假設檢定等。

#### 貝氏統計學

貝氏統計學是一種可以由吸收知識、經驗更新模型的統計學。可通過資料學習提高模型精確度。

## 統計量(statistics)

> 令$$X_1,X_2\ldots,X_N$$ 為一由感興趣的母體所得大小為$$N$$的隨機樣本，即$$X_1,X_2, \ldots,X_N$$為獨立同分佈的樣本
>
> &#x20;一統計量為一個由樣本(向量)$$\mathbf{X}=\{X_1,X_2, \ldots,X_N\}$$ 與某個已知常數所形成的函數，亦為一隨機變數，可作為母體參數(population parameters)的推論之用。
>
> 向量$$X$$的一實值函數$$\mathrm{T}(\mathbf{X})=\mathrm{T}(X_1,X_2,\ldots ,X_N ) \in \mathbb{R}^k, k=1,2,\dots,K$$稱為$$X$$的<mark style="color:red;">統計量</mark>。
>
> 簡單的說，只使用$$\mathbf{X}$$且不包含參數$$\theta$$的函數均可稱為統計量。

&#x20;統計量是對樣本的加工，好的統計量應該能夠將樣本中關於母體分佈的未知資訊盡可能集中起來。

若要研究某參數分佈族中的未知參數，為此抽取了一組樣本，樣本中所包含的資訊可分為兩類:

* 關於未知參數的資訊。
* 以及關於樣本結構的資訊等其它資訊。

**統計量是樣本的不帶任何未知量(如參數)的函數**。而函數就是一種「濃縮」訊息的動作，因此統計量中所包含的資訊，通常比整個樣本資料所包含的來得少。<mark style="background-color:red;">統計量仍為一隨機變數，因為其值會隨</mark>$$X$$<mark style="background-color:red;">的實現而變動</mark>。

統計量為一泛函(functional)，因為$$X$$在連續的狀況下為一函數，而上述定義只是取連續函數的觀測值而為離散數列。

<mark style="background-color:red;">**一統計量的機率分佈稱作此統計量的抽樣分佈（sample distribution）**</mark>。從實務觀點，此分佈可作為經由重複取樣所得的統計量的可能觀察值之相對頻率圖得出。

![幾何分佈(p=0.2)平均值與變異數的抽樣分佈](../../.gitbook/assets/sample\_dist-min.png)



```python
import numpy as np
import matplotlib.pyplot as plt

def sample_distribution(n_sample=5000, n_point=10000):
    mus = np.random.geometric(0.2, (n_sample, n_point)).mean(axis=1)   # size: n_sample
    vars = np.random.geometric(0.2, (n_sample, n_point)).var(axis=1)
    fig, ax = plt.subplots(2,1)
    n_bin = n_sample // 10
    ax[0].hist(mus, bins=n_bin, density=True, edgecolor='black', 
        label='sample distribution of mean')
    ax[1].hist(vars, bins=n_bin, density=True,edgecolor='black', 
        color='green', label='sample distribution of var')
    ax[0].set_ylabel('Frequency')
    ax[1].set_ylabel('Frequency')
    fig.suptitle('Sample distribution', fontsize=24)
    ax[0].legend(fontsize=20)
    ax[1].legend(fontsize=20)
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_distribution()
```









##
