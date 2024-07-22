---
description: binomial distribution
---

# 二項式分佈

當遇到發生次數$$N$$固定的獨立事件，而感興趣的是事件成功$$x$$的次數$$k$$，那麼就可以用二項分佈的公式快速計算出機率。

假設獨立事件次數$$N$$，令每一次成功的機率都是相等的，成功的機率用$$p$$表示。目標是算出$$N$$次事件中，成功$$k$$次的機率。

![二項分佈, N=100, p=0.2](../../.gitbook/assets/binomial\_dist\_100\_0.2-min.png)

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as spstats

def binomial_distribution(n_point=10000, n=100, p=0.2):
    # 生成二項式分佈隨機變數
    values = np.random.binomial(n, p, n_point)
    q = 1 - p

    # 以套件計算動差
    mu = values.mean()
    var = values.var()
    skew = spstats.skew(values)
    kurt = spstats.kurtosis(values)

    # skewness of scipy, Fisher-Pearson coefficient
    m2 = ((values - mu) ** 2).mean()  # variance
    m3 = ((values - mu) ** 3).mean()
    g1 = m3 / (m2 ** 1.5)
    g1f = (q - p) / np.sqrt(n * p * q)  # 偏度公式與樣本計算值偏差大

    # kurtosis of scipy
    m4 = ((values - mu) ** 4).mean()
    g2 = m4 / m2 / m2 - 3
    g2f = (1 - 6 * p * q) / (n * p * q)  # 峰度公式與樣本計算值偏差大
    print(f"{mu}, var:{var}, m2:{m2} "
          f"skew: {skew}, {g1}, {g1f}, "
          f"kurt:{kurt}, {g2}, {g2f}")

    # 驗證套件與手動計算動差的一致性
    np.testing.assert_approx_equal(mu, n * p, significant=2)
    np.testing.assert_approx_equal(var, n * p * (1 - p), significant=2)
    np.testing.assert_approx_equal(var, m2, significant=7)
    np.testing.assert_approx_equal(skew, g1, significant=7)
    np.testing.assert_approx_equal(kurt, g2, significant=7)
    
    # plot
    fig, ax = plt.subplots()
    ax.hist(values, bins=50, density=True, label='binomial distribution')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Binomial (N=100, p=0.2) $\mu = {mu:.2f}, \sigma^2={var:.2f}$')
    ax.legend(fontsize=20)
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    binomial_distribution()

```

### 分佈與統計量

* 隨機變數$$X \sim B(N,p)$$
* 機率質量函數（probability mass function） $$f(k|N,p)=\mathrm{P}(X=k)=\binom{N}{k} p^k (1−p)^{N−k}$$
* 期望值 $$\mathrm{E}(X) = Np$$
* 變異數 $$\mathrm{Var}(X) = Np(1-p)$$
* 偏度 $$\gamma_1 \equiv \mathrm{E} \bigg( (\frac{X-\mu}{\sigma})^3\bigg) = \frac{1-2p}{\sqrt{Np(1-p)}}$$
* 峰度 $$\gamma_2 = \frac{1-6p(1-p)}{np(1-p)}$$

### 獨立的二項分佈變數之和

$$X \sim B(N_X, p), Y \sim B(N_Y, p)$$且兩隨機變數獨立，則 $$X+Y \sim B( N_X + N_Y, p)$$

```python
import numpy as np
import scipy.stats as spstats

def independent_binomial_dist(n_point=10000, n1=100, n2=500, p=0.9):
    x1s = np.random.binomial(n1, p, n_point)
    x2s = np.random.binomial(n2, p, n_point)
    x12s = np.random.binomial(n1+n2, p, n_point)

    # 只有一、二階中央動差比較接近
    for k in range(1, 6):
        mk1 = spstats.moment(x1s, k)
        mk2 = spstats.moment(x2s, k)
        mk12 = spstats.moment(x12s, k)
        print(f"{k}th center moment: 
        {mk1}, {mk2}, {mk1+mk2}, {mk12}")

if __name__ == '__main__':
    independent_binomial_dist()
```

### 二項分布可逼近常態分佈

若試驗的次數$$N$$足夠大時，且機率$$p$$固定不變時，二項式分佈近似於常態分佈。即$$B(N, p) \rightarrow N(Np, Np(1-p))$$as $$N \rightarrow \infty$$。

![二項分佈在試驗次數夠大時(機率不變)，可逼近常態分佈](../../.gitbook/assets/Binomial\_Distribution-min.png)
