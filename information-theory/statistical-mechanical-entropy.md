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

## 參考資料

* Vijay P. Singh,  "_Entropy theory and its application in environmental and water engineering," ch1,_ John Wiley & Sons, 2013.
