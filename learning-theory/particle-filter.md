# 粒子濾波器(particle filter)

## 簡介

粒子濾波是指通過尋找一組在狀態空間中傳播的隨機樣本對機率密度函數$$\mathrm{P}(x_k|z_k)$$進行近似，以樣本均值代替積分運算，進而獲得狀態最小變異估計的過程，這些樣本稱為「粒子」。

對於平穩的隨機過程，假設$$k-1$$​時的系統的後驗機率密度為$$\mathrm{P}(x_{k-1}|z_{k-1})$$，依據一定原則選取$$n$$​個隨機樣本點，則$$k$$​時刻獲得觀測資訊後，經過狀態和時間更新過程，$$n$$​個粒子的後驗機率密度函數可以近似為$$\mathrm{P}(x_k|z_k)$$，隨替粒子數目的增加，粒子的機率密度函數逐漸逼近狀態的機率密度函數，粒子濾波估計即達到了最佳貝式估計的效果。

粒子濾波器不需要非線性濾波器問題中，隨機變數必須滿足高斯分佈的條件，且緩解了樣本數不足的問題。
