---
description: 37%法則
---

# 秘書聘選問題\(secretary problem\)

## 簡介

這個問題的基本形式如下：假設一個經理要招聘一位秘書，他要從$$N$$個應聘者中選出最優者。

這些應聘者以隨機的順序接受面試，每個應聘者面試結束後，經理需要立刻最初決定選此人還是不選此人。如果不選，此應聘者就不能再選了。面試過程中，經理可以為所有已經面試的應聘者評分，但是它無法獲知尚未面試的應聘者的素質如何。 

 問，它運用怎樣的策略使選中最佳秘書的概率最大化。 **如果聘選決定可以推遲到整個面試結束再作出，那麼就可以用簡單的最大值選取算法解決。難就難在，聘選決定必須當即作出**。

這個問題的最佳方案就是拒絕前$$\frac{N}{e}$$ 個面試者，然後選擇之後遇到的第一個比之前所有面試者都優秀的應聘者，如果隨後沒有出現這樣的應聘者，就選擇最後一個應聘者。

這個策略也叫作 $$\frac{1}{e}$$  停止法則，因為對於一個有限的$$N$$，選中最佳秘書的概率約為$$\frac{ 1}{e}$$ （即36.79%）。 秘書問題之所以備受關注，是因為這個問題採取的最優策略簡單易行，而且選中最佳秘書的概率總是37%。無論是有100個還是100萬個應聘者，其實對於任意的$$N$$，只要採用這一策略，選中最佳秘書的概率總是$$\frac{1}{e}$$。

此問題的最優策略為停止法則。 在此條件下，假設面試官拒絕前$$r−1$$個人（令應聘者$$M$$為這前$$r−1$$個人中的最優者）然後選擇接下來第一個比$$M$$優秀的應聘者。可以證明，最佳策略屬於這類策略集。

對於任意一個數$$r$$，選中最佳應聘者的機率為

$$\displaystyle \mathrm{P}(r)=\sum_{i=1}^N \mathrm{P}(\text{applicant i is selected and the applicant is the best}) = \sum_{i=1}^N \mathrm{P}(\text{ applicant i is selected or the applicant is the best})\times \mathrm{P}(\text{applicant i is the best}) = \bigg [sum_{i=1}^{r-1}0 + sum_{i=1}^N \text{the best of the first i-1 applicants is in the first r-1 applicants} | \text{ appplicant  i is the best} \bigg] \times \frac{1}{N} = \sum_{i=r}^N \frac{r-1}{i-r}\times \frac{1}{N} =\frac{r-1}{N}\sum_{i=r}^N \frac{1}{i-1}$$



* $$ r=1$$的情況不在這個和式的定義當中，不過對於此例，易見 $$P(1)=1/N$$。
* $$\displaystyle \lim_{N \rightarrow \infty}\mathrm{P}(r) =  \lim_{N \rightarrow \infty}\frac{r-1}{N} \sum_{i=r}^N \frac{1}{i-1}$$
* 令$$x=\frac{r}{N}$$, $$t=\frac{i}{N}$$, $$dt=\frac{1}{N}$$, 可得$$\mathrm{P}(x)=x \int_x^1 \frac{1}{t}dt=-x\log(x)$$，最大值在$$x=\frac{1}{e}$$\(QED\)

## 討論

適用於這個問題的場景很少，換句話說，這個問題需要滿足的條件很苛刻，它至少要滿足。

* 待選數列/候選人/應聘者應該是隨機數列。
* 數列各個元素應該有明顯可辨別的大小關係。
* 決策者知道$$N$$值的大小。
* 所有被拒絕者不可重用。
* 當事人必須立即決定。
* 一旦決定選用某個位置的數/候選人/應聘者，後續的元素永遠無法被選擇。



