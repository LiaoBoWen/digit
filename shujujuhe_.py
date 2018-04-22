import numpy as np
import pandas as pd
from pandas import DataFrame,Series

df =pd.read_csv("…….csv")
g = df.groupby(["city","wind"])
print(g.groups)
bj = g.get_group(["BJ",4])
