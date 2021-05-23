# Riemann-Stieltjes積分

## 簡介

令$$ \frac{d}{dx}F(x) = f(x)$$，移項得 $$dF(x)=f(x)dx$$。

因此對$$f(x)$$積分可得 $$\int_a^b f(x)dx  = \int_a^b dF(x)=F(x)|_a^b=F(b)-F(a)$$。

只要函數的微分存在，$$dF(x)$$可用$$f(x)dx$$表示。

## 分部積分（integration by parts）

> $$\int u(x) dv(x) = u(x)v(x) - \int v(x)du(x)$$

因為$$\frac{d}{dx}uv = u^{'}v+uv^{'}$$

兩邊積分得 $$uv=\int vdu + \int u dv$$ \(QED\)





