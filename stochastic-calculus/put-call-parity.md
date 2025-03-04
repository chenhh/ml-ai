---
description: 買權賣權平價理論
---

# put-call parity





## 選擇權(期權，option)

買權報酬函數(payoff function)(不含選擇權價格)：$$(S-K)^{+} \equiv \max(S-K, 0)$$

賣權報酬函數(不含選擇權價格)：$$(S-K)^{-} \equiv \max(0, K-S)=-\min(0, S-K)$$

## put-call parity

$$C_t- P_t=S_t - Ke^{-r(T-t)}$$

* $$C_t \equiv C(S_t,t)$$：為標的資產(underlying asset)價格為$$S_t$$在時間$$t$$時的買權價格。
* $$P_t \equiv P(S_t,t)$$：為標的資產價格為$$S_t$$在時間$$t$$時的賣權價格。
* $$K$$：(歐式)選擇權的履約價(strike or exercise price)。
* $$r$$：年化無風險資產報酬率。

| 持有部位 | 當期(t)價格                      | 到期日(T)價格           |
| ---- | ---------------------------- | ------------------ |
| 買權   | $$C_t$$                      | $$\max(S_T-K,0)$$  |
| 賣權   | $$-P_t$$                     | $$-\max(K-S_T,0)$$ |
| 股票   | $$-S_t$$                     | $$-S_T$$           |
| 現金   | $$Ke^{-r(T-t)}$$             | $$E$$              |
| 合計   | $$C_t-P_t-S_t+Ke^{-r(T-t)}$$ | $$0$$              |









