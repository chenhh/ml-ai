# 相似矩陣(similar matrix)

## 相似矩陣(similar matrix)

> 矩陣$$A,B \in F^{N \times N}$$> ，若存在可逆矩陣$$P \in F^{N \times N} \ni P^{−1} AP=B$$ 或$$AP=PB$$，> 則稱$$A$$與$$B$$相似($$A$$ and $$B$$ are similar)，記作$$A \sim B$$。>

> 相似矩陣即$$A$$經過（可逆的）線性轉換至〕$$B$$，再經線性轉換為$$A$$。

### 相似矩陣為等價關係(滿足反身性、對稱性、遞移性)

> 矩陣$$A,B,C \in F^{N \times N}$$> ，則：
>
> * $$A \sim A$$($$\because AI_N = I_NB$$)
> * $$A \sim B \Leftrightarrow B \sim A$$（$$AP=PB  \Rightarrow  P^{-1}AP=B\Rightarrow A=(P^{-1})^{-1}B(P^{-1})$$）
> * $$A \sim B, ~ B \sim C \Rightarrow A \sim C$$

### 同一向量空間基底相似

> 線性轉換$$T \in L(V,W)$$，且$$B,R$$為向量空間$$V$$的兩組基底，則$$[T]_B \sim [T]_R$$。

Proof:

* 因為$$[I_V ]_B^R [T]_B [I_V ]_R^B=[T]_R \Rightarrow ([I_V ]_R^B )^{−1} [T]_B [I_V ]_R^B=[T]_R$$ (QED)

### 相似矩陣的必要條件

> 矩陣$$A,B \in F^{N \times N}$$> ，且$$A$$與$$B$$相似，則：
>
> * $$tr(A)=tr(B)$$
> * $$\det⁡(A)=\det⁡(B)$$
> * $$rank(A)=rank(B)$$
> * $$nullity(A)=nullity(B)$$
> * $$A^\top \sim B^\top$$
> * $$A^k \sim B^k,\ \forall k \in \mathbb{N}$$
> * $$cA \sim cB,\ \forall c \in F$$
> * $$A+cI \sim B+cI$$
> * $$f(A) \sim f(B),\  \forall f(x)\in F[x]$$ (多項式)>

> Note: 相似矩陣的唯一充要條件是兩個矩陣的Jordan form相等。

Proof:

* 令$$B=P^{−1} AP$$
* $$tr(B)=tr(P^{−1} AP)=tr(P^{−1} (AP))=tr((AP) P^{−1} )=tr(A)$$
* $$\det⁡(B)=\det⁡(P^{−1} AP)=\det⁡(P^{−1} (AP))=\det(P^{−1}  \det⁡(A)\det⁡(P)=\det⁡(A)$$
* $$rank(B)=rank(P^{−1} AP)=rank(AP)=rank(A)$$
* $$nullity(B)=N−rank(B)=N−rank(A)=nullity(A)$$
