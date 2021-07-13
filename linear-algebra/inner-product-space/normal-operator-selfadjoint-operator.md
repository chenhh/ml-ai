# 正規算子、自伴算子\(normal operator, self-adjoint operator\)

##  正規算子、正規矩陣\(normal operator, normal matrix\)

> * 線性轉換$$ T \in L(V,V)$$，且$$T^∗$$為伴隨算子（$$\langle T(x),y \rangle=\langle x, T^∗ (y)\rangle, ~\forall x,y \in V$$），若$$T^∗ T=TT^∗$$，則稱$$T$$為正規算子。
> * $$A \in F^{N \times N}，若A^\mathrm{H} A=AA^\mathrm{H}$$，則稱$$A$$為正規矩陣。
>
> 在[最小平方解](least-square-solution.md#jian-jie)有討論過正規矩陣的性質。

### 正規算子特徵向量空間特性\(必要條件\)

> 線性轉換$$T \in L(V,V)$$，$$T$$為正規算子則：
>
> 1. （轉換後長度相同） $$\|T(v)\|=\|T^∗ (v)\|,  ~\forall v \in V$$。
> 2. $$\forall c \in F$$， $$T−cI$$為正規算子。
> 3. （特徵向量不變）若$$\lambda$$為$$T$$的特徵根，且$$v$$為$$T$$相對於$$\lambda$$的特徵向量，則$$v$$為$$T^∗$$ 相對$$\overline{\lambda}$$的特徵向量。
> 4. （相異特徵根之特徵向量必正交）若$$\lambda_1,\lambda_2$$ 為$$T$$的兩個相異特徵根，且$$v_1,v_2$$ 分別為$$T$$相對於$$\lambda_1,\lambda_2$$ 的特徵向量，則$$v_1 \bot v_2$$。

> 矩陣$$A \in F^{N \times N}$$ 為正規矩陣時可得：
>
> 1. $$\|Ax\|=|A^\mathrm{H} x\|,~\forall x \in F^{N \times 1}$$   。
> 2. $$\forall c \in F, ~A−cI$$為正規矩陣。
> 3. 若$$\lambda$$為$$A$$的特徵根，且$$v$$為$$A$$相對於$$\lambda$$的特徵向量，則$$v$$為$$A^\mathrm{H}$$ 相對$$\overline{\lambda}$$的特徵向量。
> 4. 若$$\lambda_1,\lambda_2$$ 為$$A$$的兩個相異特徵根，且$$v_1,v_2$$ 分別為$$T$$相對於$$\lambda_1,\lambda_2$$ 的特徵向量，則$$v_1 \bot v_2$$。



