# 資訊熵(information entropy)

## 簡介

由於無序、混亂、不確定性或驚奇可以被視為資訊的不同色調，熵作為其衡量標準就顯得非常方便。

考慮一個隨機實驗，其結果為$$x_1, x_2, \dots , x_N$$的機率分別為$$p_1, p_2, \dots, p_N$$。 我們可以說，這些結果是離散隨機變數$$X$$的值。$$X$$的每個值$$x_i$$代表一個事件，其發生的機率為$$p_i$$。事件$$x_i$$的機率$$p_i$$可以解釋為對事件$$x_i$$發生的不確定性的衡量。我們也可以說，事件$$x_i$$的發生提供了一個關於該機率$$p_i$$正確的可能性的測量資訊（Batty，2010）。如果$$p_i$$很低，比如說0.01，那麼我們有理由確信事件$$x_i$$不會發生，如果$$x_i$$真的發生了，那麼對於$$p_i=0.01$$的$$x_i$$的發生會有很大的驚訝，因為我們對它的預期是高度不確定的。另一方面，如果$$p_i$$非常高，比如說$$0.99$$，那麼就有理由肯定事件$$x_i$$會發生，如果$$x_i$$真的發生了，那麼對於$$p_i=0.99$$的$$x_i$$的發生幾乎不會有任何驚訝，因為我們對它的預期是相當確定的。

事件發生的不確定性表明，隨機變數可能具有不同的值。只有在事件存在不確定性的情況下，通過觀察才能獲得資訊。<mark style="color:red;">如果一個事件發生的機率很高，它所傳遞的資訊就比較少，反之亦然</mark>。另一方面，需要更多的資訊來描述機率較低或更不確定的事件，或減少對這種事件發生的不確定性。<mark style="color:red;">同樣地，如果一個事件更確定會發生，那麼它的發生或觀察所傳遞的資訊就會更少，需要更少的資訊來描述它。這表明，一個事件的不確定性越大，其發生所傳遞的資訊就越多，或需要更多的資訊來描述它</mark>。這意味著熵、資訊、不確定性和驚奇之間存在著聯絡。

可以根據發生的機率來衡量不確定性或其補充的確定性或資訊。如果$$p(x_i)=0.5$$，發生的不確定性將是最大的。應該注意的是，不確定性度量的分佈不應基於實驗的單一事件的發生，而應基於來自互斥事件集合的任何事件，其聯合體等於實驗或所有結果的集合。對事件集合的不確定性的衡量被稱為熵。因此，<mark style="color:red;">熵可以被解釋為在實驗之前對事件的不確定性的衡量</mark>。一旦進行了實驗，關於事件的結果是已知的，不確定性就被消除了。這意味著，實驗產生的關於事件的資訊等於事件集合的熵，意味著不確定性等於資訊。

現在問題來了。當兩個獨立的事件$$x$$和$$y$$以機率$$p_x$$和$$p_y$$發生時，如何計算資訊量？$$x$$和$$y$$共同發生的機率是$$p_xp_y$$。符合前述邏輯的算法是從它們的共同發生中獲得的資訊，將是它們發生機率的倒數，即$$1/(p_xp_y)$$。這表明，此資訊不等於從事件$$x$$的發生中獲得的資訊$$1/p_x$$和從事件$$y$$的發生中獲得的資訊$$1/p_y$$之和。即$$\displaystyle \frac{1}{p_x p_y} \neq \frac{1}{p_x} + \frac{1}{p_y}$$。

上述可使用函數$$g(\cdot)$$使等號成立，即$$\displaystyle g\left(\frac{1}{p_x p_y} \right) = g \left( \frac{1}{p_x} \right) + g\left( \frac{1}{p_y} \right)$$，而使等號成立的$$g(x)=-\log(x)$$，可得$$\displaystyle -\log\left(\frac{1}{p_x p_y} \right) = -\log \left( \frac{1}{p_x} \right) -\log \left( \frac{1}{p_y} \right)$$。

因此，我們可以總結出，從任何機率為$$p$$的事件發生中獲得的資訊是$$\log（\frac{1}{p}）=-\log p$$。<mark style="color:red;">Tribus（1969）認為</mark>$$-\log p$$<mark style="color:red;">是對機率為</mark>$$p$$<mark style="color:red;">的事件發生的不確定性的衡量，或者說是對該事件發生的驚訝的衡量</mark>。這個概念可以擴展到一系列以機率$$p_1, p_2, \dots, p_N$$發生的$$N$$個事件。這就導致了下面要描述的Shannon熵。

## 熵的類型

有幾種類型的資訊熵（Kapur, 1989），如Shannon熵（Shannon, 1948）、Tsallis熵（Tsallis, 1988）、指數熵（Pal and Pal, 1991a, b）、epsilon熵（Rosenthal和Binia，1988）、演算法熵（Zurek，1989）、Hartley熵（Hartley，1928）、Renyi熵（1961）、Kapur熵（Kapur，1989），等等。

