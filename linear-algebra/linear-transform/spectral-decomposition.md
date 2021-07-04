# 光譜分解\(spectral decomposition\)

## 完全投影集\(complete set of projection\)

> * 線性轉換$$T_1,T_2,\cdots,T_K\in L(V,V)$$滿足：
>   * $$T_i^2=T_i, ~i=1,2,\dots,K$$（所有線性轉換均為投影算子）
>   * $$T_i T_j=0, ~ \forall i\neq j$$ \(投影算子間互不影響\)
>   * $$(T_1+T_2+\dots+T_K)(v)=I(v)$$ \(所有投影算子的和空間等於單位空間\)
>   * 則稱$$\{T_1,T_2,\dots,T_K \}$$為$$V$$的一組完全投影集    合。

> * 矩陣$$A_1,A_2,\dots,A_K \in F^{N\times N}$$ 滿足  ：
>   * $$A_i^2=A_i, ~ i=1,2,\dots,K$$
>   * $$A_i A_j=0, ~\forall i \neq j$$
>   * $$A_1+A_2+\dots+A_K=I    $$
>   * 則稱$$\{A_1,A_2,\dots,A_K \}$$為$$V$$的一組完全投影集    合。

### 常見投影算子與完全投影集

> 線性轉換$$T \in L(V,V)$$為投影算子\($$T^2=T$$\)，則：
>
> * $$I−T$$為投影算子
>   * $$ker⁡(I−T)=R(T)    $$
>   * $$R(I−T)=ker⁡(T)$$
> * $$ \{T, I−T\}$$為完全投影集  。
>
> 註：$$\forall v \in V, ~ I(v)=v$$

Proof :

* $$(I−T)^2=(I−T)(I−T)=I−T−T+T^2=I−T−T+T=I−T$$ 
* 所以$$I-T$$為投影算子\(QED\)
* $$ker⁡(I−T)=\{v\in V|(I−T)(v)=0\}=\{v \in V|v−T(v)=0\}=\{v \in V|T(v)=v\}=R(T)$$ \(QED\)
* $$T^2=T$$且$$(I−T)^2=I−T  $$
* $$T(I−T)=T−T^2=T−T=O  $$
* $$T+(I−T)=I  $$
* 所以$$\{T, I−T\}$$為完全投影集。   \(QED\)

### 完全投影集存在性

> 向量空間$$V$$為獨立子空間的直和，則存在完全投影集將$$V$$中的任意元素投影至每一個獨立子空間中。
>
> 向量空間$$V$$定義在體$$F$$，且$$W_1, W_2,\dots, W_K$$為$$V$$的子空間，則：
>
> $$V=W_1 \oplus W_2 \oplus \dots \oplus W_K$$若且唯若存在完全投影集$$\{T_1,T_2, \dots, T_K\}$$滿足$$R(T_i)=W_i, ~=i=1,2,\dots,K$$

Proof: =&gt;

* 因為$$V=W_1 \oplus W_2 \oplus \dots \oplus W_K$$
* 所以$$\forall v∈V, \exists w_i \in W_i \ni v=w_1+\dots+w_k$$ 且表示法唯一
* 定義$$T_i:V→V$$為$$T_i (v)=w_i, ~ i=1,2,\dots,K$$
* 要證明$$\{T_1,\dots,T_k\}$$為完全投影集。
* $$T_i (v)=w_i \Rightarrow T_i^2 (v)=T_i (T_i (v))=T_i (w_i )=w_i=T_i (v)$$，所以為投影算子。
* $$T_i T_j (v)=T_i (T_j (v))=T_i (w_j )=0, \forall i \neq j$$，所以投影算子間互不影響。
* $$(T_1+ \dots +T_k )(v)=T_1 (v)+\dots+T_k (v)=w_1+\dots+w_k=v=I(v) $$
* 所以$$\{T_1,\dots,T_k\}$$為完全投影集
* 要證明$$W_i=R(T_i )$$
* $$\forall w_i \in W_i, w_i=T_i (w_i ) \in R(T_i )\Rightarrow W_i \subseteq R(T_i )$$
* $$\forall T_i (v) \in R(T_i ) \Rightarrow T_i (v)=w_i \in W_i\Rightarrow R(T_i ) \subseteq W_i$$
* 所以$$W_i=R(T_i )$$\(QED\)

Proof &lt;=:

* $$W_i$$ 為$$V$$的子空間，所以$$W_1+\dots+W_k$$ 為$$V$$的子空間，因此$$W_1+\dots+W_k \subseteq V$$。
* $$\forall v \in V, ~v=I(v)=(T_1+\dots+T_k )(v)=T_1 (v)+\dots+T_k (v) \in W_1+\dots+W_k$$
* 所以$$V \subseteq W_1+\dots+W_k$$
* 可得$$V=W_1+\dots+W_k$$
* $$\forall w_i \in W_i$$ ，證明$$w_i$$只能由$$T_i $$生成
* 若$$w_1+\dots+w_k=0$$
* 得$$0=T_i (0)=T_i (w_1+\dots+w_k )=\sum_{j=1}^k T_i (w_j ) $$
* 因為$$w_j \in W_j=R(T_j ) \Rightarrow \exists u_j \in V \ni w_j=T_j (u_j )$$
* 所以$$0=\sum_{j=1}^kT_i (w_j)=\sum_{j=1}^k T_i (T_j (u_j ))=\sum_{j=1}^k \delta_{ij} T_i (u_j )=T_i (u_i )=w_i$$
* 因此$$W_1,\dots,W_k$$ 為獨立子空間。
* 所以$$V=W_1 \oplus W_2 \oplus \dots  \oplus W_k $$ \(QED\)

