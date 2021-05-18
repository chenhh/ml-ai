# 常見可微與不可微函數

## 可微分函數

### 多項式函數（polynomial function）

> $$p(x)=a_0+a_1 x+a_2 x^2+⋯+a_n x^n, ~ p \in C^{\infty} (\mathbb{R})$$

$$p^{(k)}(x) = 0, \forall k > n$$

### 偶冪函數（even power function）

> $$f:\mathbb{R} \rightarrow [0, \infty)$$, $$n \in \mathbb{N},\ f(x)=x^{2n}$$，則$$f \in C^{\infty} (\mathbb{R})$$，$$f$$為凸函數且切$$x$$軸於原點0。

* $$(x^{2n})^{(k)}=0, ~ \forall k > 2n$$
* $$(x^{2n})^{''}=2n(2n-1)x^{2n-2} > 0$$，所以為凸函數。
* $$(x^{2n})^{'}|_{x=0}=0$$，所以$$f$$切$$x$$軸於0。

### 奇冪函數（odd power function）

> • $$f:\mathbb{R} \rightarrow [0, \infty)$$, $$n \in \mathbb{N}$$, $$f(x)=x^{2n+1}$$，則$$ f \in C^\infty (\mathbb{R})$$，且$$ f$$在$$(0,\infty)$$為凸函數，在$$(−\infty,0)$$為凹函數且切$$x$$軸於0。

### 指數函數（exponential function）

> $$f: \mathbb{R} \rightarrow \mathbb{R}$$, $$ \forall x \in \mathbb{R}, f(x)=e^x$$, $$f \in C^{\infty} (\mathbb{R})$$

* $$(e^x)^{(n)}=e^x$$

### 正弦、餘弦函數

> $$f: \mathbb{R} \rightarrow \mathbb{R}$$, $$\forall x \in \mathbb{R}$$, $$f(x)=\sin x$$⁡ 或 $$f(x) = \cos ⁡x$$, 則 $$f  \in C^{\infty} (\mathbb{R})$$。

* $$f(x)=\sin ⁡x,\ \forall k \in \mathbb{N}$$ 
  * $$f^{(4k)} (x)=\sin ⁡x$$
  * $$f^{(4k+1)} (x)=\cos ⁡x$$ 
  * $$f^{(4k+2)} (x)=−\sin ⁡x$$ 
  * $$f^{(4k+3) } (x)=−\cos x$$ 
* $$f(x)=\cos ⁡x,\ \forall k \in \mathbb{N}$$ 
  * $$f^{(4k)} (x)=\cos ⁡x$$ 
  * $$f^{(4k+1) } (x)=−\sin ⁡x$$ 
  * $$f^{(4k+2)} (x)=−\cos ⁡x$$ 
  * $$f^{(4k+3)} (x)=\sin ⁡x$$

### 對數函數（logarithmic function）

> $$f:(0, \infty) \rightarrow \mathbb{R}$$, $$f(x)= \ln x$$，則$$f \in C^{\infty}(0, \infty)$$

* $$\forall n \in \mathbb{N}$$, $$f^{(n)}(x)=(-1)^{n-1}(n-1)!x^{-n}$$

### 冪函數（power function）

> $$f: (0, \infty) \rightarrow \mathbb{R}$$, $$r \in \mathbb{R}, f(x)=x^r$$則 $$f \in C^{\infty}(0, \infty)$$

## 連續不可微函數

> $$f(x)=\bigg \{ \begin{aligned} &x \sin \frac{1}{x},& x \neq 0 \\ &0,& x = 0\end{aligned}$$在$$x=0$$不可微分

$$ \displaystyle \lim_{h \rightarrow 0^+} \frac{f(h) - f(0)}{h} =  \lim_{h \rightarrow 0^+}  \sin \frac{1}{h}$$不存在。

### 奇（偶）根函數（\(odd\) even root function）

> * $$f:[0, \infty) \rightarrow [0, \infty)$$, $$\forall n \in \mathbb{N}, f(x)=x^{\frac{1}{2n}}$$在$$x=0$$不可微分。
> * $$f:[0, \infty) \rightarrow [0, \infty)$$, $$\forall n \in \mathbb{N}, f(x)=x^{\frac{1}{2n+1}}$$在$$x=0$$不可微分。

* $$\displaystyle \lim_{x \rightarrow 0^+ }⁡ \frac{f(x)−f(0)}{x} = \lim_{x→0^+ }\frac{x^{1/2n}}{x}= \lim_{x→0^+}⁡x^{−1+1/2n}=\infty $$因此在$$x=0$$不可微。
* $$\displaystyle \lim_{x \rightarrow 0^+ }⁡ \frac{f(x)−f(0)}{x} = \lim_{x→0^+ }\frac{x^{1/(2n+1)}}{x}= \lim_{x→0^+}⁡x^{−1+1/(2n+1)}=\infty $$因此在$$x=0$$不可微。

### 絕對值（根）函數

> * $$f(x)=|x|$$在$$x=0$$連續但不可微分。
> * $$f(x)=|x|^{1/n}, \ n >1$$在$$x=0$$連續但不可微分。

* $$\lim_{h \rightarrow 0^− }⁡\frac{f(h)−f(0)}{h}=\lim_{h \rightarrow 0^− }\frac{−h}{h}=−1 $$。
* $$\lim_{h \rightarrow 0^+ } \frac{f(h)−f(0)}{h}= \lim_{h \rightarrow 0^+ }⁡\frac{h}{h}=1$$ 左右微分不相等，因此在$$x=0$$不可微分。
* $$\lim_{x \rightarrow 0^+ }⁡\frac{f(x)−f(0)}{x}= \lim_{x \rightarrow 0^+ }⁡ x^{−1+1/n} = \infty$$, 因此在$$x=0$$不可微  分。

