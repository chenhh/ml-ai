# 基底與維度\(basis and dimension\)

## 基底與維度

> $$(V, +, \cdot)$$為定義在體$$F$$的向量空間，令集合$$B \subseteq V$$滿足：
>
> * $$span(B) = V$$（向量空間$$V$$的所有元素均可用$$B$$內的元素線性組合而成）
> * $$B$$為線性獨立集合。
>
> 則稱$$B$$為$$V$$為一組基底，且集合$$B$$內的元素個數為$$V$$的（整數）維度。

* 基底集合不唯一，但是向量空間的維度唯一（即基底集合雖然不相同，但元素個數相同）。
* $$\dim⁡(V)<\infty$$時，稱為有限維度向量空間（finite-dimensional vector space），否則為無限維度向量空間（infinite-dimensional vector space）  ，線性代數中只討論有限維度向量空間，泛函分析才會討論無限維向量空間。

## 標準基底

* $$N$$維歐式空間，$$V=F^N, B=\{e_1,e_2,\dots,e_N \}, e_1=(1,0,0,\dots), e_2=(0,1,0,\dots),e_N=(0,0,⋯,0,1), \dim⁡(F^N )=N$$
* $$N$$階多項式函數空間，$$V=F_N [x] ，B=\{1,x,x^2,\dots,x^N \}, \dim⁡(F_N [x])=N+1$$
* 多項式函數空間，$$V=F[x], B=\{1,x,x^2,x^3,\dots\},\dim⁡(F(x))=\infty$$
* 矩陣空間，$$V=F^{M\times N}, B=\{E_{ij}, 1\leq i \leq M, 1\leq j \leq N\},\dim⁡(F^{M \times N} )=MN$$
* 實數\(複數\)空間，$$V=F, b=\{1\},\dim⁡(F)=1$$
* 色彩空間中, $$V=\text{RGB-color}, \dim⁡(V)=3$$
* 零空間，$$V=\{0\}，B=\{\emptyset\}，\dim⁡(\{0\})=0$$，這是唯一一個維度為0的空間。



