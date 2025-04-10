# 計數過程(counting process)

## 計數過程

計數隨機過程是一種用於描述事件發生次數的隨機過程。它通常用於建模和分析隨時間推移事件累積的情況，例如電話呼叫到達、顧客進店、網路資料包到達等場景。

## 計數過程定義

> 令隨機變數$$N(t)$$為時間$$0 \sim t$$ (包含時間$$t$$)時，已經發生的事件累積總數，則隨機過程$$\{N(t),t≥0\}$$稱為計數過程 (counting process)，其必須滿足以下條件：
>
> * $$N(t) \in \mathbb{N} \cup \{0\}$$，已發生的事件總數為自然數(包含0)。
> * \[非負性]$$N(0)=0$$，即初始時刻沒有事件發生。。
> * \[單調性] $$s \leq t$$，$$N(s) \leq N(t)$$，非遞減數列。
> * $$s < t, N(t) - N(s)$$為發生在區間$$(s,t]$$的事件總數。



![計數過程](../../.gitbook/assets/counting-process-min.png)

* 階梯狀的計數，表示次數逐漸增加(每計數一次就  +1 )。
* 時間$$t_i$$是隨機的，也就是計數過程隨機的部分是在於我們不知道某事件到底會在什麼時候發生。
* 計數過程是右連續 (簡單說就是上圖對任l意計數的右方逼近可以得到實黑點；在時間$$t_2$$ 計數為 2而不是1 )。
* 例如$$N(t_3 )−N(t_1 )=2為$$時間$$(t_1,t_3]$$內事件發生2次。

### 獨立增量性（Independent Increments）

> 如果發生在不相交區間的事件數為獨立時，則稱計數過程有**獨立增量(independent increment)**。
>
> 例如$$N(t)$$為發生在時間$$t$$之前的總事件數，其獨立於時間$$t$$至$$t+s$$的$$N(t+s)−N(t)$$發生事件數。>

### **平穩增量性**（Stationary Increments）

> **因此如果任意時間區內內發生的事件數分佈只與時間區度的長度有關時（同樣長度區間的機率分佈均相同），稱計數過程有平穩增量(stationary increment)**。
>
> 例如若為平穩增量時，則$$(t_1+s,t_2+s]$$ 應與$$(t_1,t_2]$$內的發生事件數有相同分佈。
>
> $$N(t_2 +s )- N(t_1 +s )\overset{d}{=} N(t_2) - N(t_1)$$。

### 時間連續性

> 計數隨機過程在大多數情況下是右連續的（right-continuous），並且幾乎處處有限。

## 常見計數隨機過程模型



* 泊松過程（Poisson Process）：泊松過程的計數函式$$N(t)$$ 在時間$$t$$的分佈服從泊松分佈$$P(\lambda)$$，是單位時間內隨機事件發生的次數（頻率）的離散機率分佈，$$\lambda$$是單位時間內事件發生的平均次數。。
* &#x20;非齊次泊松過程（Non-Homogeneous Poisson Process, NHPP）：其事件發生的強度$$\lambda(t)$$是時間的函數，而非固定值。這意味著事件發生的速率可能隨著時間變化。
* 更新過程（Renewal Process）：更新過程是另一種重要的計數隨機過程，它描述了事件之間的間隔時間序列$$\{T_i\}$$，這些間隔時間通常是獨立同分佈的隨機變數。更新過程的計數函式$$N(t)$$ 表示在時間$$t$$前發生的事件總數。

## **應用場景**

* **保險數學**：索賠次數建模。
* **電信網路**：封包的到達過程。
* **可靠性工程**：系統故障的發生次數。
* **等候理論**：顧客到達服務系統。





