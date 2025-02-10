---
description: Temporal Convolution Network
---

# 時間卷積網路 (TCN)

## TCN

時序卷積網路主要可以解決時序的模式識別（Time Series Discovery）問題，模型架構由1D的全連線層（Fully Convolution Network）與卷積層組成。卷積層結合了因果卷積層（Causal Network）與擴張卷積（Dilated Network）兩種結構。

因果卷積一開始的提出：是為瞭解決圖片的分割為題，會跳過部分輸入，提升 image recognition的準確率，同時它允許卷積的時的輸入存在間隔取樣。

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>從時間序列中提取具有不同時間間隔的功能，並最終結合這些功能。</p></figcaption></figure>

#### 序列建模的時序預測

在因果卷積當中，定義了 {yt} 只受過去 {Xt, Xt-1, Xt-2, ..} 影響，並不受未來資料 {Xt+1, Xt+2, ..} 影響，並且對歷史有記憶；另外，全連線層確保了輸出與輸入維度一致

#### 彈性調整感受區大小（Receptive Field Size）

擴張卷積和一般卷積的不同在於：每一層 Hidden Layer 都和輸入序列大小一樣，越到因果卷積層的上層，卷積視窗越大（意味著空洞越多），除了提高感受野以外，同時能降低計算量。

* d: 擴張卷積、以 2 的指數遞增，決定在層的級別隔幾個空格傳遞至下一層。
* k: filter size，決定每一層之間取幾個值傳到下一層，下圖 (a) 每一層皆為 k=3。

下圖為 TCN 整體模型架構：(a) 為因果卷積示意圖 ; (b) 為殘差模組內部構造 ; (c) 為殘差卷積的跳層連線在 TCN 的示意圖（較下層的特徵跳層連線到上層，提高模型準確度）

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption><p>TCN論文圖1。TCN中的基本元素。</p></figcaption></figure>

##

## 參考資料

* [https://github.com/locuslab/TCN/tree/master/TCN](https://github.com/locuslab/TCN/tree/master/TCN)
* [https://arxiv.org/pdf/1803.01271.pdf](https://arxiv.org/pdf/1803.01271.pdf)
* [https://cyeninesky3.medium.com/%E6%99%82%E9%96%93%E5%8D%B7%E7%A9%8D%E7%B6%B2%E7%B5%A1-tcn-%E9%97%9C%E6%96%BC%E5%BE%9E%E9%A2%A8%E6%8E%A7%E9%A0%85%E7%9B%AE%E7%95%B6%E4%B8%AD%E7%9A%84%E5%AD%B8%E7%BF%92-11693d762f5](https://cyeninesky3.medium.com/%E6%99%82%E9%96%93%E5%8D%B7%E7%A9%8D%E7%B6%B2%E7%B5%A1-tcn-%E9%97%9C%E6%96%BC%E5%BE%9E%E9%A2%A8%E6%8E%A7%E9%A0%85%E7%9B%AE%E7%95%B6%E4%B8%AD%E7%9A%84%E5%AD%B8%E7%BF%92-11693d762f5)
