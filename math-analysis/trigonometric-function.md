---
description: Trigonometric Function
---

# 三角函數

## 徑度與弧度（radius and arc）

* 徑度\(radians\)等於弧長\(arc\)除以半徑\(radius\)  ，$$\theta = \frac{s}{r}$$

![&#x5F91;&#x5EA6;&#x8207;&#x5F27;&#x5EA6;](../.gitbook/assets/radius_arc-min.png)

### 角度與徑度的對應關係

* 徑度$$\pi$$等於角度$$180\degree$$。
* 一正圓內，角度$$0\degree \sim 180 \degree$$是以逆時鐘方向看，對應徑度$$0 \sim \pi$$。而角度$$0\degree \sim -180 \degree$$是以順時鐘方向看，對應徑度$$0 \sim -\pi$$。

![&#x6B63;&#x503C;&#x8207;&#x8CA0;&#x503C;&#x7684;&#x5F91;&#x5EA6;](../.gitbook/assets/angle-min.png)

![&#x8D85;&#x904E;360&#x5EA6;&#x7684;&#x89D2;&#x5EA6;&#xFF08;&#x5F91;&#x5EA6;&#xFF09;](../.gitbook/assets/angle_rad_-min.png)

## 三角函數

* hypotenuse: 斜邊，opposite: 對邊，adjacent: 鄰邊。

![&#x4E09;&#x89D2;&#x51FD;&#x6578;&#x7684;&#x5B9A;&#x7FA9;](../.gitbook/assets/tri-func-min.png)

* $$\sin \theta = \frac{y}{r}$$, $$\cos \theta = \frac{x}{r}$$
* $$\tan \theta = \frac{y}{x}$$, $$\cot \theta = \frac{x}{y}$$
* $$\sec \theta = \frac{r}{x}$$, $$csc \theta = \frac{r}{y}$$

可得關係：

* $$\tan \theta =  \frac{\sin \theta} {\cos \theta}$$, $$\cot \theta = \frac{1}{\tan \theta} = \frac{\cos \theta} {\sin \theta}$$
* $$\sec \theta = \frac{1}{\cos \theta}$$, $$\csc \theta = \frac{1}{\sin \theta}$$

![&#x4E09;&#x89D2;&#x51FD;&#x6578;&#x8D85;&#x904E;90&#x5EA6;&#x6642;&#x7684;&#x5B9A;&#x7FA9;](../.gitbook/assets/tri-func_over-angle-min.png)



![&#x7279;&#x6B8A;&#x89D2;&#x5EA6;&#xFF08;30&#x3001;45&#x3001;60&#x5EA6;&#xFF09;&#x7684;&#x4E09;&#x89D2;&#x51FD;&#x6578;](../.gitbook/assets/spec_tri-func-min.png)

![&#x7279;&#x6B8A;&#x89D2;&#x5EA6;&#x7684;&#x4E09;&#x89D2;&#x51FD;&#x6578;&#x503C;](../.gitbook/assets/tri-func-spec-value-min.png)

## ASTC規則

ASTC="All Student Take Calculus"，說明四個象限中，三角函數的正負值。

* 第一象限內任何一個角的四種三角函數值\(all\)都是「+」；
* 第二象限內只有正弦\(sine\)是「+」，其餘全部是「-」；
* 第三象限內只有正切\(tan\)是「+」，其餘全部是「-」；
* 第四象限內只有餘弦\(cos\)是「+」，其餘全部是「-」。



![ASTC&#x898F;&#x5247;](../.gitbook/assets/astc-rule-in-trigonometry-min.png)

## 週期函數（periodic function）

> $$f(x)$$稱為週期函數若存在$$p>0$$滿足$$f(x+p)=f(x), ~ \forall x$$，則滿足此最條件的最小$$p$$值稱為函數$$f$$的週期（period）。

### 三角函數的週期

* 週期為$$\pi$$：
  * $$\tan (x + \pi) = \tan(x)$$
  * $$\cot(x + \pi ) =\cot (x)$$
* 週期為$$2\pi$$：
  * $$\sin(x+2\pi) = \sin(x)$$
  * $$\cos(x + 2\pi) = \cos(x)$$
  * $$\sec(x+2\pi) = \sec(x)$$
  * $$\csc(x + 2\pi) = \csc(x)$$
* 奇函數：\($$f(-x)=-f(x)$$，對稱於原點）
  * $$\sin(-x) = - \sin(x)$$
  * $$\tan(-x) = -\tan(x)$$
  * $$\csc(-x) = - \csc(x)$$
  * $$\cot(-x) =  -\cot(x)$$
* 偶函數：（$$f(-x) = f(x)$$，對稱於$$y$$軸）

  * $$\cos(-x) = \cos(x)$$
  * $$\sec(-x) = \sec(x)$$

![&#x4E09;&#x89D2;&#x51FD;&#x6578;&#x7684;&#x9031;&#x671F;](../.gitbook/assets/tri-period-plot-min.png)

## 三角函數的等式

> $$\sin^2(x)+\cos^2(x)=1$$

![&#x659C;&#x908A;&#x70BA;1&#xFF0C;&#x9130;&#x908A;&#x70BA;&#x9918;&#x5F26;&#xFF0C;&#x5C0D;&#x908A;&#x70BA;&#x6B63;&#x5F26;](../.gitbook/assets/sin2x-cos2x-eq1-plot-min.png)

> $$1+ \tan^2(x)=\sec^2(x)$$

* $$\tan(x)=\frac{\sin(x)}{\cos(x)}$$，$$\sec(x)=\frac{1}{\cos(x)}$$
* $$\begin{aligned} 1+\tan^2(x) & = 1+ \frac{\sin^2(x)}{\cos^2(x)} \\ & = \frac{\cos^2(x)+\sin^2(x)}{\cos^2(x)} \\ &= \frac{1}{\cos^2(x)}\\ &=\sec^2(x) \end{aligned}$$\(QED\)

> $$1+ \cot^2(x)=\csc^2(x)$$

