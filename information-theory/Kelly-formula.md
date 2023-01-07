# Kelly公式

## 簡介

考慮賭局如下：勝率為$$p$$，賠率為$$b$$(壓1元，贏了可拿回$$1+b$$元，輸了全賠光)。

假設這賭局可不斷的重複玩下去，且每次都壓手上全部資金的比例$$0 \leq f \leq 1$$，則$$f$$之值為何時可使總資產增加速度最快?

令$$v_t$$​為第$$t$$​局後的總資產值，可分成以下兩種狀態：

1. 在$$t-1$$​局時賭贏，則$$v_t = v_{t-1}(1+bf)$$。
2. 在$$t-1$$時賭輸，則$$v_t = v_{t-1}(1-f)$$。

假設在$$T$$次的賭局中，贏了$$w$$​次，輸了$$l=T-w$$​次，初始資金為$$v_0$$​，則期末資金$$v_T$$​為$$v_T = v_0 (1+bf)^W (1-f)^l$$。

可得無限制式最佳化問題：

> $$\displaystyle  \max_{0 \leq f \leq 1} v_T = {\color{blue}v_0} (1+ {\color{green}b}{\color{red}{f}})^{\color{green}w}  (1-{\color{red}f})^{\color{green}l}$$

* 等號兩側取log除以$$T$$，可得平均資產報酬率，再考慮$$T \rightarrow\infty$$，可得：
* $$\displaystyle \lim_{T \rightarrow \infty} \log\left(\frac{v_T}{v_0}\right)^{\frac{1}{T}} = \lim_{T \rightarrow \infty} \frac{w}{T} \log(1+bf) + \frac{l}{T} \log(1-f)$$
* 因為玩無窮局時，$$\frac{w}{T} \rightarrow p$$，同理$$\frac{l}{T} \rightarrow (1-p)$$，因此要最大化函數為：$$p\log(1+bf) + (1-p)\log(1-f)$$，此為凹函數。
* 對函數中的f微分且設為0，可得$$\frac{pb}{1+bf} - \frac{1-p}{1-f}=0$$。
* <mark style="color:red;">最後可得</mark>　$$f^* = \frac{p(1+b)-1}{b}$$ <mark style="color:red;">，可解釋為期望淨利/賠率</mark>。

分析上述結果可知：

* 當勝率$$p=100\%$$時，最佳的資金比例為$$f=100\%$$。
* 當勝率$$p=50\%$$時，最佳資金比例為$$f=\frac{0.5b-0.5}{b}$$，
  * 此時若賠率$$b \leq 1$$，則$$f=0$$。
* <mark style="color:red;">因此在期望淨利不夠高時，就不要下注，反之期望淨利高於賠率時，就依比例下注</mark>。

### 投資平均報酬率

> 投資人的$$T$$期平均報酬率為$$\displaystyle \overline{r} =  \frac{1}{T} \log\left(\frac{v_T}{v_0}\right)$$，針對平均報酬率最大化求最佳投資組合。

因為$$\displaystyle \begin{aligned} & \frac{1}{T} \left(   \log\left( \frac{v_1}{v_0} \right) +   \log\left( \frac{v_2}{v_1} \right) +   \dots +  \log\left( \frac{v_T}{v_{T-1}} \right)     \right)   \\ & = \frac{1}{T} \left(    \log\left( \frac{v_1}{v_0} \frac{v_2}{v_1} \dots \frac{v_T}{v_{T-1}} \right) \right)	 \\ &=  \frac{1}{T} \log \left( \frac{v_T}{v_0} \right)  \end{aligned}$$

## Vince最佳化比例

Kelly公式的推導中，關鍵在於固定的勝率$$p$$​與賠率$$b$$。假設每次下注總資金比例$$f$$​，則下期資金變化在賭贏時為$$(1+fb)$$​，而在賭輸時為$$(1-f)$$​。再經過$$T$$次下注後，輸贏的比例會呈現$$p$$​與$$1-p$$​的分佈，此時將每期損益連乘的式子微分求極值，可得最最佳的$$f^{*}$$。

Vince的方法使用持有期報酬率(holding period return, HPR)避開固定機率和賠率的限制。

假設有10筆交易的損益為19、8、-7、10、-11、-5、-3、20、12、-15。其中最大損損為-15。

* 第一次交易的HPR為 $$HPR1 = 1 +f(- \frac{proft}{\text{max loss}}) = -1 +f(\frac{-19}{-15})$$。
* 第二次交易的HPR為 $$HPR2 = 1 +f(- \frac{proft}{\text{max loss}}) = -1 +f(\frac{-7}{-15})$$。
* ...
* 第十次交易的HPR為$$HPR10 = 1 +f(- \frac{proft}{\text{max loss}}) = -1 +f(\frac{-15}{-15})=1-f$$。

這十次交易的幾何平均數為 $$\displaystyle \left( \prod_{i=1}^{10} HPR_i \right)^{\frac{1}{10}}$$為最後財產值。

因此最佳的比例為$$f^{*} = \max_{f} \displaystyle \left( \prod_{i=1}^{10} HPR_i \right)^{\frac{1}{10}}$$。

