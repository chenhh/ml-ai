# 基本子空間\(fundamental subspace\)

## 基本子空間

給定矩陣$$A \in F^{M \times N}$$，定義以下四個子空間：

### 列空間\(row space\)

$$RS(A)=\{xA| x \in F^{1\times M}\}=\begin{bmatrix} x_1 & \dots & x_M\end{bmatrix} \begin{bmatrix}A_{1:} \\ \vdots \\ A_{M:} \end{bmatrix} = x_1A_{1:} +\cdots +x_M A_{M:} \subseteq F^{1 \times N} $$為由矩陣$$A$$的列\(row\)生成的子空間。

![&#x77E9;&#x9663;&#x7684;&#x5217;](../../.gitbook/assets/row_space-min.png)

### 行空間\(column space\)

$$CS(A)=\{Ax| x \in F^{1\times N}\}=\begin{bmatrix}A_{: 1} & \dots & A_{:M} \end{bmatrix} \begin{bmatrix} x_1 \\ \vdots \\ x_M\end{bmatrix} = x_1A_{:1} +\cdots +x_M A_{:M} \subseteq F^{M \times 1} $$為由矩陣$$A$$的行\(column\)生成的子空間。

![&#x77E9;&#x9663;&#x7684;&#x884C;](../../.gitbook/assets/col_space-min.png)

### 核空間\(kernel space, null space\)

$$ker(A) = \{x \in F^{N \times 1} | Ax =0 \} \subseteq F^{N \times 1}$$

### 左核空間\(left kernel space\)

$$Lker(A) =\{ x \in F^{1 \times M} | xA=0\} \subseteq F^{1 \times M}$$

![&#x57FA;&#x672C;&#x5B50;&#x7A7A;&#x9593;&#x7684;&#x95DC;&#x4FC2;](../../.gitbook/assets/fundamental_space_mapping-min.png)

由定義與上圖可知$$ker(A), Lker(A)$$是定義在線性轉換$$A$$的定義域$$V$$。$$RS(A), CS(A)$$是定義在線性轉換$$A$$的值域$$W$$。





