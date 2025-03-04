---
description: Log-Periodic Power Law Singularity, 對數週期冪律奇點
---

# LPPLS模型

<figure><img src="../.gitbook/assets/image (66).png" alt="" width="360"><figcaption><p>正負(反)泡沫</p></figcaption></figure>

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

### 論文

* James A. Feigenbaum and Peter  G.O. Freund, "[Discrete Scaling in Stock Markets Before Crashes](https://www.worldscientific.com/doi/abs/10.1142/S021797929600204X)," International Journal of Modern Physics, Vol. 10, No. 27, pp. 3737-3745, 1996.
  * 本文提出了一個股票市場崩潰的關鍵點在一個系統的離散尺度不變性的圖像。臨界指數是複雜的，導致股票市場指數的對數週期波動。
* Didier Sornette, Anders Johansen and Jean-Philippe Bouchaud, "S[tock market crashes, Precursors and Replicas,](https://jp1.journaldephysique.org/articles/jp1/abs/1996/01/jp1v6p167/jp1v6p167.html) " Journal de Physique I France, No. 6, pp. 167-175 1996.
  * 本文分析了1987年10月市場崩潰前後的S\&P500指數的時間行為，並確定了隨機模式以及餘震特徵和特徵振盪。結合起來，它們都表明了一種動力學臨界點的影象，<mark style="color:blue;">具有特徵性的對數週期特徵</mark>，類似於最近發現的地震。這些觀察結果在其他較小的崩潰中得到了證實，並加強了股票市場作為自組織合作系統的一個例子的觀點。
* Anders Johansen and Didier Sornette, "[Large Stock Market Price Drawdowns are Outliers](https://www.risk.net/journal-risk/2161095/large-stock-market-price-drawdowns-are-outliers), " The Journal of Risk, Vol. 4, No. 2, pp. 69-110, 2001.
  * 下跌（drawdown, 從上一個區域性最大值到下一個區域性最小值的損失）提供了比變異數、風險值（VaR）或其他基於固定時間尺度收益分佈的度量更自然的真實的市場風險度量。
  * 約98%的下降機率分佈可以很好地由指數分佈（或具有略微粗尾的微小修改）表示，而少數最大的下降發生的速度明顯快於指數分佈的預測。這一點通過對替代資料的廣泛測試得到了證實。
  * 因此，非常大的下降分佈屬於其自身的一類且有特定的放大機制。 在所研究的市場中，只有大約一半的市場表現出類似的行為。
* Wei-Xing Zhou and Didier Sornette, "[Evidence of a Worldwide Stock Market Log- Periodic Anti-Bubble since mid-2000](https://www.sciencedirect.com/science/article/abs/pii/S0378437103008586)," Physics A, Vol. 330, No. 3, pp. 543-583, 2003.
  * 分析了38個世界股票市場指數，並確定了21個“看跌反泡沫”和6個“看漲反泡沫”。
  * 反泡沫(anti-bubbles)被定義為具有自相似膨脹對數週期振蕩的自強化價格軌跡。看跌反泡沫的特徵是冪律、價格（或價格對數）隨時間變化的下降和對數週期振蕩的擴大。我們認為，<mark style="color:blue;">看跌的反泡沫是由積極的價格對價格反饋產生的</mark>，這些反饋助長了整體悲觀情緒和負面市場情緒，而人際互動進一步加強了這種情緒。看漲的反泡沫在這裡首次被識別出來。
  * 最引人注目的發現是，<mark style="color:red;">大多數歐洲和西方股票市場指數以及其他股票指數都表現出與美國標準普爾500指數幾乎相同的對數週期冪律反泡沫結構</mark>。
* \[LPPL模型用於DJIA與HSI] Didier Sornette and Wei-Xing Zhou, "[Predictability of large future changes in major financial indices](https://www.sciencedirect.com/science/article/abs/pii/S0169207005000191), " International Journal of Forecasting, Vol 22, Issue 1, pp. 153-168, 2006.
  * 本文提出了一種系統演算法，用於測試社會系統中主體行為中集體自組織的存在性，並在 20 世紀的DJIA指數 和香港恆生指數(HSI)上進行測試。
  * 該演算法結合了關鍵現象、代理人期望的影響、多尺度分析以及稀疏資料模式識別的數學方法的想法。我們的演算法經過對DJIA指數本世紀三場重大崩盤的訓練，展現了卓越的泛化能力，並提前檢測到其他 8 次重大下跌或走勢變化。 HSI 的應用也給出了有希望的結果。對於識別演算法的變化，結果是穩健的。
