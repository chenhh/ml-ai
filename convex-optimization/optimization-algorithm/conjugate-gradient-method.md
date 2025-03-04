---
description: conjugate gradient method
---

# 共軛梯度法

## 簡介

共軛梯度法 (Conjugate Gradient method，簡稱 CG 法) 是一種**迭代演算法**，主要用於解決以下兩類重要的數學問題：

1. **解線性方程組**: 特別是大型且稀疏的線性方程組$$Ax=b$$，其中$$A$$ 是一個對稱正定矩陣$$(A^\top =A$$，且$$\forall x \in \mathbb{R}^n, x^\top A x > 0$$)。
2. **無約束最佳化問題**: 尋找目標函式$$f(x)$$ 的最小值，尤其當$$f(x)$$ 是二次函式時，CG 法表現出色。

共軛梯度法（Conjugate Gradient Method）可以用於有約束的最佳化問題(使用Lagrange multiplier)，但需要一些調整，因為基本的共軛梯度法是設計來解決無約束的最佳化問題。

### **核心思想**

共軛梯度法的核心思想是通過構造一組**共軛方向** （conjugate directions），在這些方向上進行搜尋，逐步逼近真實解。與傳統梯度下降法相比，共軛梯度法避免了搜尋方向之間的相互干擾，從而實現更快的收斂速度。

1. **共軛方向** ：若兩個向量$$p_i$$​ 和 $$p_j$$​ 滿足 $$p_i^\top ​A p_j​=0,~  i \neq j$$，則稱它們是關於矩陣$$A$$ 的共軛方向。共軛性可以視為一種廣義的「正交性」，它是針對特定的矩陣$$A$$ 定義的。
2. **優化過程** ：共軛梯度法將問題$$Ax=b$$轉化為二次型優化問題：$$f(x)=\frac{1}{2}x^\top A x -b^\top x$$，目標是最小化這個函式，其極小值點就是原方程$$Ax=b$$的解。

為了理解共軛方向的重要性，我們先簡單回顧一下最速下降法 (Steepest Descent)。

**最速下降法的缺點**: 最速下降法在每次迭代中都沿著**負梯度方向**（函式下降最快的方向）搜尋。雖然每一步都能有效減小函式值，但其搜尋路徑常常呈「鋸齒狀」，導致收斂速度較慢，尤其在接近解時更為明顯。

<figure><img src="../../.gitbook/assets/image (108).png" alt="" width="440"><figcaption><p>最速下降法搜尋路徑常常呈「鋸齒狀」，導致收斂速度較慢，特別是在接近解。</p></figcaption></figure>

**共軛方向的優勢**: 共軛梯度法克服了最速下降法的缺點，它選取的搜尋方向不是簡單的負梯度方向，而是彼此**共軛**的方向。共軛方向具有一個重要的特性：**沿著一個共軛方向搜尋得到的最佳點，不會破壞沿著先前共軛方向已達到的最佳性**。 換句話說，每一輪迭代都能在已搜尋的方向上保持最佳狀態，從而實現更快速且更穩定的收斂。

## **演算法步驟**

1. **初始化** ：
   * 初始猜測解$$x_0$$​ （通常設為零向量）。
   * 計算初始殘差$$r_0​=b−Ax_0$$​。
   * 設初始搜尋方向 $$p_0​=r_0$$​。
2. **迭代更新** ： 對於 $$k=0,1,2,\dots$$, 直到滿足停止條件：
   * 計算步長 $$\alpha_k =\frac{r_k^\top r_k}{p_k^\top A p_k}$$，其目的是確保沿著方向$$p_k$$ ​搜尋時，函式$$f(x)$$ 能夠達到最小化。。
   * 更新解$$\mathbf{x}_{k+1} =x_k + \alpha_k p_k$$
   * 更新殘差 $$\mathbf{r}_{k+1}=r_k - \alpha_k A p_k$$
   * 計算共軛係數 (Conjugate Parameter)$$\beta_k = \frac{r_{k+1}^\top r_{k+1}}{r_k^\top r_k}$$，用於確定下一個搜尋方向。
   * 計算新的搜尋方向 $$\mathbf{p}_{k+1}=r_{k+1}+\beta_k p_k$$。新的搜尋方向$$p_{k+1}$$ ​是當前殘差方向 $$r _{k+1}$$ ​和前一個搜尋方向$$p_k$$ ​的線性組合，保證了$$p_{k+1}$$ ​與之前的搜尋方向是$$A-$$共軛的。
   * 停止條件 ： 若殘差$$\|r_k\|<\epsilon$$小於某個預設的容差（tolerance），則停止迭代。



