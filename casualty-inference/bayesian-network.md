# 貝氏網路

## 簡介

貝氏網路（Bayesian network），又稱信念網路（belief network）或是有向無環圖模型（directed acyclic graphical model），是一種機率圖型模型，藉由有向無環圖（directed acyclic graphs, or DAGs）中得知一組隨機變數$$X_{1},X_{2},\dots,X_{n}$$及其n組條件機率分佈的性質。

機率圖模型是用圖來表示變數機率依賴關係的理論，由圖靈獎得主Judea Pearl開發出來。。對於一個實際問題，我們希望能夠挖掘隱含在資料中的知識。機率圖模型建構了這樣一幅圖，用觀測結點表示觀測到的資料，用隱含節點表示潛在的知識，用邊來描述知識與資料的相互關係，最後基於這樣的關係圖獲得一個機率分佈，非常“優雅”地解決了問題。

機率圖中的節點分為隱含節點和觀測節點，邊分為有向邊和無向邊。從機率論的角度，<mark style="color:red;">節點對應於隨機變數，邊對應於隨機變數的依賴或相關關係，其中有向邊表示單向的依賴(或因果關係)，無向邊表示相互依賴關係</mark>。<mark style="color:red;">而兩個節點間若沒有箭頭相互連接一起的情況就稱其隨機變數彼此間為條件獨立</mark>。兩節點若有邊相連，就會產生一個條件機率值。

機率圖模型分為**貝氏網路（Bayesian Network）**和**馬可夫網路（Markov Network）**兩大類。貝氏網路可以用一個有向圖結構表示，馬可夫網路可以表 示成一個無向圖的網路結構。

大部分的情況下，貝氏網路適用在節點的性質是屬於離散型的情況下，且依照$${\displaystyle P(X_{i}|P_{i}})$$此條件機率寫出條件機率表，此條件機率表的每一列（row）列出所有可能發生的$${\displaystyle P_{i}}$$，每一行（column）列出所有可能發生的$${\displaystyle X_{i}}$$，且任一列的機率總和必為1。

## 頻率派與貝氏派的思考方式

頻率派把需要推斷的引數$$\theta$$看做是固定的未知常數，即機率雖然是未知的，但最起碼是確定的一個值，同時，樣本$$X$$是隨機的，所以頻率派重點研究樣本空間，大部分的機率計算都是針對樣本$$X$$的分佈；&#x20;

而貝式派的觀點則截然相反，他們認為引數$$\theta$$是隨機變數，而樣本$$X$$是固定的，由於樣本是固定的，所以他們重點研究的是引數的分佈。

## 貝氏網路的三種結構形式

### head-to-head

a->c且 b->c的結構。

可得$$\mathrm{P}(a,b,c)=\mathrm{P}(a)\mathrm{P}(b)\mathrm{P}(c|a,b)$$。即在$$c$$未知的條件下，$$a,b$$被阻斷(blocked)為條件獨立。

由$$\displaystyle \sum_{c} \mathrm{P}(a,b,c)  = \sum_{c}\mathrm{P}(a)\mathrm{P}(b)\mathrm{P}(c|a,b)$$可得$$\displaystyle \mathrm{P}(a,b)  = \mathrm{P}(a) \mathrm{P}(b)$$。

### tail-to-tail

c->a且c->b的結構。

考慮$$c$$未知與$$c$$已知的兩種情形：

* $$c$$未知時，有$$\mathrm{P}(a,b,c)=\mathrm{P}(c)\mathrm{P}(a|c)\mathrm{P}(b|c)$$，此時無法得出$$\mathrm{P}(a,b)=\mathrm{P}(a)\mathrm{P}(b)$$，即$$c$$未知時，$$a,b$$不獨立。
* 在$$c$$已知時，可得$$\mathrm(P)(a,b|c)=\frac{\mathrm{P}(a,b,c)}{\mathrm{P}(c)}$$，再將$$\mathrm{P}(a,b,c)=\mathrm{P}(c)\mathrm{P}(a|c)\mathrm{P}(b|c)$$帶入式子得$$\mathrm{P}(a,b|c)=\mathrm{P}(c)\mathrm{P}(a|c)\mathrm{P}(b|c)/\mathrm{P}(c)=\mathrm{P}(a|c) \mathrm{P}(b|c)$$，即$$c$$已知時，$$a,b$$獨立。

### head-to-tail

a->c且c->b的結構。

考慮$$c$$未知與$$c$$已經的兩種情形：

* $$c$$未知時，有$$\mathrm{P}(a,b,c)=\mathrm{P}(a)\mathrm{P}(c|a)\mathrm{P}(b|c)$$，但無法得到$$\mathrm{P}(a,b)=\mathrm{P}(a)\mathrm{P}(b)$$。即$$c$$未知時，$$a,b$$ 不獨立。
* $$c$$ 已知時，有$$\mathrm{P}(a,b|c)=\frac{\mathrm{P}(a,b,c)}{\mathrm{P}(c)}$$，但根據$$\mathrm{P}(a,c)=\mathrm{P}(a)\mathrm{P}(c|a)=\mathrm{P}(c)\mathrm{P}(a|c)$$，可化簡得：$$\begin{aligned} \mathrm{P}(a,b|c) &= \frac{\mathrm{P}(a,b,c)}{\mathrm{P}(c)} \\ & = \mathrm{P}(a) \times \mathrm{P}(c|a) \times \frac{\mathrm{P}(b|c)}{\mathrm{P}(c)} \\ & = \mathrm{P}(a,c) \times \frac{\mathrm{P}(b|c)}{\mathrm{P}(c)} \\ & = \mathrm{P}(a|c) \times \mathrm{P}(b|c) \end{aligned}$$

所以在給定$$c$$的條件下，$$a,b$$被阻斷(blocked)是獨立的。

如果是$$x_1 \rightarrow x_2 \rightarrow \dots \rightarrow x_M$$這種head-to-tail結構，在給定$$x_i$$的條件下，$$x_{i+1}$$的分佈和$$x_1, x_2, \dots, x_{i-1}$$條件獨立，稱之為馬可夫鏈(Markov chain)。

### D-separation

將上述三類節點推廣到節點集，則是：對於任意的節點集$$A,B,C$$，考察所有通過$$A$$中任意節點到$$B$$中任意節點的路徑，若要求$$A,B$$條件獨立，則需要所有的路徑都被阻斷(blocked)，即滿足下列兩個前提之一：

1. $$A$$和$$B$$的head-to-tail和tail-to-tail路徑均通過$$C$$。
2. $$A$$和$$B$$的head-to-head型路徑不通過$$C$$與$$C$$的子孫。