其中最<mark style="color:red;">重要的是Shannon熵、Tsallis熵、Renyi熵和指數熵</mark>。

### Shannon熵

1948年，Shannon提出了現在被稱為資訊理論的或簡單的資訊熵。它現在更經常被稱為Shannon熵。<mark style="color:red;">他意識到，當資訊被觀祭到或給定時，事件的不確定性會減少或消除，因此他尋求一種不確定性的衡量標準</mark>。對於一個機率分佈$$P=\{p_1, p_2, \dots , p_N \}$$，其中$$p_1, p_2, \dots, p_N$$是隨機變數$$X$$或隨機實驗的$$N$$個結果（$$x_i, ~i=1,2,\dots,N$$）的機率，也就是說，每個值都對應於一個事件，我們可以寫成：

$$\displaystyle -\log \left( \frac{1}{p_1 p_2 \dots p_N} \right) = -\log \left( \frac{1}{p_1} \right) -\log \left(\frac{1}{p_2} \right) - \dots -\log \left(\frac{1}{p_N} \right)$$--(1.9)

上式說明了通過觀察$$N$$個事件的聯合發生所獲得的資訊。

可將平均資訊量視為以下期望值形式：$$\displaystyle H=-\sum_{i=1}^N p_i \log p_i$$--(1.10)，其中$$H$$為Shannon定義的熵。

式（1.10）所給出的Shannon（1948）的資訊熵與式（1.4b）所給出的熱力學熵的形式相似，後者的發展可以歸功於Boltzmann和Gibbs。因此，一些研究者將$$H$$命名為Shannon-Boltzmann-Gibbs熵（見Papalexiou和Koutsyiannis，2012）。在本文中，我們將稱其為Shannan熵。

(1.4)或(1.10)的熵可改寫如下：

$$\displaystyle \mathrm{H}(X)=\mathrm{H}(P)=-K \sum_{i=1}^N p(x_i) \log(p(x_i)) ~ \text{s.t.} ~ \sum_{i=1}^N p(x_i) = 1$$--(1.11)

* 其中$$\mathrm{H}(X)$$為隨機變數$$X$$的熵，$$X: \{x_1, x_2 ,\dots, x_N\}$$，$$P: \{p_1, p_2, \dots, p_N\}$$為$$X$$的分佈，$$K$$為依賴於對數基數的參數。如果使用不同的熵單位，那麼對數的基數就會改變。對數就會改變。例如，人們用位元表示基數2，用Napier或nat或nit表示基數e，而 分貝或logit或docit表示基數10。

通常取$$K=1$$，因此資訊熵如下：

$$\displaystyle \mathrm{H}(X)=\mathrm{H}(P)=-\sum_{i=1}^N p(x_i) \log p(x_i)$$--(1.12)

$$\mathrm{H}(X)$$<mark style="color:blue;">由式(1.12)表示隨機變數</mark>$$X$$<mark style="color:blue;">或其機率分佈</mark>$$\mathrm{P}(X)$$<mark style="color:blue;">的資訊量。它是不確定性的量的度量，或間接地是</mark>$$x$$<mark style="color:blue;">單個值的平均資訊量。方程(1.12)滿足了許多需求，如連續性、對稱性、可加性、可擴展性、遞迴性等(Shannon and Weaver, 1949)，並且與熱力學熵具有相同的表達形式，因此將</mark>$$H$$<mark style="color:blue;">定義為熵</mark>。

（1.12）指出，$$H$$是對實驗結果的不確定性的衡量，或者是對實驗中獲得的資訊的衡量，它可以減少不確定性。它也說明了機率分佈為$$(p_1 , p_2 , \dots , p_N)$$的訊號源所傳輸的資訊量的期望值。

<mark style="color:red;">Shannon熵可以被看作是猜測一種結果性質的觀察者的優柔寡斷，或者看作是可以找到不同安排的系統的無序性。這種測量方法只考慮了一個事件發生的可能性，而不是它的意義或價值。這就是熵概念的主要侷限性</mark>（Marchand, 1972）。因此，$$H$$有時被稱為資訊指數或資訊含量。

如果$$X$$是一個決定性的變數，那麼它取某一數值的機率是 1，所有其他備選值的機率為零。那麼，（1.12）可得 $$\mathrm{H}(X)=0$$，可以看作是熵函數的下限值 。這相當於絕對的確定性，也就是說，沒有不確定性，系統是完全有序的。另一方面，當所有$$x_i$$的可能性相同時，也就是說。 變數是均勻分佈的$$（p_i = 1/N, i = 1, 2, \dots, N）$$，則$$\mathrm{H}(X)=\mathrm{H}_{\max}(X)=\log N$$--(1.13)

這表明熵函數達到最大值，式(1.13)定義了上限或將導致最大熵。這也揭示了結果的不確定性最大。由式(1.10)和式(1.13)可知，<mark style="color:red;">事件數量越大，熵測度越大</mark>。這在直覺上很吸引人，因為從更多事件的發生中獲得更多資訊，<mark style="color:red;">當然，除非事件的發生機率為零。當不確定性最大或無序性最大時，熵最大</mark>。

