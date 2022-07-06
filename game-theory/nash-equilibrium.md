---
description: Nash equilibrium
---

# 納許均衡

John Nash提出「Nash equilibrium」的概念並在1994年得到諾貝爾經濟學的殊榮。Nash均衡是非合作賽局（Non-cooperative Game） 的求解觀念。

不同玩家可以互相合作以獲得利益的塞局，稱為合作賽局（cooperative game）； 反之沒有任何協議可能性的賽局稱為非合作賽局。一般討論的多是非合作賽局。

<mark style="color:red;">賽局中的均衡是一種現象中的群體狀態，本質上是由個人行為決定的</mark>。影響賽局中玩家行為的基本屬性是<mark style="color:red;">資訊和理性</mark>。

Von-Neumann的minmax定理首次指出，一般來說，兩人零和賽局總是有最大和最小的均衡。納許均衡是非合作賽局中最重要的求解概念，納許均衡是非合作性、完全資訊靜態賽局中最重要的解的概念。事實上，它是一個玩家同時以策略形式做出合理預測所需的最小值。

> 定義：單純策略納許均衡
>
> 給定一靜態賽局$$\Gamma=(\mathcal{N}, (\mathcal{A}_i)_{i \in \mathcal{N}}, (u_i)_{i \in \mathcal{N}})$$。
>
> 純策略的納許均衡為一純策略方案$$\mathbf{a}^* \in \mathcal{A}$$，其中所有玩家$$i$$的採取特定的行動$$a_i^{*}$$的報酬均高於採取其它行動的報酬，即$$u_i(a_i^{*}, \mathbf{a}_{-i}^*) \geq u_i(a_i, \mathbf{a}_{-i}^*)$$。

> 定義：混合策略的納許均衡
>
> 混合策略的納許均衡為一混合策略方案$$\mathbf{s}^{*} \in \prod_{i \in \mathcal{N}} \Delta(\mathcal{A}_i)$$，其中所有玩家採取特定的混合策略$$\mathbf{s}_i^{*}$$的報酬率$$u_i(\mathbf{s}_i^{*}, \mathbf{s}_{-i}^{*}) \geq u_i(\mathbf{s}_i, \mathbf{s}_{-i}^{*})$$

納許均衡為理性決策者提供了可能的賽局結果的一致性預測，也就是理性決策者的最優決策結果。可見，理性預測--均衡構成了賽局理論的基本模型，是賽局理論的精髓。
