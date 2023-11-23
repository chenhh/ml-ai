# Hausdorff空間

## 簡介

歐式空間中，單點集$$\{x_0\}$$為閉集，且對於收斂序列$$\{x_n\}_{n \in \mathbb{N}}$$只會收斂到唯一的點$$x$$。

但這兩個性質在任意拓樸空間中不一定成立，即單點集不一定是閉集與收斂序列收斂到多點的拓樸存在。但具備有些性質的拓樸通常被視為非正常拓樸相當少見。<mark style="color:blue;">為了避開這些少見的拓樸(如同實數上避開不可測集如Cantor集而建立Borel集)則需附加條件，由Felix Hausdorff給出，稱為Hausdorff空間</mark>。數學上重要的空間大多是Hausdorff空間。

<mark style="background-color:red;">Hausdorff空間中，任意有限集為閉集合且收斂序列只會收斂到一點</mark>。

Hausdorff條件常被加到拓樸空間的附加條件，即不處理非Hausdorff空間的拓樸空間。

## Hausdorff空間

> Hausdorff條件：如果對於拓樸空間$$X$$中相異兩點$$x_1, x_2$$，分別存在各自的鄰域$$U_1, U_2$$使得$$U_1 \cap U_2 =\emptyset$$，則稱$$X$$為Hausdorff空間。

### Hausdorff空間中任意有限集為閉集合

> 有限點集為閉集合的條件(T1公理)比Hausdorff條件更弱。
>
> 例如實數上有限補拓樸不是Hausdorffn空間，但此空間中有限點為閉集。

只要証明單點集$$\{x_0\}$$為閉集合。

令$$x \in X, x \neq x_0$$，由Hausdorff空間定義得存在相異鄰域$$U, V \ni U \cap V=\emptyset$$，因此$$U \cap \{x_0\} =\emptyset$$，即$$x$$不屬於$$\{x_0\}$$的閉包，因此$$\{x_0\}$$的閉包就是$$\{x_0\}$$，所以$$\{x_0\}$$為閉集。

### Hausdorff空間中的序列最收斂到一點

假設$$X$$中序列$$\{x_n\}_{n \in \mathbb{N}}$$收斂到$$x$$。

對於$$y \neq x$$，記$$U_y, U_x, ~ U_y \cap U_x = \emptyset$$分別為其不相交的鄰域。

由於$$U_x$$中，包含了$$\{x_n\}_{n \geq n_0}$$$$x_$$無限個元素，只有$$\{x_n\}_{n < n_0}$$有限個不在$$U_x$$中，因此$$U_y$$最多包含了有限個$$\{x_n\}$$的元素，因此$$\{x_n\}$$不會收斂到$$y$$。

### 具有有序拓樸的全序集為Hausdorff空間，兩個Hausdorff空間的積是Hausdorff空間，Hausdorff空間的子空間是Hausdorff空間
