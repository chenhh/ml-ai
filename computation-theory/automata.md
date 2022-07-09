# 自動機(automata)

## 簡介

現實的計算機相當複雜，難以定義為簡單的數學模型。因此採用稱為「計算模型」的理想計算機，此模型精確的描繪了幾種情怳，對於不同的特性，使用不同的計算模型。

## 有限自動機、有限狀態機(finite automata, finite state machine)

有限自動機是關於儲存量有限(狀態有限)的計算模型，也稱有限狀態機(finite state machine)。

這台機器的運作過程會有許多狀態，也就是許多步驟、流程。**如果這台機器的步驟及接受的字元種類是有限的，也就是數量是可數的，並面對所有字元都能對應一種狀態，而且具有起始及結束的狀態，那麼我們稱這台機器叫「有限自動機」(Finite Automaton)**。能夠被有限狀態機認識的語言，我們稱這語言叫**正規語言 (Regular Language)**。

> definition: deterministic finite automata (DFA) or finite state machine(FSM)
>
> 有限自動機是5元組 $$(Q, \Sigma, \delta, q_0, F)$$ ，
>
> * $$Q$$為有限集合，稱為狀態集(states )。
> * $$\Sigma$$為有限集合，稱為字母集(alphabets)。
> * $$\delta: Q \times \Sigma \rightarrow Q$$為轉移函數(transition function)。
> * $$q_0 \in Q$$為起始狀態 (start state)。
> * $$F \subseteq Q$$為接受狀態集(set of accept states)。

* 接受狀態集$$F$$可以為空集合，此時自動機沒有接受狀態。
* 轉移函數$$\delta$$在輸入一個字母時，會轉移到下一個狀態，此狀態依函數的定義唯一。轉移函數經常使用列表的方式表示。

DFA M1如下：

* $$Q=\{q_1, q_2, q_3 \}$$
* $$\Sigma=\{0,1\}$$
* $$\delta$$為下表
* $$q_1$$為起始狀態
* $$F=\{q_2\}$$
* $$A = \{ \omega \vert \omega \text{ 至少含有一個1，並在最後一個1後有偶數個0}\}$$

| state\input | 0       | 1       |
| ----------- | ------- | ------- |
| $$q_1$$     | $$q_1$$ | $$q_2$$ |
| $$q_2$$     | $$q_3$$ | $$q_2$$ |
| $$q_3$$     | $$q_2$$ | $$q_2$$ |

![有限自動機M1](../.gitbook/assets/finite\_automata\_m1-min.png)

* 因此有限自動機$$M$$，在給定特定的字串(strings)時，最後會進入的接受狀態。而這些可被機器接受字串的集合$$A$$，稱為**機器**$$M$$**的語言(language)，記為**$$L(M)=A$$。也稱為**機器**$$M$$**識別**$$A$$**( M recognizes A)或機器**$$M$$**接受**$$A$$ **(M accepts A)**。
* 一台機器可接受多個字串，但只能識別一種語言(即可接受的字串形成的集合唯一)。
* 如果機器不接受任何字串，則此機器只識別一種語言，即空語言$$\emptyset$$。
* 如果機器能接受亦能拒絕任一輸入字串，我們稱這機器可決定(decide)一語言，此語言可被機器決定(decidable)。

## 正規語言(regular language)

> definition: FSM accepts a string
>
> 令$$M=(Q, \Sigma, \delta, q_0, F)$$為FSM，$$\omega = \omega_1 \omega_2 \ldots \omega_n, \omega_i \in \Sigma$$為一字串。
>
> 若狀態序列 $$r_0, r_1, \ldots, r_n, \text{ in } Q$$ 滿足以下三個條件時，則$$M$$識別(接受)字串$$\omega$$。
>
> 1. \[機器從初始狀態開始]$$r_0 = q_0$$
> 2. \[狀態轉移符合轉移函數]$$\delta(r_i, w_{i+1}) =r_{i+1}, \ \forall i = 0,1,\ldots, n-1$$
> 3. \[機器結束於接受狀態]$$r_n \in F$$
>
> 如果$$A= \{ \omega \vert \ M \text{ accepts } \omega\}$$，則稱$$M$$識別(接受)語言$$A$$。



> definition: regular language
>
> 給定語言$$A$$，如果存在有限自動機$$M$$可識別$$A$$時，則$$A$$稱為正規語言(regular language)。

建構識別$$A$$的有限自動機時，要把自已當成機器，使用可利用的所有資料來建構滿足條件的機器。

## 正規運算(regular operation)

