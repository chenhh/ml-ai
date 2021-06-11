# 條件期望值

## 條件期望值

> * $$\displaystyle \mathrm{E}(Y|X=k)=\sum_{h} h \cdot\mathrm{P}(Y=h|X=k)$$，在事件$$X=k$$下，$$Y$$的條件期望值。
> * $$\displaystyle \mathrm{E}(Y|X=k)=\int_{-\infty}^{\infty}y\cdot f_{Y|X}(y|x)dy$$
> * $$\mathrm{P}(Y=h|X=k) = \frac{\mathrm{P}(Y=h \cap X=k)}{\mathrm{P}(X=k)}$$

* 條件期望值$$\mathrm{E}(Y|X=k)$$在$$X=k$$給定後，其值已經決定了，因此為$$k$$的函數，即$$\mathrm{E}(Y|X=k) = f(k)$$。如果$$X$$之值未定時，則$$\mathrm{E}(Y|X) = g(X)$$。

### 條件期望值的性質

> 給定$$a_1, a_2 \in \mathbb{R}$$
>
> 1. $$\mathrm{E}(a_1Y_1+a_2Y_2|X)=a_1 \mathrm{E}(Y_1|X) + a_2 \mathrm{E}(Y_2|X)$$
> 2. $$\mathrm{E}(f(X)Y|X)=f(x)\mathrm{E}(Y|X)$$
> 3. 對於任意函數$$g$$，$$\mathrm{E}(\mathrm{E}(Y|X) g(X))=\mathrm{E}(Yg(X))$$
> 4. 若$$X,Y$$獨立，$$\mathrm{E}(Y|X)=\mathrm{E}(Y)$$
> 5. $$C$$為常數，$$\mathrm{E}(C|X)=C$$
> 6. $$\mathrm{E}(\mathrm{E}(Z|X,Y)|X)=\mathrm{E}(Z|X)$$

### 條件期望值為最佳預測值

> $$\displaystyle \mathrm{E}(Y|X) = \arg \min_{g(X)} \mathrm{E}(Y-g(X))^2$$，即$$\mathrm{E}(Y|X)$$為對於$$Y$$的最佳預測值。