* \[book] Dean Fantazzini and Petr Geraskin, "[Everything you always wanted to know about log-periodic power laws for bubble modeling but were afraid to ask](https://www.taylorfrancis.com/chapters/edit/10.4324/9780429198557-3/everything-always-wanted-know-log-periodic-power-laws-bubble-modeling-afraid-ask-petr-geraskin-dean-fantazzini)," New Facets of Economic Complexity in Modern Financial Markets, pp. 30-55,  2019.
* Didier Sornette, Ryan Woodard, Wanfeng Yan and Wei-Xing Zhou, "[Clarifications to questions and criticisms on the Johansen–Ledoit–Sornette financial bubble model,](https://www.sciencedirect.com/science/article/abs/pii/S0378437113004342) " Physica A, pp. 4417–4428, 2013.
  * 本文建立了具有有限時間奇異崩潰風險率的理性預期泡沫的Johansen-Ledoit-Sornette（JLS）模型，用以描述金融泡沫和崩潰的動態過程。它已成功地應用於許多不同市場的各種金融泡沫。
  * 然而，這些文獻中在理論和實證方面似乎都存在一些嚴重的誤解。這些問題中的一些源於JLS模型和相關作品的文獻的快速發展。為了消除可能的誤解和促進有用的未來發展，我們總結了這些常見的問題和批評有關的JLS模型，並綜合了目前的最先進的技術和現有的最佳實踐。
* L. Lin, R.E. Ren and D. Sornette, "[The volatility-confined LPPL model: A consistent model of ‘explosive’ financial bubbles with mean-reverting residuals](https://www.sciencedirect.com/science/article/abs/pii/S1057521914000350), " International Review of Financial Analysis, Vol. 33, pp. 210-225, 2014.
  * 利用具有臨界行為的隨機貼現因數的概念，我們提出了一個自洽的金融泡沫爆炸模型，該模型結合了均值回歸波動過程和隨機條件報酬，反映了非線性的正反饋和投資者信念和情緒的持續更新。
  * 有條件的期望報酬表現出快於指數的加速度，由加速振蕩裝飾，稱為“對數週期冪律”（LPPL）。殘差測試顯示，當應用於 GARCH 基準時，誤報率非常低 （0.2%）。
  * 我們的模型還提供了對泡沫持續時間的診斷：應用於1987年10月崩盤之前的時期，有明確的證據表明泡沫至少在4年前開始。
  * 我們確認了波動率限制的LPPL模型在過去二十年中世界上發生的其他七個主要泡沫的有效性和普遍性。使用貝葉斯推理，我們發現與標準基準相比，我們的模型具有非常強的統計偏好，這與Chang和Feigenbaum（2006）使用單位根模型進行殘差相矛盾。
* Z. Forró, Ryan Woodard, and Didier Sornette, "[Using trading strategies to detect phase transitions in financial markets](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.91.042803)," Physical Review E, Vol. 91, Issue 4, 2015.
  * LPPLS模型是智慧體之間正反饋及其分層動態組織的數學體現，在金融市場中具有重要的預測能力。我們發現，基於LPPLS的策略明顯優於隨機策略，並且它們在大量資產和時間段選擇方面是穩健的。<mark style="color:blue;">因此，價格動態明顯偏離了某些可預測性的隨機性，而這種隨機性可能與泡沫市場制度有關</mark>。
  * 我們的混合方法將金融與交易策略相結合，將關鍵現象與LPPLS相結合，表明以相變相關的資訊為目標，可以預測金融泡沫和崩潰，從而影響價格動態。
