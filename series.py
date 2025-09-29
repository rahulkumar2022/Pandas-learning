import pandas as pd

data = [100.5,200,300,400,500]

series = pd.Series(data)

print(series)

data = ['a','b','c','d','e']

series = pd.Series(data)
print(series)

data = [True, False, True, False]
series = pd.Series(data, index=['a','b','c','d'])
print(series)
print(series['a'])
print(series.loc['a'])
print(series.iloc[1])

series['a'] = False
print(series)

data = [100, 200, 300, 400, 500]
series = pd.Series(data, index=['a','b','c','d','e'])
print(series)
print(series[series>=300])