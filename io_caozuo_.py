import numpy as np
import pandas as pd
from pandas import DataFrame,Series
# import webbrowser
# link = 'https://pandas.org/pandas-docs/version/0.20/io.html'
# webbrowser.open(link)
reader = pd.read_clipboard()
print(reader)
to = reader.to_clipboard()
print(to)
reader.to_csv('reader.csv')
df2 = pd.read_csv('reader.csv')
print(df2)
js = reader.to_json()
print(js)
js1 = pd.read_json(js)


df3 = reader.to_html('reader.html')

df4 = reader.to_excel('reader.excel')

