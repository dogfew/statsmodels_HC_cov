from sklearn.datasets import make_regression
from statsmodels.api import OLS, add_constant
from statsmodels_HC_cov import *

X, y = make_regression(n_features=4, random_state=0)
model = OLS(y, add_constant(X)).fit()
cov_hc5(model)
vcov_hc(model, cov_type='hc5')
test = ttest(model, cov_type='hc5')


if __name__ == '__main__':
    print(test['X0']['t'])