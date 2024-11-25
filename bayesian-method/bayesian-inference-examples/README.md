# 貝氏推論範例

## PyMC

PyMC 是一個用於貝氏統計建模和機率程式設計的 Python 庫。它允許使用者建構複雜的統計模型，並使用高效的演算法進行參數估計和推斷。

### **主要特點**

1. **貝氏統計建模**：
   * PyMC 提供了一個靈活的框架，用於建構貝氏統計模型。
   * 使用者可以定義先驗分佈、似然函數和後驗分佈，並使用 MCMC（Markov Chain Monte Carlo）等方法進行參數估計。
2. **機率程式設計**：
   * PyMC 支援機率程式設計，允許使用者以程式設計方式定義和操作隨機變數。
   * 使用者可以輕鬆地建構複雜的機率圖模型（Probabilistic Graphical Models, PGMs）。
3. **高效的採樣演算法**：
   * PyMC 內建了多種高效的採樣演算法，如 Metropolis-Hastings、Hamiltonian Monte Carlo (HMC) 和 No-U-Turn Sampler (NUTS)。
   * NUTS 是一種自適應的 HMC 演算法，能夠在高維空間中高效採樣。
4. **自動微分**：
   * PyMC 利用 Theano（PyMC3）或 TensorFlow Probability（PyMC4/5）進行自動微分，這使得梯度計算更加高效。
   * 自動微分對於最佳化和採樣演算法非常重要，特別是對於複雜的模型。
5. **可視化和診斷工具**：
   * PyMC 提供了一系列工具，用於可視化和診斷採樣結果。
   * 使用者可以使用 ArviZ 庫來繪製後驗分佈、鏈收斂圖和跡線圖等。
6. **靈活的模型定義**：
   * PyMC 的模型定義語法簡潔明了，使用者可以使用 Python 程式碼直接定義模型。
   * 支援各種分佈類型，包括連續分佈、離散分佈和混合分佈。

### **常見應用場景**

1. **貝氏線性回歸**：用於回歸分析，預測連續變數。
2. **貝氏邏輯回歸**：用於分類問題，預測離散變數。
3. **混合效應模型**：處理層次結構資料，如多級模型。
4. **時間序列分析**：處理時間序列資料，如 ARIMA 模型、狀態空間模型、季節性預測。
5. **生存分析**：處理生存時間資料，如 Cox 比例風險模型。
6. **統計建模**：用於估計未知引數及其不確定性。
7. **貝氏推斷**：在資料中包含先驗資訊時，進行更新。
8. **AB 測試**：分析不同變體的效能。
9. **醫學研究**：用於臨床試驗的資料分析，評估治療效果。
10. **經濟學**：用於預測經濟指標，評估風險。
11. **環境科學**：用於氣候變化的模擬和預測。

## 常用功能 <a href="#chang-yong-gong-neng" id="chang-yong-gong-neng"></a>

* **模型定義**：使用PyMC的API定義模型的各個組成部分，如隨機變數和機率分佈。
* **採樣**：使用MCMC或其他推理方法對模型進行採樣，獲得後驗分佈的樣本。
* **後處理**：對採樣結果進行分析，如計算後驗均值、置信區間等。
* **視覺化**：使用ArviZ等庫進行結果的視覺化。

### **PyMC 的核心元件**

1. **隨機變數** (`pm.Distributions`)
   * 提供了豐富的機率分佈（如正態分佈、貝塔分佈、Gamma 分佈等），用於定義模型的引數和資料生成過程。
2. **模型構建** (`pm.Model`)
   *   使用上下文管理器構建模型：

       ```python
       python複製程式碼with pm.Model() as model:
           alpha = pm.Normal("alpha", mu=0, sigma=10)
           beta = pm.Normal("beta", mu=0, sigma=10)
           y_obs = pm.Normal("y_obs", mu=alpha + beta * x, sigma=1, observed=y)
       ```
3. **抽樣器與推斷方法**
   * 支援如 Metropolis、Gibbs 和高效的 NUTS（基於哈密頓動力學的 MCMC 方法）抽樣器。
   * 提供變分推斷作為高維資料的快速近似解。
4. **後驗分析工具**
   * 內建豐富的視覺化和診斷工具（如跡圖、直方圖和引數間的關係圖），支援模型檢查和解釋。

## 印出PyMC的版本

```python
import pymc
print(pymc.__version__)
```



## 參考資料

* [https://github.com/pymc-devs/pymc-examples](https://github.com/pymc-devs/pymc-examples)
* [https://discourse.pymc.io/](https://discourse.pymc.io/)
*
