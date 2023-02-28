import numpy as np
import pandas as pd

from scipy.stats import t
from statsmodels.regression.linear_model import RegressionResultsWrapper
from .cov import vcov_hc

class ttest:
    def __init__(self, results: RegressionResultsWrapper,
                 cov_type: str = 'hc0',
                 cov_matrix: np.ndarray = None):
        """
        :param results:
        :param cov_type:
        :param cov_matrix:
        """
        if cov_matrix is None:
            cov_matrix = vcov_hc(results, cov_type)
        se_matrix = np.diag(cov_matrix) ** 0.5
        tvalues = results.params / se_matrix
        pvalues = t.sf(np.abs(tvalues), df=results.nobs) * 2
        self.se = se_matrix
        self.tvalues = np.array(tvalues)
        self.pvalues = np.array(pvalues)
        self.coefs = np.array(results.params)
        self.cov_type = cov_type
        try:
            self.index = results.bse.index
        except Exception:
            self.index = [f"X{i}" for i in range(len(tvalues))]

    @property
    def t_values(self):
        return self.tvalues

    @property
    def p_values(self):
        return self.pvalues

    def __repr__(self):
        df = pd.DataFrame({'coefs': self.coefs,
                           'std err': self.se,
                           't': self.tvalues,
                           'P >|t|': self.pvalues}, index=self.index)
        return str(df.round(4))