# Neyman–Pearson引理

## 簡介

一個統計假是否可靠，拒絕它的唯一正當理由是，存在著另一個對立假設，能以更大的機率來解釋觀察到的事件。

<mark style="color:red;">簡單地說，Neyman-Pearson引理(lemma)就是對於單一引數分佈的兩點似然比檢定之最佳檢定</mark>。

假設有一個檢定方法比似然比檢定更好，即在使用這個檢定方法時，犯類型I錯誤的機率$$\alpha=\mathrm{P}(\text{reject } H_0~|~ H_0 \text{ is true} )$$和使用似然比檢定時一樣或更低，而同時我們犯類型II錯誤的機率$$\beta = \mathrm{P}(\text{not reject } H_0 ~|~ H_0 \text{ is false})$$也更低。

## 假設設定步驟

針對未知參數$$\theta$$的統計檢定步驗如下：

1. 簡單虛無假設$$H_0$$，如$$H_0: \theta=\theta_0$$
2. 簡單對立假設$$H_a$$，如$$H_a: \theta=\theta_a$$
3. 確定檢定統計量$$T$$為樣本$$X_1,\dots,X_n$$的函數
4. 確定拒絕域RR(reject region)，可直接指定或由$$P$$值間接指定。當$$T \in RR$$時，則拒虛無假設$$H_0$$。

而類型1與類型2錯誤，可用拒絕域寫為：

* $$\alpha=\mathrm{P}(\text{reject } H_0~|~ H_0 \text{ is true} )  = \mathrm{P}(T \in RR ~|~ \theta=\theta_0 )$$
* $$\beta = \mathrm{P}(\text{not reject } H_0 | H_0 \text{ is false}) = \mathrm{P}(T \notin RR~|~ \theta = \theta_a)$$

在假設檢定時，通常先指定$$\alpha$$決定$$RR$$：

* 且在給定樣本大小$$n$$固定時(虛無假設的分佈形狀固定)，當$$\alpha$$上升則$$\beta$$下降，反之當$$\alpha$$下降則$$\beta$$上升，即無法同時降低兩類型錯誤。
* 如果使用更大的樣本數時(虛無假設的分佈會變的更徒峭)，可同時降低$$\alpha$$與$$\beta$$，因為更大的樣本數可降低統計量的變異數(中央極限定理)，得到更陡峭的分佈。

## 檢定力(power of a test)

> 定義：檢定力
>
> $$power(\theta)\equiv \mathrm{P}(T \in RR ~|~ \theta)$$\
> 即真實參數為$$\theta$$時，拒絕虛無假設$$H_0$$的機率。

由定義得

* 在$$\theta=\theta_0$$時，$$power(\theta_0)=\mathrm{P}(T \in RR ~|~ \theta=\theta_0)=\alpha$$。
* 在$$\theta=\theta_a$$時，$$\begin{aligned} power(\theta_a) & = \mathrm{P}(T \in RR ~|~ \theta=\theta_a)\\ & =  1 -  \mathrm{P}(T \notin RR ~|~ \theta=\theta_a)\\ & =  1-\beta  \end{aligned}$$<mark style="color:red;"></mark>

<mark style="color:red;">因此檢定力為假設檢定可以正確拒絕虛無假設的能力</mark>。

## 假設檢定

檢定步驟一般如下：

* 事先選定一個較小的型1錯誤機率$$\alpha$$。
* 針對對立假設$$H_a$$中的$$\theta_a$$，求拒絕域$$RR$$滿足型2錯誤機率$$\beta(\theta_a)$$最小化，或者說滿足最大化檢定力$$power(\theta_a)$$。

###