##  光譜分解定理\(Spectral decomposition theorem\)

> 線性轉換$$T \in L(V,V)$$，且$$\lambda_1,\lambda_2,\dots,\lambda_K$$ 為$$T$$的相異特徵根（可能重根）。
>
> 若$$T$$可對角化\($$P^{−1} [T]_B P=D$$\)，則存在一組完全投影集$$\{T_1,T_2, \dots,T_K \}$$使得$$T=\lambda_1 T_1+\lambda_2 T_2+\dots+\lambda_K T_K$$。
>
> 矩陣$$A \in F^{N \times N}$$，若$$A$$可對角化，且, $$\lambda_1,\lambda_2,\dots,\lambda_K$$ 為$$A$$的相異特徵根，則存在一完全投影集$$\{A_1,A_2,\dots,A_K \}$$使得$$A=\lambda_1 A_1+\lambda_2 A_2+\dots+\lambda_K A_K$$。

Proof:

* 因為$$T$$可對角化，根據可對角化的充要條件，所以$$V=V(\lambda_1 )\oplus V(\lambda_2 )\oplus \dots  \oplus V(\lambda_k )$$
* 因此存在一組完全投影集$$\{T_1,\dots,T_k \} \ni R(T_i )=V(\lambda_i )$$。
* 且若$$v=v_1+\dots+v_k, v_i \in V(\lambda_i )$$，則$$T_i (v)=v_i, ~\forall i$$
* 要證明$$T=\lambda_1 T_1+ \dots +\lambda_k T_k$$
* $$\forall v \in V, ~v=v_1+ \dots +v_k, ~  v_i \in V(\lambda_i )$$
* $$T(v)=T(v_1+\dots +v_k )=T(v_1 )+\dots+T(v_k )=\lambda_1 v_1+ \dots +\lambda_k v_k=\lambda_1 T_1 (v)+\dots + \lambda_k T_k (v)=(\lambda_1 T_1+\dots+\lambda_k T_k )(v)$$
* 所以$$T=\lambda_1 T_1+\dots+\lambda_k T_k$$  \(QED\)

### 範例1

* 矩陣$$A$$可對角化，且$$\lambda_1, \dots \lambda_K$$為$$A$$的相異特徵根，則存在可逆矩陣$$P \ni P^{-1}AP=D = diag\{\lambda_1 I_{m_1}, \dots, \lambda I_{m_K}\}$$
* 所以$$\begin{align} A & =PDP^{-1}\\ & = P\left\{  \lambda_1 \begin{bmatrix}  I_{m_1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 0 \end{bmatrix} + \dots + \lambda_K \begin{bmatrix}  0 & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & I_{m_K} \end{bmatrix} \right\} P^{-1} \\ &= \lambda_1 P\begin{bmatrix}  I_{m_1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & 0 \end{bmatrix} P^{-1}+ \dots +  \lambda_K P\begin{bmatrix}  0 & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & I_{m_K} \end{bmatrix} P^{-1} \\&= \lambda_1 A_1 + \dots + \lambda_K A_K \end{align}$$

### 範例2

* $$A=\begin{bmatrix} 2 & 2 & 1 \\ 1 &3 & 1\\ 1 & 2 &2 \end{bmatrix}$$
* $$char_A(x)=\det(A-xI)=-(x-1)^2(x-5)$$
* $$V(1)=ker(A-I) = span\left\{ \begin{bmatrix} 2 \\ -1 \\ 0\end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}  \right\}$$
* $$V(5)=ker(A-5I) = span\left\{ \begin{bmatrix} 1 \\ 1 \\ 1\end{bmatrix}  \right\}$$
* $$P=\begin{bmatrix} 2 & 1 & 1 \\ -1 & 0 & 1\\ 0 & -1 & 1 \end{bmatrix}$$，$$P^{-1}AP=D=\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0\\ 0 & 0 & 5 \end{bmatrix}$$
* $$A=PDP^{-1} = P\left\{  1\cdot\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0\\ 0 & 0 & 0 \end{bmatrix} +  5 \cdot  \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0\\ 0 & 0 & 1\end{bmatrix} \right\} P^{-1} = 1\left\{  P \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0\\ 0 & 0 & 0 \end{bmatrix} P^{-1} \right\} + 5 \cdot \left\{  P  \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0\\ 0 & 0 & 1\end{bmatrix} P^{-1} \right\} =  1 \begin{bmatrix} \frac{3}{4} & -\frac{1}{2} & -\frac{1}{4} \\ -\frac{1}{4} & \frac{1}{2} & -\frac{1}{4}\\ -\frac{1}{4} & -\frac{1}{2} & \frac{3}{4}\end{bmatrix} + 5 \begin{bmatrix} \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{2} & \frac{1}{4}\end{bmatrix}$$

