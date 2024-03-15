# 模型選擇方法

## 簡介

在對一堆資料進行建模時，特別是分類和回歸模型，我們有很多的變數可供使用。選擇不同的變數組合可以得到不同的模型。

資訊量準則是用來衡量統計模型品質的一種常用指標，可以用來比較不同模型間的好壞，它的評估同時考慮了兩項重要因素：

* 模型對資料點的配適程度(Goodness of fit)。
* &#x20;模型複雜度(即引數個數)。

使用 mean square error (MSE)指標來量化估計模型與真實模型的誤差。

$$\mathrm{E}(y-\hat{y})^2 = \mathrm{Bias}(\hat{y})^2+\mathrm{Var}(\hat{y})^2+\sigma^2$$

可以知道，模型的誤差來自三個部分，分別是模型偏差(bias)、模型方差(變異程度，variance)以及隨機擾動的方差。其中，可以控制的誤差為模型偏差與模型方差。

由Bias–variance trade off得知要減少模型的偏差，勢必要增加模型複雜度，然而一旦增加複雜度，便會增加模型的方差。

資訊量準則一般可以表達成下列形式：

$$-2 \log \mathcal{L}(\theta~|~M) + \lambda |M|$$

其中，M 代表的是預計使用的候選模型，而|M|是指這些候選模型各自的引數個數。

第一項是在計算 likelihood function，也就是在給定一組資料的情況下，去看模型引數為特定值的可能性，它可以反應某個模型對該組資料的配適程度。第二項則稱作是懲罰項，它考慮的是因引數增加(模型複雜度變高)所需要付出的代價。

例如我們有5個變數，排列組合共有2的5次方，我們將有32個變量組合，可以訓練出32個模型。但是哪個模型更加的好呢，可用AIC, BIC與HQIC來選擇模型。

* $$AIC=2k-2\log(L)$$，$$L$$為模型MLE之值，$$k$$為模型的參數個數。
* $$BIC=\log(n)\times k - 2\log(L)$$，$$n$$為資料的筆數。
* $$HQIC=\log(\log(n))\times k -2 \log (L)$$

經過指標選出的模型，表示該模型是可選擇的模型集合上表現相對較好的模型，但不保證就是最好模型。

很多參數估計問題均採用似然函數(likelihood function)作為目標函數，當訓練資料足夠多時，可以不斷提高模型精度，但是以提高模型復雜度為代價的，同時帶來一個機器學習中非常普遍的問題，過度擬合。所以，模型選擇問題在模型復雜度與模型對資料集描述能力（即似然函數）之間尋求最佳平衡。

<mark style="color:red;">構造這些統計量所遵循的統計思想是一致的，就是在考慮擬合殘差的同事，依自變量個數施加“懲罰”</mark>。

這種基於資訊判據(AIC/BIC)的模型選擇非常快，但它依賴於對自由度的正確估計。該方式的假設模型必需是正確, 而且是對大樣本(漸近結果)進行推導，即資料實際上是由該模型生成的。當問題的背景條件很差時(特徵數大於樣本數)，該模型選擇方式會崩潰。

## AIC (Akaike (赤池) information criterion)

AIC是評估統計模型的複雜度和衡量統計模型「擬合」資料之優良性，但是儘量避免出現過度擬合（Overfitting）的情況，所以優先考慮的模型應是AIC值最小的那一個模型。。

在一般的情況下，AIC可以表示為：$$AIC=2k-2 \log(L)$$。

* $$-\log(L)$$​為模型的資料的擬合程度，模型參數越多或者復雜度越高，則該值越小。。

假設條件是模型的誤差服從獨立正態分佈。令$$n$$為觀察數，$$RSS$$為殘差平方和，那麼AIC變為：$$AIC=2k+ n\times \log(\frac{RSS}{n})$$。

AIC鼓勵資料擬合的優良性但盡量避免出現過度擬合（Overfitting）的情況。<mark style="color:red;">所以優先考慮的模型應是AIC值最小的那一個</mark>。赤池資訊量准則的方法是尋找可以最好地解釋資料但包含最少自由參數的模型。

## BIC/SIC (Bayesian/Schwarz information criterion)

$$BIC=\log(n)k - 2 \log(L)$$

BIC的懲罰項比AIC的大，考慮了樣本數量，樣本數量過多時，可有效防止模型精度過高造成的模型復雜度過高。

AIC和BIC的原理是不同的，<mark style="color:red;">AIC是從預測角度，選擇一個好的模型用來預測，BIC是從擬合角度，選擇一個對現有資料擬合最好的模型，</mark>從貝式因子的解釋來講，就是邊際似然最大的那個模型。

## HQIC (Hannan-Quinn information criterion)



## ARIMA模型

而在 ARIMA (p,q)模型中，一個很重要的步驟就是決定引數 p 和 q 要取多少，以達到最高的準確度。

