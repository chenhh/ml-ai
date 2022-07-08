# 模型選擇方法

## 簡介

在對一堆資料進行建模時，特別是分類和回歸模型，我們有很多的變數可供使用。選擇不同的變數組合可以得到不同的模型。



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



## 參考資料

* <mark style="background-color:red;">\[AIC原始論文] Akaike, Hirotugu. "A new look at the statistical model identification." IEEE transactions on automatic control 19.6 (1974): 716-723</mark>.
* <mark style="background-color:red;">\[BIC/SIC原始論文] Schwarz, Gideon. "Estimating the dimension of a model." The annals of statistics (1978): 461-464</mark>.
* <mark style="background-color:red;">\[HQIC]原始論文] Hannan, Edward J., and Barry G. Quinn. "The determination of the order of an autoregression." Journal of the Royal Statistical Society: Series B (Methodological) 41.2 (1979): 190-195</mark>.
