# 正交對角化 (orthogonally diagonalizable)

## 么正(正交)相似

> 矩陣$$A,B \in \mathbb{C}^{N \times N}$$，若存在一個么正矩陣$$P \in \mathbb{C}^{N \times N}$$（$$P^{\mathrm{H}}P=PP^{\mathrm{H}}=I_N$$）$$\ni P^{\mathrm{H}} AP=B$$，則稱$$A$$與$$B$$么正相似(unitarily similar)，或稱$$A$$與$$B$$么正等價(unitarily equivalent)。
>
> 矩陣$$A,B \in \mathbb{R}^{N \times N}$$，若存在一個正交矩陣$$P \in \mathbb{R}^{N\times N}$$（$$P^\top P=PP^\top=I_N$$）$$\ni P^\top AP=B$$，則稱$$A$$與$$B$$正交相似(orthogonally similar)，或稱$$A$$與$$B$$正交等價(orthogonally equivalent)。

### &#x20;么正(正交)相似為相似

> * 矩陣$$A$$與$$B$$么正相似，$$B=P^{\mathrm{H}} AP=P^{−1} AP$$，所以$$A$$與$$B$$相似。
> * 矩陣$$A$$與$$B$$正交相似，$$B=P^\top AP=P^{−1} AP$$，所以$$A$$與$$B$$相似。>

## 么正(正交)對角化

> * 矩陣$$A \in \mathbb{C}^{N \times N}$$，若$$A$$與某個對角矩陣么正相似($$PP^\mathrm{H}=I_N, P^\mathrm{H} AP=D$$)，則稱$$A$$可么正對角化(unitarily diagonalizable)。
> * 矩陣$$A \in \mathbb{R}^{ N \times N}$$，若$$A$$與某個對角矩陣正交相似($$PP^\top=I_N, P^T AP=D$$)，則稱$$A$$可正交對角化(orthogonally diagonalizable)。
> * 線性轉換$$T \in L(V,V)$$，若存在$$V$$的一組單範正交基底$$B$$使得$$[T]_B$$ 為一對角矩陣，則稱$$T$$可么正對角化。
>
> ### 么正(正交)對角化為對角化
>
> * 矩陣$$A \in \mathbb{C}^{N\times N}$$ 可么正對角化，則$$A$$可對角化。
> * 矩陣$$A \in \mathbb{R}^{N \times N}$$ 可正交對角化，則$$A$$可對角化。
> * 線性轉換$$T \in L(V,V)$$可么正對角化，則$$T$$可對角化。

Proof:

因為$$A=P^\mathrm{H} DP=P^{−1} DP,~ PP^\mathrm{H}=I_N$$，則$$P$$的行向量為$$A$$的特徵向量，且行向量形成單範正交集。(QED)

### &#x20;么正相似的性質

> 矩陣$$A,B \in \mathbb{C}^{N \times N}$$ 且$$A$$與$$B$$么正相似($$P^\mathrm{H} AP=B, ~PP^\mathrm{H}=P^\mathrm{H} P=I_N$$)，則：
>
> 1. $$A$$為正規矩陣($$A^\mathrm{H} A=AA^\mathrm{H}$$)$$\Leftrightarrow B$$為正規矩陣。
> 2. $$A$$為Hermitian matrix ($$A^\mathrm{H}=A$$)$$\Leftrightarrow B$$為Hermitian matrix。
> 3. $$A$$為skew Hermitian matrix ($$A^\mathrm{H}=−A$$)$$\Leftrightarrow B$$為skew Hermitian matrix。
> 4. $$A$$為正定矩陣($$\forall 0 \neq x \in \mathbb{C}^{N \times 1},~ x^\mathrm{H} Ax>0$$) $$\Leftrightarrow B$$為正定矩陣。
> 5. $$A$$為正半定矩陣($$\forall 0\neq x \in \mathbb{C}^{N \times 1}, ~x^\mathrm{H} Ax\geq 0$$)$$\Leftrightarrow B$$為正半定矩陣。
> 6. $$A$$為么正矩陣($$A^\mathrm{H} A=AA^\mathrm{H}=I_N$$)$$\Leftrightarrow B$$為么正矩陣。>

