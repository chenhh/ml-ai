# 直方圖（Histogram）與長條圖（Bar chart）

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption><p>直方圖和長條件的比較</p></figcaption></figure>

直方圖主要在呈現資料分佈的結果，長條圖呈現的是各組資料的大小。直方圖的橫軸變數為「數值型連續變數」，長條圖則為「類別型離散變數」。至於組距的「間隔」，直方圖各組距之間是連線在一起的，彼此之間沒有間隔；長條圖則是組距之間存在著間隔（有人認為，有間隔才能呈現分佈的狀態，並讓直方圖和長條圖能有區隔；但也有人認為，有無間隔，差異不大）。

另外，直方圖的組距是有順序的，所以不可相互置換，而長條圖則無順序，可以置換。但長條圖也因為可以置換，通常在畫出圖形後，可以對橫軸的組別，依次數大小進行排序，以利使用者用在後續的決策制定。

此外，直方圖裡各組距次數的加總，即為條形圖的總面積，每個條形圖背後所佔的面積，就代表每個組距中包含的次數。當組距變大時，會使得條形圖的高度跟著改變。

最後，直方圖與長條圖在使用上，有時並不明確。舉例來說，業績報表中常會以「顧客年齡」作為呈現的依據，而年齡是數值型態的連續變數，所以是透過直方圖來呈現（如圖3所示，在此以有間隔方式呈現）。然而，一旦以顧客業績做為排序的依據時（亦即將顧客業績依高至低進行排列），這時候，各個年齡組距的順序就會被打破，此時就會呈現出企業顧客最重要的年齡組距。

## 參考資料

* [如何分辨長相近似的孿生兄弟-直方圖（Histogram）與長條圖（Bar chart）之差異](https://medium.com/marketingdatascience/%E5%A6%82%E4%BD%95%E5%88%86%E8%BE%A8%E9%95%B7%E7%9B%B8%E8%BF%91%E4%BC%BC%E7%9A%84%E5%AD%BF%E7%94%9F%E5%85%84%E5%BC%9F-%E7%9B%B4%E6%96%B9%E5%9C%96-histogram-%E8%88%87%E9%95%B7%E6%A2%9D%E5%9C%96-bar-chart-%E4%B9%8B%E5%B7%AE%E7%95%B0-154602ac0ba6)。
*
