import numpy as np
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.stats.sandwich_covariance import cov_hac, cov_hc0, cov_hc1, cov_hc2, cov_hc3


def cov_hc5(results: RegressionResultsWrapper, k=0.7) -> np.ndarray:
    """
    :param results: fitted OLS model from statsmodels
    :param k: 0.7
    :return: HC5 covariance matrix

    Cribari-Neto, Souza, & Vasconcellos (2007)
    """
    X: np.ndarray = np.array(results.model.exog)
    diaghat: np.ndarray = np.diag(X @ np.linalg.pinv(X.T @ X) @ X.T)
    n: int = len(results.resid)
    p: int = np.round(diaghat.sum())
    delta: np.ndarray = np.minimum(n * diaghat / p, np.maximum(4, n * k * np.max(diaghat) / p))
    het_scale: np.ndarray = results.resid ** 2 / np.sqrt((1 - diaghat) ** delta)
    cov_hc5_: np.ndarray = _HCCM(results, het_scale)
    return cov_hc5_


def cov_hc4m(results: RegressionResultsWrapper, gamma_1=1, gamma_2=1.5) -> np.ndarray:
    """
    :param results: fitted OLS model from statsmodels
    :param gamma_1: 1
    :param gamma_2: 1.5
    :return: HC4m covariance matrix

    Cribari-Neto & Da Silva (2011)
    """
    X: np.ndarray = np.array(results.model.exog)
    diaghat: np.ndarray = np.diag(X @ np.linalg.pinv(X.T @ X) @ X.T)
    n: int = len(results.resid)
    p: int = diaghat.sum().round()
    delta: np.ndarray = np.minimum(gamma_1, n * diaghat / p) + np.minimum(gamma_2, n * diaghat / p)
    het_scale: np.ndarray = results.resid ** 2 / (1 - diaghat) ** delta
    cov_hc4m_: np.ndarray = _HCCM(results, het_scale)
    return cov_hc4m_


def cov_hc4(results: RegressionResultsWrapper) -> np.ndarray:
    """
    :param results: fitted OLS model object from statsmodels
    :return: HC4m covariance matrix

    Cribari-Neto & Da Silva (2011)
    """
    X: np.ndarray = np.array(results.model.exog)
    diaghat: np.ndarray = np.diag(X @ np.linalg.pinv(X.T @ X) @ X.T)
    n: int = len(results.resid)
    p: int = diaghat.sum().round()
    delta: np.ndarray = np.minimum(4, n * diaghat / p)
    het_scale: np.ndarray = results.resid ** 2 / (1 - diaghat) ** delta
    cov_hc4_: np.ndarray = _HCCM(results, het_scale)
    return cov_hc4_


def _HCCM(results, scale):
    """
    sandwich with pinv(x) * diag(scale) * pinv(x).T

    where pinv(x) = (X'X)^(-1) X
    and scale is (nobs,)
    """
    H = np.dot(results.model.pinv_wexog,
               np.array(scale)[:, None] * results.model.pinv_wexog.T)
    return H


def vcov_hc(results: RegressionResultsWrapper,
            cov_type: str = "hc0"):
    """
    :param results: fitted OLS model object from statsmodels
    :param cov_type: hac, hc0, hc1, hc2, hc3, hc4, hc5, hc4m]
    :return:
    """
    types = ["hac", "hc0", "hc1", "hc2", "hc3", "hc4", "hc5", "hc4m"]
    cov_type = cov_type.lower().replace("_", "").replace('cov', "")
    match cov_type:
        case "hac":
            return cov_hac(results)
        case "hc0":
            return cov_hc0(results)
        case "hc1":
            return cov_hc1(results)
        case "hc2":
            return cov_hc2(results)
        case "hc3":
            return cov_hc3(results)
        case "hc4":
            return cov_hc4(results)
        case "hc5":
            return cov_hc5(results)
        case "hc4m":
            return cov_hc4m(results)
        case _:
            raise BaseException f"There is no such type like {cov_type}. Please, try one of these: {', '.join(types)}"

