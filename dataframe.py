import pandas as pd

# DataFrame = A Tabulation data structire with rows and column.

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)