* Jerome Kreuser and Didier Sornette, "[Super-Exponential RE Bubble Model with Efficient Crashes](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3064668), " The European Journal of Finance, 2017.
  * 我們提出了一個動態的理性預期（RE）價格泡沫模型，旨在利用它進行最佳投資策略的評估。
  * 我們的泡沫模型被定義為幾何布朗運動，結合與正泡沫（和負泡沫）相關的單獨碰撞（和反彈）離散跳躍分佈。我們假設崩盤往往會有效地將多餘的泡沫價格恢復到接近“正常”或基本值（“有效崩盤”）。然後，RE條件意味著暴露於崩盤的風險資產的超額風險溢價是預期崩盤幅度的增加函式，而預期崩盤幅度本身隨著泡沫錯誤定價而增長：因此，泡沫價格越大，其後續增長率就越大。這種價格回報的正反饋是超指數價格動態的原型，以前曾被提出作為泡沫的一般定義。
  * 我們的泡沫模型還允許一系列小幅跳躍或長期修正。我們使用 RE 條件通過加速機率函式動態估計即時崩盤機率，具體取決於增加的預期收益。
  * 在展示了如何估計模型引數之後，我們通過獲得風險資產和無風險資產的最大化預期財富對數（凱利準則）的解析表示式，研究了泡沫模型背景下的最優投資問題。我們還獲得了最優投資的閉式近似。我們在七次歷史崩盤中展示了與60/40投資組合、經典凱利組態和風險資產相比，該方法的有優異表現，以及它如何減輕正負的跳躍。
* Didier Sornette, Peter Cauwels and Georgi Smilyanov, "[Can We Use Volatility to Diagnose Financial Bubbles? Lessons from 40 historical bubbles](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3006642), "Quantitative Finance and Economics, Vol. 2, No. 1, pp. 486-​594, 2018.
  * 本文研究了金融資產泡沫之前、期間和之後的價格波動，以發現可能的共性，並根據經驗檢驗波動是否可以用作不可持續的價格上漲和相關崩潰的指標或預警訊號。
  * 一些研究人員和金融從業者認為，歷史和/或隱含波動率在崩盤前會增加，但我們不認為這是一種一致的行為。我們研究了40個著名的泡沫，並使用創造性的圖形表示來捕捉波動性的瞬態動態，<mark style="color:red;">發現波動性的動態不會是隨後崩潰的有用預測</mark>。
  * <mark style="color:blue;">在大約三分之二的研究泡沫中，崩盤發生在波動性較低的一段時間之後</mark>，這讓人想起「暴風雨前的平靜」。 從傳統資產定價模型的角度來看，這種自相矛盾的行為進一步質疑了風險與回報之間的一般關係。
* Vladimir Filimonov, Guilherme Demos and Didier Sornette, "[Modified Profile Likelihood Inference and Interval Forecast of the Burst of Financial Bubbles, ](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2739832)"Quantitative Finance, pp. 1-​20, 2017.
* Diego Ardila and Didier Sornette, "[Dating the financial cycle: a wavelet proposition](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2775271), "Finance Research Letters, Vol. 19,  pp. 298-​304, 2016.
  * 我們建議<mark style="color:blue;">使用最大重疊離散小波變換（MODWT）來測定和分析金融週期</mark>。
  * 本文指出了從經典商業週期文獻中得出的方法的侷限性，同時強調了它們與小波分析的聯絡。基本的時頻不確定性原理要求用區間估計值代替轉捩點的點估計值，區間估計值本身就是分析尺度的函式。我們使用來自19個OECD國家的金融時間序列來說明該工具的適用性。
* Qun Zhang, Qunzhi Zhang and Didier Sornette, "[Early warning signals of financial crises with multi-​scale quantile regressions of Log-​Periodic Power Law Singularities](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2674128), "PLoS ONE Vol. 11, pp. 1-​43, 2016.
* Qunzhi Zhang, Didier Sornette, Mehmet Balcilar, Rangan Gupta, Zeynel Abidin Ozdemir and Hakan Yetkiner, "[LPPLS Bubble Indicators over Two Centuries of the S\&P 500 Index](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2727755), " Physica A, Vol. 458, pp. 126-​139, 2016.
* Jan Henrik Wosnitza and Didier Sornette," [Analysis of log-​periodic power law singularity patterns in time series related to credit risk](https://link.springer.com/article/10.1140/epjb/e2015-50019-9)," The European Physical Journal B Vol. 88, No. 97, pp. 1-​11, 2015.
* Wanfeng Yan, Ryan Woodard, and Didier Sornette, "I[nferring Fundamental Value and Crash Nonlinearity from Bubble Calibration](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1719124)," Quantitative Finance Vol. 14, No. 7, pp. 1273-​1282, 2014.

