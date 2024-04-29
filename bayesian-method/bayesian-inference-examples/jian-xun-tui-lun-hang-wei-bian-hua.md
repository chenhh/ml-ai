# 簡訊推論行為變化

## 簡介

你得到了系統中一個使用者每天的簡訊條數資料，你很好奇這個使用者的簡訊使用行為是否隨著時間有023所改變，不管是循序漸進地還是突然地變化



## PyMC context

PyMC 中，我們通常在 Model 物件的上下文中處理模型中所需的所有變數。在給定 Model 上下文中建立的任何變數都會自動指派給該模型。如果您嘗試在模型上下文之外定義變數，您將收到錯誤。

透過使用 with 和我們已經建立的模型物件的名稱，我們可以繼續在同一模型的上下文中工作。一旦定義了相同的變數，我們就可以在模型上下文之外檢查它們，但要定義模型能夠識別的更多變數，它們必須位於上下文中。

當您在模型中新增變數時，PyMC 通常會向您提供有關轉換的通知。這些轉換由 PyMC 在內部完成，以修改變數取樣的空間（當我們實際對模型進行取樣時）。

```python
import pymc as pm

# 透過with 建立模型物件
with pm.Model() as model:
    # 分配給模型的每個變數都將使用自己的名稱進行定義
    parameter = pm.Exponential("poisson_param", 1.0, initval=rng.exponential(1))
    data_generator = pm.Poisson("data_generator", parameter)

# 指定特定的模型
with model:
    data_plus_one = data_generator + 1

# 一旦定義了相同的變數，我們就可以在模型上下文之外檢查它們
model.initial_values

# 定義另一個模型，其中部份變數名稱相同
with pm.Model() as model_exp:
    theta = pm.Exponential("theta", 2.0)
    data_generator = pm.Poisson("data_generator", theta)

# 再定義另一個模型
with pm.Model() as ab_testing:
    p_A = pm.Uniform("P(A)", 0, 1)
    p_B = pm.Uniform("P(B)", 0, 1)
```

## PyMC變數

所有 PyMC 變數都有一個初始值，如果您沒有區分引數 initval ，PyMC 之後會自動為您初始化它。

initval 引數僅用於模型，如果沒有指定其他起點，則作為取樣的起點。它不會因抽樣結果而改變。

```python
#leave it to automatically init
with pm.Model() as model:
    parameter = pm.Exponential("poisson_param", 1.0)
    data_generator = pm.Poisson("data_generator", parameter)

for k,v in model.initial_values.items():
    print(f"{k} initval is {v}")
# poisson_param initval is None
# data_generator initval is None

#leave it to automatically init
with pm.Model() as model:
    parameter = pm.Exponential("poisson_param", 1.0,initval=rng.exponential(1))
    data_generator = pm.Poisson("data_generator", parameter,initval=rng.poisson(10))
    
for k,v in model.initial_values.items():
    print(f"{k} initval is {v}")

# poisson_param initval is 2.2597012384790296
# data_generator initval is 10

#You can use initial_values to see all parameters above
model.initial_values
```

如果您使用的是更不穩定的先驗，可能需要更好的起點，這可能會很有幫助。

PyMC 涉及兩種型別的程式變數：隨機變數和確定性變數。

* 隨機變數是不確定的變數，即即使您知道變數引數和元件的所有值，它仍然是隨機的。此類別包含類別 Poisson 、 DiscreteUniform 和 Exponential 的例項。
* 確定性變數是在變數的引數和份量已知的情況下不是隨機的變數。一開始這可能會令人困惑：簡單的說，如果已知道變數 foo 的所有組成變數，我就可以確定 foo 的值是什麼。

## 參考資料

* Cameron Davidson-Pilon, "貝葉斯方法-機率程式設計與貝葉斯推斷, " Ch1.4, 人民郵電出版社, 2016.
* [https://dataorigami.net/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/](https://dataorigami.net/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
* [https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
