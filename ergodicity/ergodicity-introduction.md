# 遍歷性簡介

## 簡介

<mark style="color:red;">遍歷性: 是指時間平均值與空間平均值相類似</mark>。簡單點說，就是機率在時間上的分佈和機率在空間上的分佈，是可以相互替代的。

<mark style="color:red;">**如果有一個隨機過程，其過往的歷史機率不能適用於其未來的情景，那麼這個隨機過程就不具有遍歷性**</mark>。這一性質是隨著條件的變化，過往的成功經驗並不必然適用於未來和當下。

無論是對於時間的觀測樣本，還是對於空間的觀測樣本，都可以用相同的統計學的數學描述。只是一個對於時間，一個對於位置。

舉例來說: 假設你想買雙鞋且你家樓下就是間鞋店。你有兩個辦法:&#x20;

* \[時間]一個是你每天到樓下去找鞋子，最終你會找到最棒的一雙鞋。
* \[空間]另一個則是你開車到鎮上花一整天四處找鞋，找有賣有最棒一雙鞋的地方。

若這兩個辦法得出的結果一致，則該系統具遍歷性。

因為在工程應用中，我們通常無法到所有的樣本函數來構成樣本空間，所以希望通過有限次的觀測，或者一次觀測，就能夠描述這個過程的一些性質<mark style="color:red;">。對遍歷性隨機過程，只需觀察一條樣本函式且觀測時間足夠長，就可以得到隨機過程的所有取值狀態及每個狀態的機率分佈</mark>。

舉例來說：我們認為每次的樣本函數，是關於時間的單值。當該過程是遍歷的：則時間平均等於統計平均；時間自相關（Time autocorrelation)等於統計自相關(statistical autocorrelation)；也就是說，我們不需要知道這個隨機過程的所有樣本函數，就能得到相同結果。

## 遍歷性的起源

遍歷性的起源

## 參考資料

[https://www.zhihu.com/question/26070689](https://www.zhihu.com/question/26070689)