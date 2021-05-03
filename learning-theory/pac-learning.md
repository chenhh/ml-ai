# PAC \(Probability Approximately Correct\)學習理論

## 簡介

學習是希望從舊有的經驗中找尋規則，並在面對沒有看過的資料時也能成功預測。

現在問題來了，要怎麼能夠說這個模型「學得好」了呢？是要要求它「每次」都能「零錯誤率」？這樣似乎太嚴苛了。但是多少的錯誤率是可以接受的呢？又一定要每次都對嗎？還是大部分時候是對的就好？還有「尋找使得訓練錯誤率最低的函數」﹝ERM﹞這個方法什麼時候會是不錯的方法呢？

## 同態獨立分佈\(Independently and Identically Distributed \(i.i.d\)\)

首先，機器學習中，能掌握的只有訓練錯誤率，因此當然希望我們手上的訓練資料越具普遍性越好。

為了達成這個目的，我們通常假設每一組訓練資料是獨立的從相同分佈中被選出來，即「同態獨立分佈」 \(i.i.d.\)。而如果訓練資料越多，也就越能夠反應出資料的真實機率分佈。如果說訓練資料$$S$$ 總共有$$m$$ 筆資料，而它們全部都是從$$D$$ 這個分布 i.i.d. 選出來的，那我們寫成$$S \sim D^m$$。

再來，先設想簡單的情況：假設我們所使用的機器學習方法，其選到的Hypothesis set $$H$$ 有包含目標函數$$f$$，也就是$$h^{*}(=f)$$會在 $$H$$ 裡面。

因此可在訓練後，使得真實錯誤率為0 ，即$$L_{D}(h^{*},f)=P_{x \sim D}(h^{*}(x) \neq f(x)) = 0$$。

同理可得$$h^{'} \in H$$使得訓練錯誤率為0，即$$L_S(h^{'}, f)=\frac{1}{m} \sum_{i=1}^m \mathbb{I}(h^{'}(x_i) \neq f(x_i)) =0$$。

## Probably Approximately Correct

由於訓練資料是 i.i.d. 選出來的，意味著仍有可能取到離群值。為了配合機率的因素，再定義兩個參數：『信心指數』還有『正確指數』：

* 信心指數\(confidence parameter\):$$1-\delta$$ 。
* 正確指數\(accuracy parameter\): $$\epsilon $$。

如果現在$$P( [ X<\epsilon ] )>(1-\delta )$$，表示有大於$$(1-\delta )$$ 的機率 $$X$$ 會小於$$\epsilon$$ ；而$$\epsilon$$ 通常用來描述誤差的程度。



## 參考資料

* [Probably Approximately Correct — a Formal Theory of Learning](https://jeremykun.com/2014/01/02/probably-approximately-correct-a-formal-theory-of-learning/)

