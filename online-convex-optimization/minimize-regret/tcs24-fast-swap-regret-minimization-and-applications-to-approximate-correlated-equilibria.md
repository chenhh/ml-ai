# TCS24: Fast Swap Regret Minimization and Applications to Approximate Correlated Equilibria

## 摘要

我們給出一個簡單且計算高效的演算法，對於任何常數 ε > 0，僅需 T = polylog(n) 輪即可獲得 εT 的交換遺憾；與最先進演算法所需的超線性輪數相比，這是一個指數級的改進，並解決了 \[Blum and Mansour 2007] 的主要開放問題。我們的演算法對 ε 具有指數依賴性，但我們證明了一個新的、匹配的下界。

我們的交換遺憾演算法意味著在幾個領域中更快地收斂到 ε-相關均衡 (ε-CE)：對於具有 n 個動作的正規形式雙人賽局，它意味著第一個非耦合動態，可以在多對數輪次中收斂到 ε-CE 集；一個用於雙人賽局中 ε-CE 的 polylog(n) 位通訊協議（解決了 \[Babichenko-Rubinstein'2017, Goos-Rubinstein'2018, Ganor-CS'2018] 提到的一個開放問題）；以及一個用於 ε-CE 的 O\~(n) 查詢演算法（解決了 \[Babichenko'2020] 的一個開放問題，並在查詢複雜度模型中首次實現了 ε-CE 和 ε-納什均衡之間的分離）。

對於擴展形式賽局，我們的演算法意味著一個用於正規形式相關均衡的 PTAS（多項式時間近似方案），該解概念通常被推測為計算上難以處理的（例如 \[Stengel-Forges'08, Fujii'23]）。

## 參考資料

Binghui Peng and Aviad Rubinstein. "Fast swap regret minimization and applications to approximate correlated equilibria" Proceedings of the 56th Annual ACM Symposium on Theory of Computing. 2024.
