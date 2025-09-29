import pandas as pd

calories = {'day1': 420, 'day2': 380, 'day3': 390}

series = pd.Series(calories)

print(series)

series.loc["day3"] += 300

print(series)
print(series.loc['day3'])

print(series[series>400])