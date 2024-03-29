# 統計力學熵(

## 簡介

統計力學處理的是系統在原子尺度上的行為，因此<mark style="color:red;">關注的是系統的微觀狀態</mark>。由於系統中的粒子數量非常龐大，處理每個粒子的微觀狀態是不切實際的，因此要借助於統計方法；換句話說，<mark style="color:red;">更重要的是描述微觀狀態的分佈函數</mark>。在原子尺度上可能有許多微觀狀態，而這些微觀狀態在熱力學狀態層面上可能是無法區分的。換句話說，可以有許多實現熱力學狀態的可能性。

假設微觀狀態的數量為$$N$$，則<mark style="color:red;">統計熵(Boltzmann熵)</mark>定義為：$$S=k \ln N$$--(1.2)，且假設所有的微觀狀態有相同的發生機率。

* 其中$$k$$為Boltzmann常數(($$1.3806 \times 10^{−16} erg/K$$ 或 $$1.3806 \times 10^{−23} J/K (kg-m^2 /s^2 -K$$)
* 即每個分子的氣體常數$$k=\frac{R}{N_0}$$，其中$$R$$為每莫耳的氣體常數(1.9872 cal/K)，而$$N_0$$為Avogadro數(每莫耳$$6.0221 \times 10^{23}$$)。

換句話說，<mark style="color:red;">在統計力學中Boltzmann熵是正則系綜(canonical ensemble)的熵</mark>。

由(1.2)可知當微觀數量$$N$$增加時，熵$$S$$也增加；而$$S$$的最大值表示最有可能發生的狀態。因此，這可以被認為是熱力學狀態機率的直接度量。式(1.2)定義的熵體現了式(1.1)定義的熱力學熵的所有性質。

方程（1.2）可以通過考慮一個系統的集合來概括。這些系統將處於不同的微觀狀態。

若在第$$i$$個微狀態的系統數量為$$n_i$$，則第$$i$$個微狀態對應的統計熵為$$S_i=k \log n_i$$。對於總體熵可表示為加權和：$$\displaystyle S=k \sum_{i=1}^N n_i \log n_i$$--(1.4a)，其中$$N$$為所有微狀態的數量。

令$$p_i=n_i/N$$，最後可將統計熵記為$$\displaystyle S=-k \sum_{i=1}^N p_i \log n_i$$ --(1.4b)，其中$$k$$為Boltzmann常數。

令所有的微狀態發生機率相等，即$$p_i=\frac{1}{N}$$，則(1.2)可由(1.4b)得到: $$\displaystyle S=-k N \frac{1}{N} \ln \frac{1}{N} = k \ln N$$。

系統的熵是一個廣泛的熱力學性質，如質量、能量、體積、動量、電荷或化學物質的原子數，但與這些量不同的是，<mark style="color:red;">熵不服從守恆定律</mark>。廣泛的熱力學量是指當包含這些量的平衡系統被分成兩個相等的部分時，這些量減半，但密集量保持不變。廣泛變數的例子包括體積、質量、分子數和熵;密集變數的例子包括溫度和壓力。

<mark style="color:red;">一個系統的總熵等於各個部分的熵之和</mark>。<mark style="color:red;">系統中最可能的能量分佈是對應於系統最大熵的能量分佈。這發生在動態平衡的條件下</mark>。在向靜止狀態的演化過程中，單位質量的熵產生率應該最小，與外部約束相容。在熱力學中，熵被用來衡量系統狀態的無序程度。

<mark style="color:red;">一個封閉和孤立的系統的熵總是趨向於增加到最大值</mark>。在一個液壓系統中，如果沒有能量損失，該系統將是有序的和有組織的。<mark style="color:red;">正是能量損失及其原因使系統變得無序和混亂。因此，熵可以被解釋為衡量一個系統內的混亂或無序程度。</mark>在液壓學中，一部分流能（或機械能）被液壓系統消耗以克服摩擦，然後消散到外部環境中。這樣轉換的能量經常被稱為能量損失。這種轉換只有一個方向，即從可用能量到不可用能量或能量損失。

<mark style="color:red;">衡量不可恢復的流動能量數量的標準是熵，它不守恆，而且總是增加，也就是說，熵的變化是不可逆的</mark>。熵的增加意味著無序的增加。因此，水力學中表達能量（或水頭）損失的過程方程可以說是起源於熵的概念。

## 參考資料

* Vijay P. Singh,  "_Entropy theory and its application in environmental and water engineering," ch1,_ John Wiley & Sons, 2013.
