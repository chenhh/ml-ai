# 關聯結構(copula)

## 簡介

我們希望能夠建構適合描述多維度隨機變數的聯合分佈。多元常態分佈是文獻最常出現的多維度機率模式，然而許多現象卻非常態分佈所能描述。

當相異隨機變數互相之間並不獨立的時候，此時對於聯合分佈的建模會變得十分困難。此時，在已知多個隨機變數的邊緣分佈的條件下，Copula函數則是一個非常好的工具來對其相關性進行建模。

以存活變數的邊際分佈的特性為例，存活變數通常具偏斜(skewed)分佈，不具有對稱性。期望值與變異數是常態分佈最重要的參數，<mark style="color:blue;">然而動差容易受少部份的極端值影響</mark>，並不太適合用來描述偏斜的存活函數。

Copula的概念是Sklar在1959年研究多維分佈函數與低維邊際函數之間的關係的問題時首次引入。

優點：

* Copula是一種研究相依性測度的方法  。
* Copula是作為研究無標度（scale-free）依賴度量的一種方法  。
* Copula作為構造二維分佈族的起點，可用於多元模型分佈與隨機模擬。&#x20;

在研究中使用最多的 Copula 函數主要有阿基米德 Copula 函數族和橢圓 Copula 函數族兩大類。

* 橢圓 Copula 函數簇有t Copula函數 、Gaussian Copula函數等，兩者均有對稱的尾部相關性，在中心區域差別不大，差別主要體現在尾部的厚度。這類copula函數，同時通過已知的多元分佈來計算出來的。最為人所知的就是多元常態分配的copula，即高斯copula。
* 阿基米德 Copula 函數簇的分佈函數定義首先由Genest和Mackay在1986年給出，這一類函數有著統一的函數表達形式。根據不同的生成元函數能夠得到不同的阿基米德Copula函數，常見有：Frank Copula、Clayton Copula 及 Gumbel Copula。

### 應用領域

該工具最初是用在金融衍生品領域，該函數建模作為衍生品風險度量的工作進行使用。

在2008年金融危機中，這個工具被人廣發的提及，認為當時採用的高斯copula沒有能夠完整度量衍生品連帶之間的風險，從而導致一系列的違約，進而引發次貸危機、經濟危機。

也有人事後寫了“‘The Formula That Killed Wall Street’: The Gaussian Copula and Modelling Practices in Investment Banking”（殺死華爾街的公式：高斯copula和在投行的建模應用）的文章來介紹這個工具和現實社會經濟的關係。

##

## Sklar定理

> 以二元隨機變數為例，若$$H(x,y)$$是一個具有連續邊緣分佈$$F(x)$$ 與$$G(y)$$ 的二元聯合分佈函數，那麼<mark style="color:red;">存在唯一</mark>的Copula函數$$C$$ ，使得$$H(x,y)=C(F(x), G(y))$$ 。
>
> 反之，如果$$C$$是一個copula函數，而$$F$$和$$G$$是兩個任意的機率分佈函數，那麼由上式定義的$$H$$ 函數一定是一個聯合分佈函數，且對應的邊緣分佈剛好就是$$F$$ 和$$G$$ 。
>
> 假設有$$N$$個隨機變數$$X_1, X_2, \dots, X_N$$，它們各自的邊緣分佈分別為$$F_1(x_1), F_2(x_2),\dots, F_N(x_N)$$ ，它們的聯合分佈為 ，則<mark style="color:red;">存在唯一</mark>的將邊緣分佈和聯合分佈“連接”起來的函數$$C(\cdot)$$ ，使得$$H(x_1, x_2,\dots, x_N)=C(F_1(x_1), F_2(x_2),\dots, F_N(x_N))$$。
>
> 而根據邊緣分佈的CDF的逆變換，即$$x_i=F_i^{-1}(u_i), ~i=1,2,\dots, N$$ ，則Copula函數的表達形式：$$C(u_1, u_2, \dots, u_N)=H(F^{-1}_1(u_1), F^{-1}_2(u_2), \dots, F_N^{-1}(u_N))$$。

