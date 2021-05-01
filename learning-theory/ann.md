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

## 



