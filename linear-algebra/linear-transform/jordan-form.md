# Jordan form

## 簡介

* Jordan form是判斷矩陣$$A$$與$$B$$是否相似\($$A \sim B \equiv \exists P \text{ invertiable } \ni AP=PB$$\)的唯一充要條件。
* 所有方陣都唯一存在Jordan form（依定義可能為上移或下移矩陣），比可對角化矩陣性質適用範圍更大。
* Jordan form矩陣$$J$$的形狀與原始矩陣$$A$$的大小相同。
* 如果線性轉換$$T$$的所有特徵根的代數重數（特徵向量的重根數）均為1\($$m(\lambda_i )=1, \forall i$$\)，即此線性轉換可對角化，則此線性轉換的Jordan form為特徵根形成的對角矩陣$$D$$。因此可對角化矩陣為Jordan form的特例。

### 0特徵根與核空間的關係

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N<\infty$$。
>
> 若$$\dim⁡(\bigcup_{i=1}^\infty  ker⁡(T^i ) )=M$$，則：
>
> 1. 若$$M=0$$，則0不為$$char_T (x)$$的根\(因為$$ker⁡(T^i )=\{0\}, \forall i$$，因此$$T$$可逆，所以$$T$$的所有特徵根均不為0\)   。
> 2. 若$$M \geq 1$$，則0為$$char_T (x)$$的$$M$$重根。

Proof \(1\):

* 令$$W_1=\bigcup_{i=1}^\infty  ker⁡(T^i )  $$
* 根據kernel chain theorem，存在最小正整數$$k$$使得$$W_1=ker⁡(T^k )$$
* 令$$W_2=R(T^k)$$，則根據fitting引理得$$V=ker⁡(T^k ) \oplus R(T^k )=W_1 \oplus W_2$$
* 因為$$m=0$$，得$$\dim⁡(ker⁡(T^k ) )=0$$，因此$$ker⁡(T^k )=\{0\}$$。
* 因為$$\{0\} \subseteq ker⁡(T) \subseteq ker⁡(T^k )=\{0\}$$
* 所以$$k=1$$，得$$ker⁡(T)=\{0\}$$
* 因此$$T$$為可逆函數，即$$\det⁡(T) \neq 0$$，得$$char_T (0)=\det⁡(T−0I) \neq 0$$
* 所以0不為$$T$$的特徵根 \(QED\)