由於<=的證明只要把=>的證明中的$$P$$改成$$P^\mathrm{H}$$,$$P^\mathrm{H}$$ 改成$$P$$，因此只證明⇒

Proof (1) =>

* $$A^\mathrm{H} A=AA^\mathrm{H}   B^\mathrm{H} B=(P^\mathrm{H} AP)^\mathrm{H} (P^\mathrm{H} AP)=P^\mathrm{H} A^\mathrm{H} PP^\mathrm{H} AP=P^\mathrm{H} A^\mathrm{H} AP=P^\mathrm{H}AA^\mathrm{H} P=P^\mathrm{H} APP^\mathrm{H}A^\mathrm{H} P=BB^\mathrm{H}$$(QED)

Proof (2):

* $$A^\mathrm{H}=A$$
* $$B^\mathrm{H}=(P^\mathrm{H} AP)^\mathrm{H}=P^\mathrm{H} A^\mathrm{H} P=P^\mathrm{H} AP=B$$ (QED)

Proof (3):

* $$A^\mathrm{H}=−A$$
* $$B^\mathrm{H}=(P^\mathrm{H} AP)^\mathrm{H}=P^\mathrm{H} A^\mathrm{H} P=−P^\mathrm{H}AP=−B$$ (QED)

Proof (4):

* $$\forall x \neq 0,~ x^\mathrm{H} Bx=x^\mathrm{H} P^\mathrm{H} APx=(Px)^\mathrm{H} A(Px)$$
* 因為$$P$$為可逆矩陣，所以$$Px \neq 0$$, 且$$A$$為正定矩陣
* 因此 $$x^\mathrm{H} Bx=(Px)^\mathrm{H} A(Px)>0$$ (QED)

Proof (5):

* $$\forall x\neq 0, x^\mathrm{H} Bx=x^\mathrm{H} P^\mathrm{H} APx=(Px)^\mathrm{H} A(Px)$$
* 因為$$A$$為正半定矩陣
* 所以 $$x^\mathrm{H} Bx=(Px)^\mathrm{H} A(Px) \geq 0$$ (QED)

Proof (6):

* $$A^\mathrm{H} A=I_N$$
* $$B^\mathrm{H} B=(P^\mathrm{H} AP)^\mathrm{H} (P^\mathrm{H} AP)=P^\mathrm{H} A^\mathrm{H} PP^\mathrm{H} AP=P^\mathrm{H} A^\mathrm{H} AP=P^\mathrm{H} IP=P^\mathrm{H} P=I_N$$ (QED)

### &#x20;正交相似的必要條件

> 矩陣$$A,B \in \mathbb{R}^{N \times N}$$， 且$$A$$與$$B$$正交相似($$P^\top AP=B$$， $$PP^\top=P^\top P=I_N$$) ，則：
>
> 1. $$A$$為symmetric matrix ($$A^\top=A$$) $$\Leftrightarrow B$$為symmetric matrix。
> 2. $$A$$為skew symmetric matrix ($$A^\top=−A$$) $$\Leftrightarrow B$$為skew symmetric matrix。
> 3. $$A$$為正交矩陣($$A^\top A=AA^\top=I_N$$)$$\Leftrightarrow B$$為正交矩陣。

由於<=的證明只要把=>的證明中的$$P$$改成$$P^\mathrm{H}$$，$$P^\mathrm{H}$$ 改成$$P$$，因此只證明⇒。

Proof (1):

* $$A^\top＝A$$
* $$B^\top=(P^\top AP)^\top=P^\top A^\top P=P^\top AP=B$$ (QED)

Proof (2):

* $$A^\top=−A$$
* $$B^\top=(P^\top AP)^\top=P^\top A^\top P=−P^\top AP=−B$$(QED)

