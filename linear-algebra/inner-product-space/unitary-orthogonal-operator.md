# 么正\(正交\)算子\(unitary \(orthogonal\) operator\)

##  么子算子、正交算子

> 線性轉換$$T \in L(V,V)$$，$$T^{*}$$為伴隨算子，若$$T^∗ T=I$$，則：
>
> * 當體$$F$$為複數$$\mathbb{C}$$時稱么正算子\(unitary operator\)。
> * 當體$$F$$為實數$$\mathbb{R}$$時稱正交算子\(orthogonal operator\)。
>
> 矩陣$$A \in F^{N \times N}$$
>
> * 當$$A^\mathrm{H} A=I_N$$時，稱$$A$$為么正矩陣\(unitary matrix\)。
> * $$A^\top A=I_N$$時，稱$$A$$為正交矩陣\(orthogonal matrix\)。

* $$A$$為么正矩陣$$\Leftrightarrow A^{−1}=A^\mathrm{H}$$。
* $$A$$為正交矩陣$$\Leftrightarrow A^{−1}=A^\top$$。

### 正交矩陣的性質

> 矩陣$$A \in \mathbb{C}^{N \times N}$$ \(或$$A \in \mathbb{R}^{N \times N}$$\)為么正矩陣（正交矩陣），則：
>
> 1. $$A$$為正規矩陣\($$A^\mathrm{H} A=I_N=AA^\mathrm{H}$$，$$A^\top A=I_N=AA^\top$$ \)。
> 2. $$A$$的相異特徵根對應的特徵向量必正交 （因為么正\(正交\)矩陣為正規矩陣）。
> 3. $$A$$的特徵根$$\lambda$$滿足$$|\lambda|=1$$。
> 4. $$|\det⁡(A)|=1$$ \($$\det⁡(AA^\mathrm{H} )=\det(A) \overline{\det(A)}=det⁡(I_N)=1$$\)

Proof \(3\):

* $$\exists x \neq 0 \ni Ax=\lambda x$$
* 得$$x^\mathrm{H} A^\mathrm{H} Ax=x^\mathrm{H} I_N x=x^\mathrm{H} x=\|x\|^2$$。
* 且$$x^\mathrm{H} A^\mathrm{H} Ax=(Ax)^\mathrm{H} (Ax)=\|Ax\|^2=\| \lambda x\|^2=|\lambda |^2 \|x\|^2$$
* 所以$$\|x\|^2=|\lambda|^2 \|x\|^2$$且$$\|x\|^2\geq 0$$，得$$|\lambda|^2=1$$，所以$$|\lambda|=1$$ \(QED\)

