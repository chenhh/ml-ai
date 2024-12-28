---
description: conference paper
---

# A Novel Approach of Option Portfolio Construction Using the Kelly Criterion

Mu-En Wu\*, Wei-Ho Chung, “A Novel Approach of Option Portfolio Construction Using the Kelly Criterion”, IEEE Access, Volume 6, Issue 1, pp 53044-53052, Dec. 2018.



{% file src="../../.gitbook/assets/A_Novel_Approach_of_Option_Portfolio_Construction_Using_the_Kelly_Criterion.pdf" %}
paper
{% endfile %}

Mu-En Wu, Wei-Ho Chung, Chia-Jung Lee, “On the Analysis of Kelly Criterion and Its Application, ” In Proceedings of the 11th Asian Conference on Intelligent Information and Database Systems (ACIIDS 2019), Apr. 8-11, 2019, Yogyakarta, Indonesia.

## 摘要

資金管理是金融交易中最重要的問題之一。資金管理的許多技能都基於Kelly 準則，該準則對部位大小的最佳分數進行出價的理論最佳化。然而，資金管理的理論與實際交易之間仍然存在很大差距。在本文中，我們通過 Kelly 準則設計了一個選擇權交易策略。雖然選擇權的價格波動很大，但各種選擇權的投資組合可以通過以不同的行權價做多或做空來形成，以預先鎖定損失和利潤；然後我們通過持有選擇權投資組合進行固定的損益分配。因此，Kelly準則可以應用於選擇權交易，以計算最佳下注比例。我們提出了一種選擇權交易方法，通過下注最佳比例來查詢有利可圖的選擇權投資組合。與以前的工作相比，我們提出的模型是一種新穎的選擇權交易方法，具有部位大小的資金管理。進行實驗以證明我們的方法在實際場景中的可行性和盈利能力。最後一部分提供了未來的工作。

<mark style="background-color:orange;">**核心概念：資金管理在金融交易中至關重要，本文探討如何將理論上的最佳投注比例應用於實際選擇權交易。**</mark>

* **Kelly 判準的應用**
  * 解決不完美資訊下的下注問題。
  * 應用於賭場遊戲（如 BlackJack 和德州撲克）。
  * 在股票、期貨、選擇權和貨幣交易中應用於資金分配的最佳化。
* **Kelly 判準的假設與缺點**
  * **假設遊戲可無限次重複進行**：
    * 依據大數法則，勝率需要接近理論值，但實際交易中，交易次數有限。
    * 假設遊戲可無限重複，與現實不符。實際交易次數有限，雖然有限次與無限次的回報差異可透過KL散度衡量，但仍有落差。
  * **難以應用於金融市場**：
    * Kelly假設已知準確的勝率和賠率（或盈虧分佈），但在實際金融交易中，收益/損失分佈及勝率無法確定。
    * 金融交易中，勝率和賠率（類似傳統賭博中的機率和賠率）隨時間變動。
* **Ralph Vince 的 Opt. f 方法**
  * **改進 Kelly 判準**：
    * 提出持有期收益 (HPR) 的概念，計算最佳投資比例。
    * 適用於多賠率的情況，但仍面臨實務應用挑戰。
  * **挑戰**：
    * 實際交易中的勝率和賠率分佈隨時間改變。
    * 即使設定停損/停利機制，勝率仍會隨門檻值改變。
* **實務應用挑戰**
  * 金融交易的收益/損失分佈不穩定，難以精確預測。
  * 傳統賭博的賠率分佈固定，而金融交易則具高度變動性。
  * 建議使用「半 Kelly」策略來折衷風險與收益。
* **選擇權交易的應用**
  * 選擇權交易中，收益與損失分佈在建立投資組合時即已確定。
  * 可以基於歷史數據和選擇權報價計算最佳投資比例。
  * 本研究首次嘗試將金錢管理理論應用於實際選擇權交易。
* **選擇權組合與投資策略**
  * 常見選擇權組合策略包括牛市差價 (bull spread) 和熊市差價 (bear spread)。
  * 選擇權組合可視為單一資產，具固定的收益/損失分佈。
  * 本研究使用 Ralph Vince 的方法計算選擇權組合的最佳投資比例。
* **與現代投資組合理論 (MPT) 的比較**
  * MPT 適用於不同資產的組合，使用均值與方差進行風險/收益權衡。
  * 選擇權交易中，由於收益分佈固定，偏向使用 Ralph Vince 方法。
* **未來研究方向與挑戰**
  * **關鍵問題**：市場賠率分佈的不可預測性。
  * **改進空間**：提升勝率與賠率的準確預測，以應用公式計算最佳比例。
  * 本研究展示理論方法如何應用於選擇權交易，但需進一步探索其他交易策略的實用性。
