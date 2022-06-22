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
> $$L$$(有時使用符號$$B$$)稱為落後運算元，若$$L^ky_t \equiv y_{t-k}$$
>
> 由定義可得$$L$$為[線性算子](../../linear-algebra/linear-transform/#xian-xing-ying-she-zhuan-huan-linear-mapping-or-linear-transform)。
>
> * $$L^k(cy_t)=cL^k(y_t)=cy_{t-k}$$
> * $$L^k(x_t+y_t)=L^k x_t+L^ky_t=x_{t-k}+y_{t-k}$$

* $$\forall a,b \in \mathbb{R},~aL^ky_t+b=ay_{t-k}+b$$
* $$\forall c \in \mathbb{R} ~, Lc=c$$
* $$L^kL^jy_t = L^k y_{t-j}=y_{t-j-k}$$
* $$L^0y_t=y_t$$
* $$L^{-k}y_t=y_{t+k}$$
* $$\forall |c|<1 ~, (1+cL+c^2L^2+c^3L^3+\cdots)y_t = \frac{1}{1-cL}y_t$$

## 落後運子表示差分

* $$y_t$$的<mark style="color:red;">一階差分</mark>可表示為$$\Delta y_t= y_t -y_{t-1}=y_t - Ly_t=(1-L)y_t$$。
* <mark style="color:red;">二階差分</mark>可表示為$$\Delta^2 y_t =y_t-2y_{t-1}+y_{t-2}=(1-2B+B^2)y_t=(1-B)^2y_t$$。
* 以此類推，<mark style="color:red;">d階差分</mark>可表示為$$(1-B)^dy_t$$。

## 落後多項式(polynomial in the lag operator)

> 有限期：$$\phi(L)=1-\phi_1L-\phi_2 L^2-\cdots - \phi_p L^p=\sum_{j=0}^p \phi_j L^j,~\phi_0=1$$
>
> 無限期：$$\phi(L)=1-\phi_1L-\phi_2L^2-\cdots-=\sum_{j=0}^\infty \phi_j L^j$$

可得$$\phi(L)y_t=(1-\phi_1L-\phi_2 L^2-\cdots - \phi_p L^p)y_t=y_t-\phi_1y_{t-1}-\phi_2y_{t-2}-\cdots-\phi_p y_{t-p}$$



## 動差(moment)

隨機樣本的均數與變異數，<mark style="color:blue;">一般條件下會隨時間變化(時變）</mark>，即：

* $$\mathrm{E}(y_t) = \mu_t$$
* $$\mathrm{Var}(y_t)=\sigma_t^2$$

因為時間序列中的資料，過去與未來的資料不一定為獨立同分佈，具有相關性，可用自我共變異函數(autocovariance function)與自我相關函數(autocorrelation function, ACF)來計算序列的相關。

### k階自我共變異函數

> 給定時間序列$$\{y_t\}_{t=-\infty}^{\infty}$$且具有有限的變異數$$\mathrm{Var}(y_t) < \infty$$, 則其$$k$$階自我共變異函數定義為\$$