```python
import numpy as np

def conjugate_gradient(A, b, x0=None, tol=1e-5, max_iter=1000):
    """
    共軛梯度法求解 Ax = b
    參數：
        A: 對稱正定矩陣 (numpy array)
        b: 右端向量 (numpy array)
        x0: 初始猜測 (numpy array)，預設為零向量
        tol: 收斂容差
        max_iter: 最大迭代次數
    返回：
        x: 解向量
        k: 迭代次數
    """
    n = len(b)
    if x0 is None:
        x = np.zeros(n)  # 初始解設為零向量
    else:
        x = x0.copy()

    r = b - A @ x  # 初始殘差
    p = r.copy()   # 初始搜索方向
    r_norm_sq = r @ r  # 殘差的平方範數

    for k in range(max_iter):
        Ap = A @ p
        alpha = r_norm_sq / (p @ Ap)  # 步長
        x = x + alpha * p             # 更新解
        r_new = r - alpha * Ap        # 更新殘差
        r_new_norm_sq = r_new @ r_new # 新殘差的平方範數

        # 檢查是否收斂
        if np.sqrt(r_new_norm_sq) < tol:
            return x, k + 1

        beta = r_new_norm_sq / r_norm_sq  # 更新參數 beta
        p = r_new + beta * p             # 更新搜索方向
        r = r_new                        # 更新殘差
        r_norm_sq = r_new_norm_sq        # 更新殘差範數

    print("警告：達到最大迭代次數，未完全收斂")
    return x, max_iter

# 測試函數
def test_conjugate_gradient():
    # 範例問題：Ax = b
    A = np.array([[4, 1], [1, 3]], dtype=float)  # 對稱正定矩陣
    b = np.array([1, 2], dtype=float)            # 右端向量
    x_exact = np.linalg.solve(A, b)              # 精確解 (用於比較)

    # 使用共軛梯度法求解
    x_cg, iterations = conjugate_gradient(A, b)
    
    print("矩陣 A：\n", A)
    print("向量 b：", b)
    print("共軛梯度法解 x：", x_cg)
    print("精確解 x_exact：", x_exact)
    print("迭代次數：", iterations)
    print("誤差範數：", np.linalg.norm(x_cg - x_exact))

if __name__ == "__main__":
    test_conjugate_gradient()
    
/*
矩陣 A：
 [[4. 1.]
 [1. 3.]]
向量 b： [1. 2.]
共軛梯度法解 x： [0.09090909 0.63636364]
精確解 x_exact： [0.09090909 0.63636364]
迭代次數： 2
誤差範數： 0.0
*/    
```

```python
import numpy as np
# 使用linalg.cg方法求解
from scipy.sparse.linalg import cg

def test_conjugate_gradient_scipy():
    # 範例問題：Ax = b
    A = np.array([[4, 1], [1, 3]], dtype=float)  # 對稱正定矩陣
    b = np.array([1, 2], dtype=float)            # 右端向量
    x_exact = np.linalg.solve(A, b)              # 精確解 (用於比較)

    # 使用 SciPy 的共軛梯度法求解
    x_cg, info = cg(A, b, rtol=1e-5, maxiter=1000)
    
    # info 表示收斂狀態：0 表示成功收斂，>0 表示未收斂
    if info == 0:
        print("SciPy CG 成功收斂")
    else:
        print(f"SciPy CG 未完全收斂，info = {info}")

    print("矩陣 A：\n", A)
    print("向量 b：", b)
    print("SciPy CG 解 x：", x_cg)
    print("精確解 x_exact：", x_exact)
    print("誤差範數：", np.linalg.norm(x_cg - x_exact))

if __name__ == "__main__":
    test_conjugate_gradient_scipy()
    
/*
SciPy CG 成功收斂
矩陣 A：
 [[4. 1.]
 [1. 3.]]
向量 b： [1. 2.]
SciPy CG 解 x： [0.09090909 0.63636364]
精確解 x_exact： [0.09090909 0.63636364]
誤差範數： 0.0
*/
```



