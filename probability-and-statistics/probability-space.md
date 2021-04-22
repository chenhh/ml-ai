# 機率空間

給定一非空的集合$$\Omega$$稱為樣本空間\(sample space\)，$$\Omega$$的一些子集合所形成的集合$$\mathcal{F}$$\(collection of sets\)，$$\mathcal{F}$$中的元素稱為事件\(event\)，注意事件為集合。

對每一個事件$$A \in \mathcal{F}$$，以函數$$P$$得到一實數 $$P\(A\) \in mathbb{R}$$，稱為事件$$A$的機率。
	

一般使用上述方式描述機率時，多將$$\mathcal{F}$$取包含$$\Omega$$所有子集的集合，即$$\mathcal{F}$$為$$\Omega$$的冪集合\(power set\)，此時$$\Omega$$的任一子集合均為事件。但若$$\mathcal{F}$$只有$$\Omega$$所有子集之真子集\(proper subset\)時，則F必須為sigma-field (sigma-algebra)才滿足可測(measurable)的條件，條件如下：
* 考慮$$ A, B \in \mathcal{F} $$，則$$A,B$$可形成的新集合為$$A \cup B$$, $$A \cap B$$, $$A^c$$, $$B^c$$
* 因此若$$A \in \mathcal{F}$$，則 $$A^c\in \mathcal{F}$$
* 若$ A,B \in \mathcal{F}$$, 則 $$A \cup B,\ A\cap B \in \mathcal{F}$$