> definition: regular operation
>
> $$A,B$$為兩種語言，定義
>
> * 聯集 (union) $$A\cup B = \{ x \vert x \in A \lor x \in B \}$$
> * 連接(concatenation) $$A \circ B = \{ xy \vert x \in A \land y \in B\}$$
> * 星號(star) $$A^{*} = \{ x_1 x_2 \ldots x_k \vert k \geq 0, \ x_i \in A\}$$

* 聯集將$$A,B$$中的所有字串放在同一語言中。
* 連接是以所有可能的方式，將$$A$$中的任一字串接在$$B$$中所有字串的前面。
* 星號是將$$A$$中任一個字串，任意數量個串接得到新的語言。因為是任意個字串的串接，所以包含空字串$$\epsilon$$，即$$\epsilon$$必為$$A^{*}$$的元素。

例：$$\Sigma = \{a,b,c,\ldots,z\}$$, $$A=\{good, bad\}$$, $$B=\{boy, girl\}$$

* $$A\cup B = \{good, bad, boy, girl \}$$
* $$A \circ B =\{ goodboy, goodgirl, badboy, badgirl\}$$
* $$A^{*}= \{ \epsilon, good, bad, goodgood, goodbad, badgood, badbad, \\goodgoodgood, goodgoodbad, goodbadgood, goodbadbad, \ldots\}$$

### 正規運算的封閉性

> 如果$$A_1, A_2$$是正規語言(即兩個語言分別有FSM $$M_1, M_2$$可識別之)，則
>
> * $$A_1 \cup A_2$$是正規語言(存在FSM $$M$$可識別之)
> * $$A_1 \circ A_2$$是正規語言
> * $$A_1^{*}$$是正規語言。
>
> 使用非確定型有限自動機(non-deterministic finite automata, NFA)證明會比直接建構DFA簡單。



## 非確定型有限自動機(non-deterministic finite automata, NFA)

非確定性在FA中，指的是在任何一個狀態時，對於相同的輸入，下一個狀態可能存在多個選擇，而不是唯一確定。因此DFA為NFA的特例。

DFA與NFA主要是在轉移函數$$\delta$$不同。

* 在DFA中，$$\delta: Q\ \times \Sigma \rightarrow Q$$產生的是下一個確定的狀態；
* 在NFA中，$$\delta: Q\times \Sigma_{\epsilon} \rightarrow P(Q)$$產生的是下一個狀態的集合，其中$$\Sigma_{\epsilon} = \Sigma \cup {\epsilon}$$為含有空字元的字母集合，而$$P(Q)$$為$$Q$$的冪集(power set)。

> definition: non-deterministic finite automata (NFA)&#x20;
>
> NFA是5元組 $$(Q, \Sigma, \delta, q_0, F)$$ ，
>
> * $$Q$$為有限集合，稱為狀態集(states )。
> * $$\Sigma$$為有限集合，稱為字母集(alphabets)。
> * $$\delta: Q \times \Sigma_{\epsilon} \rightarrow P(Q)$$為轉移函數(transition function)。
> * $$q_0 \in Q$$為起始狀態 (start state)。
> * $$F \subseteq Q$$為接受狀態集(set of accept states)。

NFA N1的轉移函數如下表，其中輸入$$\epsilon$$(空字串)表示不必有輸入值，就會自動轉移對應的狀態集合。

|         | 0             | 1                | $$\epsilon$$  |
| ------- | ------------- | ---------------- | ------------- |
| $$q_1$$ | $$\{q_1\}$$   | $$\{q_1, q_2\}$$ | $$\emptyset$$ |
| $$q_2$$ | $$\{q_3\}$$   | $$\emptyset$$    | $$\{q_3\}$$   |
| $$q_3$$ | $$\emptyset$$ | $$\{q_4\}$$      | $$\emptyset$$ |
| $$q_4$$ | $$\{q_4\}$$   | $$\{q_4\}$$      | $$\emptyset$$ |



![NFA N1](../.gitbook/assets/nfa\_n1.png)

![NFA在讀取字元後，會分支成多個機器(類似行程的fork)，平行執行所有狀態](../.gitbook/assets/dfa\_nfa-min.png)

NFA N1對於輸入010110的計算，由狀態$$q_1$$開始，

* 因為對於輸入0只能到達$$q_1$$，所以下一個狀態為$$q_1$$
* 在$$q_1$$時對於輸入1，可到達$$q_1$$或$$q_2$$，而$$q_2$$對於空字串$$\epsilon$$會到$$q_3$$，所以有三種轉移狀態。
* 對於之後的輸入，以相同的方式遞迴分支下去。

分析後可發現N1接受含有101或11做為子字串的所有字串。

![NFA N1對於輸入010110的計算](../.gitbook/assets/nfa\_example-min.png)
