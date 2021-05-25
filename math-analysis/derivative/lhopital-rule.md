# L'Hopital法則

## 簡介

當計算兩個函數的比例$$\frac{f(x)}{g(x)}$$，當$$x$$趨近某一個常數（$$x\rightarrow a$$）後，可能會遇到結果為不定型$$\frac{0}{0}$$或是$$\frac{\infty}{\infty}$$時，可用L'Hopital法則，將分子與分母微分後（假設微分存在），再看比值$$\frac{f^{'}(x)}{g^{'}(x)}$$。如果仍然無法求得，則再微分下去。

## L'Hopital rule

> 分成兩種不定型$$\frac{0}{0}$$與$$\frac{\infty}{\infty}$$：
>
> * 當$$x=a$$時，$$\frac{f(a)}{g(a)}=\frac{0}{0}$$不定型，$$f^{'}(a), g^{'}(a)$$存在，且$$\frac{f^{'}(a)}{g^{'}(a)}$$非不定型，則 $$\displaystyle \lim_{x \rightarrow a} \frac{f(x)}{g(x)}=\lim_{x \rightarrow a} \frac{f^{'}(x)}{g^{'}(x)}$$
> * 當$$x=a$$時，$$\frac{f(a)}{g(a)}=\frac{\infty}{\infty}$$不定型，$$f^{'}(a), g^{'}(a)$$存在，且$$\frac{f^{'}(a)}{g^{'}(a)}$$非不定型，則 $$\displaystyle \lim_{x \rightarrow a} \frac{f(x)}{g(x)}=\lim_{x \rightarrow a} \frac{f^{'}(x)}{g^{'}(x)}$$
>
> 註：$$\frac{0}{\infty} =0 $$，但是$$0 \times \infty$$無法判定。

\[[證明](https://www.cnblogs.com/iMath/p/10461442.html)\]

### 範例

* $$f(x)=x^2 - 1$$, $$g(x)=x^3 -1$$
  * $$\displaystyle \lim_{x \rightarrow 1} \frac{x^2-1}{x^3-1} = \lim_{x \rightarrow 1} \frac{2x}{3x^2}=\lim_{x \rightarrow 1}\frac{2}{3x}=\frac{2}{3}$$
* $$f(x)=\ln x$$, $$g(x)=e^x$$
  * $$\displaystyle \lim_{x \rightarrow \infty} \frac{\ln x}{e^x} = \lim_{x \rightarrow \infty} \frac{1/x}{e^x}=\frac{0}{\infty}=0$$

