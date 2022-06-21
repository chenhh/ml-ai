# 時間序列分解

## 簡介

時間序列數據可以表現出多種模式，將時間序列拆分為多個組件通常很有幫助，每個組件代表一個基礎模式類別。

一般常見三種類型的時間序列模式：<mark style="color:red;">**趨勢、季節性和週期**</mark>。因此當我們將時間序列分解為組件時，我們通常將<mark style="color:red;">趨勢和週期組合成單個趨勢週期組件</mark>（為簡單起見，有時稱為趨勢）。<mark style="background-color:red;">因此，我們認為時間序列包含三個部分：</mark><mark style="background-color:red;"><mark style="color:red;">趨勢週期部分、季節性部分和剩餘部分<mark style="color:red;"></mark><mark style="background-color:red;">（包含時間序列中的任何其他內容）</mark>。

#### 加性分解(additive decomposition)

$$y_t=S_t+T_t+R_t$$

* $$y_t$$為資料，$$S_t$$為季節性部份，$$T_t$$為趨勢週期部份，$$R_t$$為剩餘部份。
* 如果季節性波動的幅度或圍繞趨勢週期的變化不隨時間序列的水平而變化，則加性分解是最合適的。

#### 乘法分解(multiplicative decomposition)

$$y_t=S_t \times T_t \times R_t$$

當季節性模式的變化或趨勢週期的變化似乎與時間序列的水平成正比時，乘法分解更合適。乘法分解在經濟時間序列中很常見。
