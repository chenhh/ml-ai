# MDP與雙人零和賽局

## 比較表

| 特性    | MDP           | 雙人零和賽局           |
| ----- | ------------- | ---------------- |
| 決策者數量 | 單個代理人         | 兩名玩家             |
| 獎勵結構  | 單方最大化         | 零和（對抗性）          |
| 行動選擇  | 單方優化          | 雙方互動             |
| 計算方法  | 值迭代、策略迭代      | Minimax 值迭代、策略迭代 |
| 應用場景  | 單代理問題（如機器人導航） | 雙人對抗（如棋類賽局）      |

## MDP

Markov Decision Process 是一種決策制定的框架，用於解決具有馬可夫性質的問題。MDP 的基本特點包括：

* **馬可夫性**：未來狀態的機率只依賴於當前狀態，而不依賴於過去的狀態序列。
* **完全或部分資訊**：決策者可能對系統的狀態具有完全或部分的資訊。
* **長期報酬**：決策者關注的是長期報酬，而不僅僅是當前的報酬。
* **策略選擇**：決策者通過選擇最佳策略來最大化長期報酬。

## **雙人零和賽局**

* **定義**：雙人零和賽局中，兩名玩家的總收益恆為零，即一方的收益即為另一方的損失。
* **策略空間**：每個玩家在特定的狀態下需要選擇最佳策略以最大化自己的收益，並最小化對方的收益。
* **價值函式**：在零和賽局中，存在一個值 $$V(s)$$ 表示在狀態 $$s$$ 下，對於雙方都採用最優策略時，玩家 1 能獲得的收益。
* **零和性**：一方的獲利必然是另一方的損失，即總收益為零。
* **完全資訊**：兩個玩家對遊戲的狀態和可能的策略都有完全的資訊。

雙人零和賽局可以視為 擴充套件的 MDP，稱為 對策型馬可夫決策過程（Markov Game），，其特點包括：

* **多代理系統**：
  * 雙人零和賽局是多代理版本的 MDP，有兩個玩家交替進行動作。
  * 每個玩家都有自己的策略和目標函式。
* **收益結構**：
  * 對於零和賽局，玩家 1 的收益 R(s,a1,a2)R(s, a\_1, a\_2)R(s,a1​,a2​) 與玩家 2 的收益滿足關係： $$R_1(s,a1,a2)=−R_2(s,a1,a2)$$。
* **值迭代和策略迭代的應用**：
  * 在雙人零和賽局中，值迭代方法可擴充套件為 **極小化最大化（Minimax）方法**，用於計算在每個狀態下的賽局價值 $$V(s)$$。
  * 策略迭代則考慮雙方策略的更新以實現最優平衡。
* **轉移機率和動作空間**：
  * 轉移機率依賴於兩名玩家的行動。
  * 例如，狀態轉移函式 $$P(s′∣s,a_1,a_2)$$同時考慮玩家 1 和玩家 2 的行動 $$a_1$$​ 和 $$a_2$$​。
* 雙人零和賽局可以被視為一個特殊的MDP,其中:
  * 環境(對手)會針對主體的策略做出最優對抗
  * 一個玩家的收益正好是另一個玩家的損失
  * 兩個玩家輪流行動,形成交替決策過程

### 主要差異

* MDP假設環境是隨機的(stochastic),而不是對抗性的
* 雙人零和賽局中,對手明確試圖最小化玩家的收益
* MDP通常關注長期累積獎勵,而許多賽局關注單次對局結果

### 建模轉換

* 可以將雙人零和賽局轉換為特殊的MDP:
  * 狀態空間是遊戲的所有可能狀態
  * 行動空間是玩家的可選擇動作
  * 獎勵函式反映遊戲的得分機制
  * 轉移函式包含對手的最優對抗策略

### 求解方法的關聯

* MDP通常使用動態規劃或強化學習求解
* 雙人零和賽局可以使用minimax演算法
* 兩種方法都在尋找最優策略,但考慮的對手模型不同

## RL中是否可將環境視為代理人成為雙人零和賽局

<mark style="background-color:orange;">在一般強化學習問題中，環境通常被視為一個非對抗性代理</mark>。

* 環境的行為不具有策略性，而是根據**固定的機率分佈**進行轉移。
* 系統回報不一定滿足零和條件。
* 強化學習解決方案更傾向於單代理問題，通過與環境互動學習最優策略。

### 環境可以視為代理人的情況

* 當環境確實具有對抗性質時（如競技遊戲）。
* 環境的行為是為了最小化代理人的獎勵。
* 獲得的回報是零和的，即決策者的回報直接影響環境的損失，或者相反。
* 環境能夠根據代理人的行為做出策略性調整。環境的行為不是完全隨機，而是有目標地影響學習代理人的決策（如設定陷阱或阻止成功）。
* 環境行為可建模為另一個代理：環境需要具備策略或行為規則（如另一個強化學習代理）。
* 例如:在機器人對抗、棋類遊戲中。

### 不適合視為代理人的情況

* 自然環境通常不具備策略性思考。
* 許多環境的轉移機率是固定的自然法則。
* 環境可能不會刻意最小化代理人的獎勵。
* 例如:天氣系統、物理環境。

### 建模考量

* 如果將環境視為對手，可能過度複雜化簡單問題。
* 可能導致代理人採取過度保守的策略。
* 在非對抗性任務中可能降低學習效率。

### 折中方案

* 可以根據任務特性決定是否採用對抗性建模。
* 在某些子問題中採用對抗性思維。
* 保持環境模型的彈性。

### **可建模為零和賽局的情境**

1. **對抗性遊戲**：兩個玩家相互競爭，環境代理可建模為對手。
2. **對抗性強化學習**：學習防禦策略（如對抗樣本生成）。
3. **自對抗訓練**：環境代理通過對抗性行為提升決策者的策略。

### **不適用零和賽局的情境**

1. **合作式強化學習**：環境與代理共同目標（非零和）。
2. **隨機環境**：環境行為不涉及策略性（如隨機噪聲或物理系統）。