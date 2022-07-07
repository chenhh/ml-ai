# Kelly公式

## 簡介

考慮賭局如下：勝率為$$p$$，賠率為$$b$$(壓1元，贏了可拿回$$1+b$$元，輸了全賠光)。

假設這賭局可不斷的重複玩下去，且每次都壓手上全部資金的比例$$0 \leq f \leq 1$$，則$$f$$之值為何時可使總資產增加速度最快?

令$$A_t$$​為第$$t$$​局後的總資產值，可分成以下兩種狀態：

1. 在$$t-1$$​局時賭贏，則$$A_t = A_{t-1}(1+bf)$$。
2. 在$$t-1$$時賭輸，則$$A_t = A_{t-1}(1-f)$$。

假設在$$T$$次的賭局中，贏了$$W$$​次，輸了$$L=T-W$$​次，初始資金為$$A_0$$​，則期末資金$$A_T$$​為$$A_T = A_0 (1+bf)^W (1-f)^L$$。

可得無限制式最佳化問題：

> $$\displaystyle  \max_{0 \leq f \leq 1} A_T = {\color{blue}A_0} (1+ {\color{green}b}{\color{red}{f}})^{\color{green}w}  (1-{\color{red}f})^{\color{green}L}$$

* 等號兩側取log，再考慮$$T \rightarrow\infty$$，可得：
* $$\displaystyle \lim_{T \rightarrow \infty} \log\left(\frac{A_T}{A_0}\right)^{\frac{1}{T}} = \lim_{T \rightarrow \infty} \frac{W}{T} \log(1+bf) + \frac{L}{T} \log(1-f)$$
* 因為玩無窮局時，$$\frac{W}{T} \rightarrow p$$，同理$$\frac{L}{T} \rightarrow (1-p)$$，因此要最大化函數為：$$p\log(1+bf) + (1-p)\log(1-f)$$，此為凹函數。
* 對函數中的f微分且設為0，可得$$\frac{pb}{1+bf} - \frac{1-p}{1-f}=0$$。
* 最後可得　$$f^* = \frac{p(1+b)-1}{b}$$ ，可解釋為<mark style="color:red;">期望淨利/賠率</mark>。

分析上述結果可知：

* 當勝率$$p=100\%$$時，最佳的資金比例為$$f=100\%$$。
* 當勝率$$p=50\%$$時，最佳資金比例為$$f=\frac{0.5b-0.5}{b}$$，
  * 此時若賠率$$b \leq 1$$，則$$f=0$$。
* <mark style="color:red;">因此在期望淨利不夠高時，就不要下注，反之期望淨利高於賠率時，就依比例下注</mark>。

## Vince最佳化比例

Kelly公式的推導中，關鍵在於固定的勝率$$p$$​與賠率$$b$$。假設每次下注總資金比例$$f$$​，則下期資金變化在賭贏時為$$(1+fb)$$​，而在賭輸時為$$(1-f)$$​。再經過$$T$$次下注後，輸贏的比例會呈現$$p$$​與$$1-p$$​的分佈，此時將每期損益連乘的式子微分求極值，可得最最佳的$$f^{*}$$。