```python
import numpy as np
# 使用minimize的cg求解
from scipy.optimize import minimize

def objective_function(x, A, b):
    """
    定義目標函數 f(x) = 1/2 * x^T A x - b^T x
    """
    return 0.5 * x.T @ A @ x - b.T @ x

def test_conjugate_gradient_minimize():
    # 範例問題：Ax = b
    A = np.array([[4, 1], [1, 3]], dtype=float)  # 對稱正定矩陣
    b = np.array([1, 2], dtype=float)            # 右端向量
    x_exact = np.linalg.solve(A, b)              # 精確解 (用於比較)

    # 初始猜測
    x0 = np.zeros(2)

    # 使用 minimize 的共軛梯度法求解
    result = minimize(
        fun=objective_function,  # 目標函數
        x0=x0,                   # 初始點
        args=(A, b),             # 傳遞 A 和 b
        method='CG',             # 使用共軛梯度法
        tol=1e-5                 # 收斂容差
    )

    # 提取結果
    x_cg = result.x
    success = result.success
    iterations = result.nit

    print("矩陣 A：\n", A)
    print("向量 b：", b)
    print("SciPy minimize CG 解 x：", x_cg)
    print("精確解 x_exact：", x_exact)
    print("是否成功收斂：", success)
    print("迭代次數：", iterations)
    print("誤差範數：", np.linalg.norm(x_cg - x_exact))

if __name__ == "__main__":
    test_conjugate_gradient_minimize()
    
/*
矩陣 A：
 [[4. 1.]
 [1. 3.]]
向量 b： [1. 2.]
SciPy minimize CG 解 x： [0.09090909 0.63636363]
精確解 x_exact： [0.09090909 0.63636364]
是否成功收斂： True
迭代次數： 2
誤差範數： 4.3893454415659835e-09
*/
```

### 預處理 (Preconditioning)

對於某些病態 (ill-conditioned) 的矩陣 $$A$$ (條件數很大)，共軛梯度法可能收斂速度較慢。為了加速收斂，可以引入預處理技術 (Preconditioning)。

預處理的思想是找到一個容易求逆的矩陣 $$M$$ (稱為預處理子)，使得預處理後的系統 $$M^{−1} Ax=M^{−1} b$$ 或 $$AM^{−1} y=b,~x=M^{−1} y$$ 比原始系統更容易求解。

理想的預處理子$$M$$應該滿足以下條件：

* $$M$$ 近似於$$A$$ (使得預處理後的系統條件數較小)。
* $$M^{−1}$$容易計算。
* 求解形如$$Mz=w$$ 的系統是容易的。

常用的預處理方法包括：對角預處理、不完全 Cholesky 分解預處理、不完全 LU 分解預處理等。

### **主要優勢**

1. **快速收斂** ：對於對稱正定矩陣，理論上最多需要$$n$$步即可精確求解（實際應用中通常遠少於$$n$$ 步）。
2. **儲存需求低** ：只需要儲存少量向量（如$$\mathbf{x}, \mathbf{r}, \mathbf{p}$$），適合處理大型稀疏矩陣。
3. **無需矩陣分解** ：避免了矩陣分解帶來的高計算成本。

### **侷限性**

1. **適用範圍有限** ：僅適用於對稱正定矩陣。對於非對稱或不定矩陣，需要使用其他變體（如廣義最小殘差法 GMRES 或雙共軛梯度法 BiCG）。
2. **精度依賴於浮點運算** ：由於計算過程中涉及多次疊代，累積誤差可能影響結果精度。

## 參考資料

* Jonathan Richard Shewchuk,  "An introduction to the conjugate gradient method without the agonizing pain," 1994.