Proof (3):

* $$A^\top A=I_N$$
* $$B^\top B=(P^\top AP)^\top (P^\top AP)=P^\top A^\top PP^\top AP=P^\top A^\top AP=P^\top P=I_N$$ (QED)

## Schur's theorem: 存在單範正交基底使得線性轉換為上三角矩陣

> 線性轉換$$T \in L(V,V)$$若$$char_T (x)$$在$$F$$中可分解，則存在$$V$$的一組單範正交基底$$B$$使得$$[T]_B$$ 為上三角矩陣。

Proof:

* 對$$\dim(V)$$作數學歸納法  ，$$\dim⁡(V)=1$$時成立  。
* 假設$$\dim⁡(V)=N−1$$時命題成立  ，考慮$$\dim⁡(V)=N$$
* 因為$$char_T (x)$$在F中可分解，所以$$T$$必有特徵根，可得$$T^∗$$ 必有特徵根  。
* 令$$\lambda$$為$$T^∗$$的一個特徵根  ，所以$$\exists z \neq 0 \ni T^∗ (z)=\lambda z$$, 不失一般性令$$\|z\|=1$$。
* 令$$W=span\{z\}$$
* 首先證明$$W^\bot$$ 為$$T$$不變子空間(即$$\forall y \in W^\bot, T(y) \in W^\bot$$)
* $$\forall y \in W^\bot, x \in W \Rightarrow x=cz, ~c \in F$$
* 所以$$\langle T(y),x \rangle= \langle y,T^∗ (x) \rangle= \langle y,T^∗ (cz) \rangle=\langle y, cT^∗ (z) \rangle=\langle y,c \lambda z \rangle=(c\overline{\lambda}) \langle y,z \rangle=0 \Rightarrow T(y) \in W^\bot$$
* 所以$$W^\bot$$ 為$$T$$不變子空間
* 因此$$char_{T_{W^\bot}} (x)|char_T (x) \Rightarrow char_{T_{W^\bot}} (x)$$在$$F$$中可分解
* 因為$$\dim⁡(W^\bot )=N−1$$
* 由數學歸納法假設知存在$$W^\bot$$ 的一組單範正交基底$$R\ni [W^\bot ]_R=U$$為上三角矩陣
* 因為$$V=W \oplus W^\bot$$
* 令 $$B=R \cup \{z\}$$
* 則$$B$$為$$V$$的一組單範正交基底且$$[T]_B=\begin{bmatrix} R & 0 \\ 0 & \lambda \end{bmatrix}$$為上三角矩陣 (QED)

## Schur's theorem: 存在單範正交基底使得正規算子可么正對角化

> 線性轉換$$T \in L(V,V)$$為正規算子($$T^∗ T=TT^∗$$)。
>
> 若存在$$V$$的一組單範正交基底$$b$$使得$$[T]_B$$ 為對角矩陣，則> $$T$$可么正對角化($$∃PP^\mathrm{H}=I \ni P^\mathrm{H} [T]_B P=D$$)。

Proof:

