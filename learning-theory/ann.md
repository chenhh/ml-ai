# 類神經網路\(neural network\)

## 神經元\(Neuron\)

![&#x55AE;&#x4E00;&#x795E;&#x7D93;&#x5143;](../.gitbook/assets/neuron-min.png)

一個神經元是有$$M+1$$個輸入的函數$$g$$得到初步輸出後，再經啟動函數得到最後的輸出$$\hat{y}$$。

* $$\hat{y} =f(\mathbf{w^{\top} x} + b)$$
* $$\mathbf{x} \in \mathbb{R}^{M \times 1}$$：輸入向量\(input vector\), 每筆資料是有$$M$$個特徵\(維度\)的實數值。
* $$\mathbf{w} \in \mathbb{R}^{M \times 1}$$ ：權重向量\(weights vector\)，每個特徵到神經元的權重值。
* $$b \in \mathbb{R}$$：神經元的偏差量\(bias\)。
* $$f(\cdot)$$：使用者自訂的啟動函數\(activation function\)。
* $$\hat{y} \in \mathbb{R}$$：輸出值或預測值\(output value or predicting value\)。

也可將偏差值與輸出合併視為輸入與權重$$\mathbf{x, w} \in \mathbb{R}^{(M+1) \times 1}$$，其中 $$x_{M+1} = b, w_{M+1}=1$$。

## 前饋神經網路\(Feed-forward network, FNN\)

* 此類網路資訊只有從輸入傳遞到輸出，沒有由輸出送回輸入的連結。
* single-hidden layer feedforward neural networks \(SLFNs\)是一個層狀的前饋結構，分為輸入層\(input layer\)，隱藏層\(hidden layer\)，與輸出層\(output layer\)，每一層都包含許多處理單元\(神經元\)。
* 網路系統中的每個處理單元都和其下一層的所有處理單元連接，但是同一層內的處理單元都不互相連接。

## 單隱藏層前饋神經網路\(Single hidden layer feedforward network, SLFN\)









## 



## 



