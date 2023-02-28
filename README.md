# statsmodels_HC_cov
Матрицы форм HC4, HC4m и HC5, точно такие же, как и в R здесь: https://www.rdocumentation.org/packages/sandwich/versions/3.0-2/topics/vcovHC
Просто код получения матрицы можно посмотреть здесь: https://github.com/dogfew/statsmodels_HC_cov/blob/main/statsmodels_HC_cov/cov.py
Тесты писать мне лень. 

#### Установка
```
git clone https://github.com/dogfew/statsmodels_HC_cov
cd statsmodels_HC_cov
python main.py 
```
Enter.
#### Удаление
```
pip uninstall statsmodels-hc-cov
```
## Подготовка к использованию библиотеки

Сначала необходимо подготовить модель типа OLS из statsmodels.api, и зафитить её.

#### Подготовка данных
```
>>> from sklearn.datasets import make_regression
>>> X, y = make_regression(n_features=4, random_state=0)
```
#### Подготовка модели
```
>>> from statsmodels.api import OLS
>>> model = OLS(y, X).fit()
```

## Использование этой библиотеки
#### Импорт потенциально необходимых вещей
```
>>> from statsmodels_HC_cov import cov_hc5, cov_hc4, cov_hc4m, vcov_hc, ttest
```
#### Получить ковариационную матрицу соответствующей функцией
```
>>> cov_hc5(model)

array([[3.88365819e-28, 9.65903402e-29, 2.11230727e-29, 5.88261484e-29],
       [9.65903402e-29, 8.21278565e-28, 5.41909916e-29, 2.47126572e-28],
       [2.11230727e-29, 5.41909916e-29, 8.18050152e-28, 1.97982505e-28],
       [5.88261484e-29, 2.47126572e-28, 1.97982505e-28, 7.42373307e-28]])
```
#### Получить такую же ковариационную матрицу иначе
```
>>> vcov_hc(model, cov_type='hc5')

array([[3.88365819e-28, 9.65903402e-29, 2.11230727e-29, 5.88261484e-29],
       [9.65903402e-29, 8.21278565e-28, 5.41909916e-29, 2.47126572e-28],
       [2.11230727e-29, 5.41909916e-29, 8.18050152e-28, 1.97982505e-28],
       [5.88261484e-29, 2.47126572e-28, 1.97982505e-28, 7.42373307e-28]])
```

### Сделать тесты так сказать
```
>>> test(model, cov_type='hc5')

      coefs  std err             t  P >|t|
X0  20.4924      0.0  1.039852e+15     0.0
X1  34.1698      0.0  1.192332e+15     0.0
X2  67.6242      0.0  2.364354e+15     0.0
X3  87.9235      0.0  3.226961e+15     0.0
```
# Зачем?

У меня сгорело, что я нигде в питоне это не нашёл. Впрочем, это никому и не нужно, кроме студентов.
