# 奇異值分解\(SVD, singular value decomposition\)

## 奇異值分解

> * 矩陣$$A \in \mathbb{F}^{M \times N}$$，$$s=\min\{m, n\}$$
> * 若存在$$U \in \mathbb{C}^{M \times M}, V \in \mathbb{C}^{N \times N}, \Sigma\in \mathbb{C}^{M \times N} \ni A=U \Sigma V^\mathrm{H}$$
> * 且$$U^\mathrm{H}U=I_M$$，$$V^\mathrm{H}V=I_N$$均為么正矩陣，
> * $$\Sigma$$為除了對角線元素外均為0的矩陣，且對角線元素由大至小排列。即$$[\Sigma]_{ij}=0, ~\forall i \neq j$$，$$[\Sigma]_{ii}=\sigma_i, i=1,2,\dots, s$$，且$$\sigma_1 \geq \sigma_2 \geq \dots \sigma_s$$。
> * 則稱$$A=U \Sigma V^\mathrm{H}$$為$$A$$的奇異值分解，$$\sigma_i$$為矩陣$$A$$的奇異值。
>
> 註：任何矩陣都可以做奇異值分解。

