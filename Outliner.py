import pandas as pd
import numpy as np
def outlier(datacolumn) :
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn,[25,75])
    IQR = Q3 - Q1
    lr = Q1 - 1.5*IQR
    ur = Q3 + 1.5*IQR
    return lr,ur