import pandas as pd

data = pd.read_csv("student.csv")

series = pd.Series(data["Marks"])

print("Pandas Series:")
print(series)
