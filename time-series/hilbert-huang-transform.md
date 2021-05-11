# Hilbert-Huang transform \(HHT\)

## 簡介

**一般自然和物理界中所觀察到的振盪訊號多半呈現出非穩態\(non-stationary）及非線性（nonlinear）之特性**。傳統傅立葉（Fourier）分析法僅能求得整段訊號之平均振盪頻率；且傅立葉頻譜（Fourier spectrum）中之眾多諧和模態（harmonic modes） 乃是傅立葉解析\(Fourier decomposition）過程中將訊號展開成固定頻率諧和函數\(harmonic functions）組合之產物，其與訊號本身之振動型態並無直接對應之物理關聯。**對於振動頻率及振幅隨時都在改變之非穩態時間訊號而言，傅立葉頻譜無法提供訊號瞬時振動頻率變化及其相關訊息**。

瞬時頻率頻譜分析法（instantaneousfrequency-timeanalysis）分析從自然界或生物體中所記錄的一些訊號。此法主要分成兩個步驟：

1. 首先將訊號分解成一系列非固定頻率之本質模態函數之組合（intrinsicmodefunctions,IMF）；
2. 接下來再將這些函數經希爾伯特（Hilbert）轉換以求得各個模態函數之瞬時頻率（instantaneousfrequency）與振幅（amplitude）隨時間變化之關係。

**藉由此種方式所獲得之希爾伯特頻譜代表著原始訊號所含能量於頻域（frequencydomain）和時域（timedomain）上的分佈狀態。**相較於傅立葉頻譜僅能提供訊號平均能量之分佈，瞬時頻率頻譜更提供了訊號振盪頻率和能量隨時間變化之情形。**由於此法是根據訊號局部時間尺度來將原始訊號分解成各個不同的模態函數**，因此可用於分析處理非穩態之時間序列

