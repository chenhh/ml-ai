# Bayesian Methods for Hackers

## 第 1 章：貝氏方法簡介

[https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1\_Introduction/Ch1\_Introduction\_PyMC\_current.ipynb](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Ch1_Introduction_PyMC_current.ipynb)

## **貝氏推斷的哲學**&#x20;

貝氏推斷是關於在考慮新證據後更新信念的過程。與傳統的統計推斷不同，貝氏推斷保留了不確定性。

個人信念和機率的範例：

* 我拋一枚硬幣，我們都猜結果。假設硬幣是公平的，我們都會同意正面朝上的機率是 1/2。那麼，假設我偷看硬幣。現在我確定結果是什麼：我將機率 1.0 分配給正面或反面（無論是哪一個）。現在你對這枚硬幣是正面的信念是什麼？我對結果的瞭解並沒有改變硬幣的結果。因此，我們為結果分配不同的機率。
* 您的程式碼要麼有錯誤，要麼沒有，但我們不知道哪個情境是真的，儘管我們確信存在或不存在錯誤。
* 一名病人出現症狀$$x,y,z$$  。而有多種疾病可能導致所有這些疾病，但只有一種疾病造成症狀。一位醫生對哪一種疾病有自己的信念，但第二位醫生的信念可能略有不同。

這種將信念視為機率的哲學對人類來說是很自然的。<mark style="color:red;">**當我們與世界互動時，我們不斷地使用它，只看到部分事實，但收集證據來形成信念**</mark>。

為了與傳統的機率符號保持一致，我們表示我們對事件$$A$$的信念記為$$\mathrm{P}(A)$$ 。我們稱這個量為<mark style="color:red;">**先驗機率**</mark>。

如果有新的證據$$X$$，將更新的信念表示為$$\mathrm{P}(A|X)$$，解釋為在已知的證據$$X$$下$$A$$發生的機率(信念)，稱為<mark style="color:red;">**後驗機率**</mark>。

* $$\mathrm{P}(A)$$：硬幣有 50% 的機會出現正面。$$\mathrm{P}(A|X)$$：已知硬幣正面落地的資訊$$X$$，因此將出現正面的機率修正為1，出現反面的機率修正為0。
* $$\mathrm{P}(A)$$：龐大而複雜的程式碼可能存在錯誤。$$\mathrm{P}(A|X)$$：程式碼全部通過$$X$$測試，仍然可能存在錯誤，但現在它出現的可能性較小。
* $$\mathrm{P}(A)$$：患者可能患有多種疾病。$$\mathrm{P}(A|X)$$：進行血液檢查產生證據 $$X$$，排除一些可能的疾病。

很明顯，在每個例子中，我們在看到新證據$$X$$後並沒有完全放棄先前的信念 ，但我們重新加權先前的內容以納入新的證據（即我們對某些信念與其他信念給予更多的權重或信心）。



* **頻率主義解釋**: 機率被解釋為長期頻率。例如，飛機事故的機率被解釋為長期的飛機事故頻率。
  * **問題**: 對於某些事件，如總統選舉的結果，沒有長期頻率可以參考。頻率主義者通過引入替代現實來解決這個問題，即在所有這些現實中，事件發生的頻率定義了機率。
* **貝氏解釋**: 機率是對事件發生的信念或信心的度量。簡單來說，機率是對某個事件的主觀意見的總結。
  * **信念度**: 一個人對某個事件賦予的信念為0，表示他完全不相信該事件會發生；信念為1，表示他完全確信該事件會發生。介於0和1之間的信念度表示對其他結果的權重。

```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl


# 設置全局字體為支持中文的字體
mpl.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 正黑體
mpl.rcParams['axes.unicode_minus'] = False  # 解決負號 '-' 顯示為方塊的問題

mpl.style.use("ggplot")
plt.figure(figsize=(11, 9))

import scipy.stats as stats

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
data = stats.bernoulli.rvs(0.5, size=n_trials[-1])
x = np.linspace(0, 1, 100)

# For the already prepared, I'm using Binomial's conj. prior.
for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials) // 2, 2, k + 1)
    plt.xlabel("$p$, 出現正面的機率") \
        if k in [0, len(n_trials) - 1] else None
    plt.setp(sx.get_yticklabels(), visible=False)
    heads = data[:N].sum()
    y = dist.pdf(x, 1 + heads, 1 + N - heads)
    plt.plot(x, y, label=f"{N}次丟銅版，觀測到{heads}次正面" )
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)

plt.suptitle("後驗機率的貝氏更新",
             y=1.02,
             fontsize=14)

plt.tight_layout()
plt.show()
```

```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.style.use("ggplot")
plt.figure(figsize=(12.5, 4))

p = np.linspace(0, 1, 50)
plt.plot(p, 2 * p / (1 + p), color="#348ABD", lw=3)
# plt.fill_between(p, 2*p/(1+p), alpha=.5, facecolor=["#A60628"])
plt.scatter(0.2, 2 * (0.2) / 1.2, s=140, c="#348ABD")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Prior, $P(A) = p$")
plt.ylabel("Posterior, $P(A|X)$, with $P(A) = p$")
plt.title("Are there bugs in my code?")
plt.show()
```



## 參考資料

* [https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
