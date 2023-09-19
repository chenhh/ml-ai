# 停時(stopping time)

## 簡介

停時這是指一個隨機過程停止表現其狀態的那個時間點，因為我們不會事先知道它什麼時候會停止，這個時間點通常是個隨機變數。通常是當作一個停止機制，只要我們的隨機過程符合某個條件，就讓它停下來， 並且把第一次符合那個條件的時間點當作停時。

關於隨機過程$$X_1,X2, X3, \dots$$的停時是隨機變數$$\tau$$ ，這一隨機變數具有如下性質：對於每一個時間 ，事件 $$\tau=t$$ 的發生與否僅取決於$$X_1,X_2, \dots,X_t$$ 的取值。從定義中可以感受到的直覺是在任一特定時刻$$t$$，可以判別在這一時刻隨機過程是否到了停時。

停時為隨機變數，且等價於停止過程(stopping process)，即初始值為1，在某時刻變為0隨機過程。討論詳見Fischer(2013)。

## 停時

> 定義：停時
>
> 給定$$I=[0, \infty)$$與機率空間$$(\Omega, \mathcal{F}, \mathcal{F}_t, \mathrm{P})$$，則隨機變數$$\tau: \Omega\rightarrow I \cup \{\infty\}$$稱為停時，若滿足$$\forall t \in I, \{ \tau \leq t \} \in \mathcal{F}_t$$。
>
> $$\forall t \in I, \{\tau = t\} \in \mathcal{F}_t$$。

$$\forall t \in I, ~$$$$\{\tau \leq t\} \in \mathcal{F}_t$$<mark style="color:red;">的意義就是，在每一個時間</mark>$$t$$<mark style="color:red;">所擁有的資訊</mark>$$\mathcal{F}_t$$<mark style="color:red;">，均足夠判斷是否在間</mark>$$t$$<mark style="color:red;">停下來，或者在之前就停下來，而不需要使用到未來</mark>$$\{\tau > t\}$$<mark style="color:red;">的資訊</mark>。停時就是滿足一定可測條件的隨機時間。截止到目前為止，所擁有的資訊能足夠做出決定是否停止。





### 停時範例

現實生活中停時的例子如賭徒離開賭桌的時刻，這一時刻可能是賭徒以前贏得錢財的函數（例如在賭徒沒有錢時，他才可能離開賭桌），但是他不可能根據還未完成的賽局的結果來選擇離開還是留下。

* 假設你現在準備從機場坐車回家，這時候家人打電話問：「還有多久到家呀？」，你當然回答不了一個精準的時間了，這時候你選擇下車的時間$$\tau$$就是一個隨機變數。而在回家路上的每個時間$$t$$ ，你都能夠判斷下車或者不下車。此已經滿足$$\{\tau \leq t \} \in \mathcal{F}_t$$，因為在時間$$t$$你所有的資訊足夠用以判斷是否應該下車了，所以$$\tau$$是停時(可選擇)。
* 如果出發十分鐘後，車子突然爆胎，那你選擇下車的時間還是停時嗎？依定義將$$\tau$$限制在{出發十分鐘後爆胎}這個集合上還是停時。因為在每個時刻$$t$$你都能夠判斷是否下車。即使爆胎了之後，你也能夠做出“下車”這個判斷。
* 如果剛上車後不久你發現車上的油只夠跑十公里了。假設你對你家離機場的距離沒有概念，那麼你選擇下車的時間 $$\tau$$不是停時。因為你此時難以判斷是否應該下車：如果你家離機場只有五公里，那麼不下車是最方便的。但如果你家離機場有二十公里，你就應該下車，因為出機場以後說不定就不好打車了。也就是說，這時候$$\tau$$ 是“無法做出選擇”的，所以不是停時。
* 假設你在坐地鐵，但是地鐵上沒有任何站名提醒，你只知道要在倒數第二站下車。你選擇下車的時間依然用$$\tau$$表示，此時你在途中任何時刻$$t$$ 都不能判斷是否應該下車，因為直到終點你才會知道哪站是倒數第二站。所以說$$\tau$$不是一個停時。
* 如果我們知道明天股票會虧本於是我們選在在今天賣，那麼賣的時間就不是一個停時。



## 參考資料

* [https://www.zhihu.com/question/24358372](https://www.zhihu.com/question/24358372)
* [https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6](https://zh.wikipedia.org/zh-tw/%E5%81%9C%E6%97%B6)
* [https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf](https://web.archive.org/web/20120226140702/http://www.bramdejonge.nl/pdf/stoppingtimes.pdf)
* [https://ece.iisc.ac.in/\~parimal/2020/spqt/lecture-04.pdf](https://ece.iisc.ac.in/\~parimal/2020/spqt/lecture-04.pdf)
* [Tom Fischer, "On simple representations of stopping times and stopping time sigma-algebras," _Statistics & Probability Letters_, Vol. _83, No._ 1,pp. 345-349, 2013](https://doi.org/10.1016/j.spl.2012.09.024).
