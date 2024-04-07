---
description: Log-Periodic Power Law Singularity, 對數週期冪律奇點
---

# LPPLS模型

Johansen 和 Sornette認為金融市場上由於投資者之間的羊群效應及正回饋機制造成的資產價格泡沫的膨脹與破裂可由 LPPL 模型進行建模。

LPPL 模型具有如下特性:&#x20;

1. 投資者之間相互模仿，呈現集體追漲的交易局面，造成對數資產價格呈超指數暴漲；
2. 隨著資產價格泡沫破裂的風險逐漸擴大，市場需要更高的回報作為補償；
3. 資產價格泡沫在臨界點 tc具有最大的崩盤機率；
4. 越接近臨界點tc，資產價格對數週期性振盪頻率越高。

LPPL 模型刻畫的股市崩盤具有典型的 3 個特徵：

1. 股價達到明顯的峰值；
2. 股價至少在 6 個月內維持上漲的態勢；
3. 股價達到峰值後在短期內便迅速下降。

Lin 等指出如果股票市場在泡沫期間的對數收盤價可以用 LPPL 模型進行有效解釋，則其擬合的殘差應該滿足 O-U(Ornstein-Uhlenbeck) 過程。其擬合的殘差若滿足平穩性(可用Dickey-Fuller檢定得$$p$$值是否顯著)，則表明其符合 O-U 過程。

在線性尺度下, 越接近崩盤的臨界點，其價格振盪的頻率越快，其表現為指數振盪的間隔週期越來越短。而在對數尺度下，其振盪頻率為常數。

並且股價越是接近臨界點，股價增長速度越快，即股價增長率呈現單調遞增的特點。



在 LPPL 模型中, 股票價格在泡沫階段的演化過程如下跳躍-擴散方程式：

$$
\frac{dp}{p}=\mu(t)dt+\sigma(t)dW-kdj
$$

* $$p$$為股票價格；
* $$\mu(t)$$為趨勢項；
* $$W$$為均值0，變異數1的Wiener過程；
* $$dj$$為跳躍。

泡沫破滅之前，$$dj=0$$，破滅之後$$dj=1$$；而發生破滅後對應的價格損失幅度由$$k$$決定。

假設股價崩盤的機率$$h(t)$$如下：

$$
h(t)=B^{'}(t_c-t)^{m-1}+C^{'}(t_c -t)^{m-1}\times \cos (\omega \ln (t_c - t) - \phi)
$$

* $$B^{'} >0, C^{'} > 0$$
* $$t_c$$為股價見頂的時間點，也稱為崩潰臨異點；
* $$m$$為冪增長指數，代表股價增長的加速度；$$m$$越小，股價增長的加速度越快，泡沫崩潰可能性越高；
* $$\omega$$為股價振盪的角頻率，$$\phi$$為振盪的初始相位。

由$$\mathrm{E}(d_j)=h(t)dt$$與$$\mathrm{E}_t(dW)=0$$及市場不存在無風險套利條件，即$$\mathrm{E}_t(dp)=0$$，對$$h(t)$$兩供取期望值可得$$\mu(t)=kh(t)$$。

假設股價崩盤已產生，則$$\frac{dp}{p}$$可簡化為：

$$
\frac{dp}{p}=\mu(t)dt+\sigma t dW = k h(t) dt + \sigma(t)dW
$$

對上式兩側取期望值得：

$$
\mathrm{E}_t \left(\frac{dp}{p} \right )=kh(t)dt
$$

上式代入$$h(t)$$可得 LPPL方程式。

### LPPL方程

$$
\ln(p(t))=A+B(t_c-t)^m+C(t_c-t)^m\times \cos(\omega\ln(t_c-t)-\phi)
$$

* $$A>0$$為股票在臨界點的價格
* $$B=-kB^{'}/m$$
* $$C=-kC^{'} / \sqrt{m^2 +\omega^2}$$
* $$B(t_c-t)^m$$反應股價由正回饋機制出現的冪律增長特性；
* $$C(t_c-t)^m \cos(\omega \ln(t_c-t)-\phi)$$描述股價在臨近見頂並崩盤時呈對數週期振蕩，為對股價冪律增長行為的修正。



## 參考資料

* \[github] [https://github.com/Boulder-Investment-Technologies/lppls](https://github.com/Boulder-Investment-Technologies/lppls)
* [\[知乎\] 泡沫理論演算法求解概述及主流演算法對比(PSY-GSADF VS LPPLS)](https://zhuanlan.zhihu.com/p/401103573)。
* [\[知乎\] 泡沫檢測的幾篇綜述和文獻對比](https://zhuanlan.zhihu.com/p/400288921)。
* [\[知乎\] 分解log-periodic power laws(LPPL)模型](https://zhuanlan.zhihu.com/p/395621402)。
* [\[知乎\] LPPL 模型所刻畫的四種泡沫型別](https://zhuanlan.zhihu.com/p/396549896)。
* [\[知乎\]金融市場中的泡沫檢測|理論泡沫模型和經驗泡沫檢測綜述](https://zhuanlan.zhihu.com/p/400062912)。
* [\[知乎\] 【原理】技術分析與LPPL模型](https://zhuanlan.zhihu.com/p/424939548)。
* [\[知乎\] 【原理】利用“趨勢”做投資：LPPL模型推導](https://zhuanlan.zhihu.com/p/422467747)。
* \[個人] [Didier Sornette](https://emeritus.er.ethz.ch/about-us/people/sornette.html).
* [https://zhuanlan.zhihu.com/p/41931776](https://zhuanlan.zhihu.com/p/41931776)
* [破解股市泡沫之謎——對數週期冪率（LPPL）模型](https://www.kancloud.cn/wizardforcel/python-quant-uqer/186247)

論文

* \[book] Dean Fantazzini and Petr Geraskin, "[Everything you always wanted to know about log-periodic power laws for bubble modeling but were afraid to ask](https://www.taylorfrancis.com/chapters/edit/10.4324/9780429198557-3/everything-always-wanted-know-log-periodic-power-laws-bubble-modeling-afraid-ask-petr-geraskin-dean-fantazzini)," New Facets of Economic Complexity in Modern Financial Markets, pp. 30-55,  2019.

## 圖書

* Didier Sornette, "Why Stock Markets Crash: Critical Events in Complex Financial Systems, "Princeton University Press.
*
