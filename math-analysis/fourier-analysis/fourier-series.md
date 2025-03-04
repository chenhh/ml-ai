---
description: Fourier series
---

# 傅立葉級數

## 傅立葉級數

給定訊號函數$$f(x)\in L^2([-\pi, \pi])$$， 令$$\displaystyle f(x)=a_0 + \sum_{k=1}^\infty a_k \cos(kx) + b_k \sin(kx)$$

由$$L^2([-\pi,\pi])$$定義的內積可得：

* $$\displaystyle \frac{1}{\pi}\int_{-\pi}^\pi \cos(nx) \cos(kx) dx =  \left\{ \begin{aligned} & 1, ~ \text{ if } n=k=1, \\ & 2, ~ \text{ if } n=k=0, \\ & 0, ~ \text{ otherwise} \end{aligned} \right.$$
* $$\displaystyle \frac{1}{\pi}\int_{-\pi}^\pi \sin(nx) \sin(kx) dx =  \left\{ \begin{aligned} & 1, ~ \text{ if } n=k \geq 1, \\ & 0, ~ \text{ otherwise} \end{aligned} \right.$$
* $$\displaystyle \frac{1}{\pi}\int_{-\pi}^\pi \cos(nx) \sin(kx) dx = 0, \forall n, k$$

因此可得$$L^2([-\pi, \pi])$$的單範正交集$$\displaystyle \left\{ \dots,  \frac{\cos(2x)}{\sqrt{\pi}}, \frac{\cos(x)}{\sqrt{\pi}}, \frac{1}{\sqrt{2\pi}} \frac{\sin(x)}{\sqrt{\pi}}, \frac{\sin(2x)}{\sqrt{\pi}} \dots  \right\}$$

由內積正交投影性質可得係數$$a_n = \langle f, e_n \rangle$$，因此：

* $$\displaystyle a_0 = \frac{1}{2\pi}\int_{-\pi}^\pi f(x) dx$$
* $$\displaystyle a_k = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos(kx) dx$$
* $$\displaystyle b_k = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin(kx) dx$$
