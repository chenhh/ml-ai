# 時間序列性質

## 基本概念

給定時間序列$$\{y_t\}_{t=1}^T$$，$$y_t$$為第$$t$$期的資料(純量或向量)。

* $$y_{t-k}$$稱為$$y_t$$<mark style="color:red;">落後</mark>$$k$$<mark style="color:red;">期(kth lag)</mark>的資料。
* $$\Delta y_t \equiv y_t - y_{t-1}$$稱為$$y_t$$的<mark style="color:red;">一階差分</mark>。

註：$$\begin{aligned} \Delta \ln y_t &= \ln y_t - \ln y_{t-1} \\ & \approx  \left[ \ln y_{t-1} + \frac{1}{y_{t-1}}(y_t - y_{t-1})  \right] - \ln y_{t-1} \\ & =  \frac{y_t - y_{t-1}}{y_{t-1}}   \end{aligned}$$

當$$y_t$$變動不大時，$$\Delta \ln y_t$$是變動量的良好近似值，經常用於報酬率的計算。

## 落後算子(lag operator)

> Definition: lag operator L
>
> $$L$$稱為落後運算元，若$$L^ky_t \equiv y_{t-k}$$
>
> 由定義可得$$L$$為[線性算子](../linear-algebra/linear-transform/#xian-xing-ying-she-zhuan-huan-linear-mapping-or-linear-transform)。

* $$\forall a,b \in \mathbb{R},~aL^ky_t+b=ay_{t-k}+b$$
* $$\forall c \in \mathbb{R} ~, Lc=c$$
* $$L^kL^jy_t = L^k y_{t-j}=y_{t-j-k}$$
* $$L^0y_t=y_t$$
* $$L^{-k}y_t=y_{t+k}$$
* $$\forall |c|<1 ~, (1+cL+c^2L^2+c^3L^3+\cdots)y_t = \frac{1}{1-cL}y_t$$

## 落後運算多項式

使用落後運算元，$$y_t$$的一階差分可表示為$$\Delta y_t= y_t -y_{t-1}=y_t - Ly_t=(1-L)y_t$$。