* 根據前述定理，可知存在$$V$$的一組單範正交基底$$B=\{b_1,\dots,b_N \}\ni[T]_B=U$$為上三角矩陣  。
* 欲證$$_1,v_2,\dots,b_N$$ 均為$$T$$的特徵向量，可對$$N$$做數學歸納法  。
* $$N=1$$時，因為$$U$$為上三角矩陣， $$T(b_1 )=[U]_{11} b_1$$，因此$$b_1$$ 為$$T$$的特徵向量。
* 假設$$N=k−1$$時, $$b_1,\dots,b_{k−1}$$ 均為$$T$$的特徵向量成立  。
* 考慮$$N=K$$
* 令$$U=\begin{bmatrix} X & Y \\ 0 & Z\end{bmatrix}$$, $$X \in F^{K−1 \times K−1}$$ 對角矩陣  。
* 則$$U^\mathrm{H}=\begin{bmatrix} X^\mathrm{H} & 0 \\Y^\mathrm{H} & Z^\mathrm{H} \end{bmatrix}$$
* 因為$$U$$為上三角矩陣，所以$$[U]_{jk}=0, ~\forall j>k$$
* 由於$$[T^∗ ]_B=[T]_{B^\mathrm{H}}=U^\mathrm{H}$$ \[因為伴隨算子的矩陣表示法為Hermetian matrix]
* &#x20;且因為$$b_1,\dots,b_{K−1}$$ 為$$T$$的特徵向量，且$$T$$為正規算子，所以$$T^∗$$ 與$$T$$有相同的特徵向量  。
* 即$$b_1,\dots,b_{K−1}$$ 為$$T^∗$$ 的特徵向量  。
* 所以得$$Y^\mathrm{H}=0 \Rightarrow [U^\mathrm{H}]_{kj}=0, \forall j<k \Rightarrow [U]_{jk}=0, \forall j<k$$
* 因此$$b_K$$ 為$$T$$的特徵向量
* 所以$$T$$可么正對角化 (QED)

## Schur's theorem: 存在么正矩陣可將矩陣轉換為上三角矩陣

> 1. 矩陣$$A \in \mathbb{C}^{N \times N}$$, 則存在一么正矩陣$$P \in \mathbb{C}^{N \times N}, P^\mathrm{H} P=I_N \ni P^\mathrm{H} AP$$為上三角矩陣。
> 2. 矩陣$$A \in \mathbb{R}^{N \times N}$$ 且$$char_A (x)$$在$$\mathbb{R}$$中可分解，則存在一個正交矩陣$$P \in \mathbb{R}^{N\times N}, ~P^\top P=I_N \ni P^\top AP$$為上三角矩陣。

Proof:數學歸納法

* $$N=1$$時顯然成立  ，假設$$N=K$$時命題成立  。
* 考慮$$N=K+1$$
* 因為$$A \in \mathbb{C}^{N \times N}$$, 所以$$A$$具有$$N$$個特徵根
* 令$$\lambda_1$$ 為$$A$$的一個特徵根且$$w_1$$ 為$$A$$相對於$$\lambda_1$$ 的一個單位特徵向量  。
* 因此存在$$v_2,\dots,v_{K+1} \in \mathbb{C}^{K+1}\ni \{w_1,v_2,\dots,v_{K+1} \}$$為$$\mathbb{C}^{K+1}$$ 的一組基底  。
* 利用Gram-Schmidt正交化過程對$$w_1,v_2,\dots,v_{K+1}$$ 正交化得$$\{w_1,w_2,\dots,w_{K+1} \}$$為$$\mathbb{C}^{K+1}$$ 的單範正交基底  。
* 令$$W=\begin{bmatrix} w_1 & w_2 & \dots & w_{K+1} \end{bmatrix}$$，因此$$W$$為么正矩陣
* 因為$$W^\mathrm{H} AW$$的第一行為$$W^\mathrm{H} AWe_1=W^\mathrm{H} Aw_1=W^\mathrm{H} \lambda_1 w_1=\lambda_1 W^H w_1=\lambda_1 e_1$$
* 整理後可得$$W^\mathrm{H} AW=\begin{bmatrix} \lambda_1 & \dots \\ 0 & M \end{bmatrix} \in \mathbb{C}^{K \times K}$$
* 由數學歸納假設知存在一個么正矩陣$$V_1 \in \mathbb{C}^{N \times N} \ni V_1^\mathrm{H} AV_1=R_1$$為上三角矩陣，令$$V=\begin{bmatrix} 1 & 0 \\ 0 & V_1\end{bmatrix}$$,　則$$V$$為么正矩陣且  &#x20;$$V^\mathrm{H} W^\mathrm{H} AWV=R$$為上三角矩陣
* 取$$P=WV$$，則$$P^\mathrm{H} P=(WV)^\mathrm{H} WV=V^\mathrm{H} W^\mathrm{H} WV=I_N$$且$$PP^\mathrm{H}=I_N$$  所以$$N=K+1$$時成立　(QED)