1. 觀察法：ACF、PACF&#x20;
2. 資訊量準則(Information Criteria)：AIC、AICC、BIC。

### ACF

ACF要是在探討「同一變數」自己所產生的資料(realization)在不同時點的線性相關性。

MA(1) 在 lag 1 以後的資料，和當期資料已沒有甚麼相關性，ACF 呈現截斷的情形(cut off)。之所以會有此現象出現，正可以從 MA(q) 推導的 ACF function 中看出，在 lag h > q 時，X\_t+h 與 X\_t 的相關性會是0。這個特徵正好能讓我們判斷 MA(q) 的 q 應該要取多少。

觀察 AR(1) 的 ACF function，可以看到 ACF function 是隨著時間間隔增加而遞減，此現象也稱作是拖尾 (tail off)。之所以會有拖尾現象，正是因為 X\_t 中包含了過去所有樣本 X\_t-1、X\_t-2、 X\_t-3、…、X\_0 的資訊，而越久遠以前的資料對當期資料造成的影響會逐漸下降。很遺憾地，如此特性不像 MA(q) ACF function的截斷性質可以輕易分辨階數的取值，也就無法利用 ACF 來決定 AR(p) 模型的階數。

### PACF

ACF 是一個條件相關係數的概念，在已知或給定 X\_t+h 和 X\_t 之間所有樣本點資訊的情況下，可藉由這項指標得知 X\_t 還有沒有多餘的資訊可以拿來預測 X\_t+h。於是，我們做的事就是將 X\_t+1、X\_t+2、…、X\_t+h-1 對 X\_t+h 以及 X\_t 的線性相關影響去除。

AR(1) 所繪製出的 PACF function，從 lag 1 之後就發生截斷，與定義的概念相符。因此，我們可以利用這種特性，在繪製出樣本 PACF 後，能很快的判斷 AR(p) 的階數取值。

### 資訊量準則(Information Criteria)

* $$AIC=-2 \log \mathcal{L}(\theta) + 2 (p+q+1)$$
* $$AICC=-2 \log \mathcal{L}(\theta) + 2 (p+q+1)n/(n-p-q-2)$$
* $$BIC=-2 \log \mathcal{L}(\theta) + \log (n)(p+q+1)$$

BIC 和 AIC、AICC(簡稱 AIC 一族) 彼此間有個顯著的差異是 BIC 指標會受到樣本個數的影響，且隨著樣本數增加，BIC 對引數個數會給予更多的懲罰。相較之下，AIC 懲罰項的 λ 為常數 2 ，與 BIC 的 log(n) 相比更容易選到較複雜的模型(較多引數)，overfitting 的可能性也會增加。

對 AIC 、AICC而言，它們的設計原理是建立在預測之上，且其擁有漸進有效性(asymptotic efficient)的性質，<mark style="color:red;">當樣本足夠大時，AIC 幾乎可以在所有候選模型當中，找出預測能力最好的那個估計模型</mark>。

而 BIC 則是擁有模型一致性的性質(model consistency)，<mark style="color:red;">也就是如果真實的模型有在眾多候選模型當中， 當樣本足夠大時 BIC 剛好可以選到該真實模型</mark>。

在時間序列的議題當中，有很大一部分都是在做「預測」，且真實模型很難存在於候選模型集合當中，於是我們會傾向使用 AIC 一族的指標來衡量模型的好壞。另一方面，若建立模型的目的是偏重「解釋」，則較適合使用 BIC 指標。

## 參考資料

* <mark style="background-color:red;">\[AIC原始論文] Akaike, Hirotugu. "A new look at the statistical model identification." IEEE transactions on automatic control 19.6 (1974): 716-723</mark>.
* <mark style="background-color:red;">\[BIC/SIC原始論文] Schwarz, Gideon. "Estimating the dimension of a model." The annals of statistics (1978): 461-464</mark>.
* <mark style="background-color:red;">\[HQIC]原始論文] Hannan, Edward J., and Barry G. Quinn. "The determination of the order of an autoregression." Journal of the Royal Statistical Society: Series B (Methodological) 41.2 (1979): 190-195</mark>.
* [https://medium.com/@cindy050244\_52136/%E6%99%82%E9%96%93%E5%BA%8F%E5%88%97%E6%8E%A2%E7%B4%A2-%E4%B8%89-%E6%A8%A1%E5%9E%8B%E5%AE%9A%E9%9A%8E%E8%88%87%E7%AF%A9%E9%81%B8-2ebe90b121f9#48dc](https://medium.com/@cindy050244\_52136/%E6%99%82%E9%96%93%E5%BA%8F%E5%88%97%E6%8E%A2%E7%B4%A2-%E4%B8%89-%E6%A8%A1%E5%9E%8B%E5%AE%9A%E9%9A%8E%E8%88%87%E7%AF%A9%E9%81%B8-2ebe90b121f9#48dc)
