---
description: lag-operator
---

# 落後運算子

## 落後算子(lag operator)

> Definition: lag operator L
>
> $$L$$(有時使用符號$$B$$)稱為落後運算子，定義$$L^ky_t = L^k(y_t) \equiv y_{t-k}$$
>
> 其中$$L^k$$為落後運算子作用$$k$$次。
>
> 如果$$k<0$$為超前運算。

### 落後算子為線性算子

> <mark style="color:red;">由定義可得</mark>$$L$$<mark style="color:red;">為</mark>[<mark style="color:red;">線性算子</mark>](../../linear-algebra/linear-transform/#xian-xing-ying-she-zhuan-huan-linear-mapping-or-linear-transform)。
>
> * $$L^k(cy_t)=cL^k(y_t)=cy_{t-k}$$
> * $$L^k(x_t+y_t)=L^k x_t+L^ky_t=x_{t-k}+y_{t-k}$$
>
> <mark style="background-color:red;">L 把時間移位變成多項式運算，讓模型像代數方程一樣處理，簡化書寫和推導</mark>。

* 交換律：$$L^iL^j(y_t)=L^{i+j}(y_t)=y_{t-i-j}=L^jL^i(y_t)$$
* 分配律：$$\forall a,b \in \mathbb{R},L^k(ax_t+by_t)=aL^k(x_t) + bL^k(y_t)=ax_{t-k}+by_{t-k}$$
* 常數不受影響：$$\forall c \in \mathbb{R} ~, Lc=c$$
* \[單位運算]：$$L^0(y_t)=y_t$$，0的冪次方為原值。
* 負數冪次方為超前運算：$$L^{-k}y_t=y_{t+k}$$
* 幾何級數展開：$$\forall |c|<1 ~, (1+cL+c^2L^2+c^3L^3+\cdots)y_t = \frac{1}{1-cL}y_t$$

### 差分運算

$$y_t$$的<mark style="color:red;">一階差分</mark>可表示為$$\Delta y_t= y_t -y_{t-1}=y_t - Ly_t=(1-L)y_t$$。

<mark style="color:red;">二階差分</mark>可表示為$$\Delta^2 y_t =y_t-2y_{t-1}+y_{t-2}=(1-2L+L^2)y_t=(1-L)^2y_t$$。

以此類推，<mark style="color:red;">d階差分</mark>可表示為$$(1-L)^dy_t$$。

這種表達方式使得差分操作變得非常簡單，特別是在處理非平穩時間序列時。

## 落後多項式(polynomial in the lag operator)

> 有限期：$$\phi(L)=1-\phi_1L-\phi_2 L^2-\cdots - \phi_p L^p=\sum_{j=0}^p \phi_j L^j,~\phi_0=1$$
>
> 無限期：$$\phi(L)=1-\phi_1L-\phi_2L^2-\cdots-=\sum_{j=0}^\infty \phi_j L^j$$

可得$$\phi(L)y_t=(1-\phi_1L-\phi_2 L^2-\cdots - \phi_p L^p)y_t=y_t-\phi_1y_{t-1}-\phi_2y_{t-2}-\cdots-\phi_p y_{t-p}$$。

範例AR(2)：

* $$X_t = \phi_1 X_{t-1}+ \phi_2X_{t-2} + \epsilon_t$$，可改寫為$$(1-\phi_1 L - \phi_2 L^2)X_t=\epsilon_t$$。
* 其中$$P(L)=1-\phi_1 L - \phi_2 L$$是滯後多項式。

Ｃ範列MA(q)：$$X_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \theta_q \epsilon_{t-q}$$，可改為：$$X_t = (1+\theta_1 L + \theta_2 L^2 + \dots + \theta_q L^q)\epsilon_t$$。

## 線性遞迴關係式

遞迴關係式是一種描述序列中當前值與過去值之間關係的數學表示式，而落後算子的本質就是處理「過去值」或「滯後項」，因此它自然適合用於分析和求解遞迴關係式。

p階遞迴式：$$y_t=a_1 y_{t-1}+ \dots + a_p y_{y-p}+b$$

可改寫為：$$y_t = a_1 Ly_t + a_2 L^2 y_t+ \dots + a_p L^p y_t + b$$，

移項整理得：$$(1-a_1 L + a_2 L^2 + \dots + a_pL^p)y_t = b$$，可得$$\phi(L)y_t =b$$。其中多項式：$$\phi(L)=(1-a_1L - \dots - a_p L^p)$$

### 齊次方程式

當$$b=0$$時，遞迴關係式為$$\phi(L)y_t =0$$，這是一個齊次線性差分方程。其解取決於特徵方程(characteristic equation) $$\phi(z)=0$$。

1. 求解$$1-a_1z - \dots -a_p z^p=0$$。
2. 根據根的情況（實根或複根），構造通解。
3. 通解中的常數$$c_1, \dots, c_p$$需要通過初始條件$$y_0$$確定。

為了求解此遞迴關係式，假設解的形式為指數函式$$y_t = z^t$$，其中$$z$$為未知的常數。

因為指數函式在離散時間下具有自然的遞迴性質，如$$y_{t-1}=z^{t-1}$$，，適合描述動態系統的增長或衰減行為。

求解$$1-a_1z - \dots -a_p z^p=0$$。可得以下三種解的情形：

1. $$p$$個相異實根$$z_1, z_2, \dots, z_p$$，則通解為$$y_t= c_1 zZ_1^t + c_2 z_2^2 + \dots + c_p z_p^t$$。
2. 實根中有$$m$$重根$$z$$。通解為$$y_t = (c_1 + c_2 t + \dots c_m t^{m-1})z^t$$。
3. 複數根(必為共軛如$$a+b_i$$)。通解為$$y_t = a^t (c_1 \cos(bt)+ c_2 \sin (bt))$$

其中：

* 實根 ：表示指數增長或衰減(取決於$$|z|$$是否大於1)。
* 複根 ：表示振盪衰減或增長（哩取決於模長$$a$$)。
* 重根 ：表示多項式修正的指數行為。