現在我們可以說，任何變數的熵總是在以下範圍內呈現正值：

$$0 \leq \mathrm{H}(X) \leq N$$--(1.14)

一般的情況是許多機率分佈位於這兩個極端之間。這表明$$H$$存在有序-無序連續統；<mark style="color:red;">也就是說，對分佈形式的更多約束導致熵的減少</mark>。統計上最可能的狀態對應於最大熵。我們可以進一步擴展這種解釋。

如果有兩個結果相等的機率分佈，一個如上所述（即$$p_i=p$$，$$i=1,2,\dots,N$$），另一個為$$q_i=q$$，$$i=1,2, \dots,M$$。，那麼就可以確定這兩個分佈的資訊含量之差為$$\Delta H = H_p - H_q = \log_2 p - \log_2 q = \log_2 (p/q)$$ bits，其中$$H_p$$是$$\{p_i, ~ i = 1, 2, \dots , N\}$$的資訊含量或熵，$$H_q$$是$$\{q_i ,~ i = 1, 2, \dots , M\}$$的資訊含量或熵。我們可以看到，如果$$q>p$$或（$$M<N$$），則$$\Delta H>0$$。在這種情況下，由於可能的結果或結果不確定性的增加，熵增加或資訊丟失。另一方面，如果$$q<p$$或($$M>N$$)，則$$\Delta H<0$$。這種情況下，由於可能結果的數量減少或不確定性的增加，對應於資訊的獲得。

對應於$$\mathrm{H}_{\max}$$，資訊的度量可建構為如下：

$$\displaystyle \begin{aligned} I & = H_{\max} - H \\ & = \log n + \sum_{i=1}^n p_i \log p_i \\ & = \sum_{i=1}^n p_i \log(\frac{p_i}{1/n}) \\ & = \sum_{i=1}^n p_i \log (\frac{p_i}{q_i}) \end{aligned}$$--(1.15)

其中$$q_i = \frac{1}{n}$$。在(1.15)中，$$\{q_i\}$$可視為先驗分佈，而$$\{p_i\}$$可視為後驗分佈。以$$H_{\max}$$正規化後得相對冗餘度$$0 \leq R \leq 1$$：

$$R = \frac{I}{H_{\max}} = 1 - \frac{H}{H_{\max}}$$--(1.16)

### 資訊增益函數(information gain function)

從Shannon熵的討論中，可得到從一個事件中獲得的資訊與它發生的機率成反比。定義增益函數$$G(p)$$如下：

$$\displaystyle G(p) = \Delta I =\log big(\frac{1}{p_i}) = - \log(p_i) \text{-- (1.18)}$$

換句話說，事件$$i$$發生的資訊或其傳遞的資訊所消除的不確定性是由公式（1.18）來衡量的。 如果一個事件發生的機率非常小，比如$$p_i=0.01$$，那麼這個事件傳遞的部分資訊就非常大。

因為獨立事件的機率組合是一種乘法關係。因此，對數允許把它們的熵的組合表達為一個簡單的加法關係。 例如，如果$$\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B)$$，那麼$$\mathrm{H}(AB) =-\log(\mathrm{P}(A))-\log (\mathrm{P}(B))=\mathrm{H}(A)+ \mathrm{H}(B)$$。

若有$$N$$個事件，可計算總資訊增益為 $$\displaystyle I = \sum_{i=1}^N \Delta I_i = - \sum_{i=1}^N \log(p_i)$$。

事件$$i$$的熵或總資訊量為加權值：$$\mathrm{H}(p_i) = -p_i \log (p_i) \text{--(1.20)}$$。

因此，資訊的平均或預期收益可以通過對單個資訊收益的加權平均來獲得：$$\displaystyle H = \mathrm{E}(\Delta I) = - \sum_{i=1}^N p_i (\Delta I_i) = - \sum_{i=1}^N p_i \log(p_i) \text{--(1.21)}$$。

這裡值得注意的是，人們可以通過簡單地定義增益函數或不確定性來定義不同類型的熵。本章中還定義了另外三種類型的熵。

方程（1.21）可以用另一種方式來看待。實驗結果的機率對應於結果之間的空間劃分。因為結果的交集是空的，所以實驗的全域性熵是$$N$$個結果的基本熵之和：

$$
\begin{aligned} H & = H_1 + H_2 + \dots + H_N = \sum_{i=1}^N H_i \\ &= p_1 \log p_1 - p_2 \log p_2 - \dots - p_N \log p_N = -\sum_{i=1}^N p_i \log(p_i) \text{--(1.22)} \end{aligned}
$$

上式可看出$$H$$最大值發生在所有事件發生機率均相等時，即$$p_i = \frac{1}{N}, ~i=1,2,\dots, N$$。

## 參考資料

* Vijay P. Singh, "_Entropy theory and its application in environmental and water engineering," ch1,_ John Wiley & Sons, 2013.
