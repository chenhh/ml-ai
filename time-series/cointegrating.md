# 共整合(cointegration)

## 簡介

提到共整合，就不得不提平穩性(定態)。

簡單地說，平穩性（stationarity）是一個序列在時間推移中保持穩定不變的性質，它是我們在進行資料的分析預測時非常好的一個性質。如果一組時間序列資料是平穩的，那就意味著它的均值和變異數保持不變，這樣我們可以方便地在序列上使用一些統計分析。

舉一個例子，如果某個資產的價格序列（或者兩個序列的價差）是平穩的，那麼當它在偏離了其均值後，人們可以期待價格會在未來的某一個時間回歸這個均值。我們可以借助這個性質進行投資從而獲利。

平穩性是很好用，但在現實中，絕大多數的股票都是非平穩的，那麼我們是否還能夠利用平穩性質進行獲利呢？答案是肯定的，這時共整合關系（cointegration）就出場了！<mark style="color:red;">如果兩組序列是非平穩的，但它們的線性組合可以得到一個平穩序列，那麼我們就說這兩組時間序列資料具有共整合的性質</mark>，我們同樣可以把統計性質用到這個組合的序列上來。但是需要指出的一點，共整合關係並不是相關關係（correlation）。

舉例來說，兩組時間序列資料的差是平穩的，則我們可以根據這個差的平穩性進行投資獲利：當兩只股票的價差過大，根據平穩性我們預期價差會收斂，因此買入低價的股票，賣空高價的股票，等待價格回歸的時候進行反向操作從而獲利。這就是<mark style="color:red;">**配對交易（pairs trading）**</mark>的由來。