範例：2階遞迴關係式

$$\begin{aligned} & y_t = a_1y_{t-1} + a_2 y_{t-2} \\ & \implies y_t = a_1(L y_t) + a_2 (L^2 y_t) \\  & \implies (1-a_1 L - a_2 L^2 ) y_t = 0 \end{aligned}$$

特徵方程：$$(1-a_1 z - a_2 z^2)=0$$

* 如果 $$z_1$$ 和$$z_2$$ 是實數且互不相同，解的形式是 $$y_t = (c_1 z_1^t + c_2 z_2^t)$$。
* 如果 $$z_1 = z_2$$​（重根），解的形式是 $$y_t = (c_1 + c_2 t) z_1^t$$。
* 如果 $$z_1$$​ 和 $$z_2$$ 是共軛複數（例如 $$z_1 = re^{i\theta}$$, $$z_2 = re^{-i\theta}$$），解的形式是 $$y_t = r^t (c_1 \cos(\theta t) + c_2 \sin(\theta t))$$。

代回原式再求$$c_1, c_2$$可得通解。

### 非齊次方程

$$b \neq 0$$ 時為非齊次方程。這是一個非齊次線性差分方程。其解由兩部分組成：

* 齊次解：對應於$$\phi(L)y_t = 0$$的解。
* 特解：滿足$$\phi(L)y_t=b$$的特定解。

## 特徵方程式(characteristic equation)

對於一個自回歸模型（AR 模型）或包含落後算子的多項式形式：$$\phi(L)y_t =b$$，其中$$\phi(L)=(1-a_1L - \dots - a_p L^p)$$是落後算子的多項式。

特徵方程式是透過令$$\phi(z)=0$$得到：$$1-\phi_1z - \phi_2 z^2 - \dots - \phi_p z^p=0$$，<mark style="color:red;">這個方程的解稱為特徵根，它們決定了模型的行為</mark>。

落後算子的特徵方程的解具有以下意義和應用：

1. **穩定性檢查** ：特徵根的模長決定模型是否穩定。(複數模長$$|z|=\sqrt{Re^2(z) + Im^2(z)}$$)
2. **單位根檢驗** ：特徵根的位置揭示序列是否平穩。
3. **差分操作** ：特徵根的位置指導如何進行差分以消除非平穩性。
4. **動態響應** ：特徵根的位置描述模型的長期行為。
5. **頻譜分析** ：特徵根的位置可用來研究序列的頻率特性。

### 特徵根的意義

特徵根的位置（在複數平面上的模長）決定了模型是否穩定(stationary)：

* 如果所有特徵根的模長 $$|z|>1$$，則模型是穩定的。
* 如果某些特徵根的模長$$|z| \leq 1$$，則模型是非穩定的。

例如AR(1)模型 $$y_t = \phi y_{t-1}+b$$，特徵方程為$$1-\phi z = 0 \implies z = \frac{1}{\phi}$$。

穩定條件為$$|z| > 1$$即$$|\phi| < 1$$。

<mark style="background-color:red;">穩定性對於時間序列建模非常重要，因為只有穩定的模型才能生成有限方差的預測</mark>。

### 單位根與非平穩性(unit root)

如果特徵方程有一個或多個根位於單位圓上（即$$|z|=1$$），則該模型存在單位根，表示序列是非平穩的。因為：

* 若$$z=1$$(單根)，該過程的長期記憶性會導致均值或方差隨時間變化，如random walk $$y_t = y_{t-1} + \epsilon_t$$，得$$(1-L)y_t = \epsilon_t$$。
* 若$$z=e^{i\omega}$$(複根)，則會導致季節性非平穩（Seasonal Non-Stationarity)。如$$(1-L^4)y_t = \epsilon_t$$$$z=1,-1, i, -i$$。
* **衝擊的永久影響**：在平穩序列中，白噪音衝擊$$\epsilon_t$$ 的影響會隨時間衰減。但單位根存在時，衝擊的影響不會消失，而是永久累積。
* **無界增長**：單位根過程的均值和方差無法保持穩定，可能呈現趨勢或無限發散的行為，這與平穩性的定義不符。

非平穩序列通常需要進行差分操作（例如一階差分$$\Delta y = y_t - y_{t-1}$$）以消除趨勢或季節性成分，從而使其變為平穩。

### 衝擊響應(Impulse Response)

特徵根的位置還決定了模型的動態響應特性：

* 如果特徵根是實數且$$|z|>1$$，則模型表現出指數衰減的行為 (衝擊逐漸衰減)。
* 如果特徵根是複數且$$|z|>1$$，則模型可能表現出振盪衰減的行為。
* 如果特徵根位於單位圓內（$$|z|<1$$），則模型可能是發散的 ((衝擊不衰減甚至成長)。

這些動態特性對於理解模型的長期行為和預測能力非常重要。
