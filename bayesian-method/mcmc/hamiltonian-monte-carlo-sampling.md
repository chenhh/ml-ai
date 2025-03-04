# Hamiltonian Monte Carlo(HMC)抽樣

直觀理解原理：把MCMC的樣本隨機遊走改成在一個勢場中具有動能的質點，勢場由分佈函數f(x)決定，初始動能隨機給定，這個質點在運動時間t後的位置記錄下來，並且作為下次採樣的初始點。

相比MH的優點：更新樣本點的時候使用了梯度，所以對複雜分佈採樣比隨機試的速度要快。

```python
def HMC(F, u0, n_iter, N_iter, h=0.01): 

# part 1: 初始化一個orbit的變數，第一行是初始點u0的坐標
    orbit = torch.zeros((n_iter+1, 2))
    orbit[0] = u0.detach()
    u = orbit[0].unsqueeze(0)
    shape = u.size()

# part 2: 循環n_iter次，每次初始化一個v0和u0，然後讓leapfrog走N_iter次，每次時長h默認=0.01
    for k in tqdm(range(n_iter)):
        v0 = torch.randn(size=u0.shape)
        u0 = torch.randn(size=u0.shape)*3
        u, v = leapfrog(F, u0, v0, h, N_iter,shape)
        u0 = orbit[k]
        a = float(ratio(F, u0, v0, u, v, shape))
        r = np.random.rand()
        if r < a:
            orbit[k+1] = u
        else:
            orbit[k+1] = u0
    return orbit #[10:, :]

# part 3: leapfrog演算法，此外還有velocity verlet等等都可以嘗試，但不要用euler
def leapfrog(F, u, v, h, N_iter,shape):
    v = v - h/2 * grad(F, u)
    for i in range(N_iter-1):
        u = u + h * v
        v = v - h * grad(F, u)
    u = u + h * v
    v = v - h/2 * grad(F, u)
    return u, v

# part 4: 對函數F求梯度
def grad(F, u):
    u = u.detach()
    if u.requires_grad == False:
        u = u.requires_grad_()
    output = -torch.log(F(u))
    output.backward()
    ugrad = u.grad.squeeze(0)
    u = u.squeeze(0)
    return ugrad

# part 5: 細節處理
def unsqueeze(tensor, shape):
    if len(list(tensor.size())) < len(list(shape)):
        tensor = tensor.unsqueeze(0)
    return tensor

# part 6: 由於leapfrog計算結果仍然不是絕對的穩定，所以接受機率是min{運行前後總能量的比值,1}
#，大多數情況下都≈1
def ratio(F, u0, v0, u, v, shape):
    u0 = unsqueeze(u0, shape)
    u = unsqueeze(u, shape)
    v0 = unsqueeze(v0, shape)
    v = unsqueeze(v, shape)

    w0 = - torch.log(F(u0)) + 0.5*torch.mm(v0, torch.t(v0))
    w1 = - torch.log(F(u)) + 0.5*torch.mm(v, torch.t(v))
    return torch.exp(w0-w1)py
```

## 參考資料

* [Wiki: HMC](https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo)
* [Hamiltonian Monte Carlo explained](https://arogozhnikov.github.io/2016/12/19/markov_chain_monte_carlo.html)
* [MCMC: Hamiltonian Monte Carlo (a.k.a. Hybrid Monte Carlo)](https://theclevermachine.wordpress.com/2012/11/18/mcmc-hamiltonian-monte-carlo-a-k-a-hybrid-monte-carlo/)
* [\[知乎\] 為什麼要用哈密頓採樣器（Hamiltonian Monte Carlo），以及如何自己寫一個](https://zhuanlan.zhihu.com/p/56568006)
