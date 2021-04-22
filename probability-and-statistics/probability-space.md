# 機率空間

給定一非空的集合$$\Omega$$稱為樣本空間\(sample space\)，$$\Omega$$的一些子集合所形成的集合$$\mathcal{F}$$\(collection of sets\)，$$\mathcal{F}$$中的元素稱為事件\(event\)，注意事件為集合。

對每一個事件$$A \in \mathcal{F}$$，以函數$$P$$得到一實數 $$P(A) \in \mathbb{R}$$，稱為事件$$A$$的機率。

一般使用上述方式描述機率時，多將$$\mathcal{F}$$取包含$$\Omega$$所有子集的集合，即$$\mathcal{F}$$為$$\Omega$$的冪集合\(power set\)，此時$$\Omega$$的任一子集合均為事件。但若$$\mathcal{F}$$只有$$\Omega$$所有子集之真子集\(proper subset\)時，則F必須為sigma-field \(sigma-algebra\)才滿足可測\(measurable\)的條件，條件如下：

考慮事件 $$A, B \in \mathcal{F}$$，則$$A,B$$可形成的新集合為$$A \cup B$$, $$A \cap B$$, $$A^c$$, $$B^c$$

* 因此若$$A \in \mathcal{F}$$，則 $$A^c\in \mathcal{F}$$
* 若$$A,B \in \mathcal{F}$$, 則 $$A \cup B,\ A\cap B \in \mathcal{F}$$

## definition: sigma-field \(sigma-algebra\)

令 $$\Omega$$為樣本空間，當集合 $$\mathcal{F}$$滿足

> 令 $$\Omega$$為樣本空間，當集合 $$\mathcal{F}$$滿足

* $$\forall A \in \mathcal{F} \Rightarrow A^c \in \mathcal{F}$$
* $$\forall n \in \mathbb{N}, \ A_n \in \mathcal{F} \Rightarrow  \cup_{n=1}^{\infty} A_n \in \mathcal{F}\  \text{and}\ \cap_{n=1}^{\infty}A_n \in \mathcal{F}$$

滿足以上兩條件的集合$$\mathcal{F}$$稱為sigma-field。



* 由以上定義可知空集合和宇集合都是sigma-field的元素，即 $$\phi,\ \Omega \in \mathcal{F}$$。
* 一個非空集合$$\Omega$$的冪集合必為sigma-field。
* 例 $$\Omega={1,2,3,4,5,6}$$， 則$$\mathcal{F}_1=\{\phi,\Omega, \{1\}, \{2,3,4,5,6\}\}$$, $$\mathcal{F}_2=\{\phi, \Omega, \{1,3,5\}, \{2,4,6\}\}$$均為sigma-field.

### Borel集合

$$\Omega=\mathbb{R}=(−\infty,\infty)$$，則存在一包含所有開區間$$(a,b) -\infty < a < b < \infty$$的sigma-field，記為$$\mathcal{B}$$，而任一集合$$A \in \mathcal{B}$$稱為Borel集合。

