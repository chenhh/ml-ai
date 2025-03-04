# No-U-Turn Sampler

## 簡介

Hamiltonian採樣器在利用梯度、仿造哈密頓力學系統構造canonical distribution的同時，放棄了MCMC的Markov Chain。但HMC的問題是，需要手動設定每次採樣需要的迭代次數（iteration number for leapfrog algorithm），所以有時間步長、迭代次數、速度的分佈、初始點的分佈這幾個要設定。而NUTS首先向解決的是動態設定迭代次數的問題。

## 參考資料

* [\[原始論文\] Hoffman, Matthew D., and Andrew Gelman. "The No-U-Turn sampler: adaptively setting path lengths in Hamiltonian Monte Carlo." pp. 1593-1623, Journal Machine Learning Research, Vol. 15, 2014](https://www.jmlr.org/papers/volume15/hoffman14a/hoffman14a.pdf).
* [\[知乎\]為什麼要用NUTS採樣器（No-U-turn Sampler），以及NUTS的演算法分析](https://zhuanlan.zhihu.com/p/59473302)
* \[github] [https://github.com/mfouesneau/NUTS](https://github.com/mfouesneau/NUTS)
* [https://www.bilibili.com/video/BV1uV4y1U7Rr/](https://www.bilibili.com/video/BV1uV4y1U7Rr/)
* [https://stats.stackexchange.com/questions/311813/can-somebody-explain-to-me-nuts-in-english](https://stats.stackexchange.com/questions/311813/can-somebody-explain-to-me-nuts-in-english)
* [https://gsejournal.biomedcentral.com/articles/10.1186/s12711-019-0515-1](https://gsejournal.biomedcentral.com/articles/10.1186/s12711-019-0515-1)

