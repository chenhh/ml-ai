# 機率的解釋

## 古典機率

令Ω為所有可能結果的集合，稱為**樣本空間\(sample space\)**，樣本空間中每一個元素ω稱為**出象\(outcome\)**。 Ω的任一子集\(subset\)稱為**事件\(event\)**，記為$$A \subseteq \Omega$$，可得$$\omega \in A \subseteq \Omega$$ 。

一事件$$A \subseteq \Omega$$ 發生若且唯若隨機變數的結果為$$A$$中的一元素。

* e.g. 丟骰子 $$\Omega={1,2,3,4,5,6}$$, 出現奇數的事件$$A={1,3,5}$$。
* 對一樣本空間$$\Omega$$與一事件 $$A \subseteq \Omega$$，定義$$A$$的機率為$$P(A)=\frac{|A|}{|Ω|}$$。

  **在古典的模式中，一事件的機率為此事件中的元素個數除以可能的結果之個數**。

定義機率時是以樣本空間$$\Omega$$的所有子集合為定義域的函數。 因此對於$$\Omega$$的子集合而非$$\Omega$$中的元素才能定義機率。

* $$\forall \omega \in \Omega$$, $${ \omega } $$ 為只包含一個元素的集合，$$ P({\omega})=\frac{1}{|\Omega|} $$，而 $$P(\omega)$$無定義。
* 機率測度P必須滿足以下三個條件： $$\forall A, B \subseteq \Omega$$ \($$A, B$$為事件集合\)
  * \[機率的上下界$$0 \leq P(A) \leq P(\Omega) = 1$$ 
  * $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$ 
  * $$P(A^C) = 1 - P(A)$$

計算古典機率，只需分別算出$$A$$與$$\Omega$$中的元素個數即可求出機率；但有時元素個數過多，必須使用排列組合方式才可求出個數。

