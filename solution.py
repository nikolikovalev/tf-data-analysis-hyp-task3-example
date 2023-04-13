import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 411809593 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    a = 0.04
    res = ztest(x, value=300, alternative='smaller')[1]
    return res < a
