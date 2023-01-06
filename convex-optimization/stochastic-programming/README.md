---
description: stochastic programming
---

# 隨機規劃

## 二階段固定補償隨機線性規劃(Two-Stage Stochastic Linear Programming with Fixed Recourse)

Recourse(補償、追索權)是隨機規劃中的核心概念，指的是在隨機事件發生後採取修正的能力。

在實際問題中，決策必須在所有隨機向量的實現值被觀測到之前就決定。一個補償問題(recourse problem)的解答必須是所有隨機事件的可行性，因此該解答允許補償和糾正錯誤的決定。

一個簡單的二階段固定補償線性隨機規劃$$(\mathbb{RP})$$如下：

$$\displaystyle  \begin{aligned} \min_{\mathbf{x}, \mathbf{y}(\xi)} & \mathbf{c^\top x} + \mathrm{E}_{\xi}(Q(\mathbf{x}, \xi)) \\ 	=&  \min_{\mathbf{x}} \mathbf{c^\top x} + \mathrm{E}_{\xi}\left( \min_{\mathbf{y}(\xi)} \mathbf{q}(\xi)^\top \mathbf{y}(\xi) \right) \\ \text{s.t.} & \mathbf{Ax} \preceq \mathbf{b}, ~ \mathbf{x} \succeq \mathbf{0}, \\ 		& \mathbf{Wy}(\xi) \preceq \mathbf{h}(\xi) + \mathbf{T}(\xi)\mathbf{x}, ~ \mathbf{y}(\xi) \succeq \mathbf{0}.   \end{aligned}$$

* 實數值目標函數為第一階段的成本$$\mathbf{c^\top x}$$加上第二階段的期望最佳成本$$\displaystyle Q(\mathbf{x,\xi})\equiv \min_{\mathbf{y(\xi)}} \mathbf{q(\xi)^\top y(\xi)}$$，其中$$\mathbf{\xi}$$為(情境)隨機向量，表示對未來的不確定性。
* $$\mathbf{x}$$為第一階段決策向量，其值必須在任意情境中均為可行解；而$$\mathbf{y}(\xi)$$為第二階段的決策向量，其值會隨情境$$\xi$$變動。<mark style="color:red;">其中最重要的一點是一階段決策變數</mark>$$\mathbf{x}$$<mark style="color:red;">與二階段發生的事件是完全獨立的，這被稱為不可預料屬性（Nonanticipativity Property</mark>)。
* 第一階段成本的限制為$$\displaystyle \mathbf{Ax \preceq b} ,~ \mathbf{x \succeq 0}$$，$$\mathbf{A}$$稱為資源矩陣(resource matrix)。
* 而第二階段的成本限制為$$\displaystyle \mathbf{Wy(\xi)  \preceq h(\xi) + T(\xi)x}, ~ \mathbf{y(\xi) \succeq 0}$$，其中要求補償矩陣$$\mathbf{W}$$為固定矩陣，而不會隨情境(scenario)變動。$$\mathbf{h(\xi)}$$為資源向量(resource vector)；$$\mathbf{T(\xi)}$$為技術矩陣(technical matrix)。

其核心概念為：

* 選擇決策變數$$\mathbf{x}$$來控制今天(第一期)發生的事，其成本為$$\mathbf{c^\top x}$$；
* 之後發生了(觀測到)隨機事件$$\mathbf{\xi}$$；
* 隔天(第二期)採取行動$$\mathbf{y}(\xi)$$來修正隨機事件帶來的不確定性，其成本為$$\mathbf{q(\xi)^\top y(\xi)}$$。

## 求解二階段固定補償隨機線性規劃

求解$$(\mathbb{RP})$$的常用方法是假設情境向量$$\mathbf{\xi}$$來自於已知的機率分佈，且可抽出隨機樣本$$\mathbf{\xi}_1, \mathbf{\xi}_2, \dots, \mathbf{\xi}_S$$。

因此$$(\mathbb{RP})$$可改寫為$$(\mathbb{SRP})$$如下：

$$
\displaystyle  \begin{aligned}  
\min_{\mathbf{x, y(\xi)}}  & \mathbf{c^\top x} + \frac{1}{S} \sum_{s=1}^S \mathbf{q(\xi_s)^\top y(\xi_s))} \\ 
\text{s.t.} & \mathbf{Ax} \preceq \mathbf{b}, \\
&  \mathbf{x} \succeq \mathbf{0}, \\ 		
& \mathbf{Wy}(\xi_s) \preceq \mathbf{h}(\xi_s) + \mathbf{T}(\xi_s)\mathbf{x}, ~ s=1,2,\dots, S \\
& \mathbf{y}(\xi_s) \succeq \mathbf{0},~ s=1,2,\dots, S
   \end{aligned}
$$
