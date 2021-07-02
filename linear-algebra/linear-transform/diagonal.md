# 對角化 \(diagonal\)

## 可對角化 \(diagonalizable\)

> 線性轉換$$T \in L(V,V)$$。
>
> * 若存在$$V$$的一組基底$$B$$使得$$[T]_B=D$$為對角矩陣，則稱$$T$$可對角化。
> * $$A\in F^{ N \times N}$$，若存在可逆矩陣$$P \in F^{N\ \times N}$$ 使得$$P^{−1} AP=D$$為對角矩陣，則稱$$A$$可對角化，且$$A$$與$$D$$相似。
> *  因此若$$A$$為可對角化矩陣，則$$A$$與對角矩陣$$D$$相似。

### 可對角化方陣必可分解為特徵向量矩陣與特徵根形成的對角矩陣

> 線性轉換$$T \in L(V,V),~\dim⁡(V)=N$$且$$B$$為$$V$$的基底，則：
>
> * $$[T]_B$$ 為對角矩陣若且唯若基底$$B$$中的元素均為$$T$$的特徵向量  。（特徵向量可做為基底）
> * $$A \in F^{N \times N}$$且$$P \in F^{N \times N}$$ 為可逆矩陣則  $$ P^{−1} AP=D$$為對角矩陣若且唯若$$P$$的行向量均為$$A$$的特徵向量  。
> * 因要求$$P$$可逆，因此所有特徵向量必須線性獨立。
> * 若$$A$$的特徵向量並非全部線性獨立時，則$$A$$不可對角化。

Proof:

* 令$$B=\{b_1,b_2,\dots,b_N \}$$為$$V$$的基底，所以$$b_i \neq 0, \forall i$$。
* 若$$[T]_B=D=diag\{\lambda_1, \lambda_2, \dots, \lambda_N\}$$，則$$T(b_1)=\lambda_1 b_1, \dots, T(b_N) = \lambda_N b_N$$，因此$$b_i$$為$$T$$相對於$$\lambda_i$$的特徵向量，反之也可得到相同結論\(QED\)。
* 令$$P=\begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix} \in F^{N \times N}$$
*  因為$$P$$為可逆矩陣，所以$$0 \neq v_i \in F^{N \times 1}, i=1,2,\dots ,N  $$。
* $$P^{−1} AP=D=diag\{\lambda_1, \lambda_2, \dots, \lambda_N\} \Leftrightarrow AP=PD $$
* 得$$A\begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix}= \begin{bmatrix}v_1 & v_2 &  \dots,v_N \end{bmatrix}diag\{\lambda_1, \lambda_2, \dots, \lambda_N\} $$
* 因此$$\begin{bmatrix}Av_1 &A v_2 &  \dots Av_N \end{bmatrix} = \begin{bmatrix} \lambda_1 v_1 & \lambda_2 v_2 &  \dots \lambda_N v_N \end{bmatrix}$$  \(QED\).





