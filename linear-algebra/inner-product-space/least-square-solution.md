# 最小平方解\(least square solution\)

## 簡介

* 矩陣$$A \in F^{M \times N} , A=\begin{bmatrix} A_{:1} & \dots & A_{:N}\end{bmatrix},~ A^{\mathrm{H}}=  \begin{bmatrix} \overline{A_{:1}^\top} \\ \vdots \\ \overline{A_{:N}^\top}\end{bmatrix} = \begin{bmatrix} A_{:1}^{\mathrm{H}} \\ \vdots \\ A_{:N}^{\mathrm{H}}\end{bmatrix}$$
* $$A^{\mathrm{H}}A =  \begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} &  \dots &A_{:1}^{\mathrm{H}}A_{:N} \\  \vdots & \ddots & v\dots \\ A_{:N}^{\mathrm{H}}A_{:1} & \dots & A_{:N}^{\mathrm{H}}A_{:N}  \end{bmatrix} \in F^{N \times N}$$
* 例如：$$A=\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{bmatrix}$$，$$A^{\mathrm{H}}=\begin{bmatrix} \overline{a_{11}} & \overline{a_{21}} & \overline{a_{31}} \\ \overline{a_{12}} & \overline{a_{22}} & \overline{a_{32}} \end{bmatrix}$$，$$A^{\mathrm{H}}A=\begin{bmatrix}  A_{:1}^{\mathrm{H}}A_{:1} & A_{:1}^{\mathrm{H}}A_{:2} \\ A_{:2}^{\mathrm{H}}A_{:1} & A_{:2}^{\mathrm{H}}A_{:2}  \end{bmatrix}$$

