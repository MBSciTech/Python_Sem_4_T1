import pandas as pd
import numpy as np

#PB29
data = {
"A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
"B": [50, 40, 40, 30, 50],
"C": [True, False, False, False, True]
}
data = pd.DataFrame(data)
data = data.drop_duplicates()
print(data.reset_index())
