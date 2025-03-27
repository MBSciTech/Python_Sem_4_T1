import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[4,5],[7,8]],
                 index=['cobra','viper','sidewind'],
                 columns=['max_speed','shield']
                 )

df.loc['cobra':'viper','shield']