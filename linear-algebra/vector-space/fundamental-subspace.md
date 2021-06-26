# 基本子空間\(fundamental subspace\)

## 列、行、核、左核空間

> 給定矩陣$$A \in F^{M \times N}$$，定義以下四個子空間：
>
> * \[列空間\(row space\)\]：$$RS(A)=\{xA| x \in F^{1\times M}\}=\begin{bmatrix} x_1 & \dots & x_M\end{bmatrix} \begin{bmatrix}A_{1:} \\ \vdots \\ A_{M:} \end{bmatrix} = x_1A_{1:} +\cdots +x_M A_{M:} \subseteq F^{1 \times N} $$為由矩陣$$A$$的列\(row\)生成的子空間。
> * \[行空間\(column space\)\]：$$CS(A)=\{Ax| x \in F^{1\times N}\}=\begin{bmatrix}A_{: 1} & \dots & A_{:M} \end{bmatrix} \begin{bmatrix} x_1 \\ \vdots \\ x_M\end{bmatrix} = x_1A_{:1} +\cdots +x_M A_{:M} \subseteq F^{M \times 1} $$為由矩陣$$A$$的行\(column\)生成的子空間。