對於$$N$$個隨機變數的聯合分佈，可以將其分解為這$$N$$個變數各自的邊緣分佈和一個Copula函數，從而將變數的隨機性和耦合性分離開來。

其中，隨機變數各自的隨機性由邊緣分佈進行描述，隨機變數之間的耦合特性由Copula函數進行描述。換句話說，一個聯合分佈關於相關性的性質，完全由其Copula函數決定。

如果已知$$H$$ ，$$F$$ 和 $$G$$，則Copula函數可以表達為：$$C(x,y)=H(F^{-1}(u), G^{-1}(v))$$。此處這裡$$F^{-1}(u)$$代表$$F(x)$$的反函數，或者叫CDF的逆變換、逆累積分佈函數。

### 分佈函數(distribution function)&#xD;

> 邊際分佈函數（marginal distribution function）
>
> * $$F(x)=\mathrm{P}(X \leq x) \in [0,1]$$
> * $$G(y) = \mathrm{P}(Y \leq y) \in [0,1]$$
>
> 聯合分佈函數（joint distribution function）
>
> * $$H(x,y)=\mathrm{P}(X \leq x, Y \leq y) \in [0,1]$$
> * $$F(x)=\int_{y \in \mathbb{Y}} H(x,y)dy$$
> * $$G(y) = \int_{x \in \mathbb{X}}H(x,y) dx$$

* 分佈函數為非遞減且右連續(cadlag)的函數。
* 分佈函數的值域為$$[0,1]$$的子集合，但值域不一定連續。

### 機率積分變換（Probability Integral transform）

> 在機率論中，機率積分變換(也稱為均勻的普適性)是指將任意給定連續分佈的隨機變數的資料值轉換成具有標準均勻分佈的隨機變數的結果。
>
> 給定隨機變數$$X_1, X_2$$，而 $$U_1=F(X_1)$$、 $$U_2=F(X_2)$$分別是二者的累計機率分佈函數，則，$$U_1 \sim U(0,1), U_2 \sim U(0,1)$$。
>
> 換句話說，任何邊際分佈的CDF值都均勻分佈在區間\[0,1]上。如果從任意分佈中隨機抽取，那麼抽取該分佈的最大值(U=1)的機率與抽取可能的最小值(U=0)或中值(U= 5)的機率相同。而copula實際上是它所建模的隨機變數的CDFs的聯合分佈。

$$F_U(u)=\mathrm{P}(U \leq u)=\mathrm{P}(F(x) \leq u)=\mathrm{P}(F^{-1}(F(x)) \leq F^{-1}(u))=\mathrm{P}(x \leq F^{-1}(u))=F(F^{-1}(u))=u$$

## 二維關聯結構

> 一個二維的關聯結構是一個有以下性質的函數$$C$$：
>
> 1. \[定義域]$$\mathrm{dom}C=[0,1] \times [0,1]$$
> 2. $$C(0,u)=C(u,0)=0$$, $$C(u,1)=C(1,u)=u ~\forall u \in [0,1]$$
> 3. $$C$$為2-increasing，即$$C(v_1, v_2 ) - C(v_1, u_2) - C(u_1, v_2) + C(u_1, u_2) \geq 0, \\ ~ (u_1, u_2) \in [0,1]^2, ~ (v_1, v_2) \in [0,1]^2 \\ ~ 0 \leq u_1 \leq v_1 \leq 1, ~ 0 \leq u_2 \leq v_2 \leq 1$$

## 參考資料

* Sklar, A. Fonctions de répartition à n dimensions et leurs marges. Publ. Inst. Statist. Univ. Paris. 1959, 8: 229–231.
* [https://zhuanlan.zhihu.com/p/138800469](https://zhuanlan.zhihu.com/p/138800469)