### 反泡沫(anti-bubbles)

* Anders Johansen and Didier Sornette, "[Financial "anti-​bubbles'': Log-​periodicity in Gold and Nikkei collapses](https://www.worldscientific.com/doi/abs/10.1142/S0129183199000437)," International Journal of Modern Physics C, Vol. 10, No. 4, pp. 563-​575, 1999.
  * 我們認為，交易員的羊群行為不僅會導致投機泡沫，金融市場估值可能加速高估，隨後可能出現崩盤，<mark style="color:red;">還會導致“反泡沫”，即市場在歷史高點後貶值減速</mark>。
  * 為此，我們提出了一個簡單的市場動態模型，在該模型中，需求緩慢下降，障礙逐漸熄滅，導致市場價格的冪律衰減，其特徵是對數週期振蕩減速。
  * 我們記錄了日本日經指數從1990年至今的這種行為，以及1980年之後的黃金期貨價格，兩者都是在歷史高點。
  * 非參數功率譜分析表明，存在具有較高統計顯著性的對數週期性，日經指數的優選尺度比為λ≈3.5，黃金期貨價格的優選尺度比為λ≈1.9，與導致崩盤的投機泡沫的值相當。
* Anders Johansen and Didier Sornette, "[Bubbles and anti-​bubbles in Latin-​American, Asian and Western stock markets: An empirical study](https://www.worldscientific.com/doi/abs/10.1142/S0219024901001218)", International Journal of Theoretical and Applied Finance, Vol. 4, No. 6, pp. 853-​920, 2001.
  * 本文確定了拉丁美洲和亞洲股市出現21個重大泡沫，隨後出現大規模崩盤或嚴重調整。
  * 我們發現，除了極少數例外，這些推測性氣泡可以用預測特定冪律加速度的泡沫的理性期望模型以及所謂的對數週期幾何模式來定量描述。該模型大大擴充套件了先前為世界主要金融市場（即美國和外匯市場）提出的泡沫後崩盤或嚴重修正的理性預期模型的適用性。
  * 根據我們的模型，分別使用價格和對數對模型預測的比較進一步表明，市場如此大幅度的下行運動只不過是前一個泡沫的耗盡，從而使市場回到均衡狀態。
  * 此外，1994年初新興市場的一連串危機也表明，一系列二級股票市場表現出密切相關的“反泡沫”。這表明，較小的股票市場不僅由於美國市場的總體影響而無法弱同步，而且由於1994年亞洲金融危機等外部因素，它們獨立於美國市場。
* Wei-Xing Zhou and Didier Sornette, "[Evidence of a Worldwide Stock Market Log-​Periodic Anti-​Bubble Since mid-​2000](https://www.sciencedirect.com/science/article/abs/pii/S0378437103008586), "Physica A, Vol. 330, pp. 543-​583, 2003.
  * 繼2000年8月開始對美國S\&P指數反泡沫進行調查後，我們分析了38個世界股票市場指數，並確定了21個“看跌反泡沫”和6個“看漲反泡沫”。
  * <mark style="color:red;">“反泡沫”被定義為具有自相似膨脹對數週期振蕩的自強化價格軌跡。</mark>從數學上講，熊市反泡沫的特徵是冪律、價格（或價格對數）隨時間變化的下降和對數週期振蕩的擴大。
  * 我們認為，<mark style="color:blue;">看跌的反泡沫是由積極的價格對價格反饋產生的，這些反饋助長了整體悲觀情緒和負面市場情緒，而人際互動進一步加強了這種情緒</mark>。
  * 牛市的反泡沫在這裡首次被識別出來。最引人注目的發現是，大多數歐洲和西方股票市場指數以及其他股票指數都表現出與美國S\&P500指數幾乎相同的對數週期冪律反泡沫結構。
  * 據發現，這些反泡沫大約在2000年8月同時在所有這些市場開始。這顯示了全球同步程度的顯著程度。因此，自2000年以來全球股票市場的下跌是一個國際事件，表明全球化正在加強。
*

## 圖書

* Didier Sornette, "Why Stock Markets Crash: Critical Events in Complex Financial Systems, "Princeton University Press.
*
