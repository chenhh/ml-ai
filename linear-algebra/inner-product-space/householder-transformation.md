# Householder轉換\(transformation\)

## Householder matrix

> $$ 0 \neq v \in \mathbb{R}^{N \times 1}$$，$$H=I - \frac{2}{v^\top v} vv^\top \in \mathbb{R}^{ \times N}$$為相對於$$v$$的Householder matrix或基本鏡射算子（elementart reflector）。
>
> 當$$\|v\|=1$$時，$$H=I-2vv^\top \in \mathbb{R}^{N \times N}$$

給定向量$$v$$，可得正交於向量$$v$$的平面$$v^\bot$$，Householder轉換即求出向量$$x$$鏡射於平面$$v^\bot$$ 的向量$$y$$。

* 令向量$$y$$為$$x$$相對於平面鏡射後的結果，則$$y−x$$正交於平面。
* 因此$$y−x$$與向量$$v$$平行，可得$$y−x=cv, ~c \in \mathbb{R}$$。
* 令$$x$$投影在平面上的向量$$\mathrm{proj}_{v^\bot} (x)=x+\frac{1}{2} (y−x)=x+\frac{1}{2} cv$$
* 因$$\mathrm{proj}_{v^\bot} (x)$$與$$v$$正交，可得$$\langle \mathrm{proj}_{v^\bot} (x),v \rangle =v^\top (x+1/2 cv)=0$$
* 所以$$v^\top x+1/2 cv^\top v=0$$，$$c=\frac{−2w^\top x}{v^\top v}$$
* 得$$y=x+cw=x+\frac{−2v\top x}{v^\top v} v=x−\frac{2}{v^\top v} vv^\top x=(I−\frac{2}{v^\top v} vv^\top )x=Hx$$\(QED\)



![Houserholder&#x8F49;&#x63DB;](../../.gitbook/assets/householder_transform-min.png)

![Householder&#x8F49;&#x63DB;](../../.gitbook/assets/householder_transform2-min.png)

