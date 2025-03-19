---
description: >-
  Ehud Lehrer,  "Approachability in infinite dimensional spaces," International
  Journal of Game Theory, Vol.31, No.2, pp. 253-268, 2003.
---

# 無限維報酬的可接近集

## 摘要

Blackwell的可接近定理被擴展到無限維回報空間。兩個玩家(玩家與對手)進行一個序貫遊戲，其回報是隨機變量。如果玩家有一個策略，能夠保證平均回報與集合S中最接近的點之間的差異幾乎肯定收斂到零，則稱隨機變量集合S對玩家來說是可接近的。文中提出了集合可接近的必要條件。

<mark style="color:red;">註：此處的無限維空間為</mark>$$L^2$$<mark style="color:red;">空間</mark>。

## 簡介

**Blackwell 的可逼近性概念(1956b):** 針對雙人序貫賽局，定義了"可逼近集S"。 玩家1 如果擁有某種策略，可以保證**平均收益向量**趨近於集合S。核心思想是讓平均報酬與集合S 的距離隨著時間趨於零。

**擴充套件到無限維空間:**&#x672C;文研究將Blackwell 的可逼近性理論**擴充套件到收益空間為無限維的**情況。這是與Blackwell 原始工作的主要區別。

**處理不同賽局場景：**&#x53EF;以將向量收益賽局視為多個同時進行的賽局。每輪中，玩家採取一個行動，該行動適用於所有正在進行的賽局。如果各賽局之間的收益不可轉移，則這些賽局的收益被視為一個向量。不僅考慮了每輪所有賽局都進行的情況（Blackwell 的原始設定），還研究了**並非所有賽局都始終進行**的情況，即每輪進行的賽局集合可能不同，某些收益坐標可能在某些輪次中不活躍。 這引入了平均收益計算的複雜性。

**平均收益的重新定義:** 在非所有賽局都進行的情況下，平均收益的計算方式被修改為：**過去收益總和/ 坐標之前活躍的次數**。 這種定義方式使得分析更加複雜，因為破壞了內積的多線性性。

**可逼近性定理的應用與發展:** 回顧了可逼近性定理的廣泛應用，包括：

* 證明Hannan 的無遺憾定理(Blackwell, 1956a; Hannan, 1957)
* 分析不完全資訊重複賽局(Aumann & Maschler, 1995)
* 校準與相關均衡研究(Foster & Vohra, 1997, 1999; Hart & Mas-Colell, 2000, 2001)
* 不完全監督下的無遺憾定理(Rustichini, 1999)
* 最小可逼近集性質研究(Spinat, 2000)**。**

**弱可逼近性和大空間可逼近性:** 提及了Blackwell 提出的弱可逼近性，以及Lehrer 和Sandroni 等人在大空間可逼近性方面的工作，及其在預測、無遺憾策略和構造正規數等方面的應用。

**論文結構:**&#x672C;文將可逼近性的**幾何面向**與**策略面**分開研究，先探討幾何原理(Section 3)，再應用於隨機變數收益賽局(Section 4)，最後討論可逼近性與大數定律的關係(Section 5)。

**總而言之，這篇文章重點關注將Blackwell 的可逼近性理論擴充套件到更複雜的賽局場景，特別是**<mark style="color:red;">**無限維收益空間和非完全活躍賽局的情況**</mark>**，並回顧了該理論的重要應用和相關研究進展。**

### 幾乎確定收斂和機率收斂

將 Blackwell 的方法（另見 Mertens, Sorin 和 Zamir（1994）第二章第四節）應用到無限維情況下，只能保證在收益空間的範數意義下的可接近性。讀者不應混淆 Blackwell 在其可接近性論述中的「幾乎確定」與平均收益的「依機率接近」。Blackwell 證明了，在幾乎所有的賽局路徑(play-path)中，平均收益與目標集合之間的歐氏範數距離會收斂到零。<mark style="color:red;">因此，「幾乎確定」這一陳述指的是賽局路徑的空間，而平均收益的收斂則是在歐氏範數意義下的收斂。</mark>

當賽局收益是定義在某個機率空間上的隨機變數時，L² 範數下的收斂僅意味著平均收益隨機變數<mark style="color:red;">依機率收斂</mark>，而非幾乎確定收斂。要證明平均收益的幾乎確定收斂需要使用一種與 Blackwell 所用方法不同的技術。

