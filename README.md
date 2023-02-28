# statsmodels_HC_cov
Матрицы форм HC4, HC4m и HC5, точно такие же, как и в R здесь: https://www.rdocumentation.org/packages/sandwich/versions/3.0-2/topics/vcovHC

#### Установка
```
https://github.com/dogfew/statsmodels_HC_cov
cd statsmodels_HC_cov
python main.py 
```
#### Удаление
```
pip uninstall statsmodels-hc-cov
```
## Подготовка к использованию библиотеки

Сначала необходимо подготовить модель типа OLS из statsmodels.api, и зафитить её.

#### Подготовка данных
```
>>> from sklearn.datasets import make_regression
>>> X, y = make_regression(n_features=4)
```
#### Подготовка модели
```
>>> from statsmodels.api import OLS
>>> model = OLS(y, X).fit()
```

## Использование этой библиотеки
#### Импорт потенциально необходимых вещей
```
>>> from statsmodels_HC_cov.cov import cov_hc5, cov_hc4, cov_hc4m, vcov_hc, ttest
```
#### Получить ковариационную матрицу соответствующей функцией
```
>>> cov_hc5(model)

array([[ 1.05090039e-28,  4.55713314e-29, -2.07878713e-29,
         1.65585695e-29],
       [ 4.55713314e-29,  2.92356870e-28,  5.59240056e-31,
        -1.48798976e-29],
       [-2.07878713e-29,  5.59240056e-31,  8.88568078e-29,
         1.20951337e-30],
       [ 1.65585695e-29, -1.48798976e-29,  1.20951337e-30,
         1.22059254e-28]])
```
#### Получить такую же ковариационную матрицу иначе
```
>>> vcov_hc(model, cov_type='hc5')

array([[ 1.05090039e-28,  4.55713314e-29, -2.07878713e-29,
         1.65585695e-29],
       [ 4.55713314e-29,  2.92356870e-28,  5.59240056e-31,
        -1.48798976e-29],
       [-2.07878713e-29,  5.59240056e-31,  8.88568078e-29,
         1.20951337e-30],
       [ 1.65585695e-29, -1.48798976e-29,  1.20951337e-30,
         1.22059254e-28]])
```

# Зачем?

У меня сгорело, что я нигде в питоне это не нашёл. Впрочем, это никому и не нужно, кроме студентов.
