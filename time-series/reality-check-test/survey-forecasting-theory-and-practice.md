# survey: Forecasting: theory and practice

{% embed url="https://www.sciencedirect.com/science/article/pii/S0169207021001758" %}

## 2.12.6. Statistical tests of forecast performance

這些測試為預測者提供了一些正式的保證，即領先預測的預測優勢在統計學上是顯著的，而不僅僅是由於隨機機會。

引發該領域增長的早期論文之一是 Diebold 和 Mariano（1995）。在他們的開創性論文中，DM提供了一種簡單而通用的方法來測試相等的預測能力，這個測試雖然最初不是針對模型的，但已被其他人廣泛用於測試預測模型的準確性（Diebold，2015）。

Harvey、Leybourne 和 Newbold （1998） 後來引入了修改，以改善測試的小樣本特性。為瞭解決DM測試在實踐中遇到的問題，例如巢狀模型（Clark和McCracken，2001，Clark和McCracken，2009），引數估計誤差（West，1996），協整變數（Corradi，Swanson和Olivetti，2001），高持續性（Rossi，2005）和面板資料（Timmermann\&Zhu，2019）。有限樣本預測能力測試也源於模型在有限樣本中可能具有同等預測能力的觀察，這產生了一類稱為條件預測準確性測試（Clark and McCracken， 2013， Giacomini and White， 2006）。

比較預測準確性的另一種方法是通過預測包含的概念，它檢查一個預測是否包含來自另一個預測的所有有用資訊（Chong and Hendry， 1986， Clark and McCracken， 2001， Harvey et al.， 1998）。雖然它有更多的假設，但在某些情況下，包含預測的檢驗可能比Diebold-Mariano的均方預測誤差檢驗更可取（Busetti\&Marcucci，2013）。

另一個可用的統計測試流同時檢視多個預測，而不是成對檢視。為瞭解決對「資料窺探」進行現實檢查的需求，White（2000）後來被Hansen（2005）修改，開發了一種多模型測試，該測試使用「卓越預測能力」的零假設，而不是DM測試中使用的同等預測能力。這些也被推廣到處理諸如協整變數（Corradi et al.， 2001）和多視界預測（Quaedvlieg， 2019）等問題。最近，Li、Liao 和 Quaedvlieg （2020） 提出了一種條件優越預測能力測試，類似於 Giacomini 和 White （2006） 對 DM 測試的創新。
