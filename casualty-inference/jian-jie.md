# 簡介

## 簡介

在試圖理解數據時，統計學家總是受到因果問題的動機。大多數統計書籍的索引中甚至沒有「因果」一詞。統計教科書陳述「關聯(相關性)並不意味著因果關係」，且大多數因果問題無法通過隨機實驗來解決。

這些問題的特殊性在於，它們無法用傳統的統計語言來回答，甚至無法表達。事實上，直到最近，科學才獲得了一種數學語言，我們可以用它來表達這些問題，並附帶工具，使我們能夠從數據中回答這些問題。

大量統計推斷的核心基本問題是因果關係；一個變數的變化是否會導致另一個變數的變化，如果是這樣，它們會引起多大的變化？

由於避免討論因果模型和因果參數，統計技術沒有提供如何解決因果關係的科學問題的基礎。

## Simpson’s Paradox

悖論是以最早普及它的統計學家Edward Simpson（生於1922年）的名字命名的，它指的是存在這樣的資料：<mark style="color:red;">在整個人口中成立的統計關聯在每個子人口中都被顛覆。</mark>

$$\frac{y_1+y_2}{x_1+x_2} \geq \frac{y_1}{x_1} \text{ and } \frac{y_2}{x_2}$$

例如，我們可能會發現，吸菸的學生比不吸菸的學生的平均成績要高。但是當我們考慮到學生的年齡時，我們可能會發現，在每個年齡組中，吸菸者的成績都比不吸菸者低。然後，如果我們同時考慮到年齡和收入，我們可能會發現，吸菸者的成績再次高於相同年齡和收入的非吸菸者。這種反轉可能會無限期地持續下去，隨著我們考慮越來越多的屬性，來回切換。在這種情況下，我們想決定吸菸是否會導致成績的提高，以及在哪個方向，提高多少，但從資料中獲得答案似乎沒有希望。

在<mark style="color:red;">Simpson</mark>（1951）使用的經典例子中，一群生病的病人被賦予了嘗試一種新藥的選擇。在那些服用藥物的人中，康復的比例比不服用的人低。然而，當我們按性別劃分時，我們看到，服用藥物的男性比不服用藥物的男性恢復得更多，而服用藥物的女性比不服用藥物的女性恢復得更多! 換句話說，這種藥物似乎幫助了男性和女性，但卻傷害了普通人。這似乎是無稽之談，甚至是不可能的--這就是為什麼，當然，它被認為是一個悖論。有些人覺得很難相信數字甚至可以以這種方式結合起來。

下表中，男性和女性用藥復原比例較高，但總體來看不用藥復原比例較高。

| 新藥試驗                               | 用藥             | 不用藥            |
| ---------------------------------- | -------------- | -------------- |
| <mark style="color:red;">男性</mark> | 81/87復原(93%)   | 234/270復原(87%) |
| 女性                                 | 192/263復原(73%) | 55/80復原(69%)   |
| 總和                                 | 273/350復原(78%) | 289/350復原(83%) |

為了嚴格理解數據背後的因果關係，我們需要做四件事：

1. 因果關係的定義。
2. 一種正式闡明因果假設的方法，即創建因果模型。
3. 一種將因果模型的結構與數據特徵聯繫起來的方法。
4. 一種從模型和數據中嵌入的因果假設的組合中得出結論的方法。

