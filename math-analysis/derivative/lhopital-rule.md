# L'Hopital法則

## 簡介

當計算兩個函數的比例$$\frac{f(x)}{g(x)}$$，當$$x$$趨近某一個常數（$$x\rightarrow a$$）後，可能會遇到結果為$$\frac{0}{0}$$或是$$\frac{\infty}{\infty}$$時，可用L'Hopital法則，將分子與分母微分後（假設微分存在），再看比值$$\frac{f^{'}(x)}{g^{'}(x)}$$。如果仍然無法求得，則再微分下去。

## L'Hopital rule

> 若$$\lim_{x \rightarrow a} f(x) = 0 \text{ or } \infty$$及 $$\lim_{x \rightarrow a} g(x) = 0 \text{ or } \infty$$，則 $$\displaystyle \lim_{x \rightarrow a} \frac{f(x)}{g(x)}=\lim_{x \rightarrow a} \frac{f^{'}(x)}{g^{'}(x)}=\frac{A}{B}$$
>
> 此處 $$\lim_{x \rightarrow a} f^{'}(x)=A$$存在， $$\lim_{x \rightarrow a} g^{'}(x)=B$$存在。

