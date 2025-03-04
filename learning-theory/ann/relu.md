# ReLU

## 簡介

ReLU 全名為 Rectified Linear Unit，中譯為「修正線性單元」，是種類神經網路中激勵函式 (activation function，也可翻譯為活化函式)。

$$ReLU(x)= \begin{cases} x, & \text{ if } x \geq 0, \\ 0, & \text{ if } x < 0, \\ \end{cases}$$

<figure><img src="../../.gitbook/assets/image (101).png" alt="" width="333"><figcaption><p>ReLU</p></figcaption></figure>

## ReLU 與其他激勵函式的比較

<figure><img src="../../.gitbook/assets/image (102).png" alt="" width="480"><figcaption><p>常見激勵函式</p></figcaption></figure>

* [Sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) 作為 Logistic Regression 的激勵函式，是這個算式當中非線性特徵的由來。由於 Logistic Regression 的目的是做分類，其輸出是一個機率值，故其值域會介於\[0,1] 之間。在[反向傳播演算法](https://www.youtube.com/watch?v=ibJpTrp5mcE\&list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49\&index=12) (Backpropagation) 發明後，人們發現在計算神經網路中每一層結點的引數時，由於 Sigmoid 會把(−∞,∞) 的輸入對映到\[0,1] 之間，會造成在反向傳播引數時每一層的數字愈算愈小，到最後幾層的數字全都是 0 的梯度消失 (Gradient Vanishing) 現象。
* 後來出現的 [Hyperbolic tangent function (tanh)](https://en.wikipedia.org/wiki/Hyperbolic_function)（長高了的 Sigmoid，其值域在\[−1,1] 之間）也有類似的問題。
* 因此，在 Yoshua Bengio 的論文 中，提到以 ReLU 取代其它激勵函式的好處：
  * ReLU 較容易使得神經網路的結構變得稀疏，因為算出來引數為負的結點被視為沒有貢獻，因此輸出為 0，相當於是從神經網路中被拿掉了。
  * ReLU 的行為比較符合生物學當中觀察到的神經活化現象（全有全無律，也就是在刺激不夠大的時候，神經根本不會有反應回饋出現的現象）。
  * ReLU 的計算量比較小。

<figure><img src="../../.gitbook/assets/image (103).png" alt="" width="480"><figcaption><p>在神經生理方面，當刺激未達一定的強度時，神經元不會興奮，因此不會產生神經衝動。如果超過某個強度，才會引起神經衝動。ReLU 較好捕捉這個生物神經元的特徵. </p></figcaption></figure>

## 總結：選擇ReLU

* 可避免梯度消失問題 (vanishing gradient problem)。
* 類神經網路的稀疏性（奧卡姆剃刀原則）：Relu會使部分神經元的輸出為0，可以讓神經網路變得稀疏，緩解過度擬合的問題。但衍生出另一個問題是，如果把一個神經元停止後，就難以再次開啟（Dead ReLU Problem），因此又有 Leaky ReLU 類 (x<0時取一個微小值而非0), maxout (增加激勵函式專用隱藏層，有點暴力) 等方法.。
* 生物事實：全有全無律 (all or none law)：在神經生理方面，當刺激未達一定的強度時，神經元不會興奮，因此不會產生神經衝動。如果超過某個強度，才會引起神經衝動。Relu比較好的捕捉了這個生物神經元的特徵。
* 計算量節省：Relu 計算量小，只需要判斷輸入是否大於0，不用指數運算。