Proof　(2):

因為$$char_A (x)$$在$$\mathbb{R}$$中可分解，所以$$A$$在$$\mathbb{R}$$有$$N$$個特徵根，剩餘證明同上(QED)。

#### 範例

* $$A=\begin{bmatrix} 0.8 & 0.2 & 0.1 \\ 0.1 & 0.7 & 0.3 \\0.1 & 0.1 & 0.6 \end{bmatrix}$$，$$char_A(x)=-(x-0.6)(x-1)(x-0.5)$$
* $$\lambda_1=0.6$$
* $$V(0.6)=ker(A-0.6I)=span\left\{ \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}\right\}$$
  * 令$$w_1=\begin{bmatrix}\frac{1}{\sqrt{2}} \\  -\frac{1}{\sqrt{2}} \\ 0\end{bmatrix}$$，由$$\mathbb{R}^3$$的標準基底經Gram-Schmidt正交化得$$w_2 = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{bmatrix}$$，$$w_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$為$$\mathbb{R}^3$$的單範正交基底。
  * 矩陣$$W=\begin{bmatrix} w_1 & w_2  & w_3\end{bmatrix}$$，可得
  * $$W^\top A W=\begin{bmatrix} 0.6 & 1& -0.1 \sqrt{2} \\ 0 & 0.9 & 0.2 \sqrt{2} \\0 & 0.1 \sqrt{2} & 0.6 \end{bmatrix}$$
  * 取$$M = \begin{bmatrix} 0.9 & 0.2 \sqrt{2} \\ 0.1 \sqrt{2} & 0.6  \end{bmatrix}$$