## 符號

考慮雙人重複賽局中，玩家與對手分別從可測集$$S_1, S_2$$中選取行動，令$$(s_1^n, s_2^n) \in S_1 \times S_2$$為兩人在<mark style="color:red;">時間</mark>$$n$$<mark style="color:red;">的行動對</mark>。

<mark style="color:red;">長度為</mark>$$n$$<mark style="color:red;">的歷史(history)</mark>為已觀測的行動序列$$h^n\equiv (s_1^1, s_2^1, s_1^2, s_2^2, \dots, s_1^n, s_2^n)$$。有限長度的歷史集合為$$H=\bigcup_n (S_1 \times S_2)^n$$。

&#x20;對於兩個有限長度的歷史$$h^s, h^n \in H$$，<mark style="color:red;">當</mark>$$h^s \leq h^n$$<mark style="color:red;">時，稱</mark>$$h^s$$<mark style="color:red;">為</mark>$$h^n$$<mark style="color:red;">的字首(prefix)</mark>(註：即$$h^n$$中，前$$s$$輪的行動序列和$$h^s$$完全相同，之後再進行$$n-s$$輪。)

定義$$\mathscr{H}=(S_1 \times S_2)^\infty$$為<mark style="color:red;">無限長度的歷史集合</mark>。對於無限長度的歷史$$h^\infty \in \mathscr{H}$$，記$$h^n$$為其第$$n$$個字首。

令$$(\Omega, \mu, \mathcal{F})$$為機率空間，且<mark style="color:red;">指示函數(indicator)</mark>$$\chi: H \to \{0,1\}$$<mark style="color:red;">為由有限歷史集至機率空間隨機變數</mark>。即$$\forall h \in H, \chi(h)(\omega) = \begin{cases} 1,  ~\omega \text{ is active. } \\ 0, ~\omega \text{ is inactive.} \end{cases}$$在經過歷史$$h$$後，判斷事件$$\omega$$是否激活(active)。

指示函數僅根據雙方玩家之前採取的行動，來判斷某一點$$\omega$$在第$$n$$輪是激活還是不激活。事實上，這個設定可以更加通用一些。指示函數不僅依賴於之前的行動，還依賴於玩家在當前階段的實際行動。

在$$n-1$$的歷史$$h^{n-1} \in H$$後，第$$n$$期的回報(payoff)由當期行動對$$(s_1^n, s_2^n)$$決定，記為$$Y_n(h^n)$$為定義在機率空間的隨機變數，其中$$h^n=(h^{n-1}, s_1^n, s_2^n)$$。此外，此外對於幾乎所有$$\omega \in \Omega$$，若$$\chi(h^{n-1})(\omega)=0$$，則$$Y_n(h^n)(\omega)=0$$. 即未激活的事件$$\omega$$的回報為0。

對於每一輪$$n$$，$$\tilde{\chi}(h^{n-1})=\sum_{h^s \leq h^{n-1}} \chi(h^s)$$記錄了在歷史$$h^{n-1}$$中，在$$\Omega$$中的事件激活的次數。

令$$\overline{Y}_n(h^n)=\frac{\sum_{h^s \leq h^n}Y_s(h^s)}{\tilde{\chi}(h^{n-1})}$$為事件$$\omega$$被激活的平均回報，若為0/0時設為0。假設隨機變數$$Y_n(h^n)$$定義在$$L_2(\Omega, \mu, \mathcal{F})$$空間中。

令$$C$$為$$L_2$$中的閉集合。$$\forall f \in L_2$$，令$$\mathrm{Proj}_C(f)$$為$$f$$最靠近$$C$$的點。(若$$C$$不是凸集合時不唯一)

## 定義：序列接近集合

> 給定歷史$$h^{\infty} \in \mathscr{H}$$，定義回報序列$$\{Y_n(h^n)\}$$接近閉集合$$C$$若滿足以下條件：
>
> * $$\overline{Y}_n(h^n) - \mathrm{Proj}C(\overline{Y}_n(h^n)) \to 0 ~ \mu-\text{a.s.}$$ 且$$\chi(h^n)=1$$ infinite often



## 參考資料

* Ehud Lehrer,  "[Approachability in infinite dimensional spaces](https://link.springer.com/article/10.1007/s001820200115)," International Journal of Game Theory, Vol.31, No.2, pp. 253-268, 2003.
