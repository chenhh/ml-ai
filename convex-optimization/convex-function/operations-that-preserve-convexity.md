# 保凸運算

## 簡介

檢驗函數是否為凸函數有以下幾種常見方法：

1. 直接由定義檢驗 $$\forall x, y \in \mathrm{dom}f, 0 \leq c \leq 1$$， $$f(cx+(1-c)y) \leq cf(x) + (1-c)y$$。
2. 對於二次可微的函數，確認$$\nabla^2 f(x) \succeq 0$$。
3. 檢驗函數是否由以下保凸運算得到。
   * 非負加權求和(non-negative weighted sum)
   * 複合仿射映射(composition with affine function)
   * 逐點最大和逐點上確界(pointwise maximum and supremum)
   * 複合(composition)
   * 最小化(minimization)
   * 透視函數(prespective)
