---
description: 平均數-變異數模型, mean-variance model
---

# 均異模型(MV-model)

## 數學模型

<mark style="color:red;">MV模型為二次規劃</mark>

$$\displaystyle \begin{aligned} \min_{\mathbf{w}} ~&~ {\color{blue}\lambda} \sum_{i=1}^N \sum_{j=1}^N {\color{red}w_i w_j} \sigma_{ij} - {\color{blue}(1-\lambda)} \sum_{i=1}^N {\color{red} w_i} u_i \\ s.t. ~&~ \sum_{i=1}^N w_i = 1  \end{aligned}$$

矩陣型：

$$\displaystyle \begin{aligned}   \min_{\mathbf{w}} ~&~ {\color{blue}\lambda} \mathbf{w}^\top \mathbf{\Sigma}  \mathbf{w} - {\color{blue}(1-\lambda)} \mathbf{w}^\top \mathbf{u}  \\   s.t. ~&~ \mathbf{w}^\top \mathbf{1} = 1  \end{aligned}$$

* 決策變數為配置在資產的權重向量$$\mathbf{w}=(w_1,w_2, \dots, w_N)$$。
* $$0 \leq \lambda \leq 1$$是使用者決定的風險偏好，$$\lambda=0$$為最大化報酬，$$\lambda=1$$為最小化波動率。
* $$\sigma_{ij}$$為第$$i$$個資產與第$$j$$個資產報酬的標準差。
* $$u_i$$為第$$i$$個資產的期望報酬。
