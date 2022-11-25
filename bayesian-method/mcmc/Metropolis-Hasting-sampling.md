# Metropolis-Hasting抽樣

## Baye's update
$$
\displaystyle \mathrm{P}(\theta|x) 
=
\frac{
\mathrm{P}(x|\theta) \mathrm{P}(\theta)}{
\mathrm{P}(x)
}
= \frac{
\mathrm{P}(x|\theta) \mathrm{P}(\theta)}{
\int \mathrm{P}(x|\theta) \mathrm{P}(\theta)d\theta
}
$$

計算分母的$$ \mathrm{P}(x)$$需要使用積分，只有在特殊情形下如共軛分佈時才有解析解。

因為$$ \mathrm{P}(x)$$為常數，上式一般可改寫為後驗分佈(posterior)正比於似然率(likelihood)乘以先驗分佈(prior)如下：
$$
\displaystyle
\mathrm{P}(\theta|x) \propto \mathrm{P}(x|\theta) \mathrm{P}(\theta)
$$

Metropolis演算法為只使用$$ \mathrm{P}(x|\theta)$$與$$ \mathrm{P}(\theta)$$，不必計算積分，
即可得到$$\mathrm{P}(\theta|x)$$的樣本。


特點：用一個多元常態分配隨機遊走，不需要對分佈本身有太多瞭解，高維空間時有效，分佈本身不需要積分=1，基本只需要保證f(x)在-∞和+∞處=0，0\<f(x)\<upper bound就行了。

問題：隨機遊走的效率仍然不夠高。

```python
def binormal_draw(xprev,beta=1):
    mean = [0, 0]
    cov = [[beta**2,0],[0,(1.5*beta)**2]]
    binormal = scipy.stats.multivariate_normal(mean,cov)
    return xprev + binormal.rvs()

def metropolis(F, qdraw, nsamp, x_init, burnin, thinning=2, beta=1):
    samples=np.empty((nsamp,2))
    x_prev = x_init
    accepted = 0
    j = 0
    for i in range((nsamp+burnin)*thinning):
        x_star = qdraw(x_prev, beta)
        logp_star = np.log(F(x_star[0], x_star[1]))
        logp_prev = np.log(F(x_prev[0], x_prev[1]))
        logpdfratio_p = logp_star-logp_prev
        u = np.random.uniform()
        if np.log(u) <= logpdfratio_p:
            x_prev = x_star
            if i >= burnin*thinning and i%thinning == 0:
                samples[j] = x_star
                j += 1
                accepted += 1
        else:#we always get a sample
            if i >= burnin*thinning and i%thinning == 0:
                samples[j]= x_prev
                j += 1
    return samples, acceptedpy
```