* $$\lambda_2 = 1$$
* $$ker(M-I)=span\left\{ \begin{bmatrix} 2 \sqrt{2} \\ 1\end{bmatrix} \right\}$$
  * $$W^{'} = \begin{bmatrix} \frac{2 \sqrt{2}}{3} & \frac{1}{3} \\ \frac{1}{3} & -\frac{2 \sqrt{2}}{3}    \end{bmatrix}$$
* $$P = W \begin{bmatrix} 1 & 0 & \dots & 0 \\  0 & & W^{'} \\ 0\end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{2}{3} & \frac{\sqrt{2}}{6} \\ -\frac{1}{\sqrt{2}} & \frac{2}{3} & \frac{\sqrt{2}}{6} \\0 & \frac{1}{3} & -\frac{2 \sqrt{2}}{3}\end{bmatrix}$$
* 所以$$P^\top A P = \begin{bmatrix}   0.6 & \frac{\sqrt{2}}{30} & \frac{1}{6} \\ 0 & 1 & \frac{\sqrt{2}}{10} \\ 0 & 0 & 0.2  \end{bmatrix}$$

## 正規矩陣且為上三角矩陣若且唯若為對角矩陣

> * $$A \in \mathbb{C}^{N \times N}$$，則$$A$$為正規矩陣($$A^\mathrm{H} A=AA^\mathrm{H}$$ )且為上三角矩陣$$\Leftrightarrow A$$為對角矩陣。
> * $$A \in \mathbb{R}^{N \times N}$$，則$$A$$為對稱矩陣($$A^\top=A$$)且為上三角矩陣$$\Leftrightarrow A$$為對角矩陣。>

Proof　(1)\=>

* 因為$$A$$為上三角矩陣，所以$$[A]_{pq}=0, ~\forall p>q$$。
* 因為$$A^\mathrm{H} A=AA^\mathrm{H}$$，所以$$\forall i=1,2,\dots,N$$&#x20;
* $$(A^\mathrm{H} A)_{ii}=(AA^\mathrm{H} )_{ii}$$
* 得$$\sum_{k=1}^N(A^\mathrm{H})_{ik} A_{ki} = \sum_{k=1}^N(A)_{ik} (A^\mathrm{H})_{ki}$$
* 因為是上三角矩陣，所以$$\sum_{k=1}^i(A^\mathrm{H})_{ik} A_{ki} = \sum_{k=i}^N(A)_{ik} (A^\mathrm{H})_{ki}$$
* 整理得$$\sum_{k=1}^i \overline{(A)_{ki}} A_{ki} = \sum_{k=i}^N(A)_{ik} \overline{(A)_{ik}}$$
* 所以$$\sum_{k=1}^i | A_{ki}|^2 = \sum_{k=i}^N |(A)_{ik} |^2$$
*   所以

    * $$|(A)_{11} |^2=|(A)_{11} |^2+|(A)_{12} |^2+\dots+|(A)_{1N} |^2$$
    * $$\vdots$$
    * $$|(A)_{1N} |^2+|(A)_{2N} |^2+\dots+|(A)_{NN} |^2=|(A)_{NN} |^2$$
    * 即$$|(A)_{pq} |^2=0, \forall p<q$$，且$$|(A)_{pq} |=0, ~p<q$$
    * 所以$$A$$為對角矩陣 (QED)

    proof <=
* $$A$$為上三角矩陣顯然成立
* 令$$A=diag(a_{11},a_{22},\dots,a_{NN} )$$
* 所以$$A^\mathrm{H} A=diag(|a_{11} |^2,|a_{22} |^2,\dots,|a_{NN} |^2 )=AA^\mathrm{H}$$，所以$$A$$為正規矩陣 (QED)

Proof (2)

* 若$$A$$為上三角矩陣且$$A^\top=A$$
* 因為$$A^\top$$ 為下三角矩陣，所以$$A$$為對角矩陣
* 反之若$$A$$為對角矩陣，則顯然$$A$$為上三角矩陣且$$A^\top=A$$(QED)

## 可么正對角化矩陣為正規矩陣

> * $$A \in \mathbb{C}^{N \times N}$$，則$$A$$為可么正對角化($$\exists P^\mathrm{H} P=I_N \ni P^\mathrm{H} AP=D$$)$$\Leftrightarrow A$$為正規矩陣($$A^\mathrm{H} A=AA^\mathrm{H}$$)。
> * $$A \in \mathbb{R}^{N \times N}$$，則$$A$$為可正交對角化($$\exists P^\top P=I_N \ni P^\top AP=D$$)$$\Leftrightarrow A$$為對稱矩陣($$A^\top=A$$)。

Proof (1)\=>

* 因為$$A$$可么正對角化，所以$$A$$與某個對角矩陣$$D$$么正相似
* 因為$$D$$為對角矩陣，所以$$D$$為正規矩陣，所以$$A$$為正規矩陣(么正對角化的特性)

<=

* 根據Schur's定理，$$A$$與某個上三角矩陣$$U$$么正相似
* 因為$$A$$為正規矩陣，因此$$U$$為正規矩陣(么正相似特性)，所以$$U$$為對角矩陣  。
* 因此$$A$$與對角矩陣$$U$$么正相似，即$$A$$可么正對角化。 (QED)

Proof (2)&#x20;\=>

* 因為$$A$$可正交對角化，所以$$A$$與某個對角矩陣$$D$$正交相似  。
* 所以$$D$$為對稱矩陣，可得$$A$$為對稱矩陣。

<=

* 因為$$A \in \mathbb{R}^{N \times N}$$ 為對稱矩陣  ，且$$A$$的特徵多項式在$$\mathbb{R}$$中可分解  。
* 根據Schur's定理，$$A$$個某個上三角矩陣$$U$$正交相似  。
* 因為$$A$$為對稱矩陣，所以$$U$$為對稱矩陣，所以$$U$$為對角矩陣
* 因此$$A$$與對角矩陣$$U$$正交相似，即$$A$$可正交對角化　(QED)
